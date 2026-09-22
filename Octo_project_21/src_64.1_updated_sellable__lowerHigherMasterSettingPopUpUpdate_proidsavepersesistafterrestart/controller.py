# controller.py
from PySide2.QtWidgets import QApplication, QMainWindow, QStackedWidget , QWidget
from PySide2.QtWidgets import QFrame
from PySide2.QtWidgets import QLineEdit
from PySide2 import QtCore, QtWidgets
from PySide2.QtCore import QTimer, QTime, QDate , QObject , QThread , Signal, Qt, QCoreApplication
from PySide2.QtGui import QPixmap
from sqlalchemy.orm import *

import sys
# import the generated UI class
from factory_config import FactoryConfig
from messageBox import CustomMessageBox
from active_ui_togglebutton_handler import *
from models import *
import models
from PySide2.QtGui import QStandardItemModel, QStandardItem

class AppController(QObject):
    """
    Handles:
    - SPI
    - Master logic
    - OK / NOT OK
    - Program / Dimension flow
    - Orchestration between UI & Data
    """

    def __init__(self, main_window, data_handler):
        try:
            super().__init__()
            self.ui = main_window
            self.data = data_handler
            self.spi_controller = None  # Will be set later by MainWindow after SPIController init
            self.ui.comboBox_toselectProbe.clear()
            #dictionary to set buttons visibile while grouping on or off as per channels
            self.master_group_buttons_with_channel = {
                "D1": self.ui.masterGroupingChannel_1,
                "D2": self.ui.masterGroupingChannel_2,
                "D3": self.ui.masterGroupingChannel_3,
                "D4": self.ui.masterGroupingChannel_4,
            }
            self.D1_masterGrouping = False
            self.D2_masterGrouping = False
            self.D3_masterGrouping = False
            self.D4_masterGrouping = False
            
            self.init_progId_and_dimension()
            self.load_as_per_progId()
            self.update_delete_button_visibility()
            self.data.probe_setttings_saved.connect(self.update_delete_button_visibility)
            self.ui.button_save.clicked.connect(self.linkage_of_saveButton)
            self.ui.button_setDateTime.clicked.connect(self.handle_set_datetime)
            default_style = ("""
                QPushButton {
                    border: 1px solid #888;
                    border-radius: 4px;
                }
                """)
            self.ui.masterGroupingChannel_1.setStyleSheet(default_style)
            self.ui.masterGroupingChannel_1.clicked.connect(self.handle_grouping_buttons)
            self.ui.masterGroupingChannel_2.setStyleSheet(default_style)
            self.ui.masterGroupingChannel_2.clicked.connect(self.handle_grouping_buttons)
            self.ui.masterGroupingChannel_3.setStyleSheet(default_style)
            self.ui.masterGroupingChannel_3.clicked.connect(self.handle_grouping_buttons)
            self.ui.masterGroupingChannel_4.setStyleSheet(default_style)
            self.ui.masterGroupingChannel_4.clicked.connect(self.handle_grouping_buttons)
            self.ui.button_delete.clicked.connect(self.handle_delete_dimension)

            # self.ui.comboBox_programIdSetting_outer.currentTextChanged.connect(self.progId_changed_outer)
            # self.ui.comboBox_programIdSetting_outer_Inner.currentTextChanged.connect(self.progId_changed_inner)
            # self.ui.comboBox_toselectProbe.currentTextChanged.connect(lambda : self.load_as_per_dimension(self.ui.comboBox_toselectProbe.currentText()))
            self.ui.comboBox_toselectProbe.currentTextChanged.connect(self.toselectProbe_handler)
            self.ui.comboBox_programIdSetting_outer.currentTextChanged.connect(self.progId_changed_outer)
            self.ui.comboBox_programIdSetting_Inner.currentTextChanged.connect(self.progId_changed_inner)
            self.Handle_master_Grouping(self.safe_int(self.ui.valueObj.activeVariables_dict["ActiveProgramId"]))
            self.data.io_settings_saved.connect(lambda :self.Handle_master_Grouping(self.safe_int(self.ui.valueObj.activeVariables_dict["ActiveProgramId"])))
            # self.data.io_settings_saved.connect(
            #     lambda: (
            #         self.Handle_master_Grouping(
            #             int(self.ui.valueObj.activeVariables_dict["ActiveProgramId"])
            #         ),
            #         self.relay_handler()
            #     )
            # )
            self.data.dimension_deleted.connect(lambda :self.Handle_master_Grouping(self.safe_int(self.ui.valueObj.activeVariables_dict["ActiveProgramId"])))
            # self.data.io_settings_saved.connect()
            # if self.spi_controller:
            #     self.spi_controller.save_completed.connect(self.handle_save_signal)
        except Exception as e:
            print(f"Error in init of Appcontroller: {e}")
            

            
    def safe_int(self, value, default=1):
        try:
            return int(value)
        except (ValueError, TypeError):
            return default
    
    def toselectProbe_handler(self):
        self.update_delete_button_visibility()
        self.load_as_per_dimension(self.ui.comboBox_toselectProbe.currentText())
        
    def relay_handler(self):
        state = self.ui.valueObj.IOSettings_dict['RELAY']['Enable']
        print(f"relay state = {state}")
        relay_value = self.ui.valueObj.IOSettings_dict['RELAY']['Value']
        print(f"relay_value = {relay_value}")
        
    def handle_grouping_buttons(self):
        btn = self.sender()

        # If button already has selected border → reset
        if "FFFF8F" in btn.styleSheet() and self.ui.masterGroupingChannel_1:
            btn.setStyleSheet("""
                QPushButton {
                    border: 1px solid #888;
                    border-radius: 4px;
                }
                """)
        else:
            btn.setStyleSheet("""
                QPushButton {
                    border: 1px solid #FFFF8F;
                    border-radius: 4px;
                }
                """)
            
        self.D1_masterGrouping = "#ffff8f" in self.ui.masterGroupingChannel_1.styleSheet().lower()
        self.D2_masterGrouping = "#ffff8f" in self.ui.masterGroupingChannel_2.styleSheet().lower()
        self.D3_masterGrouping = "#ffff8f" in self.ui.masterGroupingChannel_3.styleSheet().lower()
        self.D4_masterGrouping = "#ffff8f" in self.ui.masterGroupingChannel_4.styleSheet().lower()
    
    def get_last_dimension(self):
        try:
            program_id = self.safe_int(self.ui.valueObj.activeVariables_dict.get("ActiveProgramId", 1))
            channels = self.get_channels_for_program(program_id)

            if not channels:
                return None

            return channels[-1]  # Last dimension (e.g. D2, D3)
        except Exception as e:
            print(f"Error getting last dimension: {e}")
            return None
    
    def update_delete_button_visibility(self):
        try:
            current_dim = self.ui.comboBox_toselectProbe.currentText()
            last_dim = self.get_last_dimension()

            if current_dim == last_dim and last_dim is not None:
                self.ui.button_delete.setEnabled(True)
                self.ui.button_delete.show()
            else:
                self.ui.button_delete.setEnabled(False)
                self.ui.button_delete.hide()

        except Exception as e:
            print(f"Error updating delete button visibility: {e}")

    def handle_delete_dimension(self):
        try:
            current_dim = self.ui.comboBox_toselectProbe.currentText()
            last_dim = self.get_last_dimension()

            if current_dim != last_dim:
                msg = CustomMessageBox(
                    "Only last dimension can be deleted.",
                    "warning",
                    parent=self.ui
                )
                msg.exec_()
                return

            program_id = self.safe_int(
                self.ui.valueObj.activeVariables_dict.get("ActiveProgramId", 1)
            )

            # 🔥 Get all dimensions BEFORE delete
            all_dims = self.get_channels_for_program(program_id)

            if not all_dims:
                return

            # ✅ CASE 1: Only one dimension → delete entire program
            if len(all_dims) == 1:
                self.data.delete_program(program_id)

                # refresh program list
                self.init_progId_and_dimension()

                new_prog = self.ui.comboBox_programIdSetting_outer.currentText()
                if not new_prog:
                    new_prog = "1"

                new_prog = int(new_prog)

                self.ui.valueObj.activeVariables_dict["ActiveProgramId"] = new_prog

                # 🔥 FORCE reload fresh DB
                self.ui.valueObj.ProgramSettings_dict = \
                    self.ui.databaseObj.load_data_to_ProgramSettings_dict(new_prog)

                # 🔥 CLEAR UI
                self.ui.lineEdit_programNameSettings.clear()
                self.ui.label_programName.clear()

                self.load_as_per_progId()

            # ✅ CASE 2: Multiple dimensions → delete only last dimension
            else:
                self.data.delete_dimension(program_id, current_dim)

                self.load_as_per_progId()

                new_last_dim = self.get_last_dimension()
                if new_last_dim:
                    self.ui.comboBox_toselectProbe.setCurrentText(new_last_dim)

            # 🔄 Final UI sync
            self.update_delete_button_visibility()
            self.data.load_Higher_lower_value_to_ui(
                self.safe_int(self.ui.valueObj.activeVariables_dict.get("ActiveProgramId", "1"))
            )

        except Exception as e:
            print(f"Error deleting dimension: {e}")
            
    def get_selected_master_channels(self):
        try:
            selected = []

            if self.D1_masterGrouping :
                selected.append("D1")
            if self.D2_masterGrouping:
                selected.append("D2")
            if self.D3_masterGrouping:
                selected.append("D3")
            if self.D4_masterGrouping:
                selected.append("D4")

            return selected
        except Exception as e:  
            print(f"Error getting selected master channels: {e}")
      
    # -------- PROGRAM / DIMENSION --------
    # def init_progId_and_dimension(self):
    #     try:
    #         proIds = self.ui.databaseObj.get_all_program_ids()
            
        
    #         self.ui.comboBox_programIdSetting_outer.clear()
    #         self.ui.comboBox_programIdSetting_Inner.clear()

    #         if not proIds:
    #             proIds = [1]

    #         next_id = max(proIds) + 1
    #         self.ui.comboBox_programIdSetting_outer.addItems(map(str, proIds))
    #         self.ui.comboBox_programIdSetting_Inner.addItems(map(str, proIds + [next_id]))

    #         active_id = str(self.ui.valueObj.activeVariables_dict.get("ActiveProgramId", proIds[0]))

    #         self.ui.comboBox_programIdSetting_outer.setCurrentText(active_id)
    #         self.ui.comboBox_programIdSetting_Inner.setCurrentText(active_id)
            
    #     except Exception as e:
    #         print(f"Error in initialization of progId and dimension): {e}")
    def init_progId_and_dimension(self):
        try:
            proIds = self.ui.databaseObj.get_all_program_ids()

            if not proIds:
                proIds = [1]

            next_id = max(proIds) + 1

            outer = self.ui.comboBox_programIdSetting_outer
            inner = self.ui.comboBox_programIdSetting_Inner

            # SAVE CURRENT PROGRAM BEFORE UI CHANGES
            current_program = self.safe_int(
                self.ui.valueObj.activeVariables_dict.get(
                    "ActiveProgramId",
                    proIds[0]
                ),
                1
            )

            # BLOCK SIGNALS
            outer.blockSignals(True)
            inner.blockSignals(True)

            outer.clear()
            inner.clear()

            outer.addItems(map(str, proIds))
            inner.addItems(map(str, proIds + [next_id]))

            # RESTORE
            outer.setCurrentText(str(current_program))
            inner.setCurrentText(str(current_program))

            # UNBLOCK
            outer.blockSignals(False)
            inner.blockSignals(False)

            print("RESTORED PROGRAM =", current_program)

        except Exception as e:
            print(f"Error in initialization of progId and dimension): {e}")
    def progId_changed_outer(self):
        try:
            text = self.ui.comboBox_programIdSetting_outer.currentText()

            # 🔥 CRITICAL GUARD
            if not text.strip():
                return

            program_id = self.safe_int(text, 1)

            self.ui.valueObj.activeVariables_dict["ActiveProgramId"] = program_id

            self.ui.comboBox_programIdSetting_Inner.setCurrentText(str(program_id))

            self.data.load_Higher_lower_value_to_ui(program_id)

            self.ui.dial_indicator.set_visibility()

            self.Handle_master_Grouping(program_id)

            self.load_as_per_progId()

            self.update_delete_button_visibility()

        except Exception as e:
            print(f"Error in outer ProgId changed {e}")      

    def progId_changed_inner(self):
        try:
            self.ui.valueObj.activeVariables_dict["ActiveProgramId"] = self.ui.comboBox_programIdSetting_Inner.currentText()
            self.ui.comboBox_programIdSetting_outer.setCurrentText(str(self.ui.valueObj.activeVariables_dict.get("ActiveProgramId", "1")))
            self.load_as_per_progId()
            self.update_delete_button_visibility()
        except Exception as e:
            print(f"Error in progId changed inner {e}")
            
    def load_as_per_progId(self):
        try:
            program_id = self.safe_int(self.ui.valueObj.activeVariables_dict.get("ActiveProgramId", 1))
            
            # First reload the dictionary from database BEFORE checking channels
            self.ui.valueObj.ProgramSettings_dict = \
                self.ui.databaseObj.load_data_to_ProgramSettings_dict(program_id)
            
            # Now get channels from the FRESHLY RELOADED dictionary
            channels = self.get_channels_for_program(program_id)
            
            # Get current selected dimension from UI (before any changes)
            current_dim = self.ui.comboBox_toselectProbe.currentText()

            # Only reassign if current_dim is NOT in the valid channels list
            # This ensures we keep the user's selection when possible
            if current_dim not in channels and channels:
                current_dim = channels[-1]  # Default to last channel
            elif not current_dim and channels:
                current_dim = channels[-1]  # Default to last channel if nothing selected
            elif not channels:
                current_dim = "D1"  # Ultimate fallback
            # print("DEBUG ProgramSettings_dict keys:",
            # self.ui.valueObj.ProgramSettings_dict.keys())
        

            # 1️⃣ Load program-level UI only
            self.data.load_ProgramSettings_to_ui()
            # self.data.load_ProbeBasedSettings_to_ui()

            # 2️⃣ Update dimensions based on DB
            self.data.update_dimension_combobox(keep_dimension=current_dim)
            self.update_delete_button_visibility()
            # self.update_dimension_combobox(keep_dimension=current_dim)

            # 3️⃣ Load D1 probe + AOC

            self.data.load_ProbeBasedSettings_to_ui(current_dim)
            self.data.load_AOCBasedSettings_to_ui(current_dim)
            # self.data.load_ProbeBasedSettings_to_ui("D1")
            # self.data.load_AOCBasedSettings_to_ui("D1")
            #self.load_Higher_lower_value_to_ui()

            # 4️⃣ Load angle settings
            self.ui.valueObj.AngleCalculationSettings_dict = \
                self.ui.databaseObj.load_data_to_AngleCalculationSettings_dict(program_id)

            self.data.load_AngleCalculationSettings_to_ui()
        except Exception as e:
                print(f"Error in load as per progId: {e}")
        

    def load_as_per_dimension(self,dimension):
        try:
            #self.load_ProgramSettings_to_ui()   # ✅ ADD
            self.data.load_ProbeBasedSettings_to_ui(dimension)
            self.data.load_AOCBasedSettings_to_ui(dimension)
            # self.load_Higher_lower_value_to_ui()
        except Exception as e:
            print(f"Error in load_as_per_dimension: {e}")
            msg = CustomMessageBox("Failed to load dimension settings. Please check the database and try again.", "error",
                                   parent=self.ui)
            msg.exec_()
            

    def get_channels_for_program(self, program_id):
        """
        Returns a list of channels like ['D1', 'D2']
        in sequential order for the given ProgramId
        """

        prog_settings = self.ui.valueObj.ProgramSettings_dict.get("ProgramSpecificSettings", {})
        
        if prog_settings.get("ProgramId") != program_id:
            return []

        return sorted(
            [key for key in self.ui.valueObj.ProgramSettings_dict.keys() if key.startswith("D")],
            key=lambda x: int(x[1:])  # Extract number after 'D'
        )

    def Handle_master_Grouping(self, program_id):
        """
        Show master grouping buttons based on:
        - MASTER_GROUPING Enable flag
        - Channels present for given ProgramId
        """
        # 1️⃣ Check MASTER_GROUPING enable
        current = (
            self.ui.valueObj.IOSettings_dict
            .get('MASTER_GROUPING', {})
            .get('Enable', '0')
        )

        if current != '1':
            # Hide all buttons
            for btn in self.master_group_buttons_with_channel.values():
                btn.hide()
            return

        # 2️⃣ Get channels for program
        available_channels = self.get_channels_for_program(program_id)
        
        
        # 3️⃣ Show/hide buttons
        for channel, button in  self.master_group_buttons_with_channel.items():
            button.setVisible(channel in available_channels)

    # def set_spi_controller(self, spi_controller):
    #     self.spi_controller = spi_controller
        
    # -------- TIME --------
    def handle_set_datetime(self):
        """
        Called when button_setDateTime is pressed.
        Updates Raspberry Pi or i.MX7 system time from UI line edits.
        """
        try:
            if self.ui.utils.is_raspberry_pi():
                self.ui.utils.set_system_time_raspberyPi() # Assuming this method exists and handles its own exceptions
            elif self.ui.utils.is_imx7():
                self.ui.utils.set_system_time_imx7() # Assuming this method exists and handles its own exceptions
            else:
                print("⚠️ Unknown board, cannot set system time")
                msg = CustomMessageBox("Unknown board, cannot set system time.", "warning",
                                       parent=self.ui)
                msg.exec_()
        except Exception as e:
            print(f"Error setting system time: {e}")
            msg = CustomMessageBox("Failed to set system time. Please check inputs and try again.", "error",
                                   parent=self.ui)
            msg.exec_()
    

    # -------- SAVE --------
    def linkage_of_saveButton(self):
        try:
            current_index = self.ui.stacked.currentIndex()
            if current_index == 6:
                self.data.save_toDatabase_WifiSettings() #to save wifiSettings using save button
            elif current_index == 13:
                self.data.save_toDatabase_cncList()
            elif current_index == 8:
                self.data.save_toDatabase_IOSettings()
            elif current_index == 5: 
                self.data.save_toDatabase_IpSettings()
            elif  current_index == 3:
                self.data.save_toDatabase_rs232Settings()
            elif current_index == 25:
                # self.data.save_probe_unique_settings()
                self.ui.spi_controller.save_probe_values()
            elif current_index == 27:
                self.data.save_toDatabase_angleCalculationSettings()
            elif current_index == 26:
                self.data.save_toDatabase_programSetting()
                self.init_progId_and_dimension() 
            elif current_index == 30:
                self.data.save_toDatabase_aocBasedSettings()
                self.data.save_toDatabase_probeBasedSettings()
                self.init_progId_and_dimension() 
            elif current_index == 10:
                # Similar to above, assuming direct call.
                self.data.save_toDatabase_shiftSettings()
            elif current_index == 16:
                # Similar to above, assuming direct call.
                self.data.save_toDatabase_networkedDatabase_settings()
        except Exception as e:
            print(f"Error in linkage_of_saveButton: {e}")
            msg = CustomMessageBox(f"An unexpected error occurred while trying to save settings: {e}", "error",
                                   parent=self.ui)
            msg.exec_()

