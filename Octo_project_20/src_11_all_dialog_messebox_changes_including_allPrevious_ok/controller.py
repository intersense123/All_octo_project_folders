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
from active_ui_handler import *
from set_master import SetMasterController
from models import *

from spi_module import SPI
import models

#class for manage spi to store spi values and map with variables
class Worker(QObject):
    try:
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
    except Exception as e:
        print(f"Error in initialization of class Worker as {e} ")


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
            
            # -------- runtime state --------
            self.probe_data = {}
            self.spi_values = {}
            self.master_low = {}
            self.master_high = {}
            self.master_ready = False
            self.ui.comboBox_toselectProbe.clear()
            
            self.worker_thread = QThread()
            self.worker = Worker()
            self.worker.moveToThread(self.worker_thread)

            self.worker_thread.started.connect(self.worker.run)

            self.worker.spi_generated.connect(self.spi_handler)
            # self.worker.spi_generated.connect(self.set_master)
            self.worker_thread.start()
            
            self.init_progId_and_dimension()
            self.load_as_per_progId()
            self.ui.button_save.clicked.connect(self.linkage_of_saveButton)
            self.ui.button_setDateTime.clicked.connect(self.handle_set_datetime)
            self.ui.button_setMaster.clicked.connect(self.set_master)
            self.ui.comboBox_programIdSetting.currentTextChanged.connect(self.progId_changed_outer)
            self.ui.comboBox_programIdSettings.currentTextChanged.connect(self.progId_changed_inner)
            self.ui.comboBox_toselectProbe.currentTextChanged.connect(lambda : self.load_as_per_dimension(self.ui.comboBox_toselectProbe.currentText()))


            self.probe_labels = {
                    "D1": self.ui.label_value1,
                    "D2": self.ui.label_value2,
                    "D3": self.ui.label_value3,
                    "D4": self.ui.label_value4,
                }

            self.ui.comboBox_programIdSetting.currentTextChanged.connect(self.progId_changed_outer)
            self.ui.comboBox_programIdSettings.currentTextChanged.connect(self.progId_changed_inner)
        except Exception as e:
            print(f"Error in init of Appcontroller: {e}")
            
    # -------- SPI --------
    def spi_handler(self, v1, v2, v3, v4):
        """
        Receives live SPI values from Worker thread.
        Updates raw SPI labels and stores values for each probe.
        """
        try:
            # Update raw SPI display
            self.ui.label_value1.setText(v1)
            self.ui.label_value2.setText(v2)
            self.ui.label_value3.setText(v3)
            self.ui.label_value4.setText(v4)

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
        
    # -------- MASTER --------
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
        
    # -------- OK / NOT OK --------
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
            if self.ui.stacked.currentIndex() != 25:
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

                

        except Exception as e:
            print(f"[OK_NOTOK ERROR] {e}")


    # -------- PROGRAM / DIMENSION --------
    def init_progId_and_dimension(self):
        try:
            proIds = self.ui.databaseObj.get_all_program_ids()
            
        
            self.ui.comboBox_programIdSetting.clear()
            self.ui.comboBox_programIdSettings.clear()

            if not proIds:
                proIds = [1]

            next_id = max(proIds) + 1
            self.ui.comboBox_programIdSetting.addItems(map(str, proIds))
            self.ui.comboBox_programIdSettings.addItems(map(str, proIds + [next_id]))

            active_id = str(self.ui.valueObj.activeVariables_dict.get("ActiveProgramId", proIds[0]))

            self.ui.comboBox_programIdSetting.setCurrentText(active_id)
            self.ui.comboBox_programIdSettings.setCurrentText(active_id)
            
        except Exception as e:
            print(f"Error in initialization of progId and dimension): {e}")

    def progId_changed_outer(self):
        try:
            self.ui.valueObj.activeVariables_dict["ActiveProgramId"] = self.ui.comboBox_programIdSetting.currentText()
            self.ui.comboBox_programIdSettings.setCurrentText(self.ui.valueObj.activeVariables_dict.get("ActiveProgramId"))
            self.data.load_Higher_lower_value_to_ui(
            int(self.ui.valueObj.activeVariables_dict["ActiveProgramId"])
            )
            self.load_as_per_progId()
        except Exception as e:
            print(f"Error in outer ProgId changed {e}")
            

    def progId_changed_inner(self):
        try:
            self.ui.valueObj.activeVariables_dict["ActiveProgramId"] = self.ui.comboBox_programIdSettings.currentText()
            self.ui.comboBox_programIdSetting.setCurrentText(str(self.ui.valueObj.activeVariables_dict.get("ActiveProgramId")))
            self.load_as_per_progId()
        except Exception as e:
            print(f"Error in progId changed inner {e}")
            
    def load_as_per_progId(self):
        try:
            program_id = int(self.ui.valueObj.activeVariables_dict.get("ActiveProgramId", 1))
            
            self.ui.valueObj.ProgramSettings_dict = \
                self.ui.databaseObj.load_data_to_ProgramSettings_dict(program_id)
            print("DEBUG ProgramSettings_dict keys:",
            self.ui.valueObj.ProgramSettings_dict.keys())
        

            # 1️⃣ Load program-level UI only
            self.data.load_ProgramSettings_to_ui()

            # 2️⃣ Update dimensions based on DB
            self.data.update_dimension_combobox()

            # 3️⃣ Load D1 probe + AOC
            self.data.load_ProbeBasedSettings_to_ui("D1")
            self.data.load_AOCBasedSettings_to_ui("D1")
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

    

    # -------- TIME --------
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
            elif current_index == 7 or current_index == 8:
                self.data.save_toDatabase_IOSettings()
            elif current_index == 5: 
                self.data.save_toDatabase_IpSettings()
            elif  current_index == 3:
                self.data.save_toDatabase_rs232Settings()
            elif current_index == 27:
                self.data.save_toDatabase_angleCalculationSettings()
            elif current_index == 26:
                self.data.save_toDatabase_programSetting()
            elif current_index == 30:
                self.data.save_toDatabase_aocBasedSettings()
                self.data.save_toDatabase_probeBasedSettings()
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
            print("MainWindow destroyed, movies stopped.")
        except Exception as e:
            print(f"Error during MainWindow destruction: {e}")