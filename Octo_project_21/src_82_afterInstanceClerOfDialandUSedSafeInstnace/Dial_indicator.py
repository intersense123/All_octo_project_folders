import threading

from PySide2.QtWidgets import QHBoxLayout, QWidget
from PySide2.QtCore import QTimer, QTime, QSize, QObject , Qt, QCoreApplication,QMetaObject
from PySide2.QtGui import QPixmap, QFont
from sqlalchemy.orm import *
from models import *
from active_ui_togglebutton_handler import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PySide2.QtWidgets import (QApplication, QHBoxLayout, QMainWindow, QLabel,QSizePolicy,
     QVBoxLayout, QWidget)
from models import SessionLocal , ProbeBasedSettings,AOCBasedSettings
from messageBox import CustomMessageBox

import random
from PySide2.QtWidgets import QApplication, QWidget, QLabel
from PySide2.QtGui import QPixmap, QPainter, QTransform, QPaintEvent
from PySide2.QtCore import QTimer, Qt
from datetime import datetime
import sys
import random
from PySide2.QtWidgets import QApplication, QGraphicsView, QGraphicsScene,QGraphicsPixmapItem
from PySide2.QtGui import QPixmap
from PySide2.QtCore import QTimer, Property, QObject,QRect
from PySide2.QtWidgets import QGraphicsView, QGraphicsScene, QGraphicsPixmapItem
from PySide2.QtCore import QPropertyAnimation, QEasingCurve, QRectF

