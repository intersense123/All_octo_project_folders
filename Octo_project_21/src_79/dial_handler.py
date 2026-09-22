from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import (
    QGraphicsScene,
    QGraphicsView,
    QGraphicsPixmapItem
)
from PySide2.QtSvg import QGraphicsSvgItem
from PySide2.QtGui import QPainter
from PySide2.QtCore import QObject, Signal, Property, QTimer

class DialHandler(QObject):
    # Signal to update needle from any thread
    needle_angle_changed = Signal(float)
    
    def __init__(self, main_window, needle_pos_x, needle_pos_y, pivot_point_x, pivot_point_y, parent=None):
        super().__init__(parent)
        self.mw= main_window
        self.ui = main_window  # For compatibility
        
        self.needle_pos_x = needle_pos_x
        self.needle_pos_y = needle_pos_y
        
        self.pivot_point_x = pivot_point_x
        self.pivot_point_y = pivot_point_y
        
        self.scene = QGraphicsScene()

        # Replace label_dial1 with graphics view
        self.view = QGraphicsView(self.scene, self.ui.label_dial1.parent())
        self.view.setRenderHints(
            QPainter.Antialiasing |
            QPainter.SmoothPixmapTransform |
            QPainter.HighQualityAntialiasing
        )
        self.view.setGeometry(self.ui.label_dial1.geometry())
        self.view.setStyleSheet("background: transparent; border: none;")
        
        # Hide original labels
        self.ui.label_dial1.hide()
        self.ui.label_needle1.hide()

        # Add Dial
        self.dial_item = QGraphicsPixmapItem(
            QPixmap("/home/torizon/app/src/images/dial-img-yellow-380_new.png")
        )
        self.scene.addItem(self.dial_item)

        # Add Needle
        # self.needle_item = QGraphicsPixmapItem(
        #     QPixmap("/home/torizon/app/src/images/needle_big.png")
        # )
        self.needle_item = QGraphicsSvgItem(
            "/home/torizon/app/src/images/Needle-circle-white-svg.svg"
        )

        self.scene.addItem(self.needle_item)
        
        # Center needle on dial
        self.needle_item.setPos(self.needle_pos_x, self.needle_pos_y)

        # IMPORTANT → Set rotation pivot
        self.needle_item.setTransformOriginPoint(
            self.pivot_point_x, self.pivot_point_y
        )
        
        # Current angle
        self.current_angle = 0
        self.needle_item.setRotation(0)
        
        # Spring animation parameters
        self.spring_stiffness = 0.1#0.8 #0.15  # Spring constant (higher = faster)
        self.spring_damping = 0.60#0.83 #0.75    # Damping quotient (0-1, lower = more oscillation)
        self.velocity = 0            # Current velocity for spring physics
        self.target_angle = 0         # Target angle for animation
        self.is_animating = False     # Animation state
        
        # Animation timer
        self.animation_timer = QTimer()
        self.animation_timer.timeout.connect(self._update_needle_spring)
        
        # Connect signal to GUI update (thread-safe)
        self.needle_angle_changed.connect(self._on_needle_angle_changed)

    # ==================== UPDATE METHODS ====================
    
    def update_dial(self, image_path):
        """Update the dial image"""
        self.dial_item.setPixmap(QPixmap(image_path))
    
    def update_needle(self, image_path):
        """Update the needle image"""
        self.needle_item.setPixmap(QPixmap(image_path))
    
    # ==================== END UPDATE METHODS ====================

    # ==================== MOVE NEEDLE ====================
    
    def _on_needle_angle_changed(self, angle):
        """Slot to receive angle from signal (called in main thread) - starts spring animation"""
        self.target_angle = angle
        # self.velocity = 0  # Reset velocity for new animation
        self.is_animating = True
        
        # Start animation timer if not already running
        if not self.animation_timer.isActive():
            self.animation_timer.start(8)  # ~60 FPS for smooth animation
    
    def _update_needle_spring(self):
        """Update needle position using spring physics (called by timer)"""
        if not self.is_animating:
            return
        
        # Spring physics calculation
        # acceleration = (target - current) * stiffness
        # velocity = (velocity + acceleration) * damping
        # current = current + velocity
        
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

# class DialHandler(QObject):

