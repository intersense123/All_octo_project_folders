from decimal import Decimal
import queue
from PySide2.QtWidgets import QDialog, QLabel, QPushButton, QHBoxLayout, QVBoxLayout
from PySide2.QtWidgets import QApplication, QMainWindow, QStackedWidget , QWidget
from PySide2.QtCore import QTimer, Qt
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import QObject, Signal
from models import *
from spi_module import SPI
from PySide2.QtCore import QObject , QThread , Signal, Qt
from messageBox import CustomMessageBox
from models import SessionLocal
import re
from math import *
import copy
import threading
import time

from dial_handler import DialHandler



# Handles continuous SPI emission for master-setting popups
class Worker(QObject):

    spi_generated = Signal(list)   # ✅ CHANGED
    finished = Signal()


    # Initialize SPI worker with factory configuration and probe sensitivity
    def __init__(self, factory_config,responsiveness,probe_sensitivity,parent=None):

        try:
            super().__init__(parent)
            self.factory_config = factory_config
            # self.responsiveness = responsiveness
            self._running = True
            self.spi = SPI(factory_config, responsiveness,probe_sensitivity)
        except Exception as e:
            print(f"Error while initialization in worker thread -> {e}")

    @QtCore.Slot()
    def run(self):
        try:
            for value in self.spi.spi_value_emitter():
                if not self._running:
                    break

                # str_values = list(map(str, value))   # ✅ dynamic
                str_values = list(map(str, value))[::-1]   # ✅ reverse to match D1,D2,D3,D4 order
                self.spi_generated.emit(str_values)

        finally:
            self.cleanup()

    def stop(self):
        self._running = False

    def cleanup(self):
        try:
            self.spi.close()
        except Exception:
            pass
        self.finished.emit()

class Set_master_ui(QtWidgets.QDialog):
    def __init__(self, title_text, btn_text="OK",
             parent=None,
             db_values=None,
             mode=None,
             selected_probes=None,
             formula_list=None,
             formula_func=None
             ):
        """
        Args:
            title_text: Title of the popup
            btn_text: Button text
            parent: Parent widget
            db_values: Dict containing DB values to display (optional)
                       Keys: 'MasterHigher', 'MasterLower', 'Range', 'NominalValue', 'Method', 'Dimension'
        """
        try:
            super().__init__(parent)
            self.db_values = db_values or {}
            
            self.mode = mode              # "high" or "low"
            self.selected_probes = selected_probes or []
            self.formula_list = formula_list or []
            self.formula_func = formula_func
            self.setFixedSize(580, 300)
            self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.CustomizeWindowHint)
            self.showFullScreen()
            self.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
            self.result = None
            self.current_spi_map = {}
            # Styles
            self.setStyleSheet("""
                QDialog {
                    background-color: #444444; 
                    border-radius: 10px;
                }
                QLabel {
                    color: white;                
                    font-size: 16pt;
                }
                QPushButton {
                    background-color: #1E90FF; 
                    color: white;
                    font-size: 14pt;
                    border-radius: 5px;
                    padding: 10px 20px;
                }
                QPushButton:hover {
                    background-color: #187bcd;
                }
            """)

            # # ----- Title Layout with Close Button -----
            self.title_layout = QHBoxLayout()

            self.title_label = QLabel(title_text)
            self.title_label.setAlignment(Qt.AlignCenter)
            self.title_label.setFixedSize(500,60)
            self.title_label.setStyleSheet("background-color: #444444;font-size: 19pt; font-weight: bold;")

            self.close_btn = QPushButton("X")
            self.close_btn.setFixedSize(40, 40)
            self.close_btn.setStyleSheet("""
                QPushButton {
                    background-color: #444444;
                    color: white;
                    font-size: 10pt;
                    border-radius: 15px;
                    padding: 0px;
                }
                QPushButton:hover {
                    background-color: #187bcd;
                }
            """)

            self.close_btn.clicked.connect(self.reject)   # 🔴 IMPORTANT

            self.title_layout.addWidget(self.title_label)
            self.title_layout.addStretch()
            self.title_layout.addWidget(self.close_btn)
            self.main_label = QLabel()
            self.main_label.setAlignment(Qt.AlignCenter)
            self.main_label.setStyleSheet("""
                font-size: 16pt;
                color: white;
                font-weight: bold;
                background-color: #444444;
            """)

            # ----- Button -----
            self.btn = QPushButton(btn_text)
            self.btn.setFixedSize(140, 40)
            self.btn.clicked.connect(self.accept)
            # self.btn_layout = QHBoxLayout()
            # self.btn_layout.addStretch()
            # self.btn_layout.addWidget(self.btn)
            # self.btn_layout.addStretch()

            self.btn_layout = QHBoxLayout()
            v = QVBoxLayout()
            v.addSpacing(2)
            # v.addWidget(self.title_layout)
            v.addLayout(self.title_layout)
            v.addSpacing(5)
            v.addWidget(self.main_label)
            v.addSpacing(5)
            # v.addLayout(self.btn_layout)
            # v.addLayout(self.btn_layout)
            v.addLayout(self.btn_layout)
            # v.addWidget(self.btn, alignment=Qt.AlignCenter)
            self.setLayout(v)
            self.update_button_position()
            QtCore.QTimer.singleShot(0, self.center_on_parent)
        except Exception as e:
            print(f"Error initialization of Set master ui -> {e}")

    def update_spi_value(self, values):
            try:
                probes = ["D1", "D2", "D3", "D4"]

                # -------------------------------
                # ✅ RAW SPI VALUES
                # -------------------------------
                raw_map = {}
                for i, val in enumerate(values):
                    if i < len(probes):
                        raw_map[probes[i]] = float(val)

                # -------------------------------
                # ✅ APPLY FORMULA (same as UI)
                # -------------------------------
                if self.formula_func and self.formula_list:
                    a = raw_map.get("D1", 0)
                    b = raw_map.get("D2", 0)
                    c = raw_map.get("D3", 0)
                    d = raw_map.get("D4", 0)

                    result = self.formula_func(a, b, c, d, self.formula_list)

                    self.current_spi_map = {
                        "D1": result[0],
                        "D2": result[1],
                        "D3": result[2],
                        "D4": result[3],
                    }
                else:
                    # fallback (no formula)
                    self.current_spi_map = raw_map

                self._refresh_combined_display()

            except Exception as e:
                print("Popup SPI update error:", e)

        
    def _refresh_combined_display(self):

        lines = []

        for probe in self.selected_probes:

            spi_val = self.current_spi_map.get(probe, "")
            db_val = ""

            if self.mode == "high":
                db_val = self.db_values.get(probe, {}).get("MasterHigher", "")
                line = f"<b>{probe}</b> : {spi_val}    |     Higher Master : {db_val}"

            elif self.mode == "low":
                db_val = self.db_values.get(probe, {}).get("MasterLower", "")
                line = f"<b>{probe}</b> : {spi_val}     |    Lower Master : {db_val}"

            else:
                # Remove Parts popup
                line = f"<b>{probe}</b> : {spi_val}"

            lines.append(line)

        self.main_label.setText(
            "<div style='line-height: 1.8;'>"
            + "<br>".join(lines) +
            "</div>"
        )

    def update_button_position(self):
        # Clear existing layout
        while self.btn_layout.count():
            item = self.btn_layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.setParent(None)

        if self.mode == "high":
            # Button on LEFT
            self.btn_layout.addSpacing(50)
            self.btn_layout.addWidget(self.btn)
            self.btn_layout.addStretch()

        elif self.mode == "low":
            # Button on RIGHT
            self.btn_layout.addStretch()
            self.btn_layout.addWidget(self.btn)
            self.btn_layout.addSpacing(50)

        else:
            # CENTER (default case)
            self.btn_layout.addStretch()
            self.btn_layout.addWidget(self.btn)
            self.btn_layout.addStretch()
            
    def center_on_parent(self):
        if self.parent():
            parent_rect = self.parent().frameGeometry()
            self_rect = self.frameGeometry()
            self_rect.moveCenter(parent_rect.center())
            self.move(self_rect.topLeft())
            
       