from PySide2.QtCore import QThread, Signal
from collections import deque
from dial_handler import DialHandler
import matplotlib
matplotlib.use("Qt5Agg")
import numpy as np
from decimal import Decimal
import time
class DialIndicator(QObject):
    """
    Handles:
    - UI visibility
    - Styling
    - Navigation
    - Keyboards
    - Power / menu actions
    """

    def __init__(self, main_window):
        try:
            super().__init__(parent=None) 
            self.ui = main_window   # 🔑 MainWindow reference
            self.app = None
            self.spc_manager = None
            self.channel_count = 0
            # Track mode per channel to prevent unintended style overwrite
            self._mode_by_channel = {
                1: self.ui.button_mode1.text(),
                2: self.ui.button_mode2.text(),
                3: self.ui.button_mode3.text(),
                4: self.ui.button_mode4.text(),
            }
            self.ui.button_mode1.clicked.connect(self.set_dimension_1_ui)
            self.ui.button_mode2.clicked.connect(self.set_dimension_2_ui)
            self.ui.button_mode3.clicked.connect(self.set_dimension_3_ui)
            self.ui.button_mode4.clicked.connect(self.set_dimension_4_ui)
            
            
            self._pm = {
                380: QPixmap(u"/home/torizon/app/src/images/dial-img-yellow-380.png"),
                300: QPixmap(u"/home/torizon/app/src/images/dial-img-yellow-300.png"),
                260: QPixmap(u"/home/torizon/app/src/images/dial-img-yellow-260.png"),
            }
            self._needle = {
                100 : QPixmap(u"/home/torizon/app/src/images/needle-white_100.png"),
                131 : QPixmap(u"/home/torizon/app/src/images/needle_withdot.png"),
            }
            # print(
            #     QPixmap("/home/torizon/app/src/images/needle_withdot.png").size()
            # )
            # ── Geometry cache ────────────────────────────────────────────
            # Layout for 1 channel
            self._geo = {
                1: {
                    "dial1_Dial":    QRect(10,  -10,   751, 211),
                    "needle1_Dial":  QRect(179, 74,  41, 121),
                    "val1_Dial":     QRect(220, 207, 350, 63),
                    "sts1_Dial":     QRect(220, 295, 330, 51),
                    "btn1_Dial":     QRect(600, 295, 120, 50),
                    "val1_Digit":    QRect(220, 60,  321, 101),
                    "sts1_Digit":    QRect(220, 210, 321, 101),
                    "btn1_Digit":    QRect(600, 230, 111, 61),
                    "pm_dial":       380,
                    "pm_needle":     131,
                },
                # Layout for 2 channels
                2: {
                    "dial1_Dial":    QRect(-1,  -10, 400, 230),
                    "needle1_Dial":  QRect(171, 62,  28, 132),
                    "val1_Dial":     QRect(50,  209, 290, 70),
                    "sts1_Dial":     QRect(40,  295, 220, 60),
                    "btn1_Dial":     QRect(280, 297, 90,  50),
                    "val1_Digit":    QRect(50,  60,  291, 101),
                    "sts1_Digit":    QRect(70,  240, 221, 81),
                    "btn1_Digit":    QRect(320, 260, 81,  50),
 
                    "dial2_Dial":    QRect(380, -10, 400, 230),
                    "needle2_Dial":  QRect(561, 62,  28, 132),
                    "val2_Dial":     QRect(440, 209, 290, 70),
                    "sts2_Dial":     QRect(430, 295, 220, 60),
                    "btn2_Dial":     QRect(674, 297, 90,  50),
                    "val2_Digit":    QRect(440, 60,  291, 101),
                    "sts2_Digit":    QRect(440, 240, 241, 81),
                    "btn2_Digit":    QRect(680, 260, 81,  50),
                    "pm_dial":       380,
                },
                # Layout for 3 channels
                3: {
                    "dial1_Dial":    QRect(50,  0,   260, 130),
                    "needle1_Dial":  QRect(179, 73,  41, 121),
                    "val1_Dial":     QRect(0,   130, 171, 42),
                    "sts1_Dial":     QRect(180, 130, 112, 42),
                    "btn1_Dial":     QRect(305, 130, 67,  42),
                    "val1_Digit":    QRect(60,  30,  211, 71),
                    "sts1_Digit":    QRect(60,  130, 211, 42),
                    "btn1_Digit":    QRect(314, 130, 70,  42),
 
                    "dial2_Dial":    QRect(460, 0,   260, 130),
                    "needle2_Dial":  QRect(179, 73,  41, 121),
                    "val2_Dial":     QRect(390, 130, 171, 42),
                    "sts2_Dial":     QRect(570, 130, 112, 42),
                    "btn2_Dial":     QRect(690, 130, 67,  41),
                    "val2_Digit":    QRect(450, 30,  211, 71),
                    "sts2_Digit":    QRect(450, 130, 211, 42),
                    "btn2_Digit":    QRect(680, 130, 70,  42),
 
                    "dial3_Dial":    QRect(270, 172, 260, 130),
                    "needle3_Dial":  QRect(179, 73,  41, 121),
                    "val3_Dial":     QRect(220, 309, 171, 42),
                    "sts3_Dial":     QRect(420, 309, 141, 42),
                    "btn3_Dial":     QRect(580, 309, 67,  42),
                    "val3_Digit":    QRect(290, 210, 211, 71),
                    "sts3_Digit":    QRect(290, 310, 211, 42),
                    "btn3_Digit":    QRect(550, 310, 70,  42),
                    "pm_dial":       260,
                },
                # Layout for 4 channels
                4: {
                    "dial1_Dial":    QRect(50,  -1,   261, 130),
                    "needle1_Dial":  QRect(172, 51,  16, 61),   
                    "val1_Dial":     QRect(0,   133, 171, 41),
                    "sts1_Dial":     QRect(180, 133, 111, 41),
                    "btn1_Dial":     QRect(305, 133, 70,  41),
                    "val1_Digit":    QRect(60,  30,  211, 71),
                    "sts1_Digit":    QRect(60,  133, 211, 42),
                    "btn1_Digit":    QRect(305, 133, 70,  42),
 
                    "dial2_Dial":    QRect(460, -1,   261, 130),
                    "needle2_Dial":  QRect(581, 51,  16, 61), 
                    "val2_Dial":     QRect(390, 133, 171, 41),
                    "sts2_Dial":     QRect(570, 133, 111, 41),
                    "btn2_Dial":     QRect(690, 133, 70,  41),
                    "val2_Digit":    QRect(450, 30,  211, 71),
                    "sts2_Digit":    QRect(450, 133, 211, 42),
                    "btn2_Digit":    QRect(690, 133, 70,  42),
 
                    "dial3_Dial":    QRect(50,  180, 261, 130),
                    "needle3_Dial":  QRect(171, 233,  16, 61), 
                    "val3_Dial":     QRect(0,   311, 171, 41),
                    "sts3_Dial":     QRect(180, 311, 111, 41),
                    "btn3_Dial":     QRect(305, 311, 70,  41),
                    "val3_Digit":    QRect(60,  210, 211, 71),
                    "sts3_Digit":    QRect(60,  311, 211, 42),
                    "btn3_Digit":    QRect(305, 311, 70,  42),
 
                    "dial4_Dial":    QRect(460, 180, 261, 130),
                    "needle4_Dial":  QRect(581, 233,  16, 61), 
                    "val4_Dial":     QRect(390, 311, 171, 41),
                    "sts4_Dial":     QRect(570, 311, 111, 41),
                    "btn4_Dial":     QRect(690, 311, 70,  41),
                    "val4_Digit":    QRect(450, 210, 211, 71),
                    "sts4_Digit":    QRect(450, 311, 211, 42),
                    "btn4_Digit":    QRect(690, 311, 70,  42),
                    "pm_dial":       260,
                    "pm_needle":     100,
                },
            }
 
            # state guard — tracks last rendered state so identical probe saves
            # return immediately without touching any widget
            self._last_visibility_state = None
            self._last_channel_count = 1
            # -------------------------------------------------
            # 1️⃣ Create graphics view container inside widget_3
            # -------------------------------------------------

            # Create Scene
            # self.scene = QGraphicsScene()

            # # Replace label_dial1 with graphics view
            # self.view = QGraphicsView(self.scene, self.ui.label_dial1.parent())
            # self.view.setGeometry(self.ui.label_dial1.geometry())
            # self.view.setStyleSheet("background: transparent; border: none;")

            # # Hide original labels
            # self.ui.label_dial1.hide()
            # self.ui.label_needle1.hide()

            # # Add Dial
            # self.dial_item = QGraphicsPixmapItem(
            #     QPixmap("/home/torizon/app/src/images/green_60_small.png")
            # )
            # self.scene.addItem(self.dial_item)

            # # Add Needle
            # self.needle_item = QGraphicsPixmapItem(
            #     QPixmap("/home/torizon/app/src/images/needle.png")
            # )
            # self.scene.addItem(self.needle_item)

            # # Center needle on dial
            # self.needle_item.setPos(78, 40)

            # # IMPORTANT → Set rotation pivot
            # self.needle_item.setTransformOriginPoint(
            #     4, 45                                  #self.needle_item.boundingRect().center()
            # )
            # # Animation variables
            # self.current_angle = 0
            # self.target_angle = 0
            # self.velocity = 0

            # self.spring_constant = 0.15
            # self.damping = 0.85

            # # Animation timer (~60 FPS)
            # self.animation_timer = QTimer(self)
            # self.animation_timer.timeout.connect(self.update_animation)
            # self.animation_timer.setInterval(16)

            # # Change angle every 1 second
            # self.change_timer = QTimer(self)
            # self.change_timer.timeout.connect(self.start_new_animation)
            # self.change_timer.start(1000)

            # # Stop after 20 seconds
            # self.stop_timer = QTimer(self)
            # self.stop_timer.setSingleShot(True)
            # self.stop_timer.timeout.connect(self.stop_animation)
            # self.stop_timer.start(60000)

            # self.start_new_animation()
            self.style_value = """
border: 1px solid #ffffff;
color: white;
border-radius: 1px;
padding: 1px;
font-size: 30pt;
font-weight: bold;
"""     
            self.style_status = """
font-size: 30pt;
font-weight: bold;
"""
            self.ui.data_handler.dialVisibilityChanged.connect(
                self.set_visibility
                )
            
            # QTimer.singleShot(2000, self._test_needle)

        except Exception as e:
            print(f"Error in initializtion of Dial_Indicator : {e}")
            
    # def rotate_needle(self, angle):
    #     animation = QPropertyAnimation(self.needle_item, b"rotation")
    #     animation.setDuration(600)
    #     animation.setStartValue(self.needle_item.rotation())
    #     animation.setEndValue(angle)
    #     animation.setEasingCurve(QEasingCurve.OutBack)  # spring effect
    #     animation.start()

    #     self.animation = animation  # prevent garbage collection
    
    # Property (keeping QObject inheritance as requested)
    # @Property(float)
    # def angle(self):
    #     return self.current_angle

    # @angle.setter
    # def angle(self, value):
    #     self.current_angle = value
    #     self.needle_item.setRotation(value)

    # def start_new_animation(self):
    #     self.target_angle = random.uniform(-90, 90)
    #     self.animation_timer.start()

    # def stop_animation(self):
    #     self.animation_timer.stop()
    #     self.change_timer.stop()

    # def update_animation(self):
    #     displacement = self.current_angle - self.target_angle

    #     spring_force = -self.spring_constant * displacement
    #     damping_force = -self.damping * self.velocity
    #     acceleration = spring_force + damping_force

    #     self.velocity += acceleration
    #     self.current_angle += self.velocity

    #     # 🔥 Rotate the proxy widget (which wraps the QLabel)
    #     self.needle_item.setRotation(self.current_angle)

    #     if abs(displacement) < 0.5 and abs(self.velocity) < 0.5:
    #         self.animation_timer.stop()
  
    def set_dimension_1_ui(self):
        current_mode = self._mode_by_channel.get(1, self.ui.button_mode1.text())
        if current_mode == 'Dial':
            self.ui.button_mode1.setText('SPC')
            self.ui.label_dial1.hide()
            self.ui.widget_spc1.show()
            # self.set_visibility()
            self._mode_by_channel[1] = 'SPC'
        elif current_mode == 'SPC':
            self.ui.button_mode1.setText('Digit')
            self.ui.label_dial1.hide()
            self.ui.widget_spc1.hide()
            # self.set_visibility()
            self._mode_by_channel[1] = 'Digit'
        elif current_mode == 'Digit':
            self.ui.button_mode1.setText('Dial')
            self.ui.label_dial1.show()
            self.ui.widget_spc1.hide()
            self._mode_by_channel[1] = 'Dial'
        self.set_visibility()
           
    def set_dimension_2_ui(self):
        current_mode = self._mode_by_channel.get(2, self.ui.button_mode2.text())
        if current_mode == 'Dial':
            self.ui.button_mode2.setText('SPC')
            self.ui.label_dial2.hide()
            self.ui.widget_spc2.show()
            # self.set_visibility()
            self._mode_by_channel[2] = 'SPC'
        elif current_mode == 'SPC':
            self.ui.button_mode2.setText('Digit')
            self.ui.label_dial2.hide()
            self.ui.widget_spc2.hide()
            self._mode_by_channel[2] = 'Digit'
        elif current_mode == 'Digit':
            self.ui.button_mode2.setText('Dial')
            self.ui.label_dial2.show()
            self.ui.widget_spc2.hide()
            self._mode_by_channel[2] = 'Dial'
        self.set_visibility()
        
        
    def set_dimension_3_ui(self):
        current_mode = self._mode_by_channel.get(3, self.ui.button_mode3.text())
        if current_mode == 'Dial':
            self.ui.button_mode3.setText('SPC')
            self.ui.label_dial3.hide()
            self.ui.widget_spc3.show()
            # self.set_visibility()
            self._mode_by_channel[3] = 'SPC'
        elif current_mode == 'SPC':
            self.ui.button_mode3.setText('Digit')
            self.ui.label_dial3.hide()
            self.ui.widget_spc3.hide()
            self._mode_by_channel[3] = 'Digit'
        elif current_mode == 'Digit':
            self.ui.button_mode3.setText('Dial')
            self.ui.label_dial3.show()
            self.ui.widget_spc3.hide()
            self._mode_by_channel[3] = 'Dial'
        self.set_visibility()
        
   
    def set_dimension_4_ui(self):
        current_mode = self._mode_by_channel.get(4, self.ui.button_mode4.text())
        if current_mode == 'Dial':
            self.ui.button_mode4.setText('SPC')
            self.ui.label_dial4.hide()
            self.ui.widget_spc4.show()    
            self._mode_by_channel[4] = 'SPC'
        elif current_mode == 'SPC':
            self.ui.button_mode4.setText('Digit')
            self.ui.label_dial4.hide()
            self.ui.widget_spc4.hide()        
            self._mode_by_channel[4] = 'Digit'
        elif current_mode == 'Digit':
            self.ui.button_mode4.setText('Dial')
            self.ui.label_dial4.show()
            self.ui.widget_spc4.hide()
            self._mode_by_channel[4] = 'Dial'
        self.set_visibility()

    def _destroy_dial_handlers(self):
        """Destroy all DialHandler instances so they get recreated with correct geometry"""
        for attr in ["dial_1_anim", "dial_2_anim", "dial_3_anim", "dial_4_anim"]:
            if hasattr(self.ui, attr):
                handler = getattr(self.ui, attr)
                try:
                    handler.animation_timer.stop()
                    handler.view.hide()
                    handler.view.setParent(None)    # detach from parent widget
                    handler.view.deleteLater()      # schedule Qt cleanup
                    handler.scene.clear()           # remove all scene items
                except Exception as e:
                    print(f"Error destroying {attr}: {e}")
                delattr(self.ui, attr)
    #to enable disable line while switching combobox of Ovality ON and OFF
    def  set_visibility(self):
        try:
            self.ui.widget_spc1.hide()
            self.ui.widget_spc2.hide()
            self.ui.widget_spc3.hide()
            self.ui.widget_spc4.hide()
            
            # Ensure UI mode text matches cached mode to prevent style overwrites
            self.ui.button_mode1.setText(self._mode_by_channel.get(1, self.ui.button_mode1.text()))
            self.ui.button_mode2.setText(self._mode_by_channel.get(2, self.ui.button_mode2.text()))
            self.ui.button_mode3.setText(self._mode_by_channel.get(3, self.ui.button_mode3.text()))
            self.ui.button_mode4.setText(self._mode_by_channel.get(4, self.ui.button_mode4.text()))
 
            channels = self.app.get_channels_for_program(
                int(self.ui.valueObj.activeVariables_dict["ActiveProgramId"])
            )
            self.channel_count = len(channels)
            print(f"channel in set visibilty {self.channel_count}")
 
            # ── SPC sync (always runs, cheap) ─────────────────────────────
            if self.ui.button_mode1.text() == 'SPC':
                if self.spc_manager:
                    self.spc_manager.set_active_channels(self.channel_count)
            if self.ui.button_mode2.text() == 'SPC':
                if self.spc_manager:
                    self.spc_manager.set_active_channels(self.channel_count)
            if self.ui.button_mode3.text() == 'SPC':
                if self.spc_manager:
                    self.spc_manager.set_active_channels(self.channel_count)
            if self.ui.button_mode4.text() == 'SPC':
                if self.spc_manager:
                    self.spc_manager.set_active_channels(self.channel_count)
            
            # ── DESTROY dial handlers if channel count changed ────────
            # This forces recreation with correct geometry for new channel layout
            if self.channel_count != self._last_channel_count:
                print(f"Channel count changed {self._last_channel_count} → {self.channel_count}, rebuilding dials")
                self._destroy_dial_handlers()
                self._last_channel_count = self.channel_count
                
            # ── STATE GUARD ───────────────────────────────────────────────
            # Tuple of channel count + all 4 modes.
            # If unchanged since last call → skip every widget operation below.
            _new_state = (
                self.channel_count,
                self._mode_by_channel.get(1),
                self._mode_by_channel.get(2),
                self._mode_by_channel.get(3),
                self._mode_by_channel.get(4),
            )
            if _new_state == self._last_visibility_state:
                return      # ← probe save with no visual change exits here
            self._last_visibility_state = _new_state
            # ── END GUARD ─────────────────────────────────────────────────
            

            if (True):
                if self.channel_count == 0 or None:
                    self.ui.label_dial1.hide()
                    self.ui.label_dial2.hide()
                    self.ui.label_dial3.hide()
                    self.ui.label_dial4.hide()
                    self.ui.label_status1.hide()
                    self.ui.label_status2.hide()
                    self.ui.label_status3.hide()
                    self.ui.label_status4.hide()
                    self.ui.label_value1.hide()
                    self.ui.label_value2.hide()
                    self.ui.label_value3.hide()
                    self.ui.label_value4.hide()
                    self.ui.button_mode1.hide()
                    self.ui.button_mode2.hide()
                    self.ui.button_mode3.hide()
                    self.ui.button_mode4.hide()
 
                elif self.channel_count == 1:
                    g = self._geo[1]                        # ← pre-built rects
                    pm = self._pm[g["pm_dial"]]             # ← pre-loaded pixmap
                    needle = self._needle[g["pm_needle"]]
                    if self.ui.button_mode1.text() == 'Dial':
                        self.ui.label_dial1.show()
                        self.ui.label_needle1.show()
                        # self.ui.label_dial1.setPixmap(pm)
                        # self.ui.label_needle1.setGeometry(g["needle1_Dial"])
                        # self.ui.label_needle1.setPixmap(needle)
                        self.ui.label_dial1.setGeometry(g["dial1_Dial"])
                        self.ui.label_dial1.setAlignment(Qt.AlignmentFlag.AlignCenter)
                        self.ui.label_value1.setGeometry(g["val1_Dial"])
                        self.ui.label_value1.setAlignment(Qt.AlignmentFlag.AlignCenter)
                        self.ui.label_status1.setGeometry(g["sts1_Dial"])
                        self.ui.label_status1.setAlignment(Qt.AlignmentFlag.AlignCenter)
                        self.ui.button_mode1.setGeometry(g["btn1_Dial"])
                        # Create DialHandler once
                        if not hasattr(self.ui, "dial_1_anim"):
                            self.ui.dial_1_anim = DialHandler(
                                self.ui,
                                needle_pos_x  = 179,   # 190 - 11
                                needle_pos_y  = 74,    # 182 - 110
                                pivot_point_x = 11,    # SVG width 23 / 2
                                pivot_point_y = 110,   # dot near bottom of 120px SVG
                                dial_label = self.ui.label_dial1,
                                needle_label = self.ui.label_needle1,
                                dial = "/home/torizon/app/src/images/dial-img-yellow-380.png",
                                needle = "/home/torizon/app/src/images/Needle-circle-white-svg.svg",
                                probe="D1",
                                channel_count = self.channel_count
                            )
                        self.ui.label_value1.setStyleSheet(self.style_value)
                        self.ui.label_status1.setStyleSheet(self.style_status)
 
                    elif self.ui.button_mode1.text() == 'Digit':
                        self.ui.label_value1.setGeometry(g["val1_Digit"])
                        self.ui.label_value1.setAlignment(Qt.AlignmentFlag.AlignCenter)
                        self.ui.label_status1.setGeometry(g["sts1_Digit"])
                        self.ui.label_status1.setAlignment(Qt.AlignmentFlag.AlignCenter)
                        self.ui.button_mode1.setGeometry(g["btn1_Digit"])
 
                    self.ui.label_value1.show()
                    self.ui.label_status1.show()
                    self.ui.button_mode1.show()
                    self.ui.label_dial2.hide()
                    self.ui.label_dial3.hide()
                    self.ui.label_dial4.hide()
                    self.ui.label_needle2.hide()
                    self.ui.label_needle3.hide()
                    self.ui.label_needle4.hide()
                    self.ui.label_status2.hide()
                    self.ui.label_status3.hide()
                    self.ui.label_status4.hide()
                    self.ui.label_value2.hide()
                    self.ui.label_value3.hide()
                    self.ui.label_value4.hide()
                    self.ui.button_mode2.hide()
                    self.ui.button_mode3.hide()
                    self.ui.button_mode4.hide()
 
                elif self.channel_count == 2:
                    g = self._geo[2]
                    pm = self._pm[g["pm_dial"]]
                    self.ui.label_value2.show()
                    self.ui.label_status2.show()
                    self.ui.button_mode2.show()
                    self.ui.label_dial3.hide()
                    self.ui.label_dial4.hide()
                    self.ui.label_needle3.hide()
                    self.ui.label_needle4.hide()
                    self.ui.label_value3.hide()
                    self.ui.label_value4.hide()
                    self.ui.label_status3.hide()
                    self.ui.label_status4.hide()
                    self.ui.button_mode3.hide()
                    self.ui.button_mode4.hide()
                    if self.ui.button_mode1.text() == 'Dial':
                        self.ui.label_dial1.show()
                        # self.ui.label_dial1.setPixmap(pm)
                        self.ui.label_dial1.setGeometry(g["dial1_Dial"])
                        self.ui.label_dial1.setAlignment(Qt.AlignmentFlag.AlignCenter)
                        self.ui.label_value1.setGeometry(g["val1_Dial"])
                        self.ui.label_value1.setAlignment(Qt.AlignmentFlag.AlignCenter)
                        self.ui.label_status1.setGeometry(g["sts1_Dial"])
                        self.ui.label_status1.setAlignment(Qt.AlignmentFlag.AlignCenter)
                        self.ui.button_mode1.setGeometry(g["btn1_Dial"])
                        if not hasattr(self.ui, "dial_1_anim"):
                            self.ui.dial_1_anim = DialHandler(
                                self.ui,
                                needle_pos_x  = 179,   # 190 - 11
                                needle_pos_y  = 74,    # 182 - 110
                                pivot_point_x = 11,    # SVG width 23 / 2
                                pivot_point_y = 110,   # dot near bottom of 120px SVG
                                dial_label = self.ui.label_dial1,
                                needle_label = self.ui.label_needle1,
                                dial = "/home/torizon/app/src/images/dial-img-yellow-380.png",
                                needle = "/home/torizon/app/src/images/Needle-circle-white-svg.svg",
                                probe="D1",
                                channel_count = self.channel_count
                            )
                        self.ui.label_value1.setStyleSheet(self.style_value)
                        self.ui.label_status1.setStyleSheet(self.style_status)
 
                    if self.ui.button_mode2.text() == 'Dial':
                        self.ui.label_dial2.show()
                        # self.ui.label_dial2.setPixmap(pm)
                        self.ui.label_dial2.setGeometry(g["dial2_Dial"])
                        self.ui.label_dial2.setAlignment(Qt.AlignmentFlag.AlignCenter)
                        self.ui.label_value2.setGeometry(g["val2_Dial"])
                        self.ui.label_value2.setAlignment(Qt.AlignmentFlag.AlignCenter)
                        self.ui.label_status2.setGeometry(g["sts2_Dial"])
                        self.ui.label_status2.setAlignment(Qt.AlignmentFlag.AlignCenter)
                        self.ui.button_mode2.setGeometry(g["btn2_Dial"])
                        if not hasattr(self.ui, "dial_2_anim"):
                            self.ui.dial_2_anim = DialHandler(
                                self.ui,
                                needle_pos_x  = 179,   # 190 - 11
                                needle_pos_y  = 74,    # 182 - 110
                                pivot_point_x = 11,    # SVG width 23 / 2
                                pivot_point_y = 110,   # dot near bottom of 120px SVG
                                dial_label = self.ui.label_dial2,
                                needle_label = self.ui.label_needle2,
                                dial = "/home/torizon/app/src/images/dial-img-yellow-380.png",
                                needle = "/home/torizon/app/src/images/Needle-circle-white-svg.svg",
                                probe="D2",
                                channel_count = self.channel_count
                            )
                        self.ui.label_value2.setStyleSheet(self.style_value)
                        self.ui.label_status2.setStyleSheet(self.style_status)
 
                    if self.ui.button_mode1.text() == 'Digit':
                        self.ui.label_value1.setGeometry(g["val1_Digit"])
                        self.ui.label_value1.setAlignment(Qt.AlignmentFlag.AlignCenter)
                        self.ui.label_status1.setGeometry(g["sts1_Digit"])
                        self.ui.label_status1.setAlignment(Qt.AlignmentFlag.AlignCenter)
                        self.ui.button_mode1.setGeometry(g["btn1_Digit"])
 
                    if self.ui.button_mode2.text() == 'Digit':
                        self.ui.label_value2.setGeometry(g["val2_Digit"])
                        self.ui.label_value2.setAlignment(Qt.AlignmentFlag.AlignCenter)
                        self.ui.label_status2.setGeometry(g["sts2_Digit"])
                        self.ui.label_status2.setAlignment(Qt.AlignmentFlag.AlignCenter)
                        self.ui.button_mode2.setGeometry(g["btn2_Digit"])
 
                    # self.ui.label_value2.show()
                    # self.ui.label_status2.show()
                    # self.ui.button_mode2.show()
                    # self.ui.label_dial3.hide()
                    # self.ui.label_dial4.hide()
                    # self.ui.label_needle3.hide()
                    # self.ui.label_needle4.hide()
                    # self.ui.label_value3.hide()
                    # self.ui.label_value4.hide()
                    # self.ui.label_status3.hide()
                    # self.ui.label_status4.hide()
                    # self.ui.button_mode3.hide()
                    # self.ui.button_mode4.hide()
 
                elif self.channel_count == 3:
                    g = self._geo[3]
                    pm = self._pm[g["pm_dial"]]
 
                    if self.ui.button_mode1.text() == 'Dial':
                        self.ui.label_dial1.show()
                        self.ui.label_dial1.setPixmap(pm)
                        self.ui.label_dial1.setGeometry(g["dial1_Dial"])
                        self.ui.label_dial1.setAlignment(Qt.AlignmentFlag.AlignCenter)
                        self.ui.label_value1.setGeometry(g["val1_Dial"])
                        self.ui.label_value1.setAlignment(Qt.AlignmentFlag.AlignCenter)
                        self.ui.label_status1.setGeometry(g["sts1_Dial"])
                        self.ui.label_status1.setAlignment(Qt.AlignmentFlag.AlignCenter)
                        self.ui.button_mode1.setGeometry(g["btn1_Dial"])
                        self.ui.label_value1.setStyleSheet(self.style_value)
                        self.ui.label_status1.setStyleSheet(self.style_status)
 
                    if self.ui.button_mode2.text() == 'Dial':
                        self.ui.label_dial2.show()
                        self.ui.label_dial2.setPixmap(pm)
                        self.ui.label_dial2.setGeometry(g["dial2_Dial"])
                        self.ui.label_dial2.setAlignment(Qt.AlignmentFlag.AlignCenter)
                        self.ui.label_value2.setGeometry(g["val2_Dial"])
                        self.ui.label_value2.setAlignment(Qt.AlignmentFlag.AlignCenter)
                        self.ui.label_status2.setGeometry(g["sts2_Dial"])
                        self.ui.label_status2.setAlignment(Qt.AlignmentFlag.AlignCenter)
                        self.ui.button_mode2.setGeometry(g["btn2_Dial"])
                        self.ui.label_value2.setStyleSheet(self.style_value)
                        self.ui.label_status2.setStyleSheet(self.style_status)
 
                    if self.ui.button_mode3.text() == 'Dial':
                        self.ui.label_dial3.show()
                        self.ui.label_dial3.setPixmap(pm)
                        self.ui.label_dial3.setGeometry(g["dial3_Dial"])
                        self.ui.label_dial3.setAlignment(Qt.AlignmentFlag.AlignCenter)
                        self.ui.label_value3.setGeometry(g["val3_Dial"])
                        self.ui.label_value3.setAlignment(Qt.AlignmentFlag.AlignCenter)
                        self.ui.label_status3.setGeometry(g["sts3_Dial"])
                        self.ui.label_status3.setAlignment(Qt.AlignmentFlag.AlignCenter)
                        self.ui.button_mode3.setGeometry(g["btn3_Dial"])
                        self.ui.label_value3.setStyleSheet(self.style_value)
                        self.ui.label_status3.setStyleSheet(self.style_status)
 
                    if self.ui.button_mode1.text() == 'Digit':
                        self.ui.label_value1.setGeometry(g["val1_Digit"])
                        self.ui.label_status1.setGeometry(g["sts1_Digit"])
                        self.ui.button_mode1.setGeometry(g["btn1_Digit"])
 
                    if self.ui.button_mode2.text() == 'Digit':
                        self.ui.label_value2.setGeometry(g["val2_Digit"])
                        self.ui.label_status2.setGeometry(g["sts2_Digit"])
                        self.ui.button_mode2.setGeometry(g["btn2_Digit"])
 
                    if self.ui.button_mode3.text() == 'Digit':
                        self.ui.label_value3.setGeometry(g["val3_Digit"])
                        self.ui.label_status3.setGeometry(g["sts3_Digit"])
                        self.ui.button_mode3.setGeometry(g["btn3_Digit"])
 
                    self.ui.label_value3.show()
                    self.ui.label_status3.show()
                    self.ui.button_mode3.show()
                    self.ui.label_dial4.hide()
                    self.ui.label_value4.hide()
                    self.ui.label_status4.hide()
                    self.ui.button_mode4.hide()
 
                else:   # 4 channels
                    g = self._geo[4]
                    pm = self._pm[g["pm_dial"]]
                    needle = self._needle[g["pm_needle"]]
 
                    if self.ui.button_mode1.text() == 'Dial':
                        self.ui.label_dial1.show()
                        self.ui.label_needle1.show()
                        self.ui.label_needle1.setPixmap(needle)
                        self.ui.label_dial1.setGeometry(g["dial1_Dial"])
                        self.ui.label_needle1.setGeometry(g["needle1_Dial"])
                        self.ui.label_needle1.setAlignment(Qt.AlignmentFlag.AlignCenter)
                        self.ui.label_dial1.setPixmap(pm)
                        self.ui.label_dial1.setAlignment(Qt.AlignmentFlag.AlignCenter)
                        self.ui.label_value1.setGeometry(g["val1_Dial"])
                        self.ui.label_value1.setAlignment(Qt.AlignmentFlag.AlignCenter)
                        self.ui.label_status1.setGeometry(g["sts1_Dial"])
                        self.ui.label_status1.setAlignment(Qt.AlignmentFlag.AlignCenter)
                        self.ui.button_mode1.setGeometry(g["btn1_Dial"])
                        self.ui.label_value1.setStyleSheet(self.style_value)
                        self.ui.label_status1.setStyleSheet(self.style_status)
 
                    if self.ui.button_mode2.text() == 'Dial':
                        self.ui.label_dial2.show()
                        self.ui.label_needle2.show()
                        self.ui.label_needle2.setPixmap(needle)
                        self.ui.label_dial2.setPixmap(pm)
                        self.ui.label_dial2.setGeometry(g["dial2_Dial"])
                        self.ui.label_needle2.setGeometry(g["needle2_Dial"])
                        self.ui.label_needle2.setAlignment(Qt.AlignmentFlag.AlignCenter)
                        self.ui.label_dial2.setAlignment(Qt.AlignmentFlag.AlignCenter)
                        self.ui.label_value2.setGeometry(g["val2_Dial"])
                        self.ui.label_value2.setAlignment(Qt.AlignmentFlag.AlignCenter)
                        self.ui.label_status2.setGeometry(g["sts2_Dial"])
                        self.ui.label_status2.setAlignment(Qt.AlignmentFlag.AlignCenter)
                        self.ui.button_mode2.setGeometry(g["btn2_Dial"])
                        self.ui.label_value2.setStyleSheet(self.style_value)
                        self.ui.label_status2.setStyleSheet(self.style_status)
 
                    if self.ui.button_mode3.text() == 'Dial':
                        self.ui.label_dial3.show()
                        self.ui.label_needle3.show()
                        self.ui.label_needle3.setPixmap(needle)
                        self.ui.label_dial3.setPixmap(pm)
                        self.ui.label_dial3.setGeometry(g["dial3_Dial"])
                        self.ui.label_needle3.setGeometry(g["needle3_Dial"])
                        self.ui.label_needle3.setAlignment(Qt.AlignmentFlag.AlignCenter)
                        self.ui.label_dial3.setAlignment(Qt.AlignmentFlag.AlignCenter)
                        self.ui.label_value3.setGeometry(g["val3_Dial"])
                        self.ui.label_value3.setAlignment(Qt.AlignmentFlag.AlignCenter)
                        self.ui.label_status3.setGeometry(g["sts3_Dial"])
                        self.ui.label_status3.setAlignment(Qt.AlignmentFlag.AlignCenter)
                        self.ui.button_mode3.setGeometry(g["btn3_Dial"])
                        self.ui.label_value3.setStyleSheet(self.style_value)
                        self.ui.label_status3.setStyleSheet(self.style_status)
 
                    if self.ui.button_mode4.text() == 'Dial':
                        self.ui.label_dial4.show()
                        self.ui.label_needle4.show()
                        self.ui.label_needle4.setPixmap(needle)
                        self.ui.label_dial4.setPixmap(pm)
                        self.ui.label_dial4.setGeometry(g["dial4_Dial"])
                        self.ui.label_needle4.setGeometry(g["needle4_Dial"])
                        self.ui.label_needle4.setAlignment(Qt.AlignmentFlag.AlignCenter)
                        self.ui.label_dial4.setAlignment(Qt.AlignmentFlag.AlignCenter)
                        self.ui.label_value4.setGeometry(g["val4_Dial"])
                        self.ui.label_value4.setAlignment(Qt.AlignmentFlag.AlignCenter)
                        self.ui.label_status4.setGeometry(g["sts4_Dial"])
                        self.ui.label_status4.setAlignment(Qt.AlignmentFlag.AlignCenter)
                        self.ui.button_mode4.setGeometry(g["btn4_Dial"])
                        self.ui.label_value4.setStyleSheet(self.style_value)
                        self.ui.label_status4.setStyleSheet(self.style_status)
 
                    if self.ui.button_mode1.text() == 'Digit':
                        self.ui.label_value1.setGeometry(g["val1_Digit"])
                        self.ui.label_status1.setGeometry(g["sts1_Digit"])
                        self.ui.button_mode1.setGeometry(g["btn1_Digit"])
 
                    if self.ui.button_mode2.text() == 'Digit':
                        self.ui.label_value2.setGeometry(g["val2_Digit"])
                        self.ui.label_status2.setGeometry(g["sts2_Digit"])
                        self.ui.button_mode2.setGeometry(g["btn2_Digit"])
 
                    if self.ui.button_mode3.text() == 'Digit':
                        self.ui.label_value3.setGeometry(g["val3_Digit"])
                        self.ui.label_status3.setGeometry(g["sts3_Digit"])
                        self.ui.button_mode3.setGeometry(g["btn3_Digit"])
 
                    if self.ui.button_mode4.text() == 'Digit':
                        self.ui.label_value4.setGeometry(g["val4_Digit"])
                        self.ui.label_status4.setGeometry(g["sts4_Digit"])
                        self.ui.button_mode4.setGeometry(g["btn4_Digit"])
 
                    self.ui.label_value4.show()
                    self.ui.label_status4.show()
                    self.ui.button_mode4.show()
                    
                    # self.ui.label_needle1.hide()
                    # self.ui.label_needle2.hide()
                    # self.ui.label_needle3.hide()
                    # self.ui.label_needle4.hide()
 
        except Exception as e:
            print(f"Error in Dial Indicator : {e}")
   

