from PySide2.QtWidgets import QApplication, QMainWindow, QStackedWidget , QWidget
from PySide2.QtWidgets import QFrame
from PySide2.QtWidgets import QLineEdit
from PySide2 import QtCore, QtWidgets
from PySide2.QtCore import QTimer, QSize, QDate , QObject , QThread , Signal, Qt, QCoreApplication
from PySide2.QtGui import QPixmap
from messageBox import CustomMessageBox
from models import *
from models import SessionLocal , CNCMaster
from sqlalchemy.orm import Session , sessionmaker
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from PySide2.QtGui import QStandardItemModel, QStandardItem


class UserManager(QObject):
    """
    Handles:
    - UI visibility
    - Styling
    - Navigation
    - Keyboards
    - Power / menu actions
    """

    def __init__(self, main_window):
        try:
            super().__init__(parent=None) 
            self.ui = main_window   # 🔑 MainWindow reference
            self.ui.button_login.clicked.connect(self.validate_user)
           
        except Exception as e:
            print(f"Error initializing UserManager: {e}")
    

    def validate_user(self):
        """
        Validates username and password from UI login fields
        Returns: user object if valid, None otherwise
        """
        try:
           
            username = self.ui.lineEdit_usernameLogin.text().strip()
            password = self.ui.lineEdit_passwordLogin.text().strip()
            
            if not username or not password:
                msg = CustomMessageBox("Username and password cannot be empty", "error",
                     parent=self.ui)
                msg.exec_()
                return None
            
            session = SessionLocal()
            
            # Check if database is empty and initialize defaults
            user_count = session.query(UserManagement).count()
            if user_count == 0 :
                # print("Database is empty. Inserting default users...")
                UserManagement.insert_defaults(session)
                # Auto-login as admin
                username = "admin"
                password = "admin"
            
            user = (
                session.query(UserManagement)
                .filter(
                    UserManagement.Username == username,
                    UserManagement.Password == password
                )
                .first()
            )
            session.close()
            
            if user:
                self.check_access_level(user)  # Check access level and set UI accordingly
                return user

            else:
                msg = CustomMessageBox("Invalid username or password", "error",
                     parent=self.ui)
                msg.exec_()
                return None
        except SQLAlchemyError as e:
            # print(f"Database error during user validation: {e}")
            msg = CustomMessageBox("Invalid username or password, Please Try Again!", "error",
                     parent=self.ui)
            msg.exec_()
            # CustomMessageBox.show_error("Database Error", "Error validating user credentials")
            return None
        except Exception as e:
            print(f"Unexpected error during user validation: {e}")
            # CustomMessageBox.show_error("Error", "An unexpected error occurred")
            return None
    
    def check_access_level(self, user):
        """
        Checks access level and applies appropriate UI visibility based on access type
        AccessType: 'admin' or 'guest'
        """
        try:
            if user is None:
                return False
            
            self.ui.label_ioSettingPage.setEnabled(True)
            self.ui.label_autoOffsetSettingPage.setEnabled(True)
            self.ui.label_clockSettingsPage.setEnabled(True)
            self.ui.label_userManagementPage.setEnabled(True)
            self.ui.button_partSettings.setEnabled(True)
            self.ui.button_partSettings.setStyleSheet("color: white;")
            
            access_type = user.AccessType.lower()
            
            if access_type == "admin":
                self.set_admin_access(user)
                return True
            elif access_type == "guest":
                self.set_guest_access(user)
                return True
            else:
                msg = CustomMessageBox(f"Invalid Username and Password, Try Again!", "error",
                     parent=self.ui)
                msg.exec_()
                # CustomMessageBox.show_error("Access Error", "Unknown access type")
                return False
        except Exception as e:
            print(f"Error checking access level: {e}")
            # CustomMessageBox.show_error("Error", "Failed to check access level")
            return False
    
    def set_admin_access(self,user):
        """
        Configure UI for admin access level
        """
        try:
            self.ui.label_ioSettingPage.setEnabled(True)
            ############################tmp############
            self.ui.label_autoOffsetSettingPage.setDisabled(True) #setEnabled(True)
            ###########################################################
            self.ui.label_clockSettingsPage.setEnabled(True)
            self.ui.label_userManagementPage.setEnabled(True)
            self.ui.button_partSettings.setEnabled(True)
            self.ui.button_ProgIdDelete.setEnabled(True)
            # print("Admin access granted - showing all features")
            msg = CustomMessageBox(f"Welcome {user.Username} ", "success",
                     parent=self.ui)
            # msg.accepted.connect(self.update_ui_after_programSettings_saved)
            self.ui.stacked.setCurrentIndex(23)
            msg.exec_()
            
            # self.ui.button_login.clicked.connect(lambda : self.ui.stacked.setCurrentIndex(23))
        except Exception as e:
            print(f"Error setting admin access: {e}")
    
    def set_guest_access(self,user):
        """
        Configure UI for guest access level
        """
        try:
            self.ui.label_ioSettingPage.setDisabled(True)
            self.ui.label_autoOffsetSettingPage.setDisabled(True)
            self.ui.label_clockSettingsPage.setDisabled(True)
            self.ui.label_userManagementPage.setDisabled(True)
            self.ui.button_partSettings.setDisabled(True)
            self.ui.button_ProgIdDelete.setDisabled(True)
            self.ui.button_partSettings.setStyleSheet("color: #666666;")
            msg = CustomMessageBox(f"Welcome {user.Username} ", "success",
                     parent=self.ui)
            self.ui.stacked.setCurrentIndex(23)
            msg.exec_()
            # print("Guest access granted - showing limited features")
        except Exception as e:
            print(f"Error setting guest access: {e}")


