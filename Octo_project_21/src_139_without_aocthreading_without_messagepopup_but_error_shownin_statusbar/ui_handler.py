# ui_handler.py
import os
import subprocess

from PySide2 import QtGui
from PySide2.QtWidgets import QApplication, QInputDialog, QMainWindow, QMessageBox, QStackedWidget , QWidget
from PySide2.QtWidgets import QFrame
from PySide2.QtWidgets import QLineEdit
from PySide2 import QtCore, QtWidgets
from PySide2.QtCore import QTimer, QSize, QDate , QObject , QThread , Signal, Qt, QCoreApplication, QTimer
from PySide2.QtGui import QPixmap
from sqlalchemy.orm import *
from letters_keypad import Keyboard
from messageBox import CustomMessageBox
from numpad import numpad_window,TouchOverlay
from models import *
from active_ui_togglebutton_handler import *
from PySide2.QtCore import Qt
from PySide2.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QGridLayout,
    QPushButton,
    QLineEdit,
    QLabel,
    QMessageBox
)

class PasswordKeypad(QDialog):

    # Initialize hidden password keypad dialog
    def __init__(self, correct_password="1234", parent=None):
        try:
            super().__init__(parent)

            self.correct_password = correct_password
            self.password_value = ""

            self.setWindowTitle("Hidden Access")
            self.setFixedSize(300, 420)
        except Exception as e:
            print(f"Error initializing PasswordKeypad: {e}")

        self.setStyleSheet("""
            QDialog{
                background-color:black;
                border:3px solid #353535;
            }

            QLabel{
                color:white;
                font-size:18px;
                font-weight:bold;
            }

            QLineEdit{
                background:white;
                color:black;
                font-size:22px;
                padding:5px;
                border:2px solid gray;
            }

            QPushButton{
                background-color:#202020;
                color:white;
                font-size:20px;
                border:2px solid gray;
                border-radius:5px;
            }

            QPushButton:pressed{
                background-color:#505050;
            }
        """)

        mainLayout = QVBoxLayout(self)

        # Title
        self.label = QLabel("Enter Password")
        self.label.setAlignment(Qt.AlignCenter)
        mainLayout.addWidget(self.label)

        # Password display
        self.display = QLineEdit()
        self.display.setEchoMode(QLineEdit.Password)
        self.display.setReadOnly(True)
        self.display.setFixedHeight(40)
        mainLayout.addWidget(self.display)

        # Grid buttons
        grid = QGridLayout()

        buttons = [
            ('1', 0, 0),
            ('2', 0, 1),
            ('3', 0, 2),
            ('<-', 0, 3),

            ('4', 1, 0),
            ('5', 1, 1),
            ('6', 1, 2),
            ('C', 1, 3),

            ('7', 2, 0),
            ('8', 2, 1),
            ('9', 2, 2),
            ('0', 2, 3),
        ]

        for text, row, col in buttons:

            button = QPushButton(text)
            button.setFixedSize(60, 60)

            if text == "<-":
                button.clicked.connect(self.backspace)

            elif text == "C":
                button.clicked.connect(self.clearText)

            else:
                button.clicked.connect(
                    lambda checked, t=text: self.addNumber(t)
                )

            grid.addWidget(button, row, col)

        mainLayout.addLayout(grid)

        # OK + Cancel
        okButton = QPushButton("OK")
        okButton.setFixedHeight(50)
        okButton.clicked.connect(self.checkPassword)

        cancelButton = QPushButton("Cancel")
        cancelButton.setFixedHeight(50)
        cancelButton.clicked.connect(self.reject)

        mainLayout.addWidget(okButton)
        mainLayout.addWidget(cancelButton)

    # -----------------------------------
    # ADD NUMBER
    # -----------------------------------
    def addNumber(self, number):
        try:
            self.password_value += number
            self.display.setText(self.password_value)
        except Exception as e:
            print(f"Error adding number to password input: {e}")

    # -----------------------------------
    # BACKSPACE
    # -----------------------------------
    def backspace(self):
        try:
            self.password_value = self.password_value[:-1]
            self.display.setText(self.password_value)
        except Exception as e:
            print(f"Error deleting last character from password input: {e}")

    # -----------------------------------
    # CLEAR
    # -----------------------------------
    def clearText(self):
        try:
            self.password_value = ""
            self.display.setText("")
        except Exception as e:
            print(f"Error clearing password input: {e}")

    # -----------------------------------
    # CHECK PASSWORD
    # -----------------------------------
    def checkPassword(self):
        try:
            if self.password_value == self.correct_password:
                self.accept()
            else:
                QMessageBox.warning(
                    self,
                    "Access Denied",
                    "Wrong Password"
                )
        except Exception as e:
            print(f"Error checking password: {e}")