# class SPCWorker(QThread):
#     data_signal = Signal(int, float)

#     def __init__(self):
#         super().__init__()
#         self.queue = deque()
#         self.running = True

#     def add_data(self, ch, val):
#         self.queue.append((ch, val))

#     def run(self):
#         while self.running:
#             if self.queue:
#                 ch, val = self.queue.popleft()
#                 self.data_signal.emit(ch, val)
#             self.msleep(1)   # 🔥 control speed

#     def stop(self):
#         self.running = False       

class SPCBase:
        def __init__(self, title, lol, lsl, lcl, nominal, ucl, usl, uol,least_count):
            try:
                self.title = title
                self.limits = [lol, lsl, lcl, nominal, ucl, usl, uol]
                self.spc_count = 50
                self.data_raw = []
                self.least_count = least_count
                

                self.data_raw = deque(maxlen=self.spc_count)
                self.fig = Figure()
                self.canvas = FigureCanvas(self.fig)
                self.ax = self.fig.add_subplot(111)
                
                range_val = uol - lol
                self.padding = max(range_val * 0.2, 0.001)

                # Dark theme
                self.fig.patch.set_facecolor("#2b2b2b")
                self.ax.set_facecolor("#2b2b2b")
                self.x_data = list(range(1, self.spc_count + 1))
                self.ax.set_xlim(0, self.spc_count - 1)
                self.y_data = [np.nan] * self.spc_count
                # self.init_blank_ui()
                self.create_static_ui()
                self.update_limits_ui()
            except Exception as e:
                print(f"Error SPC init -> {e}")

        # ---------------- RESET ----------------
        # def reset_graph(self):
        #     self.data_raw = []   # 🔥 IMPORTANT
        #     self.y_data = [np.nan] * self.spc_count

        #     x_full = list(range(1, self.spc_count + 1))
        #     self.line.set_data(x_full, self.y_data)

        #     self.canvas.draw_idle()
        def reset_graph(self):
            try:
                self.data_raw.clear()

                self.line.set_data([], [])

                # self.sc.set_offsets(np.empty((0, 2)))

                self.canvas.draw_idle()

            except Exception as e:
                print(f"Error reset_graph -> {e}")

        # ---------------- LIMIT SET ----------------
        # def set_limits(self, lol, lsl, lcl, nominal, ucl, usl, uol,least_count):
        #     self.limits = [lol, lsl, lcl, nominal, ucl, usl, uol]
        #     self.least_count = least_count
        #     self.init_blank_ui()
        def set_limits(self, lol, lsl, lcl, nominal, ucl, usl, uol, least_count):

            new_limits = [lol, lsl, lcl, nominal, ucl, usl, uol]

            if (
                self.limits == new_limits and
                self.least_count == least_count
            ):
                return

            self.limits = new_limits
            self.least_count = least_count

            self.data_raw.clear()

            self.update_limits_ui()

        def create_static_ui(self):
            self.ax.clear()

            self.fig.patch.set_facecolor("#2b2b2b")
            self.ax.set_facecolor("#2b2b2b")

            self.ax.set_xlim(1, self.spc_count)
            self.ax.set_xticks(self.get_dynamic_xticks())

            self.ax.tick_params(axis='x', colors='white')
            self.ax.tick_params(axis='y', colors='white')

            self.ax.grid(False)

            self.line, = self.ax.plot([], [], color="blue", marker="o", linewidth=2)

            self.canvas.draw()
            
        # ---------------- MAIN UI ----------------
        def update_limits_ui(self):
            lol, lsl, lcl, nominal, ucl, usl, uol = self.limits

            self.ax.clear()

            self.fig.patch.set_facecolor("#2b2b2b")
            self.ax.set_facecolor("#2b2b2b")

            self.ax.set_xlim(1, self.spc_count)
            self.ax.set_xticks(self.get_dynamic_xticks())

            self.ax.tick_params(axis='x', colors='white')
            self.ax.tick_params(axis='y', colors='white')

            self.ax.grid(False)
            
            self.ax.axhline(usl, color='red', linestyle='--', linewidth=1.5)
            self.ax.axhline(lsl, color='red', linestyle='--', linewidth=1.5)

            self.ax.axhline(nominal, color='green', linestyle='--', linewidth=1.5)
            self.ax.axhline(ucl, color='green', linestyle=':', linewidth=1.5)
            self.ax.axhline(lcl, color='green', linestyle=':', linewidth=1.5)

            if uol != 0 and lol != 0:
                self.ax.axhline(uol, color='red', linestyle='-.', linewidth=1.5)
                self.ax.axhline(lol, color='red', linestyle='-.', linewidth=1.5)

            # ---------- BACKGROUND COLORS ----------
            if uol != 0 and lol != 0:
                self.ax.axhspan(lsl, lol, color='red', alpha=0.9)
                self.ax.axhspan(usl, uol, color='red', alpha=0.9)

            self.ax.axhspan(lsl, lcl, color='yellow', alpha=0.9)
            self.ax.axhspan(lcl, nominal, color='green', alpha=0.9)
            self.ax.axhspan(nominal, ucl, color='green', alpha=0.9)
            self.ax.axhspan(ucl, usl, color='yellow', alpha=0.9)

            yticks = [lsl, lcl, nominal, ucl, usl]

            if uol and lol:
                yticks.insert(0, lol)
                yticks.append(uol)

            self.ax.set_yticks(yticks)

            decimals = abs(
                Decimal(str(self.least_count)).as_tuple().exponent
            )

            self.ax.set_yticklabels(
                [f"{v:.{decimals}f}" for v in yticks],
                color="white"
            )

            padding = abs(uol - lol) * 0.08
            self.ax.set_ylim(lol - padding, uol + padding)

            self.ax.set_title(
                self.title,
                color="white",
                fontsize=10,
                fontweight="bold",
                pad=2
            )

            self.line, = self.ax.plot([], [], color="blue", marker="o", linewidth=2)

            self.canvas.draw_idle()
                
        def clamp_value(self, value):
            try:
                lol, lsl, lcl, nominal, ucl, usl, uol = self.limits

                if value > uol:
                    return uol
                elif value < lol:
                    return lol
                return value
            except Exception as e:
                print(f"Error in clamp_value - > {e}")
        # ---------------- GRAPH LOAD ----------------
        def generate_graph(self, raw_data):
            try:
                raw_data = raw_data[-self.spc_count:]

                self.data_raw = [
                    self.clamp_value(v)
                    for v in raw_data
                ]

                if not self.data_raw:
                    self.line.set_data([], [])
                    # self.sc.set_offsets(np.empty((0, 2)))
                    self.canvas.draw_idle()
                    return

                x = np.arange(1, len(self.data_raw) + 1)

                self.line.set_data(x, self.data_raw)

                # self.sc.set_offsets(
                #     np.c_[x, self.data_raw]
                # )

                self.canvas.draw_idle()

            except Exception as e:
                print(f"Error in generate_graph -> {e}")

        # def update_graph(self, value):
        #     try:
        #         value = self.clamp_value(value)

        #         self.data_raw.append(value)

        #         if len(self.data_raw) > self.spc_count:
        #             self.data_raw.pop(0)

        #         x = np.arange(1, len(self.data_raw) + 1)

        #         self.line.set_data(x, self.data_raw)

        #         # self.sc.set_offsets(
        #         #     np.c_[x, self.data_raw]
        #         # )

        #         self.canvas.draw_idle()

        #     except Exception as e:
        #         print(f"Error update_graph -> {e}")
        

        def update_graph(self, value):
            start = time.perf_counter()
            print("GRAPH UPDATE", time.time())
            self.data_raw.append(self.clamp_value(value))

            count = len(self.data_raw)

            self.line.set_data(
                self.x_data[:count],
                list(self.data_raw)
            )

            # print("before draw:", time.perf_counter() - start)

            self.canvas.draw_idle()
            from PySide2.QtWidgets import QApplication
            QApplication.processEvents()

            # print("GRAPH DRAWN", time.time())
            # print("after draw:", time.perf_counter() - start)
        # def update_graph(self, value):
        #     try:
        #         self.data_raw.append(self.clamp_value(value))

        #         count = len(self.data_raw)

        #         x = self.x_data[:count]

        #         self.line.set_data(x, list(self.data_raw))

        #         self.canvas.draw_idle()

        #     except Exception as e:
        #         print(f"Error update_graph -> {e}")
        def get_dynamic_xticks(self):
            try:
                if self.spc_count <= 10:
                    ticks = list(range(1, self.spc_count + 1))

                elif self.spc_count <= 20:
                    ticks = list(range(1, self.spc_count + 1, 2))

                else:
                    ticks = list(range(1, self.spc_count + 1, 5))

                # 🔥 ALWAYS include 50
                if self.spc_count not in ticks:
                    ticks.append(self.spc_count)

                return ticks
            except Exception as e:
                print(f"Error in get_dynamic_xticks ->{e}")

        # ---------------- MARGINS ----------------
        def set_margins(self, left, right, top, bottom):
            self.fig.subplots_adjust(left=left, right=right, top=top, bottom=bottom)
            self.canvas.draw_idle()
            
        def __del__(self):
            """Destructor: safely close the Matplotlib figure to free memory."""
            try:
                self.canvas.close(self.fig)
            except Exception:
                pass   
        
class SPCWidget(QWidget):
    def __init__(self, spc, parent=None):
        try:
            super().__init__(parent)
            self.spc = spc

            layout = QVBoxLayout(self)
            layout.setContentsMargins(0, 0, 0, 0)
            layout.setSpacing(2)

            # self.spc.canvas.setMinimumHeight(130)
            # ---- graph ----
            self.spc.canvas.setSizePolicy(
                QSizePolicy.Expanding,
                QSizePolicy.Preferred   
            )
            layout.addWidget(self.spc.canvas, 1)
        except Exception as e:
            print(f"error in SPCWidget -> {e}")


    def load_value(self, value):
        try:
            self.spc.update_graph(value)
        except Exception as e:
            print(f"error in load_value -> {e}")
            
    def reset(self):
        self.spc.reset_graph()
        
           
