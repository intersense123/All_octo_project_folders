from PySide2.QtWidgets import QApplication,  QMainWindow, QStackedWidget
from PySide2.QtWidgets import QFrame
from PySide2.QtWidgets import QLineEdit
from PySide2 import QtCore, QtWidgets
from PySide2.QtCore import QTimer, QTime, QDate
from PySide2.QtGui import QPixmap

import sys
# import the generated UI class
from main_ui_17 import Ui_MainWindow
from letters_keypad import MobileKeyboard
from numpad import numpad_window
from factory_config import FactoryConfig
from messageBox import CustomMessageBox
from value import Value
from database import DatabaseAgent
from utilities import Utilities


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):#, gif_labels: dict):
        super().__init__()
        self.setupUi(self)  # setup UI
        self.setup_lineedit_keyboards()
        self.linkage_formula_bar()
        self.powerButton()
       
        # 🔑 Set stacked widget page index
        self.stacked: QStackedWidget = getattr(self, "stackedWidget_main", None)
        self.keyboard_open = False
        if self.stacked:
            # Connecting Slot When Page Changes
            self.stacked.currentChanged.connect(self.set_labels_to_header)
            self.stacked.setCurrentIndex(0)  # second page

        self.linkage_of_ui()
        self.apply_line_styles(thickness=3, color="#555555")
        # self.showFullScreen()
        self.valueObj = Value() #instance created for Value class
        self.databaseObj = DatabaseAgent() #instance/object created for DatabaseAgent class
        self.utils = Utilities()
        self.load_databases()
        self.button_save.clicked.connect(self.linkage_of_saveButton)

    # save button link to set ui value to database
    def linkage_of_saveButton(self):
        if self.stacked.currentIndex() == 6:
            self.save_toDatabase_WifiSettings() #to save wifiSettings using save button
        elif self.stacked.currentIndex() == 2:
            self.save_toDatabase_userManagement()
        elif self.stacked.currentIndex() == 13:
            self.save_toDatabase_cncList()
        elif self.stacked.currentIndex() == 7 or self.stacked.currentIndex() == 8:
            self.save_toDatabase_IOSettings()
        elif self.stacked.currentIndex() == 5: 
            self.save_toDatabase_IpSettings()
        elif  self.stacked.currentIndex() == 3:
            self.save_toDatabase_rs232Settings()
        elif self.stacked.currentIndex() == 27:
            self.save_toDatabase_angleCalculationSettings()
        elif self.stacked.currentIndex() == 17:
            self.save_toDatabase_programSetting()
            self.save_toDatabase_aocBasedSettings()
            self.save_toDatabase_probeBasedSettings()
            

        elif self.stacked.currentIndex() == 14 or self.stacked.currentIndex() == 18:
            self.button_spcDataCount.clicked.connect(self.save_toDatabase_aocSettings)
        elif self.stacked.currentIndex() == 10:
            self.button_setShiftTimings.clicked.connect(self.save_toDatabase_shiftSettings)
        elif self.stacked.currentIndex() == 16:
            self.button_save.clicked.connect(self.save_toDatabase_networkedDatabase_settngs)

    #load Database to dictionary
    def load_databases(self):
        self.valueObj.WifiSettings_dict = self.databaseObj.load_data_to_WifiSettings_dict()
        self.valueObj.AngleCalculationSettings_dict = self.databaseObj.load_data_to_AngleCalculationSettings_dict()
        self.valueObj.AOCSettings_dict = self.databaseObj.load_data_to_AOCSettings_dict()
        self.valueObj.IOSettings_dict = self.databaseObj.load_data_to_IOSettings_dict()
        self.valueObj.IPSettings_dict = self.databaseObj.load_data_to_IPSettings_dict()
        self.valueObj.NetworkedDatabaseSettings_dict = self.databaseObj.load_data_to_NetworkedDatabaseSettings_dict()
        self.valueObj.RS232Settings_dict = self.databaseObj.load_data_to_RS232Settings_dict()

    #To save data  WifiSettings on table WifiSettings   
    def save_toDatabase_WifiSettings(self):
        ssid = self.lineEdit_wifiSsid.text()
        password = self.lineEdit_wifiPassword.text()

        # Call your database handler
        self.databaseObj.upsert_wifi_settings(ssid, password)
        self.valueObj.WifiSettings_dict = self.databaseObj.load_data_to_WifiSettings_dict()

        print("WiFi settings saved successfully.")

    #To save data  IPsettings on table IPSettings   
    def save_toDatabase_IpSettings(self):
        ip = self.lineEdit_selfIp.text()
        subnetmask = self.lineEdit_subnetMask.text()
        gateway = self.lineEdit_defaultGateway.text()

        self.databaseObj.upsert_ip_settings(ip,subnetmask,gateway)
        self.valueObj.IPSettings_dict = self.databaseObj.load_data_to_IPSettings_dict()
        
        if self.utils.is_raspberry_pi():
            self.utils.set_static_ip(ip,subnetmask,gateway)
        elif self.is_imx7():
            self.utils.set_static_ip_imx7(ip,subnetmask,gateway)

        print("Ip Setting")
    
    #To save data  shiftSettings on table shiftTimings   
    def save_toDatabase_shiftSettings(self):
        shift1 = (self.lineEdit_shift1FromTime.text(),
                 self.lineEdit_shift1ToTime.text())
        shift2 = (self.lineEdit_shift2FromTime.text(),
                  self.lineEdit_shift2ToTime.text())
        shift3 = (self.lineEdit_shift3FromTime.text(),
                  self.lineEdit_shift3ToTime.text())

        # Call DB function
        self.databaseObj.upsert_shift_timings(shift1, shift2, shift3)
        print("Shift settings saved")

    #To save data  rs232Settings on table RS232Settings   
    def save_toDatabase_rs232Settings(self):
        rs232OnOff = self.label_rs232OnOff.text()
        baudrate = self.comboBox_baudRate.currentText()
        dataBits = self.comboBox_dataBits.currentText()
        parity = self.comboBox_parity.currentText()
        stopBits = self.comboBox_stopBits.currentText()
        flowControl = self.comboBox_flowControl.currentText()
        portName = self.lineEdit_portName.text()
        
        self.databaseObj.update_rs232_settings(rs232OnOff,baudrate,dataBits,parity,stopBits,flowControl,portName)
        self.valueObj.RS232Settings_dict = self.databaseObj.load_data_to_RS232Settings_dict()
        print("rs232 settings saved successfully.")

    #To save data  networkDatabase on table NetworkDatabaseSettings   
    def save_toDatabase_networkedDatabase_settngs(self):
        networkBasedDatabaseOnOFF = self.toggleButton_networkBasedDatabase.text()
        msSqlDriverName = self.lineEdit_driverNameDb.text()
        msSqlServerName = self.lineEdit_serverNameDb.text()
        msSqlDatabaseNme = self.lineEdit_databaseNameDb.text()
        msSqlUserName = self.lineEdit_usernameDb.text()
        msSqlPassword = self.lineEdit_passwordDb.text()
        
        self.databaseObj.update_networked_database_settings(networkBasedDatabaseOnOFF,msSqlDriverName,
                                                            msSqlServerName,msSqlDatabaseNme,
                                                            msSqlUserName,msSqlPassword)
        self.valueObj.NetworkedDatabaseSettings_dict = self.databaseObj.load_data_to_NetworkedDatabaseSettings_dict()

        print("networkdatabase settings saved successfully.")

    #To save data  angleCalculationSettings on table angleCalculationSettings   
    def save_toDatabase_angleCalculationSettings(self):
        programId = self.comboBox_programIdSetting.currentText()
        angleCalculationOnOff = self.toggelButton_angleCalculation.text()
        angleDegree = self.lineEdit_angleDegree.text()
        angleMin = self.lineEdit_angleMinutes.text()
        angleSec = self.lineEdit_angleSeconds.text()
        tolaranceMin = self.lineEdit_toleranceMin.text()
        tolaranceSec = self.lineEdit_toleranceSec.text()
        negativeTolMin = self.lineEdit_negativeTolMin.text()
        negativeTolSec = self.lineEdit_negativeTolSec.text()
        distance = self.lineEdit_distanceMm.text()
        if self.radioButton_fullAngle.isChecked():
            angleType = "Full Angle"  # or whatever string you store in DB
        elif self.radioButton_halfAngle.isChecked():
            angleType = "Half Angle"

        self.databaseObj.update_angle_calculation_settings(programId,angleCalculationOnOff,angleDegree,angleMin,
                                                            angleSec,tolaranceMin,tolaranceSec,
                                                            negativeTolMin,negativeTolSec,distance,angleType)
        self.valueObj.AngleCalculationSettings_dict = self.databaseObj.load_data_to_AngleCalculationSettings_dict()

        print("angleCalculation settings saved successfully.")
    #To save data  CncList on table CNCList    
    def save_toDatabase_cncList(self):
        cncName = self.lineEdit_cncName.text()
        ipAddress = self.lineEdit_cncIpAddress.text()
        portNumber = self.lineEdit_cncPortNumber.text()
        cncSelection = self.comboBox_cncSelectionType.currentText()
        controller = self.comboBox_cncController.currentText()
        
        self.databaseObj.upsert_cnc_list(cncName,ipAddress,portNumber,
                                        cncSelection,controller)
        print("cncList settings saved successfully.")

    #To save data  IOsettings on table IOSettings   
    def save_toDatabase_IOSettings(self):        
        buzzer = self.toggleButton_buzzer.text()
        relay = self.toggelButton_relay.text()
        cycleStopTimer = self.toggelButton_cycleStopTimer.text()
        autoSaveReading = self.toggelButton_autoSaveReading.text()
        partTraceabilty = self.toggelButton_partTraceability.text()
        displayMode = self.comboBox_displayMode.currentText()
        timetoMasterSet = self.toggleButtontimeToSetMaster.text()
        masterGrouping = self.toggleButton_masterGrouping.text()

        self.databaseObj.update_io_settings(buzzer,relay,cycleStopTimer,autoSaveReading,
                                            partTraceabilty,displayMode,timetoMasterSet,
                                            masterGrouping)
        self.valueObj.IOSettings_dict = self.databaseObj.load_data_to_IOSettings_dict()
        print("Iosettings settings saved successfully.")

    #To save data  aocSettings on table AOCSettings
    def save_toDatabase_aocSettings(self):    
        aocOnOff = self.toggleButton_aoc.text()
        spcDataCount = self.lineEdit_spcDataCount.text()
        self.databaseObj.update_aoc_settings(aocOnOff,spcDataCount)
        print("aoc settings saved successfully.")

    #To save data  UserManagement on table UserManagement    
    def save_toDatabase_userManagement(self):
        
        setUsername = self.lineEdit_setUsernameLogin.text()
        setPassword = self.lineEdit_setPasswordLogin.text()
        setAccessType = int(self.comboBox_setAccessCombo.currentText())
        
        self.databaseObj.upsert_user_management(setUsername,setPassword,setAccessType)
        self.valueObj.AOCSettings_dict = self.databaseObj.load_data_to_AOCSettings_dict()

        print("userManagement settings saved successfully.")

    #To save data  ProgramSettings on table ProgramSettings
    def save_toDatabase_programSetting(self):
        programId = self.comboBox_programId.currentText()
        programName = self.lineEdit_programNameSettings.text()
        durationForAutosave = float(self.lineEdit_DurationAutosave.text())

        if self.radioButton_modeCombine.isChecked() and self.radioButton_inch.isChecked():
            mode = "Combine"  # or whatever string you store in 
            uom = "inch"
        elif self.radioButton_modeIndividual.isChecked() and self.radioButton_mm.isChecked():
            mode = "Individual"
            uom = "mm"

        self.databaseObj.upsert_program_settings(programId,programName,mode,
                                                uom,durationForAutosave)

        print("ProgramSetting settings saved successfully.")

    #To save data  ProbeBasedSettings on table ProbeBasedSettings
    def save_toDatabase_probeBasedSettings(self):
        programId = self.comboBox_programId.currentText()
        dimension = self.comboBox_toselectProbe.currentText()
        formulaBar = self.label_formulaBar.text()
        masterType = self.comboBox_masterType.currentText()
        masterLower = self.lineEdit_masterLower.text()
        master = self.lineEdit_master.text()
        masterHigher = self.lineEdit_masterHigher.text()
        uol = self.lineEdit_upperOffcetLimit.text()
        usl = self.lineEdit_usl.text()
        ucl = self.lineEdit_ucl.text()
        nominal = self.lineEdit_nominalValue.text()
        lcl = self.lineEdit_lcl.text()
        lsl = self.lineEdit_lsl.text()
        lol = self.lineEdit_lowerOffsetLimit.text()
        ovality = self.comboBox_ovalityOnOff.currentText()
        range = self.comboBox_rangeProbe.currentText()
        method = self.comboBox_methodProbe.currentText()
        case = self.comboBox_caseProbe.currentText()
        caseT = self.lineEdit_caseT.text()
        probe_sensitivity = self.lineEdit_probeSensitivity.text()
        air_sensitivity_quotient = self.lineEdit_airSensitivityQuotient.text()
        
        self.databaseObj.upsert_probe_based_settings(
            self,
            program_id = int(programId),
            dimension = str(dimension),
            formula = str(formulaBar) ,
            master_type = str(masterType) ,
            master_lower = float(masterLower) ,
            master = float(master) ,
            master_higher = float(masterHigher) ,
            upper_offset_limit = float(uol) ,
            upper_specification_limit = float(usl) ,
            upper_control_limit = float(ucl) ,
            nominal_value = float(nominal) ,
            lower_control_limit = float(lcl) ,
            lower_specification_limit = float(lsl) ,
            lower_offset_limit = float(lol) ,
            ovality = str(ovality) ,
            range_val = float(range) ,
            method = str(method) ,
            case = str(case) ,
            case_t = float(caseT) ,
            probe_sensitivity = int(probe_sensitivity) ,
            air_sensitivity_quotient = str(air_sensitivity_quotient)
        )
        print("Probebased settings saved successfully.")
    
    #To save data  aocBasedSetting on table AOCBasedSettings
    def save_toDatabase_aocBasedSettings(self):
        programId = self.comboBox_programId.currentText()
        dimension = self.comboBox_toselectProbe.currentText()
        axis = self.comboBox_axis.currentText()
        offset = self.lineEdit_offsetNo.text()
        machine = self.comboBox_machine.currentText()
        direction = self.comboBox_direction.currentText()
        turretNo = self.lineEdit_turretNo.text()
        bufferPartNo = self.lineEdit_bufferPartNo.text()

        self.upsert_aoc_based_settings(
            self,
            program_id = int(programId),
            dimension = str(dimension),
            axis = str(axis),
            offset_no = int(offset),
            machine = str(machine),
            direction = str(direction),
            turret_no = int(turretNo),
            buffer_part_no = int(bufferPartNo)
        )
        print("aocBased settings saved successfully.")

    #letter keyboard/numpad applied to follwing lineedits 
    def setup_lineedit_keyboards(self):
        # Letter/Keyboard line edits
        letter_lineedits = [
            self.lineEdit_usernameLogin,
            self.lineEdit_programNameSettings,
            self.lineEdit_passwordLogin,
            self.lineEdit_setUsernameLogin,
            self.lineEdit_setPasswordLogin,
            self.lineEdit_portName,
            self.lineEdit_wifiPassword,
            self.lineEdit_driverNameDb,
            self.lineEdit_serverNameDb,
            self.lineEdit_databaseNameDb,
            self.lineEdit_usernameDb,
            self.lineEdit_passwordDb,
            self.lineEdit_cncName,
            self.lineEdit_wifiSsid

        ]

        # Numeric/Numpad line edits
        numeric_lineedits = [
            self.lineEdit_cncIpAddress,
            self.lineEdit_cncPortNumber,
            self.lineEdit_selfIp,
            self.lineEdit_subnetMask,
            self.lineEdit_defaultGateway,
            self.lineEdit_masterLower,self.lineEdit_master,self.lineEdit_masterHigher,
            self.lineEdit_upperOffcetLimit,self.lineEdit_usl,self.lineEdit_ucl,
            self.lineEdit_nominalValue,self.lineEdit_lcl,self.lineEdit_lsl,
            self.lineEdit_lowerOffsetLimit,self.lineEdit_caseT,
            self.lineEdit_probeSensitivity,
            self.lineEdit_airSensitivityQuotient,
            self.lineEdit_offsetNo,self.lineEdit_turretNo,self.lineEdit_bufferPartNo,
            self.lineEdit_relayTime,
            self.lineEdit_cycleTime,
            self.lineEdit_day,self.lineEdit_month,self.lineEdit_year,
            self.lineEdit_hours,self.lineEdit_minutes,
            self.lineEdit_spcDataCount,self.lineEdit_lowerMasterCalibrate,
            self.lineEdit_higherMasterCalibrate,
            self.lineEdit_DurationAutosave,
            self.lineEdit_angleDegree,self.lineEdit_angleMinutes,self.lineEdit_angleSeconds,
            self.lineEdit_toleranceMin,self.lineEdit_toleranceSec,
            self.lineEdit_negativeTolMin,self.lineEdit_negativeTolSec,
            self.lineEdit_distanceMm,
            self.lineEdit_timeToMasterSet
        ]

        for le in letter_lineedits + numeric_lineedits:
            le.installEventFilter(self)

        # Store them as attributes if you need them in eventFilter
        self.letter_lineedits = letter_lineedits
        self.numeric_lineedits = numeric_lineedits

    # Function To Set Page Labels At Page Changes
    def set_labels_to_header(self):
        self.button_home.setEnabled(True)
        self.button_forward.setEnabled(True)
        self.button_back.setEnabled(True)

        if self.stacked.currentIndex() == 0:
            self.label_pageName.setText("User Login")

            self.button_home.hide()
            self.button_forward.hide()
            self.button_back.hide()
            self.button_save.hide()

        elif self.stacked.currentIndex() == 1 :
            self.label_pageName.setText("User Management")
            self.button_save.hide()
            self.button_forward.hide()
            self.button_shutdown.hide()
            self.button_back.show()
            self.button_home.show()
        elif self.stacked.currentIndex() == 2:
            self.label_pageName.setText("User Settings")
            self.button_save.hide()
            self.button_forward.hide()
            self.button_home.hide()
            self.button_shutdown.hide()
        elif self.stacked.currentIndex() == 3:
            self.label_pageName.setText("RS 232 Settings")
            self.button_save.show()
            self.button_back.show()
            self.button_forward.hide()
            self.button_home.hide()
            self.button_shutdown.hide()
        elif self.stacked.currentIndex() == 4:
            self.label_pageName.setText("Formula Settings")
            self.button_save.hide()
            self.button_back.hide()
            self.button_forward.hide()
            self.button_home.hide()
            self.button_shutdown.hide()
        elif self.stacked.currentIndex() == 5:
            self.label_pageName.setText("IP Settings")
            self.button_save.show()
            self.button_back.show()
            self.button_forward.hide()
            self.button_home.hide()
            self.button_shutdown.hide()
        elif self.stacked.currentIndex() == 6:
            self.label_pageName.setText("Wifi Settings")
            self.button_save.show()
            self.button_back.show()
            self.button_forward.hide()
            self.button_home.hide()
            self.button_shutdown.hide()
        elif self.stacked.currentIndex() == 7: 
            self.label_pageName.setText("I/O Settings")
            self.button_save.show()
            self.button_back.show()
            self.button_forward.show()
            self.button_home.hide()
            self.button_shutdown.hide()
        elif self.stacked.currentIndex() == 8:
            self.label_pageName.setText("I/O Settings")
            self.button_save.show()
            self.button_back.show()
            self.button_home.show()
            self.button_forward.hide()
            self.button_shutdown.hide()
        elif self.stacked.currentIndex() == 9:
            self.label_pageName.setText("About")
            self.button_save.hide()
            self.button_back.show()
            self.button_home.show()
            self.button_forward.hide()
            self.button_shutdown.hide()
        elif self.stacked.currentIndex() == 10:
            self.label_pageName.setText("Clock Settings")
            self.button_save.hide()
            self.button_back.show()
            self.button_home.show()
            self.button_forward.hide()
            self.button_shutdown.hide()
        elif self.stacked.currentIndex() == 12:
            self.label_pageName.setText("CNC List")
            self.button_save.hide()
            self.button_back.show()
            self.button_home.show()
            self.button_forward.hide()
            self.button_shutdown.hide()
        elif self.stacked.currentIndex() == 13:
            self.label_pageName.setText("CNC Settings")
            self.button_save.show()
            self.button_back.show()
            self.button_home.hide()
            self.button_forward.hide()
            self.button_shutdown.hide()
        elif self.stacked.currentIndex() == 14:
            self.label_pageName.setText("Auto Offset Settings")
            self.button_save.hide()
            self.button_back.show()
            self.button_home.show()
            self.button_forward.hide()
            self.button_shutdown.hide()
        elif self.stacked.currentIndex() == 16:
            self.label_pageName.setText("Database Settings")
            self.button_save.show()
            self.button_back.show()
            self.button_home.hide()
            self.button_forward.hide()
            self.button_shutdown.hide()
        elif self.stacked.currentIndex() == 17:
            self.label_pageName.setText("Part Settings")
            self.button_save.show()
            self.button_back.show()
            self.button_home.hide()
            self.button_forward.hide()
            self.button_shutdown.hide()
        elif self.stacked.currentIndex() == 18:
            self.label_pageName.setText("AOC Report")
            self.button_save.hide()
            self.button_back.hide()
            self.button_home.show()
            self.button_forward.hide()
            self.button_shutdown.hide()
        elif self.stacked.currentIndex() == 19:
            self.label_pageName.setText("Factory Calibration")
            self.button_save.hide()
            self.button_back.show()
            self.button_home.show()
            self.button_forward.hide()
            self.button_shutdown.hide()
        # elif self.stacked.currentIndex() == 20:
        #     self.label_pageName.setText("Air Saving Settings")
        elif self.stacked.currentIndex() == 21 or self.stacked.currentIndex() == 22:
            self.label_pageName.setText("Reports")
            self.button_save.hide()
            self.button_back.show()
            self.button_home.show()
            self.button_forward.hide()
            self.button_shutdown.hide()
        elif self.stacked.currentIndex() == 23:
            self.label_pageName.setText("Home Page")
            self.button_save.hide()
            self.button_back.hide()
            self.button_home.hide()
            self.button_forward.hide()
            self.button_shutdown.show()
        elif self.stacked.currentIndex() == 25:
            self.label_pageName.setText("Dial Indicator")
            self.button_save.show()
            self.button_back.hide()
            self.button_home.show()
            self.button_forward.hide()
            self.button_shutdown.hide()
        elif self.stacked.currentIndex() == 26:
            self.label_pageName.setText("Program Settings")
            self.button_save.show()
            self.button_back.show()
            self.button_home.hide()
            self.button_forward.hide()
            self.button_shutdown.hide()
        elif self.stacked.currentIndex() == 27:
            self.label_pageName.setText("Angle Calculation")
            self.button_save.show()
            self.button_back.show()
            self.button_home.hide()
            self.button_forward.hide()
            self.button_shutdown.hide()
        elif self.stacked.currentIndex() == 28:
            self.label_pageName.setText("Settings")
            self.button_save.hide()
            self.button_back.show()
            self.button_home.show()
            self.button_forward.hide()
            self.button_shutdown.hide()
        elif self.stacked.currentIndex() == 29:
            self.label_pageName.setText("Program List")
            self.button_save.hide()
            self.button_back.show()
            self.button_home.show()
            self.button_forward.hide()
            self.button_shutdown.hide()
    
    
    #Backbutton link using currentindex
    def linkage_of_backButton(self):
        if self.stacked.currentIndex() == 9:
            self.stacked.setCurrentIndex(23)
        elif self.stacked.currentIndex() == 25:
            self.stacked.setCurrentIndex(23)
        elif self.stacked.currentIndex() == 28:
            self.stacked.setCurrentIndex(23)
        elif self.stacked.currentIndex() == 26:
            self.stacked.setCurrentIndex(17)
        elif self.stacked.currentIndex() == 27:
            self.stacked.setCurrentIndex(26)
        elif self.stacked.currentIndex() == 8:
            self.stacked.setCurrentIndex(7)
        elif self.stacked.currentIndex() == 7:
            self.stacked.setCurrentIndex(23)
        elif self.stacked.currentIndex() == 18:
            self.stacked.setCurrentIndex(14)
        elif self.stacked.currentIndex() == 13:
            self.stacked.setCurrentIndex(12)
        elif self.stacked.currentIndex() == 12:
            self.stacked.setCurrentIndex(14)
        elif self.stacked.currentIndex() == 14:
            self.stacked.setCurrentIndex(23)
        elif self.stacked.currentIndex() == 19:
            self.stacked.setCurrentIndex(8)
        elif self.stacked.currentIndex() == 16:
            self.stacked.setCurrentIndex(8)
        elif self.stacked.currentIndex() == 3:
            self.stacked.setCurrentIndex(8)
        # elif self.stacked.currentIndex() == 20:
        #     self.stacked.setCurrentIndex(8)
        elif self.stacked.currentIndex() == 5:
            self.stacked.setCurrentIndex(8)
        elif self.stacked.currentIndex() == 6:
            self.stacked.setCurrentIndex(8)
        elif self.stacked.currentIndex() == 4:
            self.stacked.setCurrentIndex(17)
        elif self.stacked.currentIndex() == 10:
            self.stacked.setCurrentIndex(23)
        elif self.stacked.currentIndex() == 2:
            self.stacked.setCurrentIndex(1)
        elif self.stacked.currentIndex() == 1:
            self.stacked.setCurrentIndex(23)
        elif self.stacked.currentIndex() == 22:
            self.stacked.setCurrentIndex(21)
        elif self.stacked.currentIndex() == 21:
            self.stacked.setCurrentIndex(23)
        elif self.stacked.currentIndex() == 17:
            self.stacked.setCurrentIndex(28)
        elif self.stacked.currentIndex() == 29:
            self.stacked.setCurrentIndex(28)

    # Formula Bar code
    def insert_formula_text(self, text):
        cursor = self.lineEdit_formulaBar.cursorPosition()
        current_text = self.lineEdit_formulaBar.text()
        new_text = current_text[:cursor] + text + current_text[cursor:]
        self.lineEdit_formulaBar.setText(new_text)
        self.lineEdit_formulaBar.setCursorPosition(cursor + len(text))

    def linkage_formula_bar(self):
        # Operators
        self.button_plusFormulaBar.clicked.connect(lambda: self.insert_formula_text("+"))
        self.button_minusFormulaBar.clicked.connect(lambda: self.insert_formula_text("-"))
        self.button_multiplicationFormulaBar.clicked.connect(lambda: self.insert_formula_text("*"))
        self.button_divisionFormulaBar.clicked.connect(lambda: self.insert_formula_text("/"))
        self.button_modFormulaBar.clicked.connect(lambda: self.insert_formula_text("%"))
        self.button_commaFormulaBar.clicked.connect(lambda: self.insert_formula_text(","))

        # Braces
        self.button_leftBraceFormulaBar.clicked.connect(lambda: self.insert_formula_text("("))
        self.button_rightBraceFormulaBar.clicked.connect(lambda: self.insert_formula_text(")"))

        # Functions
        self.button_maxFormulaBar.clicked.connect(lambda: self.insert_formula_text("max"))
        self.button_minFormulaBar.clicked.connect(lambda: self.insert_formula_text("min"))
        self.button_avgFormulaBar.clicked.connect(lambda: self.insert_formula_text("avg"))
        self.button_absFormulaBar.clicked.connect(lambda: self.insert_formula_text("abs"))

        self.button_sinFormulaBar.clicked.connect(lambda: self.insert_formula_text("sin"))
        self.button_cosFormulaBar.clicked.connect(lambda: self.insert_formula_text("cos"))
        self.button_tanFormulaBar.clicked.connect(lambda: self.insert_formula_text("tan"))
        self.button_cosecFormulaBar.clicked.connect(lambda: self.insert_formula_text("cosec"))
        self.button_secFormulaBar.clicked.connect(lambda: self.insert_formula_text("sec"))
        self.button_cotFormulaBar.clicked.connect(lambda: self.insert_formula_text("cot"))

        # Backspace
        self.button_backspaceFormulaBar.clicked.connect(self.delete_last_character)

        # ComboBox variable insertion
        self.button_addFormulaBar.clicked.connect(
            lambda: self.insert_formula_text(self.comboBox_probeFormulaBar.currentText())
        )
        self.button_saveSettingsFormulaBar.clicked.connect(self.save_formula_to_label)
        

    def save_formula_to_label(self):
        self.keyboard_open = False
        if hasattr(self, "current_keyboard") and self.current_keyboard is not None:
            self.current_keyboard.close()
            self.current_keyboard = None
        text = self.lineEdit_formulaBar.text()
        print("Formula to save:", text)
        print("TextEdit reference:", self.label_formulaBar)
        if text:  # only update if not empty
            self.label_formulaBar.setText(text)
            self.stacked.setCurrentIndex(17)
        else:
            self.label_formulaBar.setText("No formula set")


    def delete_last_character(self):
        cursor = self.lineEdit_formulaBar.cursorPosition()
        if cursor > 0:
            current_text = self.lineEdit_formulaBar.text()
            new_text = current_text[:cursor-1] + current_text[cursor:]
            self.lineEdit_formulaBar.setText(new_text)
            self.lineEdit_formulaBar.setCursorPosition(cursor-1)

    #ui setting for forward button
    def linkage_of_forwardButton(self):
        if self.stacked.currentIndex() == 7:
            self.stacked.setCurrentIndex(8)


    def linkage_of_ui(self):
        # Footer Buttons Signals Slots Implementation
        self.button_back.clicked.connect(self.linkage_of_backButton)
        self.button_forward.clicked.connect(self.linkage_of_forwardButton)
        self.button_home.clicked.connect(lambda : self.stacked.setCurrentIndex(23))

        # To Be Removed
        self.button_login.clicked.connect(lambda : self.stacked.setCurrentIndex(23))

        # Dial Indicator Page Clicked Slot
        self.label_dialIndicatorPage.mousePressEvent = lambda event: self.stacked.setCurrentIndex(25)
        
        # Settings Page Clicked Slot
        self.label_settingsPage.mousePressEvent = lambda event: self.stacked.setCurrentIndex(28)
        self.button_partSettings.clicked.connect(lambda : self.stacked.setCurrentIndex(17))
        self.button_programList.clicked.connect(lambda : self.stacked.setCurrentIndex(29))
        self.button_staticSettingsForAll.clicked.connect(lambda : self.stacked.setCurrentIndex(26))
        self.button_setFormulaSettings.clicked.connect(lambda : self.stacked.setCurrentIndex(4))


        self.button_angleCalculationSetting.clicked.connect(lambda : self.stacked.setCurrentIndex(27))

        # IO Settings Page Clicked Slot
        self.label_ioSettingPage.mousePressEvent = lambda event: self.stacked.setCurrentIndex(7)
        self.button_databaseSettings.clicked.connect(lambda : self.stacked.setCurrentIndex(16))
        self.button_rs232Settings.clicked.connect(lambda : self.stacked.setCurrentIndex(3))
        #self.button_airSaving.clicked.connect(lambda : self.stacked.setCurrentIndex(20))
        self.button_ipSettings.clicked.connect(lambda : self.stacked.setCurrentIndex(5))
        self.button_wifiSettings.clicked.connect(lambda : self.stacked.setCurrentIndex(6))
        self.button_factoryCalibration.clicked.connect(lambda : self.stacked.setCurrentIndex(19))

        # AOC Page Clicked Slot
        self.label_autoOffsetSettingPage.mousePressEvent = lambda event: self.stacked.setCurrentIndex(14)
        self.button_cncListAoc.clicked.connect(lambda : self.stacked.setCurrentIndex(12))
        self.button_addCncSettings.clicked.connect(lambda : self.stacked.setCurrentIndex(13))
        self.button_modifyCncSettings.clicked.connect(lambda : self.stacked.setCurrentIndex(13))
        self.button_reportsAoc.clicked.connect(lambda : self.stacked.setCurrentIndex(18))

        # Clock Settings Page Clicked Slot
        self.label_clockSettingsPage.mousePressEvent = lambda event: self.stacked.setCurrentIndex(10)

        # User Management Page Clicked Slot
        self.label_userManagementPage.mousePressEvent = lambda event: self.stacked.setCurrentIndex(1)
        self.button_addLoginDetails.clicked.connect(lambda : self.stacked.setCurrentIndex(2))
        self.button_modifyLogin.clicked.connect(lambda : self.stacked.setCurrentIndex(2))

        # Report Page Clicked Slot
        self.label_reportPage.mousePressEvent = lambda event: self.stacked.setCurrentIndex(21)
        self.button_viewData.clicked.connect(lambda : self.stacked.setCurrentIndex(22))
        self.button_ListView.clicked.connect(lambda : self.stackedWidget.setCurrentIndex(0))
        self.button_ChartView.clicked.connect(lambda : self.stackedWidget.setCurrentIndex(1))
        self.button_HistogramChart.clicked.connect(lambda : self.stackedWidget.setCurrentIndex(2))

        # About Logo Page Clicked Slot
        self.label_aboutLogoPage.mousePressEvent = lambda event: self.stacked.setCurrentIndex(9)

        #factory config
        #factory_con = FactoryConfig()
        self.button_factoryConfig.clicked.connect(lambda: FactoryConfig().exec_())

    def apply_line_styles(self, thickness=3, color="#555555"):
        """
        Apply thickness and color to all QFrame lines in the central widget.
        Horizontal lines get fixed height, vertical lines get fixed width.
        """
        # Iterate through all QFrame children of centralwidget
        for line in self.centralwidget.findChildren(QFrame):
            if line.frameShape() == QFrame.HLine:
                line.setFixedHeight(thickness)
                line.setStyleSheet(f"background-color: {color};")
            elif line.frameShape() == QFrame.VLine:
                line.setFixedWidth(thickness)
                line.setStyleSheet(f"background-color: {color};")
    
    def powerButton(self):
        self.button_shutdown.clicked.connect(self.show_menu)

        # Create the menu
        self.menu = QtWidgets.QMenu()
        self.menu.setStyleSheet("""
            QMenu {
                background-color: #2d2d2d;
                color: white;
                font: 16pt "MS Shell Dlg 2";
            }
            QMenu::item:selected {
                background-color: #555555;
            }
        """)
        self.menu.addAction("Logout", self.logout)
        self.menu.addAction("Shutdown", self.shutdown)
        self.menu.addAction("Restart", self.restart)

    def show_menu(self):
        # Position menu below button
        self.menu.setMinimumWidth(200)  # make a little wider if you want
        pos = self.button_shutdown.mapToGlobal(
        QtCore.QPoint(0, self.button_shutdown.height() - 50)  # -30 moves menu UP
        )
        self.menu.exec_(pos)

    def logout(self):
        logout_dlg = CustomMessageBox("  Do you really want to logout?", "info")
        logout_dlg.exec_()   # Wait for user to press OK
        

    def shutdown(self):
        shudtdown_dlg = CustomMessageBox("  Do you really want to Shutdown?", "info")
        shudtdown_dlg.exec_()   # Wait for user to press OK
        #print("Shutdown clicked")

    def restart(self):
        restart_dlg = CustomMessageBox("  Do you really want to Restart?", "info")
        restart_dlg.exec_()   # Wait for user to press OK
        #("Restart clicked")

    #to manage     
    def eventFilter(self, obj, event):
        if isinstance(obj, QtWidgets.QLineEdit) and event.type() == QtCore.QEvent.MouseButtonPress:
            if getattr(self, "keyboard_open", False):  # already open
                return True
            self.keyboard_open = True
            if obj in self.letter_lineedits:
                keyboard = MobileKeyboard()
                keyboard.textEntered.connect(lambda text, line=obj: self.apply_keyboard_text(line, text, keyboard))
                keyboard.show()
                return True  # block normal focus behavior (prevents cursor)
            elif obj in self.numeric_lineedits:
                numkeyboard = numpad_window(target_lineedit=obj)
                numkeyboard.finished.connect(lambda _: setattr(self, "keyboard_open", False))
                numkeyboard.show()
                return True  # block normal focus behavior (prevents cursor)

        
        return super().eventFilter(obj, event)


    def apply_keyboard_text(self, lineedit, text,keyboard):
        lineedit.setText(text)
        lineedit.parentWidget().setFocus()  # shift focus safely
        self.keyboard_open = False

    def load_data_to_ui(self):
        pass

    # Load AngleCalculationSettings Dict To Ui
    def load_AngleCalculationSettings_to_ui(self):
        if self.AngleCalculationSettings_dict["ANGLE_CALCULATION_SETTINGS_ON_OFF"] == 'OFF':
            self.toggelButton_angleCalculation.setPixmap(QPixmap("Switcher_OFF.png"))
        elif self.AngleCalculationSettings_dict["ANGLE_CALCULATION_SETTINGS_ON_OFF"] == 'ON':
            self.toggelButton_angleCalculation.setPixmap(QPixmap("Switcher_On.png"))

        self.lineEdit_angleDegree.setText(self.AngleCalculationSettings_dict["MASTER_ANGLE_DEGREES"])
        self.lineEdit_angleMinutes.setText(self.AngleCalculationSettings_dict["MASTER_ANGLE_MINUTES"])
        self.lineEdit_angleSeconds.setText(self.AngleCalculationSettings_dict["MASTER_ANGLE_SECONDS"])
        self.lineEdit_toleranceMin.setText(self.AngleCalculationSettings_dict["PLUS_TOLERANCE_MINUTES"])
        self.lineEdit_toleranceSec.setText(self.AngleCalculationSettings_dict["PLUS_TOLERANCE_SECONDS"])
        self.lineEdit_negativeTolMin.setText(self.AngleCalculationSettings_dict["MINUS_TOLERANCE_MINUTES"])
        self.lineEdit_negativeTolSec.setText(self.AngleCalculationSettings_dict["MINUS_TOLERANCE_SECONDS"])
        self.lineEdit_distanceMm.setText(self.AngleCalculationSettings_dict["DISTANCE"])

        if self.AngleCalculationSettings_dict["ANGLETYPE"] == 'Half Angle':
            self.radioButton_halfAngle.setChecked(True)
            self.radioButton_2_fullAngle.setChecked(False)
        elif self.AngleCalculationSettings_dict["ANGLETYPE"] == 'Full Angle':
            self.radioButton_2_fullAngle.setChecked(True)
            self.radioButton_halfAngle.setChecked(False)

    # Load IOSettings Dict To Ui
    def load_IOSettings_to_ui(self):
        self.IOSettings_dict = {
                'AUTO_SAVE_READING': {'Enable': '0', 'Value': None},
                'BUZZER': {'Enable': '0', 'Value': 'Ok'},
                'CYCLE_STOP_TIMER': {'Enable': '0', 'Value': '2'},
                'MASTER_GROUPING': {'Enable': '0', 'Value': None},
                'PART_TRACEABILITY': {'Enable': '0', 'Value': 'Manual Reset'},
                'RELAY': {'Enable': '0', 'Value': '2'},
                'TIME_TO_MASTER_SET': {'Enable': '0', 'Value': '2'}
            }
        
        if self.IOSettings_dict["AUTO_SAVE_READING"]["Enable"] == '0':
            self.toggelButton_autoSaveReading.setPixmap(QPixmap("Switcher_OFF.png"))
        elif self.IOSettings_dict["AUTO_SAVE_READING"]["Enable"] == '1':
            self.toggelButton_autoSaveReading.setPixmap(QPixmap("Switcher_On.png"))

        if self.IOSettings_dict["BUZZER"]["Enable"] == '0':
            self.toggleButton_buzzer.setPixmap(QPixmap("Switcher_OFF.png"))
        elif self.IOSettings_dict["BUZZER"]["Enable"] == '1':
            self.toggleButton_buzzer.setPixmap(QPixmap("Switcher_On.png"))

        if self.IOSettings_dict["CYCLE_STOP_TIMER"]["Enable"] == '0':
            self.toggelButton_cycleStopTimer.setPixmap(QPixmap("Switcher_OFF.png"))
        elif self.IOSettings_dict["CYCLE_STOP_TIMER"]["Enable"] == '1':
            self.toggelButton_cycleStopTimer.setPixmap(QPixmap("Switcher_On.png"))

        if self.IOSettings_dict["MASTER_GROUPING"]["Enable"] == '0':
            self.toggleButton_masterGrouping.setPixmap(QPixmap("Switcher_OFF.png"))
        elif self.IOSettings_dict["MASTER_GROUPING"]["Enable"] == '1':
            self.toggleButton_masterGrouping.setPixmap(QPixmap("Switcher_On.png"))

        if self.IOSettings_dict["PART_TRACEABILITY"]["Enable"] == '0':
            self.toggelButton_partTraceability.setPixmap(QPixmap("Switcher_OFF.png"))
        elif self.IOSettings_dict["PART_TRACEABILITY"]["Enable"] == '1':
            self.toggelButton_partTraceability.setPixmap(QPixmap("Switcher_On.png"))

        if self.IOSettings_dict["RELAY"]["Enable"] == '0':
            self.toggelButton_relay.setPixmap(QPixmap("Switcher_OFF.png"))
        elif self.IOSettings_dict["RELAY"]["Enable"] == '1':
            self.toggelButton_relay.setPixmap(QPixmap("Switcher_On.png"))

        if self.IOSettings_dict["TIME_TO_MASTER_SET"]["Enable"] == '0':
            self.toggleButtontimeToSetMaster.setPixmap(QPixmap("Switcher_OFF.png"))
        elif self.IOSettings_dict["TIME_TO_MASTER_SET"]["Enable"] == '1':
            self.toggleButtontimeToSetMaster.setPixmap(QPixmap("Switcher_On.png"))

        if self.IOSettings_dict["BUZZER"]["Value"] == 'Ok':
            self.radioButton_okBuzzer.setChecked(True)
            self.radioButton_reworkNotokBuzzer.setChecked(False)
        elif self.IOSettings_dict["BUZZER"]["Value"] == 'Rework / Not Ok':
            self.radioButton_reworkNotokBuzzer.setChecked(True)
            self.radioButton_okBuzzer.setChecked(False)
        
        self.lineEdit_relayTime.setText(self.IOSettings_dict["RELAY"]["Value"])
        self.lineEdit_cycleTime.setText(self.IOSettings_dict["CYCLE_STOP_TIMER"]["Value"])

        if self.IOSettings_dict["PART_TRACEABILITY"]["Value"] == 'Manual Reset':
            self.radioButton_manualPartTraceability.setChecked(True)
            self.radioButton_autoPartTraceability.setChecked(False)
        elif self.IOSettings_dict["PART_TRACEABILITY"]["Value"] == 'Auto Reset':
            self.radioButton_autoPartTraceability.setChecked(True)
            self.radioButton_manualPartTraceability.setChecked(False)

        self.lineEdit_timeToMasterSet.setText(self.IOSettings_dict["TIME_TO_MASTER_SET"]["Value"])

    # Load IPSettings Dict To Ui
    def load_IPSettings_to_ui(self):
        self.lineEdit_selfIp.setText(self.IPSettings_dict["SelfIPAddress"])
        self.lineEdit_subnetMask.setText(self.IPSettings_dict["SubnetMask"])
        self.lineEdit_defaultGateway.setText(self.IPSettings_dict["DefaultGateway"])

    # Load NetworkedDatabaseSettings Dict To Ui
    def load_NetworkedDatabaseSettings_to_ui(self):
        if self.NetworkedDatabaseSettings_dict["NETWORKE_BASED_DATABASE_ON_OFF"] == 'OFF':
            self.toggleButton_networkBasedDatabase.setPixmap(QPixmap("Switcher_OFF.png"))
        elif self.NetworkedDatabaseSettings_dict["NETWORKE_BASED_DATABASE_ON_OFF"] == 'ON':
            self.toggleButton_networkBasedDatabase.setPixmap(QPixmap("Switcher_On.png"))

        self.lineEdit_driverNameDb.setText(self.WifiSettings_dict["MS_SQL_DRIVER_NAME"])
        self.lineEdit_serverNameDb.setText(self.WifiSettings_dict["MS_SQL_SERVER_NAME"])
        self.lineEdit_databaseNameDb.setText(self.WifiSettings_dict["MS_SQL_DATABASE_NAME"])
        self.lineEdit_usernameDb.setText(self.WifiSettings_dict["MS_SQL_USERNAME"])
        self.lineEdit_passwordDb.setText(self.WifiSettings_dict["MS_SQL_PASSWORD"])

    # Load ProbeBasedSettings Dict To Ui
    def load_ProbeBasedSettings_to_ui(self):
        pass

    # Load AOCSettings Dict To Ui
    def load_AOCSettings_to_ui(self):
        pass

    # Load ProgramSettings Dict To Ui
    def load_ProgramSettings_to_ui(self):
        pass

    # Load RS232Settings Dict To Ui
    def load_RS232Settings_to_ui(self):
        if self.RS232Settings_dict["RS232_ON_OFF"] == 'OFF':
            self.toggleButton_rs232.setPixmap(QPixmap("Switcher_OFF.png"))
        elif self.RS232Settings_dict["RS232_ON_OFF"] == 'ON':
            self.toggleButton_rs232.setPixmap(QPixmap("Switcher_On.png"))

        self.comboBox_baudRate.setCurrentText(self.RS232Settings_dict["BAUD_RATE"])
        self.comboBox_dataBits.setCurrentText(self.RS232Settings_dict["DATA_BITS"])
        self.comboBox_parity.setCurrentText(self.RS232Settings_dict["PARITY"])
        self.comboBox_stopBits.setCurrentText(self.RS232Settings_dict["STOP_BITS"])
        self.comboBox_flowControl.setCurrentText(self.RS232Settings_dict["FLOW_CONTROL"])
        self.comboBox_baudRate.setText(self.RS232Settings_dict["PORT_NAME"])

    # Load WifiSettings Dict To Ui
    def load_WifiSettings_to_ui(self):
        self.lineEdit_wifiSsid.setText(self.WifiSettings_dict["WifiSSID"])
        self.lineEdit_wifiPassword.setText(self.WifiSettings_dict["WifiPassword"])
    

    def __del__(self):
        """Destructor to clean up movies"""
        # for movie in self.movies:
        #     if movie is not None:
        #         movie.stop()
        print("MainWindow destroyed, movies stopped.")


if __name__ == "__main__":
    app = QApplication(sys.argv)



    gif_labels = {
        "label_ProgramSetting": "C:/Users/Lenovo/Downloads/indicators-ezgif.com-added-text.gif",
        "label_IOSettings": "C:/Users/Lenovo/Downloads/settings-ezgif.com-added-text.gif",
        "label_userManagement": "C:/Users/Lenovo/Downloads/userman-unscreen-ezgif.com-resize.gif",
        "label_Report": "C:/Users/Lenovo/Downloads/reports-unscreen-ezgif.com-added-text.gif",
    }

    window = MainWindow()#(gif_labels)
    window.show()
    sys.exit(app.exec_())
