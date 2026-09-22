from PySide2.QtWidgets import QApplication, QMainWindow, QStackedWidget , QWidget
from PySide2.QtWidgets import QFrame
from PySide2.QtWidgets import QLineEdit
from PySide2 import QtCore, QtWidgets
from PySide2.QtCore import QTimer, QSize, QDate , QObject , QThread , Signal, Qt, QCoreApplication
from PySide2.QtGui import QPixmap
from messageBox import CustomMessageBox
from models import *
from models import SessionLocal , UserManagement
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