class SPCManager:
    def __init__(self, main_window):
        try:
            self.ui = main_window
            
        
            self.spc_all = {
            1: SPCWidget(SPCBase("D1", lol=20.000,lsl=20.010,lcl=20.015,nominal=20.020,ucl=20.025,usl=20.030,uol=20.042,least_count = 0.001)),
            2: SPCWidget(SPCBase("D2", lol=20.000,lsl=20.010,lcl=20.015,nominal=20.020,ucl=20.025,usl=20.030,uol=20.042,least_count = 0.001)),
            3: SPCWidget(SPCBase("D3", lol=20.000,lsl=20.010,lcl=20.015,nominal=20.020,ucl=20.025,usl=20.030,uol=20.042,least_count = 0.001)),
            4: SPCWidget(SPCBase("D4", lol=20.000,lsl=20.010,lcl=20.015,nominal=20.020,ucl=20.025,usl=20.030,uol=20.042,least_count = 0.001)),
            }

            self.active_channels = []
            
            # Initialize spc_1, spc_2, spc_3, spc_4 to None first
            self.spc_1 = None
            self.spc_2 = None
            self.spc_3 = None
            self.spc_4 = None
            
            self.layout_initialized = False
            
            # self.ui.label_dial1.hide()
            # self.ui.label_needle1.hide()
            
            # ✅ CREATE layouts if not exists
            self._ensure_layout(self.ui.widget_spc1)
            self._ensure_layout(self.ui.widget_spc2)
            self._ensure_layout(self.ui.widget_spc3)
            self._ensure_layout(self.ui.widget_spc4)

            # now layouts will NOT be None - get layouts with safe access
            widget_spc1_layout = self.ui.widget_spc1.layout()
            widget_spc2_layout = self.ui.widget_spc2.layout()
            widget_spc3_layout = self.ui.widget_spc3.layout()
            widget_spc4_layout = self.ui.widget_spc4.layout()
            
            if widget_spc1_layout is not None:
                self.spc_1 = widget_spc1_layout
            if widget_spc2_layout is not None:
                self.spc_2 = widget_spc2_layout
            if widget_spc3_layout is not None:
                self.spc_3 = widget_spc3_layout
            if widget_spc4_layout is not None:
                self.spc_4 = widget_spc4_layout
            
            self.ui.button_spcReset.clicked.connect(self.reset_all_spc)
            # self.worker = SPCWorker()
            # # if self.ui.stacked.currentIndex() == 25:           
            # self.worker.data_signal.connect(self.update_value)  # SAFE UI
            # self.worker.start()
            # else:
            #     self.worker.stop()
            #     self.worker.wait()
            # self.ui.data_handler.probe_setttings_saved.connect(
            #     self.load_spc
            # )
            self.load_spc()
            # self.probe_id = 1
            self.leastcount = 0.001
            self.ui.data_handler.probe_setttings_saved.connect(self.load_spc)
            self.last_reset_counter = 0
        except Exception as e:
            print(f"Error in intialization of SPCManager :-> {e}")
            
    def load_spc(self):
        try:
            progId = int(self.ui.valueObj.activeVariables_dict["ActiveProgramId"])

            self.load_program_OnSpc(progId)
        except Exception as e:
            print(f"Error while loading_spc -> {e}")
            
    # def get_decimals(self,lc):
    #     try:
    #         s = str(lc)
    #         return len(s.split('.')[1]) if '.' in s else 0
    #     except Exception as e:
    #         print(f"Error in get_decimals {e}")
   
    def _ensure_layout(self, widget):
        try:
            if widget.layout() is None:
                layout = QVBoxLayout(widget)
                layout.setContentsMargins(0, 0, 0, 0)
                widget.setLayout(layout)
        except Exception as e:
            print(f"Error in _ensure_layout {e}")
            
    def reset_all_spc(self):
        try:
            program_dict = self.ui.valueObj.ProgramSettings_dict

            for dim in self.active_channels:
                

                    probe_settings = program_dict.get(f"D{dim}", {}).get("ProbeBasedSettings")

                    if not probe_settings:
                        continue

                    unique_string = self.ui.data_handler.build_probe_unique_string(
                        f"D{dim}",
                        probe_settings
                    )

                    probe_id = self.ui.savedbObj.get_probe_id_by_settings(unique_string)

                    if probe_id:
                        self.ui.savedbObj.reset_spc_for_probe(probe_id)

            for ch in self.active_channels:
                spc_widget = self.spc_all.get(ch)
                if spc_widget:
                    spc_widget.reset()

            self.is_spc_reset = True

        except Exception as e:
            print(f"Reset SPC error -> {e}")
            
    def load_program_OnSpc(self, program_id: int):
        session = SessionLocal()
        try:
            # 🔥 ONE query only
            probe_rows = session.query(ProbeBasedSettings)\
                .filter(ProbeBasedSettings.ProgramId == program_id)\
                .all()

            aoc_rows = session.query(AOCBasedSettings)\
                .filter(AOCBasedSettings.ProgramId == program_id)\
                .all()

            probe_map = {row.Dimension: row for row in probe_rows}
            aoc_map = {row.Dimension: row for row in aoc_rows}

            AocState = self.ui.valueObj.activeVariables_dict["AOCOnOff"]

            # for ch, spc_widget in self.spc_all.items():
            #     dim = f"D{ch}"
            #     row = probe_map.get(dim)

            #     if not row:
            #         continue
            for dim, row in probe_map.items():

                try:
                    ch = int(dim[1:])
                except:
                    continue

                spc_widget = self.spc_all.get(ch)

                if not spc_widget:
                    continue

                row_Aoc = aoc_map.get(dim)

                # decimals = self.get_decimals()
                decimals = abs(
                    Decimal(str(row.LeastCount)).as_tuple().exponent
                )

                lsl = round(row.LowerSpecificationLimit, decimals)
                usl = round(row.UpperSpecificationLimit, decimals)

                range_val = usl - lsl
                margin = round(range_val * 0.3, decimals)

                lol_probe = round(lsl - margin, decimals)
                uol_probe = round(usl + margin, decimals)

                if AocState == "ON" and row_Aoc:
                    spc_widget.spc.set_limits(
                        lol=round(row_Aoc.LowerOffsetLimit, decimals),
                        lsl=lsl,
                        lcl=round(row.LowerControlLimit, decimals),
                        nominal=round(row.NominalValue, decimals),
                        ucl=round(row.UpperControlLimit, decimals),
                        usl=usl,
                        uol=round(row_Aoc.UpperOffsetLimit, decimals),
                        least_count=row.LeastCount
                    )
                else:
                    spc_widget.spc.set_limits(
                        lol=lol_probe,
                        lsl=lsl,
                        lcl=round(row.LowerControlLimit, decimals),
                        nominal=round(row.NominalValue, decimals),
                        ucl=round(row.UpperControlLimit, decimals),
                        usl=usl,
                        uol=uol_probe,
                        least_count=row.LeastCount
                    )

        finally:
            session.close()
            
    def load_data(self, channels):
        try:

            program_dict = self.ui.valueObj.ProgramSettings_dict

            for dim in channels:

                probe_settings = program_dict.get(dim, {}).get("ProbeBasedSettings")

                unique_string = self.ui.data_handler.build_probe_unique_string(dim, probe_settings)
                                
                if not probe_settings:
                    continue
                
                probe_id = self.ui.savedbObj.get_probe_id_by_settings(unique_string)

                if not probe_id:
                    continue

                values = self.ui.savedbObj.get_probe_values_for_spc(probe_id)
                
                if not values:
                    continue

                values.reverse()   # oldest first

                channel = int(dim[1])  # D1 → 1

                self.spc_all[channel].spc.generate_graph(values)
        except Exception as e:
            print(f"Error in loading spc last Values - > {e}")
                
    #clear layout for first time
    def clear_layout(self, layout):
        try:
            if layout is None:
                return
            while layout.count():
                item = layout.takeAt(0)
                if item.widget():
                    item.widget().setParent(None)
        except Exception as e:
            print(f"Error in clear_layout:-> {e}")

    #set active channels
    def set_active_channels(self, channels):
        try:
            self.active_channels = list(range(1, channels + 1))
            self.apply_layout()
        except Exception as e:
            print(f"Error for setting active channel as-> {e}")

    #manage layout as per spc instance
    
    def apply_layout(self):
        try:
            # ensure layouts
            if self.spc_1 is None:
                self._ensure_layout(self.ui.widget_spc1)
                self.spc_1 = self.ui.widget_spc1.layout()
            if self.spc_2 is None:
                self._ensure_layout(self.ui.widget_spc2)
                self.spc_2 = self.ui.widget_spc2.layout()
            if self.spc_3 is None:
                self._ensure_layout(self.ui.widget_spc3)
                self.spc_3 = self.ui.widget_spc3.layout()
            if self.spc_4 is None:
                self._ensure_layout(self.ui.widget_spc4)
                self.spc_4 = self.ui.widget_spc4.layout()

            # ✅ ALWAYS DEFINE THIS
            spcs = [self.spc_all[ch] for ch in self.active_channels]
            count = len(spcs)

            # ✅ ADD WIDGETS ONLY ONCE
            if not self.layout_initialized:

                for layout in (self.spc_1, self.spc_2, self.spc_3, self.spc_4):
                    if layout is not None:
                        self.clear_layout(layout)

                if count >= 1 and self.spc_1:
                    self.spc_1.addWidget(spcs[0])

                if count >= 2 and self.spc_2:
                    self.spc_2.addWidget(spcs[1])

                if count >= 3 and self.spc_3:
                    self.spc_3.addWidget(spcs[2])

                if count >= 4 and self.spc_4:
                    self.spc_4.addWidget(spcs[3])

                self.layout_initialized = True

            # ---------------- UI LOGIC ----------------
            self.ui.label_dial1.hide()
            self.ui.label_needle1.hide()
            self.ui.label_dial2.hide()
            self.ui.label_needle2.hide()
            self.ui.label_dial3.hide()
            self.ui.label_needle3.hide()
            self.ui.label_dial4.hide()
            self.ui.label_needle4.hide()
            

            # ---------------- USE count safely ----------------
            if count == 1:
                spcs[0].spc.canvas.setMinimumHeight(150)
                spcs[0].spc.set_margins(
                        left=0.25,
                        right=0.97,
                        top=0.90,#0.85,
                        bottom=0.26
                    )
                if self.ui.button_mode1.text() == 'SPC' :
                    self.ui.widget_spc1.show()
                    self.ui.widget_spc1.setGeometry(0, -10, 771, 200)

            elif count == 2:
                for spc in spcs:
                    spc.spc.canvas.setMinimumHeight(150)
                    spc.spc.set_margins(
                        left=0.25,
                        right=0.97,
                        top=0.90,#0.85,
                        bottom=0.26
                    )
                if self.ui.button_mode1.text() == 'SPC' :
                    self.ui.widget_spc1.show()
                    self.ui.widget_spc1.setGeometry(QRect(0, 0, 370, 220))
                    self.ui.label_value1.setGeometry(QRect(70, 220, 291, 60))
                    self.ui.label_status1.setGeometry(QRect(70, 300, 220, 60))
                    self.ui.button_mode1.setGeometry(QRect(317,300,70,50))
                if self.ui.button_mode2.text() == 'SPC' :
                    self.ui.widget_spc2.show()
                    # self.ui.widget_spc3.setGeometry(0, 180, 771, 230)
                    self.ui.widget_spc2.setGeometry(QRect(395, 0, 370, 220))
                    self.ui.label_value2.setGeometry(QRect(440, 220, 291, 60))
                    self.ui.label_status2.setGeometry(QRect(440, 300, 220, 60))
                    self.ui.button_mode2.setGeometry(QRect(680,300,70,50))
                    

            elif count == 3:
                for spc in spcs:
                    spc.spc.canvas.setMinimumHeight(120)
                    spc.spc.set_margins(
                        left=0.20,
                        right=0.95,
                        top=0.90,#0.85,
                        bottom=0.26
                    )
                if self.ui.button_mode1.text() == 'SPC' :
                    self.ui.widget_spc1.show()
                    self.ui.widget_spc1.setGeometry(QRect(5, 0, 370, 130))
                    # self.ui.label_value1.setGeometry(QRect(0, 130, 171, 42))
                    # self.ui.label_status1.setGeometry(QRect(180, 130, 112, 42))
                    # self.ui.button_mode1.setGeometry(QRect(305,130,67,42))
                    
                if self.ui.button_mode2.text() == 'SPC' :
                    self.ui.widget_spc2.show()
                    self.ui.widget_spc2.setGeometry(QRect(383, 0, 370, 130))
                    # self.ui.label_value2.setGeometry(QRect(390, 130, 171, 42))
                    # self.ui.label_status2.setGeometry(QRect(570, 130, 112, 42))
                    # self.ui.button_mode2.setGeometry(QRect(690,130,67,41))
                    
                if self.ui.button_mode3.text() == 'SPC' :
                    self.ui.widget_spc3.show()
                    self.ui.widget_spc3.setGeometry(QRect(220, 179, 371, 130))
                    # self.ui.label_value3.setGeometry(QRect(220, 309, 171, 42))
                    # self.ui.label_status3.setGeometry(QRect(420, 309, 141, 42))
                    # self.ui.button_mode3.setGeometry(QRect(580,309,67,42))
                # if self.ui.button_mode2.text() == 'SPC' :
                    # self.ui.widget_spc1.show()

            elif count == 4:
                for spc in spcs:
                    spc.spc.canvas.setMinimumHeight(100)
                    spc.spc.set_margins(
                        left=0.20,
                        right=0.95,
                        top=0.90,#0.85,
                        bottom=0.26
                    )
                if self.ui.button_mode1.text() == 'SPC' :
                    self.ui.widget_spc1.show()
                    self.ui.widget_spc1.setGeometry(QRect(5, 0, 370, 130))
                    
                if self.ui.button_mode2.text() == 'SPC' :
                    self.ui.widget_spc2.show()
                    self.ui.widget_spc2.setGeometry(QRect(383, 0, 370, 130))

                if self.ui.button_mode3.text() == 'SPC' :
                    self.ui.widget_spc3.show()
                    self.ui.widget_spc3.setGeometry(QRect(5, 180, 370, 130))

                if self.ui.button_mode4.text() == 'SPC' :
                    self.ui.widget_spc4.show()
                    self.ui.widget_spc4.setGeometry(QRect(383, 180, 370, 130))

        except Exception as e:
            print(f"Error while applying layout -> {e}")      
 
    #update value on spc chanrt as per active channels
    def update_value(self, channel, value):
        try:
            if channel not in self.active_channels:
                return

            spc_widget = self.spc_all.get(channel)
            if not spc_widget:
                return

            spc_widget.load_value(value)
            
        except Exception as e:
            print(f"Error update value in graph -> {e}")
            msg = CustomMessageBox("Failed to update value on Graph", "error",
                                   parent=self.ui)
            msg.exec_()
    


########## DIGIT UI Working Code Hided Spc ANd Dial ###############################


# from PySide2.QtWidgets import QHBoxLayout, QWidget
# from PySide2.QtCore import QTimer, QTime, QSize, QObject , Qt, QCoreApplication,QMetaObject
# from PySide2.QtGui import QPixmap, QFont
# from sqlalchemy.orm import *
# from models import *
# from active_ui_togglebutton_handler import *
# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.figure import Figure
# from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
# from PySide2.QtWidgets import (QApplication, QHBoxLayout, QMainWindow, QLabel,QSizePolicy,
#      QVBoxLayout, QWidget)
# from models import SessionLocal , ProbeBasedSettings,AOCBasedSettings
# from messageBox import CustomMessageBox

# import random
# from PySide2.QtWidgets import QApplication, QWidget, QLabel
# from PySide2.QtGui import QPixmap, QPainter, QTransform, QPaintEvent
# from PySide2.QtCore import QTimer, Qt
# from datetime import datetime
# import sys
# import random
# from PySide2.QtWidgets import QApplication, QGraphicsView, QGraphicsScene,QGraphicsPixmapItem
# from PySide2.QtGui import QPixmap
# from PySide2.QtCore import QTimer, Property, QObject,QRect
# from PySide2.QtWidgets import QGraphicsView, QGraphicsScene, QGraphicsPixmapItem
# from PySide2.QtCore import QPropertyAnimation, QEasingCurve, QRectF

# from PySide2.QtCore import QThread, Signal
# from collections import deque
# from dial_handler import DialHandler
# import matplotlib
# matplotlib.use("Qt5Agg")
# import numpy as np

# class DialIndicator(QObject):
#     """
#     Handles:
#     - UI visibility
#     - Styling
#     - Navigation
#     - Keyboards
#     - Power / menu actions
#     """