#     def __init__(
#         self,
#         main_window,
#         needle_pos_x,
#         needle_pos_y,
#         pivot_point_x,
#         pivot_point_y,
#         dial,
#         needle,
#         parent=None
#     ):
#         super().__init__(parent)

#         self.ui = main_window

#         self.scene = QGraphicsScene()

#         self.view = QGraphicsView(
#             self.scene,
#             dial.parent()
#         )
#         self.view.setRenderHints(
#             QPainter.Antialiasing |
#             QPainter.SmoothPixmapTransform |
#             QPainter.HighQualityAntialiasing
#         )
#         self.view.setGeometry(dial.geometry())
#         self.view.setStyleSheet(
#             "background: transparent; border: none;"
#         )

#         dial.hide()
#         needle.hide()

#         # --------------------------------------------------
#         # Dial
#         # --------------------------------------------------
#         self.dial_item = QGraphicsPixmapItem(
#             QPixmap("/home/torizon/app/src/images/dial-img-yellow-380_new.png")
#         )
#         self.scene.addItem(self.dial_item)

#         # --------------------------------------------------
#         # Needle
#         # --------------------------------------------------
#         self.needle_item = QGraphicsSvgItem(
#             "/home/torizon/app/src/images/Needle-circle-white-svg.svg"
#         )

#         self.scene.addItem(self.needle_item)

#         self.needle_item.setPos(
#             needle_pos_x,
#             needle_pos_y
#         )

#         self.needle_item.setTransformOriginPoint(
#             pivot_point_x,
#             pivot_point_y
#         )

#         # --------------------------------------------------
#         # Animation variables
#         # --------------------------------------------------
#         self.current_angle = 0.0
#         self.target_angle = 0.0

#         # 0.05 = slow
#         # 0.08 = smooth
#         # 0.12 = fast
#        # Spring parameters
#         self.spring_stiffness = 0.01
#         self.spring_damping = 0.81

#         self.velocity = 0.0

#         # --------------------------------------------------
#         # Animation timer
#         # --------------------------------------------------
#         self.animation_timer = QTimer()
#         self.animation_timer.timeout.connect(
#             self._update_needle
#         )

#         # --------------------------------------------------
#         # Demo sweep
#         # --------------------------------------------------
#         self.demo_timer = QTimer()
#         self.demo_timer.timeout.connect(
#             self._continuous_rotation
#         )

#         self.sweep_direction = 1

#     # ==================================================
#     # Public Functions
#     # ==================================================

#     def update_dial(self, image_path):
#         self.dial_item.setPixmap(
#             QPixmap(image_path)
#         )

#     def update_needle(self, image_path):
#         self.needle_item.setPixmap(
#             QPixmap(image_path)
#         )

#     def move_needle(self, angle):
#         """
#         Direct angle control
#         Range: -90 to +90
#         """

#         angle = max(-90, min(90, angle))

#         self.target_angle = angle

#         if not self.animation_timer.isActive():
#             self.animation_timer.start(16)

#     def set_value(self, value):
#         """
#         Process value
#         Range: -60 to +60
#         """

#         value = max(-60, min(60, value))

#         dial_angle = value * 1.5

#         self.move_needle(dial_angle)

#     # ==================================================
#     # Internal Animation
#     # ==================================================

#     def _update_needle(self):

#         # Spring force
#         error = self.target_angle - self.current_angle

#         acceleration = error * self.spring_stiffness

#         # Apply damping
#         self.velocity = (
#             self.velocity + acceleration
#         ) * self.spring_damping

#         # Move needle
#         self.current_angle += self.velocity

#         self.needle_item.setRotation(
#             self.current_angle
#         )

#         # Stop when settled
#         if (
#             abs(error) < 0.1
#             and abs(self.velocity) < 0.1
#         ):

#             self.current_angle = self.target_angle

#             self.needle_item.setRotation(
#                 self.current_angle
#             )

#             self.velocity = 0.0

#             self.animation_timer.stop()

#     # ==================================================
#     # Demo Sweep
#     # ==================================================

#     def start_demo(self, interval_ms=2000):

#         if not self.demo_timer.isActive():
#             self.demo_timer.start(interval_ms)

#     def stop_demo(self):

#         self.demo_timer.stop()

#     def _continuous_rotation(self):

#         if self.animation_timer.isActive():
#             return

#         if self.sweep_direction > 0:

