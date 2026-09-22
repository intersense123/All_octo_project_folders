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

# from dial_handler import DialHandler



# Handles continuous SPI emission for master-setting popups
class Worker(QObject):

    spi_generated = Signal(list)   # ✅ CHANGED
    finished = Signal()
    UI_UPDATE_INTERVAL_SECONDS = 1 / 60


    # Initialize SPI worker with factory configuration and probe sensitivity
    def __init__(self, factory_config,responsiveness,probe_sensitivity,parent=None):

        try:
            super().__init__(parent)
            self.factory_config = factory_config
            # self.responsiveness = responsiveness
            self._running = True
            self.spi = SPI(factory_config, responsiveness,probe_sensitivity)
            self._last_ui_emit = 0.0
            self._latest_ui_values = None
            self._ui_update_pending = False
            self._ui_update_lock = threading.Lock()
        except Exception as e:
            print(f"Error while initialization in worker thread -> {e}")

    @QtCore.Slot()
    def run(self):
        try:
            for value in self.spi.spi_value_emitter():
                if not self._running:
                    break

                # Keep acquisition at hardware speed, but do not flood the GUI
                # event queue with samples it cannot render. The newest sample is
                # delivered within one display frame (about 16 ms).
                now = time.monotonic()
                if now - self._last_ui_emit >= self.UI_UPDATE_INTERVAL_SECONDS:
                    str_values = list(map(str, value))[::-1]
                    should_emit = False
                    with self._ui_update_lock:
                        self._latest_ui_values = str_values
                        if not self._ui_update_pending:
                            self._ui_update_pending = True
                            should_emit = True

                    if should_emit:
                        self.spi_generated.emit(str_values)

                    self._last_ui_emit = now

        finally:
            self.cleanup()
    def update_responsiveness_probesens(self, responsiveness,probe_sensitivity = None):
        try:
            if hasattr(self, "spi") and self.spi:
                self.spi.update_responsiveness_probesens(
                    responsiveness,
                    probe_sensitivity
                )
        except Exception as e:
            print(f"update_responsiveness_probesens error: {e}")
    # Stop the worker loop safely
    def stop(self):
        try:
            self._running = False
        except Exception as e:
            print(f"Error in stop -> {e}")

    def get_latest_ui_values(self):
        with self._ui_update_lock:
            return self._latest_ui_values

    def acknowledge_ui_update(self):
        with self._ui_update_lock:
            self._ui_update_pending = False

    def cleanup(self):
        try:
            self.spi.close()
        except Exception:
            pass
        self.finished.emit()