#     def __init__(self, main_window):
#         try:
#             super().__init__(parent=None) 
#             self.ui = main_window   # 🔑 MainWindow reference
#             self.app = None
#             # self.spc_manager = None
#             self.channel_count = 0
#             self.hide_labels()
#             # Track mode per channel to prevent unintended style overwrite
#             # self._mode_by_channel = {
#             #     1: self.ui.button_mode1.text(),
#             #     2: self.ui.button_mode2.text(),
#             #     3: self.ui.button_mode3.text(),
#             #     4: self.ui.button_mode4.text(),
#             # }
#             # self.ui.button_mode1.clicked.connect(self.set_dimension_1_ui)
#             # self.ui.button_mode2.clicked.connect(self.set_dimension_2_ui)
#             # self.ui.button_mode3.clicked.connect(self.set_dimension_3_ui)
#             # self.ui.button_mode4.clicked.connect(self.set_dimension_4_ui)
#             self.style_value = """
# border: 1px solid #ffffff;
# color: white;
# border-radius: 1px;
# padding: 1px;
# font-size: 35pt;
# font-weight: bold;
# """     
#             self.style_status = """
# font-size: 35pt;
# font-weight: bold;
# """
#             self.ui.data_handler.dialVisibilityChanged.connect(
#             self.set_visibility
#             )
            
#             # -------------------------------------------------
#             # 1️⃣ Create graphics view container inside widget_3
#             # -------------------------------------------------

#             # Create Scene
#             # self.scene = QGraphicsScene()

#             # # Replace label_dial1 with graphics view
#             # self.view = QGraphicsView(self.scene, self.ui.label_dial1.parent())
#             # self.view.setGeometry(self.ui.label_dial1.geometry())
#             # self.view.setStyleSheet("background: transparent; border: none;")

#             # # Hide original labels
#             # self.ui.label_dial1.hide()
#             # self.ui.label_needle1.hide()

#             # # Add Dial
#             # self.dial_item = QGraphicsPixmapItem(
#             #     QPixmap("/home/torizon/app/src/images/green_60_small.png")
#             # )
#             # self.scene.addItem(self.dial_item)

#             # # Add Needle
#             # self.needle_item = QGraphicsPixmapItem(
#             #     QPixmap("/home/torizon/app/src/images/needle.png")
#             # )
#             # self.scene.addItem(self.needle_item)

#             # # Center needle on dial
#             # self.needle_item.setPos(78, 40)

#             # # IMPORTANT → Set rotation pivot
#             # self.needle_item.setTransformOriginPoint(
#             #     4, 45                                  #self.needle_item.boundingRect().center()
#             # )
#             # # Animation variables
#             # self.current_angle = 0
#             # self.target_angle = 0
#             # self.velocity = 0

#             # self.spring_constant = 0.15
#             # self.damping = 0.85

#             # # Animation timer (~60 FPS)
#             # self.animation_timer = QTimer(self)
#             # self.animation_timer.timeout.connect(self.update_animation)
#             # self.animation_timer.setInterval(16)

#             # # Change angle every 1 second
#             # self.change_timer = QTimer(self)
#             # self.change_timer.timeout.connect(self.start_new_animation)
#             # self.change_timer.start(1000)

#             # # Stop after 20 seconds
#             # self.stop_timer = QTimer(self)
#             # self.stop_timer.setSingleShot(True)
#             # self.stop_timer.timeout.connect(self.stop_animation)
#             # self.stop_timer.start(60000)

#             # self.start_new_animation()

#         except Exception as e:
#             print(f"Error in initializtion of Dial_Indicator : {e}")
            
#     # def rotate_needle(self, angle):
#     #     animation = QPropertyAnimation(self.needle_item, b"rotation")
#     #     animation.setDuration(600)
#     #     animation.setStartValue(self.needle_item.rotation())
#     #     animation.setEndValue(angle)
#     #     animation.setEasingCurve(QEasingCurve.OutBack)  # spring effect
#     #     animation.start()

#     #     self.animation = animation  # prevent garbage collection
    
#     # Property (keeping QObject inheritance as requested)
#     # @Property(float)
#     # def angle(self):
#     #     return self.current_angle

#     # @angle.setter
#     # def angle(self, value):
#     #     self.current_angle = value
#     #     self.needle_item.setRotation(value)

#     # def start_new_animation(self):
#     #     self.target_angle = random.uniform(-90, 90)
#     #     self.animation_timer.start()

#     # def stop_animation(self):
#     #     self.animation_timer.stop()
#     #     self.change_timer.stop()

#     # def update_animation(self):
#     #     displacement = self.current_angle - self.target_angle

#     #     spring_force = -self.spring_constant * displacement
#     #     damping_force = -self.damping * self.velocity
#     #     acceleration = spring_force + damping_force

#     #     self.velocity += acceleration
#     #     self.current_angle += self.velocity

#     #     # 🔥 Rotate the proxy widget (which wraps the QLabel)
#     #     self.needle_item.setRotation(self.current_angle)

#     #     if abs(displacement) < 0.5 and abs(self.velocity) < 0.5:
#     #         self.animation_timer.stop()

      
#     def set_dimension_1_ui(self):
#         current_mode = self._mode_by_channel.get(1, self.ui.button_mode1.text())
#         if current_mode == 'Dial':
#             self.ui.button_mode1.setText('SPC')
#             self.ui.label_dial1.hide()
#             self.ui.widget_spc1.show()
#             # self.set_visibility()
#             self._mode_by_channel[1] = 'SPC'
#         elif current_mode == 'SPC':
#             self.ui.button_mode1.setText('Digit')
#             self.ui.label_dial1.hide()
#             self.ui.widget_spc1.hide()
#             # self.set_visibility()
#             self._mode_by_channel[1] = 'Digit'
#         elif current_mode == 'Digit':
#             self.ui.button_mode1.setText('Dial')
#             self.ui.label_dial1.show()
#             self.ui.widget_spc1.hide()
#             self._mode_by_channel[1] = 'Dial'
#         self.set_visibility()
           
#     def set_dimension_2_ui(self):
#         current_mode = self._mode_by_channel.get(2, self.ui.button_mode2.text())
#         if current_mode == 'Dial':
#             self.ui.button_mode2.setText('SPC')
#             self.ui.label_dial2.hide()
#             self.ui.widget_spc2.show()
#             # self.set_visibility()
#             self._mode_by_channel[2] = 'SPC'
#         elif current_mode == 'SPC':
#             self.ui.button_mode2.setText('Digit')
#             self.ui.label_dial2.hide()
#             self.ui.widget_spc2.hide()
#             self._mode_by_channel[2] = 'Digit'
#         elif current_mode == 'Digit':
#             self.ui.button_mode2.setText('Dial')
#             self.ui.label_dial2.show()
#             self.ui.widget_spc2.hide()
#             self._mode_by_channel[2] = 'Dial'
#         self.set_visibility()
        
        
#     def set_dimension_3_ui(self):
#         current_mode = self._mode_by_channel.get(3, self.ui.button_mode3.text())
#         if current_mode == 'Dial':
#             self.ui.button_mode3.setText('SPC')
#             self.ui.label_dial3.hide()
#             self.ui.widget_spc3.show()
#             # self.set_visibility()
#             self._mode_by_channel[3] = 'SPC'
#         elif current_mode == 'SPC':
#             self.ui.button_mode3.setText('Digit')
#             self.ui.label_dial3.hide()
#             self.ui.widget_spc3.hide()
#             self._mode_by_channel[3] = 'Digit'
#         elif current_mode == 'Digit':
#             self.ui.button_mode3.setText('Dial')
#             self.ui.label_dial3.show()
#             self.ui.widget_spc3.hide()
#             self._mode_by_channel[3] = 'Dial'
#         self.set_visibility()
        
   
#     def set_dimension_4_ui(self):
#         current_mode = self._mode_by_channel.get(4, self.ui.button_mode4.text())
#         if current_mode == 'Dial':
#             self.ui.button_mode4.setText('SPC')
#             self.ui.label_dial4.hide()
#             self.ui.widget_spc4.show()    
#             self._mode_by_channel[4] = 'SPC'
#         elif current_mode == 'SPC':
#             self.ui.button_mode4.setText('Digit')
#             self.ui.label_dial4.hide()
#             self.ui.widget_spc4.hide()        
#             self._mode_by_channel[4] = 'Digit'
#         elif current_mode == 'Digit':
#             self.ui.button_mode4.setText('Dial')
#             self.ui.label_dial4.show()
#             self.ui.widget_spc4.hide()
#             self._mode_by_channel[4] = 'Dial'
#         self.set_visibility()

#     def set_visibility(self):
#         channels=self.app.get_channels_for_program(
#                 int(self.ui.valueObj.activeVariables_dict["ActiveProgramId"])
#             )
            
#         self.channel_count = len(channels)
#         # print(f"channel in set visibilty {self.channel_count}")
#         self.ui.label_status1.show()
#         self.ui.label_status2.show()
#         self.ui.label_status3.show()
#         self.ui.label_status4.show()
#         self.ui.label_value1.show()
#         self.ui.label_value2.show()
#         self.ui.label_value3.show()
#         self.ui.label_value4.show()
#         if self.channel_count == 0 or None:
#             self.hide_labels()
#             self.ui.label_status1.hide()
#             self.ui.label_status2.hide()
#             self.ui.label_status3.hide()
#             self.ui.label_status4.hide()
#             self.ui.label_value1.hide()
#             self.ui.label_value2.hide()
#             self.ui.label_value3.hide()
#             self.ui.label_value4.hide()
#         if self.channel_count == 1:
#             self.ui.label_value2.hide()
#             self.ui.label_value3.hide()
#             self.ui.label_value4.hide()
#             self.ui.label_status2.hide()
#             self.ui.label_status3.hide()
#             self.ui.label_status4.hide()
#             self.ui.label_value1.setStyleSheet(self.style_value + f"font-size: 50pt;")
#             self.ui.label_status1.setStyleSheet(self.style_status+ f"font-size: 50pt;")
#             self.ui.label_value1.setGeometry(QRect(200, 80, 400, 150))
#             self.ui.label_status1.setGeometry(QRect(200, 230, 400, 130))
            
#         elif self.channel_count == 2:
#             self.ui.label_value1.setStyleSheet(self.style_value + f"font-size: 45pt;")
#             self.ui.label_status1.setStyleSheet(self.style_status + f"font-size: 45pt;")
#             self.ui.label_value2.setStyleSheet(self.style_value + f"font-size: 45pt;")
#             self.ui.label_status2.setStyleSheet( self.style_status + f"font-size: 45pt;")
            
#             self.ui.label_value1.setGeometry(QRect(40, 50, 330, 150))
#             self.ui.label_value2.setGeometry(QRect(420, 50, 330, 150))
#             self.ui.label_status1.setGeometry(QRect(40, 210, 330, 130))
#             self.ui.label_status2.setGeometry(QRect(420, 210, 330, 130))
            
            
#             self.ui.label_value3.hide()
#             self.ui.label_value4.hide()
#             self.ui.label_status3.hide()
#             self.ui.label_status4.hide()
            
            
            
#         elif self.channel_count == 3:
#             self.ui.label_value1.setStyleSheet(self.style_value)
#             self.ui.label_status1.setStyleSheet(self.style_status)
#             self.ui.label_value2.setStyleSheet(self.style_value)
#             self.ui.label_status2.setStyleSheet(self.style_status)
#             self.ui.label_value3.setStyleSheet(self.style_value)
#             self.ui.label_status3.setStyleSheet(self.style_status)
           
            
#             self.ui.label_value1.setGeometry(QRect(60, 10, 280, 100))
#             self.ui.label_value2.setGeometry(QRect(460, 10, 280, 100))
#             self.ui.label_value3.setGeometry(QRect(250, 190, 280, 100))
            
#             self.ui.label_status1.setGeometry(QRect(60, 130, 280, 40))
#             self.ui.label_status2.setGeometry(QRect(460, 130, 280, 40))
#             self.ui.label_status3.setGeometry(QRect(250, 310, 280, 40))
            
#             self.ui.label_value4.hide()
#             self.ui.label_status4.hide()
            
#         elif self.channel_count == 4:
#             # self.ui.label_dial1.show()
#             # self.ui.label_dial2.show()
#             # self.ui.label_dial3.show()
#             # self.ui.label_dial4.show()
#             self.ui.label_value1.setStyleSheet(self.style_value)
#             self.ui.label_status1.setStyleSheet(self.style_status)
#             self.ui.label_value2.setStyleSheet(self.style_value)
#             self.ui.label_status2.setStyleSheet( self.style_status)
#             self.ui.label_value3.setStyleSheet(self.style_value)
#             self.ui.label_status3.setStyleSheet( self.style_status)
#             self.ui.label_value4.setStyleSheet(self.style_value)
#             self.ui.label_status4.setStyleSheet( self.style_status)
            
#             self.ui.label_value1.setGeometry(QRect(60, 10, 280, 100))
#             self.ui.label_value2.setGeometry(QRect(460, 10, 280, 100))
#             self.ui.label_value3.setGeometry(QRect(60, 190, 280, 100))
#             self.ui.label_value4.setGeometry(QRect(460, 190, 280, 100))
            
#             self.ui.label_status1.setGeometry(QRect(60, 130, 280, 40))
#             self.ui.label_status2.setGeometry(QRect(460, 130, 280, 40))
#             self.ui.label_status3.setGeometry(QRect(60, 310, 280, 40))
#             self.ui.label_status4.setGeometry(QRect(460, 310, 280, 40))
            
            
            
#     # #to enable disable line while switching combobox of Ovality ON and OFF
#     # def set_visibility(self):
#     #     try:
#     #         self.ui.widget_spc1.hide()
#     #         self.ui.widget_spc2.hide()
#     #         self.ui.widget_spc3.hide()
#     #         self.ui.widget_spc4.hide()   

#     #         # Ensure UI mode text matches cached mode to prevent style overwrites
#     #         self.ui.button_mode1.setText(self._mode_by_channel.get(1, self.ui.button_mode1.text()))
#     #         self.ui.button_mode2.setText(self._mode_by_channel.get(2, self.ui.button_mode2.text()))
#     #         self.ui.button_mode3.setText(self._mode_by_channel.get(3, self.ui.button_mode3.text()))
#     #         self.ui.button_mode4.setText(self._mode_by_channel.get(4, self.ui.button_mode4.text()))
            
#     #         channels=self.app.get_channels_for_program(
#     #             int(self.ui.valueObj.activeVariables_dict["ActiveProgramId"])
#     #         )
            
#     #         self.channel_count = len(channels)
#     #         print(f"channel in set visibilty {self.channel_count}")
    
#     #         if self.ui.button_mode1.text() == 'SPC':
#     #             if self.spc_manager:
#     #                 # self.spc_manager.load_previous_spc_values(channels)
#     #                 self.spc_manager.set_active_channels(self.channel_count)
#     #         if self.ui.button_mode2.text() == 'SPC':
#     #             if self.spc_manager:
#     #                 self.spc_manager.set_active_channels(self.channel_count)
#     #         if self.ui.button_mode3.text() == 'SPC':
#     #             if self.spc_manager:
#     #                 self.spc_manager.set_active_channels(self.channel_count)
#     #         if self.ui.button_mode4.text() == 'SPC':
#     #             if self.spc_manager:
#     #                 self.spc_manager.set_active_channels(self.channel_count)
            
#     #         # else:
#     #         if (True):
#     #             if self.channel_count == 0 or None :
#     #                 self.hide_labels.hide()
#     #                     # self.ui.label_dial1.hide()
#     #                     # self.ui.label_dial2.hide()
#     #                     # self.ui.label_dial3.hide()
#     #                     # self.ui.label_dial4.hide()
#     #                     # self.ui.label_status1.hide()
#     #                     # self.ui.label_status2.hide()
#     #                     # self.ui.label_status3.hide()
#     #                     # self.ui.label_status4.hide()
#     #                     # self.ui.label_value1.hide()
#     #                     # self.ui.label_value2.hide()
#     #                     # self.ui.label_value3.hide()
#     #                     # self.ui.label_value4.hide()
#     #                     # self.ui.button_mode1.hide()
#     #                     # self.ui.button_mode2.hide()
#     #                     # self.ui.button_mode3.hide()
#     #                     # self.ui.button_mode4.hide()
                        
