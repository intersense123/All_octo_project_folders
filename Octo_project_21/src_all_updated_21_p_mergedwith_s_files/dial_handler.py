import random
import threading

from PySide2.QtCore import QObject, Signal, Property, QTimer
from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QGraphicsScene, QGraphicsView, QGraphicsPixmapItem

class DialHandler(QObject):
    # Signal to update needle from any thread
    needle_angle_changed = Signal(float)
    
    def __init__(self, main_window, needle_pos_x, needle_pos_y, pivot_point_x, pivot_point_y,dial,needle, parent=None):
        super().__init__(parent)
        self.mw= main_window
        self.ui = main_window  # For compatibility
        
        self.needle_pos_x = needle_pos_x
        self.needle_pos_y = needle_pos_y
        
        self.pivot_point_x = pivot_point_x
        self.pivot_point_y = pivot_point_y

        self.dial = dial
        self.needle = needle
        
        self.scene = QGraphicsScene()

        # Replace label_dial1 with graphics view
        self.view = QGraphicsView(self.scene, self.dial.parent())
        self.view.setGeometry(self.dial.geometry())
        self.view.setStyleSheet("background: transparent; border: none;")
        
        # Hide original labels
        self.dial.hide()
        self.needle.hide()

        # Add Dial
        self.dial_item = QGraphicsPixmapItem(
            QPixmap("/home/torizon/app/src/images/indicator3_green_2_big_1.png")
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
        
        # Spring animation parameters
        self.spring_stiffness = 0.4 #0.15  # Spring constant (higher = faster)
        self.spring_damping = 0.5 #0.75    # Damping quotient (0-1, lower = more oscillation)
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
        self.velocity = 0  # Reset velocity for new animation
        self.is_animating = True
        
        # Start animation timer if not already running
        if not self.animation_timer.isActive():
            self.animation_timer.start(16)  # ~60 FPS for smooth animation

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

