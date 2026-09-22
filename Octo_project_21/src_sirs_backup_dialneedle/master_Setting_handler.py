from PySide2.QtWidgets import QDialog, QLabel, QPushButton, QHBoxLayout, QVBoxLayout
from PySide2.QtWidgets import QApplication, QMainWindow, QStackedWidget , QWidget
from PySide2.QtCore import Qt
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import QObject, Signal
from models import *
from spi_module import SPI
from PySide2.QtCore import QObject , QThread , Signal, Qt
from messageBox import CustomMessageBox
from models import SessionLocal
import re
from math import *

class Worker(QObject):
    spi_generated = Signal(str, str, str, str)
    finished = Signal()

    def __init__(self, factory_config, parent=None):
        try:
            super().__init__(parent)
            self.factory_config = factory_config
            self._running = True
            self.spi = SPI(factory_config)   # ✅ correct
        except Exception as e:
            print(f"Error while initialization in worker thread -> {e}")

    @QtCore.Slot()
    def run(self):
        try:
            for value in self.spi.spi_value_emitter():
                if not self._running:
                    break

                v1, v2, v3, v4 = map(str, value)
                self.spi_generated.emit(v1, v2, v3, v4)
                
                
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
    def __init__(self, title_text, btn_text="OK",parent=None):
        try:
            super().__init__(parent)
            self.setFixedSize(500, 300)
            self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.CustomizeWindowHint)
            self.showFullScreen()
            self.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
            self.result = None
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

            # ----- Title Label -----
            self.title_label = QLabel(title_text)
            self.title_label.setAlignment(Qt.AlignCenter)
            self.title_label.setWordWrap(True)                 # 🔴 REQUIRED
            self.title_label.setMinimumHeight(240)             # enough for 2 lines
            self.title_label.setMaximumWidth(700)
            # self.title_label.setMinimumSize(500,90)
            # self.title_label.setFixedHeight(120)
            self.title_label.setStyleSheet("font-size: 18pt; font-weight: bold;")

            # ----- Live SPI Value Label -----
            # 🔴 4 LIVE SPI LABELS
            self.lbl_d1 = QLabel(" ", alignment=Qt.AlignCenter)
            self.lbl_d2 = QLabel(" ", alignment=Qt.AlignCenter)
            self.lbl_d3 = QLabel(" ", alignment=Qt.AlignCenter)
            self.lbl_d4 = QLabel(" ", alignment=Qt.AlignCenter)

            for lbl in (self.lbl_d1, self.lbl_d2, self.lbl_d3, self.lbl_d4):
                lbl.setStyleSheet("font-size: 15pt;")
                
            # ----- Button -----
            self.btn = QPushButton(btn_text)
            self.btn.setFixedSize(140, 40)
            self.btn.clicked.connect(self.accept)

            # Layout
            v = QVBoxLayout()
            v.addSpacing(5)
            v.addWidget(self.title_label)
            v.addSpacing(0)
            v.addWidget(self.lbl_d1)
            v.addWidget(self.lbl_d2)
            v.addWidget(self.lbl_d3)
            v.addWidget(self.lbl_d4)
            v.addSpacing(0)
            v.addWidget(self.btn, alignment=Qt.AlignCenter)
            v.addSpacing(5)

            self.setLayout(v)
            QtCore.QTimer.singleShot(0, self.center_on_parent)
        except Exception as e:
            print(f"Error initialization of Set master ui -> {e}")
            
    def center_on_parent(self):
        if self.parent():
            parent_rect = self.parent().frameGeometry()
            self_rect = self.frameGeometry()
            self_rect.moveCenter(parent_rect.center())
            self.move(self_rect.topLeft())
            
    # ---- Called from MainWindow when SPI emits ----
        # 🔴 SLOT CALLED BY SPI SIGNAL
    def update_spi_value(self, v1, v2, v3, v4):
        self.lbl_d1.setText(f"D1: {v4}")
        self.lbl_d2.setText(f"D2: {v3}")
        self.lbl_d3.setText(f"D3: {v2}")
        self.lbl_d4.setText(f"D4: {v1}")
    
       