#     #             elif self.channel_count == 1:
#     #                 if self.ui.button_mode1.text() == 'Dial':
#     #                     self.ui.label_dial1.show()
#     #                     self.ui.label_needle1.show()
#     #                     self.ui.label_dial1.setGeometry(QRect(0, -10, 771, 241))
#     #                     self.ui.label_dial1.setAlignment(Qt.AlignmentFlag.AlignCenter)
#     #                     self.ui.label_value1.setGeometry(QRect(30, 230, 771, 40))
#     #                     self.ui.label_value1.setAlignment(Qt.AlignmentFlag.AlignCenter)
#     #                     self.ui.label_status1.setGeometry(QRect(90, 310, 291, 40))
#     #                     self.ui.label_status1.setAlignment(Qt.AlignmentFlag.AlignCenter)
#     #                     self.ui.label_needle1.setGeometry(QRect(380, 150, 20, 40))
#     #                     self.ui.label_needle1.setAlignment(Qt.AlignmentFlag.AlignCenter)
#     #                     self.ui.button_mode1.setGeometry(QRect(540,310,101,40))
#     #                     self.ui.label_dial1.show()

#     #                     # Create DialHandler once
#     #                     # self.ui.dial_1_anim = DialHandler(self.ui, 172, 64, 6, 118, self.ui.label_dial1,self.ui.label_needle1)
                        
#     #                     # self.scene = QGraphicsScene()

#     #                     # # Replace label_dial1 with graphics view
#     #                     # self.view = QGraphicsView(self.scene, self.ui.label_dial1.parent())
#     #                     # self.view.setGeometry(self.ui.label_dial1.geometry())
#     #                     # self.view.setStyleSheet("background: transparent; border: none;")

#     #                     # # Hide original labels
#     #                     # self.ui.label_dial1.hide()
#     #                     # self.ui.label_needle1.hide()

#     #                     # # Add Dial
#     #                     # self.dial_item = QGraphicsPixmapItem(
#     #                     #     QPixmap("/home/torizon/app/src/images/green_60_big.png")
#     #                     # )
#     #                     # self.scene.addItem(self.dial_item)

#     #                     # # Add Needle
#     #                     # self.needle_item = QGraphicsPixmapItem(
#     #                     #     QPixmap("/home/torizon/app/src/images/needle.png")
#     #                     # )
#     #                     # self.scene.addItem(self.needle_item)

#     #                     # # Center needle on dial
#     #                     # self.needle_item.setPos(78, 40)

#     #                     # # IMPORTANT → Set rotation pivot
#     #                     # self.needle_item.setTransformOriginPoint(
#     #                     #     4, 45                                  #self.needle_item.boundingRect().center()
#     #                     # )
#     #                     # # Animation variables
#     #                     # self.current_angle = 0
#     #                     # self.target_angle = 0
#     #                     # self.velocity = 0

#     #                     # self.spring_constant = 0.15
#     #                     # self.damping = 0.85

#     #                     # # Animation timer (~60 FPS)
#     #                     # self.animation_timer = QTimer(self)
#     #                     # self.animation_timer.timeout.connect(self.update_animation)
#     #                     # self.animation_timer.setInterval(16)

#     #                     # # Change angle every 1 second
#     #                     # self.change_timer = QTimer(self)
#     #                     # self.change_timer.timeout.connect(self.start_new_animation)
#     #                     # self.change_timer.start(1000)

#     #                     # # Stop after 20 seconds
#     #                     # self.stop_timer = QTimer(self)
#     #                     # self.stop_timer.setSingleShot(True)
#     #                     # self.stop_timer.timeout.connect(self.stop_animation)
#     #                     # self.stop_timer.start(60000)

#     #                     # self.start_new_animation()

                        
                        
#     #                     # self.ui.label_dial1.setScaledContents(True)
#     #                     # self.ui.label_dial1.setPixmap(QPixmap(u"/home/torizon/app/src/images/green_60_big.png"))
                        
                        
                        
#     #                     # self.ui.label_dial1.setMinimumSize(280, 200)
#     #                     # self.ui.label_value1.setMinimumSize(200, 0)
#     #                     # self.ui.label_value1.setMaximumSize(16777215, 70)
#     #                     # self.ui.label_status1.setMinimumSize(200, 0)
#     #                     # self.ui.label_status1.setMaximumSize(16777215, 70)
#     #                     # self.ui.button_mode1.setMinimumSize(80, 0)
#     #                     # self.ui.button_mode1.setMaximumSize(16777215, 55)
                        
#     #                     # self.ui.label_value1.setStyleSheet(u"font-size: 45pt;font-weight: bold;")
#     #                     # self.ui.label_status1.setStyleSheet(u"font-size: 45pt;font-weight: bold;")
                    
#     #                 elif self.ui.button_mode1.text() == 'Digit':
#     #                     self.ui.label_value1.setMinimumSize(300, 0)
#     #                     self.ui.label_value1.setMaximumSize(16777215, 320)
#     #                     self.ui.label_status1.setMinimumSize(180, 0)
#     #                     self.ui.label_status1.setMaximumSize(16777215, 100)
#     #                     self.ui.button_mode1.setMinimumSize(70, 0)
#     #                     self.ui.button_mode1.setMaximumSize(16777215, 60)
                        
#     #                     # self.ui.label_value1.setStyleSheet(u"font-size: 50pt;font-weight: bold;")
#     #                     # self.ui.label_status1.setStyleSheet(u"font-size: 40pt;font-weight: bold;")
#     #                     # self.ui.button_mode1.setStyleSheet(u"font-size: 40pt;font-weight: bold;")   
                    
                    
#     #                 self.ui.label_value1.show()
#     #                 self.ui.label_status1.show()
#     #                 self.ui.button_mode1.show() 
                    
#     #                 self.ui.label_dial2.hide()
#     #                 self.ui.label_dial3.hide()
#     #                 self.ui.label_dial4.hide()
                    
#     #                 self.ui.label_needle2.hide()
#     #                 self.ui.label_needle3.hide()
#     #                 self.ui.label_needle4.hide()
                    
#     #                 self.ui.label_status2.hide()
#     #                 self.ui.label_status3.hide()
#     #                 self.ui.label_status4.hide()
                        
#     #                 self.ui.label_value2.hide()
#     #                 self.ui.label_value3.hide()
#     #                 self.ui.label_value4.hide()
                        
#     #                 self.ui.button_mode2.hide()
#     #                 self.ui.button_mode3.hide()
#     #                 self.ui.button_mode4.hide()
                    
#     #                 # self.ui.widget_spc1.hide()
#     #                 # self.ui.widget_line2.hide()

#     #             elif self.channel_count == 2:
#     #                 if self.ui.button_mode1.text() == 'Dial' :
#     #                     self.ui.label_dial1.show()
#     #                     # self.ui.label_dial1.setMinimumSize(300, 0)
#     #                     # self.ui.label_dial1.setMaximumSize(16777215, 200)
                        
#     #                     # # self.ui.label_dial2.setMinimumSize(300, 0)
#     #                     # # self.ui.label_dial2.setMaximumSize(16777215, 200)
                        
#     #                     # self.ui.label_value1.setMinimumSize(210, 0)
#     #                     # self.ui.label_value1.setMaximumSize(16777215, 70)
                        
#     #                     # # self.ui.label_value1.setMaximumSize(16777215, 80)
#     #                     # self.ui.label_status1.setMinimumSize(120, 0)
#     #                     # self.ui.label_status1.setMaximumSize(16777215, 50)
                        
#     #                     # self.ui.button_mode1.setMinimumSize(80, 0)
#     #                     # self.ui.button_mode1.setMaximumSize(16777215, 30)

#     #                     self.ui.label_value1.setGeometry(QRect(40, 270, 290, 40))
#     #                     self.ui.button_mode1.setGeometry(QRect(280, 320, 101, 40))
#     #                     self.ui.label_dial1.setGeometry(QRect(0, -9, 360, 280))
#     #                     self.ui.label_status1.setGeometry(QRect(10, 320, 211, 35))

#     #                     # Create DialHandler once
#     #                     # self.ui.dial_1_anim = DialHandler(self.ui, 171, 65, 6, 117,self.ui.label_dial1,self.ui.label_needle1)
                        
#     #                 if self.ui.button_mode2.text() == 'Dial':
#     #                     self.ui.label_dial2.show()
#     #                     # self.ui.label_dial2.setMinimumSize(300, 0)
#     #                     # self.ui.label_dial2.setMaximumSize(16777215, 200)
                        
#     #                     # self.ui.label_dial2.setMinimumSize(300, 0)
#     #                     # self.ui.label_dial2.setMaximumSize(16777215, 200)
                        
#     #                     # self.ui.label_value2.setMinimumSize(210, 70)
#     #                     # self.ui.label_value2.setMaximumSize(16777215, 80)
#     #                     # self.ui.label_status2.setMinimumSize(120, 0)
#     #                     # self.ui.label_status2.setMaximumSize(16777215, 50)
#     #                     # self.ui.button_mode2.setMinimumSize(80, 0)
#     #                     # self.ui.button_mode2.setMaximumSize(16777215, 30)
                        
#     #                     # self.ui.label_dial2.setPixmap(QPixmap(u"/home/torizon/app/src/green_60_big.png"))
#     #                     # self.ui.label_value2.setStyleSheet(u"font-size: 35pt;font-weight: bold;")
#     #                     # self.ui.label_status2.setStyleSheet(u"font-size: 30pt;font-weight: bold;")
#     #                     # self.ui.button_mode2.setStyleSheet(u"font-size: 30pt;font-weight: bold;")

                        
#     #                     self.ui.label_value2.setGeometry(QRect(440, 270, 290, 40))
#     #                     self.ui.button_mode2.setGeometry(QRect(660, 320, 101, 40))
#     #                     self.ui.label_dial2.setGeometry(QRect(400, -9, 360, 280))
#     #                     self.ui.label_status2.setGeometry(QRect(430, 320, 211, 35))
                        
#     #                     # self.ui.label_value2.setGeometry(QRect(440, 280, 221, 40))
#     #                     # self.ui.button_mode2.setGeometry(QRect(660, 340, 101, 40))
#     #                     # self.ui.label_dial2.setGeometry(QRect(400, -9, 350, 250))
#     #                     # self.ui.label_status2.setGeometry(QRect(430, 250, 211, 35))

#     #                     # Create DialHandler once
#     #                     # self.ui.dial_2_anim = DialHandler(self.ui, 171, 65, 6, 117,self.ui.label_dial2,self.ui.label_needle2)
                    
#     #                 if self.ui.button_mode1.text() == 'Digit' : 
#     #                     self.ui.label_value1.setMinimumSize(300, 0)
#     #                     self.ui.label_value1.setMaximumSize(16777215, 220)
#     #                     self.ui.label_status1.setMinimumSize(180, 0)
#     #                     self.ui.label_status1.setMaximumSize(16777215, 100)
#     #                     self.ui.button_mode1.setMinimumSize(80, 0)
#     #                     self.ui.button_mode1.setMaximumSize(16777215, 30)
#     #                     # self.ui.label_value1.setStyleSheet(u"font-size: 40pt;font-weight: bold;")
#     #                     # self.ui.label_status1.setStyleSheet(u"font-size: 30pt;font-weight: bold;")
#     #                     # self.ui.button_mode1.setStyleSheet(u"font-size: 18pt;font-weight: bold;")

#     #                 if self.ui.button_mode2.text() == 'Digit':
#     #                     self.ui.label_value2.setMinimumSize(300, 0)
#     #                     self.ui.label_value2.setMaximumSize(16777215, 220)
#     #                     self.ui.label_status2.setMinimumSize(180, 0)
#     #                     self.ui.label_status2.setMaximumSize(16777215, 100)
#     #                     self.ui.button_mode2.setMinimumSize(80, 0)
#     #                     self.ui.button_mode2.setMaximumSize(16777215, 30)
#     #                     # self.ui.label_value2.setStyleSheet(u"font-size: 40pt;font-weight: bold;")
#     #                     # self.ui.label_status2.setStyleSheet(u"font-size: 30pt;font-weight: bold;")
#     #                     # self.ui.button_mode2.setStyleSheet(u"font-size: 18pt;font-weight: bold;")
                        
#     #                 self.ui.label_value2.show()
#     #                 self.ui.label_status2.show()
#     #                 self.ui.button_mode2.show()
                    
#     #                 self.ui.label_dial3.hide()
#     #                 self.ui.label_dial4.hide()

#     #                 self.ui.label_needle3.hide()
#     #                 self.ui.label_needle4.hide()

#     #                 self.ui.label_value3.hide()
#     #                 self.ui.label_value4.hide()

#     #                 self.ui.widget_spc3.hide()
#     #                 self.ui.widget_spc4.hide()

#     #                 self.ui.label_status3.hide()
#     #                 self.ui.label_status4.hide()
                        
#     #                 self.ui.button_mode3.hide()
#     #                 self.ui.button_mode4.hide()
                    
#     #                 # self.ui.widget_line2.hide()
                        
#     #             elif self.channel_count == 3:
                                         
#     #                 if self.ui.button_mode1.text() == 'Dial' :
#     #                     self.ui.label_dial1.show()
#     #                     self.ui.label_dial1.setMinimumSize(150, 100)
#     #                     # self.ui.label_dial1.setMaximumSize(16777215, 100)
                        
#     #                     # self.ui.label_value1.setStyleSheet(u"font-size: 20pt;font-weight: bold;")
#     #                     # self.ui.label_status1.setStyleSheet(u"font-size: 18pt;font-weight: bold;")
#     #                     self.ui.label_value1.setMinimumSize(150,30)
#     #                     # self.ui.label_value1.setMaximumSize(16777215, 30)
#     #                     self.ui.label_status1.setMinimumSize(170,30)
#     #                     # self.ui.label_value1.setMaximumSize(16777215, 30)
#     #                     self.ui.button_mode1.setMinimumSize(100,30)
#     #                     # self.ui.button_mode1.setMaximumSize(16777215, 30)
#     #                     # self.ui.button_mode1.setStyleSheet(u"font-size: 18pt;font-weight: bold;")
                        
#     #                 if self.ui.button_mode2.text() == 'Dial' : 
#     #                     self.ui.label_dial2.show()
#     #                     self.ui.label_dial2.setMinimumSize(150, 100)
#     #                     # self.ui.label_dial2.setMaximumSize(16777215, 100)
#     #                     # self.ui.label_value2.setStyleSheet(u"font-size: 20pt;font-weight: bold;")
#     #                     # self.ui.label_status2.setStyleSheet(u"font-size: 18pt;font-weight: bold;")
#     #                     self.ui.label_value2.setMinimumSize(150,30)
#     #                     # self.ui.label_value2.setMaximumSize(16777215, 30)
#     #                     self.ui.label_status2.setMinimumSize(170,30)
#     #                     # self.ui.label_status2.setMaximumSize(16777215, 30)
#     #                     self.ui.button_mode2.setMinimumSize(100,30)
#     #                     # self.ui.button_mode2.setMaximumSize(16777215, 30)
#     #                     # self.ui.button_mode2.setStyleSheet(u"font-size: 18pt;font-weight: bold;")
                        
#     #                 if self.ui.button_mode3.text() == 'Dial':
#     #                     self.ui.label_dial3.show()
#     #                     self.ui.label_dial3.setMinimumSize(150, 100)
#     #                     # self.ui.label_dial3.setMaximumSize(16777215, 100)
#     #                     # self.ui.label_value3.setStyleSheet(u"font-size: 20pt;font-weight: bold;")
#     #                     # self.ui.label_status3.setStyleSheet(u"font-size: 18pt;font-weight: bold;")
#     #                     self.ui.label_value3.setMinimumSize(160,30)
#     #                     # self.ui.label_value3.setMaximumSize(16777215, 30)
#     #                     self.ui.label_status3.setMinimumSize(170,30)
#     #                     # self.ui.label_status3.setMaximumSize(16777215, 30)
#     #                     self.ui.button_mode3.setMinimumSize(100,30)
#     #                     # self.ui.button_mode3.setMaximumSize(16777215, 30)
#     #                     # self.ui.button_mode3.setStyleSheet(u"font-size: 18pt;font-weight: bold;")
                        
