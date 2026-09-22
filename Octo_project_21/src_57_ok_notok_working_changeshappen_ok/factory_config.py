from PySide2 import QtWidgets, QtCore, QtGui
from PySide2.QtCore import QSize, QRect, QMetaObject, QCoreApplication
from PySide2.QtCore import QObject, Signal,QSettings
from PySide2.QtGui import QFont
from PySide2.QtCore import Qt
from models import SessionLocal, FactoryConfigSettings
from sqlalchemy.orm import sessionmaker


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

            self.button_factory_ok = QtWidgets.QPushButton(Dialog)
            self.button_factory_ok.setObjectName(u"button_factory_ok")
            self.button_factory_ok.setGeometry(QRect(60, 130, 61, 41))
            sizePolicy.setHeightForWidth(self.button_factory_ok.sizePolicy().hasHeightForWidth())
            self.button_factory_ok.setSizePolicy(sizePolicy)
            self.button_factory_ok.setMaximumSize(QSize(250, 250))
            self.button_factory_ok.setFont(font)

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
            self.button_factory_ok.setText(QCoreApplication.translate("Dialog", u"OK", None))
        except Exception as e:
            QtWidgets.QMessageBox.critical(Dialog, "Retranslate UI Error", str(e))


class FactoryConfig(QtWidgets.QDialog, Ui_fact_config):
    config_changed = Signal(str)
    def __init__(self, parent=None,current_factory=None):
        super().__init__(parent)
        self.setupUi(self)
        
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.CustomizeWindowHint)
        #self.showFullScreen()
        self.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)


        # self.setAttribute(Qt.WA_StyledBackground, True)

        self.setStyleSheet("background-color: grey;")
        self.comboBox.setStyleSheet("background-color: grey;color: white;")
        self.button_factory_ok.setStyleSheet("color: white;")
        # 🔥 LOAD FROM DB if not provided
        if current_factory is None:
            current_factory = self.load_factory_from_db()
            
         # 🔥 restore previous selection
        index = self.comboBox.findText(current_factory)
        if index != -1:
            self.comboBox.setCurrentIndex(index)

        self.button_factory_ok.clicked.connect(self.on_ok_clicked)
        
    def showEvent(self, event):
        parent = self.parentWidget()
        if parent:
            parent_geo = parent.geometry()  # GLOBAL coordinates

            x = parent_geo.x() + (parent_geo.width() - self.width()) // 2
            y = parent_geo.y() + (parent_geo.height() - self.height()) // 2

            self.move(x, y)

        super().showEvent(event)
    

    def save_factory_to_db(self, factory):
        with SessionLocal() as session:
            try:
                row = session.query(FactoryConfigSettings).first()

                if row:
                    row.factory_config = factory
                else:
                    session.add(FactoryConfigSettings(factory_config=factory))
                
                # print("Data saved to db:")

                session.commit()
            except Exception as e:
                session.rollback()
                print("DB Error:", e)

    def load_factory_from_db(self):
        with SessionLocal() as session:
            try:
                row = session.query(FactoryConfigSettings).first()
                if row and row.factory_config:
                    return row.factory_config
            except Exception as e:
                print("DB Load Error:", e)
        return None
   
    def on_ok_clicked(self):
        config = self.comboBox.currentText()   # 👈 HERE
        # print("config:",config)
        self.save_factory_to_db(config) 
        self.config_changed.emit(config)       # send value out
        self.accept()

if __name__ == "__main__":
    try:
        import sys
        app = QtWidgets.QApplication(sys.argv)
        window = FactoryConfig()
        window.show()
        sys.exit(app.exec_())
    except Exception as e:
        QtWidgets.QMessageBox.critical(None, "Application Error", str(e))

