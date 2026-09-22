import random
import threading

from PySide2.QtCore import QObject, Signal, Property
from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QGraphicsScene, QGraphicsView, QGraphicsPixmapItem

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
        self.view.setGeometry(self.ui.label_dial1.geometry())
        self.view.setStyleSheet("background: transparent; border: none;")
        
        # Hide original labels
        self.ui.label_dial1.hide()
        self.ui.label_needle1.hide()

        # Add Dial
        self.dial_item = QGraphicsPixmapItem(
            QPixmap("/home/torizon/app/src/images/green_60_big.png")
        )
        self.scene.addItem(self.dial_item)

        # Add Needle
        self.needle_item = QGraphicsPixmapItem(
            QPixmap("/home/torizon/app/src/images/needle_big.png")
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
        """Slot to receive angle from signal (called in main thread)"""
        self.needle_item.setRotation(angle)
        self.current_angle = angle

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

