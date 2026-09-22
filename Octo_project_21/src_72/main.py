import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import Qt, QThread
from PySide2.QtWidgets import QApplication, QMainWindow, QStackedWidget , QWidget
from PySide2.QtCore import QTimer
from PySide2.QtGui import QPixmap, QPainter, QColor, QFont
# UI (Qt Designer)
from main_ui_18 import Ui_MainWindow
# from main_old import Ui_MainWindow
# from ui import Ui_MainWindow
# Separated modules
from ui_handler import UIHandler
from controller import AppController
from data_handler import DataHandler
from database import DatabaseAgent
from value import Value
from utilities import Utilities
from active_ui_togglebutton_handler import *
from factory_config import FactoryConfig
from master_Setting_handler import SPIController
from Dial_indicator import DialIndicator
from User_manager import UserManager, UserTableDisplay
from SaveModels import SaveDatabaseManager
from IO_Settings_Handler import RelayController
from gpio_input_handler import GpioInputHandler
import resources_rc
from serial_handler import SerialHandler
from help import AboutPageHandler

class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        
        # -------------------------------------------------
        # SETUP UI
        # -------------------------------------------------
        self.setupUi(self)  # setup UI
        '''
        temporary UserManager is commented for testing becuse of every time login need to fieeld so for avoiding login 
        crentials so I commented for sell need to uncomment it
        '''
        self.toggle_on_pix = QPixmap("/home/torizon/app/src/images/toggle_on.png")
        self.toggle_off_pix = QPixmap(":/images/Switcher_OFF.png")
        # #self.user_manager = UserManager(self)  # Initialize UserManager with MainWindow reference
        #  #self.user_managementTable = UserTableDisplay(self)
        self.utils = Utilities(main_window=self)                                                                                                                                                                                                                                                                                                                                                    
        self.aboutPageHandler = AboutPageHandler(self)
        # -------------------------------------------------
        # INIT UI HANDLER
        # -------------------------------------------------
        self.valueObj = Value()
        # self.valueObj.init_activeVariables_dictionary()
        self.savedbObj = SaveDatabaseManager()
        self.savedbObj.connect()
        self.savedbObj.create_tables()
        self.databaseObj = DatabaseAgent()
        self.relayController = RelayController()
        
        self.ui_handler = UIHandler(main_window=self) 
        
        # self.indicator_manager = IndicatorManager()


        self.stacked: QStackedWidget = getattr(self, "stackedWidget_main", None)
        if self.stacked:
                # Connecting Slot When Page Changes
                self.stacked.currentChanged.connect(self.ui_handler.set_labels_to_header)
                if self.stacked.currentIndex() != 0:
                    self.stacked.setCurrentIndex(0) 
        
        self.ui_handler.linkage_of_ui()
        self.valueObj.init_AngleCalculationSettings_dictionary()
        self.valueObj.init_mainProgramSettings_dictionary()
             
        
        self.utils.start_clock_updates()
        

        # ActiveProgramId Loaded Before
        # Load from DB first
        self.valueObj.AngleCalculationSettings_dict = self.databaseObj.load_data_to_AngleCalculationSettings_dict(self.valueObj.activeVariables_dict.get("ActiveProgramId", 1))
        
        # Load Active Program Id
        self.comboBox_programIdSetting_outer.setCurrentText(str(self.valueObj.activeVariables_dict["ActiveProgramId"]))
        
        # Set Inner Program Id To The Active Id
        self.comboBox_programIdSetting_Inner.setCurrentText(str(self.valueObj.activeVariables_dict["ActiveProgramId"]))
        # self.spc_manager = SPCManager(self)
        # -------------------------------------------------
        # INIT DATA HANDLER
        # -------------------------------------------------
        self.data_handler = DataHandler(main_window=self,
                                        uiHandler = self.ui_handler)
        # self.spc_manager = SPCManager(self)
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
        # self.dial_indicator.spc_manager = self.spc_manager
        self.dial_indicator.set_visibility()

        self.spi_controller = SPIController(
            main_window = self,
            data_handler = self.data_handler,
            app_controller = self.controller
        )        
        self.button_factoryConfig.clicked.connect(self.open_factory_config)
        channels=self.controller.get_channels_for_program(
                int(self.valueObj.activeVariables_dict["ActiveProgramId"])
            )
        # self.spc_manager.load_data(channels)
        # self.spc_manager.load_program_OnSpc( int(self.valueObj.activeVariables_dict["ActiveProgramId"])) 
        self.counter = 0
        self.generate_Rs232()
        self.Gpio_handling()
    
    def generate_Rs232(self):
        try:
            # This block of code is responsible for loading RS232 settings from a database and
            # initializing a `SerialHandler` object with exception handling. Here's a breakdown of what it
            # does:
            # Load RS232 settings from database and initialize SerialHandler with exception handling
            rs232_settings = self.databaseObj.load_data_to_RS232Settings_dict()
            if rs232_settings.get('RS232_ON_OFF', 'OFF') == 'ON':
                port = rs232_settings['PORT_NAME']
                baud_rate = int(rs232_settings['BAUD_RATE'])
                parity_map = {'None': 'N', 'Even': 'E', 'Odd': 'O'}
                parity = parity_map.get(rs232_settings.get('PARITY', 'None'), 'N')
                stopbits_map = {'One': 1, '1.5': 1.5, 'Two': 2}
                stopbits = stopbits_map.get(rs232_settings.get('STOP_BITS', 'One'), 1)
                data_bits = int(rs232_settings['DATA_BITS'])
                self.serial_instance = SerialHandler(port, baud_rate, parity, stopbits, data_bits)
                # print(f"SerialHandler initialized: {port} @ {baud_rate}")
            else:
                self.serial_instance = None
                print("RS232 disabled (RS232_ON_OFF=OFF)")
        except (KeyError, ValueError, RuntimeError) as e:
            self.serial_instance = None
            print(f"Failed to initialize SerialHandler: {e}")
        except Exception as e:
            self.serial_instance = None
            print(f"Unexpected error initializing SerialHandler: {e}")
    
    def Gpio_handling(self):
        # GPIO Input Handler initialization
        try:
            self.gpio_handler = GpioInputHandler(self,chip_name="gpiochip3", input_line=16)  # Adjust line as needed
            self.gpio_handler.status_changed.connect(lambda msg: print(f"GPIO: {msg}"))
            # self.gpio_handler.high_detected.connect(self.data_handler.save_current_values)  # Connect to specific task
            self.gpio_handler.start()
            # print("GPIO Input Handler started")
        except Exception as e:
            self.gpio_handler = None
            print(f"Failed to initialize GPIO Handler: {e}")
            
    def open_factory_config(self):
        #if not hasattr(self, "factory_popup"):
        self.factory_popup = FactoryConfig(parent=self,
                            current_factory=self.spi_controller.current_factory)
        self.factory_popup.config_changed.connect(
            self.spi_controller.on_factory_changed
        )
        self.factory_popup.show()
        
    def closeEvent(self, event):
        if hasattr(self, 'gpio_handler') and self.gpio_handler:
            self.gpio_handler.stop()
        if self.savedbObj:
            self.savedbObj.disconnect()
        # if self.spc_manager:
        #     self.spc_manager.worker.stop()
        #     self.spc_manager.worker.wait()

        event.accept()

if __name__ == "__main__":
    try:
        
        app = QApplication(sys.argv)

        window = MainWindow()#(gif_labels)
        window.showFullScreen()
        sys.exit(app.exec_())
    except Exception as e:
        print(f"Error starting application: {e}")
        sys.exit(1)