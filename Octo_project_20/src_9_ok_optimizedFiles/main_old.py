from PySide2.QtWidgets import QApplication, QMainWindow, QStackedWidget , QWidget
from PySide2.QtWidgets import QFrame
from PySide2.QtWidgets import QLineEdit
from PySide2 import QtCore, QtWidgets
from PySide2.QtCore import QTimer, QTime, QDate , QObject , QThread , Signal, Qt, QCoreApplication
from PySide2.QtGui import QPixmap
from sqlalchemy.orm import *

import sys
# import the generated UI class
from main_ui_18 import Ui_MainWindow
from letters_keypad import Keyboard
from numpad import numpad_window
from factory_config import FactoryConfig
from messageBox import CustomMessageBox
from database import DatabaseAgent
from utilities import Utilities
from active_ui_handler import *
from value import Value
from set_master import SetMasterController
from models import *

from spi_module import SPI
import models
from sqlalchemy.orm import Session , sessionmaker

class Worker(QObject):
    spi_generated = Signal(str,str,str,str)

    #def __init__(self):
    spi = SPI('E')
    counter = 0
    def run(self):
        for value in self.spi.spi_value_emitter():
            #print(value)
            v1 , v2 , v3 , v4 = str(value[0]) , str(value[1]) , str(value[2]) , str(value[3])
            self.spi_generated.emit(v1,v2,v3,v4)
            #print(f"{value[0]}, {value[1]}, {value[2]}, {value[3]}")


