from PySide2 import QtWidgets, QtCore, QtGui
from PySide2.QtCore import QSize, QRect, QMetaObject, QCoreApplication
from PySide2.QtGui import QFont
from PySide2.QtCore import Qt


class Ui_fact_config(object):
    def setupUi(self, Dialog):
        try:
            if not Dialog.objectName():
                Dialog.setObjectName(u"Dialog")
            Dialog.resize(200, 230)
            Dialog.setMaximumSize(QSize(200, 250))

            self.comboBox = QtWidgets.QComboBox(Dialog)
            for _ in range(5):
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
            items = ["A", "B", "C", "D", "E"]
            for i, text in enumerate(items):
                self.comboBox.setItemText(i, QCoreApplication.translate("Dialog", text, None))
            self.pushButton.setText(QCoreApplication.translate("Dialog", u"OK", None))
        except Exception as e:
            QtWidgets.QMessageBox.critical(Dialog, "Retranslate UI Error", str(e))

class FactoryConfig(Ui_fact_config, QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # self.setWindowFlags(
        #     Qt.FramelessWindowHint |
        #     Qt.WindowStaysOnTopHint |
        #     Qt.Tool
        # )

        self.setAttribute(Qt.WA_StyledBackground, True)

        self.setStyleSheet("background-color: grey;")
        self.comboBox.setStyleSheet("background-color: grey;color: white;")
        self.pushButton.setStyleSheet("color: white;")

        self.pushButton.clicked.connect(self.close)
        
    def showEvent(self, event):
        parent = self.parentWidget()
        if parent:
            parent_geo = parent.geometry()  # GLOBAL coordinates

            x = parent_geo.x() + (parent_geo.width() - self.width()) // 2
            y = parent_geo.y() + (parent_geo.height() - self.height()) // 2

            self.move(x, y)

        super().showEvent(event)


if __name__ == "__main__":
    try:
        import sys
        app = QtWidgets.QApplication(sys.argv)
        window = FactoryConfig()
        window.show()
        sys.exit(app.exec_())
    except Exception as e:
        QtWidgets.QMessageBox.critical(None, "Application Error", str(e))
