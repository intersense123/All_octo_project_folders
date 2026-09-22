from PySide2.QtWidgets import QApplication, QDialog, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox
from PySide2.QtCore import Qt
from PySide2.QtGui import QPixmap
from PySide2 import QtCore, QtGui, QtWidgets
import sys
import os

class CustomMessageBox(QtWidgets.QDialog):
    def __init__(self, message, msg_type="info"):
        try:
            super().__init__()
            self.messages = message
            self.setWindowTitle("")
            self.setFixedSize(540, 240)
            # Set window flags to hide taskbar effectively
            self.setWindowFlags(
            QtCore.Qt.Tool |
            QtCore.Qt.FramelessWindowHint |
            QtCore.Qt.WindowStaysOnTopHint |
            QtCore.Qt.BypassWindowManagerHint |
            QtCore.Qt.X11BypassWindowManagerHint
            )
            
            # Use QScreen geometry to get full screen dimensions including taskbar area
            screen = QApplication.primaryScreen()
            screen_geometry = screen.geometry()
            self.setGeometry(screen_geometry)
            self.setWindowModality(Qt.ApplicationModal)
            self.setAttribute(QtCore.Qt.WA_StyledBackground, True)

            # self.showFullScreen()

            # Styles
            self.setStyleSheet("""
                QDialog {
                    background-color: #444444;   /* grey */
                    border-radius: 10px;
                }
                QLabel {
                    color: White;                
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

            # Icon based on type
            self.icon_label = QLabel()
            self.icon_label.setFixedSize(64, 64)
            try:
                if msg_type.lower() == "success":
                    self.icon_label.setPixmap(QPixmap("success-1.png").scaled(64,64, Qt.KeepAspectRatio, Qt.SmoothTransformation))
                elif msg_type.lower() == "info":
                    self.icon_label.setPixmap(QPixmap("info-1.png").scaled(64,64, Qt.KeepAspectRatio, Qt.SmoothTransformation))
                elif msg_type.lower() == "error":
                    self.icon_label.setPixmap(QPixmap("error-1.png").scaled(64,64, Qt.KeepAspectRatio, Qt.SmoothTransformation))
                elif msg_type.lower() == "warning":
                    self.icon_label.setPixmap(QPixmap("warning.png").scaled(64,64, Qt.KeepAspectRatio, Qt.SmoothTransformation))
            except Exception as e:
                QMessageBox.critical(self, "Icon Error", f"Failed to load icon: {str(e)}")

            # Message label
            self.message_label = QLabel(self.messages)
            self.message_label.setWordWrap(True)
            self.message_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

            # Layout for icon + message
            self.h_layout = QHBoxLayout()
            self.h_layout.addWidget(self.icon_label)
            self.h_layout.addSpacing(15)
            self.h_layout.addWidget(self.message_label)

            # Button layout
            self.button_layout = QHBoxLayout()
            try:
                if msg_type.lower() == "info":
                    self.yes_button = QPushButton("YES")
                    self.yes_button.setFixedSize(120, 50)
                    self.yes_button.clicked.connect(self.accept)

                    self.no_button = QPushButton("NO")
                    self.no_button.setFixedSize(120, 50)
                    self.no_button.clicked.connect(self.reject)

                    self.button_layout.addWidget(self.yes_button)
                    self.button_layout.addWidget(self.no_button)
                else:
                    self.ok_button = QPushButton("OK")
                    self.ok_button.setFixedSize(120, 50)
                    self.ok_button.clicked.connect(self.accept)
                    self.button_layout.addWidget(self.ok_button, alignment=Qt.AlignCenter)
            except Exception as e:
                QMessageBox.critical(self, "Button Layout Error", str(e))

            # Main layout
            self.v_layout = QVBoxLayout()
            self.v_layout.addStretch()
            self.v_layout.addLayout(self.h_layout)
            self.v_layout.addStretch()
            self.v_layout.addLayout(self.button_layout)
            self.v_layout.addSpacing(10)

            self.setLayout(self.v_layout)

        except Exception as e:
            QMessageBox.critical(self, "Initialization Error", str(e))
    
        
    def accept_data(self):
        try:
            if self.messages == "  Do you really want to Shutdown?":
                # add shutdown logic here
                pass
            elif self.messages == "  Do you really want to Restart?":
                # add restart logic here
                pass
        except Exception as e:
            QMessageBox.critical(self, "Accept Data Error", str(e))


if __name__ == "__main__":
    try:
        app = QApplication(sys.argv)
        dlg = CustomMessageBox("This is an info message", msg_type="info")
        dlg.exec_()
        sys.exit(app.exec_())
    except Exception as e:
        QMessageBox.critical(None, "Application Error", str(e))
