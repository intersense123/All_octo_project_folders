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
            self.user_managementTable = UserTableDisplay(self.ui)  # Initialize UserTableDisplay with MainWindow reference
            self.ui.button_login.clicked.connect(self.validate_user)

        except Exception as e:
            print(f"Error initializing UserManager: {e}")
    
    # def on_login_clicked(self):
    #     """
    #     Handle login button click - validate user then navigate to page 23 if successful
    #     """
    #     if self.validate_user():
    #         self.ui.stacked.setCurrentIndex(23)
    
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
            if user_count == 0:
                print("Database is empty. Inserting default users...")
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
            print(f"Database error during user validation: {e}")
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
            
            access_type = user.AccessType.lower()
            
            if access_type == "admin":
                self.set_admin_access()
                return True
            elif access_type == "guest":
                self.set_guest_access()
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
    
    def set_admin_access(self):
        """
        Configure UI for admin access level
        """
        try:
            self.ui.label_ioSettingPage.setVisible(True)
            self.ui.label_autoOffsetSettingPage.setVisible(True)
            self.ui.label_clockSettingsPage.setVisible(True)
            self.ui.label_userManagementPage.setVisible(True)
            self.ui.button_partSettings.setVisible(True)
            print("Admin access granted - showing all features")
            msg = CustomMessageBox(f"Welcome Admin ", "success",
                     parent=self.ui)
            # msg.accepted.connect(self.update_ui_after_programSettings_saved)
            self.ui.stacked.setCurrentIndex(23)
            msg.exec_()
            
            # self.ui.button_login.clicked.connect(lambda : self.ui.stacked.setCurrentIndex(23))
        except Exception as e:
            print(f"Error setting admin access: {e}")
    
    def set_guest_access(self):
        """
        Configure UI for guest access level
        """
        try:
            self.ui.label_ioSettingPage.setDisabled(True)
            self.ui.label_autoOffsetSettingPage.setDisabled(True)
            self.ui.label_clockSettingsPage.setDisabled(True)
            self.ui.label_userManagementPage.setDisabled(True)
            self.ui.button_partSettings.setDisabled(True)
            msg = CustomMessageBox(f"Welcome Guest ", "success",
                     parent=self.ui)
            self.ui.stacked.setCurrentIndex(23)
            msg.exec_()
            print("Guest access granted - showing limited features")
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
            self.setup_table()
            self.load_users_to_table()
            self.ui.button_deleteLogin.clicked.connect(self.delete_record)
        except Exception as e:
            print(f"Error initializing UserTableDisplay: {e}")
    
    def setup_table(self):
        """
        Configure table view with columns
        """
        try:            
            # Create and set model for table view
            self.model = QStandardItemModel()
            self.model.setHorizontalHeaderLabels(["ID", "Username", "Password", "Access Type"])
            self.ui.tableview_loginList.setModel(self.model)
            self.ui.tableview_loginList.verticalHeader().setStyleSheet(
                "QHeaderView::section { background-color: #2b2b2b; color: white; border: 1px solid #888888; }"
            )
            
            # Set column widths
            # Set vertical header width
            # self.ui.tableview_loginList.verticalHeader().setWidth(90)
            self.ui.tableview_loginList.setColumnWidth(0, 90)
            self.ui.tableview_loginList.setColumnWidth(1, 220)
            self.ui.tableview_loginList.setColumnWidth(2, 220)
            self.ui.tableview_loginList.setColumnWidth(3, 230)
            self.ui.tableview_loginList.setStyleSheet(u"QTableView::item { border: 1px solid #888888; }\n"
"QHeaderView::section { border: 1px solid #888888; }")
            
            # Disable column resizing
            self.ui.tableview_loginList.horizontalHeader().setStretchLastSection(False)
            self.ui.tableview_loginList.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Fixed)
            # Set row height
            self.ui.tableview_loginList.verticalHeader().setDefaultSectionSize(50)
            self.ui.tableview_loginList.verticalHeader().setVisible(False)
            self.ui.tableview_loginList.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
            
            # Set header font size and bold
            header_font = self.ui.tableview_loginList.horizontalHeader().font()
            header_font.setPointSize(13)
            header_font.setBold(True)
            self.ui.tableview_loginList.horizontalHeader().setFont(header_font)
            
            # Set header background color to grey and font color to white
            self.ui.tableview_loginList.horizontalHeader().setStyleSheet(
                "QHeaderView::section { background-color: #2b2b2b; color: white; border: 1px solid #888888; min-height:40px; }"
            )
            
            # Set font size
            font = self.ui.tableview_loginList.font()
            font.setPointSize(13)
            self.ui.tableview_loginList.setFont(font)
            
            print("Table setup completed")
        except Exception as e:
            print(f"Error setting up table: {e}")
    
    def load_users_to_table(self):
        """
        Fetch all users from database and populate table view
        """
        try:
            
            session = SessionLocal()
            users = session.query(UserManagement).all()
            
            self.model = QStandardItemModel(len(users), 4)
            self.model.setHorizontalHeaderLabels(["ID", "Username", "Password", "Access Type"])
            
            for row, user in enumerate(users):
                # ID column
                user_id_item = QStandardItem(str(user.id))
                self.model.setItem(row, 0, user_id_item)
                
                # Username column
                username_item = QStandardItem(user.Username)
                self.model.setItem(row, 1, username_item)
                
                # Password column
                password_item = QStandardItem(user.Password)
                self.model.setItem(row, 2, password_item)
                
                # AccessType column
                access_item = QStandardItem(user.AccessType)
                self.model.setItem(row, 3, access_item)
            
            self.ui.tableview_loginList.setModel(self.model)
            session.close()
            print(f"Loaded {len(users)} users to table")
        except SQLAlchemyError as e:
            print(f"Database error loading users: {e}")
        except Exception as e:
            print(f"Error loading users to table: {e}")
            
    def delete_record(self):
        """
        Delete selected row from both database and table
        """
        row_index = self.ui.tableview_loginList.currentIndex().row()
        
        if row_index > -1:
            msg = CustomMessageBox(f"Do you really want to delete selected data ?", "info",
                     parent=self.ui)
            result = msg.exec_()

            if result:  # user pressed Yes / OK
                self.delrow(row_index)
        else:
            msg = CustomMessageBox(f"Please select at least one row", "warning",
                     parent=self.ui)
            msg.exec_()
            
    def modify_record(self):
        """
        Modify selected row in both database and table
        """
        row_index = self.ui.tableview_loginList.currentIndex().row()
        
        if row_index > -1:
            # Get user ID from first column
            user_id_item = self.model.item(row_index, 0)
            if user_id_item:
                user_id = int(user_id_item.text())
                # Open modify dialog (not implemented here)
                # After modification, update database and refresh table
                # self.ui.user_managementTable.refresh_table()
            else:
                print("Error: Could not retrieve user ID for modification")
        else:
            msg = CustomMessageBox(f"Please select at least one row", "warning",
                     parent=self.ui)
            msg.exec_()
    
    
    def delrow(self, row_index):
        """
        Delete row from database and table
        """
        try:
            # Get user ID from first column
            user_id_item = self.model.item(row_index, 0)
            if user_id_item:
                user_id = int(user_id_item.text())
                
                # Delete from database
                session = SessionLocal()
                user = session.query(UserManagement).filter(UserManagement.id == user_id).first()
                if user:
                    session.delete(user)
                    session.commit()
                    session.close()
                
                # Remove row from table
                self.model.removeRow(row_index)
                print(f"Row with user ID {user_id} deleted successfully")
                
                msg = CustomMessageBox(f"User deleted successfully", "success",
                         parent=self.ui)
                msg.exec_()
            else:
                print("Error: Could not retrieve user ID")
        except SQLAlchemyError as e:
            print(f"Database error deleting user: {e}")
            msg = CustomMessageBox(f"Error deleting user from database", "error",
                     parent=self.ui)
            msg.exec_()
        except Exception as e:
            print(f"Error deleting row: {e}")
            msg = CustomMessageBox(f"Error deleting row", "error",
                     parent=self.ui)
            msg.exec_()
                 
    def refresh_table(self):
        """
        Refresh table with latest user data
        """
        try:
            # self.ui.tableview_loginList.setRowCount(0)
            self.load_users_to_table()
            print("Table refreshed")
        except Exception as e:
            print(f"Error refreshing table: {e}")
    

            
    