#             self.move_needle(90)

#             self.sweep_direction = -1

#         else:

#             self.move_needle(-90)

#             self.sweep_direction = 1

# import random
# import threading








# import random
# import threading

# from PySide2.QtCore import QObject, Signal, Property, QTimer
# from PySide2.QtGui import QPixmap
# from PySide2.QtWidgets import QGraphicsScene, QGraphicsView, QGraphicsPixmapItem

# class DialHandler(QObject):
#     # Signal to update needle from any thread
#     needle_angle_changed = Signal(float)
    
#     def __init__(self, main_window, needle_pos_x, needle_pos_y, pivot_point_x, pivot_point_y,dial,needle, parent=None):
#         super().__init__(parent)
#         # self.mw= main_window
#         self.ui = main_window  # For compatibility
        
#         self.needle_pos_x = needle_pos_x
#         self.needle_pos_y = needle_pos_y
        
#         self.pivot_point_x = pivot_point_x
#         self.pivot_point_y = pivot_point_y

#         self.dial = dial
#         self.needle = needle
        
#         self.scene = QGraphicsScene()

#         # Replace label_dial1 with graphics view
#         self.view = QGraphicsView(self.scene, self.dial.parent())
#         self.view.setGeometry(self.dial.geometry())
#         self.view.setStyleSheet("background: transparent; border: none;")
        
#         # Hide original labels
#         self.dial.hide()
#         self.needle.hide()

#         # Add Dial
#         self.dial_item = QGraphicsPixmapItem(
#             QPixmap("/home/torizon/app/src/images/dial-img-yellow-380_new.png")
#         )
#         self.scene.addItem(self.dial_item)

#         # Add Needle
#         self.needle_item = QGraphicsPixmapItem(
#             QPixmap("/home/torizon/app/src/images/Needle-circle-white-svg.svg")
#         )
#         self.scene.addItem(self.needle_item)
#         print(self.needle_item.pixmap().width())
#         print(self.needle_item.pixmap().height())
#         # Center needle on dial
#         self.needle_item.setPos(self.needle_pos_x, self.needle_pos_y)

#         # IMPORTANT → Set rotation pivot
#         self.needle_item.setTransformOriginPoint(
#             self.pivot_point_x, self.pivot_point_y
#         )
        
#         # Current angle
#         self.current_angle = 0
#         self.needle_item.setRotation(0)
        
#         # Spring animation parameters
#         # self.spring_stiffness = 0.4 #0.15  # Spring constant (higher = faster)
#         # self.spring_damping = 0.5 #0.75    # Damping quotient (0-1, lower = more oscillation)
#         self.spring_stiffness = 0.02 #0.12
#         self.spring_damping = 0.84 #0.92

#         # self.demo_timer.start(1000)
#         self.velocity = 0            # Current velocity for spring physics
#         self.target_angle = 0         # Target angle for animation
#         self.is_animating = False     # Animation state
#         self.sweep_angle = -60
#         self.sweep_direction = 1

#         self.demo_timer = QTimer()
#         self.demo_timer.timeout.connect(self._continuous_rotation)
#         # Animation timer
#         self.animation_timer = QTimer()
#         self.animation_timer.timeout.connect(self._update_needle_spring)
        
#         # Connect signal to GUI update (thread-safe)
#         self.needle_angle_changed.connect(self._on_needle_angle_changed)

#     # ==================== UPDATE METHODS ====================
#     # def _continuous_rotation(self):

#     #     self.sweep_angle += self.sweep_direction * 2

#     #     if self.sweep_angle >= 90:
#     #         self.sweep_direction = -1

#     #     elif self.sweep_angle <= -90:
#     #         self.sweep_direction = 1

#     #     self.move_needle(self.sweep_angle)
#     def _continuous_rotation(self):

#         if self.is_animating:
#             return

#         if self.sweep_direction > 0:
#             self.move_needle(90)
#             self.sweep_direction = -1
#         else:
#             self.move_needle(-90)
#             self.sweep_direction = 1
        
#     def update_dial(self, image_path):
#         """Update the dial image"""
#         self.dial_item.setPixmap(QPixmap(image_path))
    
#     def update_needle(self, image_path):
#         """Update the needle image"""
#         self.needle_item.setPixmap(QPixmap(image_path))
    