class UserTableDisplay(QObject):
    """
    Displays saved user data in a table widget
    Shows: Username, Password, AccessType
    """
    
    def __init__(self, main_window):
        try:
            super().__init__(parent=None)
            self.ui = main_window
            self.selected_user_id = None
            self.protected_admin_user_id = None
            self.is_modify_mode = False
            self.setup_table()
            self.load_users_to_table()
            self.last_selected_row = -1
            self.ui.tableview_loginList.clicked.connect(self.on_program_selected)
            self.ui.button_deleteLogin.clicked.connect(self.delete_record)
            self.ui.button_addLoginDetails.clicked.connect(self.handle_addUser_clicked)
            self.ui.button_modifyLogin.clicked.connect(self.handle_UserModify_clicked)
            
        except Exception as e:
            print(f"Error initializing UserTableDisplay: {e}")
    
    def setup_table(self):
        """
        Configure table view with columns
        """
        try:            
            # Create and set model for table view
            self.model = QStandardItemModel()
            self.model.setHorizontalHeaderLabels(["ID", "Username", "Access Type"])
            self.ui.tableview_loginList.setModel(self.model)
            self.ui.tableview_loginList.verticalHeader().setStyleSheet(
                "QHeaderView::section { background-color: #2b2b2b; color: white; border: 1px solid #888888; }"
            )
            
            # Set column widths
            # Set vertical header width
            # self.ui.tableview_loginList.verticalHeader().setWidth(90)
            self.ui.tableview_loginList.setColumnWidth(0, 100)
            self.ui.tableview_loginList.setColumnWidth(1, 310)
            self.ui.tableview_loginList.setColumnWidth(2, 310)
            # self.ui.tableview_loginList.setColumnWidth(3, 230)
            self.ui.tableview_loginList.setStyleSheet(u"QTableView::item { border: 2px solid #888888; }\n"
"QHeaderView::section { border: 2px solid #888888; }")
            self.ui.tableview_loginList.verticalScrollBar().setStyleSheet("""
QScrollBar:vertical {
    background: black;
    border: 1px solid #888888;
    width: 40px;
}
""")
            # Disable column resizing
            self.ui.tableview_loginList.horizontalHeader().setStretchLastSection(False)
            self.ui.tableview_loginList.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Fixed)
            # Set row height
            self.ui.tableview_loginList.verticalHeader().setDefaultSectionSize(55)
            self.ui.tableview_loginList.verticalHeader().setVisible(False)
            self.ui.tableview_loginList.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
            self.ui.tableview_loginList.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
            self.ui.tableview_loginList.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
            self.ui.tableview_loginList.setFocusPolicy(QtCore.Qt.NoFocus)                           # ❌ no focus highlight

            # Set header font size and bold
            header_font = self.ui.tableview_loginList.horizontalHeader().font()
            header_font.setPointSize(13)
            header_font.setBold(True)
            self.ui.tableview_loginList.horizontalHeader().setFont(header_font)
            
            # Set header background color to grey and font color to white
            self.ui.tableview_loginList.horizontalHeader().setStyleSheet(
                "QHeaderView::section { background-color: #2b2b2b; color: white; border: 1px solid #888888; min-height:50px; }"
            )
            # Set font size
            font = self.ui.tableview_loginList.font()
            font.setPointSize(13)
            self.ui.tableview_loginList.setFont(font)
            
            # print("Table setup completed")
        except Exception as e:
            print(f"Error setting up table: {e}")
    def handle_UserModify_clicked(self):
        session = None

        try:
            table = self.ui.tableview_loginList
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

            # Get selected user ID from table
            user_id = int(model.index(row, 0).data())

            # Get complete user details from database
            session = SessionLocal()

            user = (
                session.query(UserManagement)
                .filter(UserManagement.id == user_id)
                .first()
            )

            if not user:
                msg = CustomMessageBox(
                    "User not found",
                    "error",
                    parent=self.ui
                )
                msg.exec_()
                return

            # Store modify information
            self.selected_user_id = user.id
            self.is_modify_mode = True

            # Load correct database values into fields
            self.ui.lineEdit_setUsernameLogin.setText(user.Username)
            self.ui.lineEdit_setPasswordLogin.setText(user.Password)
            self.ui.comboBox_setAccessCombo.setCurrentText(user.AccessType)

            protected_admin = self.is_protected_admin_row(row, user)
            self.protected_admin_user_id = user.id if protected_admin else None
            self.ui.lineEdit_setUsernameLogin.setEnabled(not protected_admin)
            self.ui.comboBox_setAccessCombo.setEnabled(not protected_admin)
            self.ui.lineEdit_setPasswordLogin.setEnabled(True)

            # Open modify page
            self.ui.stacked.setCurrentIndex(2)

            # Clear table selection
            self.ui.tableview_loginList.clearSelection()
            self.ui.tableview_loginList.setCurrentIndex(QtCore.QModelIndex())
            self.last_selected_row = -1

        except Exception as e:
            print(f"Error in handle_UserModify_clicked: {e}")

        finally:
            if session:
                session.close()

    def handle_addUser_clicked(self):
        try:
            table = self.ui.tableview_loginList
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
            self.selected_user_id = None
            self.protected_admin_user_id = None
            self.is_modify_mode = False

            # Clear fields ONLY here
            self.ui.lineEdit_setUsernameLogin.clear()
            self.ui.lineEdit_setPasswordLogin.clear()
            self.ui.comboBox_setAccessCombo.setCurrentIndex(0)
            self.ui.lineEdit_setUsernameLogin.setEnabled(True)
            self.ui.comboBox_setAccessCombo.setEnabled(True)
            self.ui.lineEdit_setPasswordLogin.setEnabled(True)

            # Switch page
            self.ui.stacked.setCurrentIndex(2)
            self.ui.tableview_loginList.clearSelection()
            self.ui.tableview_loginList.setCurrentIndex(QtCore.QModelIndex())
            self.last_selected_row = -1
        except Exception as e:
            print("Error in handle addUser_clicked:", e)        

    @staticmethod
    def is_protected_admin_row(row_index, user):
        return (
            row_index == 0
            and user.Username.strip().lower() == "admin"
            and user.AccessType.strip().lower() == "admin"
        )
    def on_program_selected(self, index):
        try:
            row = index.row()

            if self.last_selected_row == row:
                # Deselect
                self.ui.tableview_loginList.clearSelection()
                self.ui.tableview_loginList.setCurrentIndex(QtCore.QModelIndex())
                self.last_selected_row = -1
            else:
                self.last_selected_row = row
        except Exception as e:
            print(f"Error in on_program_selected -> {e}")
            
    def load_users_to_table(self):
        """
        Fetch all users from database and populate table view
        """
        try:
            
            session = SessionLocal()
            users = session.query(UserManagement).all()
            
            self.model = QStandardItemModel(len(users), 3)
            self.model.setHorizontalHeaderLabels(["ID", "Username", "Access Type"])
            
            for row, user in enumerate(users):
                # ID column
                user_id_item = QStandardItem(str(user.id))
                self.model.setItem(row, 0, user_id_item)
                
                # Username column
                username_item = QStandardItem(user.Username)
                self.model.setItem(row, 1, username_item)
                
                # Password column
                # password_item = QStandardItem(user.Password)
                # self.model.setItem(row, 2, password_item)
                
                # AccessType column
                access_item = QStandardItem(user.AccessType)
                self.model.setItem(row, 2, access_item)
            
            self.ui.tableview_loginList.setModel(self.model)
            session.close()
            # print(f"Loaded {len(users)} users to table")
        except SQLAlchemyError as e:
            print(f"Database error loading users: {e}")
        except Exception as e:
            print(f"Error loading users to table: {e}")
            
    def delete_record(self):
        try:
            """
            Delete selected row from both database and table
            """
            row_index = self.ui.tableview_loginList.currentIndex().row()
            
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
        Delete selected user from database and table.
        Admin user cannot be deleted.
        """
        session = None

        try:
            # Get user ID from first column
            user_id_item = self.model.item(row_index, 0)

            if not user_id_item:
                print("Error: Could not retrieve user ID")
                return

            user_id = int(user_id_item.text())

            # Open database session
            session = SessionLocal()

            # Find selected user
            user = (
                session.query(UserManagement)
                .filter(UserManagement.id == user_id)
                .first()
            )

            if not user:
                msg = CustomMessageBox(
                    "User not found.",
                    "error",
                    parent=self.ui
                )
                msg.exec_()
                return

            # ==========================================================
            # PROTECT ADMIN USER
            # ==========================================================
            if self.is_protected_admin_row(row_index, user):
                msg = CustomMessageBox(
                    "The first admin user cannot be deleted.",
                    "warning",
                    parent=self.ui
                )
                msg.exec_()
                return

            # ==========================================================
            # DELETE USER
            # ==========================================================
            session.delete(user)
            session.commit()

            # Remove row from table
            self.model.removeRow(row_index)

            msg = CustomMessageBox(
                "User deleted successfully",
                "success",
                parent=self.ui
            )
            msg.exec_()

            self.ui.status_manager.show(
                page_index=1,
                message="User deleted successfully.",
                timeout=6000,
                msg_type="success"
            )

        except SQLAlchemyError as e:
            if session:
                session.rollback()

            print(f"Database error deleting user: {e}")

            msg = CustomMessageBox(
                "Error deleting user from database",
                "error",
                parent=self.ui
            )
            msg.exec_()

            self.ui.status_manager.show(
                page_index=1,
                message="Failed to delete user.",
                timeout=6000,
                msg_type="error"
            )

        except Exception as e:
            if session:
                session.rollback()

            print(f"Error deleting row: {e}")

            msg = CustomMessageBox(
                "Error deleting row",
                "error",
                parent=self.ui
            )
            msg.exec_()

        finally:
            if session:
                session.close()
        
    def refresh_table(self):
        """
        Refresh table with latest user data
        """
        try:
            # self.ui.tableview_loginList.setRowCount(0)
            self.load_users_to_table()
            # print("Table refreshed")
        except Exception as e:
            print(f"Error refreshing table: {e}")
    

            
    
