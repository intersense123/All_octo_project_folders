# datahandler.py
from PySide2.QtWidgets import QApplication, QMainWindow, QStackedWidget , QWidget
from PySide2.QtWidgets import QFrame
from PySide2.QtWidgets import QLineEdit
from PySide2 import QtCore, QtWidgets
from PySide2.QtCore import QTimer, QTime, QDate , QObject , QThread , Signal, Qt, QCoreApplication
from PySide2.QtGui import QPixmap
from sqlalchemy.orm import *

import sys
# import the generated UI class
from messageBox import CustomMessageBox
from active_ui_togglebutton_handler import *
from models import *

from sqlalchemy.orm import Session , sessionmaker
from serial_handler import SerialHandler
from models import SessionLocal, ProbeBasedSettings, AOCBasedSettings
from PySide2.QtGui import QStandardItemModel, QStandardItem


class DataHandler(QObject):
    """
    Handles:
    - Database read/write
    - Program settings
    - Probe / AOC / IO / Network configs
    """
    dialVisibilityChanged = Signal()
    io_settings_saved = Signal()
    probe_setttings_saved = Signal()
    Rs232_settings_saved = Signal()
    dimension_deleted = Signal()
    def __init__(self, main_window,uiHandler):
        try:
            
            super().__init__()
            self.ui = main_window
            self.uiHandler = uiHandler
            self.load_databases()
            self.ui.button_addUpdateLogin.clicked.connect(self.save_toDatabase_userManagement)
            self.ui.button_spcDataCount.clicked.connect(self.save_toDatabase_aocSettings)
            self.ui.button_addLoginDetails.clicked.connect(self.handle_addUser_clicked)
            self.ui.button_modifyLogin.clicked.connect(self.handle_UserModify_clicked)
    
            # -------- cached data --------
            # self.raw_values = {
            #     "D1": [],
            #     "D2": [],
            #     "D3": [],
            #     "D4": [],
            # }
            self.master_rows = {
                    "D1": [
                        self.ui.label_liveD1Val,
                        self.ui.label_masterD1_1,      # M.L D1 title
                        self.ui.label_masterD1_2,      # M.H D1 title
                        self.ui.label_valMasterD1_1,   # value low
                        self.ui.label_valMasterD1_2,# value high
                        self.ui.line_10,
                        self.ui.line_84,
                        
                    ],
                    "D2": [
                        self.ui.label_liveD2Val,
                        self.ui.label_masterD2_1,
                        self.ui.label_masterD2_2,
                        self.ui.label_valMasterD2_1,
                        self.ui.label_valMasterD2_2,
                        self.ui.line_11,
                        self.ui.line_85,
                        
                    ],
                    "D3": [
                        self.ui.label_liveD3Val,
                        self.ui.label_masterD3_1,
                        self.ui.label_masterD3_2,
                        self.ui.label_valMasterD3_1,
                        self.ui.label_valMasterD3_2,
                        self.ui.line_12,
                        self.ui.line_86,
                    ],
                    "D4": [
                        self.ui.label_liveD4val,
                        self.ui.label_masterD4_1,
                        self.ui.label_masterD4_2,
                        self.ui.label_valMasterD4_1,
                        self.ui.label_valMasterD4_2,
                        self.ui.line_87,
                    ],
                }
            self.master_value_labels = {
                    "D1": {
                        "high": self.ui.label_valMasterD1_2,
                        "low":  self.ui.label_valMasterD1_1,
                    },
                    "D2": {
                        "high": self.ui.label_valMasterD2_2,
                        "low":  self.ui.label_valMasterD2_1,
                    },
                    "D3": {
                        "high": self.ui.label_valMasterD3_2,
                        "low":  self.ui.label_valMasterD3_1,
                    },
                    "D4": {
                        "high": self.ui.label_valMasterD4_2,
                        "low":  self.ui.label_valMasterD4_1,
                    },
                }
            self.selected_user_id = None
            self.is_modify_mode = False
            self.setup_program_table()
            self.load_data_to_ui()
            self.update_ui_after_programSettings_saved()
            self.Rs232_settings_saved.connect(self.regenerate_rs232_instance)
            self.probe_setttings_saved.connect(self.update_ui_after_programSettings_saved)    
        except Exception as e:
            print(f"Error in initilization of Data Handler {e}")
    
    #update ui after programsetting saved (help fun for refresh ui)    
    def update_ui_after_programSettings_saved(self):
        try:
            current_dim = self.ui.comboBox_toselectProbe.currentText()
            # program_id = int(
            #     self.ui.comboBox_programIdSetting_Inner.currentText()
            # )

            # self.ui.valueObj.activeVariables_dict["ActiveProgramId"] = program_id
            self.ui.valueObj.ProgramSettings_dict = \
                self.ui.databaseObj.load_data_to_ProgramSettings_dict(
                                                                 int(self.ui.valueObj.activeVariables_dict.get("ActiveProgramId", "1"))
                )
            self.update_dimension_combobox(keep_dimension=current_dim)
            self.load_program_table()
            self.load_Higher_lower_value_to_ui(int(self.ui.valueObj.activeVariables_dict.get("ActiveProgramId", "1")))
            # QTimer.singleShot(100, lambda: self.ui.spc_manager.load_program_OnSpc(int(self.ui.valueObj.activeVariables_dict.get("ActiveProgramId", "1"))))
            # self.ui.spc_manager.load_program_OnSpc(int(self.ui.valueObj.activeVariables_dict.get("ActiveProgramId", "1")))
            # self.ui.spc_manager.load_previous_spc_values()
            self.dialVisibilityChanged.emit()
        except Exception as e:
            print(f"Error in update_ui_after_programming {e}")
            
    # -------- LOAD --------
    def load_databases(self):
        try:
            self.ui.valueObj.WifiSettings_dict = self.ui.databaseObj.load_data_to_WifiSettings_dict()
        except Exception as e:
            print(f"Error loading WifiSettings: {e}")
            self.ui.valueObj.WifiSettings_dict = {}  # set default

        try:
            default_programId = self.ui.valueObj.activeVariables_dict.get('ActiveProgramId', 1)
            #print("default Program Id..............................................",default_programId)
            self.ui.valueObj.AngleCalculationSettings_dict = self.ui.databaseObj.load_data_to_AngleCalculationSettings_dict(str(default_programId))
        except Exception as e:
            print(f"Error loading AngleCalculationSettings: {e}")
            self.ui.valueObj.AngleCalculationSettings_dict = {}

        try:
            self.ui.valueObj.AOCSettings_dict = self.ui.databaseObj.load_data_to_AOCSettings_dict()
        except Exception as e:
            print(f"Error loading AOCSettings: {e}")
            self.ui.valueObj.AOCSettings_dict = {}

        try:
            self.ui.valueObj.IOSettings_dict = self.ui.databaseObj.load_data_to_IOSettings_dict()
        except Exception as e:
            print(f"Error loading IOSettings: {e}")
            self.ui.valueObj.IOSettings_dict = {}

        try:
            self.ui.valueObj.IPSettings_dict = self.ui.databaseObj.load_data_to_IPSettings_dict()
        except Exception as e:
            print(f"Error loading IPSettings: {e}")
            self.ui.valueObj.IPSettings_dict = {}

        try:
            self.ui.valueObj.NetworkedDatabaseSettings_dict = self.ui.databaseObj.load_data_to_NetworkedDatabaseSettings_dict()
        except Exception as e:
            print(f"Error loading NetworkedDatabaseSettings: {e}")
            self.ui.valueObj.NetworkedDatabaseSettings_dict = {}

        try:
            self.ui.valueObj.RS232Settings_dict = self.ui.databaseObj.load_data_to_RS232Settings_dict()
        except Exception as e:
            print(f"Error loading RS232Settings: {e}")
            self.ui.valueObj.RS232Settings_dict = {}

        try:
            default_programId = self.ui.valueObj.activeVariables_dict.get('ActiveProgramId', 1)
            self.ui.valueObj.ProgramSettings_dict = self.ui.databaseObj.load_data_to_ProgramSettings_dict(int(default_programId))
        except Exception as e:
            print(f"Error loading ProgramSettings: {e}")
            self.ui.valueObj.ProgramSettings_dict = {}

    #load data to ui
    def load_data_to_ui(self):
        try:
            self.load_IOSettings_to_ui()
            self.load_IPSettings_to_ui()
            self.load_NetworkedDatabaseSettings_to_ui()
            self.load_ProgramSettings_to_ui()
            self.load_RS232Settings_to_ui()
            self.load_WifiSettings_to_ui()
        except Exception as e:
            print(f"Error on load data to ui {e}")
    
    #load programsetting to ui      
    def load_ProgramSettings_to_ui(self):
        try:
            #print(self.ui.valueObj.ProgramSettings_dict,'nanana')
            # Ensure ProgramSettings_dict is loaded. This method should ideally take a program_id.
            # For now, it uses the hardcoded example from value.py or attempts to load program_id 1.
            if not hasattr(self.ui.valueObj, 'ProgramSettings_dict') or not self.ui.valueObj.ProgramSettings_dict:
                # print("Warning: ProgramSettings_dict not loaded. Attempting to load default.")
                self.ui.valueObj.ProgramSettings_dict = self.ui.databaseObj.load_data_to_ProgramSettings_dict(1) # Assuming program_id 1 as default

            program_specific_settings = self.ui.valueObj.ProgramSettings_dict.get('ProgramSpecificSettings', {})

            self.ui.lineEdit_programNameSettings.setText(str(program_specific_settings.get("ProgramName", "")))
            self.ui.label_programName.setText(str(program_specific_settings.get("ProgramName", "")))
        
            if program_specific_settings.get("Mode") == 'Combine':
                self.ui.radioButton_modeCombine.setChecked(True)
                self.ui.radioButton_modeIndividual.setChecked(False)
            elif program_specific_settings.get("Mode") == 'Individual':
                self.ui.radioButton_modeIndividual.setChecked(True)
                self.ui.radioButton_modeCombine.setChecked(False)        

            if program_specific_settings.get("Uom") == 'inch':
                self.ui.radioButton_inch.setChecked(True)
                self.ui.radioButton_mm.setChecked(False)
            elif program_specific_settings.get("Uom") == 'mm':
                self.ui.radioButton_mm.setChecked(True)
                self.ui.radioButton_inch.setChecked(False)

            self.ui.lineEdit_DurationAutosave.setText(str(program_specific_settings.get("AutoSave_Duration", "0.0")))
            self.ui.lineEdit_Responsiveness.setText(str(program_specific_settings.get("Responsiveness", "0")))
            # Get all existing dimension keys (those starting with 'D')
            existing_dims = [key for key in self.ui.valueObj.ProgramSettings_dict.keys() if key.startswith('D')]

            # Sort them numerically (D1, D2, ...)
            existing_dims.sort(key=lambda x: int(x[1:]))

            # Determine next dimension to add (limit D8)
            if existing_dims:
                last_idx = int(existing_dims[-1][1:])
            else:
                last_idx = 0

            # Build the list for combo box entries, up to D8
            combo_entries = [f"D{i}" for i in range(1, min(last_idx + 2, 9))]

            self.ui.comboBox_toselectProbe.clear()      # Clear previous items
            self.ui.comboBox_toselectProbe.addItems(combo_entries)
        except Exception as e:
            print(f"Error loading ProgramSettings to UI: {e}")

    #load probeBasedSettings to ui
    def load_ProbeBasedSettings_to_ui(self,dimension):
        try:
            
            # 1️⃣ ALWAYS RESET UI FIRST (VERY IMPORTANT)
            self.ui.label_formulaBar.setText("")
            self.ui.comboBox_masterType.setCurrentText("")

            self.ui.lineEdit_masterLower.setText("")
            self.ui.lineEdit_master.setText("")
            self.ui.lineEdit_masterHigher.setText("")

            # self.ui.lineEdit_upperOffcetLimit.setText("")
            self.ui.lineEdit_usl.setText("")
            self.ui.lineEdit_ucl.setText("")
            self.ui.lineEdit_nominalValue.setText("")
            self.ui.lineEdit_lcl.setText("")
            self.ui.lineEdit_lsl.setText("")
            # self.ui.lineEdit_lowerOffsetLimit.setText("")

            self.ui.comboBox_ovalityOnOff.setCurrentText("")
            self.ui.comboBox_rangeProbe.setCurrentText("")
            self.ui.comboBox_methodProbe.setCurrentText("")
            self.ui.comboBox_caseProbe.setCurrentText("")

            self.ui.lineEdit_caseT.setText("")
            self.ui.lineEdit_probeSensitivity.setText("")
            self.ui.lineEdit_airSensitivityQuotient.setText("")

            # self.comboBox_ovalityOnOff.blockSignals(True)
            # self.comboBox_masterType.blockSignals(True)
            # 2️⃣ ENSURE DICT IS LOADED
            if not hasattr(self.ui.valueObj, 'ProgramSettings_dict') or not self.ui.valueObj.ProgramSettings_dict:
                self.ui.valueObj.ProgramSettings_dict = self.ui.databaseObj.load_data_to_ProgramSettings_dict(
                    int(self.ui.valueObj.activeVariables_dict.get("ActiveProgramId", "1"))
                )

            # 3️⃣ GET DIMENSION DATA
            dim_data = self.ui.valueObj.ProgramSettings_dict.get(dimension)
            if not dim_data:
                return  # UI already cleared

            # 4️⃣ LOAD DATA (ONLY IF EXISTS)
            probe_settings = dim_data.get("ProbeBasedSettings", {})
            # print("MasterType:",str(probe_settings.get("MasterType", "")))
            self.ui.lineEdit_programNameSettings.setText(str(probe_settings.get("ProgramName", "")))
            self.ui.label_programName.setText(str(probe_settings.get("ProgramName", "")))
            self.ui.label_formulaBar.setText(str(probe_settings.get("Formula", "")))
            self.ui.comboBox_masterType.setCurrentText(str(probe_settings.get("MasterType", "")))


            self.ui.lineEdit_masterLower.setText(str(probe_settings.get("MasterLower", "")))
            self.ui.lineEdit_master.setText(str(probe_settings.get("Master", "")))
            self.ui.lineEdit_masterHigher.setText(str(probe_settings.get("MasterHigher", "")))

            # self.ui.lineEdit_upperOffcetLimit.setText(str(probe_settings.get("UpperOffsetLimit", "")))
            self.ui.lineEdit_usl.setText(str(probe_settings.get("UpperSpecificationLimit", "")))
            self.ui.lineEdit_ucl.setText(str(probe_settings.get("UpperControlLimit", "")))
            self.ui.lineEdit_nominalValue.setText(str(probe_settings.get("NominalValue", "")))
            self.ui.lineEdit_lcl.setText(str(probe_settings.get("LowerControlLimit", "")))
            self.ui.lineEdit_lsl.setText(str(probe_settings.get("LowerSpecificationLimit", "")))
            # self.ui.lineEdit_lowerOffsetLimit.setText(str(probe_settings.get("LowerOffsetLimit", "")))

            self.ui.comboBox_ovalityOnOff.setCurrentText(str(probe_settings.get("Ovality", "")))
            self.ui.comboBox_rangeProbe.setCurrentText(str(probe_settings.get("Range", "")))
            self.ui.comboBox_methodProbe.setCurrentText(str(probe_settings.get("Method", "")))
            self.ui.comboBox_caseProbe.setCurrentText(str(probe_settings.get("Case", "")))

            self.ui.lineEdit_caseT.setText(str(probe_settings.get("CaseT", "")))
            self.ui.lineEdit_leastCount.setCurrentText(str(probe_settings.get("LeastCount", "")))
            self.ui.lineEdit_probeSensitivity.setText(str(probe_settings.get("ProbeSensitivity", "")))
            self.ui.lineEdit_airSensitivityQuotient.setText(str(probe_settings.get("AirSensitivityQuotient", "")))

            # 🔥 FORCE final state
            self.uiHandler.apply_ProbeBasedSettings_state()
            self.uiHandler.apply_masterType_state()


        except Exception as e:
            print(f"Error loading ProbeBasedSettings for {dimension}: {e}")

    #load AocBasedSettings to ui
    def load_AOCBasedSettings_to_ui(self,dimension):
        try:
            self.ui.comboBox_axis.setCurrentText(" ")
            self.ui.lineEdit_offsetNo.setText(" ")
            
            self.ui.lineEdit_upperOffcetLimit.setText("")
            self.ui.lineEdit_lowerOffsetLimit.setText("")

            self.ui.comboBox_machine.setCurrentText(" ")
            self.ui.comboBox_direction.setCurrentText(" ")

            self.ui.lineEdit_turretNo.setText(" ")
            self.ui.lineEdit_bufferPartNo.setText(" ")
            
            # Ensure ProgramSettings_dict is loaded
            if not hasattr(self.ui.valueObj, 'ProgramSettings_dict') or not self.ui.valueObj.ProgramSettings_dict:
                # print("Warning: ProgramSettings_dict not loaded. Attempting to load default.")
                #self.ui.valueObj.ProgramSettings_dict = self.ui.databaseObj.load_data_to_ProgramSettings_dict(1) # Assuming program_id 1 as default
                self.ui.valueObj.ProgramSettings_dict = \
                    self.ui.databaseObj.load_data_to_ProgramSettings_dict(
                    int(self.ui.valueObj.activeVariables_dict.get("ActiveProgramId", "1"))
                    )
            # Check if the dimension exists in the dictionary
            dim_data = self.ui.valueObj.ProgramSettings_dict.get(dimension)
            if not dim_data:
                # print(f"{dimension} not found in ProgramSettings_dict")
                return

            aoc_settings = dim_data.get("AOCBasedSettings", {})

            self.ui.comboBox_axis.setCurrentText(str(aoc_settings.get("Axis", "")))
            self.ui.lineEdit_offsetNo.setText(str(aoc_settings.get("OffsetNo", " ")))
            self.ui.lineEdit_upperOffcetLimit.setText(str(aoc_settings.get("UpperOffsetLimit", "")))
            self.ui.lineEdit_lowerOffsetLimit.setText(str(aoc_settings.get("LowerOffsetLimit", "")))

            self.ui.comboBox_machine.setCurrentText(str(aoc_settings.get("Machine", "")))
            self.ui.comboBox_direction.setCurrentText(str(aoc_settings.get("Direction", "")))

            self.ui.lineEdit_turretNo.setText(str(aoc_settings.get("TurretNo", " ")))
            self.ui.lineEdit_bufferPartNo.setText(str(aoc_settings.get("BufferPartNo", " ")))
            
        except Exception as e:
            print(f"Error loading AOCBasedSettings to UI for dimension {dimension}: {e}")

    #load iosettings to ui
    def load_IOSettings_to_ui(self):
        try:
            # Ensure the dictionary is loaded before trying to access it
            if not hasattr(self.ui.valueObj, 'IOSettings_dict') or not self.ui.valueObj.IOSettings_dict:
                self.ui.valueObj.IOSettings_dict = self.ui.databaseObj.load_data_to_IOSettings_dict()

            # Use .get() with default values to prevent KeyError if a key is missing
            io_dict = self.ui.valueObj.IOSettings_dict
            #print("IO_Setting loading", io_dict)

            if io_dict.get("AUTO_SAVE_READING", {}).get("Enable") == '0':
                self.ui.toggelButton_autoSaveReading.setPixmap(QPixmap("Switcher_OFF.png"))
            elif io_dict.get("AUTO_SAVE_READING", {}).get("Enable") == '1':
                self.ui.toggelButton_autoSaveReading.setPixmap(QPixmap("toggle_on.png"))

            if io_dict.get("BUZZER", {}).get("Enable") == '0':
                self.ui.toggleButton_buzzer.setPixmap(QPixmap("Switcher_OFF.png"))
            elif io_dict.get("BUZZER", {}).get("Enable") == '1':
                self.ui.toggleButton_buzzer.setPixmap(QPixmap("toggle_on.png"))

            if io_dict.get("CYCLE_STOP_TIMER", {}).get("Enable") == '0':
                self.ui.toggelButton_cycleStopTimer.setPixmap(QPixmap("Switcher_OFF.png"))
            elif io_dict.get("CYCLE_STOP_TIMER", {}).get("Enable") == '1':
                self.ui.toggelButton_cycleStopTimer.setPixmap(QPixmap("toggle_on.png"))

            if io_dict.get("MASTER_GROUPING", {}).get("Enable") == '0':
                self.ui.toggleButton_masterGrouping.setPixmap(QPixmap("Switcher_OFF.png"))
            elif io_dict.get("MASTER_GROUPING", {}).get("Enable") == '1':
                self.ui.toggleButton_masterGrouping.setPixmap(QPixmap("toggle_on.png"))

            if io_dict.get("PART_TRACEABILITY", {}).get("Enable") == '0':
                self.ui.toggelButton_partTraceability.setPixmap(QPixmap("Switcher_OFF.png"))
            elif io_dict.get("PART_TRACEABILITY", {}).get("Enable") == '1':
                self.ui.toggelButton_partTraceability.setPixmap(QPixmap("toggle_on.png"))

            if io_dict.get("RELAY", {}).get("Enable") == '0':
                self.ui.toggelButton_relay.setPixmap(QPixmap("Switcher_OFF.png"))
            elif io_dict.get("RELAY", {}).get("Enable") == '1':
                self.ui.toggelButton_relay.setPixmap(QPixmap("toggle_on.png"))

            if io_dict.get("TIME_TO_MASTER_SET", {}).get("Enable") == '0':
                self.ui.toggleButtontimeToSetMaster.setPixmap(QPixmap("Switcher_OFF.png"))
            elif io_dict.get("TIME_TO_MASTER_SET", {}).get("Enable") == '1':
                self.ui.toggleButtontimeToSetMaster.setPixmap(QPixmap("toggle_on.png"))

            if io_dict.get("BUZZER", {}).get("Value") == 'Ok':
                self.ui.radioButton_okBuzzer.setChecked(True)
                self.ui.radioButton_reworkNotokBuzzer.setChecked(False)
            elif io_dict.get("BUZZER", {}).get("Value") == 'Rework / Not Ok':
                self.ui.radioButton_reworkNotokBuzzer.setChecked(True)
                self.ui.radioButton_okBuzzer.setChecked(False)
            
            self.ui.lineEdit_relayTime.setText(io_dict.get("RELAY", {}).get("Value", ""))
            self.ui.lineEdit_cycleTime.setText(io_dict.get("CYCLE_STOP_TIMER", {}).get("Value", ""))

            if io_dict.get("PART_TRACEABILITY", {}).get("Value") == 'Manual Reset':
                self.ui.radioButton_manualPartTraceability.setChecked(True)
                self.ui.radioButton_autoPartTraceability.setChecked(False)
            elif io_dict.get("PART_TRACEABILITY", {}).get("Value") == 'Auto Reset':
                self.ui.radioButton_autoPartTraceability.setChecked(True)
                self.ui.radioButton_manualPartTraceability.setChecked(False)

            self.ui.lineEdit_timeToMasterSet.setText(io_dict.get("TIME_TO_MASTER_SET", {}).get("Value", ""))
            QTimer.singleShot(0, lambda: [
                update_IOSetting_Buzzer_toggle(self.ui),
                update_IOSetting_Relay_toggle(self.ui),
                update_IOSetting_CycleStopTimer_toggle(self.ui),
                update_IOSetting_AutosaveReading_toggle(self.ui),
                update_IOSetting_PartTraceability_toggle(self.ui),
                update_IOSetting_TimetoMasterSet_toggle(self.ui),
                update_IOSetting_MasterGrouping_toggle(self.ui),
            ])
            
        except Exception as e:
            print(f"Error loading IOSettings to UI: {e}")

    #load ipsettings to ui
    def load_IPSettings_to_ui(self):
        try:
            # Ensure the dictionary is loaded before trying to access it
            if not hasattr(self.ui.valueObj, 'IPSettings_dict') or not self.ui.valueObj.IPSettings_dict:
                self.ui.valueObj.IPSettings_dict = self.ui.databaseObj.load_data_to_IPSettings_dict()
            
            # ip_dict = self.ui.valueObj.IPSettings_dict
            #print("Ip_Setting loading.....", ip_dict)

            self.ui.lineEdit_selfIp.setText(self.ui.valueObj.IPSettings_dict.get("SelfIPAddress", ""))
            self.ui.lineEdit_subnetMask.setText(self.ui.valueObj.IPSettings_dict.get("SubnetMask", ""))
            self.ui.lineEdit_defaultGateway.setText(self.ui.valueObj.IPSettings_dict.get("DefaultGateway", ""))
            
        except Exception as e:
            print(f"Error loading IPSettings to UI: {e}")

    
    #load wifisettings to ui
    def load_WifiSettings_to_ui(self):
        try:
            # Ensure the dictionary is loaded before trying to access it
            if not hasattr(self.ui.valueObj, 'WifiSettings_dict') or not self.ui.valueObj.WifiSettings_dict:
                self.ui.valueObj.WifiSettings_dict = self.ui.databaseObj.load_data_to_WifiSettings_dict()
            
            # wifi_dict = self.ui.valueObj.WifiSettings_dict
            #print("wifi setting loading: ....",wifi_dict)

            self.ui.lineEdit_wifiSsid.setText(self.ui.valueObj.WifiSettings_dict.get("WifiSSID", ""))
            self.ui.lineEdit_wifiPassword.setText(self.ui.valueObj.WifiSettings_dict.get("WifiPassword", ""))
        except Exception as e:
            print(f"Error loading WifiSettings to UI: {e}")
    
    #load rs232settings to ui
    def load_RS232Settings_to_ui(self):
        try:
            # Ensure the dictionary is loaded before trying to access it
            if not hasattr(self.ui.valueObj, 'RS232Settings_dict') or not self.ui.valueObj.RS232Settings_dict:
                self.ui.valueObj.RS232Settings_dict = self.ui.databaseObj.load_data_to_RS232Settings_dict()

            rs232_dict = self.ui.valueObj.RS232Settings_dict
            #print("loading rs232_dict is : ",rs232_dict)

            if rs232_dict.get("RS232_ON_OFF") == 'OFF':
                self.ui.toggleButton_rs232.setPixmap(QPixmap("Switcher_OFF.png"))
            elif rs232_dict.get("RS232_ON_OFF") == 'ON':
                self.ui.toggleButton_rs232.setPixmap(QPixmap("toggle_on.png"))

            self.ui.comboBox_baudRate.setCurrentText(rs232_dict.get("BAUD_RATE", ""))
            self.ui.comboBox_dataBits.setCurrentText(rs232_dict.get("DATA_BITS", ""))
            self.ui.comboBox_parity.setCurrentText(rs232_dict.get("PARITY", ""))
            self.ui.comboBox_stopBits.setCurrentText(rs232_dict.get("STOP_BITS", ""))
            self.ui.comboBox_flowControl.setCurrentText(rs232_dict.get("FLOW_CONTROL", ""))
            self.ui.lineEdit_portName.setText(rs232_dict.get("PORT_NAME", "")) # Corrected from comboBox_baudRate.setText
            update_rs232_toggle(self.ui)
        except Exception as e:
            print(f"Error loading RS232Settings to UI: {e}")

    #load networkedDatabaseSettings to ui
    def load_NetworkedDatabaseSettings_to_ui(self):
        try:
            # Ensure dict exists
            if not hasattr(self.ui.valueObj, 'NetworkedDatabaseSettings_dict') or not self.ui.valueObj.NetworkedDatabaseSettings_dict:
                self.ui.valueObj.NetworkedDatabaseSettings_dict = self.ui.databaseObj.load_data_to_NetworkedDatabaseSettings_dict()

            db_dict = self.ui.valueObj.NetworkedDatabaseSettings_dict
            
            #print("Loaded Network DB settings:", db_dict)
            # Always set lineEdit values first
            self.ui.lineEdit_driverNameDb.setText(db_dict.get("MS_SQL_DRIVER_NAME", ""))
            self.ui.lineEdit_serverNameDb.setText(db_dict.get("MS_SQL_SERVER_NAME", ""))
            self.ui.lineEdit_databaseNameDb.setText(db_dict.get("MS_SQL_DATABASE_NAME", ""))
            self.ui.lineEdit_usernameDb.setText(db_dict.get("MS_SQL_USERNAME", ""))
            self.ui.lineEdit_passwordDb.setText(db_dict.get("MS_SQL_PASSWORD", ""))

            # Then apply toggle state (this makes lineEdits enabled/disabled + opacity)
            update_networkdatabase_toggle(self.ui)

        except Exception as e:
            print(f"Error loading NetworkedDatabaseSettings to UI: {e}")

    #load anglecalculationetting to ui
    def load_AngleCalculationSettings_to_ui(self):
        try:
            default_programId = self.ui.valueObj.activeVariables_dict.get('ActiveProgramId', 1)
            # Load dict if not already loaded
            if not hasattr(self.ui.valueObj, 'AngleCalculationSettings_dict') or not self.ui.valueObj.AngleCalculationSettings_dict:
                self.ui.valueObj.AngleCalculationSettings_dict = self.ui.databaseObj.load_data_to_AngleCalculationSettings_dict(str(default_programId))

            data = self.ui.valueObj.AngleCalculationSettings_dict
            #print("angle_calculation database :",data)
            # Helper to safely convert values to string for QLineEdit
            def to_str(value, default=""):
                if value is None:
                    return default
                return str(value)  
            
            #print("loaded angle db settings :",data)
            
            # Load values into UI (always show last saved data)
            self.ui.lineEdit_angleDegree.setText(to_str(data.get("MASTER_ANGLE_DEGREES")))
            self.ui.lineEdit_angleMinutes.setText(to_str(data.get("MASTER_ANGLE_MINUTES")))
            self.ui.lineEdit_angleSeconds.setText(to_str(data.get("MASTER_ANGLE_SECONDS")))
            self.ui.lineEdit_toleranceMin.setText(to_str(data.get("PLUS_TOLERANCE_MINUTES")))
            self.ui.lineEdit_toleranceSec.setText(to_str(data.get("PLUS_TOLERANCE_SECONDS")))
            self.ui.lineEdit_negativeTolMin.setText(to_str(data.get("MINUS_TOLERANCE_MINUTES")))
            self.ui.lineEdit_negativeTolSec.setText(to_str(data.get("MINUS_TOLERANCE_SECONDS")))
            self.ui.lineEdit_distanceMm.setText(to_str(data.get("DISTANCE")))

            if data.get("ANGLETYPE") == 'Half Angle':
                self.ui.radioButton_halfAngle.setChecked(True)
                self.ui.radioButton_2_fullAngle.setChecked(False)
            elif data.get("ANGLETYPE") == 'Full Angle':
                self.ui.radioButton_2_fullAngle.setChecked(True)
                self.ui.radioButton_halfAngle.setChecked(False)

            # After loading values, update toggle state (handles enabling/disabling)
            update_angle_toggle(self.ui)

        except Exception as e:
            print(f"Error loading AngleCalculationSettings to UI: {e}")


    # -------- SAVE --------
    def save_toDatabase_programSetting(self):
        try:
            default_programId = self.ui.valueObj.activeVariables_dict.get('ActiveProgramId', 1)
            # ensure comboBox has this program as text
            if self.ui.comboBox_programId.findText(str(default_programId)) == -1:
                self.ui.comboBox_programId.addItem(str(default_programId))

            # set it as the current selection
            self.ui.comboBox_programId.setCurrentText(str(default_programId))

            # now when you read, it will not be blank
            programId = int(self.ui.comboBox_programId.currentText())
            programName = self.ui.lineEdit_programNameSettings.text()
            durationForAutosave = float(self.ui.lineEdit_DurationAutosave.text())
            Responsiveness = int(self.ui.lineEdit_Responsiveness.text())

            mode = ""
            uom = ""
            if self.ui.radioButton_modeCombine.isChecked():
                mode = "Combine"
            elif self.ui.radioButton_modeIndividual.isChecked():
                mode = "Individual"
            else:
                raise ValueError("Program mode not selected.")

            if self.ui.radioButton_inch.isChecked():
                uom = "inch"
            elif self.ui.radioButton_mm.isChecked():
                uom = "mm"
            else:
                raise ValueError("Unit of measurement not selected.")

            self.ui.databaseObj.upsert_program_settings(programId,programName,mode,
                                                    uom,durationForAutosave,Responsiveness)
            
            # print("ProgramSetting settings saved successfully.")
            with SessionLocal() as session:
                try:

                    active_program = session.query(ActiveVariables).filter_by(
                        Key="ActiveProgramId"
                    ).first()

                    if active_program:
                        active_program.Value = str(programId)

                    session.commit()

                except Exception as e:
                    print(f"Error updating ActiveProgramId: {e}")
        
            msg = CustomMessageBox("Program settings saved successfully.", "success",
                                   parent=self.ui)
            msg.exec_()
            QTimer.singleShot(0, self.probe_setttings_saved.emit)
        except Exception as e:
            print(f"Error saving program settings: {e}")
            msg = CustomMessageBox("Failed to save program settings. Please check inputs and try again.", "error",
                                   parent=self.ui)
            
            msg.exec_()


    def save_toDatabase_probeBasedSettings(self):
        try:
            default_programId = self.ui.valueObj.activeVariables_dict.get('ActiveProgramId', 1)
            # ensure comboBox has this program as text
            if self.ui.comboBox_programId.findText(str(default_programId)) == -1:
                self.ui.comboBox_programId.addItem(str(default_programId))
            

            # set it as the current selection
            self.ui.comboBox_programId.setCurrentText(str(default_programId))

            # now when you read, it will not be blank
            programId = int(self.ui.comboBox_programId.currentText())
            programName = self.ui.lineEdit_programNameSettings.text()
            #programId = self.ui.valueObj.activeVariables_dict['ActiveProgramId']
            dimension = self.ui.comboBox_toselectProbe.currentText()
            formulaBar = self.ui.label_formulaBar.text()
            masterType = self.ui.comboBox_masterType.currentText()
            # uol = float(self.ui.lineEdit_upperOffcetLimit.text())
            usl = float(self.ui.lineEdit_usl.text())
            ucl = float(self.ui.lineEdit_ucl.text())
            nominal = float(self.ui.lineEdit_nominalValue.text())
            lcl = float(self.ui.lineEdit_lcl.text())
            lsl = float(self.ui.lineEdit_lsl.text())
            # lol = float(self.ui.lineEdit_lowerOffsetLimit.text())
            ovality = self.ui.comboBox_ovalityOnOff.currentText()
            range_val = float(self.ui.comboBox_rangeProbe.currentText())
            method = self.ui.comboBox_methodProbe.currentText()
            LeastCount = float(self.ui.lineEdit_leastCount.currentText())
            probe_sensitivity = int(self.ui.lineEdit_probeSensitivity.text())
            air_sensitivity_quotient = self.ui.lineEdit_airSensitivityQuotient.text()
            if(masterType == "Single Master"):
                masterLower = 0.0
                master = float(self.ui.lineEdit_master.text())
                masterHigher = 0.0
            elif(masterType == "Double Master"):
                masterLower = float(self.ui.lineEdit_masterLower.text())
                master = 0.0
                masterHigher = float(self.ui.lineEdit_masterHigher.text())
            else:
                masterLower = 0.0
                master = 0.0
                masterHigher = 0.0
                
            if(ovality == 'OFF'):
                case = None
                caseT = None
            else:
                case = self.ui.comboBox_caseProbe.currentText()
                caseT = float(self.ui.lineEdit_caseT.text())
            self.ui.databaseObj.upsert_probe_based_settings(
                program_id = programId,
                ProgramName = programName,
                dimension = dimension,
                formula = formulaBar ,
                master_type = masterType ,
                master_lower = masterLower ,
                master = master ,
                master_higher = masterHigher ,
                # upper_offset_limit = uol ,
                upper_specification_limit = usl ,
                upper_control_limit = ucl ,
                nominal_value = nominal ,
                lower_control_limit = lcl ,
                lower_specification_limit = lsl ,
                # lower_offset_limit = lol ,
                ovality = ovality ,
                range_val = range_val ,
                method = method ,
                case = case ,
                case_t = caseT ,
                LeastCount=LeastCount,
                probe_sensitivity = probe_sensitivity ,
                air_sensitivity_quotient = air_sensitivity_quotient
            )
            with SessionLocal() as session:
                try:

                    active_program = session.query(ActiveVariables).filter_by(
                        Key="ActiveProgramId"
                    ).first()

                    if active_program:
                        active_program.Value = str(programId)

                    session.commit()

                except Exception as e:
                    print(f"Error updating ActiveProgramId: {e}")
            msg = CustomMessageBox("Probe-based settings saved successfully.", "success",
                                   parent=self.ui)        
            msg.exec_()
            QTimer.singleShot(0, self.probe_setttings_saved.emit)
        
        except Exception as e:
            print(f"Error saving probe based settings: {e}")
            msg = CustomMessageBox("Failed to save probe based settings. Please check inputs and try again.", "error",
                                   parent=self.ui)
            msg.exec_()
    
    def save_toDatabase_aocBasedSettings(self):
        try:
            current = self.ui.valueObj.AOCSettings_dict['AOC_ON_OFF']
            print("current aoc status:",current)
            if(current == "OFF"):
                return
            default_programId = self.ui.valueObj.activeVariables_dict.get('ActiveProgramId', 1)
            # ensure comboBox has this program as text
            if self.ui.comboBox_programId.findText(str(default_programId)) == -1:
                self.ui.comboBox_programId.addItem(str(default_programId))

            # set it as the current selection
            self.ui.comboBox_programId.setCurrentText(str(default_programId))

            # now when you read, it will not be blank
            programId = int(self.ui.comboBox_programId.currentText())
            #programId = self.ui.valueObj.activeVariables_dict['ActiveProgramId']
            dimension = self.ui.comboBox_toselectProbe.currentText()
            axis = self.ui.comboBox_axis.currentText()
            offset = int(self.ui.lineEdit_offsetNo.text())
            uol = float(self.ui.lineEdit_upperOffcetLimit.text())
            lol = float(self.ui.lineEdit_lowerOffsetLimit.text())
            machine = self.ui.comboBox_machine.currentText()
            direction = self.ui.comboBox_direction.currentText()
            turretNo = int(self.ui.lineEdit_turretNo.text())
            bufferPartNo = int(self.ui.lineEdit_bufferPartNo.text())

            self.ui.databaseObj.upsert_aoc_based_settings(
                program_id = programId,
                dimension = dimension,
                axis = axis,
                offset_no = offset,
                upper_offset_limit = uol,
                lower_offset_limit = lol,
                machine = machine,
                direction = direction,
                turret_no = turretNo,
                buffer_part_no = bufferPartNo
            )
            #print("aocBased settings saved successfully.")
            msg = CustomMessageBox("AOC-based settings saved successfully.", "success",
                                   parent=self.ui)
            msg.exec_()
            QTimer.singleShot(0, self.probe_setttings_saved.emit)
        except Exception as e:
            print(f"Error saving AOC based settings: {e}")
            msg = CustomMessageBox("Failed to save AOC based settings. Please check inputs and try again.", "error",
                                   parent=self.ui)
            msg.exec_()


    def save_toDatabase_IOSettings(self):
        try:
            
            buzzer_enable = self.ui.valueObj.IOSettings_dict.get('BUZZER', {}).get('Enable', '0')
            relay_enable = self.ui.valueObj.IOSettings_dict.get('RELAY', {}).get('Enable', '0')
            cycleStopTimer_enable = self.ui.valueObj.IOSettings_dict.get('CYCLE_STOP_TIMER', {}).get('Enable', '0')
            autoSaveReading_enable = self.ui.valueObj.IOSettings_dict.get('AUTO_SAVE_READING', {}).get('Enable', '0')
            partTraceabilty_enable = self.ui.valueObj.IOSettings_dict.get('PART_TRACEABILITY', {}).get('Enable', '0')
            timetoMasterSet_enable = self.ui.valueObj.IOSettings_dict.get('TIME_TO_MASTER_SET', {}).get('Enable', '0')
            masterGrouping_enable = self.ui.valueObj.IOSettings_dict.get('MASTER_GROUPING', {}).get('Enable', '0')
            

            # Assuming these line edits hold the 'Value' part of the tuple
            relay_value = self.ui.lineEdit_relayTime.text()
            cycleStopTimer_value = self.ui.lineEdit_cycleTime.text()
            timetoMasterSet_value = self.ui.lineEdit_timeToMasterSet.text()

            # Determine buzzer value based on radio buttons
            buzzer_value = ""
            if self.ui.radioButton_okBuzzer.isChecked():
                buzzer_value = "Ok"
            elif self.ui.radioButton_reworkNotokBuzzer.isChecked():
                buzzer_value = "Rework / Not Ok"
            else:
                raise ValueError("Buzzer value not selected.")
            
            # Determine part traceability value based on radio buttons
            partTraceabilty_value = ""
            if self.ui.radioButton_manualPartTraceability.isChecked():
                partTraceabilty_value = "Manual Reset"
            elif self.ui.radioButton_autoPartTraceability.isChecked():
                partTraceabilty_value = "Auto Reset"
            else:
                raise ValueError("Part traceability value not selected.")

            self.ui.databaseObj.update_io_settings(
                (buzzer_enable, buzzer_value),
                (relay_enable, relay_value),
                (cycleStopTimer_enable, cycleStopTimer_value),
                (autoSaveReading_enable, None), # Assuming autoSaveReading doesn't have a specific value field
                (partTraceabilty_enable, partTraceabilty_value),
                (timetoMasterSet_enable, timetoMasterSet_value),
                (masterGrouping_enable, None) # Assuming masterGrouping doesn't have a specific value field
            )
            self.ui.valueObj.IOSettings_dict = self.ui.databaseObj.load_data_to_IOSettings_dict()
            self.ui.valueObj.activeVariables_dict["BUZZER"] = buzzer_enable
            self.ui.valueObj.activeVariables_dict["RELAY"] = relay_enable
            self.ui.valueObj.activeVariables_dict["CYCLE_STOP_TIMER"] = cycleStopTimer_enable
            self.ui.valueObj.activeVariables_dict["AUTO_SAVE_READING"] = autoSaveReading_enable
            self.ui.valueObj.activeVariables_dict["PART_TRACEABILITY"] = partTraceabilty_enable
            self.ui.valueObj.activeVariables_dict["TIME_TO_MASTER_SET"] = timetoMasterSet_enable
            self.ui.valueObj.activeVariables_dict["MASTER_GROUPING"] = masterGrouping_enable
            
            self.ui.dial_indicator.set_visibility()
            #print("Iosettings settings saved successfully.")
            msg = CustomMessageBox("I/O settings saved successfully.", "success",
                                   parent=self.ui)
            msg.exec_()
            self.io_settings_saved.emit()  # 🔔 emit AFTER save
        except Exception as e:
            print(f"Error saving IO settings: {e}")
            msg = CustomMessageBox("Failed to save IO settings. Please check inputs and try again.", "error",
                                   parent=self.ui)
            msg.exec_()


    def save_toDatabase_IpSettings(self):
        try:
            ip = self.ui.lineEdit_selfIp.text()
            subnetmask = self.ui.lineEdit_subnetMask.text()
            gateway = self.ui.lineEdit_defaultGateway.text()

            self.ui.databaseObj.upsert_ip_settings(ip,subnetmask,gateway)
            self.ui.valueObj.IPSettings_dict = self.ui.databaseObj.load_data_to_IPSettings_dict()
            self.utils.apply_static_ip(ip,subnetmask,gateway)
            #print("Ip Setting saved successfully.")
            msg = CustomMessageBox("IP settings saved successfully.", "success",
                                   parent=self.ui)
            msg.exec_()
        except Exception as e:
            print(f"Error saving IP settings: {e}")
            msg = CustomMessageBox("Failed to save IP settings. Please check inputs and try again.", "error",
                                   parent=self.ui)
            msg.exec_()

    def save_toDatabase_WifiSettings(self):
        try:
            ssid = self.ui.lineEdit_wifiSsid.text()
            password = self.ui.lineEdit_wifiPassword.text()

            # Call your database handler
            self.utils.Wifi_Settings(ssid,password) # connect to wifi
            self.ui.databaseObj.upsert_wifi_settings(ssid, password) #to share ui text on db
            self.ui.valueObj.WifiSettings_dict = self.ui.databaseObj.load_data_to_WifiSettings_dict()

            #print("WiFi settings saved successfully.")
            msg = CustomMessageBox("WiFi settings saved successfully.", "success",
                                   parent=self.ui)
            msg.exec_()
        except Exception as e:
            print(f"Error saving WiFi settings: {e}")
            msg = CustomMessageBox("Failed to save WiFi settings. Please check inputs and try again.", "error",
                                   parent=self.ui)
            msg.exec_()

    def save_toDatabase_rs232Settings(self):
        try:
            rs232OnOff = self.ui.valueObj.activeVariables_dict.get('RS232OnOff','OFF')
            baudrate = self.ui.comboBox_baudRate.currentText()
            dataBits = self.ui.comboBox_dataBits.currentText()
            parity = self.ui.comboBox_parity.currentText()
            stopBits = self.ui.comboBox_stopBits.currentText()
            flowControl = self.ui.comboBox_flowControl.currentText()
            portName = self.ui.lineEdit_portName.text()

            self.ui.databaseObj.update_rs232_settings(rs232OnOff,baudrate,dataBits,parity,stopBits,flowControl,portName)
            self.ui.valueObj.RS232Settings_dict = self.ui.databaseObj.load_data_to_RS232Settings_dict()
            
            # Also update activeVariables_dict for consistency
            self.ui.valueObj.activeVariables_dict["RS232OnOff"] = rs232OnOff
            
            #print("rs232 settings saved successfully.")
            msg = CustomMessageBox("RS232 settings saved successfully.", "success",
                                   parent=self.ui)
            msg.exec_()
            # QTimer.singleShot(0,self.Rs232_settings_saved.emit())
            self.Rs232_settings_saved.emit()
        except Exception as e:
            print(f"Error saving RS232 settings: {e}")
            msg = CustomMessageBox("Failed to save RS232 settings. Please check inputs and try again.", "error",
                                   parent=self.ui)
            msg.exec_()
            
        

    def save_toDatabase_networkedDatabase_settings(self):
        try:
                networkBasedDatabaseOnOFF = self.ui.valueObj.activeVariables_dict.get('NetworkedDatabaseSettingsOnOff','OFF')
                msSqlDriverName = self.ui.lineEdit_driverNameDb.text()
                msSqlServerName = self.ui.lineEdit_serverNameDb.text()
                msSqlDatabaseNme = self.ui.lineEdit_databaseNameDb.text()
                msSqlUserName = self.ui.lineEdit_usernameDb.text()
                msSqlPassword = self.ui.lineEdit_passwordDb.text()

                self.ui.databaseObj.update_networked_database_settings(networkBasedDatabaseOnOFF,msSqlDriverName,
                                                                    msSqlServerName,msSqlDatabaseNme,
                                                                    msSqlUserName,msSqlPassword)
                self.ui.valueObj.NetworkedDatabaseSettings_dict = self.ui.databaseObj.load_data_to_NetworkedDatabaseSettings_dict()
                
                self.ui.valueObj.activeVariables_dict["NetworkedDatabaseSettingsOnOff"] = networkBasedDatabaseOnOFF

                #print("networkdatabase settings saved successfully.")
                msg = CustomMessageBox("Networked database settings saved successfully.", "success",
                                       parent=self.ui)
                msg.exec_()
            
        except Exception as e:
            print(f"Error saving networked database settings: {e}")
            msg = CustomMessageBox("Failed to save networked database settings. Please check inputs and try again.", "error",
                                   parent=self.ui)
            msg.exec_()


    def save_toDatabase_angleCalculationSettings(self):
        try:
            default_programId = self.ui.valueObj.activeVariables_dict.get('ActiveProgramId', 1)
            # ensure comboBox has this program as text
            if self.ui.comboBox_programId.findText(str(default_programId)) == -1:
                self.ui.comboBox_programId.addItem(str(default_programId))

            # set it as the current selection
            self.ui.comboBox_programId.setCurrentText(str(default_programId))
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
            programId = safe_int(self.ui.comboBox_programId.currentText())
            #programId = self.ui.comboBox_programIdSetting_outer.currentText()
            angleCalculationOnOff = self.ui.valueObj.activeVariables_dict.get('AngleCalculationOnOff','OFF')
            angleDegree = safe_int(self.ui.lineEdit_angleDegree.text())
            angleMin = safe_int(self.ui.lineEdit_angleMinutes.text())
            angleSec = safe_int(self.ui.lineEdit_angleSeconds.text())
            tolaranceMin = safe_int(self.ui.lineEdit_toleranceMin.text())
            tolaranceSec = safe_int(self.ui.lineEdit_toleranceSec.text())
            negativeTolMin = safe_int(self.ui.lineEdit_negativeTolMin.text())
            negativeTolSec = safe_int(self.ui.lineEdit_negativeTolSec.text())
            distance = safe_float(self.ui.lineEdit_distanceMm.text())
            angleType = ""
            if self.ui.radioButton_2_fullAngle.isChecked():
                angleType = "Full Angle"  # or whatever string you store in DB
            elif self.ui.radioButton_halfAngle.isChecked():
                angleType = "Half Angle"
            else:
                raise ValueError("Angle type not selected.")

            self.ui.databaseObj.upsert_angle_calculation_settings(programId,angleCalculationOnOff,angleDegree,angleMin,
                                                                angleSec,tolaranceMin,tolaranceSec,
                                                                negativeTolMin,negativeTolSec,distance,angleType)
            # Reload latest DB values into dictionary
            self.ui.valueObj.AngleCalculationSettings_dict = self.ui.databaseObj.load_data_to_AngleCalculationSettings_dict(programId)
            
            self.ui.valueObj.activeVariables_dict["AngleCalculationOnOff"] = angleCalculationOnOff

            #print("angleCalculation settings saved successfully.")
            msg = CustomMessageBox("Angle calculation settings saved successfully.", "success",
                                   parent=self.ui)
            msg.exec_()
        except Exception as e:
            print(f"Error saving angle calculation settings: {e}")
            msg = CustomMessageBox("Failed to save angle calculation settings. Please check inputs and try again.", "error",
                                   parent=self.ui)
            msg.exec_()

    def save_toDatabase_cncList(self):
        try:
            cncName = self.ui.lineEdit_cncName.text()
            ipAddress = self.ui.lineEdit_cncIpAddress.text()
            portNumber = self.ui.lineEdit_cncPortNumber.text()
            cncSelection = self.ui.comboBox_cncSelectionType.currentText()
            controller = self.ui.comboBox_cncController.currentText()

            self.ui.databaseObj.upsert_cnc_list(cncName,ipAddress,portNumber,
                                            cncSelection,controller)
            #print("cncList settings saved successfully.")
            msg = CustomMessageBox("CNC list settings saved successfully.", "success",
                                   parent=self.ui)
            msg.exec_()
        except Exception as e:
            print(f"Error saving CNC list: {e}")
            msg = CustomMessageBox("Failed to save CNC list. Please check inputs and try again.", "error",
                                   parent=self.ui)
            msg.exec_()


    def save_toDatabase_aocSettings(self):
        try:
            aocOnOff = self.ui.valueObj.activeVariables_dict.get('AOCOnOff',"OFF")
            spcDataCount = self.ui.lineEdit_spcDataCount.text()
            self.ui.databaseObj.update_aoc_settings(aocOnOff,spcDataCount)
            self.ui.valueObj.activeVariables_dict["AOCOnOff"] = aocOnOff
            
            #print("aoc settings saved successfully.")
            msg = CustomMessageBox("AOC settings saved successfully.", "success",
                                   parent=self.ui)
            msg.exec_()
        except Exception as e:
            print(f"Error saving AOC settings: {e}")
            msg = CustomMessageBox("Failed to save AOC settings. Please check inputs and try again.", "error",
                                   parent=self.ui)
            msg.exec_()
            
    def handle_UserModify_clicked(self):
        try:
            table = self.ui.tableview_loginList
            index = table.currentIndex()

            if not index.isValid():
                msg = CustomMessageBox(
                    "Please select a row first to modify",
                    "warning",
                    parent=self.ui
                )
                msg.exec_()
                return

            row = index.row()
            model = table.model()

            user_id = int(model.index(row, 0).data())
            username = model.index(row, 1).data()
            password = model.index(row, 2).data()
            access = model.index(row, 3).data()

            # Store for update
            self.selected_user_id = user_id
            self.is_modify_mode = True

            # Load into fields
            self.ui.lineEdit_setUsernameLogin.setText(username)
            self.ui.lineEdit_setPasswordLogin.setText(password)
            self.ui.comboBox_setAccessCombo.setCurrentText(access)

            # Switch stacked page
            self.ui.stacked.setCurrentIndex(2)

        except Exception as e:
            print(f"Error in handle_UserModify_clicked: {e}")

    def handle_addUser_clicked(self):
        try:
            # Reset modify state
            self.selected_user_id = None
            self.is_modify_mode = False

            # Clear fields ONLY here
            self.ui.lineEdit_setUsernameLogin.clear()
            self.ui.lineEdit_setPasswordLogin.clear()
            self.ui.comboBox_setAccessCombo.setCurrentIndex(0)

            # Switch page
            self.ui.stacked.setCurrentIndex(2)
        except Exception as e:
            print("Error in handle addUser_clicked:", e)


    def save_toDatabase_userManagement(self):
       
        try:
            setUsername = self.ui.lineEdit_setUsernameLogin.text()
            setPassword = self.ui.lineEdit_setPasswordLogin.text()
            setAccessType = self.ui.comboBox_setAccessCombo.currentText()
            
            user_id = self.selected_user_id if self.is_modify_mode else None

            result = self.ui.databaseObj.upsert_user_management(
                user_id,
                setUsername,
                setPassword,
                setAccessType
            )

            if result == "added":
                msg_text = "User added successfully"

            elif result == "updated":
                msg_text = "User updated successfully"

            elif result == "duplicate":
                msg = CustomMessageBox("Username already exists!", "error", parent=self.ui)
                msg.exec_()
                return

            elif result == "not_found":
                msg = CustomMessageBox("User not found!", "error", parent=self.ui)
                msg.exec_()
                return

            else:
                msg = CustomMessageBox("Database error occurred", "error", parent=self.ui)
                msg.exec_()
                return

            self.ui.user_managementTable.load_users_to_table()

            self.selected_user_id = None
            self.is_modify_mode = False

            msg = CustomMessageBox(msg_text, "success", parent=self.ui)
            msg.exec_()
            

        except Exception as e:
            print(f"Error saving/updating user: {e}")
            msg = CustomMessageBox(
                    "Failed to save user",
                    "error",
                    parent=self.ui
                )
            msg.exec_()

    def save_toDatabase_shiftSettings(self):
        try:
            shift1 = (self.ui.lineEdit_shift1FromTime.text(),
                     self.ui.lineEdit_shift1ToTime.text())
            shift2 = (self.ui.lineEdit_shift2FromTime.text(),
                      self.ui.lineEdit_shift2ToTime.text())
            shift3 = (self.ui.lineEdit_shift3FromTime.text(),
                      self.ui.lineEdit_shift3ToTime.text())

            # Call DB function
            self.ui.databaseObj.upsert_shift_timings(shift1, shift2, shift3)
            #print("Shift settings saved")
            msg = CustomMessageBox("Shift settings saved successfully.", "success",
                                   parent=self.ui)
            msg.exec_()
        except Exception as e:
            print(f"Error saving shift settings: {e}")
            msg = CustomMessageBox("Failed to save shift settings. Please check inputs and try again.", "error",
                                   parent=self.ui)
            msg.exec_()

    # -------- HELPERS --------
    def clear_master_values_ui(self):
        try:
            for labels in self.master_value_labels.values():
                labels["high"].clear()
                labels["low"].clear()
        except Exception as e:
            print(f"Error in clear master value ui {e}")        
    
    # -------- UI STATE --------
    def Hide_rows(self):
        try:
            for row_labels in self.master_rows.values():
                for lbl in row_labels:
                    lbl.hide()
        except Exception as e:
            print(f"Error in hide_rows : {e}")
                        
    def load_Higher_lower_value_to_ui(self, program_id):
        try:
            # ✅ CLEAR OLD PROGRAM VALUES FIRST
            self.clear_master_values_ui()
            self.Hide_rows()
            with self.ui.databaseObj.SessionLocal() as session:
                probes = (
                    session.query(ProbeBasedSettings)
                    .filter(ProbeBasedSettings.ProgramId == program_id)
                    .all()
                )

                # print("Loaded probes from DB:", len(probes))

                for probe in probes:
                    dim = str(probe.Dimension).strip().upper()

                    if dim not in self.master_value_labels:
                        # print("⚠️ No label mapping for", dim)
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
        try:
            # 1️⃣ Collect saved dimensions from DB
            saved_dims = sorted(
                [
                    dim for dim in self.ui.valueObj.ProgramSettings_dict.keys()
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
        except Exception as e:
            print(f"Error in get dimension list for combobox {e}")
    
    def update_dimension_combobox(self, keep_dimension=None):
        try:
            dims = self.get_dimension_list_for_combobox()

            self.ui.comboBox_toselectProbe.blockSignals(True)
            self.ui.comboBox_toselectProbe.clear()
            self.ui.comboBox_toselectProbe.addItems(dims)

            if keep_dimension in dims:
                self.ui.comboBox_toselectProbe.setCurrentText(keep_dimension)
            else:
                self.ui.comboBox_toselectProbe.setCurrentIndex(0)

            self.ui.comboBox_toselectProbe.blockSignals(False)
        except Exception as e:
            print(f"Error in update dimension combobox {e}")
    
    def build_probe_unique_string(self, dimension, probe_settings):
        #To build Probe Unique String including dimension and probe_settings.
        try:
            ps = self.ui.valueObj.ProgramSettings_dict.get('ProgramSpecificSettings', {})

            values = [
                ps.get("ProgramId"),
                ps.get("ProgramName"),
                dimension,
                probe_settings.get("Formula"),
                probe_settings.get("UpperSpecificationLimit"),
                probe_settings.get("UpperControlLimit"),
                probe_settings.get("NominalValue"),
                probe_settings.get("LowerControlLimit"),
                probe_settings.get("LowerSpecificationLimit"),
                ps.get("Uom"),
                probe_settings.get("Ovality"),
                probe_settings.get("Method"),
                probe_settings.get("Case"),
                probe_settings.get("CaseT")
            ]

            return ",".join(map(str, values))
        except Exception as e:
            print(f"Error while building a unique probe string")
            
    def delete_dimension(self, program_id, dimension):
        try:
            with SessionLocal() as session:
                try:
                    # print(f"Deleting ProgramId={program_id}, Dimension={dimension}")

                    session.query(ProbeBasedSettings).filter_by(
                        ProgramId=program_id,
                        Dimension=dimension
                    ).delete()

                    session.query(AOCBasedSettings).filter_by(
                        ProgramId=program_id,
                        Dimension=dimension
                    ).delete()

                    session.commit()
                    self.dimension_deleted.emit()
                    
                    # current_dim = self.ui.comboBox_toselectProbe.currentText()
                    # self.ui.valueObj.ProgramSettings_dict = \
                    #     self.ui.databaseObj.load_data_to_ProgramSettings_dict(
                    #         program_id
                    #     )

                    # self.update_dimension_combobox(current_dim)

                    # # FORCE UI REFRESH
                    # if current_dim:
                    #     self.load_ProbeBasedSettings_to_ui(current_dim)
                    # else:
                    #     self.load_ProbeBasedSettings_to_ui("D1")
    
                except Exception as e:
                    session.rollback()
                    print(f"Error deleting dimension in DB: {e}")
                    

        except Exception as outer_error:
            print(f"Session creation failed: {outer_error}")
            
    def delete_program(self, program_id):
        """
        Deletes entire program and all its related data safely.
        """
        try:
            with SessionLocal() as session:
                try:
                    # 🔥 Delete all dimension-related data
                    session.query(ProbeBasedSettings).filter(
                        ProbeBasedSettings.ProgramId == program_id
                    ).delete(synchronize_session=False)

                    session.query(AOCBasedSettings).filter(
                        AOCBasedSettings.ProgramId == program_id
                    ).delete(synchronize_session=False)

                    # 🔥 Delete program-level settings
                    session.query(ProgramSettings).filter(
                        ProgramSettings.ProgramId == program_id
                    ).delete(synchronize_session=False)

                    # 🔥 Delete angle calculation settings (used in your code)
                    session.query(AngleCalculationSettings).filter(
                        AngleCalculationSettings.ProgramId == program_id
                    ).delete(synchronize_session=False)

                    session.commit()
                    print(f"[INFO] Program {program_id} deleted successfully")

                except Exception as e:
                    session.rollback()
                    print(f"[ERROR] delete_program failed: {e}")

        except Exception as outer_error:
            print(f"[ERROR] Session creation failed: {outer_error}")
        
    def save_probe_unique_settings(self):
        """
        Save probe unique settings to ProbeBasedIds table.
        Creates ProbeId if unique_string doesn't exist.
        """
        try:
            programId = int(self.ui.valueObj.activeVariables_dict.get("ActiveProgramId", "1"))
            
            # Reload latest settings
            self.ui.valueObj.ProgramSettings_dict = \
                self.ui.databaseObj.load_data_to_ProgramSettings_dict(programId)
            
            program_dict = self.ui.valueObj.ProgramSettings_dict

            dims = [
                key for key, val in program_dict.items()
                if key.startswith("D") and val.get("ProbeBasedSettings")
            ]

            for dim in dims:
                probe_settings = program_dict[dim]["ProbeBasedSettings"]
                unique_string = self.build_probe_unique_string(dim, probe_settings)
                
                # print(f"Processing dimension {dim}: unique_string='{unique_string[:50]}...'")

                # Get existing or create new ProbeId
                probe_id = self.ui.savedbObj.get_probe_id_by_settings(unique_string)
                if probe_id == 0:
                    # print(f"Creating new ProbeBasedIds for {dim}")
                    probe_id = self.ui.savedbObj.insert_probe_based_ids(unique_string)
                    # print(f"New ProbeId {probe_id} created for {dim}")
                else:
                    print(f"Found existing ProbeId {probe_id} for {dim}")
                
                # Update dict with ProbeId
                program_dict[dim]["ProbeBasedSettings"]["ProbeId"] = probe_id
            
            # print("✅ All probe unique settings processed successfully")
            
        except Exception as e:
            print(f"❌ Error saving probe unique settings: {e}")
            import traceback
            traceback.print_exc()
            
    def regenerate_rs232_instance(self):
            """Regenerate SerialHandler: Always close old if exists, then recreate based on DB if 'ON'."""
            # Close existing instance safely (calls __del__ or manual close)
            if self.ui.serial_instance is not None:
                try:
                    self.ui.serial_instance.ser.close() if hasattr(self.ui.serial_instance, 'ser') and self.ui.serial_instance.ser.is_open else None
                except Exception:
                    pass
                del self.ui.serial_instance
            
            # Try to create new based on DB
            try:
                rs232_settings = self.ui.databaseObj.load_data_to_RS232Settings_dict()
                if rs232_settings.get('RS232_ON_OFF', 'OFF') == 'ON':
                    port = rs232_settings['PORT_NAME']
                    baud_rate = int(rs232_settings['BAUD_RATE'])
                    parity_map = {'None': 'N', 'Even': 'E', 'Odd': 'O'}
                    parity = parity_map.get(rs232_settings.get('PARITY', 'None'), 'N')
                    stopbits_map = {'One': 1, '1.5': 1.5, 'Two': 2}
                    stopbits = stopbits_map.get(rs232_settings.get('STOP_BITS', 'One'), 1)
                    data_bits = int(rs232_settings['DATA_BITS'])
                    self.ui.serial_instance = SerialHandler(port, baud_rate, parity, stopbits, data_bits)
                    # print(f"SerialHandler regenerated: {port} @ {baud_rate}")
                else:
                    self.ui.serial_instance = None
                    # print("RS232 disabled (RS232_ON_OFF=OFF)")
            except (KeyError, ValueError, RuntimeError) as e:
                self.ui.serial_instance = None
                # print(f"Failed to regenerate SerialHandler: {e}")
            except Exception as e:
                self.ui.serial_instance = None
                print(f"Unexpected error regenerating SerialHandler: {e}")
                
    def get_program_list(self):
        with SessionLocal() as session:
            try:
                # 1️⃣ Fetch both tables
                program_data = session.query(
                    ProgramSettings.ProgramId,
                    ProgramSettings.ProgramName
                ).all()

                probe_data = session.query(
                    ProbeBasedSettings.ProgramId,
                    ProbeBasedSettings.ProgramName
                ).distinct().all()

                # 2️⃣ Use dict for merge
                program_dict = {}

                # ✅ Step A: Insert all ProgramSettings (base)
                for pid, pname in program_data:
                    program_dict[pid] = pname

                # ✅ Step B: Override OR Add from ProbeBasedSettings
                for pid, pname in probe_data:
                    if pname:  
                        # 🔥 If exists → overwrite
                        # 🔥 If not → add new
                        program_dict[pid] = pname

                # 3️⃣ Return sorted list (optional but good)
                return sorted(program_dict.items(), key=lambda x: x[0])

            except Exception as e:
                print("Error fetching program list:", e)
                return []

    def setup_program_table(self):
        """
        Configure table view with columns
        """
        try:         
            table = self.ui.ProgramList_TableView   
            # Create and set model for table view
            self.model = QStandardItemModel()
            self.model.setHorizontalHeaderLabels(["Program ID", "Program Name"])
            table.setModel(self.model)
            table.verticalHeader().setStyleSheet(
                "QHeaderView::section { background-color: #2b2b2b; color: white; border: 1px solid #888888; }"
            )
            
            # Set column widths
            # Set vertical header width
            # table.verticalHeader().setWidth(90)
            table.setColumnWidth(0, 200)
            table.setColumnWidth(1, 560)
            # table.setColumnWidth(3, 230)
            table.setStyleSheet(u"QTableView::item { border: 2px solid #888888; }\n"
"QHeaderView::section { border: 2px solid #888888; }")
            
            # Disable column resizing
            table.horizontalHeader().setStretchLastSection(False)
            table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Fixed)
            # Set row height
            table.verticalHeader().setDefaultSectionSize(55)
            table.verticalHeader().setVisible(False)
            table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)  # already you have
            table.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)   # ❌ disable selection
            table.setFocusPolicy(QtCore.Qt.NoFocus)                           # ❌ no focus highlight
            # Set header font size and bold
            header_font = table.horizontalHeader().font()
            header_font.setPointSize(13)
            header_font.setBold(True)
            table.horizontalHeader().setFont(header_font)
            
            # Set header background color to grey and font color to white
            table.horizontalHeader().setStyleSheet(
                "QHeaderView::section { background-color: #2b2b2b; color: white; border: 1px solid #888888; min-height:50px; }"
            )
            
            # Set font size
            font = table.font()
            font.setPointSize(13)
            table.setFont(font)
            
            # print("Table setup completed")
        except Exception as e:
            print(f"Error setting up table: {e}")
                    
    
    def load_program_table(self):
        data = self.get_program_list()

        self.model.setRowCount(0)

        for pid, pname in data:
            id_item = QStandardItem(str(pid))
            name_item = QStandardItem(pname if pname else "")

            # ✅ Center align text
            id_item.setTextAlignment(Qt.AlignCenter)
            name_item.setTextAlignment(Qt.AlignCenter)

            self.model.appendRow([id_item, name_item])