#     # ==================== END UPDATE METHODS ====================

#     # ==================== MOVE NEEDLE ====================
    
#     def _on_needle_angle_changed(self, angle):
#         """Slot to receive angle from signal (called in main thread) - starts spring animation"""
#         self.target_angle = angle
#         self.velocity = 0  # Reset velocity for new animation
#         self.is_animating = True
        
#         # Start animation timer if not already running
#         if not self.animation_timer.isActive():
#             self.animation_timer.start(16)  # ~60 FPS for smooth animation

#     def _update_needle_spring(self):
#         """Update needle position using spring physics (called by timer)"""
#         print("Target:", self.target_angle,
#             "Current:", round(self.current_angle, 2))
#         if not self.is_animating:
#             return
        
        
#         acceleration = (self.target_angle - self.current_angle) * self.spring_stiffness
#         self.velocity = (self.velocity + acceleration) * self.spring_damping
#         self.velocity = max(min(self.velocity, 4), -4)
#         self.current_angle = self.current_angle + self.velocity
        
#         # Apply rotation
#         self.needle_item.setRotation(self.current_angle)

#         distance_to_target = abs(self.target_angle - self.current_angle)
        
#         if distance_to_target < 0.1 and abs(self.velocity) < 0.1:
#             # Snap to target and stop animation
#             self.current_angle = self.target_angle
#             self.needle_item.setRotation(self.current_angle)
#             self.is_animating = False
#             self.animation_timer.stop()

#     def move_needle(self, angle):
#         """Move needle to specified angle - can be called from any thread"""
#         # Emit signal to update GUI (thread-safe)
#         self.needle_angle_changed.emit(angle)
    
#     # ==================== END MOVE NEEDLE ====================

#     # Property (keeping QObject inheritance as requested)
#     @Property(float)
#     def angle(self):
#         return self.current_angle
    
#     @angle.setter
#     def angle(self, value):
#         self.current_angle = value
#         self.needle_item.setRotation(value)



# import random
# import threading

# from PySide2.QtCore import QObject, Signal, Property, QTimer
# from PySide2.QtGui import QPixmap
# from PySide2.QtWidgets import QGraphicsScene, QGraphicsView, QGraphicsPixmapItem
# from PySide2.QtSvg import QGraphicsSvgItem
# from PySide2.QtSvg import QGraphicsSvgItem

# class DialHandler(QObject):
#     # Signal to update needle from any thread
#     needle_angle_changed = Signal(float)
    
#     def __init__(self, main_window, needle_pos_x, needle_pos_y, pivot_point_x, pivot_point_y,dial,needle, parent=None):
#         super().__init__(parent)
#         self.mw= main_window
#         self.ui = main_window  # For compatibility
        
#         self.needle_pos_x = needle_pos_x
#         self.needle_pos_y = needle_pos_y
        
#         self.pivot_point_x = pivot_point_x
#         self.pivot_point_y = pivot_point_y

#         self.dial = dial
#         self.needle = needle
        
#         self.scene = QGraphicsScene()

#         # Replace label_dial1 with graphics view
#         self.view = QGraphicsView(self.scene, self.dial.parent())
#         self.view.setGeometry(self.dial.geometry())
#         self.view.setStyleSheet("background: transparent; border: none;")
        
#         # Hide original labels
#         self.dial.hide()
#         self.needle.hide()

#         # Add Dial
#         self.dial_item = QGraphicsPixmapItem(
#             QPixmap("/home/torizon/app/src/images/dial-img-yellow-380.png")
#         )
#         self.scene.addItem(self.dial_item)

#         # Add Needle
#         # self.needle_item = QGraphicsPixmapItem(
#         #     QPixmap("/home/torizon/app/src/images/needle_big.png")
#         # )
#         # self.scene.addItem(self.needle_item)

#         self.needle_item = QGraphicsSvgItem(
#             "/home/torizon/app/src/images/Needle-white-svg.svg"
#         )
#         self.scene.addItem(self.needle_item)
#         # Center needle on dial
#         self.needle_item.setPos(self.needle_pos_x, self.needle_pos_y)

#         # IMPORTANT → Set rotation pivot
#         self.needle_item.setTransformOriginPoint(
#             self.pivot_point_x, self.pivot_point_y
#         )
        
#         # Current angle
#         self.current_angle = 0
#         self.needle_item.setRotation(0)
        
