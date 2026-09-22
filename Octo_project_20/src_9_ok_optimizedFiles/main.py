import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import Qt, QThread
from PySide2.QtWidgets import QApplication, QMainWindow, QStackedWidget , QWidget


# UI (Qt Designer)
from main_ui_18 import Ui_MainWindow

# Separated modules
from ui_handler import UIHandler
from controller import AppController
from data_handler import DataHandler
from database import DatabaseAgent
from value import Value
from utilities import Utilities
from active_ui_handler import *

class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        
        # -------------------------------------------------
        # SETUP UI
        # -------------------------------------------------
        self.setupUi(self)  # setup UI
        self.utils = Utilities(self.label_time, self.label_date, self.lineEdit_formulaBar)

        # -------------------------------------------------
        # INIT UI HANDLER
        # -------------------------------------------------
        self.valueObj = Value()
        self.databaseObj = DatabaseAgent()
        
        self.ui_handler = UIHandler(main_window=self) 
        
        self.stacked: QStackedWidget = getattr(self, "stackedWidget_main", None)
        if self.stacked:
                # Connecting Slot When Page Changes
                self.stacked.currentChanged.connect(self.ui_handler.set_labels_to_header)
                self.stacked.setCurrentIndex(0)  # second page       
        
        
        # self.comboBox_toselectProbe.clear()
        self.stackedWidget_2.setCurrentIndex(0)
        
        self.valueObj.init_AngleCalculationSettings_dictionary()
        self.valueObj.init_mainProgramSettings_dictionary()
             
        
        self.utils.start_clock_updates()
        
        
        # ActiveProgramId Loaded Before
        # Load from DB first
        self.valueObj.AngleCalculationSettings_dict = self.databaseObj.load_data_to_AngleCalculationSettings_dict(self.valueObj.activeVariables_dict.get("ActiveProgramId", 1))
        
        # Load Active Program Id
        self.comboBox_programIdSetting.setCurrentText(str(self.valueObj.activeVariables_dict["ActiveProgramId"]))
        
        
        
        # Set Inner Program Id To The Active Id
        self.comboBox_programIdSettings.setCurrentText(str(self.valueObj.activeVariables_dict["ActiveProgramId"]))
        # self.comboBox_programIdSetting.setCurrentText(str(self.valueObj.activeVariables_dict["ActiveProgramId"]))
        
        
        # -------------------------------------------------
        # INIT DATA HANDLER
        # -------------------------------------------------
        self.data_handler = DataHandler(main_window=self,
                                        uiHandler = self.ui_handler)

        # -------------------------------------------------
        # INIT CONTROLLER
        # -------------------------------------------------
        self.controller = AppController(
            main_window=self,
            data_handler=self.data_handler
        )
        


if __name__ == "__main__":
    try:
        
        app = QApplication(sys.argv)

        window = MainWindow()#(gif_labels)
        window.showFullScreen()
        sys.exit(app.exec_())
    except Exception as e:
        print(f"Error starting application: {e}")
        sys.exit(1)