class SetMasterController(QObject):
    """
    Handles Set Master workflow and master calculations.
    """
    master_finished = Signal(dict,dict)   # Emits probe_data dict

    def __init__(self, parent, spi_values,spi_signal,grouped_channels=None,
                formula_list=None,
                formula_func=None
                ):
        
        super().__init__(parent)

        self.ui_parent = parent
        self.spi_values = spi_values
        self.spi_signal = spi_signal   # 🔥 SPI live signal
        self.grouped_channels = grouped_channels or []
        self.formula_list = formula_list or []
        self.formula_func = formula_func
        self.master_high = {}
        self.removed_parts = {}
        self.master_low = {}
        self.probe_data = {}
        self.raw_range = 0
        self.probe = None
        self.no_master_limits = {}
        

    def get_probe_db_values(self, probe):
        try:
            active_program_id = int(
                self.ui_parent.valueObj.activeVariables_dict["ActiveProgramId"]
            )
            # active_program_id = int(self.ui_parent.comboBox_programIdSetting_outer.currentText())
            with SessionLocal() as session:
                row = session.query(ProbeBasedSettings).filter(
                    ProbeBasedSettings.Dimension == probe,
                    ProbeBasedSettings.ProgramId == active_program_id
                ).first()

                if row:
                    return {
                        'Dimension': row.Dimension,
                        'MasterHigher': row.MasterHigher,
                        'MasterLower': row.MasterLower,
                        'Master' : row.Master,
                    }
        except Exception as e:
            print(f"[get_probe_db_values ERROR] {e}")

        return {}

    def check_autosense_conflict(self, active_channels):
        try:
            TOL = 10

            for probe in active_channels:   # 🔥 ONLY ACTIVE

                auto = self.removed_parts.get(probe)
                if auto is None:
                    continue

                auto = float(auto)

                high = self.master_high.get(probe)
                low = self.master_low.get(probe)

                if high is not None:
                    diff_high = abs(auto - float(high))
                    # print(f"[DEBUG] {probe} diff_high = {diff_high}")

                    if diff_high <= TOL:
                        return False, f"{probe}: Auto within {TOL} of HIGH"

                if low is not None:
                    diff_low = abs(auto - float(low))
                    # print(f"[DEBUG] {probe} diff_low = {diff_low}")

                    if diff_low <= TOL:
                        return False, f"{probe}: Auto within {TOL} of LOW"

            return True, None

        except Exception as e:
            return False, f"AutoSense check failed: {e}"
    
            
    def run(self):
        """
        Runs high master, low master, and calculation sequence.
        """
        try:
            # 1️⃣ Check MASTER_GROUPING enable
            current = (
                self.ui_parent.valueObj.IOSettings_dict
                .get('MASTER_GROUPING', {})
                .get('Enable', '0')
            )
            if current == '0':
                Ac=self.ui_parent.controller.get_channels_for_program(
                int(self.ui_parent.valueObj.activeVariables_dict["ActiveProgramId"])
                )
                Active_channels = sorted(Ac, key=lambda x: int(x[1:]))
                # print("Active_channels =",Active_channels)
                remove_parts = Set_master_ui(
                    "Remove parts from fixture",
                    "Next",
                    parent=self.ui_parent,
                    mode=None,                    # no DB mode
                    selected_probes=Active_channels,
                    formula_list=self.formula_list,
                    formula_func=self.formula_func
                )
                self.spi_signal.connect(remove_parts.update_spi_value)
                result = remove_parts.exec_()
                self.spi_signal.disconnect(remove_parts.update_spi_value)
                if result == QDialog.Rejected:
                    return
                # Store remove Values
                for probe, spi in self.spi_values.items():
                    self.removed_parts[probe] = spi
                    # print(f"Removed {probe}: {spi}")
                
                # ---------- LOW MASTER ----------
                # Get DB values for all probes to display
                db_values_low = {}
                for probe in self.spi_values.keys():
                    probe_db = self.get_probe_db_values(probe)
                    if probe_db:
                        db_values_low[probe] = probe_db
                

                lower_master_raw_val = Set_master_ui(
                    "Set Lower Master",
                    "OK",
                    parent=self.ui_parent,
                    db_values=db_values_low,
                    mode="low",
                    selected_probes=Active_channels,
                    formula_list=self.formula_list,
                    formula_func=self.formula_func
                )

                self.spi_signal.connect(lower_master_raw_val.update_spi_value)
                result = lower_master_raw_val.exec_()
                if result == QDialog.Rejected:
                    return
                self.spi_signal.disconnect(lower_master_raw_val.update_spi_value)

                # Store LOW master values
                for probe, spi in self.spi_values.items():
                    self.master_low[probe] = spi
                    
                # ---------- HIGH MASTER ----------
                # Get DB values for all probes to display
                db_values_high = {}
                for probe in self.spi_values.keys():
                    probe_db = self.get_probe_db_values(probe)
                    if probe_db:
                        db_values_high[probe] = probe_db
                
                higher_master_raw_val = Set_master_ui(
                    "Set Higher Master",
                    "OK",
                    parent=self.ui_parent,
                    db_values=db_values_high,
                    mode="high",
                    selected_probes=Active_channels,
                    formula_list=self.formula_list,
                    formula_func=self.formula_func
                )

                # 🔴 CONNECT SPI TO POPUP
                self.spi_signal.connect(higher_master_raw_val.update_spi_value)

                result = higher_master_raw_val.exec_()
                if result == QDialog.Rejected:
                    return
                # 🔴 DISCONNECT AFTER CLOSE
                self.spi_signal.disconnect(higher_master_raw_val.update_spi_value)
                # Store HIGH master values
                for probe, spi in self.spi_values.items():
                    self.master_high[probe] = spi

                # 🔥 NEW VALIDATION
                ok, msg = self.check_autosense_conflict(Active_channels)

                if not ok:
                    popup_error = Set_master_ui(
                        f"First Step Failed,Set Master Again.",
                        "Close",
                        parent=self.ui_parent
                    )
                    popup_error.exec_()
                    return

                success, error_msg = self.calculate()

                if not success:
                    popup_fail = Set_master_ui(
                        f"Master Set Unsuccessful.",
                        "Close",
                        parent=self.ui_parent
                    )
                    popup_fail.exec_()
                    return

                # ---------- CALCULATION ----------
                self.calculate()
                popup_res = Set_master_ui("Master Set Successfully", "Close", parent=self.ui_parent)
                popup_res.exec_()                    
                self.master_finished.emit(self.probe_data,self.removed_parts)

            elif current == '1':
                if not self.grouped_channels:
                    # print("[GROUPING] No channels selected")
                    return
                
                remove_parts = Set_master_ui("Remove parts from fixture",
                    "Next", 
                    parent=self.ui_parent,
                    mode=None,
                    selected_probes=self.grouped_channels,
                    formula_list=self.formula_list,
                    formula_func=self.formula_func   
                )
                self.spi_signal.connect(remove_parts.update_spi_value)
                
                result = remove_parts.exec_()
                if result == QDialog.Rejected:
                    return
                self.spi_signal.disconnect(remove_parts.update_spi_value)
                
                  # Store remove values
                for probe, spi in self.spi_values.items():
                    self.removed_parts[probe] = spi
                    # print(f"Removed {probe}: {spi}")  
                    
                # ---------- LOW MASTER (GROUPED) ----------
                # Get DB values for grouped probes to display
                db_values_low = {}
                for probe in self.grouped_channels:
                    probe_db = self.get_probe_db_values(probe)
                    if probe_db:
                        db_values_low[probe] = probe_db
                
                lower_master_raw_val = Set_master_ui(
                    "Set Lower Master",
                    "OK",
                    parent=self.ui_parent,
                    db_values=db_values_low,
                    mode="low",
                    selected_probes=self.grouped_channels,
                    formula_list=self.formula_list,
                    formula_func=self.formula_func
                )
                self.spi_signal.connect(lower_master_raw_val.update_spi_value)
                result = lower_master_raw_val.exec_()
                if result == QDialog.Rejected:
                    return
                self.spi_signal.disconnect(lower_master_raw_val.update_spi_value)

                for probe, spi in self.spi_values.items():
                    if probe in self.grouped_channels:
                        self.master_low[probe] = spi
                
                    
                # ---------- HIGH MASTER (GROUPED) ----------
                # Get DB values for grouped probes to display
                db_values_high = {}
                for probe in self.grouped_channels:
                    probe_db = self.get_probe_db_values(probe)
                    if probe_db:
                        db_values_high[probe] = probe_db
                
                higher_master_raw_val = Set_master_ui(
                    "Set Higher Master",
                    "OK",
                    parent=self.ui_parent,
                    db_values=db_values_high,
                    mode="high",
                    selected_probes=self.grouped_channels,
                    formula_list=self.formula_list,
                    formula_func=self.formula_func
                )
                self.spi_signal.connect(higher_master_raw_val.update_spi_value)
                result = higher_master_raw_val.exec_()
                if result == QDialog.Rejected:
                    return
                self.spi_signal.disconnect(higher_master_raw_val.update_spi_value)

                for probe, spi in self.spi_values.items():
                    if probe in self.grouped_channels:
                        self.master_high[probe] = spi

                
                # 🔥 NEW VALIDATION
                ok, msg = self.check_autosense_conflict(self.grouped_channels)

                if not ok:
                    popup_error = Set_master_ui(
                        f"First Step Failed,Set Master Again.",
                        "Close",
                        parent=self.ui_parent
                    )
                    popup_error.exec_()
                    return
                
                success, error_msg = self.calculate()

                if not success:
                    popup_fail = Set_master_ui(
                        f"Master Set Unsuccessful.",
                        "Close",
                        parent=self.ui_parent
                    )
                    popup_fail.exec_()
                    return


                # ---------- CALCULATION ----------
                self.calculate()
                popup_res = Set_master_ui("Master Set Successfully", "Close", parent=self.ui_parent)
                popup_res.exec_()

                self.master_finished.emit(self.probe_data,self.removed_parts)
                
        except Exception as e:
            print(f"[SetMasterController.run ERROR] {e}")

    def calculate(self):
        """
        Calculates mm per raw SPI for each probe.
        """
        try:
            failed_probes = []
            active_program_id = int(
                self.ui_parent.valueObj.activeVariables_dict["ActiveProgramId"]
            )

            with SessionLocal() as session:
                rows = session.query(ProbeBasedSettings).filter(
                    ProbeBasedSettings.ProgramId == active_program_id
                ).all()
            # with SessionLocal() as session:
            #     rows = session.query(ProbeBasedSettings).all()
            program_specific_settings = self.ui_parent.valueObj.ProgramSettings_dict.get('ProgramSpecificSettings', {})
            # print("Responsiveness == ", program_specific_settings.get("Responsiveness", "0"))
            
            for row in rows:
                probe = row.Dimension
                
                # 🔴 SKIP NO MASTER PROBES
                if row.MasterType == "No Master":
                    # if not hasattr(self, "no_master_limits"):
                    #     self.no_master_limits = {}

                    self.no_master_limits[row.Dimension] = {
                        "USL": row.UpperSpecificationLimit,
                        "LSL": row.LowerSpecificationLimit,
                        "method": row.Method,
                        "leastcount":row.LeastCount
                    }
                    continue
                spi_low = self.master_low.get(probe)
                spi_high = self.master_high.get(probe)

                if spi_low is None or spi_high is None:
                    continue

                self.raw_range = spi_high - spi_low
                if self.raw_range == 0:
                    print(f"[ERROR] {probe}: SPI high and low same")
                    self.probe = probe
                    return False, f"{probe}"
                    # continue 

                DB_low = row.MasterLower
                DB_high = row.MasterHigher
                Dial_range = row.Range
                Nominal = row.NominalValue

                calculated_value = (DB_high - DB_low) / self.raw_range
                if program_specific_settings.get("Uom") == 'inch':
                    
                    inch_value = calculated_value * 25.4
                    # 🔴 VALIDATION LOGIC
                    if row.Method == "OD" and inch_value < 0:
                        failed_probes.append(f"{probe} ")
                        continue
                        # return False, f"{probe}"

                    if row.Method == "ID" and inch_value > 0:
                        failed_probes.append(f"{probe} ")
                        continue

                    self.probe_data[probe] = {
                        "DB_low": DB_low,
                        "DB_high": DB_high,
                        "DB_master": row.Master,
                        "method": row.Method,
                        "USL": row.UpperSpecificationLimit,
                        "LSL": row.LowerSpecificationLimit,
                        "Master Type":row.MasterType,
                        "Range": Dial_range,
                        "Nominal": Nominal,
                        "LeastCount":row.LeastCount,
                        "SPI_low": spi_low,
                        "SPI_high": spi_high,
                        "converted_raw_value": inch_value,
                        "master_ready": True
                    }
                    
                elif program_specific_settings.get("Uom") == 'mm':
                    mm_value = calculated_value 
                
                    # 🔴 VALIDATION LOGIC
                    if row.Method == "OD" and mm_value < 0:
                        failed_probes.append(f"{probe} ")
                        continue

                    if row.Method == "ID" and mm_value > 0:
                        failed_probes.append(f"{probe} ")
                        continue

                    self.probe_data[probe] = {
                        "DB_low": DB_low,
                        "DB_high": DB_high,
                        "DB_master": row.Master,
                        "method": row.Method,
                        "USL": row.UpperSpecificationLimit,
                        "LSL": row.LowerSpecificationLimit,
                        "Master Type":row.MasterType,
                        "Range": Dial_range,
                        "Nominal": Nominal,
                        "LeastCount":row.LeastCount,
                        "SPI_low": spi_low,
                        "SPI_high": spi_high,
                        "converted_raw_value": mm_value,
                        "master_ready": True
                    }
            if failed_probes:
                return False, failed_probes
  
            return True, ""

        except Exception as e:
            print(f"[SetMasterController.calculate ERROR] {e}")
            return False, str(e)

