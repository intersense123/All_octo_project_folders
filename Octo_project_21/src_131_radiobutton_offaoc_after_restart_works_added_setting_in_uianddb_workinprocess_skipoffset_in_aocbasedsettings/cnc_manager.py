from PySide2.QtWidgets import QApplication, QMainWindow, QStackedWidget , QWidget
from PySide2.QtWidgets import QFrame
from PySide2.QtWidgets import QLineEdit
from PySide2 import QtCore, QtWidgets
from PySide2.QtCore import QTimer, QSize, QDate , QObject , QThread , Signal, Qt, QCoreApplication
from PySide2.QtGui import QPixmap
from messageBox import CustomMessageBox
from models import *
from models import SessionLocal , UserManagement
from sqlalchemy.orm import Session , sessionmaker
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from PySide2.QtGui import QStandardItemModel, QStandardItem


class CncListDisplay(QObject):
    """
    Displays saved user data in a table widget
    Shows: Username, Password, AccessType
    """
    
    def __init__(self, main_window):
        try:
            super().__init__(parent=None)
            self.ui = main_window
            self.setup_table()
            self.load_cnc_data_to_table()
            self.last_selected_row = -1
            self.selected_cnc_id = None
            self.is_modify_mode = False
            self.ui.tableView_cncList.clicked.connect(self.on_program_selected)
            self.ui.button_deleteCncSettings.clicked.connect(self.delete_record)
            self.ui.button_modifyCncSettings.clicked.connect(self.handle_cncModify_clicked)
            self.ui.button_addCncSettings.released.connect(self.handle_cncAdd_clicked)
        except Exception as e:
            print(f"Error initializing UserTableDisplay: {e}")
    
    def setup_table(self):
        """
        Configure table view with columns
        """
        try:            
            # Create and set model for table view
            self.model = QStandardItemModel()
            self.model.setHorizontalHeaderLabels([
                "ID",
                "CNC Name",
                "IP Address",
                "Port",
                "Selection Type",
                "Controller"
            ])
            self.ui.tableView_cncList.setModel(self.model)
            self.ui.tableView_cncList.verticalHeader().setStyleSheet(
                "QHeaderView::section { background-color: #2b2b2b; color: white; border: 1px solid #888888; }"
            )
            
            # Set column widths
            # Set vertical header width
            # self.ui.tableView_cncList.verticalHeader().setWidth(90)
            
            self.ui.tableView_cncList.setColumnWidth(0, 60)
            self.ui.tableView_cncList.setColumnWidth(1, 170)
            self.ui.tableView_cncList.setColumnWidth(2, 170)
            self.ui.tableView_cncList.setColumnWidth(3, 70)
            self.ui.tableView_cncList.setColumnWidth(4, 150)
            self.ui.tableView_cncList.setColumnWidth(5, 120)
            # self.ui.tableView_cncList.setColumnWidth(3, 230)
            self.ui.tableView_cncList.setStyleSheet(u"QTableView::item { border: 2px solid #888888; }\n"
"QHeaderView::section { border: 2px solid #888888; }")
            self.ui.tableView_cncList.verticalScrollBar().setStyleSheet("""
QScrollBar:vertical {
    background: black;
    border: 1px solid #888888;
    width: 40px;
}
""")
            # Disable column resizing
            self.ui.tableView_cncList.horizontalHeader().setStretchLastSection(False)
            self.ui.tableView_cncList.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Fixed)
            # Set row height
            self.ui.tableView_cncList.verticalHeader().setDefaultSectionSize(55)
            self.ui.tableView_cncList.verticalHeader().setVisible(False)
            self.ui.tableView_cncList.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
            self.ui.tableView_cncList.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
            self.ui.tableView_cncList.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
            self.ui.tableView_cncList.setFocusPolicy(QtCore.Qt.NoFocus)                           # ❌ no focus highlight

            # Set header font size and bold
            header_font = self.ui.tableView_cncList.horizontalHeader().font()
            header_font.setPointSize(13)
            header_font.setBold(True)
            self.ui.tableView_cncList.horizontalHeader().setFont(header_font)
            
            # Set header background color to grey and font color to white
            self.ui.tableView_cncList.horizontalHeader().setStyleSheet(
                "QHeaderView::section { background-color: #2b2b2b; color: white; border: 1px solid #888888; min-height:50px; }"
            )
            # Set font size
            font = self.ui.tableView_cncList.font()
            font.setPointSize(13)
            self.ui.tableView_cncList.setFont(font)
            
            # print("Table setup completed")
        except Exception as e:
            print(f"Error setting up table: {e}")
            
    def on_program_selected(self, index):
        try:
            row = index.row()

            if self.last_selected_row == row:
                # Deselect
                self.ui.tableView_cncList.clearSelection()
                self.ui.tableView_cncList.setCurrentIndex(QtCore.QModelIndex())
                self.last_selected_row = -1
            else:
                self.last_selected_row = row
        except Exception as e:
            print(f"Error in on_program_selected -> {e}")
    def handle_cncAdd_clicked(self):
        try:
            # Reset modify state
            self.selected_cnc_id = None
            self.is_modify_mode = False
    
            
            
            self.ui.lineEdit_cncName.clear()
            self.ui.lineEdit_cncIpAddress.clear()
            self.ui.lineEdit_cncPortNumber.clear()
            self.ui.comboBox_cncSelectionType.setCurrentIndex(0)
            self.ui.comboBox_cncController.setCurrentIndex(0)
            
            # Switch stacked page
            self.ui.stacked.setCurrentIndex(13)
            
            
        except Exception as e:
            print("Error in handle addUser_clicked:", e)
    def handle_cncModify_clicked(self):
        try:
            table = self.ui.tableView_cncList
            index = table.currentIndex()

            if not index.isValid():
                msg = CustomMessageBox(
                    "Please select a row first to modify",
                    "warning",
                    parent=self.ui
                )
                msg.exec_()
                return

            row = index.row()
            model = table.model()

            cnc_id = int(model.index(row, 0).data())
            CNCName = model.index(row, 1).data()
            IPAddress = model.index(row, 2).data()
            PortNumber = model.index(row, 3).data()
            CNCSelection = model.index(row, 4).data()
            ControllerName = model.index(row, 5).data()
                
            # Store for update
            self.selected_cnc_id = cnc_id
            self.is_modify_mode = True

            # Load into fields
            self.ui.lineEdit_cncName.setText(CNCName)
            self.ui.lineEdit_cncIpAddress.setText(IPAddress)
            self.ui.lineEdit_cncPortNumber.setText(PortNumber)
            self.ui.comboBox_cncSelectionType.setCurrentText(CNCSelection)
            self.ui.comboBox_cncController.setCurrentText(ControllerName)

            # Switch stacked page
            self.ui.stacked.setCurrentIndex(13)

        except Exception as e:
            print(f"Error in handle_UserModify_clicked: {e}")       
            
    def load_cnc_data_to_table(self):
        """
        Fetch all CNC records from database and populate table.
        """
        try:
            session = SessionLocal()

            cnc_list = session.query(CNCList).all()

            self.model = QStandardItemModel(len(cnc_list), 6)
            self.model.setHorizontalHeaderLabels([
                "ID",
                "CNC Name",
                "IP Address",
                "Port",
                "Selection Type",
                "Controller"
            ])
            self.ui.comboBox_machine.clear()
            for row, cnc in enumerate(cnc_list):
                self.model.setItem(row, 0, QStandardItem(str(cnc.id)))
                self.model.setItem(row, 1, QStandardItem(cnc.CNCName))
                self.model.setItem(row, 2, QStandardItem(cnc.IPAddress))
                self.model.setItem(row, 3, QStandardItem(str(cnc.PortNumber)))
                self.model.setItem(row, 4, QStandardItem(cnc.CNCSelection))
                self.model.setItem(row, 5, QStandardItem(cnc.ControllerName))

            for row, cnc in enumerate(cnc_list):

                items = [
                    QStandardItem(str(cnc.id)),
                    QStandardItem(cnc.CNCName),
                    QStandardItem(cnc.IPAddress),
                    QStandardItem(str(cnc.PortNumber)),
                    QStandardItem(cnc.CNCSelection),
                    QStandardItem(cnc.ControllerName)
                ]

                # Center align all items
                for col, item in enumerate(items):
                    item.setTextAlignment(Qt.AlignCenter)
                    self.model.setItem(row, col, item)
                # Add CNC name to combo box
                self.ui.comboBox_machine.addItem(cnc.CNCName)
            self.ui.tableView_cncList.setModel(self.model)

            session.close()

        except SQLAlchemyError as e:
            print(f"Database error loading CNC list: {e}")

        except Exception as e:
            print(f"Error loading CNC list: {e}")
            
    def delete_record(self):
        try:
            """
            Delete selected row from both database and table
            """
            row_index = self.ui.tableView_cncList.currentIndex().row()
            
            if row_index > -1:
                msg = CustomMessageBox(f"Do you really want to delete selected data ?", "info",
                        parent=self.ui)
                result = msg.exec_()

                if result == QtWidgets.QDialog.Accepted:
                    self.delrow(row_index)
            else:
                msg = CustomMessageBox(f"Please select at least one row", "warning",
                        parent=self.ui)
                msg.exec_()
        except Exception as e:
            print(f"Error in delete_record: {e}")
            
             
    def delrow(self, row_index):
        """
        Delete selected CNC record from database and table.
        """
        try:
            id_item = self.model.item(row_index, 0)

            if id_item:
                record_id = int(id_item.text())

                session = SessionLocal()

                cnc = session.query(CNCList).filter(CNCList.id == record_id).first()

                if cnc:
                    session.delete(cnc)
                    session.commit()

                session.close()

                self.model.removeRow(row_index)

                msg = CustomMessageBox(
                    "CNC record deleted successfully",
                    "success",
                    parent=self.ui
                )
                msg.exec_()

                self.ui.status_manager.show(
                    page_index=1,
                    message="CNC record deleted successfully.",
                    timeout=6000,
                    msg_type="success"
                )

            else:
                print("Could not retrieve selected record ID.")

        except SQLAlchemyError as e:
            print(f"Database error deleting CNC record: {e}")

            msg = CustomMessageBox(
                "Error deleting CNC record from database",
                "error",
                parent=self.ui
            )
            msg.exec_()

        except Exception as e:
            print(f"Error deleting CNC record: {e}")

            msg = CustomMessageBox(
                "Error deleting CNC record",
                "error",
                parent=self.ui
            )
            msg.exec_()
            
                 
    def refresh_table(self):
        """
        Refresh CNC table.
        """
        try:
            self.load_cnc_data_to_table()
        except Exception as e:
            print(f"Error refreshing CNC table: {e}")
    

            
    
