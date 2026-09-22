from PySide2 import QtGui
from PySide2.QtWidgets import QApplication, QMainWindow, QStackedWidget , QWidget
from PySide2.QtWidgets import QFrame
from PySide2.QtWidgets import QLineEdit
from PySide2 import QtCore, QtWidgets
from PySide2.QtCore import QTimer, QSize, QDate , QObject , QThread , Signal, Qt, QCoreApplication
from PySide2.QtGui import QBrush, QColor, QPixmap
from messageBox import CustomMessageBox
from models import *
from models import SessionLocal 
from SaveModels import *
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
            table = self.ui.tableView_cncList
            index = table.currentIndex()

            # If any row is selected, don't open the Add page
            if index.isValid():
                # msg = CustomMessageBox(
                #     "Please deselect the selected row before adding a new CNC.",
                #     "warning",
                #     parent=self.ui
                # )
                # msg.exec_()
                return
            # Reset modify state
            self.selected_cnc_id = None
            self.is_modify_mode = False
    
            
            
            self.ui.lineEdit_cncName.clear()
            self.ui.lineEdit_cncIpAddress.clear()
            self.ui.lineEdit_cncPortNumber.clear()
            self.ui.comboBox_cncSelectionType.setCurrentIndex(0)
            self.ui.comboBox_cncController.setCurrentIndex(0)
            self.ui.comboBox_trialMode.setCurrentIndex(0)
            
            # Switch stacked page
            self.ui.stacked.setCurrentIndex(13)
            self.ui.tableView_cncList.clearSelection()
            self.ui.tableView_cncList.setCurrentIndex(QtCore.QModelIndex())
            self.last_selected_row = -1
            
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
            self.ui.comboBox_trialMode.setCurrentIndex(0)


            # Switch stacked page
            self.ui.stacked.setCurrentIndex(13)
            self.ui.tableView_cncList.clearSelection()
            self.ui.tableView_cncList.setCurrentIndex(QtCore.QModelIndex())
            self.last_selected_row = -1
        except Exception as e:
            print(f"Error in handle_UserModify_clicked: {e}")       
            
    def load_cnc_data_to_table(self):
        """
        Fetch all CNC records from database and populate table.
        """
        try:
            session = SessionLocal()

            cnc_list = session.query(CNCMaster).all()

            self.model = QStandardItemModel(len(cnc_list), 6)
            self.model.setHorizontalHeaderLabels([
                "ID",
                "CNC Name",
                "IP Address",
                "Port",
                "Selection Type",
                "Controller",
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

                cnc = session.query(CNCMaster).filter(CNCMaster.id == record_id).first()

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
            
                 
    def refresh_Cnctable(self):
        """
        Refresh CNC table.
        """
        try:
            self.load_cnc_data_to_table()
        except Exception as e:
            print(f"Error refreshing CNC table: {e}")
    

class AocHistoryDisplay(QObject):
    """
    Displays saved user data in a table widget
    Shows: Username, Password, AccessType
    """
    
    def __init__(self, main_window):
        try:
            super().__init__(parent=None)
            self.ui = main_window
            self.setup_table()
            # self.load_aoc_history_to_table()
            self.last_selected_row = -1
            self.selected_cnc_id = None
            self.is_modify_mode = False
            self.ui.button_history.clicked.connect(self.handle_history_clicked)
            # self.ui.tableView_AocDataHistory.clicked.connect(self.on_program_selected)
            self.ui.comboBox_progid.currentIndexChanged.connect(
                self.load_aoc_history_to_table
            )

            self.ui.comboBox_dim.currentIndexChanged.connect(
                self.load_aoc_history_to_table
            )
            self.ui.cnc_manager.update_aocTable.connect(
                self.load_aoc_history_to_table
            )
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
                "Machine",
                "Dimension",
                "Part Name",
                "Nominal",
                "Reading",
                "Correction",
                "Tool Value",
                "Tool No",
                "Job",
                "Date",
                "Time"
            ])
            self.ui.tableView_AocDataHistory.setModel(self.model)
            self.ui.tableView_AocDataHistory.verticalHeader().setStyleSheet(
                "QHeaderView::section { background-color: #2b2b2b; color: white; border: 1px solid #888888; }"
            )
            self.ui.tableView_AocDataHistory.setAlternatingRowColors(False)
            # Set column widths
            # Set vertical header width
            # self.ui.tableView_AocDataHistory.verticalHeader().setWidth(90)
            
            self.ui.tableView_AocDataHistory.setColumnWidth(0, 40)
            self.ui.tableView_AocDataHistory.setColumnWidth(1, 90)
            self.ui.tableView_AocDataHistory.setColumnWidth(2, 120)
            self.ui.tableView_AocDataHistory.setColumnWidth(3, 120)
            self.ui.tableView_AocDataHistory.setColumnWidth(4, 120)
            self.ui.tableView_AocDataHistory.setColumnWidth(5, 120)
            self.ui.tableView_AocDataHistory.setColumnWidth(6, 120)
            self.ui.tableView_AocDataHistory.setColumnWidth(7, 120)
            self.ui.tableView_AocDataHistory.setColumnWidth(8, 90)
            self.ui.tableView_AocDataHistory.setColumnWidth(9, 50)
            self.ui.tableView_AocDataHistory.setColumnWidth(10, 110)
            self.ui.tableView_AocDataHistory.setColumnWidth(11, 90)
            # self.ui.tableView_AocDataHistory.setColumnWidth(3, 230)
