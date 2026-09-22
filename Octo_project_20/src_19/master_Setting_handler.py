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
            self.setFixedSize(500, 220)
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
            self.title_label.setMinimumSize(500,50)
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
            v.addStretch()
            v.addWidget(self.title_label)
            v.addSpacing(10)
            v.addWidget(self.lbl_d1)
            v.addWidget(self.lbl_d2)
            v.addWidget(self.lbl_d3)
            v.addWidget(self.lbl_d4)
            v.addStretch()
            v.addWidget(self.btn, alignment=Qt.AlignCenter)
            v.addSpacing(10)

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
                    continue

                DB_low = row.MasterLower
                DB_high = row.MasterHigher

                mm_per_raw = (DB_high - DB_low) / self.raw_range

                self.probe_data[probe] = {
                    "DB_low": DB_low,
                    "DB_high": DB_high,
                    "DB_master": row.Master,
                    "method": row.Method,
                    "SPI_low": spi_low,
                    "SPI_high": spi_high,
                    "mm_per_raw": mm_per_raw,
                    "master_ready": True
                }

        except Exception as e:
            print(f"[SetMasterController.calculate ERROR] {e}")
            
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
            factory = self.load_factory_from_db()
            if factory:
                self.current_factory = factory
                # self.hide_show_lables()
                self.on_factory_changed(factory)
            else:
                print("No factory config found on startup")
        except Exception as e:
            print(f"Error in init of Appcontroller: {e}")
    

            
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
        
    # -------- SPI --------
    def spi_handler(self, v1, v2, v3, v4):
        """
        Receives live SPI values from Worker thread.
        Updates raw SPI labels and stores values for each probe.
        """
        try:
            # display_mode = (
            #     self.ui.valueObj.IOSettings_dict
            #     .get('DISPLAY_MODE', {})
            #     .get('Value', 'Digit')
            # )
            # print(f"display_mode = {display_mode}")
            # if display_mode == 'Digit':
            # Update raw SPI display
            self.ui.label_value1.setText(v4)
            self.ui.label_value2.setText(v3)
            self.ui.label_value3.setText(v2)
            self.ui.label_value4.setText(v1)
            

            # Store cleaned SPI values mapped to probes
            self.spi_values["D1"] = float(self.clean_spi_value(v4))
            self.spi_values["D2"] = float(self.clean_spi_value(v3))
            self.spi_values["D3"] = float(self.clean_spi_value(v2))
            self.spi_values["D4"] = float(self.clean_spi_value(v1))
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
            

            
