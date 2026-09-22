# ui_handler.py
from PySide2.QtWidgets import QApplication, QMainWindow, QStackedWidget , QWidget
from PySide2.QtWidgets import QFrame
from PySide2.QtWidgets import QLineEdit
from PySide2 import QtCore, QtWidgets
from PySide2.QtCore import QTimer, QTime, QDate , QObject , QThread , Signal, Qt, QCoreApplication
from PySide2.QtGui import QPixmap
from sqlalchemy.orm import *
from letters_keypad import Keyboard
from messageBox import CustomMessageBox
from numpad import numpad_window
from factory_config import FactoryConfig
from models import *
from active_ui_handler import *

class UIHandler(QObject):
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
            super().__init__()
            self.ui = main_window   # 🔑 MainWindow reference
            self.keyboard_open = False
            self.setup_lineedit_keyboards()
            self.apply_line_styles(thickness=3, color="#555555")
            self.linkage_formula_bar()
            self.powerButton()
            self.lineedit_opacity()
            self.linkage_of_ui()
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

            self.ui.comboBox_masterType.currentTextChanged.connect(self.apply_masterType_state)
            self.ui.comboBox_ovalityOnOff.currentTextChanged.connect(self.apply_ProbeBasedSettings_state)
        except Exception as e:
            print(f"Error in initializtion of ui_handler : {e}")

        
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
               
    def apply_masterType_state(self):
        try:
            dimension = self.ui.comboBox_toselectProbe.currentText()
            dim_data = self.ui.valueObj.ProgramSettings_dict.get(dimension)
            probe = dim_data.get("ProbeBasedSettings", {})
            saved_master = probe.get("MasterType", "").strip().lower()
            current_master = self.ui.comboBox_masterType.currentText().strip().lower()
            self.ui.comboBox_masterType.blockSignals(True)
            if not saved_master:
                editable = True          # new dimension → allow edit
            else:
                editable = (saved_master == current_master)
            

            for w in (
                self.ui.lineEdit_masterLower,
                self.ui.lineEdit_master,
                self.ui.lineEdit_masterHigher
            ):
                w.setEnabled(editable)
            self.ui.comboBox_masterType.blockSignals(False)
        except Exception as e:
            print("Error in MasterType State:",e)

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
            self.ui.button_back.clicked.connect(self.linkage_of_backButton)
            self.ui.button_forward.clicked.connect(self.linkage_of_forwardButton)
            self.ui.button_home.clicked.connect(lambda : self.ui.stacked.setCurrentIndex(23))

            # To Be Removed
            self.ui.button_login.clicked.connect(lambda : self.ui.stacked.setCurrentIndex(23))

            # Dial Indicator Page Clicked Slot
            self.ui.label_dialIndicatorPage.mousePressEvent = lambda event: self.ui.stacked.setCurrentIndex(25)
            
            # Settings Page Clicked Slot
            self.ui.label_settingsPage.mousePressEvent = lambda event: self.ui.stacked.setCurrentIndex(28)
            self.ui.button_partSettings.clicked.connect(lambda : self.ui.stacked.setCurrentIndex(30))
            self.ui.button_programList.clicked.connect(lambda : self.ui.stacked.setCurrentIndex(29))
            self.ui.button_staticSettingsForAll.clicked.connect(lambda : self.ui.stacked.setCurrentIndex(26))
            self.ui.button_setFormulaSettings.clicked.connect(lambda : self.ui.stacked.setCurrentIndex(4))
             


            self.ui.button_angleCalculationSetting.clicked.connect(lambda : self.ui.stacked.setCurrentIndex(27))

            # IO Settings Page Clicked Slot
            self.ui.label_ioSettingPage.mousePressEvent = lambda event: self.ui.stacked.setCurrentIndex(7)
            self.ui.button_databaseSettings.clicked.connect(lambda : self.ui.stacked.setCurrentIndex(16))
            self.ui.button_rs232Settings.clicked.connect(lambda : self.ui.stacked.setCurrentIndex(3))
            #self.ui.button_airSaving.clicked.connect(lambda : self.ui.stacked.setCurrentIndex(20))
            self.ui.button_ipSettings.clicked.connect(lambda : self.ui.stacked.setCurrentIndex(5))
            self.ui.button_wifiSettings.clicked.connect(lambda : self.ui.stacked.setCurrentIndex(6))
            self.ui.button_factoryCalibration.clicked.connect(lambda : self.ui.stacked.setCurrentIndex(19))

            # AOC Page Clicked Slot
            self.ui.label_autoOffsetSettingPage.mousePressEvent = lambda event: self.ui.stacked.setCurrentIndex(14)
            self.ui.button_cncListAoc.clicked.connect(lambda : self.ui.stacked.setCurrentIndex(12))
            self.ui.button_addCncSettings.clicked.connect(lambda : self.ui.stacked.setCurrentIndex(13))
            self.ui.button_modifyCncSettings.clicked.connect(lambda : self.ui.stacked.setCurrentIndex(13))
            self.ui.button_reportsAoc.clicked.connect(lambda : self.ui.stacked.setCurrentIndex(18))

            # Clock Settings Page Clicked Slot
            self.ui.label_clockSettingsPage.mousePressEvent = lambda event: self.ui.stacked.setCurrentIndex(10)

            # User Management Page Clicked Slot
            self.ui.label_userManagementPage.mousePressEvent = lambda event: self.ui.stacked.setCurrentIndex(1)
            self.ui.button_addLoginDetails.clicked.connect(lambda : self.ui.stacked.setCurrentIndex(2))
            self.ui.button_modifyLogin.clicked.connect(lambda : self.ui.stacked.setCurrentIndex(2))

            # Report Page Clicked Slot
            self.ui.label_reportPage.mousePressEvent = lambda event: self.ui.stacked.setCurrentIndex(21)
            self.ui.button_viewData.clicked.connect(lambda : self.ui.stacked.setCurrentIndex(22))
            self.ui.button_ListView.clicked.connect(lambda : self.ui.stackedWidget.setCurrentIndex(0))
            self.ui.button_ChartView.clicked.connect(lambda : self.ui.stackedWidget.setCurrentIndex(1))
            self.ui.button_HistogramChart.clicked.connect(lambda : self.ui.stackedWidget.setCurrentIndex(2))

            # About Logo Page Clicked Slot
            self.ui.label_aboutLogoPage.mousePressEvent = lambda event: self.ui.stacked.setCurrentIndex(9)

            #factory config
            #factory_con = FactoryConfig()
            self.ui.button_factoryConfig.clicked.connect(lambda: FactoryConfig().exec_())
        except Exception as e:
            print(f"Error linking UI elements: {e}")


    def linkage_of_backButton(self):
        try:
            current_index = self.ui.stacked.currentIndex()
            if current_index == 9:
                self.ui.stacked.setCurrentIndex(23)
            elif current_index == 25:
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
            elif self.ui.stackedWidget_2.currentIndex() == 1:
                self.ui.stackedWidget_2.setCurrentIndex(0)
            elif self.ui.stackedWidget_2.currentIndex() == 3:
                self.ui.stackedWidget_2.setCurrentIndex(2)
            elif self.ui.stackedWidget_2.currentIndex() == 4:
                self.ui.stackedWidget_2.setCurrentIndex(3)
            elif self.ui.stackedWidget_2.currentIndex() == 2:
                self.ui.stackedWidget_2.setCurrentIndex(1)
        except Exception as e:
            print(f"Error in linkage_of_backButton: {e}")
            
    def linkage_of_forwardButton(self):
        try:
            if self.ui.stacked.currentIndex() == 7:
                self.ui.stacked.setCurrentIndex(8)
            elif self.ui.stackedWidget_2.currentIndex() == 0:
                self.ui.stackedWidget_2.setCurrentIndex(1)
            elif self.ui.stackedWidget_2.currentIndex() == 1:
                self.ui.stackedWidget_2.setCurrentIndex(2)
            elif self.ui.stackedWidget_2.currentIndex() == 2:
                self.ui.stackedWidget_2.setCurrentIndex(3)
            elif self.ui.stackedWidget_2.currentIndex() == 3:
                self.ui.stackedWidget_2.setCurrentIndex(4)
        except Exception as e:
            print(f"Error in linkage_of_forwardButton: {e}")
    
        
    def linkage_of_forwardSetting(self):
        try:
            if self.ui.stackedWidget_2.currentIndex() == 0:
                self.ui.stackedWidget_2.setCurrentIndex(1)
            elif self.ui.stackedWidget_2.currentIndex() == 1:
                self.ui.stackedWidget_2.setCurrentIndex(2)
            elif self.ui.stackedWidget_2.currentIndex() == 2:
                self.ui.stackedWidget_2.setCurrentIndex(3)
        except Exception as e :
            print(f"Error in linkage_of_forwardSettings: {e}")

    def linkage_of_backSettings(self):
        try:
            if self.ui.stackedWidget_2.currentIndex() == 1:
                self.ui.stackedWidget_2.setCurrentIndex(0)
            elif self.ui.stackedWidget_2.currentIndex() == 3:
                self.ui.stackedWidget_2.setCurrentIndex(2)
            elif self.ui.stackedWidget_2.currentIndex() == 2:
                self.ui.stackedWidget_2.setCurrentIndex(1)
        except Exception as e :
           print(f"Error in linkage_of_backSettings")

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
            self.ui.toggleButton_masterGrouping
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
                self.ui.lineEdit_wifiSsid

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
                self.ui.lineEdit_offsetNo,self.ui.lineEdit_turretNo,self.ui.lineEdit_bufferPartNo,
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
                self.ui.lineEdit_timeToMasterSet
            ]

            for le in letter_lineedits + numeric_lineedits:
                le.installEventFilter(self)

            # Store them as attributes if you need them in eventFilter
            self.ui.letter_lineedits = letter_lineedits
            self.ui.numeric_lineedits = numeric_lineedits
        except Exception as e:
            print(f"Error setting up line edit keyboards: {e}")


    def insert_formula_text(self, text):
        try:
            cursor = self.ui.lineEdit_formulaBar.cursorPosition()
            current_text = self.ui.lineEdit_formulaBar.text()
            new_text = current_text[:cursor] + text + current_text[cursor:]
            self.ui.lineEdit_formulaBar.setText(new_text)
            self.ui.lineEdit_formulaBar.setCursorPosition(cursor + len(text))
        except Exception as e:
            print(f"Error inserting formula text: {e}")

    def linkage_formula_bar(self):
        try:
            # Operators
            self.ui.button_plusFormulaBar.clicked.connect(lambda: self.insert_formula_text("+"))
            self.ui.button_minusFormulaBar.clicked.connect(lambda: self.insert_formula_text("-"))
            self.ui.button_multiplicationFormulaBar.clicked.connect(lambda: self.insert_formula_text("*"))
            self.ui.button_divisionFormulaBar.clicked.connect(lambda: self.insert_formula_text("/"))
            self.ui.button_modFormulaBar.clicked.connect(lambda: self.insert_formula_text("%"))
            self.ui.button_commaFormulaBar.clicked.connect(lambda: self.insert_formula_text(","))

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
            self.ui.button_addFormulaBar.clicked.connect(
                lambda: self.insert_formula_text(self.ui.comboBox_probeFormulaBar.currentText())
            )
            self.ui.button_saveSettingsFormulaBar.clicked.connect(self.save_formula_to_label)
        except Exception as e:
            print(f"Error linking formula bar buttons: {e}")
        

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
                self.ui.label_formulaBar.setText("No formula set")
        except Exception as e:
            print(f"Error saving formula to label: {e}")

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
    def apply_keyboard_text(self, lineedit, text,keyboard):
        try:
            lineedit.setText(text)
            lineedit.parentWidget().setFocus()  # shift focus safely
            self.keyboard_open = False
        except Exception as e:
            print(f"Error applying keyboard text: {e}")

    # Called when numpad window is closed (via OK, close button, or X button)
    def on_numpad_closed(self):
        try:
            self.keyboard_open = False
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
            self.ui.button_shutdown.show() # Assuming it's generally visible unless specified
          

            if current_index == 0:
                self.ui.label_pageName.setText("User Login")
                self.ui.button_home.hide()
                self.ui.button_forward.hide()
                self.ui.button_back.hide()
                self.ui.button_save.hide()
                self.ui.button_shutdown.hide() # Hide shutdown on login page

            elif current_index == 1 :
                self.ui.label_pageName.setText("User Management")
                self.ui.button_save.hide()
                self.ui.button_forward.hide()
                self.ui.button_shutdown.hide()
            elif current_index == 2:
                self.ui.label_pageName.setText("User Settings")
                self.ui.button_save.hide()
                self.ui.button_forward.hide()
                self.ui.button_home.hide()
                self.ui.button_shutdown.hide()
            elif current_index == 3:
                self.ui.label_pageName.setText("RS 232 Settings")
                self.ui.button_forward.hide()
                self.ui.button_home.hide()
                self.ui.button_shutdown.hide()
            elif current_index == 4:
                self.ui.label_pageName.setText("Formula Settings")
                self.ui.button_save.hide()
                self.ui.button_back.hide()
                self.ui.button_forward.hide()
                self.ui.button_home.hide()
                self.ui.button_shutdown.hide()
            elif current_index == 5:
                self.ui.label_pageName.setText("IP Settings")
                self.ui.button_forward.hide()
                self.ui.button_home.hide()
                self.ui.button_shutdown.hide()
            elif current_index == 6:
                self.ui.label_pageName.setText("Wifi Settings")
                self.ui.button_forward.hide()
                self.ui.button_home.hide()
                self.ui.button_shutdown.hide()
            elif current_index == 7: 
                self.ui.label_pageName.setText("I/O Settings")
                self.ui.button_save.hide()
                self.ui.button_home.hide()
                self.ui.button_shutdown.hide()
            elif current_index == 8:
                self.ui.label_pageName.setText("I/O Settings")
                self.ui.button_forward.hide()
                self.ui.button_shutdown.hide()
            elif current_index == 9:
                self.ui.label_pageName.setText("About")
                self.ui.button_save.hide()
                self.ui.button_forward.hide()
                self.ui.button_shutdown.hide()
            elif current_index == 10:
                self.ui.label_pageName.setText("Clock Settings")
                self.ui.button_save.hide()
                self.ui.button_forward.hide()
                self.ui.button_shutdown.hide()
            elif current_index == 12:
                self.ui.label_pageName.setText("CNC List")
                self.ui.button_save.hide()
                self.ui.button_forward.hide()
                self.ui.button_shutdown.hide()
            elif current_index == 13:
                self.ui.label_pageName.setText("CNC Settings")
                self.ui.button_forward.hide()
                self.ui.button_home.hide()
                self.ui.button_shutdown.hide()
            elif current_index == 14:
                self.ui.label_pageName.setText("Auto Offset Settings")
                self.ui.button_save.hide()
                self.ui.button_forward.hide()
                self.ui.button_shutdown.hide()
            elif current_index == 16:
                self.ui.label_pageName.setText("Database Settings")
                self.ui.button_forward.hide()
                self.ui.button_home.hide()
                self.ui.button_shutdown.hide()
            elif current_index == 30:
                self.ui.label_pageName.setText("Part Settings")
                self.ui.button_forward.show()
                self.ui.button_home.show()
                self.ui.button_back.show()
                self.ui.button_shutdown.hide()
            elif current_index == 18:
                self.ui.label_pageName.setText("AOC Report")
                self.ui.button_save.hide()
                self.ui.button_back.hide()
                self.ui.button_forward.hide()
                self.ui.button_shutdown.hide()
            elif current_index == 19:
                self.ui.label_pageName.setText("Factory Calibration")
                self.ui.button_save.hide()
                self.ui.button_forward.hide()
                self.ui.button_shutdown.hide()
            elif current_index == 21 or current_index == 22:
                self.ui.label_pageName.setText("Reports")
                self.ui.button_save.hide()
                self.ui.button_forward.hide()
                self.ui.button_shutdown.hide()
            elif current_index == 23:
                self.ui.label_pageName.setText("Home Page")
                self.ui.button_save.hide()
                self.ui.button_back.hide()
                self.ui.button_forward.hide()
            elif current_index == 25:
                self.ui.label_pageName.setText("Dial Indicator")
                self.ui.button_forward.hide()
                self.ui.button_shutdown.hide()
                self.ui.label_value3.hide()
                self.ui.label_value4.hide()
            elif current_index == 26:
                self.ui.label_pageName.setText("Program Settings")
                self.ui.button_save.show()
                self.ui.button_forward.hide()
                self.ui.button_home.hide()
                self.ui.button_shutdown.hide()
            elif current_index == 27:
                self.ui.label_pageName.setText("Angle Calculation")
                self.ui.button_forward.hide()
                self.ui.button_home.show()
                self.ui.button_shutdown.hide()
            elif current_index == 28:
                self.ui.label_pageName.setText("Settings")
                self.ui.button_save.hide()
                self.ui.button_forward.hide()
                self.ui.button_shutdown.hide()
                
                
            elif current_index == 29:
                self.ui.label_pageName.setText("Program List")
                self.ui.button_save.hide()
                self.ui.button_forward.hide()
                self.ui.button_shutdown.hide()
        except Exception as e:
            print(f"Error in set_labels_to_header: {e}")


    # -------- POWER / MENU --------
    def powerButton(self):
        try:
            # Connect the button to show the menu
            self.ui.button_shutdown.clicked.connect(self.show_menu)

            # Create the menu
            self.ui.menu = QtWidgets.QMenu()
            self.ui.menu.setStyleSheet("""
                QMenu {
                    background-color: #2d2d2d;
                    color: white;F
                    font: 16pt "MS Shell Dlg 2";
                }
                QMenu::item:selected {
                    background-color: #555555;
                }
            """)

            # Add actions immediately after creating the menu
            self.ui.menu.addAction("Logout", self.logout)
            self.ui.menu.addAction("Shutdown", self.shutdown)
            self.ui.menu.addAction("Restart", self.restart)
        except Exception as e:
            print(f"Error initializing power button menu: {e}")

    def show_menu(self):
        try:
            # Position menu below button
            self.ui.menu.setMinimumWidth(200)  # make a little wider if you want
            pos = self.ui.button_shutdown.mapToGlobal(
            QtCore.QPoint(0, self.ui.button_shutdown.height() - 50)  # -30 moves menu UP
            )
            self.ui.menu.exec_(pos)
        except Exception as e:
            print(f"Error showing power menu: {e}")

    def logout(self):
        try:
            logout_dlg = CustomMessageBox("  Do you really want to logout?", "info",
                                          parent=self.ui)
            logout_dlg.accepted.connect(self.handle_logout)
            logout_dlg.exec_()   # Wait for user to press OK
        except Exception as e:
            print(f"Error showing logout dialog: {e}")

    def shutdown(self):
        try:
            shudtdown_dlg = CustomMessageBox("  Do you really want to Shutdown?", "info",
                                             parent=self.ui)
            # Connect the 'Yes' or 'OK' button to the actual shutdown
            shudtdown_dlg.accepted.connect(self.handle_shutdown)  # runs when user clicks Yes/OK                      
            shudtdown_dlg.exec_()   # Wait for user to press OK
            #print("Shutdown clicked")
        except Exception as e:
            print(f"Error showing shutdown dialog: {e}")

    def restart(self):
        try:
            restart_dlg = CustomMessageBox("  Do you really want to Restart?", "info",
                                           parent=self.ui)
            restart_dlg.accepted.connect(self.handle_restart)                        
            restart_dlg.exec_()   # Wait for user to press OK
            #("Restart clicked")
        except Exception as e:
            print(f"Error showing restart dialog: {e}")

    def handle_logout(self):
        try:
            self.ui.stacked.setCurrentIndex(0) #to hadle logout 
        except Exception as e:
            print(f"Error during logout: {e}")
        

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
            
            if isinstance(obj, QtWidgets.QLineEdit) and event.type() == QtCore.QEvent.MouseButtonPress:
                if not obj.isEnabled():  # ✅ skip if disabled
                    return True  # block keyboard/numpad
                
                if getattr(self, "keyboard_open", False):  # already open
                    return True
                self.keyboard_open = True

                if obj in self.ui.letter_lineedits:
                    keyboard = Keyboard(parent=self.ui)
                    keyboard.textEntered.connect(lambda text, line=obj: self.apply_keyboard_text(line, text, keyboard))
                    keyboard.show()
                    return True  # block normal focus behavior (prevents cursor)
                
                elif obj in self.ui.numeric_lineedits:
                    if not hasattr(self, "numkeyboard") or self.numkeyboard is None:
                        self.numkeyboard = numpad_window(parent=self.ui)
                        # Connect the numpadClosed signal to reset keyboard_open flag
                        self.numkeyboard.numpadClosed.connect(self.on_numpad_closed)

                    # 🔑 ALWAYS update target
                    self.numkeyboard.target_lineedit = obj
                    

                    # 🔑 SHOW again
                    self.numkeyboard.show()
                    #self.raise_()
                    self.numkeyboard.activateWindow()
                    

                    return True   # ✅ VERY IMPORTANT
        except Exception as e:
            print(f"Error in eventFilter: {e}")
        
        return super().eventFilter(obj, event)