class SetMasterController(QObject):
    """
    Handles Set Master workflow and master calculations.
    """
    master_finished = Signal(dict)   # Emits probe_data dict

    def __init__(self, parent, spi_values,spi_signal,grouped_channels=None):
        super().__init__(parent)

        self.ui_parent = parent
        self.spi_values = spi_values
        self.spi_signal = spi_signal   # 🔥 SPI live signal
        self.grouped_channels = grouped_channels or []

        self.master_high = {}
        self.master_low = {}
        self.probe_data = {}
        self.raw_range = 0
        self.probe = None
       
        
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
                remove_parts = Set_master_ui("Remove parts from fixture", "OK", parent=self.ui_parent)
                remove_parts.exec_()
                # ---------- HIGH MASTER ----------
                
                higher_master_raw_val = Set_master_ui("Set Higher Master","OK",parent=self.ui_parent)

                # 🔴 CONNECT SPI TO POPUP
                self.spi_signal.connect(higher_master_raw_val.update_spi_value)

                higher_master_raw_val.exec_()

                # 🔴 DISCONNECT AFTER CLOSE
                self.spi_signal.disconnect(higher_master_raw_val.update_spi_value)

                # Store HIGH master values
                for probe, spi in self.spi_values.items():
                    self.master_high[probe] = spi

                # ---------- LOW MASTER ----------
                lower_master_raw_val = Set_master_ui("Set Lower Master","OK",parent=self.ui_parent)

                self.spi_signal.connect(lower_master_raw_val.update_spi_value)
                lower_master_raw_val.exec_()
                self.spi_signal.disconnect(lower_master_raw_val.update_spi_value)

                # Store LOW master values
                for probe, spi in self.spi_values.items():
                    self.master_low[probe] = spi
                
                success, error_msg = self.calculate()

                if not success:
                    popup_fail = Set_master_ui(
                        f"Master Set Unsuccessful\n{error_msg}",
                        "Close",
                        parent=self.ui_parent
                    )
                    popup_fail.exec_()
                    return

                # ---------- CALCULATION ----------
                self.calculate()
                popup_res = Set_master_ui("Master Set Successfully", "Close", parent=self.ui_parent)
                popup_res.exec_()                    
                self.master_finished.emit(self.probe_data)

            elif current == '1':
                if not self.grouped_channels:
                    print("[GROUPING] No channels selected")
                    return

                # ---------- HIGH MASTER (GROUPED) ----------
                higher_master_raw_val = Set_master_ui("Set Higher Master", "OK", parent=self.ui_parent)
                self.spi_signal.connect(higher_master_raw_val.update_spi_value)
                higher_master_raw_val.exec_()
                self.spi_signal.disconnect(higher_master_raw_val.update_spi_value)

                for probe, spi in self.spi_values.items():
                    if probe in self.grouped_channels:
                        self.master_high[probe] = spi

                # ---------- LOW MASTER (GROUPED) ----------
                lower_master_raw_val = Set_master_ui("Set lower Master", "OK", parent=self.ui_parent)
                self.spi_signal.connect(lower_master_raw_val.update_spi_value)
                lower_master_raw_val.exec_()
                self.spi_signal.disconnect(lower_master_raw_val.update_spi_value)

                for probe, spi in self.spi_values.items():
                    if probe in self.grouped_channels:
                        self.master_low[probe] = spi
                
                success, error_msg = self.calculate()

                if not success:
                    popup_fail = Set_master_ui(
                        f"Master Set Unsuccessful\n{error_msg}",
                        "Close",
                        parent=self.ui_parent
                    )
                    popup_fail.exec_()
                    return


                # ---------- CALCULATION ----------
                self.calculate()
                popup_res = Set_master_ui("Master Set Successfully", "Close", parent=self.ui_parent)
                popup_res.exec_()

                self.master_finished.emit(self.probe_data)
                
        except Exception as e:
            print(f"[SetMasterController.run ERROR] {e}")

    def calculate(self):
        """
        Calculates mm per raw SPI for each probe.
        """
        try:
            with SessionLocal() as session:
                rows = session.query(ProbeBasedSettings).all()
            program_specific_settings = self.ui_parent.valueObj.ProgramSettings_dict.get('ProgramSpecificSettings', {})
            print("programspecific_uom:", program_specific_settings.get("Uom"))

            for row in rows:
                probe = row.Dimension

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
                calculated_value = (DB_high - DB_low) / self.raw_range
                if program_specific_settings.get("Uom") == 'inch':
                    
                    inch_value = calculated_value * 25.4
                    # 🔴 VALIDATION LOGIC
                    if row.Method == "OD" and inch_value < 0:
                        return False, f"{probe}"

                    if row.Method == "ID" and inch_value > 0:
                        return False, f"{probe}"

                    self.probe_data[probe] = {
                        "DB_low": DB_low,
                        "DB_high": DB_high,
                        "DB_master": row.Master,
                        "method": row.Method,
                        "USL": row.UpperSpecificationLimit,
                        "LSL": row.LowerSpecificationLimit,
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
                        return False, f"{probe}"

                    if row.Method == "ID" and mm_value > 0:
                        return False, f"{probe}"

                    self.probe_data[probe] = {
                        "DB_low": DB_low,
                        "DB_high": DB_high,
                        "DB_master": row.Master,
                        "method": row.Method,
                        "USL": row.UpperSpecificationLimit,
                        "LSL": row.LowerSpecificationLimit,
                        "LeastCount":row.LeastCount,
                        "SPI_low": spi_low,
                        "SPI_high": spi_high,
                        "converted_raw_value": mm_value,
                        "master_ready": True
                    }
                    
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
            self.master_ready = False
            self.worker_thread = None
            self.worker = None
            self.current_factory = None
            
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
            factory = self.load_factory_from_db()
            if factory:
                self.current_factory = factory
                # self.hide_show_lables()
                self.on_factory_changed(factory)
            else:
                print("No factory config found on startup")
        
        
            # self.data.io_settings_saved.connect(self.refresh_display())
        except Exception as e:
            print(f"Error in init of SPIcontroller: {e}")
    
            
    def load_factory_from_db(self):
        session = SessionLocal()
        try:
            row = session.query(FactoryConfigSettings).first()
            if row and row.factory_config:
                return row.factory_config
        except Exception as e:
            print("DB Load Error:", e)
        finally:
            session.close()
        return None
    
    #Worker thread creation for spi Handle        
    def on_factory_changed(self, config):
        try:
            print("Factory changed to:", config)
            self.current_factory = config
            # self.hide_show_lables()

            # 🔴 STOP OLD WORKER
            if hasattr(self, "worker") and self.worker is not None :
                self.worker.stop()
                self.worker_thread.quit()
                self.worker_thread.wait()

            # 🔴 CREATE NEW THREAD + WORKER
            self.worker_thread = QThread()
            self.worker = Worker(config)

            self.worker.moveToThread(self.worker_thread)
            self.worker_thread.started.connect(self.worker.run)

            self.worker.spi_generated.connect(self.spi_handler)
            self.worker.finished.connect(self.worker_thread.quit)

            self.worker_thread.start()
        except Exception as e:
            print(f"Error in on factory changed -> {e}")
        
    def spi_handler(self, v1, v2, v3, v4):
        """
        Receives live SPI values from Worker thread.
        Updates raw SPI labels and stores values for each probe.
        """
        try:
            self.counter += 1

            # self.spi_values["D1"] = 0 #float(self.clean_spi_value(v4)) 
            # self.spi_values["D2"] = 0 #float(self.clean_spi_value(v3))
            # self.spi_values["D3"] = 0 #float(self.clean_spi_value(v2))
            # self.spi_values["D4"] = 0 #float(self.clean_spi_value(v1))
            
            self.spi_values["D1"] = float(self.clean_spi_value(v4)) 
            self.spi_values["D2"] = float(self.clean_spi_value(v3))
            self.spi_values["D3"] = float(self.clean_spi_value(v2))
            self.spi_values["D4"] = float(self.clean_spi_value(v1))

            # Use Formula
            # formula_bar_text = self.get_formula_bar()
            # values_list = self.set_per_formula(float(self.clean_spi_value(v4)),float(self.clean_spi_value(v3)),
            #                      float(self.clean_spi_value(v2)),float(self.clean_spi_value(v1))
            #                      ,formula_bar_text)
            
            # if len(formula_bar_text) >= 1:
            #     self.spi_values["D1"] = values_list[0]
            # if len(formula_bar_text) >= 2:
            #     self.spi_values["D2"] = values_list[1]
            # if len(formula_bar_text) >= 3:
            #     self.spi_values["D3"] = values_list[2]
            # if len(formula_bar_text) == 4:
            #     self.spi_values["D4"] = values_list[3]

            # Update raw SPI display
            self.ui.label_value1.setText(str(self.spi_values["D1"]))
            self.ui.label_value2.setText(str(self.spi_values["D2"]))
            self.ui.label_value3.setText(str(self.spi_values["D3"]))
            self.ui.label_value4.setText(str(self.spi_values["D4"]))
            
            # # Store cleaned SPI values mapped to probes
            # self.spi_values["D1"] = float(self.clean_spi_value(v4))
            # self.spi_values["D2"] = float(self.clean_spi_value(v3))
            # self.spi_values["D3"] = float(self.clean_spi_value(v2))
            # self.spi_values["D4"] = float(self.clean_spi_value(v1))
            # self.refresh_display()

            self.ok_notok_part_check()

        except Exception as e:
            print(f"Error in spi_handler - > {e}")

    def set_per_formula(self,a,b,c,d,formula_list):
        try:

            values = []

            if len(formula_list) >= 1:
                real_formula_1 = re.sub(r'\bP([1-4])\b', lambda m: "abcd"[int(m.group(1))-1], formula_list[0])
                try:
                    val_1 = eval(real_formula_1)
                except:
                    val_1 = 0
                values.append(val_1)

            if len(formula_list) >= 2:
                real_formula_2 = re.sub(r'\bP([1-4])\b', lambda m: "abcd"[int(m.group(1))-1], formula_list[1])
                try:
                    val_2 = eval(real_formula_2)
                except:
                    val_2 = 0
                values.append(val_2)

            if len(formula_list) >= 3:
                real_formula_3 = re.sub(r'\bP([1-4])\b', lambda m: "abcd"[int(m.group(1))-1], formula_list[2])
                try:
                    val_3 = eval(real_formula_3)
                except:
                    val_3 = 0
                values.append(val_3)

            if len(formula_list) == 4:
                real_formula_4 = re.sub(r'\bP([1-4])\b', lambda m: "abcd"[int(m.group(1))-1], formula_list[3])
                try:
                    val_4 = eval(real_formula_4)
                except:
                    val_4 = 0
                values.append(val_4)

            return (values + [None]*4)[:4]
        except Exception as e:
            print(f"Error in set per formula -> {e}")


    def get_formula_bar(self):
        try:
            formula_bar_text = []
            channels=self.app.get_channels_for_program(
                    int(self.ui.valueObj.activeVariables_dict["ActiveProgramId"])
                )
            
            channel_count = len(channels)

            if channel_count >= 1:
                formula_text = ''
                formula_text = session.query(ProbeBasedSettings.Formula) \
                    .filter(
                        ProbeBasedSettings.id == self.ui.valueObj.activeVariables_dict["ActiveProgramId"],
                        ProbeBasedSettings.Dimension == "D1"
                    ) \
                    .scalar()

                formula_bar_text.append(formula_text)
                # print(formula_text)

            if channel_count >= 2:
                formula_text = ''
                formula_text = session.query(ProbeBasedSettings.Formula) \
                    .filter(
                        ProbeBasedSettings.id == self.ui.valueObj.activeVariables_dict["ActiveProgramId"],
                        ProbeBasedSettings.Dimension == "D2"
                    ) \
                    .scalar()
                
                formula_bar_text.append(formula_text)
                # print(formula_text)         
            
            if channel_count >= 3:
                formula_text = ''
                formula_text = session.query(ProbeBasedSettings.Formula) \
                    .filter(
                        ProbeBasedSettings.id == self.ui.valueObj.activeVariables_dict["ActiveProgramId"],
                        ProbeBasedSettings.Dimension == "D3"
                    ) \
                    .scalar()
                
                formula_bar_text.append(formula_text)
                # print(formula_text)

            if channel_count == 4:
                formula_text = ''
                formula_text = session.query(ProbeBasedSettings.Formula) \
                    .filter(
                        ProbeBasedSettings.id == self.ui.valueObj.activeVariables_dict["ActiveProgramId"],
                        ProbeBasedSettings.Dimension == "D4"
                    ) \
                    .scalar()
                
                formula_bar_text.append(formula_text)
                # print(formula_text)

            return formula_bar_text
            # return (values + [None]*4)[:4]
        except Exception as e:
            print(f"Error in get_formula_bar -> {e}")

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
                    grouped_channels = None
                )

                # Receive computed probe calibration data
                self.master_set.master_finished.connect(self.on_master_finished)

                # Blocking call (modal dialogs inside)
                self.master_set.run()
                
            elif current == '1':
                selected_channels = self.app.get_selected_master_channels()
                
                if not selected_channels:
                    print("Grouping enabled but no channels selected")
                    return

                self.master_set = SetMasterController(
                    parent=self.ui,
                    spi_values=self.spi_values,
                    spi_signal=self.worker.spi_generated,
                    grouped_channels=selected_channels
                )

                self.master_set.master_finished.connect(self.on_master_finished)
                self.master_set.run()
            
        except Exception as e:
            print(f"[SET_MASTER ERROR] {e}")

    def on_master_finished(self, probe_data):
        self.probe_data = probe_data
        self.master_ready = True
        
    def smash(self,value, step):
        return round(round(value / step) * step,10) 
     
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
            if self.ui.stacked.currentIndex() != 25 :
                return

            
            for probe, pdata in self.probe_data.items():

                spi_new = self.spi_values.get(probe)
                if spi_new is None:
                    continue
                
                # SPI -> mm conversion
                calculated_master_value = pdata["DB_low"] + \
                        (spi_new - pdata["SPI_low"]) * pdata["converted_raw_value"]

                if(pdata["method"] == 'OD'):
                    if(pdata["USL"] < calculated_master_value):
                        status = 'REWORK'
                    elif(pdata["LSL"] > calculated_master_value):
                        status = 'NOT OK'
                    else:
                        status = 'OK'

                elif(pdata["method"] == 'ID'):
                    if(pdata["USL"] < calculated_master_value):
                        status = 'NOT OK'
                    elif(pdata["LSL"] > calculated_master_value):
                        status = 'REWORK'
                    else:
                        status = 'OK'

                leastcount = pdata["LeastCount"]
                
                Final_value = self.smash(calculated_master_value, leastcount)
                # Update corresponding probe label
                label = self.probe_labels.get(probe)
                if label:
                    label.setText(f"{Final_value}")
                    
                # ---- update status label (NEW) ----
                status_label = self.status_labels.get(probe)
                if status_label:
                    status_label.setText(status)

                    if status == "OK":
                        color = "green"
                    elif status == "REWORK":
                        color = "yellow"
                    else:
                        color = "red"

                    status_label.setStyleSheet(
                        f"color: {color}; font-size: 30px; font-weight: bold;"
                    )

        except Exception as e:
            print(f"[OK_NOTOK ERROR] {e}")
            
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
            

            
