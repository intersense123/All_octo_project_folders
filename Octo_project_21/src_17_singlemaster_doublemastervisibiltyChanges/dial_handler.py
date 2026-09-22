import random

from PySide2.QtCore import QObject, QTimer, Property
from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QGraphicsScene, QGraphicsView, QGraphicsPixmapItem

class DialHandler(QObject):
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

        # self.ui.label_dial1.setPixmap(QPixmap("/home/torizon/app/src/images/green_60_big.png"))
        # self.ui.label_needle1.setPixmap(QPixmap("/home/torizon/app/src/images/needle_big.png"))
        
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
            self.pivot_point_x, self.pivot_point_y                                  #self.needle_item.boundingRect().center()
        )
        # Animation variables
        self.current_angle = 0
        self.target_angle = 0
        self.velocity = 0

        self.spring_constant = 0.15
        self.damping = 0.85

        # Animation timer (~60 FPS)
        self.animation_timer = QTimer(self)
        self.animation_timer.timeout.connect(self.update_animation)
        self.animation_timer.setInterval(16)

        # Change angle every 1 second
        self.change_timer = QTimer(self)
        self.change_timer.timeout.connect(self.start_new_animation)
        self.change_timer.start(1000)

        # Stop after 20 seconds
        self.stop_timer = QTimer(self)
        self.stop_timer.setSingleShot(True)
        self.stop_timer.timeout.connect(self.stop_animation)
        self.stop_timer.start(120000)

        self.start_new_animation()

    # ==================== UPDATE METHODS ====================
    
    def update_dial(self, image_path):
        """Update the dial image"""
        self.dial_item.setPixmap(QPixmap(image_path))
    
    def update_needle(self, image_path):
        """Update the needle image"""
        self.needle_item.setPixmap(QPixmap(image_path))
    
    # ==================== END UPDATE METHODS ====================

    # Property (keeping QObject inheritance as requested)
    @Property(float)
    def angle(self):
        return self.current_angle
    
    @angle.setter
    def angle(self, value):
        self.current_angle = value
        self.needle_item.setRotation(value)

    def start_new_animation(self):
        self.target_angle = random.uniform(-90, 90)
        self.animation_timer.start()

    def stop_animation(self):
        self.animation_timer.stop()
        self.change_timer.stop()

    def update_animation(self):
        d = self.current_angle - self.target_angle
        self.velocity += -self.spring_constant * d - self.damping * self.velocity
        self.current_angle += self.velocity
        self.needle_item.setRotation(self.current_angle)

        if -0.5 < d < 0.5 and -0.5 < self.velocity < 0.5:
            self.animation_timer.stop()