#     #                 if self.ui.button_mode1.text() == 'Digit' : 
#     #                     self.ui.label_value1.setStyleSheet(u"font-size: 35pt;font-weight: bold;")
#     #                     self.ui.label_status1.setStyleSheet(u"font-size: 25pt;font-weight: bold;")
#     #                     self.ui.label_value1.setMinimumSize(250,60)
#     #                     # self.ui.label_value1.setMaximumSize(16777215, 60)
#     #                     self.ui.label_status1.setMinimumSize(200,60)
#     #                     # self.ui.label_status1.setMaximumSize(16777215, 30)
#     #                     self.ui.button_mode1.setMinimumSize(100,30)
#     #                     # self.ui.button_mode1.setMaximumSize(16777215, 30)
#     #                     self.ui.button_mode1.setStyleSheet(u"font-size: 18pt;font-weight: bold;")
                        
#     #                 if self.ui.button_mode2.text() == 'Digit': 
#     #                     self.ui.label_value2.setStyleSheet(u"font-size: 35pt;font-weight: bold;")
#     #                     self.ui.label_status2.setStyleSheet(u"font-size: 25pt;font-weight: bold;")
#     #                     self.ui.label_value2.setMinimumSize(250,60)
#     #                     # self.ui.label_value2.setMaximumSize(16777215, 60)
#     #                     self.ui.label_status2.setMinimumSize(200,60)
#     #                     # self.ui.label_status2.setMaximumSize(16777215, 30)
#     #                     self.ui.button_mode2.setMinimumSize(100,30)
#     #                     # self.ui.button_mode2.setMaximumSize(16777215, 30)
#     #                     self.ui.button_mode2.setStyleSheet(u"font-size: 18pt;font-weight: bold;")
                        
#     #                 if self.ui.button_mode3.text() == 'Digit' :
#     #                     self.ui.label_value3.setStyleSheet(u"font-size: 35pt;font-weight: bold;")
#     #                     self.ui.label_status3.setStyleSheet(u"font-size: 25pt;font-weight: bold;")
#     #                     self.ui.label_value3.setMinimumSize(350,90)
#     #                     # self.ui.label_value3.setMaximumSize(16777215, 90)
#     #                     self.ui.label_status3.setMinimumSize(270,30)
#     #                     # self.ui.label_status3.setMaximumSize(16777215, 30)
#     #                     self.ui.button_mode3.setMinimumSize(100,30)
#     #                     # self.ui.button_mode3.setMaximumSize(16777215, 30)
#     #                     self.ui.button_mode3.setStyleSheet(u"font-size: 18pt;font-weight:bold")
                    
#     #                 self.ui.label_value3.show()
#     #                 self.ui.label_status3.show()
#     #                 self.ui.button_mode3.show()
                    
#     #                 self.ui.label_dial4.hide()
#     #                 self.ui.label_value4.hide()
#     #                 self.ui.label_status4.hide()
#     #                 self.ui.button_mode4.hide()
                        
#     #             else:   
#     #                 if self.ui.button_mode1.text() == 'Dial' :
#     #                     self.ui.label_dial1.show()
#     #                     self.ui.label_value1.setStyleSheet(u"font-size: 20pt;font-weight: bold;")
#     #                     self.ui.label_status1.setStyleSheet(u"font-size: 15pt;font-weight: bold;")
#     #                     self.ui.label_value1.setMinimumSize(160,30)
#     #                     # self.ui.label_value1.setMaximumSize(16777215, 40)
#     #                     self.ui.label_status1.setMinimumSize(150,30)
#     #                     # self.ui.label_status1.setMaximumSize(16777215, 30)
#     #                     self.ui.label_dial1.setMinimumSize(100,40)
#     #                     # self.ui.label_dial1.setMaximumSize(16777215, 50)
#     #                     self.ui.button_mode1.setMinimumSize(100,30)
#     #                     # self.ui.button_mode1.setMaximumSize(16777215, 30)
#     #                     self.ui.button_mode1.setStyleSheet(u"font-size: 18pt;font-weight: bold;")
                    
#     #                 if self.ui.button_mode2.text() == 'Dial' :
#     #                     self.ui.label_dial2.show()
#     #                     self.ui.label_value2.setStyleSheet(u"font-size: 20pt;font-weight: bold;")
#     #                     self.ui.label_status2.setStyleSheet(u"font-size: 15pt;font-weight: bold;")
#     #                     self.ui.label_value2.setMinimumSize(160,30)
#     #                     # self.ui.label_value2.setMaximumSize(16777215, 40)
#     #                     self.ui.label_status2.setMinimumSize(150,30)
#     #                     # self.ui.label_status2.setMaximumSize(16777215, 30)
#     #                     self.ui.label_dial2.setMinimumSize(100,40)
#     #                     # self.ui.label_dial2.setMaximumSize(16777215, 50)
#     #                     self.ui.button_mode2.setMinimumSize(100,30)
#     #                     # self.ui.button_mode2.setMaximumSize(16777215, 30)
#     #                     self.ui.button_mode2.setStyleSheet(u"font-size: 18pt;font-weight: bold;")
                    
#     #                 if self.ui.button_mode3.text() == 'Dial' :
#     #                     self.ui.label_dial3.show()    
#     #                     self.ui.label_value3.setStyleSheet(u"font-size: 20pt;font-weight: bold;")
#     #                     self.ui.label_status3.setStyleSheet(u"font-size: 15pt;font-weight: bold;")
#     #                     self.ui.label_value3.setMinimumSize(160,30)
#     #                     # self.ui.label_value3.setMaximumSize(16777215, 40)
#     #                     self.ui.label_status3.setMinimumSize(150,30)
#     #                     # self.ui.label_status3.setMaximumSize(16777215, 30)
#     #                     self.ui.label_dial3.setMinimumSize(100,40)
#     #                     # self.ui.label_dial3.setMaximumSize(16777215, 50)
#     #                     self.ui.button_mode3.setMinimumSize(100,30)
#     #                     # self.ui.button_mode3.setMaximumSize(16777215, 30)
#     #                     self.ui.button_mode3.setStyleSheet(u"font-size: 18pt;font-weight: bold;")
                        
#     #                 if self.ui.button_mode4.text() == 'Dial':   
#     #                     self.ui.label_dial4.show()
#     #                     self.ui.label_value4.setStyleSheet(u"font-size: 20pt;font-weight: bold;")
#     #                     self.ui.label_status4.setStyleSheet(u"font-size: 15pt;font-weight: bold;")
#     #                     self.ui.label_value4.setMinimumSize(160,30)
#     #                     # self.ui.label_value4.setMaximumSize(16777215, 40)
#     #                     self.ui.label_status4.setMinimumSize(150,30)
#     #                     # self.ui.label_status4.setMaximumSize(16777215, 30)
#     #                     self.ui.label_dial4.setMinimumSize(100,40)
#     #                     # self.ui.label_dial4.setMaximumSize(16777215, 50)
#     #                     self.ui.button_mode4.setMinimumSize(100,30)
#     #                     # self.ui.button_mode4.setMaximumSize(16777215, 30)
#     #                     self.ui.button_mode4.setStyleSheet(u"font-size: 18pt;font-weight: bold;")
                        
#     #                 if self.ui.button_mode1.text() == 'Digit' :
#     #                     self.ui.label_value1.setStyleSheet(u"font-size: 30pt;font-weight: bold;")
#     #                     self.ui.label_status1.setStyleSheet(u"font-size: 20pt;font-weight: bold;")
#     #                     self.ui.label_value1.setMinimumSize(220,100)
#     #                     # self.ui.label_value1.setMaximumSize(16777215, 100)

#     #                     self.ui.label_status1.setMinimumSize(200,30)
#     #                     # self.ui.label_status1.setMaximumSize(16777215, 30)

#     #                     self.ui.button_mode1.setMinimumSize(100,30)
#     #                     # self.ui.button_mode1.setMaximumSize(16777215, 30)
#     #                     self.ui.button_mode1.setStyleSheet(u"font-size: 18pt;font-weight: bold;")
                    
#     #                 if self.ui.button_mode2.text() == 'Digit' :
#     #                     self.ui.label_value2.setStyleSheet(u"font-size: 30pt;font-weight: bold;")
#     #                     self.ui.label_status2.setStyleSheet(u"font-size: 20pt;font-weight: bold;")
#     #                     self.ui.label_value2.setMinimumSize(250,100)
#     #                     # self.ui.label_value2.setMaximumSize(16777215, 100)
#     #                     self.ui.label_status2.setMinimumSize(200,30)
#     #                     # self.ui.label_status2.setMaximumSize(16777215, 30)
#     #                     self.ui.button_mode2.setMinimumSize(100,30)
#     #                     # self.ui.button_mode2.setMaximumSize(16777215, 30)
#     #                     self.ui.button_mode2.setStyleSheet(u"font-size: 18pt;font-weight: bold;")
                        
#     #                 if self.ui.button_mode3.text() == 'Digit' :   
#     #                     self.ui.label_value3.setStyleSheet(u"font-size: 30pt;font-weight: bold;")
#     #                     self.ui.label_status3.setStyleSheet(u"font-size: 20pt;font-weight: bold;")
#     #                     self.ui.label_value3.setMinimumSize(220,100)
#     #                     # self.ui.label_value3.setMaximumSize(16777215, 100)
#     #                     self.ui.label_status3.setMinimumSize(200,30)
#     #                     # self.ui.label_status3.setMaximumSize(16777215, 30)
#     #                     self.ui.button_mode3.setMinimumSize(100,30)
#     #                     # self.ui.button_mode3.setMaximumSize(16777215, 30)
#     #                     self.ui.button_mode3.setStyleSheet(u"font-size: 18pt;font-weight: bold;")
                        
#     #                 if self.ui.button_mode4.text() == 'Digit':    
#     #                     self.ui.label_value4.setStyleSheet(u"font-size: 30pt;font-weight: bold;")
#     #                     self.ui.label_status4.setStyleSheet(u"font-size: 20pt;font-weight: bold;")
#     #                     self.ui.label_value4.setMinimumSize(220,100)
#     #                     # self.ui.label_value4.setMaximumSize(16777215, 100)
#     #                     self.ui.label_status4.setMinimumSize(200,30)
#     #                     # self.ui.label_status4.setMaximumSize(16777215, 30)
#     #                     self.ui.button_mode4.setMinimumSize(100,30)
#     #                     # self.ui.button_mode4.setMaximumSize(16777215, 30)
#     #                     self.ui.button_mode4.setStyleSheet(u"font-size: 18pt;font-weight: bold;")
                        
#     #                 self.ui.label_value4.show()
#     #                 self.ui.label_status4.show()
#     #                 self.ui.button_mode4.show()


#     #     except Exception as e:
#     #         print(f"Error in Dial Indicator : {e}") 
      
#     def hide_labels(self):
#         for i in range(1,5):
#             getattr(self.ui, f"widget_spc{i}").hide()
#             getattr(self.ui, f"label_dial{i}").show()
#             getattr(self.ui, f"label_status{i}").show()
#             getattr(self.ui, f"label_value{i}").show()
#             getattr(self.ui, f"label_needle{i}").hide()
#             getattr(self.ui, f"button_mode{i}").show()
       


# # class SPCWorker(QThread):
# #     data_signal = Signal(int, float)

# #     def __init__(self):
# #         super().__init__()
# #         self.queue = deque()
# #         self.running = True

# #     def add_data(self, ch, val):
# #         self.queue.append((ch, val))

# #     def run(self):
# #         while self.running:
# #             if self.queue:
# #                 ch, val = self.queue.popleft()
# #                 self.data_signal.emit(ch, val)
# #             self.msleep(1)   # 🔥 control speed

# #     def stop(self):
# #         self.running = False       
              
# class SPCBase:
#         def __init__(self, title, lol, lsl, lcl, nominal, ucl, usl, uol):
#             try:
#                 self.title = title
#                 self.limits = [lol, lsl, lcl, nominal, ucl, usl, uol]
#                 self.spc_count = 50
#                 self.data_raw = []

#                 self.fig = Figure()
#                 self.canvas = FigureCanvas(self.fig)
#                 self.ax = self.fig.add_subplot(111)
                
#                 range_val = uol - lol
#                 self.padding = max(range_val * 0.2, 0.001)

#                 # Dark theme
#                 self.fig.patch.set_facecolor("#2b2b2b")
#                 self.ax.set_facecolor("#2b2b2b")
#                 self.x_data = list(range(1, self.spc_count + 1))
#                 self.y_data = [np.nan] * self.spc_count
#                 self.init_blank_ui()

#             except Exception as e:
#                 print(f"Error SPC init -> {e}")

#         # ---------------- RESET ----------------
#         def reset_graph(self):
#             self.data_raw = []   # 🔥 IMPORTANT
#             self.y_data = [np.nan] * self.spc_count

#             x_full = list(range(1, self.spc_count + 1))
#             self.line.set_data(x_full, self.y_data)

#             self.canvas.draw_idle()

#         # ---------------- LIMIT SET ----------------
#         def set_limits(self, lol, lsl, lcl, nominal, ucl, usl, uol):
#             self.limits = [lol, lsl, lcl, nominal, ucl, usl, uol]
#             self.init_blank_ui()

#         # ---------------- MAIN UI ----------------
#         def init_blank_ui(self):
#             try:
#                 self.ax.clear()

#                 lol, lsl, lcl, nominal, ucl, usl, uol = self.limits
#   # minimum padding safety

#                 # self.ax.set_ylim(lol - self.padding, uol + self.padding)

#                 # ---------- LIMIT LINES ----------
#                 self.ax.axhline(usl, color='red', linestyle='--', linewidth=1.5)
#                 self.ax.axhline(lsl, color='red', linestyle='--', linewidth=1.5)

#                 self.ax.axhline(nominal, color='green', linestyle='--', linewidth=1.5)
#                 self.ax.axhline(ucl, color='green', linestyle=':', linewidth=1.5)
#                 self.ax.axhline(lcl, color='green', linestyle=':', linewidth=1.5)

#                 if uol != 0 and lol != 0:
#                     self.ax.axhline(uol, color='red', linestyle='-.', linewidth=1.5)
#                     self.ax.axhline(lol, color='red', linestyle='-.', linewidth=1.5)

#                 # ---------- BACKGROUND COLORS ----------
#                 if uol != 0 and lol != 0:
#                     self.ax.axhspan(lsl, lol, color='red', alpha=0.9)
#                     self.ax.axhspan(usl, uol, color='red', alpha=0.9)

#                 self.ax.axhspan(lsl, lcl, color='yellow', alpha=0.9)
#                 self.ax.axhspan(lcl, nominal, color='green', alpha=0.9)
#                 self.ax.axhspan(nominal, ucl, color='green', alpha=0.9)
#                 self.ax.axhspan(ucl, usl, color='yellow', alpha=0.9)

#                 # ---------- EMPTY GRAPH ----------
#                 self.line, = self.ax.plot(self.x_data, self.y_data, color="blue", marker="o", linewidth=2)

#                 # ---------- Y TICKS ----------
#                 # yticks = [lsl, lcl, (lcl + ucl) / 2, ucl, usl]
#                 yticks = [lsl, lcl, nominal, ucl, usl]

#                 if uol != 0 and lol != 0:
#                     yticks.insert(0, lol)
#                     yticks.append(uol)

#                 self.ax.set_yticks(yticks)
#                 # self.ax.set_xticks(self.get_dynamic_xticks())

#                 # FIX DECIMAL DISPLAY
#                 labels = [("{:.5f}".format(v)).rstrip('0').rstrip('.') for v in yticks]
#                 self.ax.set_yticklabels(labels, color="white")

       
#                 # ---------- AXIS FIX ----------
#                 self.ax.set_xlim(1, self.spc_count)
#                 self.ax.set_xticks(self.get_dynamic_xticks())

#                 self.ax.set_ylim(lol - self.padding, uol + self.padding)

#                 self.ax.set_autoscale_on(False)
#                 self.ax.autoscale(False)
#                 # ---------- TITLE ----------
#                 self.ax.set_title(self.title, color="white", fontsize=10, fontweight="bold")

#                 # ---------- AXIS STYLE ----------
#                 self.ax.tick_params(axis='x', colors='white')
#                 self.ax.tick_params(axis='y', colors='white')

#                 self.ax.grid(False)

#                 self.canvas.draw_idle()

#             except Exception as e:
#                 print(f"Error init UI -> {e}")
                
#         def clamp_value(self, value):
#             try:
#                 lol, lsl, lcl, nominal, ucl, usl, uol = self.limits

#                 if value > uol:
#                     return uol
#                 elif value < lol:
#                     return lol
#                 return value
#             except Exception as e:
#                 print(f"Error in clamp_value - > {e}")
#         # ---------------- GRAPH LOAD ----------------
#         def generate_graph(self, raw_data):
#             try:
#                 # keep only last 50
#                 raw_data = raw_data[-self.spc_count:]

