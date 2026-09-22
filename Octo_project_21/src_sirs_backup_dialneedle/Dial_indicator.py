from PySide2.QtWidgets import QHBoxLayout, QWidget
from PySide2.QtCore import QTimer, QTime, QSize, QObject , Qt, QCoreApplication,QMetaObject
from PySide2.QtGui import QPixmap, QFont
from sqlalchemy.orm import *
from models import *
from active_ui_handler import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PySide2.QtWidgets import (QApplication, QHBoxLayout, QMainWindow, QLabel,QSizePolicy,
    QVBoxLayout, QWidget)
from models import SessionLocal , ProbeBasedSettings
from messageBox import CustomMessageBox

import random
from PySide2.QtWidgets import QApplication, QWidget, QLabel
from PySide2.QtGui import QPixmap, QPainter, QTransform, QPaintEvent
from PySide2.QtCore import QTimer, Qt

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
            
            self.ui.data_handler.dialVisibilityChanged.connect(
            self.set_visibility
            )

            self.angle = 0
            self.target_angle = 0
            self.timer = QTimer(self)
            self.timer.timeout.connect(self.update_rotation)
            self.timer.start(10)  # Update every 16ms for smooth animation (~60fps)

            # Stop after 5 seconds
            QTimer.singleShot(10000, self.timer.stop)

        except Exception as e:
            print(f"Error in initializtion of Dial_Indicator : {e}")
    
      
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

    def update_rotation(self):
        if abs(self.angle - self.target_angle) < 1:
            self.target_angle = random.uniform(-90, 90)
        self.angle += (self.target_angle - self.angle) * 0.1  # Smooth interpolation
        # self.update()
        self.refresh_needle()

    def refresh_needle(self):
        """Call this method to manually trigger a repaint of the needle."""
        event = QPaintEvent(self.ui.label_dial1.rect())
        self.paintEvent(event)

    def paintEvent(self, event):
        painter = QPainter(self.ui)

        # Draw dial
        painter.drawPixmap(0, 0, self.ui.label_dial1.pixmap().scaled(self.size(), Qt.KeepAspectRatio))

        # Calculate center for needle (lower center of dial)
        dial_center_x = self.width() // 2
        dial_center_y = self.height() * 3 // 4  # Lower center

        # Rotate needle, pivoting at the bottom center of the needle
        transform = QTransform()
        transform.translate(dial_center_x, dial_center_y)
        transform.rotate(self.angle)
        transform.translate(-self.ui.label_needle1.pixmap().width() // 2, -self.ui.label_needle1.pixmap().height())

        painter.setTransform(transform)
        painter.drawPixmap(0, 0, self.ui.label_needle1.pixmap())

    #to enable disable line while switching combobox of Ovality ON and OFF
    def set_visibility(self):
        return
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
            
            channels=self.app.get_channels_for_program(
                int(self.ui.valueObj.activeVariables_dict["ActiveProgramId"])
            )
            channel_count = len(channels)
            print(f"channel in set visibilty {channel_count}")
    
            # if self.ui.button_mode1.text() == 'SPC':
            #     if self.spc_manager:
            #         self.spc_manager.set_active_channels(channel_count)
            # if self.ui.button_mode2.text() == 'SPC':
            #     if self.spc_manager:
            #         self.spc_manager.set_active_channels(channel_count)
            # if self.ui.button_mode3.text() == 'SPC':
            #     if self.spc_manager:
            #         self.spc_manager.set_active_channels(channel_count)
            # if self.ui.button_mode4.text() == 'SPC':
            #     if self.spc_manager:
            #         self.spc_manager.set_active_channels(channel_count)
            
            # else:
            if (True):
                if channel_count == 0 or None :
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
                        
                elif channel_count == 1:
                    if self.ui.button_mode1.text() == 'Dial':
                        self.ui.label_dial1.show()
                        self.ui.label_dial1.setMinimumSize(280, 200)
                        self.ui.label_value1.setMinimumSize(200, 0)
                        self.ui.label_value1.setMaximumSize(16777215, 70)
                        self.ui.label_status1.setMinimumSize(200, 0)
                        self.ui.label_status1.setMaximumSize(16777215, 70)
                        self.ui.button_mode1.setMinimumSize(80, 0)
                        self.ui.button_mode1.setMaximumSize(16777215, 55)
                        self.ui.label_dial1.setPixmap(QPixmap(u"/home/torizon/app/src/green_60_big.png"))
                        
                        # self.ui.label_value1.setStyleSheet(u"font-size: 45pt;font-weight: bold;")
                        # self.ui.label_status1.setStyleSheet(u"font-size: 45pt;font-weight: bold;")
                    
                    elif self.ui.button_mode1.text() == 'Digit':
                        self.ui.label_value1.setMinimumSize(300, 0)
                        self.ui.label_value1.setMaximumSize(16777215, 320)
                        self.ui.label_status1.setMinimumSize(180, 0)
                        self.ui.label_status1.setMaximumSize(16777215, 100)
                        self.ui.button_mode1.setMinimumSize(70, 0)
                        self.ui.button_mode1.setMaximumSize(16777215, 60)
                        
                        # self.ui.label_value1.setStyleSheet(u"font-size: 50pt;font-weight: bold;")
                        # self.ui.label_status1.setStyleSheet(u"font-size: 40pt;font-weight: bold;")
                        # self.ui.button_mode1.setStyleSheet(u"font-size: 40pt;font-weight: bold;")   
                    
                    self.ui.label_value1.show()
                    self.ui.label_status1.show()
                    self.ui.button_mode1.show() 
                    
                    self.ui.label_dial2.hide()
                    self.ui.label_dial3.hide()
                    self.ui.label_dial4.hide()
                        
                    self.ui.label_status2.hide()
                    self.ui.label_status3.hide()
                    self.ui.label_status4.hide()
                        
                    self.ui.label_value2.hide()
                    self.ui.label_value3.hide()
                    self.ui.label_value4.hide()
                        
                    self.ui.button_mode2.hide()
                    self.ui.button_mode3.hide()
                    self.ui.button_mode4.hide()
                    
                    # self.ui.widget_spc1.hide()
                    # self.ui.widget_line2.hide()

                elif channel_count == 2:
                    if self.ui.button_mode1.text() == 'Dial' : 
                        self.ui.label_dial1.show()
                        self.ui.label_dial1.setMinimumSize(300, 0)
                        self.ui.label_dial1.setMaximumSize(16777215, 200)
                        
                        # self.ui.label_dial2.setMinimumSize(300, 0)
                        # self.ui.label_dial2.setMaximumSize(16777215, 200)
                        
                        self.ui.label_value1.setMinimumSize(210, 0)
                        self.ui.label_value1.setMaximumSize(16777215, 70)
                        
                        # self.ui.label_value1.setMaximumSize(16777215, 80)
                        self.ui.label_status1.setMinimumSize(120, 0)
                        self.ui.label_status1.setMaximumSize(16777215, 50)
                        
                        self.ui.button_mode1.setMinimumSize(80, 0)
                        self.ui.button_mode1.setMaximumSize(16777215, 30)
                        
                        # self.ui.button_mode1.setStyleSheet(u"font-size: 30pt;font-weight: bold;")
                        # self.ui.label_value1.setStyleSheet(u"font-size: 35pt;font-weight: bold;")
                        # self.ui.label_status1.setStyleSheet(u"font-size: 30pt;font-weight: bold;")
                        # self.ui.label_dial1.setPixmap(QPixmap(u"/home/torizon/app/src/green_60_big.png"))
                    
                        
                    if self.ui.button_mode2.text() == 'Dial':
                        self.ui.label_dial2.show()
                        self.ui.label_dial2.setMinimumSize(300, 0)
                        self.ui.label_dial2.setMaximumSize(16777215, 200)
                        
                        self.ui.label_dial2.setMinimumSize(300, 0)
                        self.ui.label_dial2.setMaximumSize(16777215, 200)
                        
                        self.ui.label_value2.setMinimumSize(210, 70)
                        self.ui.label_value2.setMaximumSize(16777215, 80)
                        self.ui.label_status2.setMinimumSize(120, 0)
                        self.ui.label_status2.setMaximumSize(16777215, 50)
                        self.ui.button_mode2.setMinimumSize(80, 0)
                        self.ui.button_mode2.setMaximumSize(16777215, 30)
                        
                        # self.ui.label_dial2.setPixmap(QPixmap(u"/home/torizon/app/src/green_60_big.png"))
                        # self.ui.label_value2.setStyleSheet(u"font-size: 35pt;font-weight: bold;")
                        # self.ui.label_status2.setStyleSheet(u"font-size: 30pt;font-weight: bold;")
                        # self.ui.button_mode2.setStyleSheet(u"font-size: 30pt;font-weight: bold;")
                    
                    if self.ui.button_mode1.text() == 'Digit' : 
                        self.ui.label_value1.setMinimumSize(300, 0)
                        self.ui.label_value1.setMaximumSize(16777215, 220)
                        self.ui.label_status1.setMinimumSize(180, 0)
                        self.ui.label_status1.setMaximumSize(16777215, 100)
                        self.ui.button_mode1.setMinimumSize(80, 0)
                        self.ui.button_mode1.setMaximumSize(16777215, 30)
                        # self.ui.label_value1.setStyleSheet(u"font-size: 40pt;font-weight: bold;")
                        # self.ui.label_status1.setStyleSheet(u"font-size: 30pt;font-weight: bold;")
                        # self.ui.button_mode1.setStyleSheet(u"font-size: 18pt;font-weight: bold;")

                    if self.ui.button_mode2.text() == 'Digit':
                        self.ui.label_value2.setMinimumSize(300, 0)
                        self.ui.label_value2.setMaximumSize(16777215, 220)
                        self.ui.label_status2.setMinimumSize(180, 0)
                        self.ui.label_status2.setMaximumSize(16777215, 100)
                        self.ui.button_mode2.setMinimumSize(80, 0)
                        self.ui.button_mode2.setMaximumSize(16777215, 30)
                        # self.ui.label_value2.setStyleSheet(u"font-size: 40pt;font-weight: bold;")
                        # self.ui.label_status2.setStyleSheet(u"font-size: 30pt;font-weight: bold;")
                        # self.ui.button_mode2.setStyleSheet(u"font-size: 18pt;font-weight: bold;")
                        
                    self.ui.label_value2.show()
                    self.ui.label_status2.show()
                    self.ui.button_mode2.show()
                    
                    self.ui.label_dial3.hide()
                    self.ui.label_dial4.hide()
                    self.ui.label_status3.hide()
                    self.ui.label_status4.hide()
                        
                    self.ui.button_mode3.hide()
                    self.ui.button_mode4.hide()
                        
                    # self.ui.widget_line2.hide()
                        
                elif channel_count == 3:
                                         
                    if self.ui.button_mode1.text() == 'Dial' :
                        self.ui.label_dial1.show()
                        self.ui.label_dial1.setMinimumSize(150, 100)
                        # self.ui.label_dial1.setMaximumSize(16777215, 100)
                        
                        # self.ui.label_value1.setStyleSheet(u"font-size: 20pt;font-weight: bold;")
                        # self.ui.label_status1.setStyleSheet(u"font-size: 18pt;font-weight: bold;")
                        self.ui.label_value1.setMinimumSize(150,30)
                        # self.ui.label_value1.setMaximumSize(16777215, 30)
                        self.ui.label_status1.setMinimumSize(170,30)
                        # self.ui.label_value1.setMaximumSize(16777215, 30)
                        self.ui.button_mode1.setMinimumSize(100,30)
                        # self.ui.button_mode1.setMaximumSize(16777215, 30)
                        # self.ui.button_mode1.setStyleSheet(u"font-size: 18pt;font-weight: bold;")
                        
                    if self.ui.button_mode2.text() == 'Dial' : 
                        self.ui.label_dial2.show()
                        self.ui.label_dial2.setMinimumSize(150, 100)
                        # self.ui.label_dial2.setMaximumSize(16777215, 100)
                        # self.ui.label_value2.setStyleSheet(u"font-size: 20pt;font-weight: bold;")
                        # self.ui.label_status2.setStyleSheet(u"font-size: 18pt;font-weight: bold;")
                        self.ui.label_value2.setMinimumSize(150,30)
                        # self.ui.label_value2.setMaximumSize(16777215, 30)
                        self.ui.label_status2.setMinimumSize(170,30)
                        # self.ui.label_status2.setMaximumSize(16777215, 30)
                        self.ui.button_mode2.setMinimumSize(100,30)
                        # self.ui.button_mode2.setMaximumSize(16777215, 30)
                        # self.ui.button_mode2.setStyleSheet(u"font-size: 18pt;font-weight: bold;")
                        
                    if self.ui.button_mode3.text() == 'Dial':
                        self.ui.label_dial3.show()
                        self.ui.label_dial3.setMinimumSize(150, 100)
                        # self.ui.label_dial3.setMaximumSize(16777215, 100)
                        # self.ui.label_value3.setStyleSheet(u"font-size: 20pt;font-weight: bold;")
                        # self.ui.label_status3.setStyleSheet(u"font-size: 18pt;font-weight: bold;")
                        self.ui.label_value3.setMinimumSize(160,30)
                        # self.ui.label_value3.setMaximumSize(16777215, 30)
                        self.ui.label_status3.setMinimumSize(170,30)
                        # self.ui.label_status3.setMaximumSize(16777215, 30)
                        self.ui.button_mode3.setMinimumSize(100,30)
                        # self.ui.button_mode3.setMaximumSize(16777215, 30)
                        # self.ui.button_mode3.setStyleSheet(u"font-size: 18pt;font-weight: bold;")
                        
                    if self.ui.button_mode1.text() == 'Digit' : 
                        self.ui.label_value1.setStyleSheet(u"font-size: 35pt;font-weight: bold;")
                        self.ui.label_status1.setStyleSheet(u"font-size: 25pt;font-weight: bold;")
                        self.ui.label_value1.setMinimumSize(250,60)
                        # self.ui.label_value1.setMaximumSize(16777215, 60)
                        self.ui.label_status1.setMinimumSize(200,60)
                        # self.ui.label_status1.setMaximumSize(16777215, 30)
                        self.ui.button_mode1.setMinimumSize(100,30)
                        # self.ui.button_mode1.setMaximumSize(16777215, 30)
                        self.ui.button_mode1.setStyleSheet(u"font-size: 18pt;font-weight: bold;")
                        
                    if self.ui.button_mode2.text() == 'Digit': 
                        self.ui.label_value2.setStyleSheet(u"font-size: 35pt;font-weight: bold;")
                        self.ui.label_status2.setStyleSheet(u"font-size: 25pt;font-weight: bold;")
                        self.ui.label_value2.setMinimumSize(250,60)
                        # self.ui.label_value2.setMaximumSize(16777215, 60)
                        self.ui.label_status2.setMinimumSize(200,60)
                        # self.ui.label_status2.setMaximumSize(16777215, 30)
                        self.ui.button_mode2.setMinimumSize(100,30)
                        # self.ui.button_mode2.setMaximumSize(16777215, 30)
                        self.ui.button_mode2.setStyleSheet(u"font-size: 18pt;font-weight: bold;")
                        
                    if self.ui.button_mode3.text() == 'Digit' :
                        self.ui.label_value3.setStyleSheet(u"font-size: 35pt;font-weight: bold;")
                        self.ui.label_status3.setStyleSheet(u"font-size: 25pt;font-weight: bold;")
                        self.ui.label_value3.setMinimumSize(350,90)
                        # self.ui.label_value3.setMaximumSize(16777215, 90)
                        self.ui.label_status3.setMinimumSize(270,30)
                        # self.ui.label_status3.setMaximumSize(16777215, 30)
                        self.ui.button_mode3.setMinimumSize(100,30)
                        # self.ui.button_mode3.setMaximumSize(16777215, 30)
                        self.ui.button_mode3.setStyleSheet(u"font-size: 18pt;font-weight:bold")
                    
                    self.ui.label_value3.show()
                    self.ui.label_status3.show()
                    self.ui.button_mode3.show()
                    
                    self.ui.label_dial4.hide()
                    self.ui.label_value4.hide()
                    self.ui.label_status4.hide()
                    self.ui.button_mode4.hide()
                        
                else:   
                    if self.ui.button_mode1.text() == 'Dial' :
                        self.ui.label_dial1.show()
                        self.ui.label_value1.setStyleSheet(u"font-size: 20pt;font-weight: bold;")
                        self.ui.label_status1.setStyleSheet(u"font-size: 15pt;font-weight: bold;")
                        self.ui.label_value1.setMinimumSize(160,30)
                        # self.ui.label_value1.setMaximumSize(16777215, 40)
                        self.ui.label_status1.setMinimumSize(150,30)
                        # self.ui.label_status1.setMaximumSize(16777215, 30)
                        self.ui.label_dial1.setMinimumSize(100,40)
                        # self.ui.label_dial1.setMaximumSize(16777215, 50)
                        self.ui.button_mode1.setMinimumSize(100,30)
                        # self.ui.button_mode1.setMaximumSize(16777215, 30)
                        self.ui.button_mode1.setStyleSheet(u"font-size: 18pt;font-weight: bold;")
                    
                    if self.ui.button_mode2.text() == 'Dial' :
                        self.ui.label_dial2.show()
                        self.ui.label_value2.setStyleSheet(u"font-size: 20pt;font-weight: bold;")
                        self.ui.label_status2.setStyleSheet(u"font-size: 15pt;font-weight: bold;")
                        self.ui.label_value2.setMinimumSize(160,30)
                        # self.ui.label_value2.setMaximumSize(16777215, 40)
                        self.ui.label_status2.setMinimumSize(150,30)
                        # self.ui.label_status2.setMaximumSize(16777215, 30)
                        self.ui.label_dial2.setMinimumSize(100,40)
                        # self.ui.label_dial2.setMaximumSize(16777215, 50)
                        self.ui.button_mode2.setMinimumSize(100,30)
                        # self.ui.button_mode2.setMaximumSize(16777215, 30)
                        self.ui.button_mode2.setStyleSheet(u"font-size: 18pt;font-weight: bold;")
                    
                    if self.ui.button_mode3.text() == 'Dial' :
                        self.ui.label_dial3.show()    
                        self.ui.label_value3.setStyleSheet(u"font-size: 20pt;font-weight: bold;")
                        self.ui.label_status3.setStyleSheet(u"font-size: 15pt;font-weight: bold;")
                        self.ui.label_value3.setMinimumSize(160,30)
                        # self.ui.label_value3.setMaximumSize(16777215, 40)
                        self.ui.label_status3.setMinimumSize(150,30)
                        # self.ui.label_status3.setMaximumSize(16777215, 30)
                        self.ui.label_dial3.setMinimumSize(100,40)
                        # self.ui.label_dial3.setMaximumSize(16777215, 50)
                        self.ui.button_mode3.setMinimumSize(100,30)
                        # self.ui.button_mode3.setMaximumSize(16777215, 30)
                        self.ui.button_mode3.setStyleSheet(u"font-size: 18pt;font-weight: bold;")
                        
                    if self.ui.button_mode4.text() == 'Dial':   
                        self.ui.label_dial4.show()
                        self.ui.label_value4.setStyleSheet(u"font-size: 20pt;font-weight: bold;")
                        self.ui.label_status4.setStyleSheet(u"font-size: 15pt;font-weight: bold;")
                        self.ui.label_value4.setMinimumSize(160,30)
                        # self.ui.label_value4.setMaximumSize(16777215, 40)
                        self.ui.label_status4.setMinimumSize(150,30)
                        # self.ui.label_status4.setMaximumSize(16777215, 30)
                        self.ui.label_dial4.setMinimumSize(100,40)
                        # self.ui.label_dial4.setMaximumSize(16777215, 50)
                        self.ui.button_mode4.setMinimumSize(100,30)
                        # self.ui.button_mode4.setMaximumSize(16777215, 30)
                        self.ui.button_mode4.setStyleSheet(u"font-size: 18pt;font-weight: bold;")
                        
                    if self.ui.button_mode1.text() == 'Digit' :
                        self.ui.label_value1.setStyleSheet(u"font-size: 30pt;font-weight: bold;")
                        self.ui.label_status1.setStyleSheet(u"font-size: 20pt;font-weight: bold;")
                        self.ui.label_value1.setMinimumSize(220,100)
                        # self.ui.label_value1.setMaximumSize(16777215, 100)

                        self.ui.label_status1.setMinimumSize(200,30)
                        # self.ui.label_status1.setMaximumSize(16777215, 30)

                        self.ui.button_mode1.setMinimumSize(100,30)
                        # self.ui.button_mode1.setMaximumSize(16777215, 30)
                        self.ui.button_mode1.setStyleSheet(u"font-size: 18pt;font-weight: bold;")
                    
                    if self.ui.button_mode2.text() == 'Digit' :
                        self.ui.label_value2.setStyleSheet(u"font-size: 30pt;font-weight: bold;")
                        self.ui.label_status2.setStyleSheet(u"font-size: 20pt;font-weight: bold;")
                        self.ui.label_value2.setMinimumSize(250,100)
                        # self.ui.label_value2.setMaximumSize(16777215, 100)
                        self.ui.label_status2.setMinimumSize(200,30)
                        # self.ui.label_status2.setMaximumSize(16777215, 30)
                        self.ui.button_mode2.setMinimumSize(100,30)
                        # self.ui.button_mode2.setMaximumSize(16777215, 30)
                        self.ui.button_mode2.setStyleSheet(u"font-size: 18pt;font-weight: bold;")
                        
                    if self.ui.button_mode3.text() == 'Digit' :   
                        self.ui.label_value3.setStyleSheet(u"font-size: 30pt;font-weight: bold;")
                        self.ui.label_status3.setStyleSheet(u"font-size: 20pt;font-weight: bold;")
                        self.ui.label_value3.setMinimumSize(220,100)
                        # self.ui.label_value3.setMaximumSize(16777215, 100)
                        self.ui.label_status3.setMinimumSize(200,30)
                        # self.ui.label_status3.setMaximumSize(16777215, 30)
                        self.ui.button_mode3.setMinimumSize(100,30)
                        # self.ui.button_mode3.setMaximumSize(16777215, 30)
                        self.ui.button_mode3.setStyleSheet(u"font-size: 18pt;font-weight: bold;")
                        
                    if self.ui.button_mode4.text() == 'Digit':    
                        self.ui.label_value4.setStyleSheet(u"font-size: 30pt;font-weight: bold;")
                        self.ui.label_status4.setStyleSheet(u"font-size: 20pt;font-weight: bold;")
                        self.ui.label_value4.setMinimumSize(220,100)
                        # self.ui.label_value4.setMaximumSize(16777215, 100)
                        self.ui.label_status4.setMinimumSize(200,30)
                        # self.ui.label_status4.setMaximumSize(16777215, 30)
                        self.ui.button_mode4.setMinimumSize(100,30)
                        # self.ui.button_mode4.setMaximumSize(16777215, 30)
                        self.ui.button_mode4.setStyleSheet(u"font-size: 18pt;font-weight: bold;")
                        
                    self.ui.label_value4.show()
                    self.ui.label_status4.show()
                    self.ui.button_mode4.show()


        except Exception as e:
            print(f"Error in Dial Indicator : {e}") 
                
class SPCBase:
    """
    Base class for one SPC chart (D1–D4).
    Handles:
    - scaling values
    - background zones
    - plotting data
    """

    def __init__(self, title, lol, lsl, lcl, nominal, ucl, usl, uol):
        try:
            self.title = title                  # Graph title (D1, D2, ...)
            self.limits = [lol, lsl, lcl, nominal, ucl, usl, uol]                # SPC limits

            self.data_raw = []                  # Raw input values
            self.data_scaled = []               # Scaled values for plotting

            self.y_positions = np.arange(7)     # 7 SPC zones

            # Colors and styles for limit lines
            self.line_colors = ["red","red","yellow","green","yellow","red","red"]
            self.line_styles = ["-","--",":","-.",":","--","-"]

            # Create matplotlib figure and canvas
            self.fig = Figure()#Figure(figsize=(4.5, 2.2))
            self.canvas = FigureCanvas(self.fig)
            # self.fig.set_figheight(9)
            # self.fig.set_size_inches(7,9)
            self.ax = self.fig.add_subplot(111)

            # Dark theme
            self.fig.patch.set_facecolor("black")
            self.ax.tick_params(axis="x", colors="white")
            self.ax.tick_params(axis="y", colors="white")

            # Draw empty graph initially
            self.init_blank_ui()
        except Exception as e:
            print(f"Error in SPC Base class initialization :{e}")   
            
    def scale_value(self, v):
        try:
            for i in range(len(self.limits)-1):
                low = self.limits[i]
                high = self.limits[i + 1]

                if low <= v <= high or high <= v <= low:
                    return i + (v - low) / (high - low)

            return 0 if v < self.limits[0] else 6
        except Exception as e:
            print(f"Error in scale_value -> {e}")
    

    def set_margins(self, left, right, top, bottom):
        try:
            self.fig.subplots_adjust(
                left=left,
                right=right,
                top=top,
                bottom=bottom
            )
            self.canvas.draw_idle()
        except Exception as e:
            print(f"error in set margins - > {e}")

    def draw_background(self):
        try:
            self.ax.axhspan(0, 1, color="red", alpha=0.9)
            self.ax.axhspan(1, 2, color="yellow", alpha=0.9)
            self.ax.axhspan(2, 4, color="green", alpha=0.9)
            self.ax.axhspan(4, 5, color="yellow", alpha=0.9)
            self.ax.axhspan(5, 6, color="red", alpha=0.9)
        except Exception as e:
            print("Error")

    def draw_limit_lines(self):
        try:
            xmax = len(self.data_raw) if self.data_raw else 1
            for i in range(7):
                self.ax.hlines(
                    self.y_positions[i],
                    xmin=0,
                    xmax=xmax,
                    colors=self.line_colors[i],
                    linestyles=self.line_styles[i],
                    linewidth=1.5
                )
        except Exception as e:
            print("Error in draw_limit_lines -> {e}")
    
    def set_limits(self, lol, lsl, lcl, nominal, ucl, usl, uol):
        try:
            self.limits = [lol, lsl, lcl, nominal, ucl, usl, uol]
            #print("LIMITS:", self.limits)
            self.init_blank_ui()
        except Exception as e:
            print(f"Error in setting limits -> {e}")
    
    
    def init_blank_ui(self):
        try:
            self.ax.clear()
            self.draw_background()
            self.draw_limit_lines()

            # IMPORTANT: add padding
            self.ax.set_ylim(-0.6, 6.7)
            

            self.ax.set_yticks(self.y_positions)
            self.ax.set_yticklabels(self.limits, color="white")

            self.ax.set_yticks(self.y_positions)
            self.ax.set_yticklabels(self.limits)

            self.ax.set_title(self.title, color="white",fontweight="bold",pad=4)
            self.ax.set_xlabel("")
            self.ax.set_ylabel(self.title)
            
            # Ticks size
            self.ax.tick_params(axis="x", labelsize=9, pad=4, colors="white")
            self.ax.tick_params(axis="y", labelsize=9, colors="white")

            # self._apply_responsive_layout()
            
            # plt.draw()
            # plt.pause(0.01)
            self.canvas.draw_idle()
        except Exception as e:
            print(f"Error in init blank ui -> {e}")

    
    def generate_graph(self, raw_data):
        try:
            self.data_raw = raw_data
            self.data_scaled = [self.scale_value(v) for v in raw_data]

            self.ax.clear()
            self.draw_background()
            self.draw_limit_lines()

            x = np.arange(1, len(self.data_scaled) + 1)
            self.ax.plot(x, self.data_scaled, "bo-", markersize=3)
            
            # IMPORTANT: add padding
            self.ax.set_ylim(-0.6, 6.7)
            

            self.ax.set_yticks(self.y_positions)
            self.ax.set_yticklabels(self.limits, color="white")

            self.ax.set_yticks(self.y_positions)
            self.ax.set_yticklabels(self.limits)

            self.ax.set_title(self.title, color="white",fontweight="bold",pad=4)
            self.ax.set_xlabel("")
            self.ax.set_ylabel(self.title)

            # Ticks size
            self.ax.tick_params(axis="x", labelsize=9, pad=4, colors="white")
            self.ax.tick_params(axis="y", labelsize=9, colors="white")

            # self.apply_responsive_layout()
        
            # plt.draw()
            # plt.pause(0.01)
        except Exception as e:
            print("Erro in gnerate_graph -> {e}")
            
    
    
    def update_graph(self, value):
        try:
            self.data_raw.append(value)

            if len(self.data_raw) > 30:
                self.data_raw.pop(0)

            scaled = [self.scale_value(v) for v in self.data_raw]

            self.ax.clear()
            self.draw_background()
            self.draw_limit_lines()

            x = np.arange(1, len(scaled) + 1)
            self.ax.plot(x, scaled, "bo-", markersize=3)
            
            # IMPORTANT: add padding
            self.ax.set_ylim(-0.6, 6.7)
            

            self.ax.set_yticks(self.y_positions)
            self.ax.set_yticklabels(self.limits, color="white")

            self.ax.set_yticks(self.y_positions)
            self.ax.set_yticklabels(self.limits)

            self.ax.set_title(self.title, color="white",fontweight="bold",pad=4)
            self.ax.set_xlabel("")
            self.ax.set_ylabel(self.title)

            # Ticks size
            self.ax.tick_params(axis="x", labelsize=9, pad=4, colors="white")
            self.ax.tick_params(axis="y", labelsize=9, colors="white")

            # self.apply_responsive_layout()
            
            # self.generate_graph(self.data_raw)
            self.canvas.draw_idle()
        except Exception as e:
            print(f"Error in update_graph -> {e}")
    
            
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

            
class SPCManager:
    def __init__(self, main_window):
        try:
            self.ui = main_window
            
            self.spc_all = {
            1: SPCWidget(SPCBase("D1", lol=20.000,lsl=20.010,lcl=20.015,nominal=20.020,ucl=20.025,usl=20.030,uol=20.042)),
            2: SPCWidget(SPCBase("D2", lol=20.000,lsl=20.010,lcl=20.015,nominal=20.020,ucl=20.025,usl=20.030,uol=20.042)),
            3: SPCWidget(SPCBase("D3", lol=20.000,lsl=20.010,lcl=20.015,nominal=20.020,ucl=20.025,usl=20.030,uol=20.042)),
            4: SPCWidget(SPCBase("D4", lol=20.000,lsl=20.010,lcl=20.015,nominal=20.020,ucl=20.025,usl=20.030,uol=20.042)),
            }

            self.active_channels = []
            
            # Layouts from Qt Designer
            self.spc_1 = self.ui.verticalLayout_30
            self.spc_2 = self.ui.verticalLayout_31
            self.spc_3 = self.ui.verticalLayout_32
            self.spc_4 = self.ui.verticalLayout_33

            self.ui.horizontalLayout_56.setStretch(0, 1)
            self.ui.horizontalLayout_56.setStretch(1, 1)
            self.ui.horizontalLayout_71.setStretch(0, 1)
            self.ui.horizontalLayout_71.setStretch(1, 1)

            # ✅ ROW stretch (THIS WAS MISSING)
            self.ui.verticalLayout_24.setStretch(0, 1)
            self.ui.verticalLayout_24.setStretch(1, 1)
            self.ui.verticalLayout_28.setStretch(0, 1)
            self.ui.verticalLayout_28.setStretch(1, 1)

        except Exception as e:
            print(f"Error in intialization of SPCManager :-> {e}")
            
    def load_program_OnSpc(self, program_id: int):
        """
        Load SPC limits for all channels for given ProgramId
        """
        session = SessionLocal()
        try:
            for ch, spc_widget in self.spc_all.items():
                dim = f"D{ch}"

                row = (
                    session.query(ProbeBasedSettings)
                    .filter(
                        ProbeBasedSettings.ProgramId == program_id,
                        ProbeBasedSettings.Dimension == dim
                    )
                    .first()
                )

                if not row:
                    continue

                spc_widget.spc.set_limits(
                    lol=row.LowerOffsetLimit,
                    lsl=row.LowerSpecificationLimit,
                    lcl=row.LowerControlLimit,
                    nominal=row.NominalValue,
                    ucl=row.UpperControlLimit,
                    usl=row.UpperSpecificationLimit,
                    uol=row.UpperOffsetLimit,
                )

                # spc_widget.spc.reset_graph()

        finally:
            session.close()
                
    #clear layout for first time
    def clear_layout(self, layout):
        try:
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
            # clear everything
            for layout in (self.spc_1, self.spc_2, self.spc_3, self.spc_4):
                self.clear_layout(layout)

            spcs = [self.spc_all[ch] for ch in self.active_channels]
            count = len(spcs)
            # self.ui.label_dial1.hide()
            # self.ui.label_dial2.hide()
            # self.ui.label_dial3.hide()
            # self.ui.label_dial4.hide()  
            
            # ---------------- 1 SPC ----------------
            if count == 1:
                self.spc_1.addWidget(spcs[0])
                spcs[0].spc.canvas.setMinimumHeight(150)
                spcs[0].spc.set_margins(
                    left=0.12,
                    right=0.97,
                    top=0.88,
                    bottom=0.22
                )
                if self.ui.button_mode1.text() == 'SPC' :
                    self.ui.widget_spc1.show()
                
                
                self.ui.verticalLayout_24.setStretch(0, 1)  # first row (graphs)
                self.ui.verticalLayout_28.setStretch(1, 0)  # second row (hidden)
                

            # ---------------- 2 SPC ----------------
            elif count == 2:
                # TOP SPC
                self.spc_1.addWidget(spcs[0], stretch=1)

                # BOTTOM SPC → USE BOTTOM-LEFT (IMPORTANT)
                self.spc_2.addWidget(spcs[1], stretch=1)

                # margins for half-height SPCs
                for spc in spcs:
                    spc.spc.canvas.setMinimumHeight(150)
                    spc.spc.set_margins(
                        left=0.12,
                        right=0.97,
                        top=0.90,#0.85,
                        bottom=0.26
                    )
                if self.ui.button_mode1.text() == 'SPC' :
                    self.ui.widget_spc1.show()
                if self.ui.button_mode2.text() == 'SPC' :
                    self.ui.widget_spc2.show()
                
                self.ui.verticalLayout_24.setStretch(0, 1)
                self.ui.verticalLayout_24.setStretch(1, 1)
                self.ui.verticalLayout_25.setStretch(0, 1)
                self.ui.verticalLayout_25.setStretch(1, 1)
                
            # ---------------- 3 SPC (FIXED) ----------------
            elif count == 3:
                self.spc_1.addWidget(spcs[0])
                self.spc_2.addWidget(spcs[1])

                # put SPC3 in bottom-left
                self.spc_3.addWidget(spcs[2])

                for spc in spcs:
                    spc.spc.canvas.setMinimumHeight(120)

                spcs[0].spc.set_margins(
                    left=0.15,
                    right=0.96,
                    top=0.83,
                    bottom=0.20
                )
                spcs[1].spc.set_margins(
                    left=0.15,
                    right=0.96,
                    top=0.83,
                    bottom=0.20
                )

                # bottom full-width SPC
                spcs[2].spc.set_margins(
                    left=0.12,
                    right=0.97,
                    top=0.83,
                    bottom=0.20
                )
                if self.ui.button_mode1.text() == 'SPC' :
                    self.ui.widget_spc1.show()
                if self.ui.button_mode2.text() == 'SPC' :
                    self.ui.widget_spc2.show()
                if self.ui.button_mode3.text() == 'SPC' :
                    self.ui.widget_spc3.show()
                        
                # balance rows
                self.ui.verticalLayout_24.setStretch(0, 1)
                self.ui.verticalLayout_24.setStretch(1, 1)
                self.ui.verticalLayout_28.setStretch(0, 0)
                self.ui.verticalLayout_28.setStretch(1, 1)
                
                # stretch bottom-left to full width
                self.ui.horizontalLayout_71.setStretch(0, 1)
                self.ui.horizontalLayout_71.setStretch(1, 0)
            

            # ---------------- 4 SPC ----------------
            elif count == 4:
                self.spc_1.addWidget(spcs[0])
                self.spc_2.addWidget(spcs[1])
                self.spc_3.addWidget(spcs[2])
                self.spc_4.addWidget(spcs[3])
                
                for spc in spcs:
                    spc.spc.canvas.setMinimumHeight(100)
                    spc.spc.set_margins(
                        left=0.15,
                        right=0.97,
                        top=0.83,
                        bottom=0.25
                    )
                if self.ui.button_mode1.text() == 'SPC' :
                    self.ui.widget_spc1.show()
                if self.ui.button_mode2.text() == 'SPC' :
                    self.ui.widget_spc2.show()
                if self.ui.button_mode3.text() == 'SPC' :
                    self.ui.widget_spc3.show()
                if self.ui.button_mode4.text() == 'SPC':
                    self.ui.widget_spc4.show()
                
                self.ui.verticalLayout_24.setStretch(0, 1)
                self.ui.verticalLayout_24.setStretch(1, 1)
                self.ui.verticalLayout_28.setStretch(0, 1)
                self.ui.verticalLayout_28.setStretch(1, 1)
                
                # restore visibility
                self.ui.horizontalLayout_56.setStretch(0, 1)
                self.ui.horizontalLayout_56.setStretch(1, 1)
                self.ui.horizontalLayout_71.setStretch(0, 1)
                self.ui.horizontalLayout_71.setStretch(1, 1)
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

            spc_widget.update_value(value)
        except Exception as e:
            print(f"Error update value in graph -> {e}")
            msg = CustomMessageBox("Failed to update value on Graph", "error",
                                   parent=self.ui)
            msg.exec_()