class Set_master_ui(QtWidgets.QDialog):
    # Initialize the set-master dialog and its UI state
    def __init__(self,
                title_text,
                btn_text="OK",
                parent=None,
                db_values=None,
                mode=None,
                selected_probes=None,
                formula_list=None,
                formula_func=None):

        try:
            super().__init__(parent)

            self.db_values = db_values or {}
            self.mode = mode
            self.selected_probes = selected_probes or []
            self.formula_list = formula_list or []
            self.formula_func = formula_func

            self.result = None
            self.current_spi_map = {}

            # ------------------------------------------------------------------
            # Dialog (fullscreen overlay)
            # ------------------------------------------------------------------
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
                border: 2px solid #888888;
                border-radius:16px;
            }

            QLabel{
                color:white;
                font-size:16pt;
            }

            QPushButton{
                background:black;
                color:white;
                font-size:14pt;
                border-radius:5px;
                padding:10px 20px;
            }

            QPushButton:hover{
                background:black;
            }
            
            QPushButton:pressed {
                background-color: #222222;
                border: 3px solid #fec822;
            }
            """)

            # ------------------------------------------------------------------
            # Main panel
            # ------------------------------------------------------------------
            self.panel = QtWidgets.QWidget(self)
            self.panel.setObjectName("mainWidget")
            self.panel.setFixedSize(600, 320)

            

            self.close_btn = QPushButton("X")
            self.close_btn.setFixedSize(40, 40)
            self.close_btn.setStyleSheet("""
                QPushButton{
                    background:black;
                    color:white;
                    border-radius:15px;
                    padding:0px;
                }

                QPushButton:hover{
                    background:black;
                }
                
                QPushButton:pressed {
                    background-color: #222222;
                    border: 3px solid #fec822;
                }
            """)

            self.close_btn.clicked.connect(self.reject)

            title_layout = QHBoxLayout()
            # ------------------------------------------------------------------
            # Title
            # ------------------------------------------------------------------
            self.title_label = QLabel(title_text)
            self.title_label.setAlignment(Qt.AlignCenter)
            self.title_label.setFixedSize(530,60)
            self.title_label.setStyleSheet(
                "background:black;font-size:17pt;font-weight:bold;"
            )
            title_layout.addWidget(self.title_label)
            title_layout.addStretch()
            title_layout.addWidget(self.close_btn)

            # ------------------------------------------------------------------
            # Main text
            # ------------------------------------------------------------------
            self.main_label = QLabel()
            self.main_label.setAlignment(Qt.AlignCenter)
            self.main_label.setStyleSheet("""
                font-size:16pt;
                color:white;
                font-weight:bold;
                background:black;
            """)

            # ------------------------------------------------------------------
            # OK Button
            # ------------------------------------------------------------------
            self.btn = QPushButton(btn_text)
            self.btn.setFixedSize(140, 40)
            self.btn.clicked.connect(self.accept)

            self.btn_layout = QHBoxLayout()

            # ------------------------------------------------------------------
            # Panel Layout
            # ------------------------------------------------------------------
            layout = QVBoxLayout(self.panel)
            layout.addSpacing(5)
            layout.addLayout(title_layout)
            layout.addSpacing(5)
            layout.addWidget(self.main_label)
            layout.addSpacing(5)
            layout.addLayout(self.btn_layout)
            layout.addSpacing(5)
            # self.setLayout(layout)

            self.update_button_position()

    
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
        try:
            lines = []
            
            for probe in self.selected_probes:
                # if self.mode in ["high", "low"] and probe not in self.db_values:
                #     continue
                spi_val = self.current_spi_map.get(probe, "")
                if spi_val is None:
                    continue
                db_val = ""

                if self.mode == "high":
                    db_val = self.db_values.get(probe, {}).get("MasterHigher", "")
                    line = f"<b>{probe}</b> : {spi_val}    |     Higher Master : {db_val}"

                elif self.mode == "low":
                    db_val = self.db_values.get(probe, {}).get("MasterLower", "")
                    line = f"<b>{probe}</b> : {spi_val}     |    Lower Master : {db_val}"

                elif self.mode == "master":
                    db_val = self.db_values.get(probe, {}).get("Master", "")
                    line = f"<b>{probe}</b> : {spi_val}     |     Master : {db_val}"
                else:
                    # Remove Parts / no DB mode
                    line = f"<b>{probe}</b> : {spi_val}"

                    # Remove Parts popup
                    # line = f"<b>{probe}</b> : {spi_val}"

                lines.append(line)

            self.main_label.setText(
                "<div style='line-height: 1.8;'>"
                + "<br>".join(lines) +
                "</div>"
            )
        except Exception as e:
            print(f"Error in _referesh_combine_display ->",e)
            
    def update_button_position(self):
        try:
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
        except Exception as e:
            print(f"Error in update_button_position -> {e}")   
            
            
    def showEvent(self, event):
        try:
            super().showEvent(event)

            if self.parent():
                self.setGeometry(self.parent().rect())
            else:
                self.setGeometry(QtWidgets.QApplication.primaryScreen().geometry())

            self.panel.move(
                (self.width() - self.panel.width()) // 2,
                (self.height() - self.panel.height()) // 2
            )       
        except Exception as e:
            print(f"Error in showEvent -> {e}")
            
    # Center the popup panel when the dialog is shown
    def showEvent(self, event):
        try:
            super().showEvent(event)

            if self.parent():
                self.setGeometry(self.parent().rect())
            else:
                self.setGeometry(QtWidgets.QApplication.primaryScreen().geometry())

            self.panel.move(
                (self.width() - self.panel.width()) // 2,
                (self.height() - self.panel.height()) // 2
            )
        except Exception as e:
            print(f"Error in showEvent -> {e}")
            
class SetMasterController(QObject):
    """
    Handles Set Master workflow and master calculations.
    """
    master_finished = Signal(dict,dict)   # Emits probe_data dict

    def __init__(self, parent, spi_values,spi_signal,grouped_channels=None,
                formula_list=None,
                formula_func=None,
                single_master_low_spi=None,
                single_master_high_spi=None,
                single_master_low_value=None,
                single_master_high_value=None
                ):
        try:
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
            self.master_val = {}
            self.probe_data = {}
            self.raw_range = 0
            self.probe = None
        
            self.no_master_limits = {}
            self.single_master_low_spi = single_master_low_spi or {}
            self.single_master_high_spi = single_master_high_spi or {}

            self.single_master_low_value = single_master_low_value or {}
            self.single_master_high_value = single_master_high_value or {}
            self.single_master_converted_raw_value = {}
            self.single_master_masterSpi = {}
            self.single_master_master_spi = self.single_master_masterSpi
            self.load_single_master_calibration_db()
        except Exception as e:
            print(f"Error in init of setmasterController -> {e}")
            
    # Load probe calibration values from the database for a given probe
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

    def check_autosense_conflict(self, active_channels,single_master=False):
        try:
            TOL = 10

            for probe in active_channels:   # 🔥 ONLY ACTIVE

                auto = self.removed_parts.get(probe)
                if auto is None:
                    continue

                auto = float(auto)

                if single_master:

                    master_spi = self.single_master_masterSpi.get(probe)

                    if master_spi is not None:

                        diff_master = abs(auto - float(master_spi))

                        if diff_master <= TOL:
                            return False, f"{probe}: Auto near MASTER"

                else:

                    high = self.master_high.get(probe)
                    low = self.master_low.get(probe)

                    if high is not None:

                        diff_high = abs(auto - float(high))

                        if diff_high <= TOL:
                            return False, f"{probe}: Auto within {TOL} of HIGH"

                    if low is not None:

                        diff_low = abs(auto - float(low))

                        if diff_low <= TOL:
                            return False, f"{probe}: Auto within {TOL} of LOW"

            return True, None

        except Exception as e:
            return False, f"AutoSense check failed: {e}"
    def load_single_master_calibration_db(self):
        try:
            active_program_id = int(
                self.ui_parent.valueObj.activeVariables_dict["ActiveProgramId"]
            )

            with SessionLocal() as session:

                conversion_rows = session.query(SingleMasterCalibration).filter(
                    SingleMasterCalibration.ProgramId == active_program_id
                ).all()

                for calibration in conversion_rows:
                    if calibration.ConvertedRawValue is not None:
                        probe = self.normalize_calibration_probe(
                            calibration.Probe
                        )
                        self.single_master_converted_raw_value[
                            probe
                        ] = calibration.ConvertedRawValue

                rows = session.query(SetMasterSettings).filter(
                    SetMasterSettings.ProgramId == active_program_id
                ).all()

                if not rows:
                    print(
                        f"[SINGLE MASTER] No saved calibration for "
                        f"ProgramId={active_program_id}"
                    )
                    return False

                for row in rows:

                    probe = row.Dimension

                    # -----------------------------------------
                    # ONLY LOAD IF FACTORY DB CALIBRATION EXISTS
                    # -----------------------------------------
                    if row.DB_low is None or row.DB_high is None:
                        continue

                    if row.SPI_low is None or row.SPI_high is None:
                        continue

                    self.single_master_low_spi[probe] = row.SPI_low
                    self.single_master_high_spi[probe] = row.SPI_high

                    self.single_master_low_value[probe] = row.DB_low
                    self.single_master_high_value[probe] = row.DB_high

                    print(
                        f"[SINGLE MASTER LOADED] {probe} | "
                        f"SPI_LOW={row.SPI_low} | "
                        f"SPI_HIGH={row.SPI_high} | "
                        f"DB_LOW={row.DB_low} | "
                        f"DB_HIGH={row.DB_high}"
                    )

                return True

        except Exception as e:
            print(f"load_single_master_calibration_db ERROR -> {e}")
            return False

    @staticmethod
    def normalize_calibration_probe(probe):
        probe = str(probe or "").strip().upper()
        if probe.startswith("D") and probe[1:].isdigit():
            return f"P{probe[1:]}"
        return probe

    def get_calibration_probe(self, row):
        """Return the physical probe referenced by a dimension formula."""
        formula = str(getattr(row, "Formula", "") or "")
        match = re.search(r"\bP[1-8]\b", formula.upper())
        if match:
            return self.normalize_calibration_probe(match.group(0))

        dimension = str(getattr(row, "Dimension", "") or "").upper()
        return self.normalize_calibration_probe(dimension)

    def get_calibration_dimension(self, row):
        """Return the SPI dimension that stores this row's probe calibration."""
        calibration_probe = self.get_calibration_probe(row)
        if calibration_probe.startswith("P") and calibration_probe[1:].isdigit():
            return f"D{calibration_probe[1:]}"
        return row.Dimension

    def get_saved_calibration(self, program_id, probe):
        """Load a saved single-master factor by physical probe identity."""
        probe = self.normalize_calibration_probe(probe)
        cached_value = self.single_master_converted_raw_value.get(probe)
        if cached_value is not None:
            return cached_value

        with SessionLocal() as session:
            rows = session.query(SingleMasterCalibration).filter(
                SingleMasterCalibration.ProgramId == program_id
            ).all()

            for calibration in rows:
                if (
                    self.normalize_calibration_probe(calibration.Probe)
                    == probe
                    and calibration.ConvertedRawValue is not None
                ):
                    value = calibration.ConvertedRawValue
                    self.single_master_converted_raw_value[probe] = value
                    return value

        return None

            
    def run(self):
        """
        Runs high master, low master, and calculation sequence.
        """
        try:
            # Clear old program data
            self.removed_parts.clear()
            self.master_low.clear()
            self.master_high.clear()
            self.probe_data.clear()
            self.single_master_masterSpi = {}
            self.single_master_master_spi = self.single_master_masterSpi
            active_program_id = int(
                self.ui_parent.valueObj.activeVariables_dict["ActiveProgramId"]
            )


            with SessionLocal() as session:

                rows = session.query(ProbeBasedSettings).filter(
                    ProbeBasedSettings.ProgramId == active_program_id
                ).all()

                for row in rows:

                    if row.MasterType == "Single Master":
                        single_master_found = True
                        break
                    
            # 1️⃣ Check MASTER_GROUPING enable
            current = (
                self.ui_parent.valueObj.IOSettings_dict
                .get('MASTER_GROUPING', {})
                .get('Enable', '0')
            )

            active_program_id = int(
                self.ui_parent.valueObj.activeVariables_dict["ActiveProgramId"]
            )

            with SessionLocal() as session:
                rows = session.query(ProbeBasedSettings).filter(
                    ProbeBasedSettings.ProgramId == active_program_id
                ).all()
            
            for row in rows:
                probe = row.Dimension
                # print(f"Probe: {probe}, MasterType: {row.MasterType}")
                # 🔴 SKIP NO MASTER PROBES
                if row.MasterType == "Single Master":
                    # ----------------------------------------
                    # GROUPING LOGIC
                    # ----------------------------------------
                    if current == '1':

                        selected_probes = self.grouped_channels

                        if probe not in selected_probes:
                            continue

                    else:
                        selected_probes = [probe]

                    # ---------------- REMOVE PART ----------------

                    remove_parts = Set_master_ui(
                        "Remove parts from fixture",
                        "Next",
                        parent=self.ui_parent,
                        selected_probes=selected_probes,
                        formula_list=self.formula_list,
                        formula_func=self.formula_func
                    )

                    self.spi_signal.connect(remove_parts.update_spi_value)

                    result = remove_parts.exec_()
                    
                    self.spi_signal.disconnect(remove_parts.update_spi_value)

                    if result == QDialog.Rejected:
                        self.ui_parent.status_manager.show(
                        page_index=28,
                        message=f"Master Setup Closed for {', '.join(selected_probes)}",
                        timeout=5000,
                        msg_type="success"
                        )
                        return

                    # ----------------------------------------
                    # STORE REMOVE VALUES
                    # ----------------------------------------
                    for p in selected_probes:
                        self.removed_parts[p] = self.spi_values.get(p)

                    # ---------------- SET MASTER ----------------
                    # Get DB master values for selected probes
                    master_db_values = {}

                    for probe in selected_probes:
                        probe_db = self.get_probe_db_values(probe)
                        if probe_db:
                            master_db_values[probe] = probe_db
                    set_master_popup = Set_master_ui(
                        "Set Master",
                        "OK",
                        parent=self.ui_parent,
                        db_values=master_db_values,
                        mode="master",
                        selected_probes=selected_probes,
                        formula_list=self.formula_list,
                        formula_func=self.formula_func
                    )

                    # set_master_popup = Set_master_ui(
                    #     "Set Master",
                    #     "OK",
                    #     parent=self.ui_parent,
                    #     selected_probes=selected_probes,
                    #     formula_list=self.formula_list,
                    #     formula_func=self.formula_func
                    # )
                    
                    self.spi_signal.connect(set_master_popup.update_spi_value)

                    result = set_master_popup.exec_()
                    

                    self.spi_signal.disconnect(set_master_popup.update_spi_value)

                    if result == QDialog.Rejected:
                        self.ui_parent.status_manager.show(
                        page_index=28,
                        message=f"Master Setup Closed for {', '.join(selected_probes)}",
                        timeout=5000,
                        msg_type="error"
                        )
                        return
                    for p in selected_probes:
                        master_spi = self.spi_values.get(p)

                        if master_spi is not None:
                            self.single_master_masterSpi[p] = master_spi
                    # ----------------------------------------
                    # STORE LOW/HIGH USING spi_values
                    # ----------------------------------------
                    for p in selected_probes:

                        calibration_dimension = self.get_calibration_dimension(row)
                        low_spi = self.single_master_low_spi.get(
                            calibration_dimension
                        )
                        high_spi = self.single_master_high_spi.get(
                            calibration_dimension
                        )

                        if low_spi is None or high_spi is None:

                            popup_fail = Set_master_ui(
                                "Please calibrate LOW and HIGH master",
                                "Close",
                                parent=self.ui_parent
                            )

                            popup_fail.exec_()
                            self.ui_parent.status_manager.show(
                                page_index=28,
                                message=f"Please calibrate LOW and HIGH master",
                                timeout=5000,
                                msg_type="error"
                            )
                            return

                        self.master_low[p] = low_spi
                        self.master_high[p] = high_spi
                    # 🔥 ADD AUTOSENSE VALIDATION HERE
                    ok, msg = self.check_autosense_conflict(selected_probes,single_master=True)

                    if not ok:

                        popup_error = Set_master_ui(
                            "First Step Failed, Set Master Again.",
                            "Close",
                            parent=self.ui_parent
                        )

                        popup_error.exec_()
                        self.ui_parent.status_manager.show(
                            page_index=28,
                            message=f"First step Failed,Set master Again",
                            timeout=0,
                            msg_type="error"
                        )
                        return
                    # ----------------------------------------
                    # CURRENT ROW VALUES
                    # ----------------------------------------
                    calibration_dimension = self.get_calibration_dimension(row)
                    row.MasterLower = self.single_master_low_value.get(
                        calibration_dimension
                    )
                    row.MasterHigher = self.single_master_high_value.get(
                        calibration_dimension
                    )

                    success, error_msg = self.calculate_single_master(row)

                    if not success:

                        popup_fail = Set_master_ui(
                            "Master Set Unsuccessful.",
                            "Close",
                            parent=self.ui_parent
                        )

                        popup_fail.exec_()
                        self.ui_parent.status_manager.show(
                            page_index=28,
                            message=f"Master dosn't set Successful for {', '.join(selected_probes)}",
                            timeout=0,
                            msg_type="error"
                        )
                        return

                    popup_ok = Set_master_ui(
                        "Master Set Successfully",
                        "Close",
                        parent=self.ui_parent
                    )
                    
                    popup_ok.exec_()
                    self.ui_parent.status_manager.show(
                        page_index=28,
                        message=f"Single Master Set Successful for {', '.join(selected_probes)}",
                        timeout=0,
                        msg_type="success"
                    )
                    self.master_finished.emit(
                        self.probe_data,
                        self.removed_parts
                    )

                    return

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
                        self.ui_parent.status_manager.show(
                        page_index=28,
                        message=f"Master Setup Closed for {', '.join(Active_channels)}",
                        timeout=5000,
                        msg_type="success"
                        )
                        return
                    # Store remove Values
                    for probe in Active_channels:
                        spi = self.spi_values.get(probe)
                        if spi is not None:
                            self.removed_parts[probe] = spi
                    # for probe, spi in self.spi_values.items():
                    #     self.removed_parts[probe] = spi
                        # print(f"Removed {probe}: {spi}")
                    
                    # ---------- LOW MASTER ----------
                    # Get DB values for all probes to display
                    db_values_low = {}
                    for probe in Active_channels:
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
                        self.ui_parent.status_manager.show(
                        page_index=28,
                        message=f"Master Setup Closed for {', '.join(Active_channels)}",
                        timeout=5000,
                        msg_type="success"
                        )
                        return
                    self.spi_signal.disconnect(lower_master_raw_val.update_spi_value)

                    # Store LOW master values
                    for probe in Active_channels:
                        spi = self.spi_values.get(probe)
                        if spi is not None:
                            self.master_low[probe] = spi
                    # for probe, spi in self.spi_values.items():
                    #     self.master_low[probe] = spi
                        
                    # ---------- HIGH MASTER ----------
                    # Get DB values for all probes to display
                    db_values_high = {}
                    for probe in Active_channels:
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
                        self.ui_parent.status_manager.show(
                        page_index=28,
                        message=f"Master Setup Closed for {', '.join(Active_channels)}",
                        timeout=5000,
                        msg_type="success"
                        )
                        return
                    # 🔴 DISCONNECT AFTER CLOSE
                    self.spi_signal.disconnect(higher_master_raw_val.update_spi_value)
                    # Store HIGH master values
                    for probe in Active_channels:
                        spi = self.spi_values.get(probe)
                        if spi is not None:
                            self.master_high[probe] = spi
                    # for probe, spi in self.spi_values.items():
                    #     self.master_high[probe] = spi

                    # 🔥 NEW VALIDATION
                    ok, msg = self.check_autosense_conflict(Active_channels)

                    if not ok:
                        popup_error = Set_master_ui(
                            f"First Step Failed,Set Master Again.",
                            "Close",
                            parent=self.ui_parent
                        )
                        popup_error.exec_()
                        self.ui_parent.status_manager.show(
                        page_index=28,
                        message=f"First Step Failed , Set Master Again for {', '.join(Active_channels)}",
                        timeout=0,
                        msg_type="error"
                        )
                        return

                    success, error_msg = self.calculate()

                    if not success:
                        popup_fail = Set_master_ui(
                            f"Master Set Unsuccessful.",
                            "Close",
                            parent=self.ui_parent
                        )
                        popup_fail.exec_()
                        self.ui_parent.status_manager.show(
                        page_index=28,
                        message=f"Master dosn't set Successful for {', '.join(Active_channels)}",
                        timeout=0,
                        msg_type="error"
                        )
                        return

                    # ---------- CALCULATION ----------
                    self.calculate()
                    popup_res = Set_master_ui("Master Set Successfully", "Close", parent=self.ui_parent)
                    popup_res.exec_()      
                    self.ui_parent.status_manager.show(
                        page_index=28,
                        message=f"Master Set Successful for {', '.join(Active_channels)}",
                        timeout=0,
                        msg_type="success"
                    )              
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
                        self.ui_parent.status_manager.show(
                        page_index=28,
                        message=f"Master Setup Closed for {', '.join(self.grouped_channels)}",
                        timeout=5000,
                        msg_type="success"
                        )
                        return
                    self.spi_signal.disconnect(remove_parts.update_spi_value)
                    
                    # Store remove values
                    for probe in self.grouped_channels:
                        spi = self.spi_values.get(probe)
                        if spi is not None:
                            self.removed_parts[probe] = spi
                    # for probe, spi in self.spi_values.items():
                    #     self.removed_parts[probe] = spi
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
                        self.ui_parent.status_manager.show(
                        page_index=28,
                        message=f"Master Setup Closed for {', '.join(self.grouped_channels)}",
                        timeout=5000,
                        msg_type="success"
                        )
                        return
                    self.spi_signal.disconnect(lower_master_raw_val.update_spi_value)

                    # for probe, spi in self.spi_values.items():
                    #     if probe in self.grouped_channels:
                    #         self.master_low[probe] = spi
                    for probe in self.grouped_channels:
                        spi = self.spi_values.get(probe)
                        if spi is not None:
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
                        self.ui_parent.status_manager.show(
                        page_index=28,
                        message=f"Master Setup Closed for {', '.join(self.grouped_channels)}",
                        timeout=5000,
                        msg_type="success"
                        )
                        return
                    self.spi_signal.disconnect(higher_master_raw_val.update_spi_value)

                    # for probe, spi in self.spi_values.items():
                    #     if probe in self.grouped_channels:
                    #         self.master_high[probe] = spi
                    for probe in self.grouped_channels:
                        spi = self.spi_values.get(probe)
                        if spi is not None:
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
                        self.ui_parent.status_manager.show(
                        page_index=28,
                        message=f"First Step Failed,Set Master Again for {', '.join(self.grouped_channels)}",
                        timeout=0,
                        msg_type="error"
                        )
                        return
                    
                    success, error_msg = self.calculate()

                    if not success:
                        popup_fail = Set_master_ui(
                            f"Master Set Unsuccessful.",
                            "Close",
                            parent=self.ui_parent
                        )
                        popup_fail.exec_()
                        self.ui_parent.status_manager.show(
                        page_index=28,
                        message=f"Master dosn't set Successful for {', '.join(self.grouped_channels)}",
                        timeout=0,
                        msg_type="error"
                        )
                        return


                    # ---------- CALCULATION ----------
                    self.calculate()
                    popup_res = Set_master_ui("Master Set Successfully", "Close", parent=self.ui_parent)
                    popup_res.exec_()
                    self.ui_parent.status_manager.show(
                    page_index=28,
                    message=f"Master Set Successful for {', '.join(self.grouped_channels)}",
                    timeout=0,
                    msg_type="success"
                    )
                    self.master_finished.emit(self.probe_data,self.removed_parts)
                
        except Exception as e:
            print(f"[SetMasterController.run ERROR] {e}")
            
    def calculate_single_master(self, row):
        try:

            probe = row.Dimension
            calibration_dimension = self.get_calibration_dimension(row)

            spi_low = self.single_master_low_spi.get(calibration_dimension)
            spi_high = self.single_master_high_spi.get(calibration_dimension)
            spi_master = self.single_master_masterSpi.get(probe)
            if spi_low is None or spi_high is None or spi_master is None:
                return False, "LOW/HIGH/MASTER SPI missing"

            raw_range = spi_high - spi_low

            if raw_range == 0:
                return False, "RAW RANGE ZERO"

            DB_low = self.single_master_low_value.get(calibration_dimension)
            DB_high = self.single_master_high_value.get(calibration_dimension)
            
            calibration_probe = self.get_calibration_probe(row)
            active_program_id = int(
                self.ui_parent.valueObj.activeVariables_dict["ActiveProgramId"]
            )
            converted_raw_value = self.get_saved_calibration(
                active_program_id,
                calibration_probe
            )
            if converted_raw_value is None and calibration_probe != probe:
                converted_raw_value = self.get_saved_calibration(
                    active_program_id,
                    probe
                )
            conversion_loaded = converted_raw_value is not None
            if not conversion_loaded:
                converted_raw_value = (DB_high - DB_low) / raw_range

            # -----------------------------------
            # VALIDATION
            # -----------------------------------
            program_specific_settings = (
                self.ui_parent.valueObj.ProgramSettings_dict
                .get('ProgramSpecificSettings', {})
            )

            if program_specific_settings.get("Uom") == 'inch' and not conversion_loaded:
                converted_raw_value *= 25.4
                
            if row.Method == "OD" and converted_raw_value < 0:
                return False, "OD FAILED"

            if row.Method == "ID" and converted_raw_value > 0:
                return False, "ID FAILED"
            # print("spi_low =", spi_low)
            # print("spi_high =", spi_high)
            # print("raw_range =", raw_range)

            # print("DB_low =", DB_low)
            # print("DB_high =", DB_high)

            # print("converted_raw_value =", converted_raw_value)
            # -----------------------------------
            # STORE PROBE DATA
            # -----------------------------------
            self.probe_data[probe] = {

                "DB_low": DB_low,
                "DB_high": DB_high,

                "DB_master": row.Master,

                "method": row.Method,

                "USL": row.UpperSpecificationLimit,
                "LSL": row.LowerSpecificationLimit,

                "Master Type": row.MasterType,

                "Range": row.Range,
                "Nominal": row.NominalValue,
                "LeastCount": row.LeastCount,

                "SPI_low": spi_low,
                "SPI_high": spi_high,
                "SPI_master": spi_master,
                "converted_raw_value": converted_raw_value,

                "master_ready": True
            }

            self.save_single_master_runtime_calibration(row, converted_raw_value)

            return True, ""

        except Exception as e:
            print(f"[calculate_single_master ERROR] {e}")
            return False, str(e)

    def save_single_master_runtime_calibration(self, row, converted_raw_value):
        try:
            active_program_id = int(
                self.ui_parent.valueObj.activeVariables_dict["ActiveProgramId"]
            )
            dimension = self.get_calibration_dimension(row)
            probe = self.get_calibration_probe(row)

            with SessionLocal() as session:
                calibration = session.query(SingleMasterCalibration).filter(
                    SingleMasterCalibration.ProgramId == active_program_id,
                    SingleMasterCalibration.Probe == probe,
                    SingleMasterCalibration.Dimension == dimension
                ).first()

                if calibration is None:
                    calibration = SingleMasterCalibration(
                        ProgramId=active_program_id,
                        Probe=probe,
                        Dimension=dimension
                    )
                    session.add(calibration)

                calibration.ConvertedRawValue = converted_raw_value
                session.commit()

            self.single_master_converted_raw_value[probe] = converted_raw_value
            self.single_master_converted_raw_value[dimension] = converted_raw_value

        except Exception as e:
            print(f"save_single_master_runtime_calibration ERROR -> {e}")
    

    #double master calculation function  
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
                # if program_specific_settings.get("Uom") == 'inch':
                    
                #     inch_value = calculated_value #* 25.4
                #     # 🔴 VALIDATION LOGIC
                #     if row.Method == "OD" and inch_value < 0:
                #         failed_probes.append(f"{probe} ")
                #         continue
                #         # return False, f"{probe}"

                #     if row.Method == "ID" and inch_value > 0:
                #         failed_probes.append(f"{probe} ")
                #         continue

                #     self.probe_data[probe] = {
                #         "DB_low": DB_low,
                #         "DB_high": DB_high,
                #         "DB_master": row.Master,
                #         "method": row.Method,
                #         "USL": row.UpperSpecificationLimit,
                #         "LSL": row.LowerSpecificationLimit,
                #         "Master Type":row.MasterType,
                #         "Range": Dial_range,
                #         "Nominal": Nominal,
                #         "LeastCount":row.LeastCount,
                #         "SPI_low": spi_low,
                #         "SPI_high": spi_high,
                #         "converted_raw_value": inch_value,
                #         "master_ready": True
                #     }
                    
                if program_specific_settings.get("Uom") == 'mm' or program_specific_settings.get("Uom") == 'inch':
                    value = calculated_value 
                
                    # 🔴 VALIDATION LOGIC
                    if row.Method == "OD" and value < 0:
                        failed_probes.append(f"{probe} ")
                        continue

                    if row.Method == "ID" and value > 0:
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
                        "SPI_master": None,
                        "converted_raw_value": value,
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
    SPI_RAW_MIN = 28887
    SPI_RAW_MAX = 29250
    SPI_MM_MIN = 20.589
    SPI_MM_MAX = 20.611
    DISPLAY_MM_MIN = 0.0
    DISPLAY_MM_MAX = 2.0
    NO_PROBE_MM_THRESHOLD = 1.900

    save_completed = Signal(bool) 
    probe_value_ready_for_cnc = Signal(int, str, float)  # program_id, dimension, value
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
            self.raw_spi_values  = {}
            self.master_low = {}
            self.master_high = {}
            self.removed_parts = {}
            self.changed_probes = {}
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
            self.update_auto_save()
            self.current_measurements = {}
            self.previous_measurements = {}
            self.last_saved_measurements = {}
            self.last_measurement_change_time = time.time()
            self.measurement_changed_since_save = False
            self.last_saved_status = {}
            self.single_master_low_spi = {}
            self.single_master_high_spi = {}
            self.single_master_low_value = {}
            self.single_master_high_value = {}
            self.master_popup_shown = False
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
                    self.update_auto_save(),
                )
            )
            # self.data.io_settings_saved.connect(self.relay_handler)
            self.data.probe_setttings_saved.connect(lambda:(self.load_least_counts(),
                                                            self.update_auto_save()))
            # self.app.dimension_deleted.connect(self.refresh_settings)
            self.app.dimension_cache_status_deleted.connect(self.dimension_cache_status_clear)
            self.app.program_deleted_clear_caches.connect(self.program_cache_status_clear)
            self.global_counter = self.ui.savedbObj.get_next_global_counter()
            self.job_count = self.ui.savedbObj.get_job_counts()
            savemasterOnDb = (
                self.ui.valueObj.IOSettings_dict
                .get('SAVE_MASTER_CALIBRATION', {})
                .get('Enable', 'OFF')
            )

            if savemasterOnDb == 'ON':
                self.load_saved_master_settings()
            else:
                self.probe_data = {}
                self.removed_parts = {}
                self.master_ready = False
            self.ui.button_calibrateLower.clicked.connect(
                self.calibrate_lower_clicked
            )

            self.ui.button_calibrateHigher.clicked.connect(
                self.calibrate_higher_clicked
            )
            self.data.program_deleted.connect(self.refresh_settings)
            self.data.load_program.connect(self.refresh_settings)
            self.ui.comboBox_probeCalibrate.currentTextChanged.connect(
                self.update_probe_raw_label
            )
        except Exception as e:
            print(f"Error in init of SPIcontroller: {e}")
    def update_probe_raw_label(self):
        try:
            index = self.ui.comboBox_probeCalibrate.currentIndex()

            probes = ["D1", "D2", "D3", "D4"]

            if 0 <= index < len(probes):
                d_key = probes[index]
                raw = self.raw_spi_values.get(d_key, "")
                self.ui.label_proberawval.setText(str(raw))
            else:
                self.ui.label_proberawval.clear()

        except Exception as e:
            print(f"update_probe_raw_label -> {e}")
    def program_cache_status_clear(self,program_id):
        # Clear old cache first
        self.load_saved_master_settings()
        channels = self.app.get_channels_for_program(program_id)

        for dim in channels:
            self.dimension_cache_status_clear(dim)  
        self.load_least_counts()     
        
    def dimension_cache_status_clear(self, dimension):
        try:
            self.refresh_settings()
            # self.load_saved_master_settings()
            # Clear only deleted dimension
            # Clear old cache first
            self.status_labels[dimension].clear()
            self.load_least_counts() 
        except Exception as e:
            print(f"Error in dimension_cache_status_clear: {e}")
        
    ###### SINGLE MASTER CAlIBRATION LOGIC ###############################
    def calibrate_lower_clicked(self):
        try :
            probe = self.ui.comboBox_probeCalibrate.currentText()
            btn = self.ui.button_calibrateLower

            # # toggle border
            # if "border" in btn.styleSheet():

            #     btn.setStyleSheet("")

            # else:

            #     btn.setStyleSheet("""
            #         QPushButton{
            #             border: 2px solid #fec822;
            #         }
            #     """)

            self.capture_single_master_spi(probe, "low")
            
        except Exception as e:
            print(f"Error in calibrate lower clicked: {e}")
            
    
    def calibrate_higher_clicked(self):
        try:
            probe = self.ui.comboBox_probeCalibrate.currentText()
            btn = self.ui.button_calibrateHigher

            # # toggle border
            # if "border" in btn.styleSheet():

            #     btn.setStyleSheet("")

            # else:

            #     btn.setStyleSheet("""
            #         QPushButton{
            #             border: 2px solid #fec822;
            #         }
            #     """)

            self.capture_single_master_spi(probe, "high")
           
        except Exception as e:
            print(f"Error in calibrate higher clicked: {e}")
            
            
    def capture_single_master_spi(self, probe, mode):
        """
        mode = low / high
        """
        try:
            
            d_key = self.get_dimension_from_probe(probe)
            if not d_key:
                return

            spi = self.spi_values.get(d_key)
            print("probe =", probe)
            print("spi_values =", self.spi_values)
            if spi is None:
                return
            
            if mode == "low":
                # for probe, spi in self.spi_values.items():
                #     self.single_master_low_spi[probe] = spi
                self.single_master_low_spi[d_key] = spi
                
                low_val = float(
                    self.ui.lineEdit_lowerMasterCalibrate.text()
                )

                self.single_master_low_value[d_key] = low_val
                print(f"[SINGLE LOW] {d_key} SPI={spi} VALUE={low_val}")
                self.ui.status_manager.show(
                    page_index=19,
                    message= f"Lower Calibration for {probe} Completed",
                    timeout=5000,
                    msg_type="success"
                )

            elif mode == "high":
                # for probe, spi in self.spi_values.items():
                #     self.single_master_high_spi[probe] = spi
                self.single_master_high_spi[d_key] = spi
                high_spi = self.single_master_high_spi[d_key]
                high_val = float(
                    self.ui.lineEdit_higherMasterCalibrate.text()
                )

                self.single_master_high_value[d_key] = high_val
                low_spi = self.single_master_low_spi.get(d_key)
                if low_spi is not None and low_spi == high_spi:
                    self.ui.status_manager.show(
                        page_index=19,
                        message=f"{probe}: Lower and Higher SPI cannot be same",
                        timeout=5000,
                        msg_type="error"
                    )
                    return
                print(f"[SINGLE HIGH] {d_key} SPI={spi} VALUE={high_val}")
                self.ui.status_manager.show(
                    page_index=19,
                    message= f"Higher Calibration for {probe} Completed",
                    timeout=5000,
                    msg_type="success"
                )
                self.save_single_master_calibration_db(d_key)
        except Exception as e:
            print(f"[capture_single_master_spi ERROR] {e}")
            self.ui.status_manager.show(
                    page_index=19,
                    message="Please check inputs and try again.",
                    timeout=5000,
                    msg_type="error",
                )
    def save_single_master_calibration_db(self, probe):
            try:
                active_program_id = int(
                    self.ui.valueObj.activeVariables_dict["ActiveProgramId"]
                )
    
                spi_low = self.single_master_low_spi.get(probe)
                spi_high = self.single_master_high_spi.get(probe)
    
                db_low = self.single_master_low_value.get(probe)
                db_high = self.single_master_high_value.get(probe)
    
                # conversion_factor = self.single_master_conversion_factor.get(probe)
    
                if spi_low is None or spi_high is None:
                    print(f"[FACTORY CAL] {probe}: SPI LOW/HIGH missing")
                    return False
    
                # if conversion_factor is None:
                #     print(f"[FACTORY CAL] {probe}: conversion factor missing")
                #     return False
    
                with SessionLocal() as session:
    
                    row = session.query(SetMasterSettings).filter(
                        SetMasterSettings.ProgramId == active_program_id,
                        SetMasterSettings.Dimension == probe
                    ).first()
    
                    if row is None:
                        row = SetMasterSettings(
                            ProgramId=active_program_id,
                            Dimension=probe
                        )
                        session.add(row)
    
                    # ALWAYS SAVE FACTORY CALIBRATION
                    row.SPI_low = spi_low
                    row.SPI_high = spi_high
    
                    row.DB_low = db_low
                    row.DB_high = db_high
    
                    # row.single_master_conversion_factor = conversion_factor
    
                    session.commit()
    
                print(
                    f"[FACTORY CAL SAVED] {probe} | "
                    f"SPI_LOW={spi_low} | "
                    f"SPI_HIGH={spi_high} | "
                    
                )
    
                return True
    
            except Exception as e:
                print(f"save_single_master_calibration_db ERROR -> {e}")
                return False
    def get_dimension_from_probe(self, probe):
        try:
            for i, item in enumerate(self.formula_Cache):

                if item == probe:
                    return f"D{i+1}"

        except Exception as e:
            print("get_dimension_from_probe ERROR", e)

        return None         
    ###### END OF SINGLE MASTER CAlIBRATION LOGIC ###############################
    def setup_auto_save(self):
        try:
            self.auto_save_timer = QTimer()
            self.auto_save_timer.timeout.connect(self.autoSave_Handler)

            # ---- Runtime state ----
            self.auto_save_pending = False
            self.auto_save_stable_since = None
            self.last_auto_save_values = {}
            self.current_auto_save_values = {}
        except Exception as e:
            print(f"Error in setup_auto_save ->{e}")
    #to autosave sec when autosave should happen after this sec.      
    def update_auto_save(self):
        try:
            state = self.ui.valueObj.IOSettings_dict[
                'AUTO_SAVE_READING'
            ]['Enable']

            if state != '1':
                self.auto_save_timer.stop()
                self.auto_save_pending = False
                return

            ps = self.ui.valueObj.ProgramSettings_dict.get(
                "ProgramSpecificSettings", {}
            )

            self.auto_save_duration = float(
                ps.get("AutoSave_Duration", 0.5)
            )

            # Check frequently.
            # Stability time is handled in autoSave_Handler.
            self.auto_save_timer.start(100)
        except Exception as e:
            print(f"Auto Save Update Error -> {e}") 
    
    # handle save single show on Dial Indicator ui when save button clicked or footswitch clicked.           
    def handle_save_signal(self, success):
        try:
            state = self.ui.valueObj.IOSettings_dict[
                'AUTO_SAVE_READING'
            ]['Enable']
            if state == '1':
                return
            if not success:
                self.ui.label_savesignal.hide()
                return

            if self.ui.stacked.currentIndex() != 25:
                return

            self.ui.label_savesignal.show()
            QTimer.singleShot(1000, self.ui.label_savesignal.hide)
        except Exception as e:
            print(f"Handle Save Signal Error -> {e}")
    # Relay Handler to get value of relay when relay is Enable in IO settings       
    def relay_handler(self):
        try:
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
        except Exception as e:
            print(f"Error in relay_handler: {e}")
            
    # Refresh cache values and responsiveness settings after settings change
    def refresh_settings(self):
        try:
            # print("Refreshing settings...")
            self.formula_Cache = self.get_formula_bar()
            self.load_responsiveness_probesens()
            # save_master = (
            #     self.ui.valueObj.IOSettings_dict
            #     .get("SAVE_MASTER_CALIBRATION", {})
            #     .get("Enable", "OFF")
            #     )

            # if save_master == "ON":
            #     self.load_saved_master_settings()
            # else:
            #     self.probe_data = {}
            #     self.removed_parts = {}
            #     self.master_ready = False
            # self.load_saved_master_settings()
        except Exception as e:
            print(f"Error in refresh_settings: {e}")
        
    #  TO GET PROBE SENSITIVITY VALUES FOR ALL PROBES FROM DB (USED IN FACTORY CHANGE TO UPDATE WORKER)
    def get_all_probe_sensitivity(self):
        try:
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
        except Exception as e:
            print(f"Error in get_all_probe_sensitivity: {e}")
           
    # 🔥 LOAD FACTORY CONFIG FROM DB ON STARTUP (TO START CORRECT WORKER THREAD)   
    # Load saved factory configuration from the database
    def load_factory_from_db(self):
        try:
            with SessionLocal() as session:
                row = session.query(FactoryConfigSettings).first()
                if row and row.factory_config:
                    return row.factory_config
        except Exception as e:
            print("DB Load Error:", e)
        return None
    def load_responsiveness_probesens(self):
        try:
            ps = self.ui.valueObj.ProgramSettings_dict.get(
                "ProgramSpecificSettings", {}
            )

            Responsiveness = ps.get("Responsiveness", "0")
            probe_sensitivity = self.get_all_probe_sensitivity()

            if hasattr(self, "worker") and self.worker is not None:
                self.worker.update_responsiveness_probesens(
                    Responsiveness,
                    probe_sensitivity
                )

        except Exception as e:
            print(f"Error in load_responsiveness_probesens -> {e}")
            
    #Worker thread creation for spi Handle        
    def on_factory_changed(self, config):
        try:
            # print("Factory changed to:", config)
            self.current_factory = config
            # self.hide_show_lables()
            ps = self.ui.valueObj.ProgramSettings_dict.get("ProgramSpecificSettings", {})
            Responsiveness = ps.get("Responsiveness", "0")
            probe_sensitivity = self.get_all_probe_sensitivity()

            # print("Probe Sens:", probe_sensitivity)  # debug
            
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
    # 🔥 CORE SPI HANDLER - GETS RAW SPI VALUES, APPLIES FORMULAS, UPDATES UI, CHECKS OK/NOT OK       
    def spi_handler(self, values):
        try:
            self.counter += 1

            latest_values = self.worker.get_latest_ui_values()
            if latest_values is not None:
                values = latest_values

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
                    self.raw_spi_values[probes[i]] = float(self.clean_spi_value(val))
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
            self.update_probe_raw_label()
            self.ok_notok_part_check()

        except Exception as e:
            print(f"Error in spi_handler -> {e}")
        finally:
            if self.worker is not None:
                self.worker.acknowledge_ui_update()
    def convert_spi_to_mm(self, value):
        """Map a raw SPI value to millimetres using the two calibration points."""
        try:
            raw_value = float(value)
            raw_span = self.SPI_RAW_MAX - self.SPI_RAW_MIN
            mm_span = self.SPI_MM_MAX - self.SPI_MM_MIN
            converted_val = mm_span / raw_span
            mm_val = abs(raw_value * converted_val)

            mm_val = max(self.DISPLAY_MM_MIN, min(self.DISPLAY_MM_MAX, mm_val))
            if mm_val >= self.NO_PROBE_MM_THRESHOLD:
                mm_val = self.DISPLAY_MM_MAX

            return mm_val
        except (TypeError, ValueError):
            return None

    # Get processed SPI values in millimetres for the Set Master popup.
    def get_processed_spi_map(self, values): 
        try:
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

                raw_map = {
                    probe: result[index]
                    for index, probe in enumerate(probes)
                    if result[index] is not None
                }

            return {
                probe: self.convert_spi_to_mm(raw_value)
                for probe, raw_value in raw_map.items()
            }
        except Exception as e:
            print(f"Error in get_processed_spi_map -> {e}")
            
    # 🔥 TO UPDATE RAW SPI LABELS IN SET MASTER Page     
    def update_raw_labels(self, values):
        try:
            spi_map = self.get_processed_spi_map(values)
            self.ui.label_liveD1Val.setText(self.format_spi_mm(spi_map.get("D1")))
            self.ui.label_liveD2Val.setText(self.format_spi_mm(spi_map.get("D2")))
            self.ui.label_liveD3Val.setText(self.format_spi_mm(spi_map.get("D3")))
            self.ui.label_liveD4val.setText(self.format_spi_mm(spi_map.get("D4")))
            
        except Exception as e:
            print("Live processed label error:", e)

    @staticmethod
    def format_spi_mm(value):
        return "" if value is None else f"{value:.3f}"
    # 🔥 CORE FUNCTION TO RESOLVE FORMULAS WITH D1-D4 REFERENCES       
    def resolve_formulas(self, formula_list):
        pattern = re.compile(r'\bD([1-4])\b')

        while True:
            changed = False
            new_list = []

            # for formula in formula_list:
            for current_index, formula in enumerate(formula_list):
                if formula is None:
                    new_list.append("")
                    continue

                formula = str(formula).strip()

                if formula == "":
                    new_list.append("")
                    continue
                # def replacer(m):
                #     idx = int(m.group(1)) - 1
                #     if 0 <= idx < len(formula_list):
                #         return f"({formula_list[idx]})"  # wrap to preserve math precedence
                #     return m.group(0)
                def replacer(m):
                    idx = int(m.group(1)) - 1

                    if 0 <= idx < len(formula_list):

                        # ⭐ Prevent only self reference
                        if idx == current_index:
                            return m.group(0)

                        replacement = formula_list[idx]

                        if replacement is None:
                            return ""

                        replacement = str(replacement).strip()

                        if replacement == "":
                            return ""

                        return f"({replacement})"

                    return m.group(0)
                updated = pattern.sub(replacer, formula)
                if updated == formula and formula == f"D{current_index + 1}":
                    new_list.append(formula)
                    continue
                if updated != formula:
                    changed = True

                new_list.append(updated)

            formula_list = new_list

            # stop when no D1–D4 left in any formula
            if not changed:
                break

        return formula_list         
    # 🔥 CORE FUNCTION TO APPLY FORMULAS PER PROBE             
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
    # 🔥 NEW FUNCTION TO GET FORMULA BAR VALUES IN A LIST
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
                    formula_func=self.set_per_formula,
                    single_master_low_spi=self.single_master_low_spi,
                    single_master_high_spi=self.single_master_high_spi,

                    single_master_low_value=self.single_master_low_value,
                    single_master_high_value=self.single_master_high_value
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
                    formula_func=self.set_per_formula,
                    single_master_low_spi=self.single_master_low_spi,
                    single_master_high_spi=self.single_master_high_spi,

                    single_master_low_value=self.single_master_low_value,
                    single_master_high_value=self.single_master_high_value
                )

                self.master_set.master_finished.connect(self.on_master_finished)
                self.master_set.run()
            
        except Exception as e:
            print(f"[SET_MASTER ERROR] {e}")
            
    # Saves master settings to DB for persistence. Called after master setting process is completed and when "Save Master Calibration" is enabled in settings.
    def save_master_settings_db(self):
        try:
            active_program_id = int(
                self.ui.valueObj.activeVariables_dict["ActiveProgramId"]
            )
            with SessionLocal() as session:
                for probe, data in self.probe_data.items():
                    row = session.query(SetMasterSettings).filter(
                        SetMasterSettings.ProgramId == active_program_id,
                        SetMasterSettings.Dimension == probe
                    ).first()

                    if row is None:
                        row = SetMasterSettings(
                            ProgramId=active_program_id,
                            Dimension=probe
                        )
                        session.add(row)

                    row.MasterValue = data.get("converted_raw_value")
                    spi_low = data.get("SPI_low")
                    spi_high = data.get("SPI_high")
                    spi_master = data.get("SPI_master")
                    row.RemovedPartValue = self.removed_parts.get(probe)

                    # Keep the factory calibration already saved for a single master.
                    if data.get("Master Type") == "Single Master":
                        spi_low = row.SPI_low if spi_low is None else spi_low
                        spi_high = row.SPI_high if spi_high is None else spi_high
                        if data.get("DB_low") is not None:
                            row.DB_low = data.get("DB_low")
                        if data.get("DB_high") is not None:
                            row.DB_high = data.get("DB_high")

                    row.SPI_low = spi_low
                    row.SPI_high = spi_high
                    row.SPI_master = spi_master

                session.commit()

        except Exception as e:
            print(f"save_master_settings_db ERROR -> {e}")
    # This function is called when master setting process is completed in the modal. It receives the computed probe calibration data and updates the SPIController state accordingly.
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

        if not probe_data:
            self.probe_data = {}
            self.removed_parts = {}
            self.master_ready = False
            self.single_master_low_spi.clear()
            self.single_master_high_spi.clear()
            self.single_master_low_value.clear()
            self.single_master_high_value.clear()
            return

        if grouping_enabled == '1':
            # ✅ ONLY MERGE (DO NOT DELETE ANYTHING)
            self.probe_data.update(probe_data)
            self.removed_parts.update(removed_parts)

        else:
            # Preserve calibrations from other channels when they are set
            # individually, especially when master types are mixed.
            self.probe_data.update(probe_data)
            self.removed_parts.update(removed_parts)

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
    # Load master settings on startup if enabled in DB. This allows users to persist master calibration across sessions.
    def load_saved_master_settings(self):
        try:
            active_program_id = int(
                self.ui.valueObj.activeVariables_dict["ActiveProgramId"]
            )

            # -------------------------------------------------
            # ALWAYS START WITH MASTER NOT READY
            # -------------------------------------------------
            self.probe_data = {}
            self.removed_parts = {}
            self.master_ready = False

            # -------------------------------------------------
            # SAVE MASTER CALIBRATION MUST BE ON
            # -------------------------------------------------
            save_master = (
                self.ui.valueObj.IOSettings_dict
                .get("SAVE_MASTER_CALIBRATION", {})
                .get("Enable", "OFF")
            )

            if save_master != "ON":
                print("[MASTER LOAD] SAVE_MASTER_CALIBRATION = OFF")
                return

            loaded_count = 0

            with SessionLocal() as session:

                rows = session.query(SetMasterSettings).filter(
                    SetMasterSettings.ProgramId == active_program_id
                ).all()

                # print(
                #     f"[MASTER LOAD] Program={active_program_id}, "
                #     f"SetMaster rows={len(rows)}"
                # )

                if not rows:
                    # print("[MASTER LOAD] No saved master found")
                    return

                for row in rows:

                    probe_db = session.query(ProbeBasedSettings).filter(
                        ProbeBasedSettings.ProgramId == active_program_id,
                        ProbeBasedSettings.Dimension == row.Dimension
                    ).first()

                    if not probe_db:
                        # print(
                        #     f"[MASTER LOAD] {row.Dimension}: "
                        #     "ProbeBasedSettings missing; skipping temporary "
                        #     "master restore. Permanent single-master conversion "
                        #     "is retained."
                        # )
                        continue

                    master_type = probe_db.MasterType

                    # -------------------------------------------------
                    # SINGLE MASTER
                    # -------------------------------------------------
                    if master_type == "Single Master":

                        db_low = row.DB_low
                        db_high = row.DB_high

                        if (row.SPI_low is None or row.SPI_high is None or
                                db_low is None or db_high is None):
                            # print(
                            #     f"[MASTER LOAD] {row.Dimension}: "
                            #     "Single Master LOW/HIGH calibration missing"
                            # )
                            continue

                        self.single_master_low_spi[row.Dimension] = row.SPI_low
                        self.single_master_high_spi[row.Dimension] = row.SPI_high
                        self.single_master_low_value[row.Dimension] = db_low
                        self.single_master_high_value[row.Dimension] = db_high

                        spi_master = getattr(row, "SPI_master", None)

                        if spi_master is None:
                            print(
                                f"[MASTER LOAD] {row.Dimension}: "
                                f"Single Master SPI_master missing"
                            )
                            continue

                    # -------------------------------------------------
                    # DOUBLE MASTER
                    # -------------------------------------------------
                    elif master_type == "Double Master":

                        db_low = probe_db.MasterLower
                        db_high = probe_db.MasterHigher

                        if row.SPI_low is None or row.SPI_high is None:
                            # print(
                            #     f"[MASTER LOAD] {row.Dimension}: "
                            #     f"Double Master SPI LOW/HIGH missing"
                            # )
                            continue

                        spi_master = None

                    # -------------------------------------------------
                    # NO MASTER
                    # -------------------------------------------------
                    else:
                        # print(
                        #     f"[MASTER LOAD] {row.Dimension}: "
                        #     f"MasterType={master_type}, skipping"
                        # )
                        continue

                    # -------------------------------------------------
                    # VALID MASTER DATA
                    # -------------------------------------------------
                    if row.MasterValue is None:
                        # print(
                        #     f"[MASTER LOAD] {row.Dimension}: "
                        #     f"MasterValue missing"
                        # )
                        continue

                    self.removed_parts[row.Dimension] = row.RemovedPartValue

                    converted_raw_value = row.MasterValue
                    if master_type == "Single Master":
                        calibration_probe = self.get_calibration_probe(probe_db)
                        conversion = session.query(SingleMasterCalibration).filter(
                            SingleMasterCalibration.ProgramId == active_program_id,
                            SingleMasterCalibration.Probe == calibration_probe
                        ).first()
                        if conversion is None and calibration_probe != row.Dimension:
                            conversion = session.query(SingleMasterCalibration).filter(
                                SingleMasterCalibration.ProgramId == active_program_id,
                                SingleMasterCalibration.Dimension == row.Dimension
                            ).first()
                        if conversion and conversion.ConvertedRawValue is not None:
                            converted_raw_value = conversion.ConvertedRawValue

                    self.probe_data[row.Dimension] = {
                        "DB_low": db_low,
                        "DB_high": db_high,
                        "DB_master": probe_db.Master,
                        "method": probe_db.Method,
                        "USL": probe_db.UpperSpecificationLimit,
                        "LSL": probe_db.LowerSpecificationLimit,
                        "Master Type": master_type,
                        "Range": probe_db.Range,
                        "Nominal": probe_db.NominalValue,
                        "LeastCount": probe_db.LeastCount,

                        "SPI_low": row.SPI_low,
                        "SPI_high": row.SPI_high,
                        "SPI_master": spi_master,

                        "converted_raw_value": converted_raw_value,

                        "master_ready": True
                    }

                    loaded_count += 1

            # -------------------------------------------------
            # FINAL MASTER STATE
            # -------------------------------------------------
            self.master_ready = loaded_count > 0

            # print(
            #     f"[MASTER LOAD] loaded_count={loaded_count}, "
            #     f"master_ready={self.master_ready}"
            # )

        except Exception as e:
            self.probe_data = {}
            self.removed_parts = {}
            self.master_ready = False

            print(f"load_saved_master_settings ERROR -> {e}")

    @staticmethod
    def normalize_calibration_probe(probe):
        probe = str(probe or "").strip().upper()
        if probe.startswith("D") and probe[1:].isdigit():
            return f"P{probe[1:]}"
        return probe

    def get_calibration_probe(self, row):
        formula = str(getattr(row, "Formula", "") or "")
        match = re.search(r"\bP[1-8]\b", formula.upper())
        if match:
            return self.normalize_calibration_probe(match.group(0))

        dimension = str(getattr(row, "Dimension", "") or "").upper()
        return self.normalize_calibration_probe(dimension)
      
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
            
    # Return cached least count value for a probe
    def get_lc_cached(self, probe):
        try:
            return self.least_count_map.get(probe, 0.0)
        except Exception as e:
            print(f"Error in get_lc_cached: {e}")
            return 0.0
    
    
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
    # def ok_notok_part_check(self):
    #     try:
    #         AUTOSENSE_TOLERANCE_RANGE = 20
    #         channel_count = self.ui.dial_indicator.channel_count
    #         font_size = "40pt" if channel_count == 1 else "33pt" if channel_count == 2 else "17pt"

    #         ps = self.ui.valueObj.ProgramSettings_dict.get("ProgramSpecificSettings", {})
    #         self.auto_save_duration = float(ps.get("AutoSave_Duration", 0.5))

    #         if not getattr(self, "master_ready", False):
    #             for label in self.status_labels.values():
    #                 label.setText("")
    #             return

    #         if self.ui.stacked.currentIndex() != 25:
    #             return

    #         current_time = time.time()
    #         calculated_values = {}

    #         # -------------------------------------------------
    #         # 1️⃣ MASTER CALCULATION (NO LC HERE)
    #         # -------------------------------------------------
    #         for probe, pdata in self.probe_data.items():
    #             spi_new = self.spi_values.get(probe)
    #             if spi_new is None:
    #                 continue
    #             calculated_values[probe] = (
    #                 pdata["DB_low"]
    #                 + (spi_new - pdata["SPI_low"]) * pdata["converted_raw_value"]
    #             )

    #         # -------------------------------------------------
    #         # 2️⃣ FORMULA
    #         # -------------------------------------------------
    #         formula_list = self.formula_Cache
    #         if formula_list:
    #             variables = self.map_values(calculated_values, formula_list)
    #             a, b, c, d = variables["a"], variables["b"], variables["c"], variables["d"]
    #             formula_results = self.set_per_formula(a, b, c, d, formula_list)

    #             for i, probe in enumerate(["D1", "D2", "D3", "D4"]):
    #                 if i >= len(formula_list) or not formula_list[i]:
    #                     continue
    #                 result = formula_results[i]
    #                 if result is not None:
    #                     calculated_values[probe] = result

    #         # -------------------------------------------------
    #         # 3️⃣ FINAL LOOP (🔥 APPLY LC HERE ONLY)
    #         # -------------------------------------------------
    #         for probe, pdata in self.probe_data.items():
    #             raw_value = calculated_values.get(probe)
    #             if raw_value is None:
    #                 continue

    #             lc = self.get_lc_cached(probe)
    #             final_value = self.smash(raw_value, lc)

    #             label = self.probe_labels.get(probe)
    #             status_label = self.status_labels.get(probe)
    #             style_value = self.ui.dial_indicator.style_value
    #             style_status = self.ui.dial_indicator.style_status

    #             # -------------------------------
    #             # DISPLAY VALUE
    #             # -------------------------------
    #             if label:
    #                 label.setText(self.format_by_leastcount(final_value, lc))

    #             if probe == "D1":
    #                 angle = self.calculate_angle(final_value, pdata["Nominal"], pdata["Range"])
    #                 self.ui.dial_1_anim.move_needle(angle)
    #             elif probe == "D2":
    #                 angle = self.calculate_angle(final_value, pdata["Nominal"], pdata["Range"])
    #                 self.ui.dial_2_anim.move_needle(angle)

    #             # -------------------------------
    #             # AUTOSENSE
    #             # -------------------------------
    #             autoSense_value = self.removed_parts.get(probe)
    #             spi_new = self.spi_values.get(probe)

    #             if autoSense_value is not None and spi_new is not None:
    #                 if abs(spi_new - autoSense_value) < AUTOSENSE_TOLERANCE_RANGE:
    #                     if label:
    #                         label.setText(self.format_by_leastcount(final_value, lc))
    #                         label.setStyleSheet(f"{style_value}color: white;font-size: {font_size};")
    #                     if status_label:
    #                         status_label.setText("")
    #                     self.ui.dial_1_anim.set_dial_color("red")
    #                     self.last_status[probe] = ""
    #                     self.last_raw_status[probe] = None
    #                     self.status_stable_since[probe] = None
    #                     continue

    #             # -------------------------------
    #             # RAW STATUS
    #             # -------------------------------
    #             method = pdata["method"]
    #             usl, lsl = pdata["USL"], pdata["LSL"]

    #             if method == "OD":
    #                 raw_status = "REWORK" if final_value > usl else "NOT OK" if final_value < lsl else "OK"
    #             elif method == "ID":
    #                 raw_status = "NOT OK" if final_value > usl else "REWORK" if final_value < lsl else "OK"
    #             else:
    #                 raw_status = ""

    #             # -------------------------------
    #             # STABILITY CHECK  ← KEY FIX HERE
    #             # -------------------------------
    #             if self.last_raw_status.get(probe) != raw_status:
    #                 # Status changed — reset timer and CLEAR label so stale status disappears
    #                 self.last_raw_status[probe] = raw_status
    #                 self.status_stable_since[probe] = current_time
    #                 if status_label:
    #                     status_label.setText("")         # ← FIX: clear stale status
    #                 if label:
    #                     label.setStyleSheet(f"{style_value}color: white;font-size: {font_size};")
    #                 continue

    #             stable_since = self.status_stable_since.get(probe)
    #             if stable_since is None:
    #                 self.status_stable_since[probe] = current_time
    #                 if status_label:
    #                     status_label.setText("")         # ← FIX: clear on first encounter
    #                 continue

    #             if (current_time - stable_since) < self.auto_save_duration:
    #                 # Still within wait period — keep label blank
    #                 if status_label:
    #                     status_label.setText("")         # ← FIX: keep clearing until stable
    #                 continue

    #             # -------------------------------
    #             # STABLE — SHOW FINAL STATUS
    #             # -------------------------------
    #             self.last_status[probe] = raw_status

    #             color_map = {"OK": "green", "REWORK": "yellow", "NOT OK": "red"}
    #             color = color_map.get(raw_status, "white")

    #             if probe == "D1":
    #                 self.ui.dial_1_anim.set_dial_color(color if raw_status in color_map else "red")

    #             if status_label:
    #                 status_label.setText(raw_status)
    #                 status_label.setStyleSheet(f"{style_status}color: {color};font-size: {font_size};")
    #             if label:
    #                 label.setStyleSheet(f"{style_value}color: {color};font-size: {font_size};")

    #         # -------------------------------------------------
    #         # STATUS CHANGE DETECTION FOR RELAY
    #         # -------------------------------------------------
    #         if not hasattr(self, "previous_status"):
    #             self.previous_status = {}

    #         status_changed = any(
    #             self.previous_status.get(p) != s
    #             for p, s in self.last_status.items()
    #         )
    #         self.previous_status = self.last_status.copy()

    #         # -------------------------------------------------
    #         # RELAY (DIMENSION BASED)
    #         # -------------------------------------------------
    #         if self.relay_state == '1' and self.last_status:
    #             relay_color = self.get_relay_color(self.last_status)

    #             if not hasattr(self, "relay_triggered_for_cycle"):
    #                 self.relay_triggered_for_cycle = False

    #             if status_changed:
    #                 self.last_trigger_time = current_time
    #                 self.relay_triggered_for_cycle = False

    #             if (current_time - self.last_trigger_time) >= self.auto_save_duration:
    #                 if not self.relay_triggered_for_cycle:
    #                     self.ui.relayController.trigger(relay_color, self.relay_value)
    #                     self.last_relay_color = relay_color
    #                     self.relay_triggered_for_cycle = True

    #     except Exception as e:
    #         print(f"[OK_NOTOK ERROR] {e}")
    # # This is the main function that checks OK/NOT OK status and updates the UI accordingly.
    def ok_notok_part_check(self):
        try:
            AUTOSENSE_TOLERANCE_RANGE = 20
            channel_count = self.ui.dial_indicator.channel_count

            # ✅ calculate once per probe OUTSIDE loop only if all modes are same
            # But since each dial can have different mode (one Digit, one Dial)
            # calculate once for each probe number before loop

            font_sizes = {
                n: self.ui.dial_indicator.get_font_size(n)
                for n in range(1, channel_count + 1)
            }
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
            self.current_measurements = {}
            # -------------------------------------------------
            # 1️⃣ MASTER CALCULATION (NO LC HERE)
            # -------------------------------------------------
            for probe, pdata in self.probe_data.items():
                spi_new = self.spi_values.get(probe)
                
                if spi_new is None:
                    continue
                
                if pdata["Master Type"] == "Single Master":
                    if pdata["SPI_master"] is None:
                        continue
                    calculated_master_value = (
                    pdata["DB_master"]
                    + (
                        (spi_new - pdata["SPI_master"])
                        * pdata["converted_raw_value"]
                    )
                )
                else:
                    calculated_master_value = (
                        pdata["DB_low"]
                        + (
                            (spi_new - pdata["SPI_low"])
                            * pdata["converted_raw_value"]
                        )
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
                probe_num = int(probe[1])
                font_size = font_sizes.get(probe_num, "17pt") 
                # -------------------------------
                # DISPLAY VALUE
                # -------------------------------
                if label:
                    last_color = {"OK": "green", "REWORK": "yellow", "NOT OK": "red"}.get(
                        self.last_status.get(probe, ""), "white"
                    )
                    label.setStyleSheet(
                        self.ui.dial_indicator.style_value +
                        f"color: {last_color};font-size: {font_size};"
                    )
                    label.setText(self.format_by_leastcount(final_value, lc))
                
                angle = self.calculate_angle(final_value,pdata["Nominal"],pdata["Range"],lc)
                self.safe_move_needle(probe,angle)

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
                        #to set dial image colur when it is in autosense range.
                        # for dial in ("dial_1_anim", "dial_2_anim","dial_3_anim","dial_4_anim"):
                        #     if hasattr(self.ui, dial):
                        #         getattr(self.ui, dial).set_dial_color("red")
                        self.safe_set_dial_color(probe, "red")
                        self.last_status[probe] = ""
                        self.last_raw_status[probe] = None
                        self.status_stable_since[probe] = None
                        continue


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
                    if status_label:
                        status_label.setText("")        
                    continue
                    
                
                stable_since = self.status_stable_since.get(probe)
                if stable_since is None:
                    self.status_stable_since[probe] = current_time
                    if status_label:
                        status_label.setText("")         # ← FIX: clear on first encounter
                    continue

                if (current_time - stable_since) < self.auto_save_duration:
                    # Still within wait period — keep label blank
                    if status_label:
                        status_label.setText("")         # ← FIX: keep clearing until stable
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
                
                self.safe_set_dial_color(probe, color)
         
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
                self.current_measurements[probe] = (
                    final_value,
                    status
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
            # Measurement Stability
            # -------------------------------------------------
            measurement_changed = False

            for probe, current in self.current_measurements.items():

                previous = self.previous_measurements.get(probe)

                if previous != current:
                    measurement_changed = True
                    self.changed_probes[probe] = True

            self.previous_measurements = self.current_measurements.copy()

            if measurement_changed:
                self.last_measurement_change_time = current_time
                self.measurement_changed_since_save = True
            # measurement_changed = (
            #     self.current_measurements != self.previous_measurements
            # )

            # if measurement_changed:
            #     self.last_measurement_change_time = current_time
            #     self.measurement_changed_since_save = True

            # self.previous_measurements = self.current_measurements.copy()
            # -------------------------------------------------
            # RELAY (DIMENSION BASED ✅)
            # -------------------------------------------------
            if self.relay_state == '1' and self.last_status:

                relay_color = self.get_relay_color(self.last_status)

                # Init
                if not hasattr(self, "relay_triggered_for_cycle"):
                    self.relay_triggered_for_cycle = False

                # If ANY dimension changed → restart cycle
                # if status_changed:
                #     self.last_trigger_time = current_time
                #     self.relay_triggered_for_cycle = False
                if measurement_changed:
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
    
    # Calculate_angle function calculates the needle angle based on the measured value's position relative to the nominal value and the dial's specifications. It ensures the needle stays within the dial's limits and provides a visual representation of how far off the measurement is from the nominal value.
    def calculate_angle(self, value, nominal, dial_range,least_count):
        try:
            max_divisions = (
                30 if dial_range in [0.3, 0.03, 0.003]
                else 60
            )

            program_specific_settings = (
                self.ui.valueObj.ProgramSettings_dict
                .get("ProgramSpecificSettings", {})
            )

            uom = str(
                program_specific_settings.get("Uom", "")
            ).strip().lower()

            deviation = float(value) - float(nominal)

            # Same physical resolution:
            # 1 micron = 0.001 mm
            if uom == "mm":
                dial_tick = 0.001
                   
            elif uom == "inch":
                # Convert 0.001 mm (1 micron) to inch
                dial_tick = 0.00005

            else:
                return 0.0

            divisions = deviation / dial_tick

            # Limit needle to dial boundaries
            divisions = max(
                -max_divisions,
                min(max_divisions, divisions)
            )

            angle = (divisions / max_divisions) * 90.0

            return angle

        except Exception as e:
            print(f"calculate_angle error: {e}")
            return 0.0
        
    # Move the dial needle safely if the UI dial exists
    def safe_move_needle(self, probe, angle):
        try:
            dial_map = {"D1": "dial_1_anim", "D2": "dial_2_anim",
                        "D3": "dial_3_anim", "D4": "dial_4_anim"}
            attr = dial_map.get(probe)
            if attr and hasattr(self.ui, attr):
                getattr(self.ui, attr).move_needle(angle)
        except Exception as e:
            print(f"Error in safe_move_needle: {e}")
            
    def safe_set_dial_color(self, probe, color):
        """Safely set dial color only if dial handler exists"""
        try:
            dial_map = {
                "D1": "dial_1_anim",
                "D2": "dial_2_anim",
                "D3": "dial_3_anim",
                "D4": "dial_4_anim",
            }
            attr = dial_map.get(probe)
            if attr and hasattr(self.ui, attr):
                getattr(self.ui, attr).set_dial_color(color)
        except Exception as e:
            print(f"Error in safe_set_dial_color: {e}")
    # If IO Setting Relay On then Applied relay logic as per below cases.                        
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
            font_size = "20pt" if channel_count == 1 else "45pt" if channel_count == 2 else "35pt"
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
                
    # For automatically save when Io setting Autosave enable .            
    def autoSave_Handler(self):
        try:
            
            if self.ui.stacked.currentIndex() != 25:
                return
            state = self.ui.valueObj.IOSettings_dict[
                'AUTO_SAVE_READING'
            ]['Enable']
            if not self.master_ready:
                return

            if not self.current_measurements:
                return
            

            if state != '1':
                return
            # Values still changing
            if (
                time.time() - self.last_measurement_change_time
            ) < self.auto_save_duration:
                return

            # Already saved these measurements
            if not self.measurement_changed_since_save:
                return

            self.auto_save_probe_values()

            self.measurement_changed_since_save = False
            self.last_saved_measurements = self.current_measurements.copy()

            print("Auto Saved")

        except Exception as e:
            print(e)
            
    def auto_save_probe_values(self):
        """Save live probe values into ProbeValues table"""
        try:
            # -------------------------------
            # MASTER CHECK
            # -------------------------------
            records = []
            saved_values = []
            saved_job_counts = []
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
            self.data.save_Aoc_unique_settings()

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
                    if not self.probe_data.get(dim, {}).get("master_ready", False):
                        continue
                    status_label = self.status_labels.get(dim)

                    if not status_label:
                        continue

                    status_text = status_label.text().strip()

                    if status_text == "":
                        # CustomMessageBox(
                        #     f"Status missing for {dim}. Cannot save in Combine mode.",
                        #     "error",
                        #     parent=self.ui
                        # ).exec_()
                        return

            # -------------------------------
            # SAVE VALUES
            # -------------------------------
            for dim in channels:
                # Individual mode → save only changed dimensions
                if mode == "Individual" and dim not in self.changed_probes:
                    continue
                if not self.probe_data.get(dim, {}).get("master_ready", False):
                        continue
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
                saved_values.append((dim, value))
                self.probe_value_ready_for_cnc.emit(int(self.ui.valueObj.activeVariables_dict["ActiveProgramId"]), dim, value)
                job_count = self.job_count.get(probe_id, 1)
                # ✅ STORE (NO DB YET)
                records.append((
                    probe_id,
                    self.global_counter,
                    mode_char,
                    job_count,
                    value,
                    status_text
                ))
                # Keep the job count that was actually saved
                saved_job_counts.append((dim, job_count))
                self.global_counter += 1
                self.job_count[probe_id] = job_count + 1
                
                if self.ui.valueObj.activeVariables_dict["RS232OnOff"] == 'ON':
                    self.ui.serial_instance.send_data(str(dim) + ', ' + str(formatted_value) + ', ' + str(status_text) + ', ' + str(job_count) +'\n')
            
            if records:
                # QApplication.processEvents()
                self.db_queue.put(records)
                self.save_completed.emit(True)
                # self.handle_save_signal()
                self.changed_probes.clear()
                if saved_job_counts:
                    self.data.show_job_count_on_dimension_labels(saved_job_counts)
                saved_dims = [dim for dim, _ in saved_values]

                msg = f"{', '.join(saved_dims)} values saved successfully"

                self.ui.status_manager.show(
                    page_index=25,      # your probe page index
                    message=msg,
                    timeout=2000,
                    msg_type="success"
                )
            else:
                self.save_completed.emit(False)
            if saved_values:
                self.load_spc_values(saved_values)
        except Exception as e:
            print(f"Error while saving Probe Values -> {e}")
            self.save_completed.emit(False)
            self.ui.status_manager.show(
                page_index=25,
                message="Error while saving Probe Values",
                timeout=5000,
                msg_type="error"
            )
    # Save Probe Values for spc, database for reports.using footswitch or savebutton.       

    def save_probe_values(self):
        """Save live probe values into ProbeValues table"""
        try:
            # -------------------------------
            # MASTER CHECK
            # -------------------------------
            records = []
            saved_values = []
            saved_job_counts = []
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
            self.data.save_Aoc_unique_settings()

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
                    if not self.probe_data.get(dim, {}).get("master_ready", False):
                        continue
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
                if not self.probe_data.get(dim, {}).get("master_ready", False):
                        continue
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
                saved_values.append((dim, value))
                self.probe_value_ready_for_cnc.emit(int(self.ui.valueObj.activeVariables_dict["ActiveProgramId"]), dim, value)

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

                job_count = self.job_count.get(probe_id, 1)
                # ✅ STORE (NO DB YET)
                records.append((
                    probe_id,
                    self.global_counter,
                    mode_char,
                    job_count,
                    value,
                    status_text
                ))
                # Keep the job count that was actually saved
                saved_job_counts.append((dim, job_count))

                self.global_counter += 1
                self.job_count[probe_id] = job_count + 1
                
                if self.ui.valueObj.activeVariables_dict["RS232OnOff"] == 'ON':
                    self.ui.serial_instance.send_data(str(dim) + ', ' + str(formatted_value) + ', ' + str(status_text) + ', ' + str(job_count) +'\n')
            
            if records:
                # QApplication.processEvents()
                self.db_queue.put(records)
                self.save_completed.emit(True)
                if saved_job_counts:
                    self.data.show_job_count_on_dimension_labels(saved_job_counts)
                # self.handle_save_signal()
                saved_dims = [dim for dim, _ in saved_values]

                msg = f"{', '.join(saved_dims)} values saved successfully"

                
                # ✅ Delay this so it doesn't stomp any CNC-correction status message
                # that fired synchronously during probe_value_ready_for_cnc.emit() above
                QTimer.singleShot(2200, lambda: self.ui.status_manager.show(
                    page_index=25,
                    message=msg,
                    timeout=2000,
                    msg_type="success"
                ))
                # self.ui.status_manager.show(
                #     page_index=25,      # your probe page index
                #     message=msg,
                #     timeout=2000,
                #     msg_type="success"
                # )
            else:
                self.save_completed.emit(False)
            if saved_values:
                self.load_spc_values(saved_values)
        except Exception as e:
            print(f"Error while saving Probe Values -> {e}")
            self.save_completed.emit(False)
            self.ui.status_manager.show(
                page_index=25,
                message="Error while saving Probe Values",
                timeout=5000,
                msg_type="error"
            )
            
    # Update SPC display values for saved probe measurements
    def load_spc_values(self,saved_values):
        try:
            for dim,value in saved_values:
                if not dim:
                    continue
                try:
                    ch = int(dim[1])
                    self.ui.spc_manager.update_value(ch, value)
                
                except:
                    continue
        except Exception as e:
            print(f"Error in load_spc_values")
        
                 
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