class SPIController(QObject):
    """
    Handles:
    - SPI
    - Master logic
    - OK / NOT OK
    """
    save_completed = Signal(bool) 
    def __init__(self, main_window, data_handler,app_controller):
        try:
            super().__init__()
            self.ui = main_window
            self.data = data_handler
            self.app = app_controller
            self.counter = 0
            
            # -------- runtime state --------
            self.probe_data = {}
            self.spi_values = {}
            self.master_low = {}
            self.master_high = {}
            self.removed_parts = {}
            self.previous_values = {}
            self.status_stable_since = {}   # per probe
            self.last_raw_status = {}       # per probe (instant status)
            self.auto_save_duration = 0.5
            self.last_checked_relay_color = None
            self.master_ready_popup_shown = False
            
            self.master_ready = False
            self.worker_thread = None
            self.worker = None
            self.master_set = None
            self.no_master_limits = {}
            self.current_factory = None
            self.relay_state = None
            self.relay_value = 0.0
            self.last_relay_color = None
            self.prev_status = {}
            self.load_least_counts()
            self.last_trigger_time = 0
            self.setup_auto_save()
            self.ui.button_setMaster.clicked.connect(self.set_master)
            self.probe_labels = {
                    "D1": self.ui.label_value1,
                    "D2": self.ui.label_value2,
                    "D3": self.ui.label_value3,
                    "D4": self.ui.label_value4,
                }
            self.status_labels = {
                    "D1": self.ui.label_status1,
                    "D2": self.ui.label_status2,
                    "D3": self.ui.label_status3,
                    "D4": self.ui.label_status4,
            }
            self.db_queue = queue.Queue()

            threading.Thread(
                target=self.save_worker, 
                daemon=True
            ).start()

            # # Create DialHandler once
            # self.dial_1_anim = DialHandler(self.ui, 135, 60, 6, 85)

            factory = self.load_factory_from_db()
            if factory:
                self.current_factory = factory
                # self.hide_show_lables()
                self.on_factory_changed(factory)
            else:
                print("No factory config found on startup")

            # self.combine_individual()
            self.formula_Cache = self.get_formula_bar()
            self.data.probe_setttings_saved.connect(self.refresh_settings)
            self.save_completed.connect(self.handle_save_signal)
            self.relay_handler()
            self.last_status = {}   # store last status per probe
            self.data.io_settings_saved.connect(
                lambda: (
                    self.relay_handler(),
                    self.update_auto_save()
                )
            )
            # self.data.io_settings_saved.connect(self.relay_handler)
            self.data.probe_setttings_saved.connect(lambda:(self.load_least_counts(),
                                                            self.update_auto_save()))
            self.global_counter, self.job_count = self.ui.savedbObj.get_next_counters()
            savemasterOnDb = (
                self.ui.valueObj.IOSettings_dict
                .get('SAVE_MASTER_CALIBRATION', {})
                .get('Enable', 'OFF')
            )

            if savemasterOnDb == 'ON':
                self.load_saved_master_settings()
        except Exception as e:
            print(f"Error in init of SPIcontroller: {e}")
            
    def setup_auto_save(self):
        self.auto_save_timer = QTimer()
        self.auto_save_timer.timeout.connect(self.autoSave_Handler)
          
    def update_auto_save(self):
        try:

            # state = self.ui.valueObj.IOSettings_dict.get(
            #     'AUTO_SAVE_READING', {}
            # ).get('Enable', '0')
            state = self.ui.valueObj.IOSettings_dict['AUTO_SAVE_READING']['Enable']

            # -----------------------------
            # DISABLE
            # -----------------------------
            if state != '1':

                self.auto_save_timer.stop()
                return

            # -----------------------------
            # GET DURATION
            # -----------------------------
            ps = self.ui.valueObj.ProgramSettings_dict.get(
                "ProgramSpecificSettings", {}
            )
            auto_save_duration = float(
                ps.get("AutoSave_Duration", 0.5)
            )
            # milliseconds
            interval = int(auto_save_duration * 1000)
            self.auto_save_timer.start(interval)

        except Exception as e:
            print(f"Auto Save Update Error -> {e}")    
                 
    # def handle_save_signal(self, success):
    #     if success:
    #         if self.ui.stacked.currentIndex() == 25:
    #             self.ui.label_savesignal.show()

    #             # auto-hide after 1 second
    #             QTimer.singleShot(1000, self.ui.label_savesignal.hide)
    #     else:
    #         self.ui.label_savesignal.hide()
    def handle_save_signal(self, success):

        if not success:
            self.ui.label_savesignal.hide()
            return

        if self.ui.stacked.currentIndex() != 25:
            return

        self.ui.label_savesignal.show()
        QTimer.singleShot(1000, self.ui.label_savesignal.hide)
            
    def relay_handler(self):
        self.relay_state = self.ui.valueObj.IOSettings_dict['RELAY']['Enable']
        # print(f"relay state = {self.relay_state}")
        relay_value = self.ui.valueObj.IOSettings_dict['RELAY']['Value']
        if relay_value is None or str(relay_value).strip() == '':
            self.relay_value = 0.0
        else:
            try:
                self.relay_value = float(relay_value)
            except ValueError:
                self.relay_value = 0.0
    
    def refresh_settings(self):
        # print("Refreshing settings...")
        self.formula_Cache = self.get_formula_bar()    
    
    def get_all_probe_sensitivity(self):
        active_program_id = int(
            self.ui.valueObj.activeVariables_dict["ActiveProgramId"]
        )

        probes = ["D1", "D2", "D3", "D4"]
        sensitivities = []

        with SessionLocal() as session:
            for probe in probes:
                row = session.query(ProbeBasedSettings).filter(
                    ProbeBasedSettings.Dimension == probe,
                    ProbeBasedSettings.ProgramId == active_program_id
                ).first()

                if row and row.ProbeSensitivity is not None:
                    sensitivities.append(row.ProbeSensitivity)
                else:
                    sensitivities.append(0)  # default fallback

        return sensitivities  
        
    def load_factory_from_db(self):
        with SessionLocal() as session:
            try:
                row = session.query(FactoryConfigSettings).first()
                if row and row.factory_config:
                    return row.factory_config
            except Exception as e:
                print("DB Load Error:", e)
        return None
    
    #Worker thread creation for spi Handle        
    def on_factory_changed(self, config):
        try:
            # print("Factory changed to:", config)
            self.current_factory = config
            # self.hide_show_lables()
            ps = self.ui.valueObj.ProgramSettings_dict.get("ProgramSpecificSettings", {})
            Responsiveness = ps.get("Responsiveness", "0")
            probe_sensitivity = self.get_all_probe_sensitivity()

            print("Probe Sens:", probe_sensitivity)  # debug
            
            # 🔴 STOP OLD WORKER
            if hasattr(self, "worker") and self.worker is not None :
                self.worker.stop()
                self.worker_thread.quit()
                self.worker_thread.wait()

            # 🔴 CREATE NEW THREAD + WORKER
            self.worker_thread = QThread()
            self.worker = Worker(config,Responsiveness,probe_sensitivity)

            self.worker.moveToThread(self.worker_thread)
            self.worker_thread.started.connect(self.worker.run)

            self.worker.spi_generated.connect(self.spi_handler)
            self.worker.spi_generated.connect(self.update_raw_labels)
            self.worker.finished.connect(self.worker_thread.quit)

            self.worker_thread.start()
        except Exception as e:
            print(f"Error in on factory changed -> {e}")
            
    def spi_handler(self, values):
        try:
            self.counter += 1

            # -------------------------------
            # ✅ DYNAMIC MAPPING
            # -------------------------------
            probes = ["D1", "D2", "D3", "D4"]

            # reset first
            for p in probes:
                self.spi_values[p] = 0
                        
            for i, val in enumerate(values):
                if i < len(probes):
                    self.spi_values[probes[i]] = float(self.clean_spi_value(val))

            # -------------------------------
            # ✅ PREPARE a,b,c,d FOR FORMULA
            # -------------------------------
            a = self.spi_values.get("D1", 0)
            b = self.spi_values.get("D2", 0)
            c = self.spi_values.get("D3", 0)
            d = self.spi_values.get("D4", 0)

            # -------------------------------
            # ✅ APPLY FORMULA
            # -------------------------------
            formula_bar_text = self.formula_Cache

            values_list = self.set_per_formula(a, b, c, d, formula_bar_text)

            if len(formula_bar_text) >= 1:
                self.spi_values["D1"] = values_list[0]
            if len(formula_bar_text) >= 2:
                self.spi_values["D2"] = values_list[1]
            if len(formula_bar_text) >= 3:
                self.spi_values["D3"] = values_list[2]
            if len(formula_bar_text) == 4:
                self.spi_values["D4"] = values_list[3]

            # -------------------------------
            # ✅ UI UPDATE
            # -------------------------------
            self.ui.label_value1.setText(str(self.spi_values["D1"]))
            self.ui.label_value2.setText(str(self.spi_values["D2"]))
            self.ui.label_value3.setText(str(self.spi_values["D3"]))
            self.ui.label_value4.setText(str(self.spi_values["D4"]))

            # -------------------------------
            # ✅ OK/NOT OK
            # -------------------------------
            self.ok_notok_part_check()

        except Exception as e:
            print(f"Error in spi_handler -> {e}")
            
    def get_processed_spi_map(self, values): 
        #for SetMater Page SHow Raw VAlues
        probes = ["D1", "D2", "D3", "D4"]

        raw_map = {}
        for i, val in enumerate(values):
            if i < len(probes):
                raw_map[probes[i]] = float(self.clean_spi_value(val))

        if self.set_per_formula and self.formula_Cache:
            a = raw_map.get("D1", 0)
            b = raw_map.get("D2", 0)
            c = raw_map.get("D3", 0)
            d = raw_map.get("D4", 0)

            result = self.set_per_formula(a, b, c, d, self.formula_Cache)

            return {
                "D1": result[0],
                "D2": result[1],
                "D3": result[2],
                "D4": result[3],
            }

        return raw_map  
         
    def update_raw_labels(self, values):
        try:
            spi_map = self.get_processed_spi_map(values)
            self.ui.label_liveD1Val.setText(str(spi_map.get("D1", "")))
            self.ui.label_liveD2Val.setText(str(spi_map.get("D2", "")))
            self.ui.label_liveD3Val.setText(str(spi_map.get("D3", "")))
            self.ui.label_liveD4val.setText(str(spi_map.get("D4", "")))

        except Exception as e:
            print("Live processed label error:", e)
            
    def resolve_formulas(self, formula_list):
        pattern = re.compile(r'\bD([1-4])\b')

        while True:
            changed = False
            new_list = []

            for formula in formula_list:
                def replacer(m):
                    idx = int(m.group(1)) - 1
                    if 0 <= idx < len(formula_list):
                        return f"({formula_list[idx]})"  # wrap to preserve math precedence
                    return m.group(0)

                updated = pattern.sub(replacer, formula)

                if updated != formula:
                    changed = True

                new_list.append(updated)

            formula_list = new_list

            # stop when no D1–D4 left in any formula
            if not changed:
                break

        return formula_list         
                  
    def set_per_formula(self, a, b, c, d, formula_list):
        try:
            # 🔥 freeze original values
            base_vars = {
                "a": a,
                "b": b,
                "c": c,
                "d": d
            }

            values = []

            formula_list = self.resolve_formulas(formula_list)

            for formula in formula_list:

                if not formula:
                    values.append(None)
                    continue

                real_formula = re.sub(
                    r'\bP([1-4])\b',
                    lambda m: str(base_vars["abcd"[int(m.group(1)) - 1]]),
                    formula
                )

                try:
                    result = eval(real_formula)
                except:
                    result = 0

                values.append(result)
                # print("FORMULA:", real_formula)
            return (values + [None]*4)[:4]

        except Exception as e:
            print("Error in set_per_formula ->", e)

    def get_formula_bar(self):
        try:
            formula_bar_text = []
            channels=self.app.get_channels_for_program(
                    int(self.ui.valueObj.activeVariables_dict["ActiveProgramId"])
                )
            
            channel_count = len(channels)
            active_program_id = int(
                self.ui.valueObj.activeVariables_dict["ActiveProgramId"]
            )

            with SessionLocal() as session:
                if channel_count >= 1:
                    formula_text = ''
                    formula_text = session.query(ProbeBasedSettings.Formula) \
                        .filter(
                            ProbeBasedSettings.ProgramId == active_program_id,
                            ProbeBasedSettings.Dimension == "D1"
                        ) \
                        .scalar()

                    formula_bar_text.append(formula_text)

                if channel_count >= 2:
                    formula_text = ''
                    formula_text = session.query(ProbeBasedSettings.Formula) \
                        .filter(
                            ProbeBasedSettings.ProgramId == active_program_id,
                            ProbeBasedSettings.Dimension == "D2"
                        ) \
                        .scalar()
                    
                    formula_bar_text.append(formula_text)         
                
                if channel_count >= 3:
                    formula_text = ''
                    formula_text = session.query(ProbeBasedSettings.Formula) \
                        .filter(
                            ProbeBasedSettings.ProgramId == active_program_id,
                            ProbeBasedSettings.Dimension == "D3"
                        ) \
                        .scalar()
                    
                    formula_bar_text.append(formula_text)

                if channel_count == 4:
                    formula_text = ''
                    formula_text = session.query(ProbeBasedSettings.Formula) \
                            .filter(
                                ProbeBasedSettings.ProgramId == active_program_id,
                                ProbeBasedSettings.Dimension == "D4"
                            ) \
                            .scalar()
                    
                    formula_bar_text.append(formula_text)

            return formula_bar_text
        except Exception as e:
            print(f"Error in get_formula_bar -> {e}")
            return []

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
            current = (
                self.ui.valueObj.IOSettings_dict
                .get('MASTER_GROUPING', {})
                .get('Enable', '0')
            )
            if current == '0':
                self.master_set = SetMasterController(
                    parent=self.ui,
                    spi_values=self.spi_values,
                    spi_signal=self.worker.spi_generated,  # 🔥 PASS SIGNAL
                    grouped_channels = None,
                    formula_list=self.formula_Cache,
                    formula_func=self.set_per_formula
                )

                # Receive computed probe calibration data
                self.master_set.master_finished.connect(self.on_master_finished)

                # Blocking call (modal dialogs inside)
                self.master_set.run()
                
            elif current == '1':
                selected_channels = self.app.get_selected_master_channels()
                
                if not selected_channels:
                    # print("Grouping enabled but no channels selected")
                    msg = CustomMessageBox("Grouping enabled but no channels selected.", "error",
                                   parent=self.ui)
                    msg.exec_()
                    return

                self.master_set = SetMasterController(
                    parent=self.ui,
                    spi_values=self.spi_values,
                    spi_signal=self.worker.spi_generated,
                    grouped_channels=selected_channels,
                    formula_list=self.formula_Cache,
                    formula_func=self.set_per_formula
                )

                self.master_set.master_finished.connect(self.on_master_finished)
                self.master_set.run()
            
        except Exception as e:
            print(f"[SET_MASTER ERROR] {e}")

    def save_master_settings_db(self):

        try:

            active_program_id = int(
                self.ui.valueObj.activeVariables_dict["ActiveProgramId"]
            )

            with SessionLocal() as session:

                # remove old entries
                session.query(SetMasterSettings).filter(
                    SetMasterSettings.ProgramId == active_program_id
                ).delete()

                # save latest master values
                for probe, data in self.probe_data.items():

                    row = SetMasterSettings(
                        ProgramId=active_program_id,
                        Dimension=probe,

                        MasterValue=data.get("converted_raw_value"),

                        SPI_low=data.get("SPI_low"),
                        SPI_high=data.get("SPI_high"),
                        RemovedPartValue=self.removed_parts.get(probe)
                    )

                    session.add(row)

                session.commit()

        except Exception as e:
            print(f"save_master_settings_db ERROR -> {e}")

    def on_master_finished(self, probe_data, removed_parts):
        grouping_enabled = (
            self.ui.valueObj.IOSettings_dict
            .get('MASTER_GROUPING', {})
            .get('Enable', '0')
        )

        # Initialize if not exists
        if not hasattr(self, "probe_data") or self.probe_data is None:
            self.probe_data = {}

        if not hasattr(self, "removed_parts") or self.removed_parts is None:
            self.removed_parts = {}

        if grouping_enabled == '1':
            # ✅ ONLY MERGE (DO NOT DELETE ANYTHING)
            self.probe_data.update(probe_data)
            self.removed_parts.update(removed_parts)

        else:
            # ✅ NON-GROUP MODE → FULL REPLACE
            self.probe_data = probe_data
            self.removed_parts = removed_parts

        self.master_ready = True
        self.formula_Cache = self.get_formula_bar()
        self.master_popup_shown = False
        savemasterOnDb = (
            self.ui.valueObj.IOSettings_dict
            .get('SAVE_MASTER_CALIBRATION', {})
            .get('Enable', 'OFF')
        )
        if savemasterOnDb == 'ON':
            self.save_master_settings_db()
        else:
            return
    
    def load_saved_master_settings(self):
        try:

            active_program_id = int(
                self.ui.valueObj.activeVariables_dict["ActiveProgramId"]
            )

            with SessionLocal() as session:

                rows = session.query(SetMasterSettings).filter(
                    SetMasterSettings.ProgramId == active_program_id
                ).all()

                if not rows:
                    self.master_ready = False
                    return

                self.probe_data = {}
                self.removed_parts = {}
                # load probe DB settings
                for row in rows:

                    probe_db = session.query(ProbeBasedSettings).filter(
                        ProbeBasedSettings.ProgramId == active_program_id,
                        ProbeBasedSettings.Dimension == row.Dimension
                    ).first()

                    if not probe_db:
                        continue
                    self.removed_parts[row.Dimension] = row.RemovedPartValue

                    self.probe_data[row.Dimension] = {
                        "DB_low": probe_db.MasterLower,
                        "DB_high": probe_db.MasterHigher,
                        "DB_master": probe_db.Master,
                        "method": probe_db.Method,
                        "USL": probe_db.UpperSpecificationLimit,
                        "LSL": probe_db.LowerSpecificationLimit,
                        "Master Type": probe_db.MasterType,
                        "Range": probe_db.Range,
                        "Nominal": probe_db.NominalValue,
                        "LeastCount": probe_db.LeastCount,
                        "SPI_low": row.SPI_low,
                        "SPI_high": row.SPI_high,
                        "converted_raw_value": row.MasterValue,
                        "master_ready": True
                    }

                self.master_ready = True

                print("Master auto-loaded successfully")

        except Exception as e:
            print(f"load_saved_master_settings ERROR -> {e}")
      
    # def smash(self,value, step):
    #     return round(round(value / step) * step,10) 
    def smash(self, value, least_count):
        try:
            if least_count and least_count > 0:
                return round(round(value / least_count) * least_count, 10)
            return value
        except Exception as e:
            print("[Apply LC ERROR]", e)
            return value
        
    def load_least_counts(self):
        """
        Load all least counts once and cache them.
        Avoids DB hit in loop → prevents hanging.
        """
        self.least_count_map = {}

        try:
            active_program_id = int(
                self.ui.valueObj.activeVariables_dict["ActiveProgramId"]
            )

            with SessionLocal() as session:
                rows = session.query(ProbeBasedSettings).filter(
                    ProbeBasedSettings.ProgramId == active_program_id
                ).all()

                for row in rows:
                    self.least_count_map[row.Dimension] = float(row.LeastCount or 0)
            # self.load_saved_master_settings()
        except Exception as e:
            print("[LC CACHE ERROR]", e)
            
    def get_lc_cached(self, probe):
        return self.least_count_map.get(probe, 0.0)
    
    def map_values(self,calculated_values, formula_list):
        try:
            '''this function maps the calculated master values to a,b,c,d 
            based on the formula list and returns the variable dict for 
            formula evaluation
            '''
            
            variables = {"a": 0, "b": 0, "c": 0, "d": 0}

            for i, item in enumerate(formula_list):
                if not item:
                    continue

                match = re.match(r'P([1-4])', item)
                if not match:
                    continue

                p_index = int(match.group(1)) - 1  # P1→0, P2→1...

                d_key = f"D{i+1}"  # index 0→D1
                if d_key not in calculated_values:
                    continue   # 🔥 SAFETY
            
                value = calculated_values.get(d_key, 0)

                variables["abcd"[p_index]] = value

            return variables
        except Exception as e:
            print(f"Error in map_values -> {e}")
            return {"a": 0, "b": 0, "c": 0, "d": 0}
    
    # from decimal import Decimal
    def format_by_leastcount(self,value, leastcount):
        decimals = abs(Decimal(str(leastcount)).as_tuple().exponent)
        return f"{value:.{decimals}f}"  
    
    def ok_notok_part_check(self):
        try:
            AUTOSENSE_TOLERANCE_RANGE = 20
            channel_count = self.ui.dial_indicator.channel_count
            font_size = "50pt" if channel_count == 1 else "45pt" if channel_count == 2 else "35pt"

            ps = self.ui.valueObj.ProgramSettings_dict.get("ProgramSpecificSettings", {})
            self.auto_save_duration = float(ps.get("AutoSave_Duration", 0.5))

            if not getattr(self, "master_ready", False):
                for label in self.status_labels.values():
                    label.setText("")
                return

            if self.ui.stacked.currentIndex() != 25:
                return

            current_time = time.time()
            calculated_values = {}

            # -------------------------------------------------
            # 1️⃣ MASTER CALCULATION (NO LC HERE)
            # -------------------------------------------------
            for probe, pdata in self.probe_data.items():

                spi_new = self.spi_values.get(probe)
                if spi_new is None:
                    continue

                calculated_master_value = (
                    pdata["DB_low"]
                    + (spi_new - pdata["SPI_low"]) * pdata["converted_raw_value"]
                )

                calculated_values[probe] = calculated_master_value

            # -------------------------------------------------
            # 2️⃣ FORMULA
            # -------------------------------------------------
            formula_list = self.formula_Cache

            if formula_list:
                variables = self.map_values(calculated_values, formula_list)

                a = variables["a"]
                b = variables["b"]
                c = variables["c"]
                d = variables["d"]

                formula_results = self.set_per_formula(a, b, c, d, formula_list)

                probes = ["D1", "D2", "D3", "D4"]

                for i, probe in enumerate(probes):
                    if i >= len(formula_list) or not formula_list[i]:
                        continue

                    result = formula_results[i]
                    if result is None:
                        continue

                    calculated_values[probe] = result

            # -------------------------------------------------
            # 3️⃣ FINAL LOOP (🔥 APPLY LC HERE ONLY)
            # -------------------------------------------------
            for probe, pdata in self.probe_data.items():

                raw_value = calculated_values.get(probe)
                if raw_value is None:
                    continue

                # ✅ APPLY LC HERE ONLY
                lc = self.get_lc_cached(probe)
                final_value = self.smash(raw_value, lc)

                label = self.probe_labels.get(probe)
                status_label = self.status_labels.get(probe)

                # -------------------------------
                # AUTOSENSE
                # -------------------------------
                autoSense_value = self.removed_parts.get(probe)
                spi_new = self.spi_values.get(probe)

                if autoSense_value is not None and spi_new is not None:
                    if abs(spi_new - autoSense_value) < AUTOSENSE_TOLERANCE_RANGE:

                        if label:
                            label.setText(self.format_by_leastcount(final_value, lc))
                            # label.setText(str(final_value))
                            label.setStyleSheet(
                                self.ui.dial_indicator.style_value +
                                f"color: white;font-size: {font_size};"
                            )

                        if status_label:
                            status_label.setText("")

                        self.last_status[probe] = ""
                        self.last_raw_status[probe] = None
                        self.status_stable_since[probe] = None
                        continue

                # -------------------------------
                # DISPLAY VALUE
                # -------------------------------
                if label:
                    label.setText(self.format_by_leastcount(final_value, lc))
                    # label.setText(str(final_value))

                # -------------------------------
                # STATUS
                # -------------------------------
                if pdata["method"] == "OD":
                    if pdata["USL"] < final_value:
                        raw_status = "REWORK"
                    elif pdata["LSL"] > final_value:
                        raw_status = "NOT OK"
                    else:
                        raw_status = "OK"

                elif pdata["method"] == "ID":
                    if pdata["USL"] < final_value:
                        raw_status = "NOT OK"
                    elif pdata["LSL"] > final_value:
                        raw_status = "REWORK"
                    else:
                        raw_status = "OK"
                else:
                    raw_status = ""

                # -------------------------------
                # STABILITY CHECK
                # -------------------------------
                if self.last_raw_status.get(probe) != raw_status:
                    self.last_raw_status[probe] = raw_status
                    self.status_stable_since[probe] = current_time
                    continue

                stable_since = self.status_stable_since.get(probe)

                if stable_since is None:
                    self.status_stable_since[probe] = current_time
                    continue

                if (current_time - stable_since) < self.auto_save_duration:
                    continue

                # -------------------------------
                # FINAL STATUS
                # -------------------------------
                status = raw_status
                self.last_status[probe] = status

                if status == "OK":
                    color = "green"
                elif status == "REWORK":
                    color = "yellow"
                elif status == "NOT OK":
                    color = "red"
                else:
                    color = "white"

                if status_label:
                    status_label.setText(status)
                    status_label.setStyleSheet(
                        self.ui.dial_indicator.style_status +
                        f"color: {color};font-size: {font_size};"
                    )

                if label:
                    label.setStyleSheet(
                        self.ui.dial_indicator.style_value +
                        f"color: {color};font-size: {font_size};"
                    )

            status_changed = False

            if not hasattr(self, "previous_status"):
                self.previous_status = {}

            for probe, status in self.last_status.items():
                if self.previous_status.get(probe) != status:
                    status_changed = True
                    break  # one change is enough

            # Save snapshot
            self.previous_status = self.last_status.copy()

            # -------------------------------------------------
            # RELAY (DIMENSION BASED ✅)
            # -------------------------------------------------
            if self.relay_state == '1' and self.last_status:

                relay_color = self.get_relay_color(self.last_status)

                # Init
                if not hasattr(self, "relay_triggered_for_cycle"):
                    self.relay_triggered_for_cycle = False

                # If ANY dimension changed → restart cycle
                if status_changed:
                    self.last_trigger_time = current_time
                    self.relay_triggered_for_cycle = False

                # Wait for stable delay
                if (current_time - self.last_trigger_time) >= self.auto_save_duration:

                    if not self.relay_triggered_for_cycle:
                        self.ui.relayController.trigger(relay_color, self.relay_value)

                        self.last_relay_color = relay_color
                        self.relay_triggered_for_cycle = True
        
            # self.Nomaster_label(calculated_values)

        except Exception as e:
            print(f"[OK_NOTOK ERROR] {e}")       
                   
                
    def get_relay_color(self, statuses_dict):
        try:

            ps = self.ui.valueObj.ProgramSettings_dict.get("ProgramSpecificSettings", {})
            mode = ps.get("Mode", "Individual")

            statuses = list(statuses_dict.values())

            ok = statuses.count("OK")
            notok = statuses.count("NOT OK")
            rework = statuses.count("REWORK")
            white = statuses.count("")

            total = len(statuses)

            # -------------------------------
            # 🔵 INDIVIDUAL MODE (NO CHANGE)
            # -------------------------------
            if mode == "Individual":
                # ⚪ All empty
                if white == total:
                    return "white"

                # ✅ ANY OK → GREEN (your main rule)
                elif ok >= 1:
                    return "green"

                # ❌ If no OK → check others
                elif notok >= 1:
                    return "red"

                elif rework >= 1:
                    return "yellow"

                
            # -------------------------------
            # 🔴 COMBINE MODE (UPDATED 🔥)
            # -------------------------------
            elif mode == "Combine":
                
                # ⚪ ANY WHITE
                if white >= 1:
                    return "white"

                # ❌ ANY NOT OK → RED (highest priority)
                elif notok >= 1:
                    return "red"

                # ⚠️ OK + REWORK → YELLOW
                elif ok >= 1 and rework >= 1:
                    return "yellow"

                # ⚠️ ONLY REWORK
                elif rework >= 1:
                    return "yellow"

                # ✅ ONLY OK
                elif ok >= 1:
                    return "green"

            return "white"
        except Exception as e :
            print(f"Error in get_realy_color function -> {e}")
    
            
    def Nomaster_label(self, calculated_values):
        try:
            AUTOSENSE_TOLERANCE_RANGE = 20            
            channel_count = self.ui.dial_indicator.channel_count
            font_size = "50pt" if channel_count == 1 else "45pt" if channel_count == 2 else "35pt"
            for probe, pdata in self.master_set.no_master_limits.items():

                final_value = calculated_values.get(probe)
                if final_value is None:
                    continue
                
                status_label = self.status_labels.get(probe)
                label = self.probe_labels.get(probe)
                # -------------------------------------------------
                # 🔥 AUTOSENSE CHECK (FIRST PRIORITY)
                # -------------------------------------------------
                autoSense_value = self.removed_parts.get(probe)
                spi_new = self.spi_values.get(probe)

                if autoSense_value is not None and spi_new is not None:
                    if abs(spi_new - autoSense_value) < AUTOSENSE_TOLERANCE_RANGE:

                        if label:
                            # label.setText(final_value)
                            label.setStyleSheet(
                                self.ui.dial_indicator.style_value + f"color: white;font-size: {font_size};"
                            )

                        if status_label:
                            status_label.setText("")

                        continue   # 🚀 skip normal status logic
                
                if pdata["method"] == "OD":
                    if pdata["USL"] < final_value:
                        status = "REWORK"
                    elif pdata["LSL"] > final_value:
                        status = "NOT OK"
                    else:
                        status = "OK"

                elif pdata["method"] == "ID":
                    if pdata["USL"] < final_value:
                        status = "NOT OK"
                    elif pdata["LSL"] > final_value:
                        status = "REWORK"
                    else:
                        status = "OK"

                if status_label:
                    status_label.setText(status)

                    if status == "OK":
                        color = "green"
                    elif status == "REWORK":
                        color = "yellow"
                    elif status == "NOT OK":
                        color = "red"
                    else:
                        color = "white"

                    status_label.setStyleSheet(
                        self.ui.dial_indicator.style_status + f"color: {color};font-size: {font_size};"
                    )

                    if label:
                        # label.setText(final_value)
                        label.setStyleSheet(
                            self.ui.dial_indicator.style_value + f"color: {color};font-size: {font_size};"
                        )
        except Exception as e:
            print(f"Error in Nomaster_label: {e}")
                
   
    def save_worker(self):
        while True:
            records = self.db_queue.get()
            try:
                self.ui.savedbObj.insert_probe_values(records)
            except Exception as e:
                print("DB Worker Error:", e)
                
    def autoSave_Handler(self):
        try:

            if getattr(self, "saving_in_progress", False):
                return

            self.save_probe_values()

        except Exception as e:
            print(f"Auto Save Error -> {e}")
            
    def save_probe_values(self):
        """Save live probe values into ProbeValues table"""
        try:
            # -------------------------------
            # MASTER CHECK
            # -------------------------------
            records = []
            if not getattr(self, "master_ready", False):
                # prevent repeated popup
                if not self.master_popup_shown:

                    self.master_popup_shown = True

                    CustomMessageBox(
                        "Master not set. Please complete Master setting first.",
                        "error",
                        parent=self.ui
                    ).exec_()

                return
            self.data.save_probe_unique_settings()

            program_dict = self.ui.valueObj.ProgramSettings_dict
            ps = program_dict.get("ProgramSpecificSettings", {})

            mode = ps.get("Mode", "Individual")
            mode_char = mode[0]
            

            channels = self.app.get_channels_for_program(
                int(self.ui.valueObj.activeVariables_dict["ActiveProgramId"])
            )

            # print("Active Channels ->", channels)

            # -------------------------------
            # COMBINE MODE VALIDATION
            # -------------------------------
            if mode == "Combine":

                for dim in channels:
                    status_label = self.status_labels.get(dim)

                    if not status_label:
                        continue

                    status_text = status_label.text().strip()

                    if status_text == "":
                        CustomMessageBox(
                            f"Status missing for {dim}. Cannot save in Combine mode.",
                            "error",
                            parent=self.ui
                        ).exec_()
                        return

            # -------------------------------
            # SAVE VALUES
            # -------------------------------
            for dim in channels:

                value_label = self.probe_labels.get(dim)
                status_label = self.status_labels.get(dim)

                if not value_label or not status_label:
                    continue

                value_text = value_label.text().strip()
                status_text = status_label.text().strip()

                if value_text == "":
                    continue
                # 🔴 INDIVIDUAL MODE RULE
                if mode == "Individual" and status_text == "":
                    continue
                try:
                    value = float(value_text)
                    formatted_value = value_text
                except ValueError:
                    continue
                
                # self.ui.spc_manager.worker.add_data(ch, value)
                probe_settings = program_dict.get(dim, {}).get("ProbeBasedSettings")

                if not probe_settings:
                    continue

                probe_id = probe_settings.get("ProbeId")

                if not probe_id:
                    continue
                
                ch = int(dim[1])
                # self.ui.spc_manager.update_value(ch, value)
                # spc_batch.append((ch, value))
                # print(
                #     f"SAVING -> {dim} | ProbeId:{probe_id} | "
                #     f"Value:{value} | Status:{status_text} | "
                #     f"GlobalCounter:{self.global_counter} | JobCount:{self.job_count}"
                # )

                # self.ui.savedbObj.insert_probe_values(
                #     probe_based_id=probe_id,
                #     global_counter=global_counter,
                #     mode=mode_char,
                #     job_count=job_count,
                #     value=value,
                #     status=status_text
                # )

                # ✅ STORE (NO DB YET)
                records.append((
                    probe_id,
                    self.global_counter,
                    mode_char,
                    self.job_count,
                    value,
                    status_text
                ))
                # saved_values.append((dim, value))

                # -------------------------------
                # INCREMENT GLOBAL COUNTER
                # -------------------------------
                self.global_counter += 1

            # self.ui.spc_manager.load_spc_values(saved_values)
                if self.ui.valueObj.activeVariables_dict["RS232OnOff"] == 'ON':
                    self.ui.serial_instance.send_data(str(dim) + ', ' + str(formatted_value) + ', ' + str(status_text) + ', ' + str(self.job_count) +'\n')
            if records:
                self.db_queue.put(records)
                self.job_count += 1
                self.save_completed.emit(True)
            else:
                self.save_completed.emit(False)
        except Exception as e:
            print(f"Error while saving Probe Values -> {e}")
            self.save_completed.emit(False)
    # def load_spc_values(self,saved_values):
    #     for dim,value in saved_values:
    #         if not dim:
    #             continue
    #         try:
    #             channel = int(dim[1])
    #         except:
    #             continue
    #         self.update_value(channel, value)
        
                 
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
            print("MainWindow destroyed, stopped.")
        except Exception as e:
            print(f"Error during MainWindow destruction: {e}")
