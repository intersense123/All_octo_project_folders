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



class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()

        # -------------------------------------------------
        # SETUP UI
        # -------------------------------------------------
        #self.ui = Ui_MainWindow()
        self.setupUi(self)
        self.valueObj = Value()
        self.databaseObj = DatabaseAgent()
        self.utils = Utilities(self.label_time, self.label_date, self.lineEdit_formulaBar)
        # 🔑 IMPORTANT: expose widgets directly on MainWindow
        # keeps backward compatibility with old code
        # self.__dict__.update(self.ui.__dict__)
        # -------------------------------------------------
        # INIT UI HANDLER
        # -------------------------------------------------
        self.ui_handler = UIHandler(main_window=self)
        
        self.ui_handler.setup_lineedit_keyboards()
        self.ui_handler.linkage_formula_bar()
        self.ui_handler.powerButton
        self.stacked: QStackedWidget = getattr(self, "stackedWidget_main", None)
        if self.stacked:
                # Connecting Slot When Page Changes
                self.stacked.currentChanged.connect(self.ui_handler.set_labels_to_header)
                self.stacked.setCurrentIndex(0)  # second page
                
        self.ui_handler.linkage_of_ui()
        self.ui_handler.lineedit_opacity()
        self.comboBox_toselectProbe.clear()

        
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

        
        # -------------------------------------------------
        # THREAD / WORKER (if used)
        # -------------------------------------------------
        self.worker_thread = QThread(self)
        # If you already have Worker class:
        # self.worker = Worker()
        # self.worker.moveToThread(self.worker_thread)
        # self.worker_thread.started.connect(self.worker.run)
        # self.worker.spi_generated.connect(self.controller.spi_handler)
        # self.worker_thread.start()
        self.stackedWidget_2.setCurrentIndex(0)

        # -------------------------------------------------
        # CONNECT SIGNALS
        # -------------------------------------------------
        self._connect_signals()

        # -------------------------------------------------
        # INITIAL LOAD
        # -------------------------------------------------
        self._initial_load()

    # -------------------------------------------------
    # SIGNAL CONNECTIONS
    # -------------------------------------------------
    def _connect_signals(self):
        # Program / Dimension
        self.comboBox_programIdSettings.currentTextChanged.connect(
            self.controller.progId_changed_outer
        )

        self.comboBox_dimension.currentTextChanged.connect(
            self.controller.progId_changed_inner
        )

        # Save
        self.button_save.clicked.connect(
            self.controller.linkage_of_saveButton
        )

        # Master
        self.button_setMaster.clicked.connect(
            self.controller.set_master
        )

        # Probe based UI state
        self.comboBox_ovalityOnOff.currentTextChanged.connect(
            self.ui_handler.apply_ProbeBasedSettings_state
        )

        # Master type UI state
        self.comboBox_masterType.currentTextChanged.connect(
            self.ui_handler.apply_masterType_state
        )
        self.lineEdit_formulaBar.textChanged.connect(self.utils.validate_formulabar)

        # Power / Menu
        # self.button_shutdown.clicked.connect()

    # -------------------------------------------------
    # INITIAL LOAD SEQUENCE
    # -------------------------------------------------
    def _initial_load(self):
        # Load DB data
        self.data_handler.load_databases()

        # Init program + dimension
        self.controller.init_progId_and_dimension()

        # Apply UI defaults
        self.data_handler.Hide_rows()
        self.ui_handler.apply_ProbeBasedSettings_state()
        self.ui_handler.apply_masterType_state()
        self.ui_handler.apply_line_styles()
        self.ui_handler.setup_lineedit_keyboards()
        self.ui_handler.set_labels_to_header()

    # -------------------------------------------------
    # EVENT FILTER (delegate to UI handler)
    # -------------------------------------------------
    def eventFilter(self, obj, event):
        return self.ui_handler.eventFilter(obj, event)

    # -------------------------------------------------
    # CLEAN EXIT
    # -------------------------------------------------
    def closeEvent(self, event):
        try:
            if hasattr(self, "worker_thread"):
                self.worker_thread.quit()
                self.worker_thread.wait()
        except Exception as e:
            print("Close error:", e)

        event.accept()

    def __del__(self):
        pass



if __name__ == "__main__":
    try:
        
        app = QApplication(sys.argv)

        window = MainWindow()#(gif_labels)
        window.showFullScreen()
        sys.exit(app.exec_())
    except Exception as e:
        print(f"Error starting application: {e}")
        sys.exit(1)