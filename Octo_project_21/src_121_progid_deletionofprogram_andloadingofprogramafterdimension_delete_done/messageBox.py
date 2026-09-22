from PySide2.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton,
    QVBoxLayout, QHBoxLayout, QMessageBox
)
from PySide2.QtCore import Qt
from PySide2.QtGui import QPixmap
from PySide2 import QtCore, QtWidgets
import sys


class CustomMessageBox(QtWidgets.QDialog):

    accepted = QtCore.Signal()
    rejected = QtCore.Signal()
    def __init__(self, message, msg_type="info", parent=None):
        try:
            super().__init__(parent)

            self.messages = message
            self.result = None  # True / False

            # self.setFixedSize(300, 220)

            # 🔑 SAME BEHAVIOR AS NUMPAD
            self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.CustomizeWindowHint)
            
            # self.showFullScreen()
            self.setStyleSheet("""
            QDialog {
                background-color: rgba(0,0,0,0);
            }

            #mainWidget {
                background-color: black;
                border: 3px solid white;
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
            self.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
            # self.setModal(True)
            # background-color: #444444;
            # Styles
            self.panel = QtWidgets.QWidget(self)
            self.panel.setFixedSize(300, 230)
            self.panel.setObjectName("mainWidget")
            
            # Icon
            self.icon_label = QLabel()
            self.icon_label.setFixedSize(40, 40)

            icon_map = {
                "success": "/home/torizon/app/src/images/success-40.png",
                "info": "/home/torizon/app/src/images/info-40.png",
                "error": "/home/torizon/app/src/images/error-40.png",
                "warning": "/home/torizon/app/src/images/warning_40.png",
            }

            icon_path = icon_map.get(msg_type.lower())
            if icon_path:
                self.icon_label.setPixmap(
                    QPixmap(icon_path).scaled(
                        40, 40, Qt.KeepAspectRatio, Qt.SmoothTransformation
                    )
                )

            # Message
            self.message_label = QLabel(self.messages)
            self.message_label.setWordWrap(True)
            self.message_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
            self.message_label.setFixedWidth(180)
            # Layouts
            h_layout = QHBoxLayout()
            h_layout.addWidget(self.icon_label)
            h_layout.addSpacing(7)
            h_layout.addWidget(self.message_label)

            button_layout = QHBoxLayout()

            if msg_type.lower() == "info":
                yes_btn = QPushButton("YES")
                no_btn = QPushButton("NO")

                yes_btn.setFixedSize(120, 50)
                no_btn.setFixedSize(120, 50)

                yes_btn.released.connect(self._accept)
                no_btn.released.connect(self._reject)

                button_layout.addWidget(yes_btn)
                button_layout.addWidget(no_btn)
            else:
                ok_btn = QPushButton("OK")
                ok_btn.setFixedSize(120, 50)
                ok_btn.released.connect(self._accept)
                button_layout.addWidget(ok_btn, alignment=Qt.AlignCenter)

            v_layout = QVBoxLayout(self.panel)
            v_layout.addStretch()
            v_layout.addLayout(h_layout)
            v_layout.addStretch()
            v_layout.addLayout(button_layout)
            v_layout.addSpacing(10)

        except Exception as e:
            QMessageBox.critical(self, "Init Error", str(e))
        
    # def center_on_parent(self):
    #     self.panel.move(
    #         (self.width() - self.panel.width()) // 2,
    #         (self.height() - self.panel.height()) // 2
    #     )
    #     # if self.parent():
    #     #     parent_rect = self.parent().frameGeometry()
    #     #     self_rect = self.frameGeometry()
    #     #     self_rect.moveCenter(parent_rect.center())
    #     #     self.move(self_rect.topLeft())
    
    

    # ---------- behavior like dialog ----------
    def _accept(self):
        try:
            # Accept the dialog and emit the accepted signal
            self.result = True
            self.accept()
            self.accepted.emit()
            self.close()
        except Exception as e:
            QMessageBox.critical(self, "Accept Error", str(e))

    def _reject(self):
        try:
            # Reject the dialog and emit the rejected signal
            self.result = False
            self.reject()
            self.rejected.emit()
            self.close()
        except Exception as e:
            QMessageBox.critical(self, "Reject Error", str(e))
    
    def exec_(self):
        try:
            # Center the dialog before executing it safely
            if self.parent():
                self.setGeometry(self.parent().rect())
            else:
                self.setGeometry(
                    QtWidgets.QApplication.primaryScreen().geometry()
                )

            self.panel.move(
                (self.width() - self.panel.width()) // 2,
                (self.height() - self.panel.height()) // 2
            )

            return super().exec_()
        except Exception as e:
            QMessageBox.critical(self, "Execution Error", str(e))
            return -1

    # def exec_(self):
    #     self.show()
    #     QtCore.QTimer.singleShot(0, self.center_on_parent)

    #     loop = QtCore.QEventLoop()
    #     self.destroyed.connect(loop.quit)
    #     loop.exec_()
    #     return self.result


# ---------- TEST ----------
if __name__ == "__main__":
    app = QApplication(sys.argv)

    main = QWidget()
    main.setFixedSize(800, 480)
    main.show()

    msg = CustomMessageBox(
        "Do you really want to logout?",
        "info",
        parent=main
    )
    result = msg.exec_()
    print("Result:", result)

    sys.exit(app.exec_())
