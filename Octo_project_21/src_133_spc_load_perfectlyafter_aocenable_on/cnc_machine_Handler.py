from PySide2.QtWidgets import QApplication, QMainWindow, QStackedWidget , QWidget
from PySide2.QtWidgets import QFrame
from PySide2.QtWidgets import QLineEdit
from PySide2 import QtCore, QtWidgets
from PySide2.QtCore import QTimer, QSize, QDate , QObject , QThread , Signal, Qt, QCoreApplication
from PySide2.QtGui import QPixmap
from messageBox import CustomMessageBox
from models import *
from models import SessionLocal , AOCBasedSettings,CNCMaster
from sqlalchemy.orm import Session , sessionmaker
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from PySide2.QtGui import QStandardItemModel, QStandardItem
from FanucLibDefs import FANUCDEFS
import subprocess

class CNCManager(QObject):
    def __init__(self, main_window):
        try:
            super().__init__(parent=None)
            self.ui = main_window
            self.ui.button_ping.clicked.connect(self.ping_button_clicked)
            # dict to hold cnc connection details, keyed by (program_id, dimension)
            self.cnc_details_dict = {}

            # Connect to DataHandler's signal once data_handler exists on ui
            if hasattr(self.ui, "data_handler"):
                self.ui.data_handler.aoc_settings_saved.connect(self.on_aoc_settings_saved)
        except Exception as e:
            print(f"Error in CNCManager -> {e}")

    def ping_button_clicked(self,event):
        
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
    
    def get_cnc_details_for_program(self, program_id, dimension):
        """
        Given a ProgramId and Dimension, walk:
        ProgramId -> Dimension -> AOCBasedSettings (Machine) -> CNCMaster (match CNCName)
        Returns a dict with IPAddress, PortNumber, CNCSelection, ControllerName
        (also cached on self.cnc_connection_details), or None if not found.
        """
        try:
            session = SessionLocal()
            try:
                # Step 1: Get AOC based settings row for this program + dimension
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
 
                # Step 2: Match Machine name against CNCMaster.CNCName
                cnc_row = session.query(CNCMaster).filter_by(
                    CNCName=machine_name
                ).first()
 
                if not cnc_row:
                    print(f"No CNCMaster entry found for machine name '{machine_name}'")
                    return None
 
                # Step 3: Grab required fields and store them
                self.cnc_connection_details = {
                    "CNCName": cnc_row.CNCName,
                    "IPAddress": cnc_row.IPAddress,
                    "PortNumber": cnc_row.PortNumber,
                    "CNCSelection": cnc_row.CNCSelection,
                    "ControllerName": cnc_row.ControllerName,
                }
                return self.cnc_connection_details
 
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
            details = self.get_cnc_details_for_program(program_id, dimension)
            if details:
                self.cnc_details_dict[(program_id, dimension)] = details
                print(self.cnc_details_dict)
        except Exception as e:
            print(f"Error in on_aoc_settings_saved -> {e}")   
    
    def operate_string(self):
        pass