#         # Spring animation parameters
#         self.spring_stiffness = 0.4 #0.15  # Spring constant (higher = faster)
#         self.spring_damping = 0.5 #0.75    # Damping quotient (0-1, lower = more oscillation)
#         self.velocity = 0            # Current velocity for spring physics
#         self.target_angle = 0         # Target angle for animation
#         self.is_animating = False     # Animation state
        
#         # Animation timer
#         self.animation_timer = QTimer()
#         self.animation_timer.timeout.connect(self._update_needle_spring)
        
#         # Connect signal to GUI update (thread-safe)
#         self.needle_angle_changed.connect(self._on_needle_angle_changed)

#     # ==================== UPDATE METHODS ====================
    
#     def update_dial(self, image_path):
#         """Update the dial image"""
#         self.dial_item.setPixmap(QPixmap(image_path))

#     # def update_needle(self, image_path):
#     #     """Update the needle image"""
#     #     self.needle_item.setPixmap(QPixmap(image_path))
#     def update_needle(self, svg_path):
#         self.scene.removeItem(self.needle_item)

#         self.needle_item = QGraphicsSvgItem(svg_path)
#         self.scene.addItem(self.needle_item)

#         self.needle_item.setPos(
#             self.needle_pos_x,
#             self.needle_pos_y
#         )

#         self.needle_item.setTransformOriginPoint(
#             self.pivot_point_x,
#             self.pivot_point_y
#         )
#     # ==================== END UPDATE METHODS ====================

#     # ==================== MOVE NEEDLE ====================
    
#     def _on_needle_angle_changed(self, angle):
#         """Slot to receive angle from signal (called in main thread) - starts spring animation"""
#         self.target_angle = angle
#         self.velocity = 0  # Reset velocity for new animation
#         self.is_animating = True
        
#         # Start animation timer if not already running
#         if not self.animation_timer.isActive():
#             self.animation_timer.start(16)  # ~60 FPS for smooth animation

#     def _update_needle_spring(self):
#         """Update needle position using spring physics (called by timer)"""
#         if not self.is_animating:
#             return
        
#         # Spring physics calculation
#         # acceleration = (target - current) * stiffness
#         # velocity = (velocity + acceleration) * damping
#         # current = current + velocity
        
#         acceleration = (self.target_angle - self.current_angle) * self.spring_stiffness
#         self.velocity = (self.velocity + acceleration) * self.spring_damping
#         self.current_angle = self.current_angle + self.velocity
        
#         # Apply rotation
#         self.needle_item.setRotation(self.current_angle)
        
#         # Check if animation is complete (velocity and distance are negligible)
#         distance_to_target = abs(self.target_angle - self.current_angle)
        
#         if distance_to_target < 0.1 and abs(self.velocity) < 0.1:
#             # Snap to target and stop animation
#             self.current_angle = self.target_angle
#             self.needle_item.setRotation(self.current_angle)
#             self.is_animating = False
#             self.animation_timer.stop()

#     def move_needle(self, angle):
#         """Move needle to specified angle - can be called from any thread"""
#         # Emit signal to update GUI (thread-safe)
#         self.needle_angle_changed.emit(angle)
    
#     # ==================== END MOVE NEEDLE ====================

#     # Property (keeping QObject inheritance as requested)
#     @Property(float)
#     def angle(self):
#         return self.current_angle
    
#     @angle.setter
#     def angle(self, value):
#         self.current_angle = value
#         self.needle_item.setRotation(value)











# import random
# import threading

# from PySide2.QtCore import QObject, Signal, Property, QTimer
# from PySide2.QtGui import QPixmap
# from PySide2.QtWidgets import QGraphicsScene, QGraphicsView, QGraphicsPixmapItem

# class DialHandler(QObject):
#     # Signal to update needle from any thread
#     needle_angle_changed = Signal(float)
    
#     def __init__(self, main_window, needle_pos_x, needle_pos_y, pivot_point_x, pivot_point_y,dial,needle, parent=None):
#         super().__init__(parent)
#         self.mw= main_window
#         self.ui = main_window  # For compatibility
        
#         self.needle_pos_x = needle_pos_x
#         self.needle_pos_y = needle_pos_y
        
#         self.pivot_point_x = pivot_point_x
#         self.pivot_point_y = pivot_point_y