class UIHandler(QObject):
    """
    Handles:
    - UI visibility
    - Styling
    - Navigation
    - Keyboards
    - Power / menu actions
    """

    # Initialize UI handler and wire application callbacks
    def __init__(self, main_window):
        try:
            super().__init__(parent=None) 
            self.ui = main_window   # 🔑 MainWindow reference
            self.keyboard_open = False

            # self.ui.tabWi dget_2.setCurrentIndex(0)
            # self.ui.stackedWidget_2.setCurrentIndex(0)
            # self.ui.stackedWidget_3.setCurrentIndex(0)
            self.setup_lineedit_keyboards()
            self.apply_line_styles(thickness=3, color="#555555")
            self.linkage_formula_bar()
            self.powerButton()
            self.lineedit_opacity()

            # self.linkage_of_ui()
            self.last_formula_source = None
            self.ui.lineEdit_formulaBar.textChanged.connect(self.ui.utils.validate_formulabar)
            self.toggle_button_eventHandling()
            update_angle_toggle(self.ui)  # initialize toggle state at startup for anglecalculation
            update_rs232_toggle(self.ui) #initialize toggle state at startup for rs232
            update_autooffcet_toggle(self.ui)
            update_networkdatabase_toggle(self.ui)
            update_IOSetting_Buzzer_toggle(self.ui)
            update_IOSetting_Relay_toggle(self.ui)
            update_IOSetting_CycleStopTimer_toggle(self.ui)
            update_IOSetting_AutosaveReading_toggle(self.ui)
            update_IOSetting_PartTraceability_toggle(self.ui)
            update_IOSetting_TimetoMasterSet_toggle(self.ui)
            update_IOSetting_MasterGrouping_toggle(self.ui)
            update_IOSetting_SaveMasterCalibration_toggle(self.ui)
            
            self.apply_masterType_state()
            self.ui.comboBox_masterType.currentTextChanged.connect(self.apply_masterType_state)
            self.ui.comboBox_ovalityOnOff.currentTextChanged.connect(self.apply_ProbeBasedSettings_state)
            self.ui.radioButton_aocEnableOn.toggled.connect(self.apply_aocBasedSettings_state)
            self.ui.radioButton_aocEnableOFF.toggled.connect(self.apply_aocBasedSettings_state)
            self.ui.comboBox_probeFormulaBar.activated.connect(
                lambda: self.set_formula_source("probe")
            )

            self.ui.comboBox_dimenstionFormulaBar.activated.connect(
                lambda: self.set_formula_source("dimension")
            )
            self.ui.tabWidget_2.currentChanged.connect(
                lambda _: self.set_labels_to_header()
            )
            self.setup_logoLongPress()
            self.overlay = None
            self.numkeyboard = None
            self.keyboard = None
            self.ui.button_touchCalibration.clicked.connect(self.touch_Calibration_setup)
            # self.ui.stackedWidget_2.currentChanged.connect(self.update_buttons)
            self.ui.stackedWidget_2.currentChanged.connect(
                lambda _: self.set_labels_to_header()
            )
            self.ui.stackedWidget_3.currentChanged.connect(
                lambda _: self.set_labels_to_header()
            )
            self.ui.label_spcDataCount.hide()
            self.ui.lineEdit_spcDataCount.hide()
        except Exception as e:
            print(f"Error in initializtion of ui_handler : {e}")
    # Request touch calibration by creating a temporary trigger file
    def touch_Calibration_setup(self):
        try:
            open("/tmp/start_touch_calibration", "w").close()
            print("Calibration requested.")
        except Exception as e:
            print(f"Error requesting touch calibration: {e}")
                      
    # Open the part settings screen and reset nested tabs
    def open_part_settings(self):
        try:
            self.ui.stacked.setCurrentIndex(30)
            self.ui.tabWidget_2.setCurrentIndex(0)
            self.ui.stackedWidget_2.setCurrentIndex(0)
            self.ui.stackedWidget_3.setCurrentIndex(0)
        except Exception as e:
            print(f"Error opening part settings: {e}")

    #to enable disable line while switching combobox of Ovality ON and OFF
    def apply_ProbeBasedSettings_state(self):
        try:
            is_off = self.ui.comboBox_ovalityOnOff.currentText() == "OFF"
            self.ui.comboBox_ovalityOnOff.blockSignals(True)
            widgets = [
                self.ui.label_case,
                self.ui.label_caseT,
                self.ui.comboBox_caseProbe,
                self.ui.lineEdit_caseT
            ]
            for w in widgets:
                w.hide() if is_off else w.show()
            self.ui.comboBox_ovalityOnOff.blockSignals(False)
        except Exception as e:
            print(f"Error in probebasedsetting state : {e}") 
    
    def apply_aocBasedSettings_state(self):
        try:
            is_off = self.ui.radioButton_aocEnableOFF.isChecked()
            aoc_settings = self.ui.valueObj.AOCSettings_dict or {}
            main_toggle_on = aoc_settings.get('AOC_ON_OFF', 'OFF') == 'ON'
            should_enable = main_toggle_on and not is_off
            # print("IsOff -> ",is_off)
            # self.ui.comboBox_aocEnableONOFF.blockSignals(True)
            widgets = [
                self.ui.label_axis,self.ui.comboBox_axis,
                self.ui.label_offsetNo,self.ui.lineEdit_offsetNo,
                self.ui.label_upperOffsetLimit,self.ui.lineEdit_upperOffcetLimit,
                self.ui.label_lowerOffsetLimit,self.ui.lineEdit_lowerOffsetLimit,
                self.ui.label_machine,self.ui.comboBox_machine,
                self.ui.label_direction,self.ui.comboBox_direction,
                self.ui.label_turretNo,self.ui.lineEdit_turretNo,
                self.ui.label_workInProcess,self.ui.lineEdit_workInProcess,
                self.ui.label_skipOffsetCount,self.ui.lineEdit_skipOffsetCount

            ]
            for w in widgets:
                w.setEnabled(should_enable)
            # self.ui.comboBox_aocEnableONOFF.blockSignals(False)
        except Exception as e:
            print(f"Error in probebasedsetting state : {e}") 
               
    # Update enabled/disabled state of master type fields based on selection
    def apply_masterType_state(self):
        try:
            self.ui.comboBox_masterType.blockSignals(True)
            
            dimension = self.ui.comboBox_toselectProbe.currentText()
            program_dict = self.ui.valueObj.ProgramSettings_dict or {}
            dim_data = program_dict.get(dimension, {})
            
            probe = dim_data.get("ProbeBasedSettings", {})
            saved_master = probe.get("MasterType", "").strip().lower()
            current_master = self.ui.comboBox_masterType.currentText().strip().lower()
            
            editable = not saved_master or (saved_master == current_master)
            
            single_master = self.ui.comboBox_masterType.currentText() == "Single Master"
            double_master = self.ui.comboBox_masterType.currentText() == "Double Master"
            no_master = self.ui.comboBox_masterType.currentText() == "No Master"

            if editable:
                if single_master:
                    self.ui.lineEdit_masterLower.setDisabled(True)
                    self.ui.lineEdit_master.setEnabled(True)
                    self.ui.lineEdit_masterHigher.setDisabled(True)
                elif double_master:
                    self.ui.lineEdit_masterLower.setEnabled(True)
                    self.ui.lineEdit_master.setDisabled(True)
                    self.ui.lineEdit_masterHigher.setEnabled(True)
                elif no_master:
                    self.ui.lineEdit_masterLower.setDisabled(True)
                    self.ui.lineEdit_master.setDisabled(True)
                    self.ui.lineEdit_masterHigher.setDisabled(True)
                    
            else:
                for w in (
                    self.ui.lineEdit_masterLower,
                    self.ui.lineEdit_master,
                    self.ui.lineEdit_masterHigher
                ):
                    w.setDisabled(True)
            
            self.ui.comboBox_masterType.blockSignals(False)
            
        except Exception as e:
            print("Error in MasterType State:", e)
        
    # Apply disabled opacity styling to master line edits
    def lineedit_opacity(self):
        try:
            style = """
            QLineEdit:disabled {
                background-color: #666666;
                
            }
            """
            self.ui.lineEdit_masterLower.setStyleSheet(style)
            self.ui.lineEdit_master.setStyleSheet(style)
            self.ui.lineEdit_masterHigher.setStyleSheet(style)
        except Exception as e:
            print(f"Error in lineedit opacity: {e}")        

    # Apply styling to line frames in the main UI layout
    # Apply styling to line frames in the main UI layout
    def apply_line_styles(self, thickness=3, color="#555555"):
        """
        Apply thickness and color to all QFrame lines in the central widget.
        Horizontal lines get fixed height, vertical lines get fixed width.
        """
        try:
            # Iterate through all QFrame children of centralwidget
            for line in self.ui.centralwidget.findChildren(QFrame):
                if line.frameShape() == QFrame.HLine:
                    line.setFixedHeight(thickness)
                    line.setStyleSheet(f"background-color: {color};")
                elif line.frameShape() == QFrame.VLine:
                    line.setFixedWidth(thickness)
                    line.setStyleSheet(f"background-color: {color};")
        except Exception as e:
            print(f"Error applying line styles: {e}")

    # -------- NAVIGATION --------
    def linkage_of_ui(self):
        try:
            # Footer Buttons Signals Slots Implementation
            # self.ui.button_back.clicked.connect(self.linkage_of_backButton)
        #     self.ui.button_back.released.connect(lambda checked=False: (
        #         self.linkage_of_backButton(),
        #         self.handle_aocwidget_backButton()
        #     )
        # )
            
        #     self.ui.button_forward.released.connect(lambda checked = False :(
        #                                             self.linkage_of_forwardButton(),
        #                                            self.handle_aocwidget_forwardButton())
        #     )
            self.ui.button_back.released.connect(self.linkage_of_backButton)
            self.ui.button_forward.released.connect(self.linkage_of_forwardButton)
            self.ui.button_home.released.connect(
                lambda: self.ui.stacked.setCurrentIndex(23)
            )
            # self.ui.button_home.clicked.connect(lambda : self.ui.stacked.setCurrentIndex(23))
            # To Be Removed
            self.ui.button_login.released.connect(lambda : self.ui.stacked.setCurrentIndex(23))

            # Dial Indicator Page Clicked Slot
            # self.ui.label_dialIndicatorPage.mousePressEvent = self.on_dial_label_clicked #lambda event: self.ui.stacked.setCurrentIndex(25)
            # self.ui.label_dialIndicatorPage.mousePressEvent = (
            #     lambda event: self.on_dial_label_clicked()
            # )
            self.ui.label_dialIndicatorPage.mousePressEvent = lambda event: self.ui.stacked.setCurrentIndex(25)
            self.ui.label_ioSettingPage.mousePressEvent = lambda event: self.ui.stacked.setCurrentIndex(7)

            # Settings Page Clicked Slot
            self.ui.label_settingsPage.mousePressEvent = lambda event: self.ui.stacked.setCurrentIndex(28)
            self.ui.button_partSettings.released.connect(self.open_part_settings)
            self.ui.button_programList.released.connect(lambda : self.ui.stacked.setCurrentIndex(29))
            self.ui.button_staticSettingsForAll.released.connect(lambda : self.ui.stacked.setCurrentIndex(26))
            self.ui.button_setFormulaSettings.released.connect(lambda : self.ui.stacked.setCurrentIndex(4))
             
            self.ui.button_angleCalculationSetting.released.connect(lambda : self.ui.stacked.setCurrentIndex(27))

            # IO Settings Page Clicked Slot
            # self.ui.label_ioSettingPage.mousePressEvent = lambda event: self.ui.stacked.setCurrentIndex(7)
            self.ui.button_databaseSettings.released.connect(lambda : self.ui.stacked.setCurrentIndex(16))
            self.ui.button_rs232Settings.released.connect(lambda : self.ui.stacked.setCurrentIndex(3))
            #self.ui.button_airSaving.released.connect(lambda : self.ui.stacked.setCurrentIndex(20))
            self.ui.button_ipSettings.released.connect(lambda : self.ui.stacked.setCurrentIndex(5))
            self.ui.button_wifiSettings.released.connect(lambda : self.ui.stacked.setCurrentIndex(6))
            self.ui.button_factoryCalibration.released.connect(lambda : self.ui.stacked.setCurrentIndex(19))

            # AOC Page Clicked Slot
            self.ui.label_autoOffsetSettingPage.mousePressEvent = lambda event: self.ui.stacked.setCurrentIndex(14)
            self.ui.button_cncListAoc.released.connect(lambda : self.ui.stacked.setCurrentIndex(12))
            # self.ui.button_addCncSettings.released.connect(lambda : self.ui.stacked.setCurrentIndex(13))
            # self.ui.button_modifyCncSettings.released.connect(lambda : self.ui.stacked.setCurrentIndex(13))
            self.ui.button_reportsAoc.released.connect(lambda : self.ui.stacked.setCurrentIndex(18))

            # Clock Settings Page Clicked Slot
            self.ui.label_clockSettingsPage.mousePressEvent = lambda event: self.ui.stacked.setCurrentIndex(10)

            # User Management Page Clicked Slot
            self.ui.label_userManagementPage.mousePressEvent = lambda event: self.ui.stacked.setCurrentIndex(1)
           

            # Report Page Clicked Slot
            self.ui.label_reportPage.mousePressEvent = lambda event: self.ui.stacked.setCurrentIndex(21)
            self.ui.button_viewData.released.connect(lambda : self.ui.stacked.setCurrentIndex(22))
            self.ui.button_ListView.released.connect(lambda : self.ui.stackedWidget.setCurrentIndex(0))
            self.ui.button_ChartView.released.connect(lambda : self.ui.stackedWidget.setCurrentIndex(1))
            self.ui.button_HistogramChart.released.connect(lambda : self.ui.stackedWidget.setCurrentIndex(2))

            # About Logo Page Clicked Slot
            # self.ui.label_aboutLogoPage.mousePressEvent = lambda event: self.ui.stacked.setCurrentIndex(9)

            #factory config
            
        except Exception as e:
            print(f"Error linking UI elements: {e}")


    # Handle back button navigation across stacked pages
    def linkage_of_backButton(self):
        try:
            current_index = self.ui.stacked.currentIndex()
            if current_index == 9:
                self.ui.stacked.setCurrentIndex(23)
            elif current_index == 25 :#or current_index == 11 or current_index == 15:
                self.ui.stacked.setCurrentIndex(23)
            elif current_index == 28:
                self.ui.stacked.setCurrentIndex(23)
            # elif current_index == 26:
            #     self.ui.stacked.setCurrentIndex(17)
            elif current_index == 26:
                self.ui.stacked.setCurrentIndex(30)
            elif current_index == 27:
                self.ui.stacked.setCurrentIndex(26)
            elif current_index == 8:
                self.ui.stacked.setCurrentIndex(7)
            elif current_index == 7:
                self.ui.stacked.setCurrentIndex(23)
            elif current_index == 18:
                self.ui.stacked.setCurrentIndex(14)
            elif current_index == 13:
                self.ui.stacked.setCurrentIndex(12)
            elif current_index == 12:
                self.ui.stacked.setCurrentIndex(14)
            elif current_index == 14:
                self.ui.stacked.setCurrentIndex(23)
            elif current_index == 19:
                self.ui.stacked.setCurrentIndex(8)
            elif current_index == 16:
                self.ui.stacked.setCurrentIndex(8)
            elif current_index == 3:
                self.ui.stacked.setCurrentIndex(8)
            elif current_index == 5:
                self.ui.stacked.setCurrentIndex(8)
            elif current_index == 6:
                self.ui.stacked.setCurrentIndex(8)
            elif current_index == 4:
                self.ui.stacked.setCurrentIndex(30)
            elif current_index == 10:
                self.ui.stacked.setCurrentIndex(23)
            elif current_index == 2:
                self.ui.stacked.setCurrentIndex(1)
            elif current_index == 1:
                self.ui.stacked.setCurrentIndex(23)
            elif current_index == 22:
                self.ui.stacked.setCurrentIndex(21)
            elif current_index == 21:
                self.ui.stacked.setCurrentIndex(23)
            elif current_index == 29:
                self.ui.stacked.setCurrentIndex(28)
            elif  current_index == 31:
                self.ui.stacked.setCurrentIndex(25)
            # elif self.ui.stackedWidget_2.currentIndex() == 0:
            #     self.ui.stacked.setCurrentIndex(28)
            # elif self.ui.stackedWidget_2.currentIndex() == 1:
            #     self.ui.stackedWidget_2.setCurrentIndex(0)
            # elif self.ui.stackedWidget_2.currentIndex() == 3:
            #     self.ui.stackedWidget_2.setCurrentIndex(1)
            # elif self.ui.stackedWidget_2.currentIndex() == 4:
            #     self.ui.stackedWidget_2.setCurrentIndex(3)
            elif current_index == 30:
                if self.ui.tabWidget_2.currentIndex() == 0:

                    if self.ui.stackedWidget_2.currentIndex() == 0:
                        self.ui.stacked.setCurrentIndex(28)

                    elif self.ui.stackedWidget_2.currentIndex() == 1:
                        self.ui.stackedWidget_2.setCurrentIndex(0)

                    elif self.ui.stackedWidget_2.currentIndex() == 3:
                        self.ui.stackedWidget_2.setCurrentIndex(1)

                    elif self.ui.stackedWidget_2.currentIndex() == 4:
                        self.ui.stackedWidget_2.setCurrentIndex(3)

                elif self.ui.tabWidget_2.currentIndex() == 1:
                    if self.ui.stackedWidget_3.currentIndex() == 1:
                        self.ui.stackedWidget_3.setCurrentIndex(0)
        
        except Exception as e:
            print(f"Error in linkage_of_backButton: {e}")
    
    # Navigate AOC widget back to the previous view
    def handle_aocwidget_backButton(self):
        try:
            # if  self.ui.tabWidget_2.currentIndex() == 1:
            if self.ui.stackedWidget_3.currentIndex() == 1:
                self.ui.stackedWidget_3.setCurrentIndex(0)
        except Exception as e:
            print(f"Error handling AOC widget back button: {e}")
            
    # Navigate AOC widget forward to the next view
    def handle_aocwidget_forwardButton(self):
        try:
            # if  self.ui.tabWidget_2.currentIndex() == 1:
            if self.ui.stackedWidget_3.currentIndex() == 0:
                self.ui.stackedWidget_3.setCurrentIndex(1)
        except Exception as e:
            print(f"Error handling AOC widget forward button: {e}")
            
    # Handle forward button navigation across stacked pages
    def linkage_of_forwardButton(self):
        try:
            if self.ui.stacked.currentIndex() == 7:
                self.ui.stacked.setCurrentIndex(8)
            # elif self.ui.stackedWidget_2.currentIndex() == 0:
            #     self.ui.stackedWidget_2.setCurrentIndex(1)
            # elif self.ui.stackedWidget_2.currentIndex() == 1:
            #     self.ui.stackedWidget_2.setCurrentIndex(3)
            # # elif self.ui.stackedWidget_2.currentIndex() == 2:
            # #     self.ui.stackedWidget_2.setCurrentIndex(3)
            # elif self.ui.stackedWidget_2.currentIndex() == 3:
            #     self.ui.stackedWidget_2.setCurrentIndex(4)
            elif self.ui.stacked.currentIndex() == 30:

                # Part Settings tab
                if self.ui.tabWidget_2.currentIndex() == 0:
                    if self.ui.stackedWidget_2.currentIndex() == 0:
                        self.ui.stackedWidget_2.setCurrentIndex(1)

                    elif self.ui.stackedWidget_2.currentIndex() == 1:
                        self.ui.stackedWidget_2.setCurrentIndex(3)

                    elif self.ui.stackedWidget_2.currentIndex() == 3:
                        self.ui.stackedWidget_2.setCurrentIndex(4)

                # AOC tab
                elif self.ui.tabWidget_2.currentIndex() == 1:
                    if self.ui.stackedWidget_3.currentIndex() == 0:
                        self.ui.stackedWidget_3.setCurrentIndex(1)
                
        except Exception as e:
            print(f"Error in linkage_of_forwardButton: {e}")
    

    # Install event filters for all toggle buttons to manage custom behavior
    def toggle_button_eventHandling(self):
        try:
            toggle_buttons = [
            self.ui.toggelButton_angleCalculation,
            self.ui.toggleButton_rs232,
            self.ui.toggleButton_aoc,
            self.ui.toggleButton_networkBasedDatabase,
            self.ui.toggleButton_buzzer,
            self.ui.toggelButton_relay,
            self.ui.toggelButton_cycleStopTimer,
            self.ui.toggelButton_autoSaveReading,
            self.ui.toggelButton_partTraceability,
            self.ui.toggleButtontimeToSetMaster,
            self.ui.toggleButton_masterGrouping,
            self.ui.toggleButtonSaveMasterCalibration
            ]

            for btn in toggle_buttons:
                btn.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents, False)
                btn.setMouseTracking(True)
                btn.installEventFilter(self)
        except Exception as e:
            print(f"Error in toggle button eventhandling {e}")    
        

    # -------- KEYBOARD / FORMULA --------
    def setup_lineedit_keyboards(self):
        try:
            # Letter/Keyboard line edits
            letter_lineedits = [
                self.ui.lineEdit_usernameLogin,
                self.ui.lineEdit_programNameSettings,
                self.ui.lineEdit_dimensionName,
                self.ui.lineEdit_passwordLogin,
                self.ui.lineEdit_setUsernameLogin,
                self.ui.lineEdit_setPasswordLogin,
                self.ui.lineEdit_portName,
                self.ui.lineEdit_wifiPassword,
                self.ui.lineEdit_driverNameDb,
                self.ui.lineEdit_serverNameDb,
                self.ui.lineEdit_databaseNameDb,
                self.ui.lineEdit_usernameDb,
                self.ui.lineEdit_passwordDb,
                self.ui.lineEdit_cncName,
                self.ui.lineEdit_wifiSsid,
                self.ui.lineEdit_modelNo

            ]

            # Numeric/Numpad line edits
            numeric_lineedits = [
                self.ui.lineEdit_cncIpAddress,
                self.ui.lineEdit_cncPortNumber,
                self.ui.lineEdit_selfIp,
                self.ui.lineEdit_subnetMask,
                self.ui.lineEdit_leastCount,
                self.ui.lineEdit_defaultGateway,
                self.ui.lineEdit_masterLower,self.ui.lineEdit_master,self.ui.lineEdit_masterHigher,
                self.ui.lineEdit_upperOffcetLimit,self.ui.lineEdit_usl,self.ui.lineEdit_ucl,
                self.ui.lineEdit_nominalValue,self.ui.lineEdit_lcl,self.ui.lineEdit_lsl,
                self.ui.lineEdit_lowerOffsetLimit,self.ui.lineEdit_caseT,
                self.ui.lineEdit_probeSensitivity,
                self.ui.lineEdit_airSensitivityQuotient,
                self.ui.lineEdit_offsetNo,self.ui.lineEdit_turretNo,self.ui.lineEdit_workInProcess,
                self.ui.lineEdit_skipOffsetCount,
                self.ui.lineEdit_relayTime,
                self.ui.lineEdit_cycleTime,
                self.ui.lineEdit_day,self.ui.lineEdit_month,self.ui.lineEdit_year,
                self.ui.lineEdit_hours,self.ui.lineEdit_minutes,
                self.ui.lineEdit_spcDataCount,self.ui.lineEdit_lowerMasterCalibrate,
                self.ui.lineEdit_higherMasterCalibrate,
                self.ui.lineEdit_DurationAutosave,
                self.ui.lineEdit_angleDegree,self.ui.lineEdit_angleMinutes,self.ui.lineEdit_angleSeconds,
                self.ui.lineEdit_toleranceMin,self.ui.lineEdit_toleranceSec,
                self.ui.lineEdit_negativeTolMin,self.ui.lineEdit_negativeTolSec,
                self.ui.lineEdit_distanceMm,
                self.ui.lineEdit_timeToMasterSet,self.ui.lineEdit_Responsiveness,
                self.ui.lineEdit_serialNo
            ]

            for le in letter_lineedits + numeric_lineedits:
                le.installEventFilter(self)

            # Store them as attributes if you need them in eventFilter
            self.ui.letter_lineedits = letter_lineedits
            self.ui.numeric_lineedits = numeric_lineedits
        except Exception as e:
            print(f"Error setting up line edit keyboards: {e}")


    # Insert text at the current cursor position inside the formula bar
    def insert_formula_text(self, text):
        try:
            cursor = self.ui.lineEdit_formulaBar.cursorPosition()
            current_text = self.ui.lineEdit_formulaBar.text()
            new_text = current_text[:cursor] + text + current_text[cursor:]
            self.ui.lineEdit_formulaBar.setText(new_text)
            self.ui.lineEdit_formulaBar.setCursorPosition(cursor + len(text))
        except Exception as e:
            print(f"Error inserting formula text: {e}")

    # Link formula bar buttons to insertion and save actions
    def linkage_formula_bar(self):
        try:
            # Operators
            self.ui.button_plusFormulaBar.clicked.connect(lambda: self.insert_formula_text("+"))
            self.ui.button_minusFormulaBar.clicked.connect(lambda: self.insert_formula_text("-"))
            self.ui.button_multiplicationFormulaBar.clicked.connect(lambda: self.insert_formula_text("*"))
            self.ui.button_divisionFormulaBar.clicked.connect(lambda: self.insert_formula_text("/"))
            self.ui.button_modFormulaBar.clicked.connect(lambda: self.insert_formula_text("%"))
            self.ui.button_commaFormulaBar.clicked.connect(lambda: self.insert_formula_text(","))

            # Digits
            self.ui.button_0FormulaBar.clicked.connect(lambda: self.insert_formula_text("0"))
            self.ui.button_1FormulaBar.clicked.connect(lambda: self.insert_formula_text("1"))
            self.ui.button_2FormulaBar.clicked.connect(lambda: self.insert_formula_text("2"))
            self.ui.button_3FormulaBar.clicked.connect(lambda: self.insert_formula_text("3"))
            self.ui.button_4FormulaBar.clicked.connect(lambda: self.insert_formula_text("4"))
            self.ui.button_5FormulaBar.clicked.connect(lambda: self.insert_formula_text("5"))
            self.ui.button_6FormulaBar.clicked.connect(lambda: self.insert_formula_text("6"))
            self.ui.button_7FormulaBar.clicked.connect(lambda: self.insert_formula_text("7"))
            self.ui.button_8FormulaBar.clicked.connect(lambda: self.insert_formula_text("8"))
            self.ui.button_9FormulaBar.clicked.connect(lambda: self.insert_formula_text("9"))

            # Braces
            self.ui.button_leftBraceFormulaBar.clicked.connect(lambda: self.insert_formula_text("("))
            self.ui.button_rightBraceFormulaBar.clicked.connect(lambda: self.insert_formula_text(")"))

            # Functions
            self.ui.button_maxFormulaBar.clicked.connect(lambda: self.insert_formula_text("max"))
            self.ui.button_minFormulaBar.clicked.connect(lambda: self.insert_formula_text("min"))
            self.ui.button_avgFormulaBar.clicked.connect(lambda: self.insert_formula_text("avg"))
            self.ui.button_absFormulaBar.clicked.connect(lambda: self.insert_formula_text("abs"))

            self.ui.button_sinFormulaBar.clicked.connect(lambda: self.insert_formula_text("sin"))
            self.ui.button_cosFormulaBar.clicked.connect(lambda: self.insert_formula_text("cos"))
            self.ui.button_tanFormulaBar.clicked.connect(lambda: self.insert_formula_text("tan"))
            self.ui.button_cosecFormulaBar.clicked.connect(lambda: self.insert_formula_text("cosec"))
            self.ui.button_secFormulaBar.clicked.connect(lambda: self.insert_formula_text("sec"))
            self.ui.button_cotFormulaBar.clicked.connect(lambda: self.insert_formula_text("cot"))

            # Backspace
            self.ui.button_backspaceFormulaBar.clicked.connect(self.delete_last_character)

            # ComboBox variable insertion
            # self.ui.button_addFormulaBar.clicked.connect(
            #     lambda: self.insert_formula_text(self.ui.comboBox_probeFormulaBar.currentText()),
                         
            # )
            self.ui.button_addFormulaBar.clicked.connect(self.handle_add_formula_click)
            self.ui.button_saveSettingsFormulaBar.clicked.connect(self.save_formula_to_label)
        except Exception as e:
            print(f"Error linking formula bar buttons: {e}")
    # Track which formula source is active (probe or dimension)
    def set_formula_source(self, source):
        try:
            self.last_formula_source = source
        except Exception as e:
            print(f"Error setting formula source: {e}")
    # Handle click on add-formula button and insert selected variable
    def handle_add_formula_click(self):
        try:
            if self.last_formula_source == "probe":
                text = self.ui.comboBox_probeFormulaBar.currentText()

            elif self.last_formula_source == "dimension":
                text = self.ui.comboBox_dimenstionFormulaBar.currentText()

            else:
                # Nothing selected yet
                return

            self.insert_formula_text(text)
        except Exception as e:
            print(f"Error handling add formula click: {e}")

    # Save the current formula text into the formula label and close the keyboard
    def save_formula_to_label(self):
        try:
            self.keyboard_open = False
            if hasattr(self.ui, "current_keyboard") and self.ui.current_keyboard is not None:
                self.ui.current_keyboard.close()
                self.ui.current_keyboard = None
            text = self.ui.lineEdit_formulaBar.text()
            print("Formula to save:", text)
            print("TextEdit reference:", self.ui.label_formulaBar)
            if text:  # only update if not empty
                self.ui.label_formulaBar.setText(text)
                #self.ui.stacked.setCurrentIndex(17)
                self.ui.stacked.setCurrentIndex(30)
                
            else:
                # self.ui.label_formulaBar.setText("")
                if not self.ui.label_formulaBar.text().strip():
                    dim = self.ui.comboBox_toselectProbe.currentText().strip()
                    if dim:
                        self.ui.label_formulaBar.setText(f"P{dim[1:]}")
        except Exception as e:
            print(f"Error saving formula to label: {e}")

    # Remove the last character typed in the formula bar
    def delete_last_character(self):
        try:
            cursor = self.ui.lineEdit_formulaBar.cursorPosition()
            if cursor > 0:
                current_text = self.ui.lineEdit_formulaBar.text()
                new_text = current_text[:cursor-1] + current_text[cursor:]
                self.ui.lineEdit_formulaBar.setText(new_text)
                self.ui.lineEdit_formulaBar.setCursorPosition(cursor-1)
        except Exception as e:
            print(f"Error deleting last character from formula bar: {e}")


    # Applies entered keyboard text to line edit and closes keyboard
    # def apply_keyboard_text(self, lineedit, text,keyboard):
    #     try:
    #         lineedit.setText(text)
    #         lineedit.parentWidget().setFocus()  # shift focus safely
    #         self.keyboard_open = False
    #     except Exception as e:
    #         print(f"Error applying keyboard text: {e}")
    def apply_keyboard_text(self, lineedit, text):
        try:
            lineedit.setText(text)
            lineedit.parentWidget().setFocus()
            self.keyboard_open = False
        except Exception as e:
            print(f"Error applying keyboard text: {e}")
    # Handle cleanup when the keyboard overlay is closed
    def on_keyboard_closed(self):
        try:
            self.keyboard_open = False
            if self.overlay:
                self.overlay.deleteLater()
                self.overlay = None

            self.keyboard = None
        except Exception as e:
            print(f"Error handling keyboard closed: {e}")
    # Called when numpad window is closed (via OK, close button, or X button)
    def on_numpad_closed(self):
        try:
            self.keyboard_open = False
            if self.overlay:
                self.overlay.deleteLater()
                self.overlay = None
            self.numkeyboard = None  
        except Exception as e:
            print(f"Error in on_numpad_closed: {e}")

    # -------- HEADER / LABELS --------
    def set_labels_to_header(self):
        try:
            self.ui.button_home.setEnabled(True)
            self.ui.button_forward.setEnabled(True)
            self.ui.button_back.setEnabled(True)

            current_index = self.ui.stacked.currentIndex()

            # Reset visibility for all buttons to default (show) before specific hides
            self.ui.button_home.show()
            self.ui.button_forward.show()
            self.ui.button_back.show()
            self.ui.button_save.show()
            self.ui.line_header.show()
            self.ui.label_savesignal.hide()
            self.ui.button_ProgIdLoad.hide()
            self.ui.button_ProgIdDelete.hide()
            self.ui.button_shutdown.show() # Assuming it's generally visible unless specified
            self.ui.button_ping.hide()
            self.ui.label_CNCconnectionstatus.hide()
            self.ui.button_history.hide()
            if current_index == 0:
                self.ui.label_pageName.setText("User Login")
                self.ui.button_home.hide()
                self.ui.button_forward.hide()
                self.ui.button_back.hide()
                self.ui.button_save.hide()
                self.ui.button_spcReset.hide()
                self.ui.line_header.hide()
                self.ui.button_shutdown.hide() # Hide shutdown on login page
            elif current_index == 1 :
                self.ui.label_pageName.setText("User Management")
                self.ui.button_save.hide()
                self.ui.button_forward.hide()
                self.ui.button_shutdown.hide()
                self.ui.button_spcReset.hide()
                self.ui.button_back.hide()
            elif current_index == 2:
                self.ui.label_pageName.setText("User Settings")
                self.ui.button_save.hide()
                self.ui.button_forward.hide()
                self.ui.button_home.show()
                self.ui.button_shutdown.hide()
                self.ui.button_spcReset.hide()
            elif current_index == 3:
                self.ui.label_pageName.setText("RS 232 Settings")
                self.ui.button_forward.hide()
                self.ui.button_home.hide()
                self.ui.button_shutdown.hide()
                self.ui.button_spcReset.hide()
            elif current_index == 4:
                self.ui.label_pageName.setText("Formula Settings")
                self.ui.button_save.hide()
                self.ui.button_back.show()
                self.ui.button_forward.hide()
                self.ui.button_home.hide()
                self.ui.button_shutdown.hide()
                self.ui.button_spcReset.hide()
            elif current_index == 5:
                self.ui.label_pageName.setText("IP Settings")
                self.ui.button_forward.hide()
                self.ui.button_home.hide()
                self.ui.button_shutdown.hide()
                self.ui.button_spcReset.hide()
            elif current_index == 6:
                self.ui.label_pageName.setText("Wifi Settings")
                self.ui.button_forward.hide()
                self.ui.button_home.hide()
                self.ui.button_shutdown.hide()
                self.ui.button_spcReset.hide()
            elif current_index == 7: 
                self.ui.label_pageName.setText("I/O Settings")
                self.ui.button_save.hide()
                self.ui.button_home.hide()
                self.ui.button_shutdown.hide()
                self.ui.button_spcReset.hide()
            elif current_index == 8:
                self.ui.label_pageName.setText("I/O Settings")
                self.ui.button_forward.hide()
                self.ui.button_shutdown.hide()
                self.ui.button_spcReset.hide()
            elif current_index == 9:
                self.ui.label_pageName.setText("About")
                self.ui.button_save.hide()
                self.ui.button_forward.hide()
                self.ui.button_shutdown.hide()
                self.ui.button_spcReset.hide()
                self.ui.button_back.hide()
            elif current_index == 10:
                self.ui.label_pageName.setText("Clock Settings")
                self.ui.button_save.hide()
                self.ui.button_forward.hide()
                self.ui.button_shutdown.hide()
                self.ui.button_spcReset.hide()
                self.ui.button_back.hide()
            elif current_index == 12:
                self.ui.label_pageName.setText("CNC List")
                self.ui.button_save.hide()
                self.ui.button_forward.hide()
                self.ui.button_shutdown.hide()
                self.ui.button_spcReset.hide()
                self.ui.button_back.show()
            elif current_index == 13:
                self.ui.label_pageName.setText("CNC Settings")
                self.ui.button_ping.show()
                self.ui.button_forward.hide()
                self.ui.button_home.hide()
                self.ui.button_shutdown.hide()
                self.ui.button_spcReset.hide()
            elif current_index == 14:
                self.ui.label_pageName.setText("Auto Offset Settings")
                self.ui.button_save.show()
                self.ui.button_forward.hide()
                self.ui.button_shutdown.hide()
                self.ui.button_spcReset.hide()
                self.ui.button_back.hide()
            elif current_index == 15:
                self.ui.label_pageName.setText("Super Admin Settings")
                self.ui.button_forward.hide()
                self.ui.button_shutdown.hide()
                self.ui.button_spcReset.hide()
                self.ui.button_back.hide()
            elif current_index == 16:
                self.ui.label_pageName.setText("Database Settings")
                self.ui.button_forward.hide()
                self.ui.button_home.hide()
                self.ui.button_shutdown.hide()
                self.ui.button_spcReset.hide()
            elif current_index == 30:
                self.ui.label_pageName.setText("Part Settings")
                # self.ui.button_forward.show()
                self.ui.button_shutdown.hide()
                self.ui.button_spcReset.hide()
                self.ui.button_home.show()
                if self.ui.tabWidget_2.currentIndex() == 0:
                    page = self.ui.stackedWidget_2.currentIndex()
                    if page in (0, 1, 2, 3):
                        self.ui.button_forward.show()
                        self.ui.button_back.show()
                        self.ui.button_save.hide()

                    elif page == 4:
                        self.ui.button_forward.hide()
                        self.ui.button_back.show()
                        self.ui.button_save.show()
                elif self.ui.tabWidget_2.currentIndex() == 1:
                    aoc_page = self.ui.stackedWidget_3.currentIndex()
                    if aoc_page == 0:
                        self.ui.button_forward.show()
                        self.ui.button_back.show()
                        self.ui.button_save.hide()

                    elif aoc_page == 1:
                        self.ui.button_forward.hide()
                        self.ui.button_back.show()
                        self.ui.button_save.show()
            elif current_index == 18:
                self.ui.label_pageName.setText("AOC Report")
                self.ui.button_save.hide()
                self.ui.button_back.show()
                self.ui.button_forward.hide()
                self.ui.button_shutdown.hide()
                self.ui.button_spcReset.hide()
            elif current_index == 19:
                self.ui.label_pageName.setText("Factory Calibration")
                self.ui.button_save.hide()
                self.ui.button_forward.hide()
                self.ui.button_shutdown.hide()
                self.ui.button_spcReset.hide()
            elif current_index == 21 or current_index == 22:
                self.ui.label_pageName.setText("Reports")
                self.ui.button_save.hide()
                self.ui.button_forward.hide()
                self.ui.button_shutdown.hide()
                self.ui.button_spcReset.hide()
                self.ui.button_back.hide()
            elif current_index == 23:
                self.ui.label_pageName.setText("Home Page")
                self.ui.button_save.hide()
                self.ui.button_back.hide()
                self.ui.button_forward.hide()
                self.ui.button_spcReset.hide()
                self.ui.button_home.hide()
            elif current_index == 25 :#or current_index == 11 or current_index == 15:
                self.ui.label_pageName.setText("Dial Indicator")
                self.ui.button_forward.hide()
                self.ui.button_shutdown.hide()
                self.ui.button_spcReset.show()
                aoc_toggle_state = self.ui.valueObj.activeVariables_dict.get("AOCOnOff", "OFF")
                aoc_enable_on = not self.ui.radioButton_aocEnableOFF.isChecked()
                if aoc_toggle_state == "ON" and aoc_enable_on:
                    self.ui.label_CNCconnectionstatus.show()
                    self.ui.button_history.show()
                # else:
                #     self.ui.label_CNCconnectionstatus.hide()
                #     self.ui.button_history.hide()
                self.ui.button_back.hide()
                
            elif current_index == 26:
                self.ui.label_pageName.setText("Program Settings")
                self.ui.button_save.show()
                self.ui.button_forward.hide()
                self.ui.button_home.hide()
                self.ui.button_shutdown.hide()
                self.ui.button_spcReset.hide()
                # self.ui.button_back.hide()
            elif current_index == 27:
                self.ui.label_pageName.setText("Angle Calculation")
                self.ui.button_forward.hide()
                self.ui.button_home.show()
                self.ui.button_shutdown.hide()
                self.ui.button_spcReset.hide()
            elif current_index == 28:
                self.ui.label_pageName.setText("Settings")
                self.ui.button_save.hide()
                self.ui.button_forward.hide()
                self.ui.button_shutdown.hide()
                self.ui.button_spcReset.hide() 
                self.ui.button_back.hide()
            elif current_index == 29:
                self.ui.label_pageName.setText("Program List")
                self.ui.button_save.hide()
                self.ui.button_forward.hide()
                self.ui.button_shutdown.hide()
                self.ui.button_spcReset.hide()
                self.ui.button_ProgIdLoad.show()
                self.ui.button_ProgIdDelete.show()
                # self.ui.label_date.hide()
                # self.ui.label_time.hide()
                # self.ui.label_pageName.hide()
            elif current_index == 31:
                self.ui.label_pageName.setText("AOC Offset Table")
                self.ui.button_save.hide()
                self.ui.button_forward.hide()
                self.ui.button_shutdown.hide()
                self.ui.button_spcReset.hide()
                self.ui.button_home.show()
               
        except Exception as e:
            print(f"Error in set_labels_to_header: {e}")


    # -------- POWER / MENU --------
    def powerButton(self):
        try:
            # Validate button exists
            if not hasattr(self.ui, 'button_shutdown'):
                print("Error: button_shutdown not found in UI")
                return
            
            # Connect the button to show the menu
            self.ui.button_shutdown.released.connect(self.show_menu)

        except AttributeError as ae:
            print(f"Error: Missing UI attribute in powerButton: {ae}")
        except Exception as e:
            print(f"Error initializing power button menu: {e}")
            
    def show_menu(self):
        dlg = ShutdownMenu(self.ui)
        dlg.exec_()
    
            
        #to manage     
    # Captures mouse press events on line edits to show custom keyboard/numpad
    def eventFilter(self, obj, event):
        try:
                        
            # Handle toggle button click
            if obj == self.ui.toggelButton_angleCalculation and event.type() == event.MouseButtonPress:
                current = self.ui.valueObj.AngleCalculationSettings_dict['ANGLE_CALCULATION_SETTINGS_ON_OFF']
                # Flip the value
                self.ui.valueObj.AngleCalculationSettings_dict['ANGLE_CALCULATION_SETTINGS_ON_OFF'] = 'OFF' if current == 'ON' else 'ON'
                # Update the pixmap and other widgets
                update_angle_toggle(self.ui)
                return True  # Event handled
            
            if obj == self.ui.toggleButton_rs232 and event.type() == event.MouseButtonPress:
                current = self.ui.valueObj.RS232Settings_dict['RS232_ON_OFF']
                # Flip the value
                self.ui.valueObj.RS232Settings_dict['RS232_ON_OFF'] = 'OFF' if current == 'ON' else 'ON'
                # Update the pixmap and other widgets
                update_rs232_toggle(self.ui)
                return True  # Event handled
            
            if obj == self.ui.toggleButton_networkBasedDatabase and event.type() == event.MouseButtonPress:
                current = self.ui.valueObj.NetworkedDatabaseSettings_dict['NETWORKE_BASED_DATABASE_ON_OFF']
                self.ui.valueObj.NetworkedDatabaseSettings_dict['NETWORKE_BASED_DATABASE_ON_OFF'] = 'OFF' if current == 'ON' else 'ON'
                update_networkdatabase_toggle(self.ui)

            if obj == self.ui.toggleButton_aoc and event.type() == event.MouseButtonPress:
                current = self.ui.valueObj.AOCSettings_dict['AOC_ON_OFF']
                # Flip the value
                self.ui.valueObj.AOCSettings_dict['AOC_ON_OFF'] = 'OFF' if current == 'ON' else 'ON'
                # Update the pixmap and other widgets
                update_autooffcet_toggle(self.ui)
                return True  # Event handled
            
            if obj == self.ui.toggleButton_buzzer and event.type() == event.MouseButtonPress:
                current = self.ui.valueObj.IOSettings_dict.get('BUZZER', {}).get('Enable', '0')
                # Flip the value
                self.ui.valueObj.IOSettings_dict['BUZZER']['Enable'] = '0' if current == '1' else '1'
                # Update the pixmap and other widgets
                update_IOSetting_Buzzer_toggle(self.ui)
                return True  # Event handled

            if obj == self.ui.toggelButton_relay and event.type() == event.MouseButtonPress:
                current = self.ui.valueObj.IOSettings_dict.get('RELAY', {}).get('Enable', '0')
                # Flip the value
                self.ui.valueObj.IOSettings_dict['RELAY']['Enable'] = '0' if current == '1' else '1'
                # Update the pixmap and other widgets
                update_IOSetting_Relay_toggle(self.ui)
                return True  # Event handled
            
            if obj == self.ui.toggelButton_cycleStopTimer and event.type() == event.MouseButtonPress:
                current = self.ui.valueObj.IOSettings_dict.get('CYCLE_STOP_TIMER', {}).get('Enable', '0')
                # Flip the value
                self.ui.valueObj.IOSettings_dict['CYCLE_STOP_TIMER']['Enable'] = '0' if current == '1' else '1'
                # Update the pixmap and other widgets
                update_IOSetting_CycleStopTimer_toggle(self.ui)
                return True  # Event handled
            
            if obj == self.ui.toggelButton_autoSaveReading and event.type() == event.MouseButtonPress:
                current = self.ui.valueObj.IOSettings_dict.get('AUTO_SAVE_READING', {}).get('Enable', '0')
                # Flip the value
                self.ui.valueObj.IOSettings_dict['AUTO_SAVE_READING']['Enable'] = '0' if current == '1' else '1'
                # Update the pixmap and other widgets
                update_IOSetting_AutosaveReading_toggle(self.ui)
                return True  # Event handled

            if obj == self.ui.toggelButton_partTraceability and event.type() == event.MouseButtonPress:
                current = self.ui.valueObj.IOSettings_dict.get('PART_TRACEABILITY', {}).get('Enable', '0')
                # Flip the value
                self.ui.valueObj.IOSettings_dict['PART_TRACEABILITY']['Enable'] = '0' if current == '1' else '1'
                # Update the pixmap and other widgets
                update_IOSetting_PartTraceability_toggle(self.ui)
                return True  # Event handled
 
            
            if obj == self.ui.toggleButtontimeToSetMaster and event.type() == event.MouseButtonPress:
                current = self.ui.valueObj.IOSettings_dict.get('TIME_TO_MASTER_SET', {}).get('Enable', '0')
                # Flip the value
                self.ui.valueObj.IOSettings_dict['TIME_TO_MASTER_SET']['Enable'] = '0' if current == '1' else '1'
                # Update the pixmap and other widgets
                update_IOSetting_TimetoMasterSet_toggle(self.ui)
                return True  # Event handled

            if obj == self.ui.toggleButton_masterGrouping and event.type() == event.MouseButtonPress:
                current = self.ui.valueObj.IOSettings_dict.get('MASTER_GROUPING', {}).get('Enable', '0')
                # Flip the value
                self.ui.valueObj.IOSettings_dict['MASTER_GROUPING']['Enable'] = '0' if current == '1' else '1'
                # Update the pixmap and other widgets
                update_IOSetting_MasterGrouping_toggle(self.ui)
                return True  # Event handled
            if obj == self.ui.toggleButtonSaveMasterCalibration and event.type() == event.MouseButtonPress:
                current = self.ui.valueObj.IOSettings_dict.get('SAVE_MASTER_CALIBRATION', {}).get('Enable', 'OFF')
                # Flip the value
                self.ui.valueObj.IOSettings_dict['SAVE_MASTER_CALIBRATION']['Enable'] = 'OFF' if current == 'ON' else 'ON'
                # Update the pixmap and other widgets
                update_IOSetting_SaveMasterCalibration_toggle(self.ui)
                return True  # Event handled

            if isinstance(obj, QtWidgets.QLineEdit) and event.type() == QtCore.QEvent.MouseButtonPress:
                if not obj.isEnabled():  # ✅ skip if disabled
                    return True  # block keyboard/numpad
                
                if getattr(self, "keyboard_open", False):  # already open
                    return True
                self.keyboard_open = True

                if obj in self.ui.letter_lineedits:
                    if self.overlay is None:
                        self.overlay = TouchOverlay(self.ui)

                    if not hasattr(self, "keyboard") or self.keyboard is None:
                        self.keyboard = Keyboard(parent=self.overlay)
                        self.keyboard.keyboardClosed.connect(self.on_keyboard_closed)

                    # Always update target
                    self.keyboard.target_lineedit = obj

                    # Preload current text
                    self.keyboard.input_box.setText(obj.text())

                    # Re-parent in case overlay was recreated
                    self.keyboard.setParent(self.overlay)

                    # Position keyboard
                    self.keyboard.move(
                        (self.overlay.width() - self.keyboard.width()) // 2,
                        self.overlay.height() - self.keyboard.height() - 50
                    )

                    self.keyboard.show()
                    self.keyboard.raise_()
                    self.keyboard.activateWindow()

                    return True
                    # if not hasattr(self, "keyboard") or self.keyboard is None:
                    #     self.keyboard = Keyboard(target_lineedit=obj, parent=self.ui)

                    #     # signals
                    #     # self.keyboard.textEntered.connect(
                    #     #     lambda text, line=obj: self.apply_keyboard_text(line, text)
                    #     # )
                    #     self.keyboard.keyboardClosed.connect(self.on_keyboard_closed)

                    # # 🔑 ALWAYS update target
                    # self.keyboard.target_lineedit = obj

                    # # 🔑 preload text (IMPORTANT)
                    # self.keyboard.input_box.setText(obj.text())

                    # # 🔑 show
                    # self.keyboard.show()
                    # self.keyboard.activateWindow()

                    # return True
                    
                elif obj in self.ui.numeric_lineedits:
                    if not hasattr(self, "overlay") or self.overlay is None:
                        self.overlay = TouchOverlay(self.ui)

                    if not hasattr(self, "numkeyboard") or self.numkeyboard is None:
                        # IMPORTANT: parent is overlay, NOT self.ui
                        self.numkeyboard = numpad_window(parent=self.overlay)
                        self.numkeyboard.numpadClosed.connect(self.on_numpad_closed)

                    self.numkeyboard.target_lineedit = obj
                    self.numkeyboard.Input_box.setText(obj.text())

                    # Center on overlay
                    self.numkeyboard.move(
                        (self.overlay.width() - self.numkeyboard.width()) // 2,
                        self.overlay.height() - self.numkeyboard.height() - 10
                    )

                    self.numkeyboard.show()
                    self.numkeyboard.raise_()
                        # if not hasattr(self, "numkeyboard") or self.numkeyboard is None:
                        #     self.numkeyboard = numpad_window(parent=self.ui,)
                        #     # Connect the numpadClosed signal to reset keyboard_open flag
                        #     self.numkeyboard.numpadClosed.connect(self.on_numpad_closed)

                        # # 🔑 ALWAYS update target
                        # self.numkeyboard.target_lineedit = obj
                        # self.numkeyboard.submit_callback = None
                        # # ✅ FORCE update numpad display
                        # self.numkeyboard.Input_box.setText(obj.text())
                        # # 🔑 SHOW again
                        # if not hasattr(self, "touch_blocker") or self.touch_blocker is None:
                        #     self.touch_blocker = TouchBlocker(self.ui)

                        # self.touch_blocker.raise_()
                        # self.numkeyboard.show()
                        # self.numkeyboard.exec_()
                        #self.raise_()
                    self.numkeyboard.activateWindow()
                        

                    return True   # ✅ VERY IMPORTANT
        except Exception as e:
            print(f"Error in eventFilter: {e}")
        
        return super().eventFilter(obj, event)

    # -----------------------------------
    # SETUP LONG PRESS
    # -----------------------------------
    # Configure long-press handling on the logo to display hidden access
    def setup_logoLongPress(self):
        self.longPressTriggered = False
        # self.hiddenPassword = "431136"

        self.logoPressTimer = QTimer()
        self.logoPressTimer.setSingleShot(True)
        self.logoPressTimer.timeout.connect(self.askHiddenPassword)

        self.ui.label_aboutLogoPage.mousePressEvent = self.logo_mousePressEvent
        self.ui.label_aboutLogoPage.mouseReleaseEvent = self.logo_mouseReleaseEvent


    # -----------------------------------
    # PRESS
    # -----------------------------------
    # Track logo mouse press events for hidden-access long press detection
    def logo_mousePressEvent(self, event):
        try:
            if event.button() == Qt.LeftButton:
                self.longPressTriggered = False
                # Start 5 second timer
                self.logoPressTimer.start(1000)
        except Exception as e:
            print(f"Error during logo mouse press event: {e}")


    # -----------------------------------
    # RELEASE
    # -----------------------------------
    def logo_mouseReleaseEvent(self, event):
        try:
            self.logoPressTimer.stop()

            # Normal click
            if not self.longPressTriggered:
                self.ui.stacked.setCurrentIndex(9)
        except Exception as e:
            print(f"Error during logo mouse release event: {e}")

    # Show the hidden password entry overlay when the logo is long pressed
    def askHiddenPassword(self):
        try:
            self.longPressTriggered = True

            # Hidden lineedit
            self.password_edit = QtWidgets.QLineEdit()
            self.password_edit.setEchoMode(QtWidgets.QLineEdit.Password)

            # Create overlay
            if self.overlay is None:
                self.overlay = TouchOverlay(self.ui)

            # Create numpad if needed
            if self.numkeyboard is None:
                self.numkeyboard = numpad_window(parent=self.overlay)
                self.numkeyboard.numpadClosed.connect(self.on_numpad_closed)

            # Target
            self.numkeyboard.target_lineedit = self.password_edit

            # Clear old text
            self.numkeyboard.Input_box.clear()

            # Callback after OK pressed
            self.numkeyboard.submit_callback = self.verifyHiddenPassword

            # Position
            self.numkeyboard.move(
                (self.overlay.width() - self.numkeyboard.width()) // 2,
                self.overlay.height() - self.numkeyboard.height() - 10
            )

            self.numkeyboard.show()
            self.numkeyboard.raise_()
            self.numkeyboard.activateWindow()
        except Exception as e:
            print(f"Error in askHiddenPassword -> {e}")
            
    # Verify hidden access password and open hidden admin page
    def verifyHiddenPassword(self):
        try:
            entered_password = self.password_edit.text()

            if entered_password == "431136":
                self.ui.stacked.setCurrentIndex(15)
            else:
                msg = CustomMessageBox("Wrong Password", "warning",
                                       parent=self.ui)
                msg.exec_()
        except Exception as e:
            print(f"Error verifying hidden password: {e}")
        