#                 # ✅ store ONLY real data (no NaN padding)
#                 self.data_raw = [self.clamp_value(v) for v in raw_data]

#                 y_full = [np.nan] * self.spc_count

#                 for i, v in enumerate(self.data_raw):
#                     y_full[i] = v

#                 x_full = list(range(1, self.spc_count + 1))

#                 self.line.set_data(x_full, y_full)

#                 self.canvas.draw_idle()

#             except Exception as e:
#                 print(f"Error in Generate_graph function -> {e}")
#         # def generate_graph(self, raw_data):
#         #     try:
#         #         # keep only last 50
#         #         raw_data = raw_data[-self.spc_count:]
#         #         # self.data_raw = raw_data
                
#         #         # x = list(range(1, len(raw_data) + 1))
#         #         # y = [self.clamp_value(v) for v in raw_data]
#         #         # self.data_raw = y
                
#         #         y_full = [np.nan] * self.spc_count

#         #         for i, v in enumerate(raw_data):
#         #             y_full[i] = self.clamp_value(v)
                
                
#         #         x_full = list(range(1, self.spc_count + 1))
#         #         self.data_raw = y_full
#         #         self.line.set_data(x_full, y_full)

#         #         self.canvas.draw_idle()

#         #     except Exception as e:
#         #         print(f"Error in Generate_graph function -> {e}")

#         def update_graph(self, value):
#             value = self.clamp_value(value)  
#             self.data_raw.append(value)

#             if len(self.data_raw) > self.spc_count:
#                 self.data_raw = self.data_raw[-self.spc_count:]

#             y = self.data_raw
#             x = list(range(1, len(y) + 1))   # 🔥 dynamic

#             self.line.set_data(x, y)

#             self.ax.set_xlim(1, max(len(x), self.spc_count))
#             self.ax.set_xticks(x[::max(1, len(x)//5)])  # clean ticks

#             self.canvas.draw_idle()

#         def get_dynamic_xticks(self):
#             try:
#                 if self.spc_count <= 10:
#                     ticks = list(range(1, self.spc_count + 1))

#                 elif self.spc_count <= 20:
#                     ticks = list(range(1, self.spc_count + 1, 2))

#                 else:
#                     ticks = list(range(1, self.spc_count + 1, 5))

#                 # 🔥 ALWAYS include 50
#                 if self.spc_count not in ticks:
#                     ticks.append(self.spc_count)

#                 return ticks
#             except Exception as e:
#                 print(f"Error in get_dynamic_xticks ->{e}")

#         # ---------------- MARGINS ----------------
#         def set_margins(self, left, right, top, bottom):
#             self.fig.subplots_adjust(left=left, right=right, top=top, bottom=bottom)
#             self.canvas.draw_idle()
            
#         def __del__(self):
#             """Destructor: safely close the Matplotlib figure to free memory."""
#             try:
#                 self.canvas.close(self.fig)
#             except Exception:
#                 pass   
        
# class SPCWidget(QWidget):
#     def __init__(self, spc, parent=None):
#         try:
#             super().__init__(parent)
#             self.spc = spc

#             layout = QVBoxLayout(self)
#             layout.setContentsMargins(0, 0, 0, 0)
#             layout.setSpacing(2)

#             # self.spc.canvas.setMinimumHeight(130)
#             # ---- graph ----
#             self.spc.canvas.setSizePolicy(
#                 QSizePolicy.Expanding,
#                 QSizePolicy.Preferred   
#             )
#             layout.addWidget(self.spc.canvas, 1)
#         except Exception as e:
#             print(f"error in SPCWidget -> {e}")


#     def load_value(self, value):
#         try:
#             self.spc.update_graph(value)
#         except Exception as e:
#             print(f"error in load_value -> {e}")
            
#     def reset(self):
#         self.spc.reset_graph()
        
           
# class SPCManager:
#     def __init__(self, main_window):
#         try:
#             self.ui = main_window
            
        
#             self.spc_all = {
#             1: SPCWidget(SPCBase("D1", lol=20.000,lsl=20.010,lcl=20.015,nominal=20.020,ucl=20.025,usl=20.030,uol=20.042)),
#             2: SPCWidget(SPCBase("D2", lol=20.000,lsl=20.010,lcl=20.015,nominal=20.020,ucl=20.025,usl=20.030,uol=20.042)),
#             3: SPCWidget(SPCBase("D3", lol=20.000,lsl=20.010,lcl=20.015,nominal=20.020,ucl=20.025,usl=20.030,uol=20.042)),
#             4: SPCWidget(SPCBase("D4", lol=20.000,lsl=20.010,lcl=20.015,nominal=20.020,ucl=20.025,usl=20.030,uol=20.042)),
#             }

#             self.active_channels = []
            
#             # Initialize spc_1, spc_2, spc_3, spc_4 to None first
#             self.spc_1 = None
#             self.spc_2 = None
#             self.spc_3 = None
#             self.spc_4 = None
            
#             self.layout_initialized = False
            
#             # self.ui.label_dial1.hide()
#             # self.ui.label_needle1.hide()
            
#             # ✅ CREATE layouts if not exists
#             self._ensure_layout(self.ui.widget_spc1)
#             self._ensure_layout(self.ui.widget_spc2)
#             self._ensure_layout(self.ui.widget_spc3)
#             self._ensure_layout(self.ui.widget_spc4)

#             # now layouts will NOT be None - get layouts with safe access
#             widget_spc1_layout = self.ui.widget_spc1.layout()
#             widget_spc2_layout = self.ui.widget_spc2.layout()
#             widget_spc3_layout = self.ui.widget_spc3.layout()
#             widget_spc4_layout = self.ui.widget_spc4.layout()
            
#             if widget_spc1_layout is not None:
#                 self.spc_1 = widget_spc1_layout
#             if widget_spc2_layout is not None:
#                 self.spc_2 = widget_spc2_layout
#             if widget_spc3_layout is not None:
#                 self.spc_3 = widget_spc3_layout
#             if widget_spc4_layout is not None:
#                 self.spc_4 = widget_spc4_layout
            
#             self.ui.button_spcReset.clicked.connect(self.reset_all_spc)
#             # self.worker = SPCWorker()
#             # # if self.ui.stacked.currentIndex() == 25:           
#             # self.worker.data_signal.connect(self.update_value)  # SAFE UI
#             # self.worker.start()
#             # else:
#             #     self.worker.stop()
#             #     self.worker.wait()
#             # self.ui.data_handler.probe_setttings_saved.connect(
#             #     self.load_spc
#             # )
#             # self.ui.data_handler.probe_setttings_saved.connect(self.load_spc)
#             self.last_reset_counter = 0
#         except Exception as e:
#             print(f"Error in intialization of SPCManager :-> {e}")
            
#     def load_spc(self):
#         try:
#             progId = int(self.ui.valueObj.activeVariables_dict["ActiveProgramId"])

#             self.load_program_OnSpc(progId)
#         except Exception as e:
#             print(f"Error while loading_spc -> {e}")
            
#     def get_decimals(self,lc):
#         try:
#             s = str(lc)
#             return len(s.split('.')[1]) if '.' in s else 0
#         except Exception as e:
#             print(f"Error in get_decimals {e}")
    
#     def _ensure_layout(self, widget):
#         try:
#             if widget.layout() is None:
#                 layout = QVBoxLayout(widget)
#                 layout.setContentsMargins(0, 0, 0, 0)
#                 widget.setLayout(layout)
#         except Exception as e:
#             print(f"Error in _ensure_layout {e}")
            
#     def reset_all_spc(self):
#         try:
#             probe_id = int(self.ui.valueObj.activeVariables_dict["ActiveProgramId"])

#             # 🔥 DELETE FROM DB
#             self.ui.savedbObj.reset_spc_for_probe(probe_id)
#             for ch in self.active_channels:
#                 spc_widget = self.spc_all.get(ch)
#                 if spc_widget:
#                     spc_widget.reset()
#                     self.is_spc_reset = True
#         except Exception as e:
#             print(f"Reset SPC error -> {e}")
            

#     def load_program_OnSpc(self, program_id: int):
#         session = SessionLocal()
#         try:
#             # 🔥 ONE query only
#             probe_rows = session.query(ProbeBasedSettings)\
#                 .filter(ProbeBasedSettings.ProgramId == program_id)\
#                 .all()

#             aoc_rows = session.query(AOCBasedSettings)\
#                 .filter(AOCBasedSettings.ProgramId == program_id)\
#                 .all()

#             probe_map = {row.Dimension: row for row in probe_rows}
#             aoc_map = {row.Dimension: row for row in aoc_rows}

#             AocState = self.ui.valueObj.activeVariables_dict["AOCOnOff"]

#             for ch, spc_widget in self.spc_all.items():
#                 dim = f"D{ch}"
#                 row = probe_map.get(dim)

#                 if not row:
#                     continue

#                 row_Aoc = aoc_map.get(dim)

#                 decimals = self.get_decimals(row.LeastCount)

#                 lsl = round(row.LowerSpecificationLimit, decimals)
#                 usl = round(row.UpperSpecificationLimit, decimals)

#                 range_val = usl - lsl
#                 margin = round(range_val * 0.3, decimals)

#                 lol_probe = round(lsl - margin, decimals)
#                 uol_probe = round(usl + margin, decimals)

#                 if AocState == "ON" and row_Aoc:
#                     spc_widget.spc.set_limits(
#                         lol=round(row_Aoc.LowerOffsetLimit, decimals),
#                         lsl=lsl,
#                         lcl=round(row.LowerControlLimit, decimals),
#                         nominal=round(row.NominalValue, decimals),
#                         ucl=round(row.UpperControlLimit, decimals),
#                         usl=usl,
#                         uol=round(row_Aoc.UpperOffsetLimit, decimals)
#                     )
#                 else:
#                     spc_widget.spc.set_limits(
#                         lol=lol_probe,
#                         lsl=lsl,
#                         lcl=round(row.LowerControlLimit, decimals),
#                         nominal=round(row.NominalValue, decimals),
#                         ucl=round(row.UpperControlLimit, decimals),
#                         usl=usl,
#                         uol=uol_probe
#                     )

#         finally:
#             session.close()
            
#     def load_data(self, channels):
#         try:

#             program_dict = self.ui.valueObj.ProgramSettings_dict

#             for dim in channels:

#                 probe_settings = program_dict.get(dim, {}).get("ProbeBasedSettings")

#                 if not probe_settings:
#                     continue

#                 probe_id =  int(self.ui.valueObj.activeVariables_dict["ActiveProgramId"])

#                 if not probe_id:
#                     continue

#                 values = self.ui.savedbObj.get_probe_values_for_spc(probe_id)

#                 if not values:
#                     continue

#                 values.reverse()   # oldest first

#                 channel = int(dim[1])  # D1 → 1

#                 self.spc_all[channel].spc.generate_graph(values)
#         except Exception as e:
#             print(f"Error in loading spc last Values - > {e}")
                
#     #clear layout for first time
#     def clear_layout(self, layout):
#         try:
#             if layout is None:
#                 return
#             while layout.count():
#                 item = layout.takeAt(0)
#                 if item.widget():
#                     item.widget().setParent(None)
#         except Exception as e:
#             print(f"Error in clear_layout:-> {e}")

#     #set active channels
#     def set_active_channels(self, channels):
#         try:
#             self.active_channels = list(range(1, channels + 1))
#             self.apply_layout()
#         except Exception as e:
#             print(f"Error for setting active channel as-> {e}")

#     #manage layout as per spc instance
    
#     def apply_layout(self):
#         try:
#             # ensure layouts
#             if self.spc_1 is None:
#                 self._ensure_layout(self.ui.widget_spc1)
#                 self.spc_1 = self.ui.widget_spc1.layout()
#             if self.spc_2 is None:
#                 self._ensure_layout(self.ui.widget_spc2)
#                 self.spc_2 = self.ui.widget_spc2.layout()
#             if self.spc_3 is None:
#                 self._ensure_layout(self.ui.widget_spc3)
#                 self.spc_3 = self.ui.widget_spc3.layout()
#             if self.spc_4 is None:
#                 self._ensure_layout(self.ui.widget_spc4)
#                 self.spc_4 = self.ui.widget_spc4.layout()

#             # ✅ ALWAYS DEFINE THIS
#             spcs = [self.spc_all[ch] for ch in self.active_channels]
#             count = len(spcs)

#             # ✅ ADD WIDGETS ONLY ONCE
#             if not self.layout_initialized:

#                 for layout in (self.spc_1, self.spc_2, self.spc_3, self.spc_4):
#                     if layout is not None:
#                         self.clear_layout(layout)

#                 if count >= 1 and self.spc_1:
#                     self.spc_1.addWidget(spcs[0])

#                 if count >= 2 and self.spc_2:
#                     self.spc_2.addWidget(spcs[1])

#                 if count >= 3 and self.spc_3:
#                     self.spc_3.addWidget(spcs[2])

#                 if count >= 4 and self.spc_4:
#                     self.spc_4.addWidget(spcs[3])

#                 self.layout_initialized = True

#             # ---------------- UI LOGIC ----------------
#             self.ui.label_dial1.hide()
#             # self.ui.label_needle1.hide()
#             self.ui.label_dial2.hide()
#             # self.ui.label_needle2.hide()
#             self.ui.label_dial3.hide()
#             # self.ui.label_needle3.hide()
#             self.ui.label_dial4.hide()
#             # self.ui.label_needle4.hide()
            

#             # ---------------- USE count safely ----------------
#             if count == 1:
#                 spcs[0].spc.canvas.setMinimumHeight(150)
#                 if self.ui.button_mode1.text() == 'SPC' :
#                     self.ui.widget_spc1.show()
#                     self.ui.widget_spc1.setGeometry(0, -10, 771, 241)

#             elif count == 2:
#                 for spc in spcs:
#                     spc.spc.canvas.setMinimumHeight(150)
#                 if self.ui.button_mode1.text() == 'SPC' :
#                     self.ui.widget_spc1.show()
#                     self.ui.widget_spc1.setGeometry(QRect(0, -10, 771, 150))
#                     self.ui.label_value1.setGeometry(QRect(80, 140,221, 20))
#                     self.ui.label_status1.setGeometry(QRect(75,170,211,20))
#                     self.ui.button_mode1.setGeometry(QRect(300,170,101,20))
#                 if self.ui.button_mode2.text() == 'SPC' :
#                     self.ui.widget_spc2.show()
#                     # self.ui.widget_spc3.setGeometry(0, 180, 771, 230)
#                     self.ui.widget_spc2.setGeometry(QRect(0, 185, 771, 150))
#                     self.ui.label_value2.setGeometry(QRect(80, 330,221, 20))
#                     self.ui.label_status2.setGeometry(QRect(75,350,211,20))
#                     self.ui.button_mode2.setGeometry(QRect(300,350,101,20))

#             elif count == 3:
#                 for spc in spcs:
#                     spc.spc.canvas.setMinimumHeight(120)
#                 if self.ui.button_mode1.text() == 'SPC' :
#                     self.ui.widget_spc1.show()
#                 if self.ui.button_mode2.text() == 'SPC' :
#                     self.ui.widget_spc2.show()
#                 if self.ui.button_mode3.text() == 'SPC' :
#                     self.ui.widget_spc3.show()
#                 # if self.ui.button_mode2.text() == 'SPC' :
#                     # self.ui.widget_spc1.show()

#             elif count == 4:
#                 for spc in spcs:
#                     spc.spc.canvas.setMinimumHeight(100)
#                 if self.ui.button_mode1.text() == 'SPC' :
#                     self.ui.widget_spc1.show()
#                 if self.ui.button_mode2.text() == 'SPC' :
#                     self.ui.widget_spc2.show()
#                 if self.ui.button_mode3.text() == 'SPC' :
#                     self.ui.widget_spc3.show()
#                 if self.ui.button_mode4.text() == 'SPC' :
#                     self.ui.widget_spc4.show()
#         except Exception as e:
#             print(f"Error while applying layout -> {e}")      
 
#     #update value on spc chanrt as per active channels
#     def update_value(self, channel, value):
#         try:
#             if channel not in self.active_channels:
#                 return

#             spc_widget = self.spc_all.get(channel)
#             if not spc_widget:
#                 return

#             spc_widget.load_value(value)
#         except Exception as e:
#             print(f"Error update value in graph -> {e}")
#             msg = CustomMessageBox("Failed to update value on Graph", "error",
#                                    parent=self.ui)
#             msg.exec_()
    