#         self.dial = dial
#         self.needle = needle
        
#         self.scene = QGraphicsScene()

#         # Replace label_dial1 with graphics view
#         self.view = QGraphicsView(self.scene, self.dial.parent())
#         self.view.setGeometry(self.dial.geometry())
#         self.view.setStyleSheet("background: transparent; border: none;")
        
#         # Hide original labels
#         self.dial.hide()
#         self.needle.hide()

#         # Add Dial
#         self.dial_item = QGraphicsPixmapItem(
#             QPixmap("/home/torizon/app/src/images/green_60_big.png")
#         )
#         self.scene.addItem(self.dial_item)

#         # Add Needle
#         self.needle_item = QGraphicsPixmapItem(
#             QPixmap("/home/torizon/app/src/images/needle_big.png")
#         )
#         self.scene.addItem(self.needle_item)
        
#         # Center needle on dial
#         self.needle_item.setPos(self.needle_pos_x, self.needle_pos_y)

#         # IMPORTANT → Set rotation pivot
#         self.needle_item.setTransformOriginPoint(
#             self.pivot_point_x, self.pivot_point_y
#         )
        
#         # Current angle
#         self.current_angle = 0
#         self.needle_item.setRotation(0)
        
#         # Spring animation parameters
#         self.spring_stiffness = 0.4 #0.15  # Spring constant (higher = faster)
#         self.spring_damping = 0.5 #0.75    # Damping quotient (0-1, lower = more oscillation)
#         self.velocity = 0            # Current velocity for spring physics
#         self.target_angle = 0         # Target angle for animation
#         self.is_animating = False     # Animation state
        
#         # Animation timer
#         self.animation_timer = QTimer()
#         self.animation_timer.timeout.connect(self._update_needle_spring)
        
#         # Connect signal to GUI update (thread-safe)
#         self.needle_angle_changed.connect(self._on_needle_angle_changed)

#     # ==================== UPDATE METHODS ====================
    
#     def update_dial(self, image_path):
#         """Update the dial image"""
#         self.dial_item.setPixmap(QPixmap(image_path))
    
#     def update_needle(self, image_path):
#         """Update the needle image"""
#         self.needle_item.setPixmap(QPixmap(image_path))
    
#     # ==================== END UPDATE METHODS ====================

#     # ==================== MOVE NEEDLE ====================
    
#     def _on_needle_angle_changed(self, angle):
#         """Slot to receive angle from signal (called in main thread) - starts spring animation"""
#         self.target_angle = angle
#         self.velocity = 0  # Reset velocity for new animation
#         self.is_animating = True
        
#         # Start animation timer if not already running
#         if not self.animation_timer.isActive():
#             self.animation_timer.start(16)  # ~60 FPS for smooth animation

#     def _update_needle_spring(self):
#         """Update needle position using spring physics (called by timer)"""
#         if not self.is_animating:
#             return
        
#         # Spring physics calculation
#         # acceleration = (target - current) * stiffness
#         # velocity = (velocity + acceleration) * damping
#         # current = current + velocity
        
#         acceleration = (self.target_angle - self.current_angle) * self.spring_stiffness
#         self.velocity = (self.velocity + acceleration) * self.spring_damping
#         self.current_angle = self.current_angle + self.velocity
        
#         # Apply rotation
#         self.needle_item.setRotation(self.current_angle)
        
#         # Check if animation is complete (velocity and distance are negligible)
#         distance_to_target = abs(self.target_angle - self.current_angle)
        
#         if distance_to_target < 0.1 and abs(self.velocity) < 0.1:
#             # Snap to target and stop animation
#             self.current_angle = self.target_angle
#             self.needle_item.setRotation(self.current_angle)
#             self.is_animating = False
#             self.animation_timer.stop()

#     def move_needle(self, angle):
#         """Move needle to specified angle - can be called from any thread"""
#         # Emit signal to update GUI (thread-safe)
#         self.needle_angle_changed.emit(angle)
    
#     # ==================== END MOVE NEEDLE ====================

#     # Property (keeping QObject inheritance as requested)
#     @Property(float)
#     def angle(self):
#         return self.current_angle
    
#     @angle.setter
#     def angle(self, value):
#         self.current_angle = value
#         self.needle_item.setRotation(value)