# Main application window class, inherits QMainWindow and Ui_MainWindow
class MainWindow(QMainWindow, Ui_MainWindow):
    # Constructor: initializes UI, sets up stacked widget, keyboards, formulas, DB connections
    def __init__(self):#, gif_labels: dict):
        try:
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
            self.lineedit_opacity()
            self.comboBox_toselectProbe.clear()


            #self.spi = SPI('A')
            #self.spi_thread = threading.Thread(target=self.spi_handler,daemon=True)
            #self.spi_thread.start()

            self.worker_thread = QThread()
            self.worker = Worker()
            self.worker.moveToThread(self.worker_thread)

            self.worker_thread.started.connect(self.worker.run)

            self.worker.spi_generated.connect(self.spi_handler)
           # self.worker.spi_generated.connect(self.set_master)
            self.worker_thread.start()

            
            #self.stackedWidget_2.currentChanged.connect(self.labels_hide_from_ProgramSettings)
            self.stackedWidget_2.setCurrentIndex(0)
            self.apply_line_styles(thickness=3, color="#555555")
            # self.showFullScreen()
            self.valueObj = Value() #instance created for Value class
            self.databaseObj = DatabaseAgent() #instance/object created for DatabaseAgent class
            self.utils = Utilities(self.label_time, self.label_date, self.lineEdit_formulaBar)
            

            self.current_lineedit = None

            
            self.lineEdit_formulaBar.textChanged.connect(self.utils.validate_formulabar)
            self.valueObj.init_AngleCalculationSettings_dictionary()
            self.valueObj.init_mainProgramSettings_dictionary()
                 
            
            self.utils.start_clock_updates()
            self.load_databases()
            self.init_progId_and_dimension()
            self.load_as_per_progId()
            self.button_save.clicked.connect(self.linkage_of_saveButton)
            self.button_addUpdateLogin.clicked.connect(self.save_toDatabase_userManagement)
            self.button_spcDataCount.clicked.connect(self.save_toDatabase_aocSettings)
            self.button_setDateTime.clicked.connect(self.handle_set_datetime)
            self.button_setMaster.clicked.connect(self.set_master)
            
           
            self.toggle_button_eventHandling()

            
            # self.init_progId_and_dimension()
            # self.load_ProgramSettings_to_ui()

            #Update ui while __init__()
            
           
            update_angle_toggle(self)  # initialize toggle state at startup for anglecalculation
            update_rs232_toggle(self) #initialize toggle state at startup for rs232
            update_autooffcet_toggle(self)
            update_networkdatabase_toggle(self)
            update_IOSetting_Buzzer_toggle(self)
            update_IOSetting_Relay_toggle(self)
            update_IOSetting_CycleStopTimer_toggle(self)
            update_IOSetting_AutosaveReading_toggle(self)
            update_IOSetting_PartTraceability_toggle(self)
            update_IOSetting_TimetoMasterSet_toggle(self)
            update_IOSetting_MasterGrouping_toggle(self)
            
            self.master_value_labels = {
                "D1": {
                    "high": self.label_valMasterD1_2,
                    "low":  self.label_valMasterD1_1,
                },
                "D2": {
                    "high": self.label_valMasterD2_2,
                    "low":  self.label_valMasterD2_1,
                },
                "D3": {
                    "high": self.label_valMasterD3_2,
                    "low":  self.label_valMasterD3_1,
                },
                "D4": {
                    "high": self.label_valMasterD4_2,
                    "low":  self.label_valMasterD4_1,
                },
            }
            
            
            # ActiveProgramId Loaded Before
            # Load from DB first
            self.valueObj.AngleCalculationSettings_dict = self.databaseObj.load_data_to_AngleCalculationSettings_dict(self.valueObj.activeVariables_dict.get("ActiveProgramId", 1))
            
            self.load_data_to_ui()
            self.probe_data = {}

            # Load Active Program Id
            self.comboBox_programIdSetting.setCurrentText(str(self.valueObj.activeVariables_dict["ActiveProgramId"]))
         
            # Set Inner Program Id To The Active Id
            self.comboBox_programIdSettings.setCurrentText(str(self.valueObj.activeVariables_dict["ActiveProgramId"]))
            self.comboBox_programIdSetting.setCurrentText(str(self.valueObj.activeVariables_dict["ActiveProgramId"]))

            self.comboBox_programIdSetting.currentTextChanged.connect(self.progId_changed_outer)
            self.comboBox_programIdSettings.currentTextChanged.connect(self.progId_changed_inner)

            self.comboBox_toselectProbe.currentTextChanged.connect(lambda : self.load_as_per_dimension(self.comboBox_toselectProbe.currentText()))
            self.master_higher_value = None
            self.master_lower_value= None
            self.master_ready = False
            self.probe_labels = {
                "D1": self.label_value1,
                "D2": self.label_value2,
                "D3": self.label_value3,
                "D4": self.label_value4,
            }
            self.master_rows = {
                "D1": [
                    self.label_masterD1_1,      # M.L D1 title
                    self.label_masterD1_2,      # M.H D1 title
                    self.label_valMasterD1_1,   # value low
                    self.label_valMasterD1_2,# value high
                    self.line_10,
                    self.line_84,
                    
                ],
                "D2": [
                    self.label_masterD2_1,
                    self.label_masterD2_2,
                    self.label_valMasterD2_1,
                    self.label_valMasterD2_2,
                    self.line_11,
                    self.line_85,
                    
                ],
                "D3": [
                    self.label_masterD3_1,
                    self.label_masterD3_2,
                    self.label_valMasterD3_1,
                    self.label_valMasterD3_2,
                    self.line_12,
                    self.line_86,
                ],
                "D4": [
                    self.label_masterD4_1,
                    self.label_masterD4_2,
                    self.label_valMasterD4_1,
                    self.label_valMasterD4_2,
                    self.line_87,
                ],
            }

            self.spi_values = {}
            self.master_low = {}
            self.master_high = {}
             
            self.update_ui_after_programSettings_saved()
            
            self.comboBox_masterType.currentTextChanged.connect(self.apply_masterType_state)
            self.comboBox_ovalityOnOff.currentTextChanged.connect(self.apply_ProbeBasedSettings_state)

        except Exception as e:
            print(f"Error during initialization: {e}")
            raise  # re-raise to prevent app from starting
        
    def Hide_rows(self):
        for row_labels in self.master_rows.values():
            for lbl in row_labels:
                lbl.hide()

    #to enable disable line while switching combobox of Ovality ON and OFF
    def apply_ProbeBasedSettings_state(self):
        is_off = self.comboBox_ovalityOnOff.currentText() == "OFF"
        self.comboBox_ovalityOnOff.blockSignals(True)
        widgets = [
            self.label_case,
            self.label_caseT,
            self.comboBox_caseProbe,
            self.lineEdit_caseT
        ]
        for w in widgets:
            w.hide() if is_off else w.show()
        self.comboBox_ovalityOnOff.blockSignals(False)
        
    #to enable disable line while switching combobox of master Type single and double
    def apply_masterType_state(self):
        try:
            dimension = self.comboBox_toselectProbe.currentText()
            dim_data = self.valueObj.ProgramSettings_dict.get(dimension)
            probe = dim_data.get("ProbeBasedSettings", {})
            saved_master = probe.get("MasterType", "").strip().lower()
            print("Saved Master:",saved_master)
            current_master = self.comboBox_masterType.currentText().strip().lower()
            print("Current Master:",current_master)
            self.comboBox_masterType.blockSignals(True)
            if not saved_master:
                editable = True          # new dimension → allow edit
            else:
                editable = (saved_master == current_master)
            # editable = (saved_master == current_master)

            for w in (
                self.lineEdit_masterLower,
                self.lineEdit_master,
                self.lineEdit_masterHigher
            ):
                w.setEnabled(editable)
            self.comboBox_masterType.blockSignals(False)
        except Exception as e:
            print("Error in MasterType State:",e)

    #when line disable in probebased setting below function works for opacity
    def lineedit_opacity(self):
        style = """
        QLineEdit:disabled {
            background-color: #666666;
            
        }
        """
        self.lineEdit_masterLower.setStyleSheet(style)
        self.lineEdit_master.setStyleSheet(style)
        self.lineEdit_masterHigher.setStyleSheet(style)

    def spi_handler(self, v1, v2, v3, v4):
        """
        Receives live SPI values from Worker thread.
        Updates raw SPI labels and stores values for each probe.
        """
        try:
            # Update raw SPI display
            self.label_value1.setText(v1)
            self.label_value2.setText(v2)
            self.label_value3.setText(v3)
            self.label_value4.setText(v4)

            # Store cleaned SPI values mapped to probes
            self.spi_values["D1"] = float(self.clean_spi_value(v1))
            self.spi_values["D2"] = float(self.clean_spi_value(v2))
            self.spi_values["D3"] = float(self.clean_spi_value(v3))
            self.spi_values["D4"] = float(self.clean_spi_value(v4))

            # Check OK / NOT OK if master is set
            self.ok_notok_part_check()

        except Exception as e:
            print(f"[SPI_HANDLER ERROR] {e}")

        
    def clean_spi_value(self, value):
        """
        Cleans incoming SPI value.
        Example:
            "[1677]" -> "1677"
            [1677]   -> 1677
        """
        try:
            if isinstance(value, list):
                return value[0]
            if isinstance(value, str):
                return value.strip("[]")
            return value
        except Exception as e:
            print(f"[CLEAN_SPI ERROR] {e}")
            return 0

    
    def set_master(self):
        """
        Starts master setting process:
        - Captures High & Low master SPI
        - Calculates mm per raw
        - Stores probe calibration data
        """
        try:
            self.master_set = SetMasterController(
                parent=self,
                spi_values=self.spi_values,
                spi_signal=self.worker.spi_generated  # 🔥 PASS SIGNAL
            )

            # Receive computed probe calibration data
            self.master_set.master_finished.connect(self.on_master_finished)

            # Blocking call (modal dialogs inside)
            self.master_set.run()

        except Exception as e:
            print(f"[SET_MASTER ERROR] {e}")

    
    def on_master_finished(self, probe_data):
        self.probe_data = probe_data
        self.master_ready = True

    
    def ok_notok_part_check(self):
        """
        Converts live SPI values to mm and updates labels.
        Executed only when:
        - Master is set
        - Correct UI page is active
        """
        try:
            # Do nothing if master not ready
            if not getattr(self, "master_ready", False):
                return

            # Only active on measurement page
            if self.stacked.currentIndex() != 25:
                return

            for probe, pdata in self.probe_data.items():

                spi_new = self.spi_values.get(probe)
                if spi_new is None:
                    continue

                # SPI -> mm conversion
                new_mm = pdata["DB_low"] + \
                        (spi_new - pdata["SPI_low"]) * pdata["mm_per_raw"]

                # OK / NOT OK decision
                status = (
                    "OK"
                    if pdata["DB_low"] <= new_mm <= pdata["DB_high"]
                    else "NOT OK"
                )

                # Update corresponding probe label
                label = self.probe_labels.get(probe)
                if label:
                    label.setText(f"{new_mm:.3f}")

                # Optional debug
                # print(f"{probe} → {new_mm:.3f} [{status}]")

        except Exception as e:
            print(f"[OK_NOTOK ERROR] {e}")

        
        
    # On Program Id Changed , At Outer Page
    def progId_changed_outer(self):
        self.valueObj.activeVariables_dict["ActiveProgramId"] = self.comboBox_programIdSetting.currentText()
        self.comboBox_programIdSettings.setCurrentText(self.valueObj.activeVariables_dict.get("ActiveProgramId"))
        self.load_Higher_lower_value_to_ui(
        int(self.valueObj.activeVariables_dict["ActiveProgramId"])
        )
        # self.init_progId_and_dimension()
        self.load_as_per_progId()
        
    # On Program Id Changed , At Inner Page
    def progId_changed_inner(self):
        self.valueObj.activeVariables_dict["ActiveProgramId"] = self.comboBox_programIdSettings.currentText()
        self.comboBox_programIdSetting.setCurrentText(str(self.valueObj.activeVariables_dict.get("ActiveProgramId")))
        # self.init_progId_and_dimension()
        self.load_as_per_progId()
        #update d1 ,with set
        
    def update_ui_after_programSettings_saved(self):
        current_dim = self.comboBox_toselectProbe.currentText()

        self.valueObj.ProgramSettings_dict = \
            self.databaseObj.load_data_to_ProgramSettings_dict(
                int(self.valueObj.activeVariables_dict["ActiveProgramId"])
            )

        self.update_dimension_combobox(keep_dimension=current_dim)
        self.load_Higher_lower_value_to_ui(int(self.valueObj.activeVariables_dict["ActiveProgramId"]))


    def init_progId_and_dimension(self):
        try:
            proIds = self.databaseObj.get_all_program_ids()

            self.comboBox_programIdSetting.clear()
            self.comboBox_programIdSettings.clear()

            if not proIds:
                proIds = [1]

            next_id = max(proIds) + 1
            self.comboBox_programIdSetting.addItems(map(str, proIds))
            self.comboBox_programIdSettings.addItems(map(str, proIds + [next_id]))

            active_id = str(self.valueObj.activeVariables_dict.get("ActiveProgramId", proIds[0]))

            self.comboBox_programIdSetting.setCurrentText(active_id)
            self.comboBox_programIdSettings.setCurrentText(active_id)
        except Exception as e:
            print(f"Error in initialization of progId and dimension): {e}")
    
    def clear_master_values_ui(self):
        #help function to remove previous stored values
        for labels in self.master_value_labels.values():
            labels["high"].clear()
            labels["low"].clear()
        
    def load_Higher_lower_value_to_ui(self, program_id):
        try:
            # ✅ CLEAR OLD PROGRAM VALUES FIRST
            self.clear_master_values_ui()
            self.Hide_rows()
            with self.databaseObj.SessionLocal() as session:
                probes = (
                    session.query(ProbeBasedSettings)
                    .filter(ProbeBasedSettings.ProgramId == program_id)
                    .all()
                )

                print("Loaded probes from DB:", len(probes))

                for probe in probes:
                    dim = str(probe.Dimension).strip().upper()

                    print(
                        f"DB → {dim} | "
                        f"High={probe.MasterHigher}, "
                        f"Low={probe.MasterLower}"
                    )

                    if dim not in self.master_value_labels:
                        print("⚠️ No label mapping for", dim)
                        continue

                    labels = self.master_value_labels[dim]
                    for lbl in self.master_rows[dim]:
                        lbl.show()


                    lbl_high = labels["high"]
                    lbl_low  = labels["low"]

                    lbl_high.setText("" if probe.MasterHigher is None else str(probe.MasterHigher))
                    lbl_low.setText("" if probe.MasterLower is None else str(probe.MasterLower))
        except Exception as e:
            print(f"Error in load_higher_lower_value in ui): {e}")
            


    
    def get_dimension_list_for_combobox(self):
        # 1️⃣ Collect saved dimensions from DB
        saved_dims = sorted(
            [
                dim for dim in self.valueObj.ProgramSettings_dict.keys()
                if dim.startswith("D")
            ],
            key=lambda x: int(x[1:])
        )

        # 2️⃣ If nothing saved → start with D1
        if not saved_dims:
            return ["D1"]

        # 3️⃣ Find highest saved dimension
        last_dim_num = int(saved_dims[-1][1:])

        # 4️⃣ Allow one extra dimension (max D8)
        if last_dim_num < 8:
            return saved_dims + [f"D{last_dim_num + 1}"]

        return saved_dims


    def update_dimension_combobox(self, keep_dimension=None):
        dims = self.get_dimension_list_for_combobox()

        self.comboBox_toselectProbe.blockSignals(True)
        self.comboBox_toselectProbe.clear()
        self.comboBox_toselectProbe.addItems(dims)

        if keep_dimension in dims:
            self.comboBox_toselectProbe.setCurrentText(keep_dimension)
        else:
            self.comboBox_toselectProbe.setCurrentIndex(0)

        self.comboBox_toselectProbe.blockSignals(False)


    def load_as_per_progId(self):
        program_id = int(self.valueObj.activeVariables_dict.get("ActiveProgramId", 1))
        
        self.valueObj.ProgramSettings_dict = \
            self.databaseObj.load_data_to_ProgramSettings_dict(program_id)
        print("DEBUG ProgramSettings_dict keys:",
        self.valueObj.ProgramSettings_dict.keys())


        # 1️⃣ Load program-level UI only
        self.load_ProgramSettings_to_ui()

        # 2️⃣ Update dimensions based on DB
        self.update_dimension_combobox()

        # 3️⃣ Load D1 probe + AOC
        self.load_ProbeBasedSettings_to_ui("D1")
        self.load_AOCBasedSettings_to_ui("D1")
        #self.load_Higher_lower_value_to_ui()

        # 4️⃣ Load angle settings
        self.valueObj.AngleCalculationSettings_dict = \
            self.databaseObj.load_data_to_AngleCalculationSettings_dict(program_id)

        self.load_AngleCalculationSettings_to_ui()
        


    # As per dimension load to ui (ProbeBased & AOCBased)
    def load_as_per_dimension(self,dimension):
        try:
            #self.load_ProgramSettings_to_ui()   # ✅ ADD
            self.load_ProbeBasedSettings_to_ui(dimension)
            # print(self.valueObj.ProgramSettings_dict["D1"])
            # print(self.valueObj.ProgramSettings_dict["D2"])
            self.load_AOCBasedSettings_to_ui(dimension)
            # self.load_Higher_lower_value_to_ui()
        except Exception as e:
            print(f"Error in load_as_per_dimension: {e}")
            msg = CustomMessageBox("Failed to load dimension settings. Please check the database and try again.", "error",
                                   parent=self)
            msg.exec_()
    
    def toggle_button_eventHandling(self):
        toggle_buttons = [
        self.toggelButton_angleCalculation,
        self.toggleButton_rs232,
        self.toggleButton_aoc,
        self.toggleButton_networkBasedDatabase,
        self.toggleButton_buzzer,
        self.toggelButton_relay,
        self.toggelButton_cycleStopTimer,
        self.toggelButton_autoSaveReading,
        self.toggelButton_partTraceability,
        self.toggleButtontimeToSetMaster,
        self.toggleButton_masterGrouping
        ]

        for btn in toggle_buttons:
            btn.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents, False)
            btn.setMouseTracking(True)
            btn.installEventFilter(self)

    def handle_set_datetime(self):
        """
        Called when button_setDateTime is pressed.
        Updates Raspberry Pi or i.MX7 system time from UI line edits.
        """
        try:
            if self.utils.is_raspberry_pi():
                self.utils.set_system_time_raspberyPi() # Assuming this method exists and handles its own exceptions
            elif self.utils.is_imx7():
                self.utils.set_system_time_imx7() # Assuming this method exists and handles its own exceptions
            else:
                print("⚠️ Unknown board, cannot set system time")
                msg = CustomMessageBox("Unknown board, cannot set system time.", "warning",
                                       parent=self)
                msg.exec_()
        except Exception as e:
            print(f"Error setting system time: {e}")
            msg = CustomMessageBox("Failed to set system time. Please check inputs and try again.", "error",
                                   parent=self)
            msg.exec_()

    # save button link to set ui value to database
    # Handles save button functionality depending on current stacked widget page
    def linkage_of_saveButton(self):
        try:
            current_index = self.stacked.currentIndex()
            if current_index == 6:
                self.save_toDatabase_WifiSettings() #to save wifiSettings using save button
            elif current_index == 13:
                self.save_toDatabase_cncList()
            elif current_index == 7 or current_index == 8:
                self.save_toDatabase_IOSettings()
            elif current_index == 5: 
                self.save_toDatabase_IpSettings()
            elif  current_index == 3:
                self.save_toDatabase_rs232Settings()
            elif current_index == 27:
                self.save_toDatabase_angleCalculationSettings()
            elif current_index == 26:
                self.save_toDatabase_programSetting()
            elif current_index == 30:
                #self.save_toDatabase_programSetting()
                self.save_toDatabase_aocBasedSettings()
                # self.comboBox_ovalityOnOff.blockSignals(True)
                self.save_toDatabase_probeBasedSettings()
                # self.comboBox_ovalityOnOff.blockSignals(False)
            # elif current_index == 14 or current_index == 18:
            #     # This line seems to connect a button click inside another button click handler.
            #     # It should probably be self.save_toDatabase_aocSettings() directly,
            #     # or the connection should be made once during __init__.
            #     # For now, assuming it should call the save method directly.
            #     self.save_toDatabase_aocSettings()
            elif current_index == 10:
                # Similar to above, assuming direct call.
                self.save_toDatabase_shiftSettings()
            elif current_index == 16:
                # Similar to above, assuming direct call.
                self.save_toDatabase_networkedDatabase_settings()
        except Exception as e:
            print(f"Error in linkage_of_saveButton: {e}")
            msg = CustomMessageBox(f"An unexpected error occurred while trying to save settings: {e}", "error",
                                   parent=self)
            msg.exec_()

    #load Database to dictionary
    # Loads all settings from database into value object dictionaries
    def load_databases(self):
        try:
            self.valueObj.WifiSettings_dict = self.databaseObj.load_data_to_WifiSettings_dict()
        except Exception as e:
            print(f"Error loading WifiSettings: {e}")
            self.valueObj.WifiSettings_dict = {}  # set default

        try:
            default_programId = self.valueObj.activeVariables_dict.get('ActiveProgramId', 1)
            #print("default Program Id..............................................",default_programId)
            self.valueObj.AngleCalculationSettings_dict = self.databaseObj.load_data_to_AngleCalculationSettings_dict(str(default_programId))
        except Exception as e:
            print(f"Error loading AngleCalculationSettings: {e}")
            self.valueObj.AngleCalculationSettings_dict = {}

        try:
            self.valueObj.AOCSettings_dict = self.databaseObj.load_data_to_AOCSettings_dict()
        except Exception as e:
            print(f"Error loading AOCSettings: {e}")
            self.valueObj.AOCSettings_dict = {}

        try:
            self.valueObj.IOSettings_dict = self.databaseObj.load_data_to_IOSettings_dict()
        except Exception as e:
            print(f"Error loading IOSettings: {e}")
            self.valueObj.IOSettings_dict = {}

        try:
            self.valueObj.IPSettings_dict = self.databaseObj.load_data_to_IPSettings_dict()
        except Exception as e:
            print(f"Error loading IPSettings: {e}")
            self.valueObj.IPSettings_dict = {}

        try:
            self.valueObj.NetworkedDatabaseSettings_dict = self.databaseObj.load_data_to_NetworkedDatabaseSettings_dict()
        except Exception as e:
            print(f"Error loading NetworkedDatabaseSettings: {e}")
            self.valueObj.NetworkedDatabaseSettings_dict = {}

        try:
            self.valueObj.RS232Settings_dict = self.databaseObj.load_data_to_RS232Settings_dict()
        except Exception as e:
            print(f"Error loading RS232Settings: {e}")
            self.valueObj.RS232Settings_dict = {}

        try:
            default_programId = self.valueObj.activeVariables_dict.get('ActiveProgramId', 1)
            self.valueObj.ProgramSettings_dict = self.databaseObj.load_data_to_ProgramSettings_dict(int(default_programId))
        except Exception as e:
            print(f"Error loading ProgramSettings: {e}")
            self.valueObj.ProgramSettings_dict = {}

    #To save data  WifiSettings on table WifiSettings
    # Saves WiFi SSID and password into database
    def save_toDatabase_WifiSettings(self):
        try:
            ssid = self.lineEdit_wifiSsid.text()
            password = self.lineEdit_wifiPassword.text()

            # Call your database handler
            self.utils.Wifi_Settings(ssid,password) # connect to wifi
            self.databaseObj.upsert_wifi_settings(ssid, password) #to share ui text on db
            self.valueObj.WifiSettings_dict = self.databaseObj.load_data_to_WifiSettings_dict()

            #print("WiFi settings saved successfully.")
            msg = CustomMessageBox("WiFi settings saved successfully.", "success",
                                   parent=self)
            msg.exec_()
        except Exception as e:
            print(f"Error saving WiFi settings: {e}")
            msg = CustomMessageBox("Failed to save WiFi settings. Please check inputs and try again.", "error",
                                   parent=self)
            msg.exec_()

    #To save data  IPsettings on table IPSettings
    # Saves IP, subnetmask, and gateway into database and applies to device
    def save_toDatabase_IpSettings(self):
        try:
            ip = self.lineEdit_selfIp.text()
            subnetmask = self.lineEdit_subnetMask.text()
            gateway = self.lineEdit_defaultGateway.text()

            self.databaseObj.upsert_ip_settings(ip,subnetmask,gateway)
            self.valueObj.IPSettings_dict = self.databaseObj.load_data_to_IPSettings_dict()
            self.utils.apply_static_ip(ip,subnetmask,gateway)
            #print("Ip Setting saved successfully.")
            msg = CustomMessageBox("IP settings saved successfully.", "success",
                                   parent=self)
            msg.exec_()
        except Exception as e:
            print(f"Error saving IP settings: {e}")
            msg = CustomMessageBox("Failed to save IP settings. Please check inputs and try again.", "error",
                                   parent=self)
            msg.exec_()
    
    #To save data  shiftSettings on table shiftTimings
    # Saves shift timings (from-to) for 3 shifts into database
    def save_toDatabase_shiftSettings(self):
        try:
            shift1 = (self.lineEdit_shift1FromTime.text(),
                     self.lineEdit_shift1ToTime.text())
            shift2 = (self.lineEdit_shift2FromTime.text(),
                      self.lineEdit_shift2ToTime.text())
            shift3 = (self.lineEdit_shift3FromTime.text(),
                      self.lineEdit_shift3ToTime.text())

            # Call DB function
            self.databaseObj.upsert_shift_timings(shift1, shift2, shift3)
            #print("Shift settings saved")
            msg = CustomMessageBox("Shift settings saved successfully.", "success",
                                   parent=self)
            msg.exec_()
        except Exception as e:
            print(f"Error saving shift settings: {e}")
            msg = CustomMessageBox("Failed to save shift settings. Please check inputs and try again.", "error",
                                   parent=self)
            msg.exec_()

    #To save data  rs232Settings on table RS232Settings
    # Saves RS232 communication settings into database
    def save_toDatabase_rs232Settings(self):
        try:
            rs232OnOff = self.valueObj.activeVariables_dict.get('RS232OnOff','OFF')
            baudrate = self.comboBox_baudRate.currentText()
            dataBits = self.comboBox_dataBits.currentText()
            parity = self.comboBox_parity.currentText()
            stopBits = self.comboBox_stopBits.currentText()
            flowControl = self.comboBox_flowControl.currentText()
            portName = self.lineEdit_portName.text()

            self.databaseObj.update_rs232_settings(rs232OnOff,baudrate,dataBits,parity,stopBits,flowControl,portName)
            self.valueObj.RS232Settings_dict = self.databaseObj.load_data_to_RS232Settings_dict()
            
            # Also update activeVariables_dict for consistency
            self.valueObj.activeVariables_dict["RS232OnOff"] = rs232OnOff
            
            #print("rs232 settings saved successfully.")
            msg = CustomMessageBox("RS232 settings saved successfully.", "success",
                                   parent=self)
            msg.exec_()
        except Exception as e:
            print(f"Error saving RS232 settings: {e}")
            msg = CustomMessageBox("Failed to save RS232 settings. Please check inputs and try again.", "error",
                                   parent=self)
            msg.exec_()

    #To save data  networkDatabase on table NetworkDatabaseSettings
    # Saves network-based database connection settings
    def save_toDatabase_networkedDatabase_settings(self):
        try:
                networkBasedDatabaseOnOFF = self.valueObj.activeVariables_dict.get('NetworkedDatabaseSettingsOnOff','OFF')
                msSqlDriverName = self.lineEdit_driverNameDb.text()
                msSqlServerName = self.lineEdit_serverNameDb.text()
                msSqlDatabaseNme = self.lineEdit_databaseNameDb.text()
                msSqlUserName = self.lineEdit_usernameDb.text()
                msSqlPassword = self.lineEdit_passwordDb.text()

                self.databaseObj.update_networked_database_settings(networkBasedDatabaseOnOFF,msSqlDriverName,
                                                                    msSqlServerName,msSqlDatabaseNme,
                                                                    msSqlUserName,msSqlPassword)
                self.valueObj.NetworkedDatabaseSettings_dict = self.databaseObj.load_data_to_NetworkedDatabaseSettings_dict()
                
                self.valueObj.activeVariables_dict["NetworkedDatabaseSettingsOnOff"] = networkBasedDatabaseOnOFF

                #print("networkdatabase settings saved successfully.")
                msg = CustomMessageBox("Networked database settings saved successfully.", "success",
                                       parent=self)
                msg.exec_()
            
        except Exception as e:
            print(f"Error saving networked database settings: {e}")
            msg = CustomMessageBox("Failed to save networked database settings. Please check inputs and try again.", "error",
                                   parent=self)
            msg.exec_()

    #To save data  angleCalculationSettings on table angleCalculationSettings
    # Saves angle calculation settings (degree, min, sec, tolerances) into database
    def save_toDatabase_angleCalculationSettings(self):
        try:
            default_programId = self.valueObj.activeVariables_dict.get('ActiveProgramId', 1)
            # ensure comboBox has this program as text
            if self.comboBox_programId.findText(str(default_programId)) == -1:
                self.comboBox_programId.addItem(str(default_programId))

            # set it as the current selection
            self.comboBox_programId.setCurrentText(str(default_programId))
            def safe_int(value, default=0):
                try:
                    return int(value)
                except (ValueError, TypeError):
                    return default

            def safe_float(value, default=0.0):
                try:
                    return float(value)
                except (ValueError, TypeError):
                    return default
            # now when you read, it will not be blank
            programId = safe_int(self.comboBox_programId.currentText())
            #programId = self.comboBox_programIdSetting.currentText()
            angleCalculationOnOff = self.valueObj.activeVariables_dict.get('AngleCalculationOnOff','OFF')
            angleDegree = safe_int(self.lineEdit_angleDegree.text())
            angleMin = safe_int(self.lineEdit_angleMinutes.text())
            angleSec = safe_int(self.lineEdit_angleSeconds.text())
            tolaranceMin = safe_int(self.lineEdit_toleranceMin.text())
            tolaranceSec = safe_int(self.lineEdit_toleranceSec.text())
            negativeTolMin = safe_int(self.lineEdit_negativeTolMin.text())
            negativeTolSec = safe_int(self.lineEdit_negativeTolSec.text())
            distance = safe_float(self.lineEdit_distanceMm.text())
            angleType = ""
            if self.radioButton_2_fullAngle.isChecked():
                angleType = "Full Angle"  # or whatever string you store in DB
            elif self.radioButton_halfAngle.isChecked():
                angleType = "Half Angle"
            else:
                raise ValueError("Angle type not selected.")

            self.databaseObj.upsert_angle_calculation_settings(programId,angleCalculationOnOff,angleDegree,angleMin,
                                                                angleSec,tolaranceMin,tolaranceSec,
                                                                negativeTolMin,negativeTolSec,distance,angleType)
            # Reload latest DB values into dictionary
            self.valueObj.AngleCalculationSettings_dict = self.databaseObj.load_data_to_AngleCalculationSettings_dict(programId)
            
            self.valueObj.activeVariables_dict["AngleCalculationOnOff"] = angleCalculationOnOff

            #print("angleCalculation settings saved successfully.")
            msg = CustomMessageBox("Angle calculation settings saved successfully.", "success",
                                   parent=self)
            msg.exec_()
        except Exception as e:
            print(f"Error saving angle calculation settings: {e}")
            msg = CustomMessageBox("Failed to save angle calculation settings. Please check inputs and try again.", "error",
                                   parent=self)
            msg.exec_()
    #To save data  CncList on table CNCList
    # Saves CNC machine list details (name, ip, port, controller) into database
    def save_toDatabase_cncList(self):
        try:
            cncName = self.lineEdit_cncName.text()
            ipAddress = self.lineEdit_cncIpAddress.text()
            portNumber = self.lineEdit_cncPortNumber.text()
            cncSelection = self.comboBox_cncSelectionType.currentText()
            controller = self.comboBox_cncController.currentText()

            self.databaseObj.upsert_cnc_list(cncName,ipAddress,portNumber,
                                            cncSelection,controller)
            #print("cncList settings saved successfully.")
            msg = CustomMessageBox("CNC list settings saved successfully.", "success",
                                   parent=self)
            msg.exec_()
        except Exception as e:
            print(f"Error saving CNC list: {e}")
            msg = CustomMessageBox("Failed to save CNC list. Please check inputs and try again.", "error",
                                   parent=self)
            msg.exec_()

    #To save data  IOsettings on table IOSettings
    # Saves I/O related settings (buzzer, relay, cycleStop, displayMode, etc.)
    def save_toDatabase_IOSettings(self):
        try:
            
            buzzer_enable = self.valueObj.IOSettings_dict.get('BUZZER', {}).get('Enable', '0')
            relay_enable = self.valueObj.IOSettings_dict.get('RELAY', {}).get('Enable', '0')
            cycleStopTimer_enable = self.valueObj.IOSettings_dict.get('CYCLE_STOP_TIMER', {}).get('Enable', '0')
            autoSaveReading_enable = self.valueObj.IOSettings_dict.get('AUTO_SAVE_READING', {}).get('Enable', '0')
            partTraceabilty_enable = self.valueObj.IOSettings_dict.get('PART_TRACEABILITY', {}).get('Enable', '0')
            displayMode_value = self.comboBox_displayMode.currentText()
            timetoMasterSet_enable = self.valueObj.IOSettings_dict.get('TIME_TO_MASTER_SET', {}).get('Enable', '0')
            masterGrouping_enable = self.valueObj.IOSettings_dict.get('MASTER_GROUPING', {}).get('Enable', '0')
            

            # Assuming these line edits hold the 'Value' part of the tuple
            relay_value = self.lineEdit_relayTime.text()
            cycleStopTimer_value = self.lineEdit_cycleTime.text()
            timetoMasterSet_value = self.lineEdit_timeToMasterSet.text()

            # Determine buzzer value based on radio buttons
            buzzer_value = ""
            if self.radioButton_okBuzzer.isChecked():
                buzzer_value = "Ok"
            elif self.radioButton_reworkNotokBuzzer.isChecked():
                buzzer_value = "Rework / Not Ok"
            else:
                raise ValueError("Buzzer value not selected.")
            
            # Determine part traceability value based on radio buttons
            partTraceabilty_value = ""
            if self.radioButton_manualPartTraceability.isChecked():
                partTraceabilty_value = "Manual Reset"
            elif self.radioButton_autoPartTraceability.isChecked():
                partTraceabilty_value = "Auto Reset"
            else:
                raise ValueError("Part traceability value not selected.")

            self.databaseObj.update_io_settings(
                (buzzer_enable, buzzer_value),
                (relay_enable, relay_value),
                (cycleStopTimer_enable, cycleStopTimer_value),
                (autoSaveReading_enable, None), # Assuming autoSaveReading doesn't have a specific value field
                (partTraceabilty_enable, partTraceabilty_value),
                (None, displayMode_value), # Assuming displayMode is only a value, not an enable toggle
                (timetoMasterSet_enable, timetoMasterSet_value),
                (masterGrouping_enable, None) # Assuming masterGrouping doesn't have a specific value field
            )
            self.valueObj.IOSettings_dict = self.databaseObj.load_data_to_IOSettings_dict()
            #
            self.valueObj.activeVariables_dict["BUZZER"] = buzzer_enable
            self.valueObj.activeVariables_dict["RELAY"] = relay_enable
            self.valueObj.activeVariables_dict["CYCLE_STOP_TIMER"] = cycleStopTimer_enable
            self.valueObj.activeVariables_dict["AUTO_SAVE_READING"] = autoSaveReading_enable
            self.valueObj.activeVariables_dict["PART_TRACEABILITY"] = partTraceabilty_enable
            self.valueObj.activeVariables_dict["TIME_TO_MASTER_SET"] = timetoMasterSet_enable
            self.valueObj.activeVariables_dict["MASTER_GROUPING"] = masterGrouping_enable

            #print("Iosettings settings saved successfully.")
            msg = CustomMessageBox("I/O settings saved successfully.", "success",
                                   parent=self)
            msg.exec_()
        except Exception as e:
            print(f"Error saving IO settings: {e}")
            msg = CustomMessageBox("Failed to save IO settings. Please check inputs and try again.", "error",
                                   parent=self)
            msg.exec_()

    #To save data  aocSettings on table AOCSettings
    # Saves Auto Offset Correction (AOC) settings into database
    def save_toDatabase_aocSettings(self):
        try:
            aocOnOff = self.valueObj.activeVariables_dict.get('AOCOnOff',"OFF")
            spcDataCount = self.lineEdit_spcDataCount.text()
            self.databaseObj.update_aoc_settings(aocOnOff,spcDataCount)
            self.valueObj.activeVariables_dict["AOCOnOff"] = aocOnOff
            
            #print("aoc settings saved successfully.")
            msg = CustomMessageBox("AOC settings saved successfully.", "success",
                                   parent=self)
            msg.exec_()
        except Exception as e:
            print(f"Error saving AOC settings: {e}")
            msg = CustomMessageBox("Failed to save AOC settings. Please check inputs and try again.", "error",
                                   parent=self)
            msg.exec_()

    #To save data  UserManagement on table UserManagement
    # Saves user management credentials and access type into database
    def save_toDatabase_userManagement(self):
        try:
            setUsername = self.lineEdit_setUsernameLogin.text()
            setPassword = self.lineEdit_setPasswordLogin.text()
            setAccessType = self.comboBox_setAccessCombo.currentText()

            self.databaseObj.upsert_user_management(setUsername,setPassword,setAccessType)
            # The line below seems incorrect, AOCSettings_dict is not related to user management.
            # It should probably be self.valueObj.UserManagment_dict = self.databaseObj.load_data_to_UserManagment_dict()
            # Assuming for now it's just a placeholder or will be corrected elsewhere.
            # self.valueObj.AOCSettings_dict = self.databaseObj.load_data_to_AOCSettings_dict() 
            #print("userManagement settings saved successfully.")
            msg = CustomMessageBox("User management settings saved successfully.", "success",
                                   parent=self)
            msg.exec_()
        except Exception as e:
            print(f"Error saving user management: {e}")
            msg = CustomMessageBox("Failed to save user management. Please check inputs and try again.", "error",
                                   parent=self)
            msg.exec_()

    #To save data  ProgramSettings on table ProgramSettings
    # Saves program settings (programId, name, mode, unit, autosave duration) into database
    def save_toDatabase_programSetting(self):
        try:
            default_programId = self.valueObj.activeVariables_dict.get('ActiveProgramId', 1)
            # ensure comboBox has this program as text
            if self.comboBox_programId.findText(str(default_programId)) == -1:
                self.comboBox_programId.addItem(str(default_programId))

            # set it as the current selection
            self.comboBox_programId.setCurrentText(str(default_programId))

            # now when you read, it will not be blank
            programId = int(self.comboBox_programId.currentText())
            programName = self.lineEdit_programNameSettings.text()
            durationForAutosave = float(self.lineEdit_DurationAutosave.text())

            mode = ""
            uom = ""
            if self.radioButton_modeCombine.isChecked():
                mode = "Combine"
            elif self.radioButton_modeIndividual.isChecked():
                mode = "Individual"
            else:
                raise ValueError("Program mode not selected.")

            if self.radioButton_inch.isChecked():
                uom = "inch"
            elif self.radioButton_mm.isChecked():
                uom = "mm"
            else:
                raise ValueError("Unit of measurement not selected.")

            self.databaseObj.upsert_program_settings(programId,programName,mode,
                                                    uom,durationForAutosave)

            # print("ProgramSetting settings saved successfully.")
            msg = CustomMessageBox("Program settings saved successfully.", "success",
                                   parent=self)
            msg.exec_()
        except Exception as e:
            print(f"Error saving program settings: {e}")
            msg = CustomMessageBox("Failed to save program settings. Please check inputs and try again.", "error",
                                   parent=self)
            msg.exec_()

    #To save data  ProbeBasedSettings on table ProbeBasedSettings
    # Saves probe-based measurement settings into database
    def save_toDatabase_probeBasedSettings(self):
        try:
            default_programId = self.valueObj.activeVariables_dict.get('ActiveProgramId', 1)
            # ensure comboBox has this program as text
            if self.comboBox_programId.findText(str(default_programId)) == -1:
                self.comboBox_programId.addItem(str(default_programId))
            

            # set it as the current selection
            self.comboBox_programId.setCurrentText(str(default_programId))

            # now when you read, it will not be blank
            programId = int(self.comboBox_programId.currentText())
            #programId = self.valueObj.activeVariables_dict['ActiveProgramId']
            dimension = self.comboBox_toselectProbe.currentText()
            formulaBar = self.label_formulaBar.text()
            masterType = self.comboBox_masterType.currentText()
            masterLower = float(self.lineEdit_masterLower.text())
            master = float(self.lineEdit_master.text())
            masterHigher = float(self.lineEdit_masterHigher.text())
            uol = float(self.lineEdit_upperOffcetLimit.text())
            usl = float(self.lineEdit_usl.text())
            ucl = float(self.lineEdit_ucl.text())
            nominal = float(self.lineEdit_nominalValue.text())
            lcl = float(self.lineEdit_lcl.text())
            lsl = float(self.lineEdit_lsl.text())
            lol = float(self.lineEdit_lowerOffsetLimit.text())
            ovality = self.comboBox_ovalityOnOff.currentText()
            #range_val = float(self.comboBox_rangeProbe.currentText())
            method = self.comboBox_methodProbe.currentText()
            probe_sensitivity = int(self.lineEdit_probeSensitivity.text())
            air_sensitivity_quotient = self.lineEdit_airSensitivityQuotient.text()
            
            if(ovality == 'OFF'):
                case = None
                caseT = None
            else:
                case = self.comboBox_caseProbe.currentText()
                caseT = float(self.lineEdit_caseT.text())
                
            self.databaseObj.upsert_probe_based_settings(
                program_id = programId,
                dimension = dimension,
                formula = formulaBar ,
                master_type = masterType ,
                master_lower = masterLower ,
                master = master ,
                master_higher = masterHigher ,
                upper_offset_limit = uol ,
                upper_specification_limit = usl ,
                upper_control_limit = ucl ,
                nominal_value = nominal ,
                lower_control_limit = lcl ,
                lower_specification_limit = lsl ,
                lower_offset_limit = lol ,
                ovality = ovality ,
                range_val = 0.6 ,
                method = method ,
                case = case ,
                case_t = caseT ,
                probe_sensitivity = probe_sensitivity ,
                air_sensitivity_quotient = air_sensitivity_quotient
            )
            self.update_ui_after_programSettings_saved() #to refresh database updated on ui
            #self.update_label_value_Higher_lower()
            # print("Probebased settings saved successfully.")
            msg = CustomMessageBox("Probe-based settings saved successfully.", "success",
                                   parent=self)
            msg.exec_()
        except Exception as e:
            print(f"Error saving probe based settings: {e}")
            msg = CustomMessageBox("Failed to save probe based settings. Please check inputs and try again.", "error",
                                   parent=self)
            msg.exec_()
    

    #To save data  aocBasedSetting on table AOCBasedSettings
    # Saves AOC-based (Auto Offset Correction) settings into database
    def save_toDatabase_aocBasedSettings(self):
        try:
            current = self.valueObj.AOCSettings_dict['AOC_ON_OFF']
            print("current aoc status:",current)
            if(current == "OFF"):
                return
            default_programId = self.valueObj.activeVariables_dict.get('ActiveProgramId', 1)
            # ensure comboBox has this program as text
            if self.comboBox_programId.findText(str(default_programId)) == -1:
                self.comboBox_programId.addItem(str(default_programId))

            # set it as the current selection
            self.comboBox_programId.setCurrentText(str(default_programId))

            # now when you read, it will not be blank
            programId = int(self.comboBox_programId.currentText())
            #programId = self.valueObj.activeVariables_dict['ActiveProgramId']
            dimension = self.comboBox_toselectProbe.currentText()
            axis = self.comboBox_axis.currentText()
            offset = int(self.lineEdit_offsetNo.text())
            machine = 'cnc' #self.comboBox_machine.currentText()
            direction = self.comboBox_direction.currentText()
            turretNo = int(self.lineEdit_turretNo.text())
            bufferPartNo = int(self.lineEdit_bufferPartNo.text())

            self.databaseObj.upsert_aoc_based_settings(
                program_id = programId,
                dimension = dimension,
                axis = axis,
                offset_no = offset,
                machine = machine,
                direction = direction,
                turret_no = turretNo,
                buffer_part_no = bufferPartNo
            )
            #print("aocBased settings saved successfully.")
            msg = CustomMessageBox("AOC-based settings saved successfully.", "success",
                                   parent=self)
            msg.exec_()
        except Exception as e:
            print(f"Error saving AOC based settings: {e}")
            msg = CustomMessageBox("Failed to save AOC based settings. Please check inputs and try again.", "error",
                                   parent=self)
            msg.exec_()

    #letter keyboard/numpad applied to follwing lineedits 
    # Assigns on-screen keyboard/numpad to specific line edits for text/numeric input
    def setup_lineedit_keyboards(self):
        try:
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
                self.lineEdit_leastCount,
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
        except Exception as e:
            print(f"Error setting up line edit keyboards: {e}")

    # Function To Set Page Labels At Page Changes
    # Updates the header label and button visibility based on current page index
    def set_labels_to_header(self):
        try:
            self.button_home.setEnabled(True)
            self.button_forward.setEnabled(True)
            self.button_back.setEnabled(True)

            current_index = self.stacked.currentIndex()

            # Reset visibility for all buttons to default (show) before specific hides
            self.button_home.show()
            self.button_forward.show()
            self.button_back.show()
            self.button_save.show()
            self.button_shutdown.show() # Assuming it's generally visible unless specified
          

            if current_index == 0:
                self.label_pageName.setText("User Login")
                self.button_home.hide()
                self.button_forward.hide()
                self.button_back.hide()
                self.button_save.hide()
                self.button_shutdown.hide() # Hide shutdown on login page

            elif current_index == 1 :
                self.label_pageName.setText("User Management")
                self.button_save.hide()
                self.button_forward.hide()
                self.button_shutdown.hide()
            elif current_index == 2:
                self.label_pageName.setText("User Settings")
                self.button_save.hide()
                self.button_forward.hide()
                self.button_home.hide()
                self.button_shutdown.hide()
            elif current_index == 3:
                self.label_pageName.setText("RS 232 Settings")
                self.button_forward.hide()
                self.button_home.hide()
                self.button_shutdown.hide()
            elif current_index == 4:
                self.label_pageName.setText("Formula Settings")
                self.button_save.hide()
                self.button_back.hide()
                self.button_forward.hide()
                self.button_home.hide()
                self.button_shutdown.hide()
            elif current_index == 5:
                self.label_pageName.setText("IP Settings")
                self.button_forward.hide()
                self.button_home.hide()
                self.button_shutdown.hide()
            elif current_index == 6:
                self.label_pageName.setText("Wifi Settings")
                self.button_forward.hide()
                self.button_home.hide()
                self.button_shutdown.hide()
            elif current_index == 7: 
                self.label_pageName.setText("I/O Settings")
                self.button_save.hide()
                self.button_home.hide()
                self.button_shutdown.hide()
            elif current_index == 8:
                self.label_pageName.setText("I/O Settings")
                self.button_forward.hide()
                self.button_shutdown.hide()
            elif current_index == 9:
                self.label_pageName.setText("About")
                self.button_save.hide()
                self.button_forward.hide()
                self.button_shutdown.hide()
            elif current_index == 10:
                self.label_pageName.setText("Clock Settings")
                self.button_save.hide()
                self.button_forward.hide()
                self.button_shutdown.hide()
            elif current_index == 12:
                self.label_pageName.setText("CNC List")
                self.button_save.hide()
                self.button_forward.hide()
                self.button_shutdown.hide()
            elif current_index == 13:
                self.label_pageName.setText("CNC Settings")
                self.button_forward.hide()
                self.button_home.hide()
                self.button_shutdown.hide()
            elif current_index == 14:
                self.label_pageName.setText("Auto Offset Settings")
                self.button_save.hide()
                self.button_forward.hide()
                self.button_shutdown.hide()
            elif current_index == 16:
                self.label_pageName.setText("Database Settings")
                self.button_forward.hide()
                self.button_home.hide()
                self.button_shutdown.hide()
            # elif current_index == 17:
            #     self.label_pageName.setText("Part Settings")
            #     self.button_forward.hide()
            #     self.button_home.hide()
            #     self.button_shutdown.hide()
            elif current_index == 30:
                self.label_pageName.setText("Part Settings")
                self.button_forward.show()
                self.button_home.show()
                self.button_back.show()
                self.button_shutdown.hide()
            elif current_index == 18:
                self.label_pageName.setText("AOC Report")
                self.button_save.hide()
                self.button_back.hide()
                self.button_forward.hide()
                self.button_shutdown.hide()
            elif current_index == 19:
                self.label_pageName.setText("Factory Calibration")
                self.button_save.hide()
                self.button_forward.hide()
                self.button_shutdown.hide()
            # elif self.stacked.currentIndex() == 20:
            #     self.label_pageName.setText("Air Saving Settings")
            elif current_index == 21 or current_index == 22:
                self.label_pageName.setText("Reports")
                self.button_save.hide()
                self.button_forward.hide()
                self.button_shutdown.hide()
            elif current_index == 23:
                self.label_pageName.setText("Home Page")
                self.button_save.hide()
                self.button_back.hide()
                self.button_forward.hide()
            elif current_index == 25:
                self.label_pageName.setText("Dial Indicator")
                self.button_forward.hide()
                self.button_shutdown.hide()
                self.label_value3.hide()
                self.label_value4.hide()
            elif current_index == 26:
                self.label_pageName.setText("Program Settings")
                self.button_save.show()
                self.button_forward.hide()
                self.button_home.hide()
                self.button_shutdown.hide()
            elif current_index == 27:
                self.label_pageName.setText("Angle Calculation")
                self.button_forward.hide()
                self.button_home.show()
                self.button_shutdown.hide()
            elif current_index == 28:
                self.label_pageName.setText("Settings")
                self.button_save.hide()
                self.button_forward.hide()
                self.button_shutdown.hide()
                
                
            elif current_index == 29:
                self.label_pageName.setText("Program List")
                self.button_save.hide()
                self.button_forward.hide()
                self.button_shutdown.hide()
        except Exception as e:
            print(f"Error in set_labels_to_header: {e}")

            
    #Backbutton link using currentindex
    # Handles back button navigation depending on current page index
    def linkage_of_backButton(self):
        try:
            current_index = self.stacked.currentIndex()
            if current_index == 9:
                self.stacked.setCurrentIndex(23)
            elif current_index == 25:
                self.stacked.setCurrentIndex(23)
            elif current_index == 28:
                self.stacked.setCurrentIndex(23)
            # elif current_index == 26:
            #     self.stacked.setCurrentIndex(17)
            elif current_index == 26:
                self.stacked.setCurrentIndex(30)
            elif current_index == 27:
                self.stacked.setCurrentIndex(26)
            elif current_index == 8:
                self.stacked.setCurrentIndex(7)
            elif current_index == 7:
                self.stacked.setCurrentIndex(23)
            elif current_index == 18:
                self.stacked.setCurrentIndex(14)
            elif current_index == 13:
                self.stacked.setCurrentIndex(12)
            elif current_index == 12:
                self.stacked.setCurrentIndex(14)
            elif current_index == 14:
                self.stacked.setCurrentIndex(23)
            elif current_index == 19:
                self.stacked.setCurrentIndex(8)
            elif current_index == 16:
                self.stacked.setCurrentIndex(8)
            elif current_index == 3:
                self.stacked.setCurrentIndex(8)
            # elif self.stacked.currentIndex() == 20:
            #     self.stacked.setCurrentIndex(8)
            elif current_index == 5:
                self.stacked.setCurrentIndex(8)
            elif current_index == 6:
                self.stacked.setCurrentIndex(8)
            # elif current_index == 4:
            #     self.stacked.setCurrentIndex(17)
            elif current_index == 4:
                self.stacked.setCurrentIndex(30)
            elif current_index == 10:
                self.stacked.setCurrentIndex(23)
            elif current_index == 2:
                self.stacked.setCurrentIndex(1)
            elif current_index == 1:
                self.stacked.setCurrentIndex(23)
            elif current_index == 22:
                self.stacked.setCurrentIndex(21)
            elif current_index == 21:
                self.stacked.setCurrentIndex(23)
            # elif current_index == 17:
            #     self.stacked.setCurrentIndex(28)
            #elif current_index == 30:
                #self.stacked.setCurrentIndex(28)
            elif current_index == 29:
                self.stacked.setCurrentIndex(28)
            elif self.stackedWidget_2.currentIndex() == 1:
                self.stackedWidget_2.setCurrentIndex(0)
            elif self.stackedWidget_2.currentIndex() == 3:
                self.stackedWidget_2.setCurrentIndex(2)
            elif self.stackedWidget_2.currentIndex() == 4:
                self.stackedWidget_2.setCurrentIndex(3)
            elif self.stackedWidget_2.currentIndex() == 2:
                self.stackedWidget_2.setCurrentIndex(1)
        except Exception as e:
            print(f"Error in linkage_of_backButton: {e}")

    # Formula Bar code
    # Inserts operators or variables into the formula bar line edit
    def insert_formula_text(self, text):
        try:
            cursor = self.lineEdit_formulaBar.cursorPosition()
            current_text = self.lineEdit_formulaBar.text()
            new_text = current_text[:cursor] + text + current_text[cursor:]
            self.lineEdit_formulaBar.setText(new_text)
            self.lineEdit_formulaBar.setCursorPosition(cursor + len(text))
        except Exception as e:
            print(f"Error inserting formula text: {e}")

    # Connects formula bar buttons (+, -, *, functions, etc.) to formula text insertion
    def linkage_formula_bar(self):
        try:
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
        except Exception as e:
            print(f"Error linking formula bar buttons: {e}")
        

    # Saves current formula bar content to a label (for display/storage)
    def save_formula_to_label(self):
        try:
            self.keyboard_open = False
            if hasattr(self, "current_keyboard") and self.current_keyboard is not None:
                self.current_keyboard.close()
                self.current_keyboard = None
            text = self.lineEdit_formulaBar.text()
            print("Formula to save:", text)
            print("TextEdit reference:", self.label_formulaBar)
            if text:  # only update if not empty
                self.label_formulaBar.setText(text)
                #self.stacked.setCurrentIndex(17)
                self.stacked.setCurrentIndex(30)
                
            else:
                self.label_formulaBar.setText("No formula set")
        except Exception as e:
            print(f"Error saving formula to label: {e}")


    # Deletes the last character from the formula bar line edit
    def delete_last_character(self):
        try:
            cursor = self.lineEdit_formulaBar.cursorPosition()
            if cursor > 0:
                current_text = self.lineEdit_formulaBar.text()
                new_text = current_text[:cursor-1] + current_text[cursor:]
                self.lineEdit_formulaBar.setText(new_text)
                self.lineEdit_formulaBar.setCursorPosition(cursor-1)
        except Exception as e:
            print(f"Error deleting last character from formula bar: {e}")

    #ui setting for forward button
    # Handles forward button navigation for certain pages
    def linkage_of_forwardButton(self):
        try:
            if self.stacked.currentIndex() == 7:
                self.stacked.setCurrentIndex(8)
            elif self.stackedWidget_2.currentIndex() == 0:
                self.stackedWidget_2.setCurrentIndex(1)
            elif self.stackedWidget_2.currentIndex() == 1:
                self.stackedWidget_2.setCurrentIndex(2)
            elif self.stackedWidget_2.currentIndex() == 2:
                self.stackedWidget_2.setCurrentIndex(3)
            elif self.stackedWidget_2.currentIndex() == 3:
                self.stackedWidget_2.setCurrentIndex(4)
        except Exception as e:
            print(f"Error in linkage_of_forwardButton: {e}")
    
     
    def linkage_of_forwardSetting(self):
        try:
            if self.stackedWidget_2.currentIndex() == 0:
                self.stackedWidget_2.setCurrentIndex(1)
            elif self.stackedWidget_2.currentIndex() == 1:
                self.stackedWidget_2.setCurrentIndex(2)
            elif self.stackedWidget_2.currentIndex() == 2:
                self.stackedWidget_2.setCurrentIndex(3)
        except Exception as e :
            print(f"Error in linkage_of_forwardSettings: {e}")
            
    def linkage_of_backSettings(self):
        try:
            if self.stackedWidget_2.currentIndex() == 1:
                self.stackedWidget_2.setCurrentIndex(0)
            elif self.stackedWidget_2.currentIndex() == 3:
                self.stackedWidget_2.setCurrentIndex(2)
            elif self.stackedWidget_2.currentIndex() == 2:
                self.stackedWidget_2.setCurrentIndex(1)
        except Exception as e :
           print(f"Error in linkage_of_backSettings")
            


    # Connects all UI buttons and labels to their respective slots/pages
    def linkage_of_ui(self):
        try:
            # Footer Buttons Signals Slots Implementation
            self.button_back.clicked.connect(self.linkage_of_backButton)
            self.button_forward.clicked.connect(self.linkage_of_forwardButton)
            #self.button_fowardSettings.clicked.connect(self.linkage_of_forwardSetting)
            #self.button_backSettings.clicked.connect(self.linkage_of_backSettings)
            self.button_home.clicked.connect(lambda : self.stacked.setCurrentIndex(23))

            # To Be Removed
            self.button_login.clicked.connect(lambda : self.stacked.setCurrentIndex(23))

            # Dial Indicator Page Clicked Slot
            self.label_dialIndicatorPage.mousePressEvent = lambda event: self.stacked.setCurrentIndex(25)
            
            # Settings Page Clicked Slot
            self.label_settingsPage.mousePressEvent = lambda event: self.stacked.setCurrentIndex(28)
            self.button_partSettings.clicked.connect(lambda : self.stacked.setCurrentIndex(30))
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
        except Exception as e:
            print(f"Error linking UI elements: {e}")

    # Applies thickness and color styles to all QFrame lines in the UI
    def apply_line_styles(self, thickness=3, color="#555555"):
        """
        Apply thickness and color to all QFrame lines in the central widget.
        Horizontal lines get fixed height, vertical lines get fixed width.
        """
        try:
            # Iterate through all QFrame children of centralwidget
            for line in self.centralwidget.findChildren(QFrame):
                if line.frameShape() == QFrame.HLine:
                    line.setFixedHeight(thickness)
                    line.setStyleSheet(f"background-color: {color};")
                elif line.frameShape() == QFrame.VLine:
                    line.setFixedWidth(thickness)
                    line.setStyleSheet(f"background-color: {color};")
        except Exception as e:
            print(f"Error applying line styles: {e}")
    
    def handle_shutdown(self):
        """
        Called when the shutdown button is pressed.
        Delegates the shutdown to Utilities class.
        """
        try:
            # Call the shutdown function from utils
            self.utils.shutdown_device()
        except Exception as e:
            print(f"Error during shutdown: {e}")
            msg = CustomMessageBox("Failed to shutdown device. Please try again.", "error")
            msg.exec_()

    def handle_restart(self):
        """
        Called when the reboot button is pressed.
        Delegates the rebbot to Utilities class.
        """
        try:
            # Call the reboot function from utils
            self.utils.restart_device()
        except Exception as e:
            print(f"Error during restart: {e}")
            msg = CustomMessageBox("Failed to restart device. Please try again.", "error",
                                   parent=self)
            msg.exec_()
    
    def handle_logout(self):
        try:
            self.stacked.setCurrentIndex(0) #to hadle logout 
        except Exception as e:
            print(f"Error during logout: {e}")
        
    # Initializes the shutdown button with logout/shutdown/restart menu actions
    def powerButton(self):
        try:
            # Connect the button to show the menu
            self.button_shutdown.clicked.connect(self.show_menu)

            # Create the menu
            self.menu = QtWidgets.QMenu()
            self.menu.setStyleSheet("""
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
            self.menu.addAction("Logout", self.logout)
            self.menu.addAction("Shutdown", self.shutdown)
            self.menu.addAction("Restart", self.restart)
        except Exception as e:
            print(f"Error initializing power button menu: {e}")
                                        
    def show_menu(self):
        try:
            # Position menu below button
            self.menu.setMinimumWidth(200)  # make a little wider if you want
            pos = self.button_shutdown.mapToGlobal(
            QtCore.QPoint(0, self.button_shutdown.height() - 50)  # -30 moves menu UP
            )
            self.menu.exec_(pos)
        except Exception as e:
            print(f"Error showing power menu: {e}")

    # Shows logout confirmation dialog
    def logout(self):
        try:
            logout_dlg = CustomMessageBox("  Do you really want to logout?", "info",
                                          parent=self)
            logout_dlg.accepted.connect(self.handle_logout)
            logout_dlg.exec_()   # Wait for user to press OK
        except Exception as e:
            print(f"Error showing logout dialog: {e}")
        

    # Shows shutdown confirmation dialog
    def shutdown(self):
        try:
            shudtdown_dlg = CustomMessageBox("  Do you really want to Shutdown?", "info",
                                             parent=self)
            # Connect the 'Yes' or 'OK' button to the actual shutdown
            shudtdown_dlg.accepted.connect(self.handle_shutdown)  # runs when user clicks Yes/OK                      
            shudtdown_dlg.exec_()   # Wait for user to press OK
            #print("Shutdown clicked")
        except Exception as e:
            print(f"Error showing shutdown dialog: {e}")

    # Shows restart confirmation dialog
    def restart(self):
        try:
            restart_dlg = CustomMessageBox("  Do you really want to Restart?", "info",
                                           parent=self)
            restart_dlg.accepted.connect(self.handle_restart)                        
            restart_dlg.exec_()   # Wait for user to press OK
            #("Restart clicked")
        except Exception as e:
            print(f"Error showing restart dialog: {e}")
      
        # These lines are redundant as they are already in powerButton()
        # self.menu.addAction("Logout", self.logout)
        # self.menu.addAction("Shutdown", self.shutdown)
        # self.menu.addAction("Restart", self.restart)

    # Displays the power menu below the shutdown button
 
    #to manage     
    # Captures mouse press events on line edits to show custom keyboard/numpad
    def eventFilter(self, obj, event):
        try:
            # Handle toggle button click
            if obj == self.toggelButton_angleCalculation and event.type() == event.MouseButtonPress:
                current = self.valueObj.AngleCalculationSettings_dict['ANGLE_CALCULATION_SETTINGS_ON_OFF']
                # Flip the value
                self.valueObj.AngleCalculationSettings_dict['ANGLE_CALCULATION_SETTINGS_ON_OFF'] = 'OFF' if current == 'ON' else 'ON'
                # Update the pixmap and other widgets
                update_angle_toggle(self)
                return True  # Event handled
            
            if obj == self.toggleButton_rs232 and event.type() == event.MouseButtonPress:
                current = self.valueObj.RS232Settings_dict['RS232_ON_OFF']
                # Flip the value
                self.valueObj.RS232Settings_dict['RS232_ON_OFF'] = 'OFF' if current == 'ON' else 'ON'
                # Update the pixmap and other widgets
                update_rs232_toggle(self)
                return True  # Event handled
            
            if obj == self.toggleButton_networkBasedDatabase and event.type() == event.MouseButtonPress:
                current = self.valueObj.NetworkedDatabaseSettings_dict['NETWORKE_BASED_DATABASE_ON_OFF']
                self.valueObj.NetworkedDatabaseSettings_dict['NETWORKE_BASED_DATABASE_ON_OFF'] = 'OFF' if current == 'ON' else 'ON'
                update_networkdatabase_toggle(self)

            if obj == self.toggleButton_aoc and event.type() == event.MouseButtonPress:
                current = self.valueObj.AOCSettings_dict['AOC_ON_OFF']
                # Flip the value
                self.valueObj.AOCSettings_dict['AOC_ON_OFF'] = 'OFF' if current == 'ON' else 'ON'
                # Update the pixmap and other widgets
                update_autooffcet_toggle(self)
                return True  # Event handled
            
            if obj == self.toggleButton_buzzer and event.type() == event.MouseButtonPress:
                current = self.valueObj.IOSettings_dict.get('BUZZER', {}).get('Enable', '0')
                # Flip the value
                self.valueObj.IOSettings_dict['BUZZER']['Enable'] = '0' if current == '1' else '1'
                # Update the pixmap and other widgets
                update_IOSetting_Buzzer_toggle(self)
                return True  # Event handled

            if obj == self.toggelButton_relay and event.type() == event.MouseButtonPress:
                current = self.valueObj.IOSettings_dict.get('RELAY', {}).get('Enable', '0')
                # Flip the value
                self.valueObj.IOSettings_dict['RELAY']['Enable'] = '0' if current == '1' else '1'
                # Update the pixmap and other widgets
                update_IOSetting_Relay_toggle(self)
                return True  # Event handled
            
            if obj == self.toggelButton_cycleStopTimer and event.type() == event.MouseButtonPress:
                current = self.valueObj.IOSettings_dict.get('CYCLE_STOP_TIMER', {}).get('Enable', '0')
                # Flip the value
                self.valueObj.IOSettings_dict['CYCLE_STOP_TIMER']['Enable'] = '0' if current == '1' else '1'
                # Update the pixmap and other widgets
                update_IOSetting_CycleStopTimer_toggle(self)
                return True  # Event handled
            
            if obj == self.toggelButton_autoSaveReading and event.type() == event.MouseButtonPress:
                current = self.valueObj.IOSettings_dict.get('AUTO_SAVE_READING', {}).get('Enable', '0')
                # Flip the value
                self.valueObj.IOSettings_dict['AUTO_SAVE_READING']['Enable'] = '0' if current == '1' else '1'
                # Update the pixmap and other widgets
                update_IOSetting_AutosaveReading_toggle(self)
                return True  # Event handled

            if obj == self.toggelButton_partTraceability and event.type() == event.MouseButtonPress:
                current = self.valueObj.IOSettings_dict.get('PART_TRACEABILITY', {}).get('Enable', '0')
                # Flip the value
                self.valueObj.IOSettings_dict['PART_TRACEABILITY']['Enable'] = '0' if current == '1' else '1'
                # Update the pixmap and other widgets
                update_IOSetting_PartTraceability_toggle(self)
                return True  # Event handled
 
            
            if obj == self.toggleButtontimeToSetMaster and event.type() == event.MouseButtonPress:
                current = self.valueObj.IOSettings_dict.get('TIME_TO_MASTER_SET', {}).get('Enable', '0')
                # Flip the value
                self.valueObj.IOSettings_dict['TIME_TO_MASTER_SET']['Enable'] = '0' if current == '1' else '1'
                # Update the pixmap and other widgets
                update_IOSetting_TimetoMasterSet_toggle(self)
                return True  # Event handled

            if obj == self.toggleButton_masterGrouping and event.type() == event.MouseButtonPress:
                current = self.valueObj.IOSettings_dict.get('MASTER_GROUPING', {}).get('Enable', '0')
                # Flip the value
                self.valueObj.IOSettings_dict['MASTER_GROUPING']['Enable'] = '0' if current == '1' else '1'
                # Update the pixmap and other widgets
                update_IOSetting_MasterGrouping_toggle(self)
                return True  # Event handled
            
            if isinstance(obj, QtWidgets.QLineEdit) and event.type() == QtCore.QEvent.MouseButtonPress:
                if not obj.isEnabled():  # ✅ skip if disabled
                    return True  # block keyboard/numpad
                
                if getattr(self, "keyboard_open", False):  # already open
                    return True
                self.keyboard_open = True

                if obj in self.letter_lineedits:
                    keyboard = Keyboard(parent=self)
                    keyboard.textEntered.connect(lambda text, line=obj: self.apply_keyboard_text(line, text, keyboard))
                    keyboard.show()
                    return True  # block normal focus behavior (prevents cursor)
                
                elif obj in self.numeric_lineedits:
                    # numkeyboard = numpad_window(target_lineedit=obj)
                    # numkeyboard.finished.connect(lambda _: setattr(self, "keyboard_open", False))
                    # numkeyboard.show_numpad()
                    # return True  # block normal focus behavior (prevents cursor)
                    if not hasattr(self, "numkeyboard") or self.numkeyboard is None:
                        self.numkeyboard = numpad_window(parent=self)
                        # Connect the numpadClosed signal to reset keyboard_open flag
                        self.numkeyboard.numpadClosed.connect(self.on_numpad_closed)

                    # 🔑 ALWAYS update target
                    self.numkeyboard.target_lineedit = obj
                    

                    # 🔑 SHOW again
                    self.numkeyboard.show()
                    self.raise_()
                    self.numkeyboard.activateWindow()
                    

                    return True   # ✅ VERY IMPORTANT

                    # self.numkeyboard = numpad_window(target_lineedit=obj)
                    # self.numkeyboard.finished.connect(lambda _: setattr(self, "keyboard_open", False))
                    # self.numkeyboard.show()
                    # return True  # block normal focus behavior (prevents cursor)
        except Exception as e:
            print(f"Error in eventFilter: {e}")
        
        return super().eventFilter(obj, event)

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

    def load_data_to_ui(self):
        # All load functions call here for better use
        #self.load_AngleCalculationSettings_to_ui()
        self.load_IOSettings_to_ui()
        self.load_IPSettings_to_ui()
        self.load_NetworkedDatabaseSettings_to_ui()
        self.load_ProgramSettings_to_ui()
        self.load_RS232Settings_to_ui()
        self.load_WifiSettings_to_ui()
        #self.load_Higher_lower_value_to_ui()
     
            
    # Load AngleCalculationSettings Dict To Ui
    # Loads AngleCalculationSettings dictionary values into UI fields
    def load_AngleCalculationSettings_to_ui(self):
    
        try:
            default_programId = self.valueObj.activeVariables_dict.get('ActiveProgramId', 1)
            # Load dict if not already loaded
            if not hasattr(self.valueObj, 'AngleCalculationSettings_dict') or not self.valueObj.AngleCalculationSettings_dict:
                self.valueObj.AngleCalculationSettings_dict = self.databaseObj.load_data_to_AngleCalculationSettings_dict(str(default_programId))

            data = self.valueObj.AngleCalculationSettings_dict
            #print("angle_calculation database :",data)
            # Helper to safely convert values to string for QLineEdit
            def to_str(value, default=""):
                if value is None:
                    return default
                return str(value)  
            
            #print("loaded angle db settings :",data)
            
            # Load values into UI (always show last saved data)
            self.lineEdit_angleDegree.setText(to_str(data.get("MASTER_ANGLE_DEGREES")))
            self.lineEdit_angleMinutes.setText(to_str(data.get("MASTER_ANGLE_MINUTES")))
            self.lineEdit_angleSeconds.setText(to_str(data.get("MASTER_ANGLE_SECONDS")))
            self.lineEdit_toleranceMin.setText(to_str(data.get("PLUS_TOLERANCE_MINUTES")))
            self.lineEdit_toleranceSec.setText(to_str(data.get("PLUS_TOLERANCE_SECONDS")))
            self.lineEdit_negativeTolMin.setText(to_str(data.get("MINUS_TOLERANCE_MINUTES")))
            self.lineEdit_negativeTolSec.setText(to_str(data.get("MINUS_TOLERANCE_SECONDS")))
            self.lineEdit_distanceMm.setText(to_str(data.get("DISTANCE")))

            if data.get("ANGLETYPE") == 'Half Angle':
                self.radioButton_halfAngle.setChecked(True)
                self.radioButton_2_fullAngle.setChecked(False)
            elif data.get("ANGLETYPE") == 'Full Angle':
                self.radioButton_2_fullAngle.setChecked(True)
                self.radioButton_halfAngle.setChecked(False)

            # After loading values, update toggle state (handles enabling/disabling)
            update_angle_toggle(self)

        except Exception as e:
            print(f"Error loading AngleCalculationSettings to UI: {e}")

    # Load IOSettings Dict To Ui
    # Loads IOSettings dictionary values into UI fields and toggles
    def load_IOSettings_to_ui(self):
        try:
            # Ensure the dictionary is loaded before trying to access it
            if not hasattr(self.valueObj, 'IOSettings_dict') or not self.valueObj.IOSettings_dict:
                self.valueObj.IOSettings_dict = self.databaseObj.load_data_to_IOSettings_dict()

            # Use .get() with default values to prevent KeyError if a key is missing
            io_dict = self.valueObj.IOSettings_dict
            #print("IO_Setting loading", io_dict)

            if io_dict.get("AUTO_SAVE_READING", {}).get("Enable") == '0':
                self.toggelButton_autoSaveReading.setPixmap(QPixmap("Switcher_OFF.png"))
            elif io_dict.get("AUTO_SAVE_READING", {}).get("Enable") == '1':
                self.toggelButton_autoSaveReading.setPixmap(QPixmap("Switcher_On.png"))

            if io_dict.get("BUZZER", {}).get("Enable") == '0':
                self.toggleButton_buzzer.setPixmap(QPixmap("Switcher_OFF.png"))
            elif io_dict.get("BUZZER", {}).get("Enable") == '1':
                self.toggleButton_buzzer.setPixmap(QPixmap("Switcher_On.png"))

            if io_dict.get("CYCLE_STOP_TIMER", {}).get("Enable") == '0':
                self.toggelButton_cycleStopTimer.setPixmap(QPixmap("Switcher_OFF.png"))
            elif io_dict.get("CYCLE_STOP_TIMER", {}).get("Enable") == '1':
                self.toggelButton_cycleStopTimer.setPixmap(QPixmap("Switcher_On.png"))

            if io_dict.get("MASTER_GROUPING", {}).get("Enable") == '0':
                self.toggleButton_masterGrouping.setPixmap(QPixmap("Switcher_OFF.png"))
            elif io_dict.get("MASTER_GROUPING", {}).get("Enable") == '1':
                self.toggleButton_masterGrouping.setPixmap(QPixmap("Switcher_On.png"))

            if io_dict.get("PART_TRACEABILITY", {}).get("Enable") == '0':
                self.toggelButton_partTraceability.setPixmap(QPixmap("Switcher_OFF.png"))
            elif io_dict.get("PART_TRACEABILITY", {}).get("Enable") == '1':
                self.toggelButton_partTraceability.setPixmap(QPixmap("Switcher_On.png"))

            if io_dict.get("RELAY", {}).get("Enable") == '0':
                self.toggelButton_relay.setPixmap(QPixmap("Switcher_OFF.png"))
            elif io_dict.get("RELAY", {}).get("Enable") == '1':
                self.toggelButton_relay.setPixmap(QPixmap("Switcher_On.png"))

            if io_dict.get("TIME_TO_MASTER_SET", {}).get("Enable") == '0':
                self.toggleButtontimeToSetMaster.setPixmap(QPixmap("Switcher_OFF.png"))
            elif io_dict.get("TIME_TO_MASTER_SET", {}).get("Enable") == '1':
                self.toggleButtontimeToSetMaster.setPixmap(QPixmap("Switcher_On.png"))

            if io_dict.get("BUZZER", {}).get("Value") == 'Ok':
                self.radioButton_okBuzzer.setChecked(True)
                self.radioButton_reworkNotokBuzzer.setChecked(False)
            elif io_dict.get("BUZZER", {}).get("Value") == 'Rework / Not Ok':
                self.radioButton_reworkNotokBuzzer.setChecked(True)
                self.radioButton_okBuzzer.setChecked(False)
            
            self.lineEdit_relayTime.setText(io_dict.get("RELAY", {}).get("Value", ""))
            self.lineEdit_cycleTime.setText(io_dict.get("CYCLE_STOP_TIMER", {}).get("Value", ""))

            if io_dict.get("PART_TRACEABILITY", {}).get("Value") == 'Manual Reset':
                self.radioButton_manualPartTraceability.setChecked(True)
                self.radioButton_autoPartTraceability.setChecked(False)
            elif io_dict.get("PART_TRACEABILITY", {}).get("Value") == 'Auto Reset':
                self.radioButton_autoPartTraceability.setChecked(True)
                self.radioButton_manualPartTraceability.setChecked(False)

            self.lineEdit_timeToMasterSet.setText(io_dict.get("TIME_TO_MASTER_SET", {}).get("Value", ""))
            self.comboBox_displayMode.setCurrentText(io_dict.get("DISPLAY_MODE", {}).get("Value", "Digit")) # Set display mode
            update_IOSetting_Buzzer_toggle(self)
            update_IOSetting_Relay_toggle(self)
            update_IOSetting_CycleStopTimer_toggle(self)
            update_IOSetting_AutosaveReading_toggle(self)
            update_IOSetting_PartTraceability_toggle(self)
            update_IOSetting_TimetoMasterSet_toggle(self)
            update_IOSetting_MasterGrouping_toggle(self)
            
        except Exception as e:
            print(f"Error loading IOSettings to UI: {e}")
    
    # Load IPSettings Dict To Ui
    # Loads IPSettings dictionary values into UI fields
    def load_IPSettings_to_ui(self):
        try:
            # Ensure the dictionary is loaded before trying to access it
            if not hasattr(self.valueObj, 'IPSettings_dict') or not self.valueObj.IPSettings_dict:
                self.valueObj.IPSettings_dict = self.databaseObj.load_data_to_IPSettings_dict()
            
            # ip_dict = self.valueObj.IPSettings_dict
            #print("Ip_Setting loading.....", ip_dict)

            self.lineEdit_selfIp.setText(self.valueObj.IPSettings_dict.get("SelfIPAddress", ""))
            self.lineEdit_subnetMask.setText(self.valueObj.IPSettings_dict.get("SubnetMask", ""))
            self.lineEdit_defaultGateway.setText(self.valueObj.IPSettings_dict.get("DefaultGateway", ""))
            
        except Exception as e:
            print(f"Error loading IPSettings to UI: {e}")

    # Load NetworkedDatabaseSettings Dict To Ui
    # Loads networked database settings dictionary values into UI fields
    def load_NetworkedDatabaseSettings_to_ui(self):
        try:
            # Ensure dict exists
            if not hasattr(self.valueObj, 'NetworkedDatabaseSettings_dict') or not self.valueObj.NetworkedDatabaseSettings_dict:
                self.valueObj.NetworkedDatabaseSettings_dict = self.databaseObj.load_data_to_NetworkedDatabaseSettings_dict()

            db_dict = self.valueObj.NetworkedDatabaseSettings_dict
            
            #print("Loaded Network DB settings:", db_dict)
            # Always set lineEdit values first
            self.lineEdit_driverNameDb.setText(db_dict.get("MS_SQL_DRIVER_NAME", ""))
            self.lineEdit_serverNameDb.setText(db_dict.get("MS_SQL_SERVER_NAME", ""))
            self.lineEdit_databaseNameDb.setText(db_dict.get("MS_SQL_DATABASE_NAME", ""))
            self.lineEdit_usernameDb.setText(db_dict.get("MS_SQL_USERNAME", ""))
            self.lineEdit_passwordDb.setText(db_dict.get("MS_SQL_PASSWORD", ""))

            # Then apply toggle state (this makes lineEdits enabled/disabled + opacity)
            update_networkdatabase_toggle(self)

        except Exception as e:
            print(f"Error loading NetworkedDatabaseSettings to UI: {e}")

    def load_ProbeBasedSettings_to_ui(self, dimension):
        try:
            # 1️⃣ ALWAYS RESET UI FIRST (VERY IMPORTANT)
            self.label_formulaBar.setText("")
            self.comboBox_masterType.setCurrentText("")

            self.lineEdit_masterLower.setText("")
            self.lineEdit_master.setText("")
            self.lineEdit_masterHigher.setText("")

            self.lineEdit_upperOffcetLimit.setText("")
            self.lineEdit_usl.setText("")
            self.lineEdit_ucl.setText("")
            self.lineEdit_nominalValue.setText("")
            self.lineEdit_lcl.setText("")
            self.lineEdit_lsl.setText("")
            self.lineEdit_lowerOffsetLimit.setText("")

            self.comboBox_ovalityOnOff.setCurrentText("")
            self.comboBox_rangeProbe.setCurrentText("")
            self.comboBox_methodProbe.setCurrentText("")
            self.comboBox_caseProbe.setCurrentText("")

            self.lineEdit_caseT.setText("")
            self.lineEdit_probeSensitivity.setText("")
            self.lineEdit_airSensitivityQuotient.setText("")

            # self.comboBox_ovalityOnOff.blockSignals(True)
            # self.comboBox_masterType.blockSignals(True)
            # 2️⃣ ENSURE DICT IS LOADED
            if not hasattr(self.valueObj, 'ProgramSettings_dict') or not self.valueObj.ProgramSettings_dict:
                self.valueObj.ProgramSettings_dict = self.databaseObj.load_data_to_ProgramSettings_dict(
                    int(self.valueObj.activeVariables_dict["ActiveProgramId"])
                )

            # 3️⃣ GET DIMENSION DATA
            dim_data = self.valueObj.ProgramSettings_dict.get(dimension)
            if not dim_data:
                return  # UI already cleared

            # 4️⃣ LOAD DATA (ONLY IF EXISTS)
            probe_settings = dim_data.get("ProbeBasedSettings", {})
            print("MasterType:",str(probe_settings.get("MasterType", "")))

            self.label_formulaBar.setText(str(probe_settings.get("Formula", "")))
            self.comboBox_masterType.setCurrentText(str(probe_settings.get("MasterType", "")))


            self.lineEdit_masterLower.setText(str(probe_settings.get("MasterLower", "")))
            self.lineEdit_master.setText(str(probe_settings.get("Master", "")))
            self.lineEdit_masterHigher.setText(str(probe_settings.get("MasterHigher", "")))

            self.lineEdit_upperOffcetLimit.setText(str(probe_settings.get("UpperOffsetLimit", "")))
            self.lineEdit_usl.setText(str(probe_settings.get("UpperSpecificationLimit", "")))
            self.lineEdit_ucl.setText(str(probe_settings.get("UpperControlLimit", "")))
            self.lineEdit_nominalValue.setText(str(probe_settings.get("NominalValue", "")))
            self.lineEdit_lcl.setText(str(probe_settings.get("LowerControlLimit", "")))
            self.lineEdit_lsl.setText(str(probe_settings.get("LowerSpecificationLimit", "")))
            self.lineEdit_lowerOffsetLimit.setText(str(probe_settings.get("LowerOffsetLimit", "")))

            self.comboBox_ovalityOnOff.setCurrentText(str(probe_settings.get("Ovality", "")))
            self.comboBox_rangeProbe.setCurrentText(str(probe_settings.get("Range", "")))
            self.comboBox_methodProbe.setCurrentText(str(probe_settings.get("Method", "")))
            self.comboBox_caseProbe.setCurrentText(str(probe_settings.get("Case", "")))

            self.lineEdit_caseT.setText(str(probe_settings.get("CaseT", "")))
            self.lineEdit_probeSensitivity.setText(str(probe_settings.get("ProbeSensitivity", "")))
            self.lineEdit_airSensitivityQuotient.setText(str(probe_settings.get("AirSensitivityQuotient", "")))

            # 🔥 FORCE final state
            self.apply_ProbeBasedSettings_state()
            self.apply_masterType_state()


        except Exception as e:
            print(f"Error loading ProbeBasedSettings for {dimension}: {e}")

    # Load AOCBasedSettings Dict To Ui
    def load_AOCBasedSettings_to_ui(self,dimension):
        try:
            self.comboBox_axis.setCurrentText(" ")
            self.lineEdit_offsetNo.setText(" ")

            self.comboBox_machine.setCurrentText(" ")
            self.comboBox_direction.setCurrentText(" ")

            self.lineEdit_turretNo.setText(" ")
            self.lineEdit_bufferPartNo.setText(" ")
            
            # Ensure ProgramSettings_dict is loaded
            if not hasattr(self.valueObj, 'ProgramSettings_dict') or not self.valueObj.ProgramSettings_dict:
                print("Warning: ProgramSettings_dict not loaded. Attempting to load default.")
                #self.valueObj.ProgramSettings_dict = self.databaseObj.load_data_to_ProgramSettings_dict(1) # Assuming program_id 1 as default
                self.valueObj.ProgramSettings_dict = \
                    self.databaseObj.load_data_to_ProgramSettings_dict(
                    int(self.valueObj.activeVariables_dict["ActiveProgramId"])
                    )
            # Check if the dimension exists in the dictionary
            dim_data = self.valueObj.ProgramSettings_dict.get(dimension)
            if not dim_data:
                print(f"{dimension} not found in ProgramSettings_dict")
                return

            aoc_settings = dim_data.get("AOCBasedSettings", {})

            self.comboBox_axis.setCurrentText(str(aoc_settings.get("Axis", "")))
            self.lineEdit_offsetNo.setText(str(aoc_settings.get("OffsetNo", " ")))

            self.comboBox_machine.setCurrentText(str(aoc_settings.get("Machine", "")))
            self.comboBox_direction.setCurrentText(str(aoc_settings.get("Direction", "")))

            self.lineEdit_turretNo.setText(str(aoc_settings.get("TurretNo", " ")))
            self.lineEdit_bufferPartNo.setText(str(aoc_settings.get("BufferPartNo", " ")))
            
        except Exception as e:
            print(f"Error loading AOCBasedSettings to UI for dimension {dimension}: {e}")

    # Load ProgramSettings Dict To Ui
    def load_ProgramSettings_to_ui(self):
        try:
            #print(self.valueObj.ProgramSettings_dict,'nanana')
            # Ensure ProgramSettings_dict is loaded. This method should ideally take a program_id.
            # For now, it uses the hardcoded example from value.py or attempts to load program_id 1.
            if not hasattr(self.valueObj, 'ProgramSettings_dict') or not self.valueObj.ProgramSettings_dict:
                print("Warning: ProgramSettings_dict not loaded. Attempting to load default.")
                self.valueObj.ProgramSettings_dict = self.databaseObj.load_data_to_ProgramSettings_dict(1) # Assuming program_id 1 as default

            program_specific_settings = self.valueObj.ProgramSettings_dict.get('ProgramSpecificSettings', {})

            self.lineEdit_programNameSettings.setText(str(program_specific_settings.get("ProgramName", "")))
            self.label_programName.setText(str(program_specific_settings.get("ProgramName", "")))
        
            if program_specific_settings.get("Mode") == 'Combine':
                self.radioButton_modeCombine.setChecked(True)
                self.radioButton_modeIndividual.setChecked(False)
            elif program_specific_settings.get("Mode") == 'Individual':
                self.radioButton_modeIndividual.setChecked(True)
                self.radioButton_modeCombine.setChecked(False)        

            if program_specific_settings.get("Uom") == 'inch':
                self.radioButton_inch.setChecked(True)
                self.radioButton_mm.setChecked(False)
            elif program_specific_settings.get("Uom") == 'mm':
                self.radioButton_mm.setChecked(True)
                self.radioButton_inch.setChecked(False)

            self.lineEdit_DurationAutosave.setText(str(program_specific_settings.get("AutoSave_Duration", "0.0")))

            # Get all existing dimension keys (those starting with 'D')
            existing_dims = [key for key in self.valueObj.ProgramSettings_dict.keys() if key.startswith('D')]

            # Sort them numerically (D1, D2, ...)
            existing_dims.sort(key=lambda x: int(x[1:]))

            # Determine next dimension to add (limit D8)
            if existing_dims:
                last_idx = int(existing_dims[-1][1:])
            else:
                last_idx = 0

            # Build the list for combo box entries, up to D8
            combo_entries = [f"D{i}" for i in range(1, min(last_idx + 2, 9))]

            self.comboBox_toselectProbe.clear()      # Clear previous items
            self.comboBox_toselectProbe.addItems(combo_entries)
        except Exception as e:
            print(f"Error loading ProgramSettings to UI: {e}")


    # Load RS232Settings Dict To Ui
    # Loads RS232 settings dictionary values into UI fields
    def load_RS232Settings_to_ui(self):
        try:
            # Ensure the dictionary is loaded before trying to access it
            if not hasattr(self.valueObj, 'RS232Settings_dict') or not self.valueObj.RS232Settings_dict:
                self.valueObj.RS232Settings_dict = self.databaseObj.load_data_to_RS232Settings_dict()

            rs232_dict = self.valueObj.RS232Settings_dict
            #print("loading rs232_dict is : ",rs232_dict)

            if rs232_dict.get("RS232_ON_OFF") == 'OFF':
                self.toggleButton_rs232.setPixmap(QPixmap("Switcher_OFF.png"))
            elif rs232_dict.get("RS232_ON_OFF") == 'ON':
                self.toggleButton_rs232.setPixmap(QPixmap("Switcher_On.png"))

            self.comboBox_baudRate.setCurrentText(rs232_dict.get("BAUD_RATE", ""))
            self.comboBox_dataBits.setCurrentText(rs232_dict.get("DATA_BITS", ""))
            self.comboBox_parity.setCurrentText(rs232_dict.get("PARITY", ""))
            self.comboBox_stopBits.setCurrentText(rs232_dict.get("STOP_BITS", ""))
            self.comboBox_flowControl.setCurrentText(rs232_dict.get("FLOW_CONTROL", ""))
            self.lineEdit_portName.setText(rs232_dict.get("PORT_NAME", "")) # Corrected from comboBox_baudRate.setText
            update_rs232_toggle(self)
        except Exception as e:
            print(f"Error loading RS232Settings to UI: {e}")

    # Load WifiSettings Dict To Ui
    # Loads Wifi settings dictionary values into UI fields
    def load_WifiSettings_to_ui(self):
        try:
            # Ensure the dictionary is loaded before trying to access it
            if not hasattr(self.valueObj, 'WifiSettings_dict') or not self.valueObj.WifiSettings_dict:
                self.valueObj.WifiSettings_dict = self.databaseObj.load_data_to_WifiSettings_dict()
            
            # wifi_dict = self.valueObj.WifiSettings_dict
            #print("wifi setting loading: ....",wifi_dict)

            self.lineEdit_wifiSsid.setText(self.valueObj.WifiSettings_dict.get("WifiSSID", ""))
            self.lineEdit_wifiPassword.setText(self.valueObj.WifiSettings_dict.get("WifiPassword", ""))
        except Exception as e:
            print(f"Error loading WifiSettings to UI: {e}")


    # Destructor called when MainWindow is destroyed, stops movies
    def __del__(self,event):
        """Destructor to clean up movies"""
        try:
            if self.spi.trigger_line:
                self.spi.trigger_line.release()
            self.spi.close()
            self.worker_thread.quit()
            self.worker_thread.wait()
            event.accept()
            # for movie in self.movies:
            #     if movie is not None:
            #         movie.stop()
            print("MainWindow destroyed, movies stopped.")
        except Exception as e:
            print(f"Error during MainWindow destruction: {e}")
            



if __name__ == "__main__":
    try:
        
        app = QApplication(sys.argv)

        window = MainWindow()#(gif_labels)
        window.showFullScreen()
        sys.exit(app.exec_())
    except Exception as e:
        print(f"Error starting application: {e}")
        sys.exit(1)