#             self.ui.tableView_AocDataHistory.setStyleSheet(u"QTableView::item { border: 2px solid #888888; }\n"
# "QHeaderView::section { border: 2px solid #888888; }")
#             self.ui.tableView_AocDataHistory.verticalScrollBar().setStyleSheet("""
# QScrollBar:vertical {
#     background: black;
#     border: 1px solid #888888;
#     width: 30px;
# }
# """)
            # Disable column resizing
            self.ui.tableView_AocDataHistory.horizontalHeader().setStretchLastSection(False)
            self.ui.tableView_AocDataHistory.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Fixed)
            # Set row height
            self.ui.tableView_AocDataHistory.verticalHeader().setDefaultSectionSize(40)
            self.ui.tableView_AocDataHistory.verticalHeader().setVisible(False)
            self.ui.tableView_AocDataHistory.setSelectionMode(
                QtWidgets.QAbstractItemView.NoSelection
            )
            # self.ui.tableView_AocDataHistory.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
            # self.ui.tableView_AocDataHistory.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
            self.ui.tableView_AocDataHistory.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
            self.ui.tableView_AocDataHistory.setFocusPolicy(QtCore.Qt.NoFocus)                           # ❌ no focus highlight

            # Set header font size and bold
            header_font = self.ui.tableView_AocDataHistory.horizontalHeader().font()
            header_font.setPointSize(13)
            header_font.setBold(True)
            self.ui.tableView_AocDataHistory.horizontalHeader().setFont(header_font)
            
            # Set header background color to grey and font color to white
            self.ui.tableView_AocDataHistory.horizontalHeader().setStyleSheet(
                "QHeaderView::section { background-color: #2b2b2b; color: white; border: 1px solid #888888; min-height:50px; }"
            )
            # Set font size
            font = self.ui.tableView_AocDataHistory.font()
            font.setPointSize(13)
            self.ui.tableView_AocDataHistory.setFont(font)
            
            # print("Table setup completed")
        except Exception as e:
            print(f"Error setting up table: {e}")
            
    def get_aoc_ids_by_program(self, program_id):
        """
        Return all AOCIds that belong to the given ProgramId.
        """
        if not hasattr(self.ui, "savedbObj") or self.ui.savedbObj is None:
            return []

        session = self.ui.savedbObj.get_session()

        try:
            ids = []

            rows = session.query(self.ui.savedbObj.AOCBasedIds).all()

            for row in rows:
                try:
                    prog = row.AOCUniqueSettings.split(",")[0].strip()

                    if prog == str(program_id):
                        ids.append(row.AOCId)

                except Exception:
                    pass

            return ids

        finally:
            session.close()
    def handle_history_clicked(self):
        try:
            self.ui.stacked.setCurrentIndex(31)
            self.load_aoc_history_to_table()
        except Exception as e:
            print(f"Error in handle_history_clicked -> {e}")

    def load_aoc_history_to_table(self):
        try:

            if self.ui.stacked.currentIndex() != 31:
                return

            if not hasattr(self.ui, "savedbObj") or self.ui.savedbObj is None:
                return

            session = self.ui.savedbObj.get_session()

            # ------------------- FILTER -------------------

            query = session.query(self.ui.savedbObj.AOCValues)

            program = self.ui.comboBox_progid.currentText().strip()
            dimension = self.ui.comboBox_dim.currentText().strip()

            # -------- Program filter --------

            if program.upper() != "ALL":

                aoc_ids = self.get_aoc_ids_by_program(program)

                if aoc_ids:
                    query = query.filter(
                        self.ui.savedbObj.AOCValues.AOCBasedId.in_(aoc_ids)
                    )
                else:
                    self.model.removeRows(0, self.model.rowCount())
                    session.close()
                    return

            # -------- Dimension filter --------

            if dimension.upper() != "ALL":

                query = query.filter(
                    self.ui.savedbObj.AOCValues.Dimension == dimension
                )

            aoc_records = (
                query.order_by(
                    self.ui.savedbObj.AOCValues.Id.asc()
                )
                .all()
            )

            self.model.removeRows(0, self.model.rowCount())

            font = QtGui.QFont()
            font.setPointSize(13)

            for record in aoc_records:

                correction = float(record.Correction or 0)
                date_str = record.Date.strftime("%Y-%m-%d") if record.Date else ""
                time_str = record.Date.strftime("%H:%M:%S") if record.Date else ""
                values = [
                    record.Id,
                    record.Machine,
                    record.Dimension,
                    record.PartName,
                    record.NominalValue,
                    record.Reading,
                    record.Correction,
                    record.ToolValue,
                    record.ToolNo,
                    record.JobCount,
                    date_str,
                    time_str
                ]

                items = []

                for col, value in enumerate(values):

                    # Nominal, Reading, Correction, Tool Value
                    if col in (4, 5, 6, 7):
                        text = f"{float(value):.3f}"
                    else:
                        text = str(value)

                    item = QStandardItem(text)
                    item.setEditable(False)
                    item.setTextAlignment(Qt.AlignCenter)
                    item.setFont(font)

                    items.append(item)

                # ---------------- COLOUR ----------------

                if abs(correction - 999.999) < 0.001:

                    items[6].setText("0.000")

                    bg = QColor(184, 184, 0)
                    fg = QColor("black")

                elif abs(correction - 999.998) < 0.001:

                    items[6].setText("0.000")

                    bg = QColor(166, 174, 164)
                    fg = QColor("black")

                elif abs(correction - 999.997) < 0.001:

                    items[6].setText("0.000")

                    bg = QColor(205, 139, 98)
                    fg = QColor("black")

                elif abs(correction) < 0.001:

                    bg = QColor(135, 206, 235)
                    fg = QColor("black")

                else:

                    bg = QColor("white")
                    fg = QColor("black")

                for item in items:
                    item.setData(QBrush(bg), Qt.BackgroundRole)
                    item.setData(QBrush(fg), Qt.ForegroundRole)

                self.model.appendRow(items)

            session.close()

        except Exception as e:
            print("load_aoc_history_to_table ->", e)

    def on_program_selected(self, index):
            try:
                row = index.row()
    
                if self.last_selected_row == row:
                    # Deselect
                    self.ui.tableView_AocDataHistory.clearSelection()
                    self.ui.tableView_AocDataHistory.setCurrentIndex(QtCore.QModelIndex())
                    self.last_selected_row = -1
                else:
                    self.last_selected_row = row
            except Exception as e:
                print(f"Error in on_program_selected -> {e}")