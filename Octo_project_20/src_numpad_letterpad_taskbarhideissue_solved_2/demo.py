from PySide2.QtWidgets import QApplication, QDialog, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from PySide2.QtCore import Qt
from PySide2.QtGui import QPixmap
import sys

class CustomMessageBox(QDialog):
    def __init__(self, message, msg_type="info"):
        super().__init__()
        self.messages = message
        self.setWindowTitle("")
        self.setFixedSize(540, 240)
        self.setWindowFlags(Qt.Dialog | Qt.FramelessWindowHint)

        # Styles
        self.setStyleSheet("""
            QDialog {
                background-color: #444444;   /* grey */
                border-radius: 10px;
            }
            QLabel {
                color: black;                /* Black text for visibility */
                font-size: 16pt;
            }
            QPushButton {
                background-color: #1E90FF;   /* DodgerBlue */
                color: white;
                font-size: 14pt;
                border-radius: 5px;
                padding: 10px 20px;
            }
            QPushButton:hover {
                background-color: #187bcd;   /* Darker blue */
            }
        """)

        # Icon based on type
        icon_label = QLabel()
        icon_label.setFixedSize(64, 64)
        if msg_type.lower() == "success":
            icon_label.setPixmap(QPixmap("success-1.png").scaled(64,64, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        elif msg_type.lower() == "info":
            icon_label.setPixmap(QPixmap("info-1.png").scaled(64,64, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        elif msg_type.lower() == "error":
            icon_label.setPixmap(QPixmap("error-1.png").scaled(64,64, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        elif msg_type.lower() == "warning":
            icon_label.setPixmap(QPixmap("warning.png").scaled(64,64, Qt.KeepAspectRatio, Qt.SmoothTransformation))

        # Message label
        message_label = QLabel(self.messages)
        message_label.setWordWrap(True)
        message_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        # Layout for icon + message
        h_layout = QHBoxLayout()
        h_layout.addWidget(icon_label)
        h_layout.addSpacing(15)
        h_layout.addWidget(message_label)

        # Button layout
        button_layout = QHBoxLayout()
        if msg_type.lower() == "info":
            yes_button = QPushButton("YES")
            yes_button.setFixedSize(120, 50)
            yes_button.clicked.connect(self.accept)

            no_button = QPushButton("NO")
            no_button.setFixedSize(120, 50) 
            no_button.clicked.connect(self.reject)

            button_layout.addWidget(yes_button)
            button_layout.addWidget(no_button)
        else:
            ok_button = QPushButton("OK")
            ok_button.setFixedSize(120, 50)
            ok_button.clicked.connect(self.accept)
            button_layout.addWidget(ok_button, alignment=Qt.AlignCenter)

        # Main layout
        v_layout = QVBoxLayout()
        v_layout.addStretch()
        v_layout.addLayout(h_layout)
        v_layout.addStretch()
        v_layout.addLayout(button_layout)
        v_layout.addSpacing(10)

        self.setLayout(v_layout)

    def accept_data(self):
        if self.messages == "  Do you really want to Shutdown?":
            pass
        elif self.messages == "  Do you really want to Restart?":
            pass


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Example usage
    dlg = CustomMessageBox("Operation completed successfully!", "success")
    dlg.exec_()

    dlg2 = CustomMessageBox("This is an information message.", "info")
    dlg2.exec_()

    dlg3 = CustomMessageBox("Something went wrong!!!", "error")
    dlg3.exec_()
