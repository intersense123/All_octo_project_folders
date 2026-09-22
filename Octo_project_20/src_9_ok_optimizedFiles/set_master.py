from PySide2.QtWidgets import QDialog, QLabel, QPushButton, QHBoxLayout, QVBoxLayout
from PySide2.QtCore import Qt
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import QObject, Signal
from models import *


class Set_master_ui(QDialog):
    def __init__(self, title_text, btn_text="OK"):
        super().__init__()

        self.setWindowTitle("")
        self.setFixedSize(500, 220)
        self.setWindowFlags(Qt.Dialog | QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)

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
        self.title_label.setStyleSheet("font-size: 18pt; font-weight: bold;")

        # ----- Live SPI Value Label -----
        # 🔴 4 LIVE SPI LABELS
        self.lbl_d1 = QLabel("D1: ---", alignment=Qt.AlignCenter)
        self.lbl_d2 = QLabel("D2: ---", alignment=Qt.AlignCenter)
        self.lbl_d3 = QLabel("D3: ---", alignment=Qt.AlignCenter)
        self.lbl_d4 = QLabel("D4: ---", alignment=Qt.AlignCenter)

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

    def showEvent(self, event):
        if self.parent():
            parent = self.parent()
            x = parent.x() + (parent.width() - self.width()) // 2
            y = parent.y() + (parent.height() - self.height()) // 2
            self.move(x, y)
        else:
            # fallback: center on screen
            screen = QtWidgets.QApplication.primaryScreen().availableGeometry()
            x = (screen.width() - self.width()) // 2
            y = (screen.height() - self.height()) // 2
            self.move(x, y)

        super().showEvent(event)


    # ---- Called from MainWindow when SPI emits ----
        # 🔴 SLOT CALLED BY SPI SIGNAL
    def update_spi_value(self, v1, v2, v3, v4):
        self.lbl_d1.setText(f"D1: {v1}")
        self.lbl_d2.setText(f"D2: {v2}")
        self.lbl_d3.setText(f"D3: {v3}")
        self.lbl_d4.setText(f"D4: {v4}")

    
    
    
class SetMasterController(QObject):
    """
    Handles Set Master workflow and master calculations.
    """
    master_finished = Signal(dict)   # Emits probe_data dict

    def __init__(self, parent, spi_values,spi_signal):
        super().__init__(parent)

        self.parent = parent
        self.spi_values = spi_values
        self.spi_signal = spi_signal   # 🔥 SPI live signal

        self.master_high = {}
        self.master_low = {}
        self.probe_data = {}
        self.master_ready = False

    def run(self):
        """
        Runs high master, low master, and calculation sequence.
        """
        try:
            # ---------- HIGH MASTER ----------
            popup_high = Set_master_ui("Set Higher Master")

            # 🔴 CONNECT SPI TO POPUP
            self.spi_signal.connect(popup_high.update_spi_value)

            popup_high.exec_()

            # 🔴 DISCONNECT AFTER CLOSE
            self.spi_signal.disconnect(popup_high.update_spi_value)

            # Store HIGH master values
            for probe, spi in self.spi_values.items():
                self.master_high[probe] = spi

            # ---------- LOW MASTER ----------
            popup_low = Set_master_ui("Set Lower Master")

            self.spi_signal.connect(popup_low.update_spi_value)
            popup_low.exec_()
            self.spi_signal.disconnect(popup_low.update_spi_value)

            # Store LOW master values
            for probe, spi in self.spi_values.items():
                self.master_low[probe] = spi

            # ---------- CALCULATION ----------
            self.calculate()

            popup_res = Set_master_ui("Master Set Successfully", "Close")
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

                raw_range = spi_high - spi_low
                if raw_range == 0:
                    print(f"[ERROR] {probe}: SPI high and low same")
                    continue

                DB_low = row.MasterLower
                DB_high = row.MasterHigher

                mm_per_raw = (DB_high - DB_low) / raw_range

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
