import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import Qt, QThread
from PySide2.QtWidgets import QApplication, QMainWindow, QStackedWidget , QWidget
from PySide2.QtCore import QTimer
from PySide2.QtGui import QPixmap, QPainter, QColor, QFont


# UI (Qt Designer)
from main_ui_18 import Ui_MainWindow
# from main_old import Ui_MainWindow
# from main_old import Ui_MainWindow
# Separated modules
from ui_handler import UIHandler
from controller import AppController
from data_handler import DataHandler
from database import DatabaseAgent
from value import Value
from utilities import Utilities
from active_ui_handler import *
from factory_config import FactoryConfig
from master_Setting_handler import SPIController
from Dial_indicator import DialIndicator, SPCManager
from User_manager import UserManager, UserTableDisplay

import resources_rc
class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        
        # -------------------------------------------------
        # SETUP UI
        # -------------------------------------------------
        self.setupUi(self)  # setup UI
        self.user_managementTable = UserTableDisplay(self)
        # self.user_manager = UserManager(self)  # Initialize UserManager with MainWindow reference
        self.utils = Utilities(self.label_time, self.label_date, self.lineEdit_formulaBar)

        # -------------------------------------------------
        # INIT UI HANDLER
        # -------------------------------------------------
        self.valueObj = Value()
        self.databaseObj = DatabaseAgent()
        
        
        self.ui_handler = UIHandler(main_window=self) 
        # self.indicator_manager = IndicatorManager()


        self.stacked: QStackedWidget = getattr(self, "stackedWidget_main", None)
        if self.stacked:
                # Connecting Slot When Page Changes
                self.stacked.currentChanged.connect(self.ui_handler.set_labels_to_header)
                self.stacked.setCurrentIndex(0)  # second page   
        
        
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
        # self.page_16 = self.stackedWidget_main.widget(15)
        # self.spc_ui = Ui_SPCPage()
        # self.spc_ui.setupUi(self.page_16)
        self.spc_manager = SPCManager(self)
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
        self.dial_indicator = DialIndicator(
            main_window = self
        )
       
     
        self.dial_indicator.app = self.controller
        self.dial_indicator.spc_manager = self.spc_manager
        self.dial_indicator.set_visibility()

        self.spi_controller = SPIController(
            main_window = self,
            data_handler = self.data_handler,
            app_controller = self.controller
        )        
        
        self.button_factoryConfig.clicked.connect(self.open_factory_config)
        
        self.counter = 0
            
    def open_factory_config(self):
        #if not hasattr(self, "factory_popup"):
        self.factory_popup = FactoryConfig(parent=self,
                            current_factory=self.spi_controller.current_factory)
        self.factory_popup.config_changed.connect(
            self.spi_controller.on_factory_changed
        )
        self.factory_popup.show()
        


if __name__ == "__main__":
    try:
        
        app = QApplication(sys.argv)

        window = MainWindow()#(gif_labels)
        window.showFullScreen()
        sys.exit(app.exec_())
    except Exception as e:
        print(f"Error starting application: {e}")
        sys.exit(1)