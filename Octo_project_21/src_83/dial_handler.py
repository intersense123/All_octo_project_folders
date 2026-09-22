from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import (
    QGraphicsScene,
    QGraphicsView,
    QGraphicsPixmapItem
)
from PySide2.QtSvg import QGraphicsSvgItem
from PySide2.QtGui import QPainter
from PySide2.QtCore import QObject, Signal, Property, QTimer,Qt
from PySide2.QtGui import QBrush, QColor

class DialHandler(QObject):
    needle_angle_changed = Signal(float)

    def __init__(self, main_window, needle_pos_x, needle_pos_y,
                 pivot_point_x, pivot_point_y,
                 dial_label, needle_label, dial, needle,
                 probe="D1", channel_count=1, parent=None):
        super().__init__(parent)
        self.mw = main_window
        self.ui = main_window

        self.needle_pos_x = needle_pos_x
        self.needle_pos_y = needle_pos_y
        self.pivot_point_x = pivot_point_x
        self.pivot_point_y = pivot_point_y

        self.scene = QGraphicsScene()

        # ✅ FIX 1: use dial_label.parent(), NOT hardcoded label_dial1.parent()
        self.view = QGraphicsView(self.scene, dial_label.parent())

        self.view.setRenderHints(
            QPainter.Antialiasing |
            QPainter.SmoothPixmapTransform |
            QPainter.HighQualityAntialiasing
        )
        self.view.setGeometry(dial_label.geometry())
        self.view.setStyleSheet("background: transparent; border: none;")

        # ✅ FIX 2: force full viewport repaint to eliminate ghost/trail artifacts
        self.view.setViewportUpdateMode(QGraphicsView.FullViewportUpdate)

        # ✅ FIX 3: transparent background on both view and scene
        self.view.setBackgroundBrush(QBrush(Qt.transparent))
        self.scene.setBackgroundBrush(QBrush(Qt.transparent))

        dial_label.hide()
        needle_label.hide()

        self.current_color = "yellow"
        size_map = {
            1: {"D1": "380"},
            2: {"D1": "380", "D2": "380"},
            3: {"D1": "260", "D2": "260", "D3": "260"},
            4: {"D1": "260", "D2": "260", "D3": "260", "D4": "260"},
        }
        size = size_map.get(channel_count, {}).get(probe, "260")

        self.dial_pixmaps = {
            "green":  QPixmap(f"/home/torizon/app/src/images/dial-img-green-{size}.png"),
            "yellow": QPixmap(f"/home/torizon/app/src/images/dial-img-yellow-{size}.png"),
            "red":    QPixmap(f"/home/torizon/app/src/images/dial-img-red-{size}.png"),
        }

        self.dial_item = QGraphicsPixmapItem(QPixmap(dial))
        self.scene.addItem(self.dial_item)

        self.needle_item = QGraphicsSvgItem(needle)
        self.scene.addItem(self.needle_item)

        # ✅ FIX 4: lock scene rect to dial image — stops viewport from drifting/expanding
        dial_pixmap = self.dial_item.pixmap()
        self.scene.setSceneRect(0, 0, dial_pixmap.width(), dial_pixmap.height())

        # needle_pos_x/y are already scene-local (0,0 = top-left of dial image)
        self.needle_item.setPos(self.needle_pos_x, self.needle_pos_y)
        self.needle_item.setTransformOriginPoint(self.pivot_point_x, self.pivot_point_y)
        self.current_angle = 0
        self.needle_item.setRotation(0)

        self.spring_stiffness = 2
        self.spring_damping = 0.20
        self.velocity = 0
        self.target_angle = 0
        self.is_animating = False

        self.animation_timer = QTimer()
        self.animation_timer.timeout.connect(self._update_needle_spring)
        self.needle_angle_changed.connect(self._on_needle_angle_changed)
        # print("SVG bounds =", self.needle_item.boundingRect())

        # ✅ FIX 5: show the view (it was never explicitly shown)
        self.view.show()
    # ==================== UPDATE METHODS ====================
    def set_dial_color(self, color):
        try:
            if color not in self.dial_pixmaps:
                print(f"Unknown dial color: {color}")
                return

            if self.current_color == color:
                return

            self.current_color = color
            self.dial_item.setPixmap(self.dial_pixmaps[color])
        except Exception as e:
            print(f"Error setting dial color: {e}")
        

    
    # ==================== END UPDATE METHODS ====================

    # ==================== MOVE NEEDLE ====================
    
    def _on_needle_angle_changed(self, angle):
        try:
            """Slot to receive angle from signal (called in main thread) - starts spring animation"""
            self.target_angle = angle
            # self.velocity = 0  # Reset velocity for new animation
            self.is_animating = True
            
            # Start animation timer if not already running
            if not self.animation_timer.isActive():
                self.animation_timer.start(8)  # ~60 FPS for smooth animation
        except Exception as e:
            print(f"Error in needle angle change: {e}")
            self.is_animating = False
            self.animation_timer.stop()
    
    def _update_needle_spring(self):
        try:
            """Update needle position using spring physics (called by timer)"""
            if not self.is_animating:
                return
            
            acceleration = (self.target_angle - self.current_angle) * self.spring_stiffness
            self.velocity = (self.velocity + acceleration) * self.spring_damping
            self.current_angle = self.current_angle + self.velocity
            
            # Apply rotation
            self.needle_item.setRotation(self.current_angle)
            
            # Check if animation is complete (velocity and distance are negligible)
            distance_to_target = abs(self.target_angle - self.current_angle)
            
            if distance_to_target < 0.1 and abs(self.velocity) < 0.1:
                # Snap to target and stop animation
                self.current_angle = self.target_angle
                self.needle_item.setRotation(self.current_angle)
                self.is_animating = False
                self.animation_timer.stop()
        except Exception as e:
            print(f"Error in spring animation: {e}")
            self.is_animating = False
            self.animation_timer.stop()
            
    def move_needle(self, angle):
        """Move needle to specified angle - can be called from any thread"""
        # Emit signal to update GUI (thread-safe)
        self.needle_angle_changed.emit(angle)
    
    # ==================== END MOVE NEEDLE ====================

    # Property (keeping QObject inheritance as requested)
    @Property(float)
    def angle(self):
        return self.current_angle
    
    @angle.setter
    def angle(self, value):
        self.current_angle = value
        self.needle_item.setRotation(value)





