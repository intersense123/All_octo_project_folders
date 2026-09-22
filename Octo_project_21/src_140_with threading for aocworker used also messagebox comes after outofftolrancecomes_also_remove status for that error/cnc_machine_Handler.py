from datetime import date

from PySide2.QtWidgets import QApplication, QMainWindow, QStackedWidget, QTextEdit , QWidget
from PySide2.QtWidgets import QFrame
from PySide2.QtWidgets import QLineEdit
from PySide2 import QtCore, QtWidgets
from PySide2.QtCore import QTimer, QSize, QDate , QObject , QThread , Signal, Qt, QCoreApplication
from PySide2.QtGui import QPixmap, QStandardItemModel, QStandardItem, QBrush, QColor
from messageBox import CustomMessageBox
from models import *
from models import SessionLocal , AOCBasedSettings,CNCMaster
from sqlalchemy.orm import Session , sessionmaker
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from FanucLibDefs import FANUCDEFS
import subprocess
from PySide2.QtWidgets import QApplication, QMainWindow, QStackedWidget , QWidget
from PySide2.QtWidgets import QFrame
from PySide2.QtWidgets import QLineEdit
from PySide2 import QtCore, QtWidgets
from PySide2.QtCore import QTimer, QSize, QDate , QObject , QThread , Signal, Qt, Slot
from PySide2.QtGui import QPixmap
from messageBox import CustomMessageBox
from models import *
from models import SessionLocal , AOCBasedSettings , CNCMaster
from sqlalchemy.orm import Session , sessionmaker
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from PySide2.QtGui import QStandardItemModel, QStandardItem
from FanucLibDefs import FANUCDEFS
import subprocess
from PySide2.QtWidgets import (QApplication, QButtonGroup, QCheckBox, QComboBox,
    QFrame, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLayout, QLineEdit, QMainWindow,
    QPushButton, QRadioButton, QScrollArea, QSizePolicy,
    QSpacerItem, QStackedWidget, QTabWidget, QTableView,
    QTableWidget, QTableWidgetItem, QToolButton, QVBoxLayout,
    QWidget)
from queue import Queue,Empty
# try:
#     import RPi.GPIO as GPIO
# except Exception:
#     GPIO = None
#     print("RPi.GPIO not available — live GPIO machine selection disabled.")

class ConnectionsUI(QWidget):
    closed_signal = Signal()
    update_signal = Signal(str)
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Serial Test")
        self.setMinimumSize(QtCore.QSize(400, 280))
        self.setMaximumSize(QtCore.QSize(400, 280))
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.CustomizeWindowHint)
        #self.showFullScreen()
        self.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)

        # Label to show messages
        self.output_label = QTextEdit(self)
        self.output_label.setReadOnly(True)
        self.output_label.setStyleSheet("font-size: 22px; color: black; background-color: #87CEEB; padding: 10px;")
       
        
        # Status label
        self.status_label = QLabel("Machine Connection Status")
        self.status_label.setAlignment(Qt.AlignCenter)
        self.status_label.setStyleSheet("font-size: 24px; color: black;")

        # Close button
        self.close_button = QPushButton("Close", self)
        self.close_button.setStyleSheet(
            "font-size: 16px; padding: 8px; background-color: #f33; color: white; border-radius: 8px;"
        )
        self.close_button.clicked.connect(self.close_window)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.status_label)
        layout.addWidget(self.output_label)
        layout.addWidget(self.close_button)
        self.setLayout(layout)
        self.update_signal.connect(self.update_label)

        #global_signals.serial_line_signal.connect(self.update_label)
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            return
        super().keyPressEvent(event)
           
    def update_label(self, text):
        self.output_label.append(text)

    def show_status(self, msg):
        self.status_label.setText(f"Status: {msg}")

    def close_window(self):
        self.close()

    def closeEvent(self, event):
        """Ensure thread closes on window close."""
        self.closed_signal.emit()
        #serial_control.enable()
        # try:
        #     serial_control.toggle_signal.emit(True)
        #     print("Serial toggle signal emitted from closeEvent (True)")
        # except Exception as e:
        #     print("Error emitting toggle signal from closeEvent:", e)
        event.accept()

class AOCWorker(QObject):

    finished = Signal()
    error = Signal(str)

    def __init__(self, manager):
        super().__init__()

        self.manager = manager

        self.jobs = Queue()

        self.running = True

    @Slot()
    def process(self):

        while self.running:

            try:
                job = self.jobs.get(timeout=1)
            except Empty:
                continue

            if job is None:
                break
    

            try:

                program_id, dimension, value = job

                self.manager.process_reading_and_write_correction(
                    program_id,
                    dimension,
                    value
                )

            except Exception as e:

                self.error.emit(str(e))

        self.finished.emit()

    def add_job(self, program_id, dimension, value):

        self.jobs.put(
            (
                program_id,
                dimension,
                value
            )
        )

    def stop(self):

        self.running = False

        self.jobs.put(None)
