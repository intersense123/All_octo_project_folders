from PySide2.QtWidgets import QApplication,  QMainWindow, QStackedWidget
import sys
# import the generated UI class
from main_ui_17 import Ui_MainWindow
from PySide2.QtGui import QPixmap

# Load UI
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):#, gif_labels: dict):
        super().__init__()
        self.setupUi(self)  # setup UI

        # 🔑 Set stacked widget page index
        self.stacked: QStackedWidget = getattr(self, "stackedWidget_main", None)
        if self.stacked:
            # Connecting Slot When Page Changes
            self.stacked.currentChanged.connect(self.set_labels)
            self.stacked.setCurrentIndex(0)  # second page

        self.linkage_of_ui()
        # self.showFullScreen()
    
    # Function To Set Page Label At Page Changes
    def set_labels(self):
        self.button_home.setEnabled(True)
        self.button_forward.setEnabled(True)
        self.button_back.setEnabled(True)

        if self.stacked.currentIndex() == 0:
            self.label_pageName.setText("User Login")

            self.button_home.setEnabled(False)
            self.button_forward.setEnabled(False)
            self.button_back.setEnabled(False)

        elif self.stacked.currentIndex() == 1 :
            self.label_pageName.setText("User Management")
        elif self.stacked.currentIndex() == 2:
            self.label_pageName.setText("User Settings")
        elif self.stacked.currentIndex() == 3:
            self.label_pageName.setText("RS 232 Settings")
        elif self.stacked.currentIndex() == 4:
            self.label_pageName.setText("Formula Settings")
        elif self.stacked.currentIndex() == 5:
            self.label_pageName.setText("IP Settings")
        elif self.stacked.currentIndex() == 6:
            self.label_pageName.setText("Wifi Settings")
        elif self.stacked.currentIndex() == 7 or self.stacked.currentIndex() == 8:
            self.label_pageName.setText("I/O Settings")
        elif self.stacked.currentIndex() == 9:
            self.label_pageName.setText("About")
        elif self.stacked.currentIndex() == 10:
            self.label_pageName.setText("Clock Settings")
        elif self.stacked.currentIndex() == 12:
            self.label_pageName.setText("CNC List")
        elif self.stacked.currentIndex() == 13:
            self.label_pageName.setText("CNC Settings")
        elif self.stacked.currentIndex() == 14:
            self.label_pageName.setText("Auto Offset Settings")
        elif self.stacked.currentIndex() == 16:
            self.label_pageName.setText("Database Settings")
        elif self.stacked.currentIndex() == 17:
            self.label_pageName.setText("Part Settings")
        elif self.stacked.currentIndex() == 18:
            self.label_pageName.setText("AOC Report")
        elif self.stacked.currentIndex() == 19:
            self.label_pageName.setText("Factory Calibration")
        elif self.stacked.currentIndex() == 20:
            self.label_pageName.setText("Air Saving Settings")
        elif self.stacked.currentIndex() == 21 or self.stacked.currentIndex() == 22:
            self.label_pageName.setText("Reports")
        elif self.stacked.currentIndex() == 23:
            self.label_pageName.setText("Home Page")
            self.label_userManagementPage.setDisabled(True)
        elif self.stacked.currentIndex() == 25:
            self.label_pageName.setText("Dial Indicator")
        elif self.stacked.currentIndex() == 26:
            self.label_pageName.setText("Program Settings")
        elif self.stacked.currentIndex() == 27:
            self.label_pageName.setText("Angle Calculation")
        elif self.stacked.currentIndex() == 28:
            self.label_pageName.setText("Settings")
        elif self.stacked.currentIndex() == 29:
            self.label_pageName.setText("Program List")

    # Link What To Set Page When Back Button Clicked
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
        elif self.stacked.currentIndex() == 20:
            self.stacked.setCurrentIndex(8)
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

    # Link What To Set Page When Forward Button Clicked
    def linkage_of_forwardButton(self):
        if self.stacked.currentIndex() == 7:
            self.stacked.setCurrentIndex(8)

    # What To Open Page When Button Gets Clicked
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
        self.button_addUpdateLogin.clicked.connect(lambda : self.stacked.setCurrentIndex(2))
        self.button_modifyLogin.clicked.connect(lambda : self.stacked.setCurrentIndex(2))

        # Report Page Clicked Slot
        self.label_reportPage.mousePressEvent = lambda event: self.stacked.setCurrentIndex(21)
        self.button_viewData.clicked.connect(lambda : self.stacked.setCurrentIndex(22))
        self.button_ListView.clicked.connect(lambda : self.stackedWidget.setCurrentIndex(0))
        self.button_ChartView.clicked.connect(lambda : self.stackedWidget.setCurrentIndex(1))
        self.button_HistogramChart.clicked.connect(lambda : self.stackedWidget.setCurrentIndex(2))

        # About Logo Page Clicked Slot
        self.label_aboutLogoPage.mousePressEvent = lambda event: self.stacked.setCurrentIndex(9)


    def load_data_to_ui(self):
        pass

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

    def load_IOSettings_to_ui(self):
        self.IOSettings_dict = {
                'AUTO_SAVE_READING': {'Enable': '0', 'Value': None},
                'BUZZER': {'Enable': '0', 'Value': 'Ok'},
                'CYCLE_STOP_TIMER': {'Enable': '0', 'Value': '2'},
                'DISPLAY_MODE': {'Enable': None, 'Value': 'Digit'},
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

    def load_IPSettings_to_ui(self):
        self.lineEdit_selfIp.setText(self.IPSettings_dict["SelfIPAddress"])
        self.lineEdit_subnetMask.setText(self.IPSettings_dict["SubnetMask"])
        self.lineEdit_defaultGateway.setText(self.IPSettings_dict["DefaultGateway"])

    def load_NetworkedDatabseSettings_to_ui(self):
        if self.NetworkedDatabaseSettings_dict["NETWORKE_BASED_DATABASE_ON_OFF"] == 'OFF':
            self.toggleButton_networkBasedDatabase.setPixmap(QPixmap("Switcher_OFF.png"))
        elif self.NetworkedDatabaseSettings_dict["NETWORKE_BASED_DATABASE_ON_OFF"] == 'ON':
            self.toggleButton_networkBasedDatabase.setPixmap(QPixmap("Switcher_On.png"))

        self.lineEdit_driverNameDb.setText(self.WifiSettings_dict["MS_SQL_DRIVER_NAME"])
        self.lineEdit_serverNameDb.setText(self.WifiSettings_dict["MS_SQL_SERVER_NAME"])
        self.lineEdit_databaseNameDb.setText(self.WifiSettings_dict["MS_SQL_DATABASE_NAME"])
        self.lineEdit_usernameDb.setText(self.WifiSettings_dict["MS_SQL_USERNAME"])
        self.lineEdit_passwordDb.setText(self.WifiSettings_dict["MS_SQL_PASSWORD"])

    def load_ProbeBasedSettings_to_ui(self):
        pass

    def load_AOCSettings_to_ui(self):
        pass

    def load_ProgramSettings_to_ui(self):
        pass

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


    def load_WifiSettings_to_ui(self):
        self.lineEdit_wifiSsid.setText(self.WifiSettings_dict["WifiSSID"])
        self.lineEdit_wifiPassword.setText(self.WifiSettings_dict["WifiPassword"])

    # Destructor Of Main Class
    def __del__(self):
        """Destructor to clean up"""
        # for movie in self.movies:
        #     if movie is not None:
        #         movie.stop()
        print("MainWindow destroyed.")

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
