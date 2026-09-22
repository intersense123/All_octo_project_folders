from PySide2 import QtWidgets, QtCore, QtGui
from PySide2.QtCore import QSize, QRect, QMetaObject, QCoreApplication
from PySide2.QtGui import QFont

class Ui_fact_config(object):
    def setupUi(self, Dialog):
        try:
            if not Dialog.objectName():
                Dialog.setObjectName(u"Dialog")
            Dialog.resize(200, 230)
            Dialog.setMaximumSize(QSize(200, 250))

            self.comboBox = QtWidgets.QComboBox(Dialog)
            for _ in range(8):
                self.comboBox.addItem("")
            self.comboBox.setObjectName(u"comboBox")
            self.comboBox.setGeometry(QRect(60, 30, 61, 41))

            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
            self.comboBox.setSizePolicy(sizePolicy)
            self.comboBox.setMaximumSize(QSize(250, 250))

            font = QFont()
            font.setPointSize(20)
            self.comboBox.setFont(font)

            self.pushButton = QtWidgets.QPushButton(Dialog)
            self.pushButton.setObjectName(u"pushButton")
            self.pushButton.setGeometry(QRect(60, 130, 61, 41))
            sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
            self.pushButton.setSizePolicy(sizePolicy)
            self.pushButton.setMaximumSize(QSize(250, 250))
            self.pushButton.setFont(font)

            self.retranslateUi(Dialog)
            QMetaObject.connectSlotsByName(Dialog)
        except Exception as e:
            QtWidgets.QMessageBox.critical(Dialog, "Setup UI Error", str(e))

    def retranslateUi(self, Dialog):
        try:
            Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
            items = ["A", "B", "C", "D", "E", "F", "G", "H"]
            for i, text in enumerate(items):
                self.comboBox.setItemText(i, QCoreApplication.translate("Dialog", text, None))
            self.pushButton.setText(QCoreApplication.translate("Dialog", u"OK", None))
        except Exception as e:
            QtWidgets.QMessageBox.critical(Dialog, "Retranslate UI Error", str(e))

class FactoryConfig(QtWidgets.QDialog, Ui_fact_config):
    def __init__(self, parent=None):
        try:
            super().__init__(parent)
            self.setupUi(self)

            self.setWindowFlags(QtCore.Qt.FramelessWindowHint |
                                QtCore.Qt.WindowStaysOnTopHint |
                                QtCore.Qt.CustomizeWindowHint)
            self.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
            self.setModal(True)

            # ---- Styling ----
            self.setStyleSheet("background-color: grey;")  # background
            self.comboBox.setStyleSheet("color: white;")   # combobox text
            self.pushButton.setStyleSheet("color: white;") # button text

            # ---- Connect OK button ----
            self.pushButton.clicked.connect(self.accept)  # closes dialog

        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Initialization Error", str(e))

if __name__ == "__main__":
    try:
        import sys
        app = QtWidgets.QApplication(sys.argv)
        window = FactoryConfig()
        window.show()
        sys.exit(app.exec_())
    except Exception as e:
        QtWidgets.QMessageBox.critical(None, "Application Error", str(e))