# class ConnectionMonitorThread(QThread):
#     status_changed = Signal(dict)

#     def __init__(self, manager):
#         super().__init__()
#         self.manager = manager
#         self.running = True

#     def stop(self):
#         self.running = False
#         self.wait()

#     def run(self):

#         while self.running:

#             status = {}

#             try:

#                 cnc_dict = dict(self.manager.cnc_details_dict)

#                 for machine_name, details in cnc_dict.items():

#                     connected = False

#                     try:

#                         controller = details["ControllerName"]

#                         if controller == "FANUC":
#                             connected = (
#                                 self.manager.ping_pi(details["IPAddress"])
#                                 == "True"
#                             )

#                         elif controller == "HAAS NGC":
#                             connected = False
#                             # connected = ping_haas(...)

#                     except:
#                         connected = False

#                     status[machine_name] = connected

#                 self.status_changed.emit(status)

#             except Exception as e:
#                 print("Connection Thread :", e)

#             self.msleep(2000)
class CNCManager(QObject):
    update_aocTable = Signal()
    show_message_signal = Signal(str, str)  
    def __init__(self, main_window):
        try:
            super().__init__(parent=None)
            self.ui = main_window
            self.ui.button_ping.clicked.connect(self.ping_button_clicked)
            self.connection_window = ConnectionsUI()
            # cnc connection + AOC details, keyed by machine name (CNCMaster.CNCName)
            self.cnc_details_dict = {}
 
            # live FANUC connection instances, keyed by machine name (kept open across calls)
            self.fanuc_instances = {}
            self.aoc_thread = QThread()

            self.aoc_worker = AOCWorker(self)

            self.aoc_worker.moveToThread(self.aoc_thread)

            self.aoc_thread.started.connect(
                self.aoc_worker.process
            )

            self.aoc_worker.finished.connect(
                self.aoc_thread.quit
            )

            self.aoc_worker.error.connect(
                lambda e: print("AOC Worker:", e)
            )

            self.aoc_thread.start()
            # GPIO pins for live machine selection (same pins used for buzzer scenario elsewhere)
            # IN1 -> 27, IN2 -> 17, IN3 -> 24, IN4 -> 25 ; default "Not Applicable"
            self.selection_pins = {
                "IN1": 27,
                "IN2": 17,
                "IN3": 24,
                "IN4": 25,
            }
            # self.init_selection_gpio()
            self.work_in_process_started = {"D1": False, "D2": False, "D3": False, "D4": False}
            self.work_in_process_counter = {"D1": 0, "D2": 0, "D3": 0, "D4": 0}
            self.skip_offset_counter = {"D1": 0, "D2": 0, "D3": 0, "D4": 0}
           
            # trial mode ON/OFF simulated tool values (mirrors old p1_tool_value..p4_tool_value)
            self.trial_tool_value = {"D1": 0.0, "D2": 0.0, "D3": 0.0, "D4": 0.0}
            # Connect to DataHandler's signal once data_handler exists on ui
            if hasattr(self.ui, "data_handler"):
                self.ui.data_handler.aoc_settings_saved.connect(self.on_aoc_settings_saved)
            if hasattr(self.ui,"spi_controller"):
                self.ui.spi_controller.probe_value_ready_for_cnc.connect(
                    self.on_probe_value_saved
                )
            self.aoc_global_counter = self.ui.savedbObj.get_next_aoc_global_counter()
            self.aoc_job_count = self.ui.savedbObj.get_aoc_job_counts()
            # self.machine_connection_status = {}
            self.show_message_signal.connect(self._show_message_on_main_thread)

            # self.connection_thread = None

            # self.start_connection_monitor()
            # self.ui.label_CNCconnectionstatus.mousePressEvent = lambda event: self.open_connection_status()
            
        except Exception as e:
            print(f"Error in CNCManager -> {e}")
    def _show_message_on_main_thread(self, text, msg_type):
        msg = CustomMessageBox(text, msg_type, parent=self.ui)
        msg.exec_()
    def ping_button_clicked(self):
        
        if (self.ui.comboBox_cncController.currentText() == "FANUC"):
            # Ping 3 times, wait max 2s for each
            command = ['ping', '-c', '3', '-W', '1', self.ui.lineEdit_cncIpAddress.text()]
            # print(f"Pinging FANUC with IP {self.ui.lineEdit_cncIpAddress.text()} (3 attempts)...")

            result = subprocess.run(
                    command,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True
            )

            # Check if at least one packet received successfully
            output = result.stdout
            # print("PING OUTPUT:\n", output)


            # -------- CORRECT LOGIC --------
            if " 0 received" in output or ", 0%" not in output and "received, 0" in output:
                # Means 0 packets received → NOT connected
                msg = CustomMessageBox(
                    'Machine is not connected!!\n' + self.ping_fanuc(),
                    "error",
                    parent=self.ui
                )
                msg.exec_()
                
            else:
                # Means >=1 packets received → CONNECTED
                msg = CustomMessageBox(
                    'Machine is connected successfully!!\n' + self.ping_fanuc(),
                    "success",
                    parent=self.ui
                )
                msg.exec_()                
                
    
    def ping_fanuc(self):
        serial_id = ''

        try:
            # FanucLibDefs
            machine = FANUCDEFS(self.ui.lineEdit_cncIpAddress.text().strip(), int(self.ui.lineEdit_cncPortNumber.text().strip()))
            ret = machine.focas.cnc_startupprocess(0, "focas.log")
            if ret != 0:
                raise Exception(f"Failed to create required log file! ({ret})")
            machine.connectFanuc()
            machine_id = machine.readFanuc()
            serial_id = f"{machine_id}"
            machine.disconnectMachine()
        except:
            serial_id = 'Fanuc Not Connected!!'

        return serial_id
    #############################################################################
    # def start_connection_monitor(self):
    #     try:
    #         if self.connection_thread:

    #             self.connection_thread.stop()

    #         self.connection_thread = ConnectionMonitorThread(self)

    #         self.connection_thread.status_changed.connect(
    #             self.on_connection_status_changed
    #         )

    #         self.connection_thread.start()
    #     except Exception as e:
    #         print(f"Erro in start_connection_monitor -> {e}")
    # def stop_connection_monitor(self):
    #     try:
    #         if self.connection_thread:

    #             self.connection_thread.stop()

    #             self.connection_thread = None
    #     except Exception as e:
    #         print(f"Error in stop_connection_monitor -> {e}")
    # def on_connection_status_changed(self, status_dict):
    #     try:
    #         self.machine_connection_status = status_dict

    #         all_connected = True

    #         for connected in status_dict.values():

    #             if not connected:
    #                 all_connected = False
    #                 break

    #         if all_connected:

    #             self.ui.label_CNCconnectionstatus.setStyleSheet("""
    #             QLabel{
    #                 background:#19b500;
    #                 color:white;
    #                 border-radius:6px;
    #             }
    #             """)

    #         else:

    #             self.ui.label_CNCconnectionstatus.setStyleSheet("""
    #             QLabel{
    #                 background:red;
    #                 color:white;
    #                 border-radius:6px;
    #             }
    #             """)

    #         if self.connection_window.isVisible():

    #             self.connection_window.output_label.clear()

    #             self.connection_window.update_label(
    #                 self.generate_text_for_machine_connection()
    #             )
    #     except Exception as e:
    #         print(f"Error in on_connection_status_changed -> {e}")
    # def generate_text_for_machine_connection(self):
    #     try:
    #         lines = []

    #         for machine in sorted(self.machine_connection_status):

    #             if self.machine_connection_status[machine]:
    #                 status = "Connected"
    #             else:
    #                 status = "Disconnected"

    #             lines.append(f"{machine}  -->  {status}")

    #         return "\n".join(lines)
    #     except Exception as e:
    #         print(f"Error in generate_text_for_machine_connection -> {e}")
    #         return ""
    # def open_connection_status(self):
    #     try:
    #         self.connection_window.output_label.clear()

    #         self.connection_window.update_label(
    #             self.generate_text_for_machine_connection()
    #         )

    #         self.connection_window.show()

    #         self.connection_window.raise_()

    #         self.connection_window.activateWindow()
    #     except Exception as e:
    #         print(f"Error in open_connection_status -> {e}")
    # def on_cnc_settings_saved(self):
    #     try:
    #         self.stop_connection_monitor()

    #         # reload cnc_details_dict here

    #         self.start_connection_monitor()
    #     except Exception as e:
    #         print(f"Error in on_cnc_settings_saved -> {e}")
    ######################################################################################
    def get_live_selection(self):
        """
        Return the currently active machine selection: "IN1".."IN4" or "Not Applicable".
        Mirrors old operate_string's get_live_selection() using the same GPIO pins
        (27, 17, 24, 25) that are also used for the buzzer scenario elsewhere in the app.
        """
        try:
            # if GPIO is None:
            #     return "Not Applicable"
 
            # for label, pin in self.selection_pins.items():
            #     if GPIO.input(pin) == GPIO.HIGH:
            #         return label
 
            return "Not Applicable"
        except Exception as e:
            print(f"Error in get_live_selection -> {e}")
            return "Not Applicable"
 
    def get_machine_key_by_selection(self, selection):
        """
        Return the machine name (CNCMaster.CNCName) whose cached CNCSelection
        matches the given selection string ("IN1".."IN4" or "Not Applicable").
        """
        try:
            for machine_name, details in self.cnc_details_dict.items():
                cnc_selection = (details.get("CNCSelection") or "").strip().upper()
                if cnc_selection == (selection or "").strip().upper():
                    return machine_name
            return None
        except Exception as e:
            print(f"Error in get_machine_key_by_selection -> {e}")
            return None
    
    # ==================== CNC DETAILS LOOKUP ====================
 
    def get_cnc_details_for_program(self, program_id, dimension):
        """
        Given a ProgramId and Dimension, walk:
        ProgramId -> Dimension -> AOCBasedSettings (Machine) -> CNCMaster (match CNCName)
 
        Stores/updates the result in self.cnc_details_dict, keyed by machine name.
        Skips the write entirely if identical details already exist for that machine.
 
        Returns the details dict for this machine (IP/Port/Controller +
        Axis/Direction/OffsetNo/UpperOffsetLimit/LowerOffsetLimit), or None if not found.
        """
        try:
            if not hasattr(self, "cnc_details_dict"):
                self.cnc_details_dict = {}
 
            session = SessionLocal()
            try:
                aoc_row = session.query(AOCBasedSettings).filter_by(
                    ProgramId=program_id,
                    Dimension=dimension
                ).first()
 
                if not aoc_row:
                    print(f"No AOCBasedSettings found for ProgramId={program_id}, Dimension={dimension}")
                    return None
 
                machine_name = aoc_row.Machine
                if not machine_name:
                    print(f"AOCBasedSettings row found but Machine is empty (ProgramId={program_id}, Dimension={dimension})")
                    return None
 
                cnc_row = session.query(CNCMaster).filter_by(
                    CNCName=machine_name
                ).first()
 
                if not cnc_row:
                    print(f"No CNCMaster entry found for machine name '{machine_name}'")
                    return None
 
                details = {
                    "IPAddress": cnc_row.IPAddress,
                    "PortNumber": cnc_row.PortNumber,
                    "CNCSelection": cnc_row.CNCSelection,
                    "ControllerName": cnc_row.ControllerName,
                    # AOC fields needed for read/write + limit check
                    "Axis": aoc_row.Axis,
                    "Direction": aoc_row.Direction,
                    "OffsetNo": aoc_row.OffsetNo,
                    "UpperOffsetLimit": aoc_row.UpperOffsetLimit,
                    "LowerOffsetLimit": aoc_row.LowerOffsetLimit,
                }
 
                # Only update/append if this machine's details are new or changed
                existing = self.cnc_details_dict.get(machine_name)
                if existing != details:
                    self.cnc_details_dict[machine_name] = details
                    # print(f"Updated cnc_details_dict for '{machine_name}': {details}")
                else:
                    print(f"No change for '{machine_name}', skipping update.")
 
                return self.cnc_details_dict[machine_name]
 
            finally:
                session.close()
 
        except SQLAlchemyError as e:
            print(f"Database error in get_cnc_details_for_program -> {e}")
            return None
        except Exception as e:
            print(f"Error in get_cnc_details_for_program -> {e}")
            return None
 
    def on_aoc_settings_saved(self, program_id, dimension):
        """Slot: refresh cnc details for this program+dimension whenever AOC settings are saved"""
        try:
            # close any old FANUC connection
            machine = self.machine_name_for(program_id, dimension)
            if machine:
                self.cleanup_fanuc(machine)

            # reload latest cnc details
            self.get_cnc_details_for_program(program_id, dimension)

            print(self.cnc_details_dict)
        except Exception as e:
            print(f"Error in on_aoc_settings_saved -> {e}")
 
    def machine_name_for(self, program_id, dimension):
        """Helper: look up the machine name for a given program_id/dimension from DB."""
        try:
            session = SessionLocal()
            try:
                aoc_row = session.query(AOCBasedSettings).filter_by(
                    ProgramId=program_id,
                    Dimension=dimension
                ).first()
                return aoc_row.Machine if aoc_row else None
            finally:
                session.close()
        except Exception as e:
            print(f"Error in machine_name_for -> {e}")
            return None
 
    # ==================== FANUC CONNECTION MANAGEMENT ====================
 
    def get_fanuc_instance(self, machine_name):
        """
        Get (or create + cache) a live FANUC connection for a given machine name.
        Mirrors old operate_string's self.get_fanuc_instance(machine_key).
        """
        try:
            if machine_name in self.fanuc_instances:
                return self.fanuc_instances[machine_name]
 
            details = self.cnc_details_dict.get(machine_name)
            if not details:
                print(f"No cached cnc details for machine '{machine_name}'")
                return None
 
            instance = FANUCDEFS(details["IPAddress"], int(details["PortNumber"]))
            ret = instance.focas.cnc_startupprocess(0, "focas.log")
            if ret != 0:
                raise Exception(f"Failed to create required log file! ({ret})")
            instance.connectFanuc()
 
            self.fanuc_instances[machine_name] = instance
            return instance
        except Exception as e:
            print(f"Error in get_fanuc_instance -> {e}")
            return None
 
    def cleanup_fanuc(self, machine_name):
        """Disconnect and drop a cached FANUC instance for a machine name."""
        try:
            instance = self.fanuc_instances.pop(machine_name, None)
            if instance:
                instance.disconnectMachine()
        except Exception as e:
            print(f"Error in cleanup_fanuc -> {e}")
    
    def on_probe_value_saved(self, program_id, dimension, value):
        """Slot: only pass value to CNC when the global AOC toggle and the dimension setting are both enabled."""
        try:
            session = SessionLocal()
            try:
                aoc_row = session.query(AOCBasedSettings).filter_by(
                    ProgramId=program_id, Dimension=dimension
                ).first()
            finally:
                session.close()

            aoc_toggle_state = "OFF"
            if hasattr(self.ui, "valueObj"):
                aoc_dict = getattr(self.ui.valueObj, "AOCSettings_dict", {})
                if hasattr(self.ui.valueObj, "activeVariables_dict"):
                    aoc_toggle_state = str(
                        aoc_dict.get(
                            "AOC_ON_OFF",
                            self.ui.valueObj.activeVariables_dict.get("AOCOnOff", "OFF"),
                        )
                    ).strip().upper()
                else:
                    aoc_toggle_state = str(aoc_dict.get("AOC_ON_OFF", "OFF")).strip().upper()

            if not aoc_row:
                return
            if aoc_toggle_state != "ON":
                return
            if (aoc_row.aocEnable or "").strip().upper() != "ON":
                return
            self.aoc_worker.add_job(program_id, dimension, value)
            # self.process_reading_and_write_correction(program_id, dimension, value)
        except Exception as e:
            print(f"Error in on_probe_value_saved -> {e}")
    def fanuc_read(self, instance, offset_no, column):
        try:
            return float(instance.read(int(offset_no), column, 8))
        except Exception as e:
            print(f"FANUC read error -> {e}")
            raise
 
    def fanuc_write(self, instance, offset_no, column, new_value):
        try:
            instance.write(int(offset_no), column, 8, float(new_value))
        except Exception as e:
            print(f"FANUC write error -> {e}")
            raise
    def save_aoc_values(self, aoc_id,machine_name,dimension, part_name,nominal, offset_no, offs,
                           correction, tool_value):
        """
        Persist one reading/correction cycle to Dial_indicator, mirroring old
        operate_string's session.add(Dial_indicator(...)) calls — logged on
        every branch (auto-correction-zone error, zero-correction, real write,
        skip-offset), not just successful writes.
        """
        try:
            
            aoc_job = self.aoc_job_count.get(aoc_id, 1)

            record = (
                aoc_id,
                self.aoc_global_counter,
                aoc_job,
                dimension,
                machine_name,
                part_name,
                nominal,
                offset_no,
                offs,                   # measured value
                correction,   # correction applied
                tool_value    # final tool offset
            )

            self.ui.savedbObj.insert_aoc_values([record])
            self.aoc_global_counter += 1
            self.aoc_job_count[aoc_id] = aoc_job + 1
            self.update_aocTable.emit()
        except Exception as e:
            print(f"Error in save_aoc_values -> {e}")
 
    def process_reading_and_write_correction(
        self, program_id, dimension, offs, trial_mode="OFF"
    ):
        """
        
        1. Looks up ProbeBasedSettings (LSL/USL/LCL/UCL/Nominal) and
           AOCBasedSettings (Axis/Direction/OffsetNo/UpperOffsetLimit/LowerOffsetLimit/
           WorkInProcess/SkipOffsetCount) for program_id + dimension.
        2. Resolves the CNC machine + live-selection gate (via write_correction_to_cnc's
           helpers) and connects to FANUC.
        3. 
             - offs outside [LSL, USL]:
                 - outside [LowerOffsetLimit, UpperOffsetLimit] -> "Auto-correction Zone"
                   block: no correction written, just reads current z, work-in-process
                   counters updated, correction sentinel recorded (999.999/999.997)
                 - inside offset limits -> writes real correction (mean - offs), signed
                   by direction, gated by work-in-process 'todo' (serve/halt)
             - offs inside [LSL, USL]:
                 - inside [LCL, UCL] -> writes 0 (no correction needed)
                 - outside [LCL, UCL] -> applies skip-offset-count logic, then writes
                   real correction if not skipped
        4. Always disconnects the FANUC instance at the end (success or failure).
 
        Returns a result dict:
            {
                "dimension": ..., "machine": ..., "offs": ..., "mean": ...,
                "correction": <float actual value written, or sentinel>,
                "tool_value": <z, the CNC offset value after the operation>,
                "todo": "serve" | "halt",
                "status": "auto_correction_zone_error" | "tolerance_limit_error"
                          | "written" | "zero_correction" | "skipped_offset" | "error",
            }
        DB logging is NOT done here since your current schema has no Dial_indicator-
        equivalent table — persist the returned dict wherever you need it.
        """
        result = {
            "dimension": dimension, "machine": None, "offs": offs, "mean": None,
            "correction": None, "tool_value": None, "todo": "serve", "status": None,
        }
        try:
            # ---- 1. Pull ProbeBasedSettings + AOCBasedSettings ----
            session = SessionLocal()
            try:
                probe = session.query(ProbeBasedSettings).filter_by(
                    ProgramId=program_id, Dimension=dimension
                ).first()
                aoc_row = session.query(AOCBasedSettings).filter_by(
                    ProgramId=program_id, Dimension=dimension
                ).first()
            finally:
                session.close()

            if not probe:
                print(f"No ProbeBasedSettings for ProgramId={program_id}, Dimension={dimension}")
                result["status"] = "error"
                return result
            if not aoc_row:
                print(f"No AOCBasedSettings for ProgramId={program_id}, Dimension={dimension}")
                result["status"] = "error"
                return result

            # ✅ Build unique string from the FRESH DB row (aoc_row), not the
            # in-memory ProgramSettings_dict cache — that dict is only reliably
            # populated for the currently-active program and can be stale/out
            # of sync, which was silently short-circuiting this whole function
            # (returning "error" before ever reaching save_aoc_values).
            aoc_settings_for_key = {
                "Axis": aoc_row.Axis,
                "OffsetNo": aoc_row.OffsetNo,
                "UpperOffsetLimit": aoc_row.UpperOffsetLimit,
                "LowerOffsetLimit": aoc_row.LowerOffsetLimit,
                "Machine": aoc_row.Machine,
                "Direction": aoc_row.Direction,
                "TurretNo": aoc_row.TurretNo,
                "WorkInProcess": aoc_row.WorkInProcess,
                "SkipOffsetCount": aoc_row.SkipOffsetCount,
            }
            unique_string = self.ui.data_handler.build_aoc_unique_string(
                f"{dimension}", aoc_settings_for_key)
            aoc_id = self.ui.savedbObj.get_aoc_id_by_settings(unique_string)

            if not aoc_id:
                print(
                    f"No AOCBasedIds entry found for ProgramId={program_id}, "
                    f"Dimension={dimension} (unique_string not yet registered). "
                    f"Was save_Aoc_unique_settings() called before this?"
                )
                result["status"] = "error"
                return result

            LSL = probe.LowerSpecificationLimit #float(f"{probe.LowerSpecificationLimit:.3f}")
            USL = probe.UpperSpecificationLimit #float(f"{probe.UpperSpecificationLimit:.3f}")
            LCL = probe.LowerControlLimit #float(f"{probe.LowerControlLimit:.3f}")
            UCL = probe.UpperControlLimit #float(f"{probe.UpperControlLimit:.3f}")
            mean = probe.NominalValue #float(f"{probe.NominalValue:.3f}")
            part_name = probe.ProgramName
            result["mean"] = mean
 
            work_in_process = aoc_row.WorkInProcess or 0
            skip_offset = aoc_row.SkipOffsetCount or 0
            direction = aoc_row.Direction
            axis = (aoc_row.Axis or "").lower()
            offset_no = aoc_row.OffsetNo
            lower_offs_limit = aoc_row.LowerOffsetLimit
            upper_offs_limit = aoc_row.UpperOffsetLimit
 
            # ---- 2. Resolve machine + live selection gate ----
            machine_name = self.machine_name_for(program_id, dimension)
            if not machine_name:
                print(f"No machine found for ProgramId={program_id}, Dimension={dimension}")
                result["status"] = "error"
                return result
            result["machine"] = machine_name
 
            details = self.cnc_details_dict.get(machine_name) or \
                self.get_cnc_details_for_program(program_id, dimension)
            if not details:
                result["status"] = "error"
                return result
 
            cnc_selection = (details.get("CNCSelection") or "").strip().upper()
            live_sel = self.get_live_selection().strip().upper()
            if cnc_selection not in ("", "NOT APPLICABLE") and cnc_selection != live_sel:
                print(f"Selection mismatch for '{machine_name}': expects '{cnc_selection}', live is '{live_sel}'")
                # msg = CustomMessageBox(
                #     "Machine not selected or incorrect machine selection.",
                #     "error", parent=self.ui
                # )
                # msg.exec_()
                self.show_message_signal.emit(f"Machine not selected or incorrect machine selection.", "error")
                result["status"] = "error"
                return result
 
            controller = details.get("ControllerName")
            column = 0 if axis == 'x' else (2 if axis == 'z' else 0)
 
            offs = offs #float(f"{offs:.3f}") 
 
            # ---- Helper to get current z (read-only, no write) ----
            def read_cnc_val():
                if trial_mode == 'OFF':
                    if controller == "FANUC":
                        instance = self.get_fanuc_instance(machine_name)
                        if not instance:
                            raise Exception("No FANUC instance")
                        return self.fanuc_read(instance, offset_no, column)
                    elif controller == "HAAS NGC":
                        print("HAAS NGC read not implemented in CNCManager yet.")
                        raise Exception("HAAS not implemented")
                    else:
                        raise Exception(f"Unknown controller '{controller}'")
                else:
                    return round(self.trial_tool_value[dimension], 3)
 
            wip_started = self.work_in_process_started
            wip_counter = self.work_in_process_counter
            skip_counter = self.skip_offset_counter
            def update_wip_for_block_condition(triggered):
                """Mirrors old per-dimension work_in_process_dX logic."""
                if wip_started[dimension]:
                    wip_counter[dimension] += 1
                    if work_in_process < wip_counter[dimension]:
                        todo = 'serve'
                        wip_counter[dimension] = 0
                        wip_started[dimension] = triggered
                    else:
                        todo = 'halt'
                else:
                    if triggered:
                        todo = 'halt' if False else 'serve'  # not started -> matches old fallthrough
                    else:
                        wip_started[dimension] = True
                        todo = 'serve'
                skip_counter[dimension] = 0
                return todo
 
            try:

                # ================= BRANCH 1: offs outside [LSL, USL] =================
                if (offs < float(LSL)) or (offs > float(USL)):
                    # ---- 1a: outside offset limits -> Auto-correction Zone error ----
                    if offs > float(upper_offs_limit or 0) or offs < float(lower_offs_limit or 0):
                        todo = update_wip_for_block_condition(triggered=False)
                        result["todo"] = todo
                        try:
                            z = read_cnc_val()
                        except Exception:
                            result["status"] = "error"
                            return result
 
                        result["tool_value"] = z
                        result["correction"] = 999.999 if todo == 'serve' else 999.997
                        result["status"] = "auto_correction_zone_error"

                        self.save_aoc_values(
                            aoc_id,
                            machine_name,
                            dimension,
                            part_name,
                            result["mean"],
                            offset_no,
                            offs,
                            result["correction"],
                            z,
                        )
 
                        print(f"DEBUG: {dimension} out of Auto-correction Zone.")
                        self.show_message_signal.emit(f"Dimension {dimension} is out of the Tolarance ", "error")
                        # msg = CustomMessageBox(
                        #     f"Dimension {dimension} is out of the Tolarance ",
                        #     "error", parent=self.ui
                        # )
                        # msg.exec_()
                        # self.ui.status_manager.show(
                        # page_index=25,      # your probe page index
                        # message=f"Dimension {dimension} is out of Tolerance.",
                        # timeout=2000,
                        # msg_type="error"
                        # )
                        return result
 
                    # ---- 1b: within offset limits -> write real correction ----
                    else:
                        print(f"Dimension {dimension} is out of Tolerance Limit.")
                        # self.ui.status_manager.show(
                        # page_index=25,      # your probe page index
                        # message=f"Dimension {dimension} is out of Tolerance Limit.",
                        # timeout=2000,
                        # msg_type="error"
                        # )
                        self.show_message_signal.emit(f"Machine not selected or incorrect machine selection.", "error")
                        # msg = CustomMessageBox(
                        #     f"Dimension {dimension} is out of Tolerance Limit.",
                        #     "error", parent=self.ui
                        # )
                        # msg.exec_()
 
                        todo = update_wip_for_block_condition(triggered=True)
                        result["todo"] = todo
 
                        mean_r = mean#float(f"{mean:.3f}")
                        offs_r = offs#float(f"{offs:.3f}")
                        value = mean_r - offs_r
 
                        d = 0 if direction == "P" else 1
                        signed_value = ((-1) ** d) * round(value, 3)
                        signed_value = {'serve': signed_value}.get(todo, 0)
 
                        if trial_mode == 'OFF':
                            if controller == "FANUC":
                                instance = self.get_fanuc_instance(machine_name)
                                if not instance:
                                    result["status"] = "error"
                                    return result
                                var = self.fanuc_read(instance, offset_no, column)
                                self.fanuc_write(instance, offset_no, column, round(var, 3) + round(signed_value, 3))
                                z = self.fanuc_read(instance, offset_no, column)
                            elif controller == "HAAS NGC":
                                print("HAAS NGC write not implemented in CNCManager yet.")
                                result["status"] = "error"
                                return result
                            else:
                                result["status"] = "error"
                                return result
                        else:
                            self.trial_tool_value[dimension] = round(self.trial_tool_value[dimension] + signed_value, 3)
                            z = self.trial_tool_value[dimension]
 
                        result["tool_value"] = z
                        result["correction"] = signed_value if todo == 'serve' else 999.997
                        result["status"] = "written"
                        self.save_aoc_values(
                            aoc_id,
                            machine_name,
                            dimension,
                            part_name,
                            result["mean"],
                            offset_no,
                            offs,
                            result["correction"],
                            z,
                        )
                        return result
 
                # ================= BRANCH 2: offs inside [LSL, USL] =================
                else:
                    # ---- 2a: inside [LCL, UCL] -> write 0 (no correction needed) ----
                    # Use inclusive bounds so exact LCL/UCL values do not trigger correction.
                    if (offs > float(LCL)) and (offs < float(UCL)):
                        todo = update_wip_for_block_condition(triggered=False)
                        result["todo"] = todo
                        try:
                            z = read_cnc_val()
                        except Exception:
                            result["status"] = "error"
                            return result
 
                        result["tool_value"] = z
                        result["correction"] = 0.000
                        result["status"] = "zero_correction"
                        self.save_aoc_values(
                            aoc_id,
                            machine_name,
                            dimension,
                            part_name,
                            result["mean"],
                            offset_no,
                            offs,
                            result["correction"],
                            z,
                        )
                        return result
 
                    # ---- 2b: outside [LCL, UCL] -> skip-offset-count then correct ----
                    else:
                        todo = update_wip_for_block_condition(triggered=True)
                        result["todo"] = todo
 
                        mean_r = mean#float(f"{mean:.3f}")
                        offs_r = offs#float(f"{offs:.3f}")
                        value = mean_r - offs_r
 
                        d = 0 if direction == "P" else 1
                        is_skip_offset = False
 
                        if trial_mode == 'OFF':
                            if controller == "FANUC":
                                instance = self.get_fanuc_instance(machine_name)
                                if not instance:
                                    result["status"] = "error"
                                    return result
                                var = self.fanuc_read(instance, offset_no, column)
 
                                if skip_offset > skip_counter[dimension]:
                                    signed_value = 0.000
                                    is_skip_offset = True
                                    skip_counter[dimension] += 1
                                else:
                                    signed_value = ((-1) ** d) * round(value, 3)
                                    signed_value = {'serve': signed_value}.get(todo, 0)
                                    self.fanuc_write(instance, offset_no, column, round(var, 3) + round(signed_value, 3))
                                    skip_counter[dimension] = 0
 
                                z = self.fanuc_read(instance, offset_no, column)
                            elif controller == "HAAS NGC":
                                print("HAAS NGC write not implemented in CNCManager yet.")
                                result["status"] = "error"
                                return result
                            else:
                                result["status"] = "error"
                                return result
                        else:
                            if skip_offset > skip_counter[dimension]:
                                signed_value = 0.000
                                is_skip_offset = True
                                skip_counter[dimension] += 1
                            else:
                                signed_value = ((-1) ** d) * round(value, 3)
                                signed_value = {'serve': signed_value}.get(todo, 0)
                                skip_counter[dimension] = 0
                            self.trial_tool_value[dimension] = round(self.trial_tool_value[dimension] + signed_value, 3)
                            z = self.trial_tool_value[dimension]
 
                        result["tool_value"] = z
                        if todo == 'halt':
                            result["correction"] = 999.997
                        elif is_skip_offset:
                            result["correction"] = 999.998
                        else:
                            result["correction"] = signed_value
                        result["status"] = "skipped_offset" if is_skip_offset else "written"
                        self.save_aoc_values(
                            aoc_id,
                            machine_name,
                            dimension,
                            part_name,
                            result["mean"],
                            offset_no,
                            offs,
                            result["correction"],
                            z,
                        )
                        return result
 
            finally:
                # ✅ Always disconnect after read/write, regardless of branch/outcome
                if controller == "FANUC":
                    self.cleanup_fanuc(machine_name)
 
        except Exception as e:
            print(f"Error in process_reading_and_write_correction -> {e}")
            result["status"] = "error"
            # self.ui.status_manager.show(
            # page_index=25,      # your probe page index
            # message=f"Fanuc Connection Issues!!!",
            # timeout=2000,
            # msg_type="error"
            # )
            self.show_message_signal.emit(f"Fanuc Connection Issues!!!", "error")
            # msg = CustomMessageBox("Fanuc Connection Issues!!!", "error", parent=self.ui)
            # msg.exec_()
            try:
                if machine_name:
                    self.cleanup_fanuc(machine_name)
            except Exception:
                pass
            return result
         
    def cleanup_thread(self):

        self.aoc_worker.stop()

        self.aoc_thread.quit()

        self.aoc_thread.wait()