class ShutdownMenu(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setGeometry(parent.rect())
        self.ui = parent   
        self.setWindowFlags(
            Qt.FramelessWindowHint |
            Qt.WindowStaysOnTopHint |
            Qt.CustomizeWindowHint
        )

        self.setWindowModality(Qt.ApplicationModal)

        self.setStyleSheet("""
        QDialog{
            background-color: rgba(0,0,0,0);
        }

        #mainWidget{
            background:black;
            border:2px solid gray;
        }
        """)

        # Main layout (centers popup)
        self.panel = QtWidgets.QWidget(self)
        self.panel.setObjectName("mainWidget")
        self.panel.setFixedSize(300, 230)

        self.panel.setStyleSheet("""
        #mainWidget{
            background:black;
            border:2px solid gray;
        }
        """)

        # Popup frame
        frame = QtWidgets.QFrame()
        frame.setFixedSize(300, 230)
        frame.setStyleSheet("""
            QFrame {
                background-color: black;
                border: 1px solid gray;
                border-radius: 2px;
            }
        """)

        layout = QtWidgets.QVBoxLayout(self.panel)
        layout.setContentsMargins(10,10,10,10)
        layout.setSpacing(5)

        
        # Buttons
        self.btn_shutdown = QtWidgets.QPushButton("Shutdown")
        self.btn_reboot = QtWidgets.QPushButton("Restart")
        self.btn_logout = QtWidgets.QPushButton("Logout")
        self.btn_cancel = QtWidgets.QPushButton("Cancel")

        button_style = """
            QPushButton {
                background-color: black;
                color: white;
                border: 1px solid gray;
                border-radius: 2px;
                font: 15pt "MS Shell Dlg 2";
                min-height: 35px;
            }

            QPushButton:hover {
                background-color: #303030;
            }

            QPushButton:pressed {
                background-color: #505050;
            }
        """

        for btn in (self.btn_shutdown, self.btn_reboot,self.btn_logout, self.btn_cancel):
            btn.setStyleSheet(button_style)
            layout.addWidget(btn)


        # Connections
        self.btn_shutdown.released.connect(self.shutdown)
        self.btn_reboot.released.connect(self.restart)
        self.btn_logout.released.connect(self.logout)
        self.btn_cancel.released.connect(self.reject)
        
         
    # Prompt the user to confirm logout action
    def logout(self):
        try:
            self.accept()      # closes menu first
            logout_dlg = CustomMessageBox("Do you really want to logout?", "info",
                                          parent=self.ui)
            logout_dlg.accepted.connect(self.handle_logout)
            logout_dlg.exec_()   # Wait for user to press OK
        except Exception as e:
            print(f"Error showing logout dialog: {e}")

    # Prompt the user to confirm shutdown action
    def shutdown(self):
        try:
            self.accept()      # closes menu first
            shudtdown_dlg = CustomMessageBox("Do you really want to Shutdown?", "info",
                                             parent=self.ui)
            # Connect the 'Yes' or 'OK' button to the actual shutdown
            shudtdown_dlg.accepted.connect(self.handle_shutdown)  # runs when user clicks Yes/OK                      
            shudtdown_dlg.exec_()   # Wait for user to press OK
            #print("Shutdown clicked")
        except Exception as e:
            print(f"Error showing shutdown dialog: {e}")

    # Prompt the user to confirm restart action
    def restart(self):
        try:
            self.accept()      # closes menu first
            restart_dlg = CustomMessageBox("Do you really want to Restart?", "info",
                                           parent=self.ui)
            restart_dlg.accepted.connect(self.handle_restart)                        
            restart_dlg.exec_()   # Wait for user to press OK
            #("Restart clicked")
        except Exception as e:
            print(f"Error showing restart dialog: {e}")

    # Perform logout cleanup and return to login screen
    def handle_logout(self):
        try:
            # Clear login fields
            self.ui.lineEdit_usernameLogin.clear()
            self.ui.lineEdit_passwordLogin.clear()
            self.ui.stacked.setCurrentIndex(0) #to hadle logout 
        except Exception as e:
            print(f"Error during logout: {e}")
        

    # Called when the shutdown menu item is confirmed
    def handle_shutdown(self):
        """
        Called when the shutdown button is pressed.
        Delegates the shutdown to Utilities class.
        """
        try:
            # Call the shutdown function from utils
            self.ui.utils.shutdown_device()
        except Exception as e:
            print(f"Error during shutdown: {e}")
            msg = CustomMessageBox("Failed to shutdown device. Please try again.", "error",parent=self.ui)
            msg.exec_()
            
    # Called when the restart menu item is confirmed
    def handle_restart(self):
        """
        Called when the reboot button is pressed.
        Delegates the rebbot to Utilities class.
        """
        try:
            # Call the reboot function from utils
            self.ui.utils.restart_device()
        except Exception as e:
            print(f"Error during restart: {e}")
            msg = CustomMessageBox("Failed to restart device. Please try again.", "error",
                                   parent=self.ui)
            msg.exec_()
    
    def exec_(self):
        try:
            if self.parent():
                self.setGeometry(self.parent().rect())
            else:
                self.setGeometry(
                    QtWidgets.QApplication.primaryScreen().geometry()
                )

            self.panel.move(
                (self.width() - self.panel.width()) // 2,
                (self.height() - self.panel.height()) // 2
            )

            return super().exec_()
        except Exception as e:
            print(f"Error executing ShutdownMenu dialog: {e}")