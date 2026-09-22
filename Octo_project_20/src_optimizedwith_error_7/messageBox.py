from PySide2.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton,
    QVBoxLayout, QHBoxLayout, QMessageBox
)
from PySide2.QtCore import Qt
from PySide2.QtGui import QPixmap
from PySide2 import QtCore, QtWidgets
import sys


class CustomMessageBox(QtWidgets.QWidget):
    accepted = QtCore.Signal()
    rejected = QtCore.Signal()
    def __init__(self, message, msg_type="info", parent=None):
        try:
            super().__init__(parent)

            self.messages = message
            self.result = None  # True / False

            self.setFixedSize(540, 240)

            # 🔑 SAME BEHAVIOR AS NUMPAD
            self.setWindowFlags(
                QtCore.Qt.Tool |
                QtCore.Qt.FramelessWindowHint |
                QtCore.Qt.WindowStaysOnTopHint
            )

            self.setAttribute(QtCore.Qt.WA_StyledBackground, True)

            # Center relative to parent (like numpad)
            if parent:
                geo = parent.geometry()
                self.move(
                    geo.center().x() - self.width() // 2,
                    geo.center().y() - self.height() // 2
                )
            else:
                screen = QApplication.primaryScreen().availableGeometry()
                self.move(
                    screen.center().x() - self.width() // 2,
                    screen.center().y() - self.height() // 2
                )

            # Styles
            self.setStyleSheet("""
                QWidget {
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

            # Icon
            self.icon_label = QLabel()
            self.icon_label.setFixedSize(64, 64)

            icon_map = {
                "success": "/home/torizon/app/src/success-1.png",
                "info": "/home/torizon/app/src/info-1.png",
                "error": "/home/torizon/app/src/error-1.png",
                "warning": "/home/torizon/app/src/warning.png",
            }

            icon_path = icon_map.get(msg_type.lower())
            if icon_path:
                self.icon_label.setPixmap(
                    QPixmap(icon_path).scaled(
                        64, 64, Qt.KeepAspectRatio, Qt.SmoothTransformation
                    )
                )

            # Message
            self.message_label = QLabel(self.messages)
            self.message_label.setWordWrap(True)
            self.message_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

            # Layouts
            h_layout = QHBoxLayout()
            h_layout.addWidget(self.icon_label)
            h_layout.addSpacing(15)
            h_layout.addWidget(self.message_label)

            button_layout = QHBoxLayout()

            if msg_type.lower() == "info":
                yes_btn = QPushButton("YES")
                no_btn = QPushButton("NO")

                yes_btn.setFixedSize(120, 50)
                no_btn.setFixedSize(120, 50)

                yes_btn.clicked.connect(self._accept)
                no_btn.clicked.connect(self._reject)

                button_layout.addWidget(yes_btn)
                button_layout.addWidget(no_btn)
            else:
                ok_btn = QPushButton("OK")
                ok_btn.setFixedSize(120, 50)
                ok_btn.clicked.connect(self._accept)
                button_layout.addWidget(ok_btn, alignment=Qt.AlignCenter)

            v_layout = QVBoxLayout(self)
            v_layout.addStretch()
            v_layout.addLayout(h_layout)
            v_layout.addStretch()
            v_layout.addLayout(button_layout)
            v_layout.addSpacing(10)

        except Exception as e:
            QMessageBox.critical(self, "Init Error", str(e))

    # ---------- behavior like dialog ----------
    def _accept(self):
        self.accepted.emit()
        self.close()

    def _reject(self):
        self.rejected.emit()
        self.close()

    def exec_(self):
        self.show()
        loop = QtCore.QEventLoop()
        self.destroyed.connect(loop.quit)
        loop.exec_()
        return self.result


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
