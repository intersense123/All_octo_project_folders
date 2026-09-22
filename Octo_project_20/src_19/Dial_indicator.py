from PySide2.QtWidgets import QApplication, QMainWindow, QStackedWidget , QWidget
from PySide2.QtWidgets import QFrame
from PySide2.QtWidgets import QLineEdit
from PySide2 import QtCore, QtWidgets
from PySide2.QtCore import QTimer, QTime, QSize, QObject , QThread , Signal, Qt, QCoreApplication
from PySide2.QtGui import QPixmap
from sqlalchemy.orm import *
from letters_keypad import Keyboard
from messageBox import CustomMessageBox
from numpad import numpad_window
from models import *
from active_ui_handler import *

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
            # self.set_visibility()
        except Exception as e:
            print(f"Error in initializtion of Dial_Indicator : {e}")

    
    #to enable disable line while switching combobox of Ovality ON and OFF
    def set_visibility(self):
        try:
            channels=self.app.get_channels_for_program(
                int(self.ui.valueObj.activeVariables_dict["ActiveProgramId"])
            )
            channel_count = len(channels)
            print(f"channel in set visibilty {channel_count}")
            display_mode = (
                self.ui.valueObj.IOSettings_dict
                .get('DISPLAY_MODE', {})
                .get('Value', 'Digit')
            )
            print(f"display_mode = {display_mode}")
            if channel_count == 1:
                if display_mode == 'Dial':
                    self.ui.dial_2.hide()
                    self.ui.dial_3.hide()
                    self.ui.dial_4.hide()
                    self.ui.label_status_dial2.hide()
                    self.ui.label_status_dial3.hide()
                    self.ui.label_status_dial4.hide()
                    self.ui.label_value2.hide()
                    self.ui.label_value3.hide()
                    self.ui.label_value4.hide()
                    self.ui.dial_1.setFixedSize(QSize(280, 280))
                    self.ui.dial_1.setPixmap(QPixmap(u":/images/indicator6_green_2_probe.png"))
                elif display_mode == 'Digit':
                    self.ui.label_digitVal1.setMinimumSize(QSize(200, 0))
                    self.ui.label_digitVal1.setMaximumSize(QSize(800, 100))
                    self.ui.label_digitStatus1.setMinimumSize(QSize(200, 0))
                    self.ui.label_digitStatus1.setMaximumSize(QSize(800, 100))
                    self.ui.label_digitVal2.hide()
                    self.ui.label_digitVal3.hide()
                    self.ui.label_digitVal4.hide()
                    self.ui.label_digitStatus2.hide()
                    self.ui.label_digitStatus3.hide()
                    self.ui.label_digitStatus4.hide()
            elif channel_count == 2:
                if display_mode == 'Dial':
                    self.ui.dial_3.hide()
                    self.ui.dial_4.hide()
                    self.ui.label_value3.hide()
                    self.ui.label_value4.hide()
                    self.ui.label_status_dial3.hide()
                    self.ui.label_status_dial4.hide()
                    self.ui.dial_1.setFixedSize(QSize(280, 280))
                    self.ui.dial_2.setFixedSize(QSize(280, 280))
                    self.ui.dial_1.setPixmap(QPixmap(u":/images/indicator6_green_2_probe.png"))
                    self.ui.dial_2.setPixmap(QPixmap(u":/images/indicator6_green_2_probe.png"))
                elif display_mode == 'Digit':
                    self.ui.label_digitVal1.setMinimumSize(QSize(120, 0))
                    self.ui.label_digitVal1.setMaximumSize(QSize(800, 80))
                    self.ui.label_digitStatus1.setMinimumSize(QSize(120, 0))
                    self.ui.label_digitStatus1.setMaximumSize(QSize(800, 80))
                    
                    self.ui.label_digitVal2.setMinimumSize(QSize(120, 0))
                    self.ui.label_digitVal2.setMaximumSize(QSize(800, 80))
                    self.ui.label_digitStatus2.setMinimumSize(QSize(120, 0))
                    self.ui.label_digitStatus2.setMaximumSize(QSize(800, 80))
                    
                    self.ui.label_digitVal3.hide()
                    self.ui.label_digitVal4.hide()
                    self.ui.label_digitStatus3.hide()
                    self.ui.label_digitStatus4.hide()
            elif channel_count == 3:
                if display_mode == 'Dial':
                    self.ui.dial_4.hide()
                    self.ui.label_value4.hide()
                    self.ui.label_status_dial4.hide()
                    self.ui.dial_1.setFixedSize(QSize(280, 280))
                    self.ui.dial_2.setFixedSize(QSize(280, 280))
                    self.ui.dial_3.setFixedSize(QSize(280, 280))
                    self.ui.dial_1.setPixmap(QPixmap(u":/images/indicator6_green.png"))
                    self.ui.dial_2.setPixmap(QPixmap(u":/images/indicator6_green.png"))
                    self.ui.dial_3.setPixmap(QPixmap(u":/images/indicator6_green.png"))
                elif display_mode == 'Digit':
                    self.ui.label_digitVal1.setMinimumSize(QSize(150, 0))
                    self.ui.label_digitVal1.setMaximumSize(QSize(800, 80))
                    self.ui.label_digitStatus1.setMinimumSize(QSize(150, 0))
                    self.ui.label_digitStatus1.setMaximumSize(QSize(800, 80))
                    
                    self.ui.label_digitVal2.setMinimumSize(QSize(150, 0))
                    self.ui.label_digitVal2.setMaximumSize(QSize(800, 80))
                    self.ui.label_digitStatus2.setMinimumSize(QSize(150, 0))
                    self.ui.label_digitStatus2.setMaximumSize(QSize(800, 80))
                    
                    self.ui.label_digitVal3.setMinimumSize(QSize(150, 0))
                    self.ui.label_digitVal3.setMaximumSize(QSize(800, 80))
                    self.ui.label_digitStatus3.setMinimumSize(QSize(150, 0))
                    self.ui.label_digitStatus3.setMaximumSize(QSize(800, 80))
                    
                    self.ui.label_digitVal4.hide()
                    self.ui.label_digitStatus4.hide()
            else:
                    pass
                    


            
        except Exception as e:
            print(f"Error in Dial Indicator : {e}") 
