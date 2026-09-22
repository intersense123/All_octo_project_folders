from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtGui import QFont

class Ui_Formulabar(object):
    def __init__(self, target_lineedit=None, parent=None):
        try:
            super().__init__(parent)
            self.setupUi(self)
            self.target_lineedit = target_lineedit
            self.buttons['OK'].clicked.connect(self.push_buttonsubmit_clicked)
            self.setWindowFlags(QtCore.Qt.FramelessWindowHint |
                                QtCore.Qt.WindowStaysOnTopHint |
                                QtCore.Qt.CustomizeWindowHint)
            self.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        except Exception as e:
            print(f"Error initializing formula bar: {e}")

    def show_numpad(self):
        try:
            self.exec_()
        except Exception as e:
            print(f"Error showing numpad: {e}")

    def push_buttonsubmit_clicked(self):
        try:
            # Set the target field and close the dialog safely
            if self.target_lineedit:
                self.target_lineedit.setText(self.Input_box.text())
            self.close()
        except Exception as e:
            print(f"Error submitting formula input: {e}")
        # if self.Input_box.text() != "":
        #     self.numberSet = self.Input_box.text()
        # self.output = str(self.Input_box.text())
        # if self.on_input is not None:
        #     self.on_input(self.output)
        # self.close()
