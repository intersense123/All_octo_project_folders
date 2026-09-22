from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtGui import QFont

class Ui_Numpad(object):
    def setupUi(self, Numpad, on_input=None):
        try:
            self.on_input = on_input
            self.Numpad = Numpad
            self.Numpad.setObjectName("Numpad")
            self.Numpad.resize(300, 470)
            self.Numpad.setMinimumSize(QtCore.QSize(300, 470))
            self.Numpad.setMaximumSize(QtCore.QSize(300, 470))
            self.Numpad.setStyleSheet("background-color: #2e2e2e;")  # dark grey background

            self.verticalLayout = QtWidgets.QVBoxLayout(self.Numpad)
            # Header layout
            self.headerLayout = QtWidgets.QHBoxLayout()
            self.headerLayout.setContentsMargins(0, 0, 0, 10)

            self.headerLabel = QtWidgets.QLabel("Numpad", self.Numpad)
            self.headerLabel.setStyleSheet("color: white; font-size: 15px;")
            self.headerLayout.addWidget(self.headerLabel)

            self.closeButton = QtWidgets.QPushButton("X", self.Numpad)
            self.closeButton.setFixedSize(30, 30)
            self.closeButton.setStyleSheet("background-color: #aa0000; color: white; font-size: 14px; border-radius: 5px;")
            self.closeButton.clicked.connect(self.close_numpad)
            self.headerLayout.addWidget(self.closeButton)

            self.verticalLayout.addLayout(self.headerLayout)
            self.horizontalLayout = QtWidgets.QHBoxLayout()
            
            # Input box
            self.Input_box = QtWidgets.QLineEdit(self.Numpad)
            self.Input_box.setFont(QFont("", 15))
            self.Input_box.setStyleSheet("color: white; background-color: #444444; padding: 5px;")
            self.Input_box.setObjectName("Input_box")
            self.horizontalLayout.addWidget(self.Input_box)
            self.verticalLayout.addLayout(self.horizontalLayout)
            

            # Grid layout for buttons
            self.gridLayout = QtWidgets.QGridLayout()
            self.buttons = {}

            button_names = [
                ('1', 0, 0), ('2', 0, 1), ('3', 0, 2),
                ('4', 1, 0), ('5', 1, 1), ('6', 1, 2),
                ('7', 2, 0), ('8', 2, 1), ('9', 2, 2),
                ('0', 3, 0), ('.', 3, 1), ('+', 3, 2),
                ('-', 4, 0), ('<-', 4, 1), ('OK', 4, 2)
            ]

            for name, row, col in button_names:
                btn = QtWidgets.QPushButton(name, self.Numpad)
                btn.setMinimumSize(QtCore.QSize(90, 60))
                btn.setMaximumSize(QtCore.QSize(90, 60))
                btn.setStyleSheet("color: white; background-color: #555555; font: 14pt 'MS Shell Dlg 2';")
                self.gridLayout.addWidget(btn, row, col, 1, 1)
                self.buttons[name] = btn

            self.verticalLayout.addLayout(self.gridLayout)

            # Connect buttons safely
            for i in range(10):
                self.buttons[str(i)].clicked.connect(self.make_number_handler(str(i)))

            self.buttons['.'].clicked.connect(self.make_number_handler('.'))
            self.buttons['+'].clicked.connect(self.make_number_handler('+'))
            self.buttons['-'].clicked.connect(self.make_number_handler('-'))
            self.buttons['<-'].clicked.connect(self.pushButton_erase_clicked)

            self.retranslateUi(self.Numpad)
            QtCore.QMetaObject.connectSlotsByName(self.Numpad)

        except Exception as e:
            QtWidgets.QMessageBox.critical(Numpad, "Setup UI Error", str(e))

    def close_numpad(self):
        self.Numpad.close()
        self.numpadClosed.emit()
    
    # Helper to safely connect buttons
    def make_number_handler(self, char):
        try:
            def handler(checked=False):
                try:
                    self.Input_box.setText(self.Input_box.text() + char)
                except Exception as e:
                    QtWidgets.QMessageBox.critical(self.Numpad, "Input Error", str(e))
            return handler
        except Exception as e:
            QtWidgets.QMessageBox.critical(self.Numpad, "Handler Error", str(e))
            return lambda checked=False: None

    def pushButton_erase_clicked(self, checked=False):
        try:
            text = self.Input_box.text()
            self.Input_box.setText(text[:-1])
        except Exception as e:
            QtWidgets.QMessageBox.critical(self.Numpad, "Erase Error", str(e))

    def retranslateUi(self, Numpad):
        try:
            Numpad.setWindowTitle("Virtual Numpad")
        except Exception as e:
            QtWidgets.QMessageBox.critical(Numpad, "Translate UI Error", str(e))


class numpad_window(Ui_Numpad, QtWidgets.QWidget):
    # Signal to notify when numpad is closed
    numpadClosed = QtCore.Signal()
    
    def __init__(self, target_lineedit=None, parent=None):
        try:
            super().__init__(parent)
            self.setupUi(self)
            self.target_lineedit = target_lineedit
            self.buttons['OK'].clicked.connect(self.push_buttonsubmit_clicked)
            # self.setWindowFlags(
            #     QtCore.Qt.FramelessWindowHint |
            #     QtCore.Qt.WindowStaysOnTopHint |
            #     QtCore.Qt.Tool
            # )

            # self.setWindowModality(QtCore.Qt.NonModal)
            self.setAttribute(QtCore.Qt.WA_StyledBackground, True)
            

        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Init Error", str(e))
        
        
    # def show_numpad(self):
    #     screen = QtWidgets.QApplication.primaryScreen()
    #     self.setGeometry(screen.geometry())
    #     self.exec_()
    def showEvent(self, event):
        parent = self.parentWidget()
        if parent:
            geo = parent.rect()
            self.move(
                (geo.width() - self.width()) // 2,
                geo.height() - self.height() - 10
            )
        super().showEvent(event)
    # def showEvent(self, event):
    #     try:
    #         # ✅ Load existing value into numpad
    #         # if self.target_lineedit:
    #         #     self.Input_box.setText(self.target_lineedit.text())

    #         parent = self.parentWidget()
    #         if parent:
    #             geo = parent.rect()
    #             self.move(
    #                 (geo.width() - self.width()) // 2,
    #                 geo.height() - self.height() - 10
    #             )

    #     except Exception as e:
    #         print(f"Error in showEvent: {e}")

    #     super().showEvent(event)
        

    def push_buttonsubmit_clicked(self):
        try:
            if self.target_lineedit:
                self.target_lineedit.setText(self.Input_box.text())
                self.target_lineedit.parentWidget().setFocus()

            # ❌ REMOVE THIS LINE
            # self.Input_box.clear()

            self.close() # self.hide() if you want full close
            self.numpadClosed.emit()

        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Submit Error", str(e))


if __name__ == "__main__":
    try:
        import sys
        app = QtWidgets.QApplication(sys.argv)
        numpad = numpad_window()
        #numpad.show_numpad()
        sys.exit(app.exec_())
    except Exception as e:
        QtWidgets.QMessageBox.critical(None, "Application Error", str(e))
