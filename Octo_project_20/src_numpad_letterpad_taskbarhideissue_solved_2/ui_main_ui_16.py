# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_ui_16.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide2.QtWidgets import (QApplication, QButtonGroup, QCheckBox, QComboBox,
    QFrame, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLayout, QLineEdit, QMainWindow,
    QPushButton, QRadioButton, QScrollArea, QSizePolicy,
    QSpacerItem, QStackedWidget, QTabWidget, QTableWidget,
    QTableWidgetItem, QToolButton, QVBoxLayout, QWidget)

import os

# Get the directory where the current .py file is located
script_dir = os.path.dirname(os.path.abspath(__file__))



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 490)
        MainWindow.setMinimumSize(QSize(800, 480))
        MainWindow.setMaximumSize(QSize(800, 506))
        MainWindow.setSizeIncrement(QSize(180, 600))
        font = QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"QPushButton:pressed {\n"
"    background-color: #4682B4;  /* darker blue on press */\n"
"    color: white;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.topLayout = QHBoxLayout()
        self.topLayout.setObjectName(u"topLayout")
        self.line_35 = QFrame(self.centralwidget)
        self.line_35.setObjectName(u"line_35")
        self.line_35.setFrameShape(QFrame.Shape.VLine)
        self.line_35.setFrameShadow(QFrame.Shadow.Sunken)

        self.topLayout.addWidget(self.line_35)

        self.label_pageName = QLabel(self.centralwidget)
        self.label_pageName.setObjectName(u"label_pageName")
        font1 = QFont()
        font1.setPointSize(15)
        self.label_pageName.setFont(font1)

        self.topLayout.addWidget(self.label_pageName, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.line_verticalOne = QFrame(self.centralwidget)
        self.line_verticalOne.setObjectName(u"line_verticalOne")
        self.line_verticalOne.setFrameShape(QFrame.Shape.VLine)
        self.line_verticalOne.setFrameShadow(QFrame.Shadow.Sunken)

        self.topLayout.addWidget(self.line_verticalOne)

        self.label_time = QLabel(self.centralwidget)
        self.label_time.setObjectName(u"label_time")
        self.label_time.setFont(font1)

        self.topLayout.addWidget(self.label_time, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.line_verticalTwo = QFrame(self.centralwidget)
        self.line_verticalTwo.setObjectName(u"line_verticalTwo")
        self.line_verticalTwo.setFrameShape(QFrame.Shape.VLine)
        self.line_verticalTwo.setFrameShadow(QFrame.Shadow.Sunken)

        self.topLayout.addWidget(self.line_verticalTwo)

        self.label_date = QLabel(self.centralwidget)
        self.label_date.setObjectName(u"label_date")
        self.label_date.setFont(font1)

        self.topLayout.addWidget(self.label_date, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.verticalLayout.addLayout(self.topLayout)

        self.line_9 = QFrame(self.centralwidget)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.Shape.HLine)
        self.line_9.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_9)

        self.horizontalLayout_36 = QHBoxLayout()
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        font2 = QFont()
        font2.setBold(False)
        self.label_6.setFont(font2)

        self.horizontalLayout_36.addWidget(self.label_6)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_36.addWidget(self.label)

        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_36.addItem(self.horizontalSpacer_24)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 0))
        self.label_5.setBaseSize(QSize(0, 0))
        self.label_5.setPixmap(QPixmap(u"../green_1.png"))

        self.horizontalLayout_36.addWidget(self.label_5, 0, Qt.AlignmentFlag.AlignRight)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setPixmap(QPixmap(u"../red_1_OLD.png"))

        self.horizontalLayout_36.addWidget(self.label_2, 0, Qt.AlignmentFlag.AlignRight)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setPixmap(QPixmap(u"../green_1.png"))

        self.horizontalLayout_36.addWidget(self.label_4, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout.addLayout(self.horizontalLayout_36)

        self.line_header = QFrame(self.centralwidget)
        self.line_header.setObjectName(u"line_header")
        self.line_header.setFrameShape(QFrame.Shape.HLine)
        self.line_header.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_header)

        self.stackedWidget_main = QStackedWidget(self.centralwidget)
        self.stackedWidget_main.setObjectName(u"stackedWidget_main")
        self.stackedWidget_main.setFont(font)
        self.page1 = QWidget()
        self.page1.setObjectName(u"page1")
        self.page1Layout = QVBoxLayout(self.page1)
        self.page1Layout.setObjectName(u"page1Layout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.page1)
        self.label_3.setObjectName(u"label_3")
        font3 = QFont()
        font3.setPointSize(15)
        font3.setBold(True)
        self.label_3.setFont(font3)

        self.horizontalLayout_4.addWidget(self.label_3, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignBottom)


        self.page1Layout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_username = QLabel(self.page1)
        self.label_username.setObjectName(u"label_username")
        self.label_username.setFont(font3)

        self.horizontalLayout.addWidget(self.label_username, 0, Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignBottom)

        self.lineEdit_usernameLogin = QLineEdit(self.page1)
        self.lineEdit_usernameLogin.setObjectName(u"lineEdit_usernameLogin")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_usernameLogin.sizePolicy().hasHeightForWidth())
        self.lineEdit_usernameLogin.setSizePolicy(sizePolicy)
        self.lineEdit_usernameLogin.setFont(font1)

        self.horizontalLayout.addWidget(self.lineEdit_usernameLogin, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignBottom)


        self.page1Layout.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 25, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.page1Layout.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_password = QLabel(self.page1)
        self.label_password.setObjectName(u"label_password")
        self.label_password.setFont(font3)

        self.horizontalLayout_2.addWidget(self.label_password, 0, Qt.AlignmentFlag.AlignRight)

        self.lineEdit_passwordLogin = QLineEdit(self.page1)
        self.lineEdit_passwordLogin.setObjectName(u"lineEdit_passwordLogin")
        sizePolicy.setHeightForWidth(self.lineEdit_passwordLogin.sizePolicy().hasHeightForWidth())
        self.lineEdit_passwordLogin.setSizePolicy(sizePolicy)
        self.lineEdit_passwordLogin.setFont(font1)
        self.lineEdit_passwordLogin.setEchoMode(QLineEdit.EchoMode.Password)

        self.horizontalLayout_2.addWidget(self.lineEdit_passwordLogin, 0, Qt.AlignmentFlag.AlignLeft)


        self.page1Layout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 25, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.page1Layout.addItem(self.verticalSpacer_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.button_login = QPushButton(self.page1)
        self.button_login.setObjectName(u"button_login")
        self.button_login.setFont(font1)

        self.horizontalLayout_3.addWidget(self.button_login, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)


        self.page1Layout.addLayout(self.horizontalLayout_3)

        self.stackedWidget_main.addWidget(self.page1)
        self.page2 = QWidget()
        self.page2.setObjectName(u"page2")
        self.page2Layout = QVBoxLayout(self.page2)
        self.page2Layout.setObjectName(u"page2Layout")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.button_addUpdateLogin = QPushButton(self.page2)
        self.button_addUpdateLogin.setObjectName(u"button_addUpdateLogin")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.button_addUpdateLogin.sizePolicy().hasHeightForWidth())
        self.button_addUpdateLogin.setSizePolicy(sizePolicy1)
        self.button_addUpdateLogin.setFont(font1)

        self.horizontalLayout_5.addWidget(self.button_addUpdateLogin, 0, Qt.AlignmentFlag.AlignHCenter)

        self.button_modifyLogin = QPushButton(self.page2)
        self.button_modifyLogin.setObjectName(u"button_modifyLogin")
        self.button_modifyLogin.setFont(font1)

        self.horizontalLayout_5.addWidget(self.button_modifyLogin, 0, Qt.AlignmentFlag.AlignHCenter)

        self.button_deleteLogin = QPushButton(self.page2)
        self.button_deleteLogin.setObjectName(u"button_deleteLogin")
        self.button_deleteLogin.setFont(font1)

        self.horizontalLayout_5.addWidget(self.button_deleteLogin, 0, Qt.AlignmentFlag.AlignHCenter)


        self.page2Layout.addLayout(self.horizontalLayout_5)

        self.tableWidget_login = QTableWidget(self.page2)
        self.tableWidget_login.setObjectName(u"tableWidget_login")
        self.tableWidget_login.setFont(font)

        self.page2Layout.addWidget(self.tableWidget_login)

        self.stackedWidget_main.addWidget(self.page2)
        self.page3 = QWidget()
        self.page3.setObjectName(u"page3")
        self.page3Layout = QVBoxLayout(self.page3)
        self.page3Layout.setObjectName(u"page3Layout")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_setUsernameLogin = QLabel(self.page3)
        self.label_setUsernameLogin.setObjectName(u"label_setUsernameLogin")
        self.label_setUsernameLogin.setFont(font1)

        self.horizontalLayout_6.addWidget(self.label_setUsernameLogin, 0, Qt.AlignmentFlag.AlignRight)

        self.lineEdit_setUsernameLogin = QLineEdit(self.page3)
        self.lineEdit_setUsernameLogin.setObjectName(u"lineEdit_setUsernameLogin")
        sizePolicy.setHeightForWidth(self.lineEdit_setUsernameLogin.sizePolicy().hasHeightForWidth())
        self.lineEdit_setUsernameLogin.setSizePolicy(sizePolicy)
        self.lineEdit_setUsernameLogin.setFont(font1)

        self.horizontalLayout_6.addWidget(self.lineEdit_setUsernameLogin, 0, Qt.AlignmentFlag.AlignLeft)


        self.page3Layout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_setPasswordLogin = QLabel(self.page3)
        self.label_setPasswordLogin.setObjectName(u"label_setPasswordLogin")
        self.label_setPasswordLogin.setFont(font1)

        self.horizontalLayout_7.addWidget(self.label_setPasswordLogin, 0, Qt.AlignmentFlag.AlignRight)

        self.lineEdit_setPasswordLogin = QLineEdit(self.page3)
        self.lineEdit_setPasswordLogin.setObjectName(u"lineEdit_setPasswordLogin")
        sizePolicy.setHeightForWidth(self.lineEdit_setPasswordLogin.sizePolicy().hasHeightForWidth())
        self.lineEdit_setPasswordLogin.setSizePolicy(sizePolicy)
        self.lineEdit_setPasswordLogin.setFont(font1)

        self.horizontalLayout_7.addWidget(self.lineEdit_setPasswordLogin, 0, Qt.AlignmentFlag.AlignLeft)


        self.page3Layout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_setAccessLogin = QLabel(self.page3)
        self.label_setAccessLogin.setObjectName(u"label_setAccessLogin")
        self.label_setAccessLogin.setFont(font1)

        self.horizontalLayout_9.addWidget(self.label_setAccessLogin, 0, Qt.AlignmentFlag.AlignRight)

        self.comboBox_setAccessCombo = QComboBox(self.page3)
        self.comboBox_setAccessCombo.addItem("")
        self.comboBox_setAccessCombo.addItem("")
        self.comboBox_setAccessCombo.addItem("")
        self.comboBox_setAccessCombo.setObjectName(u"comboBox_setAccessCombo")
        self.comboBox_setAccessCombo.setMinimumSize(QSize(150, 0))
        self.comboBox_setAccessCombo.setFont(font1)

        self.horizontalLayout_9.addWidget(self.comboBox_setAccessCombo, 0, Qt.AlignmentFlag.AlignLeft)


        self.page3Layout.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.button_addUpdateLogin_2 = QPushButton(self.page3)
        self.button_addUpdateLogin_2.setObjectName(u"button_addUpdateLogin_2")
        self.button_addUpdateLogin_2.setFont(font1)

        self.horizontalLayout_10.addWidget(self.button_addUpdateLogin_2, 0, Qt.AlignmentFlag.AlignHCenter)


        self.page3Layout.addLayout(self.horizontalLayout_10)

        self.stackedWidget_main.addWidget(self.page3)
        self.page4 = QWidget()
        self.page4.setObjectName(u"page4")
        self.page4Layout = QVBoxLayout(self.page4)
        self.page4Layout.setObjectName(u"page4Layout")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_5)

        self.label_rs232 = QLabel(self.page4)
        self.label_rs232.setObjectName(u"label_rs232")
        self.label_rs232.setFont(font1)

        self.horizontalLayout_8.addWidget(self.label_rs232, 0, Qt.AlignmentFlag.AlignRight)

        self.toggleButton_rs232 = QLabel(self.page4)
        self.toggleButton_rs232.setObjectName(u"toggleButton_rs232")
        self.toggleButton_rs232.setMinimumSize(QSize(100, 0))

        # Build the full path to your image
        image_path = os.path.join(script_dir, "Switcher_On.png")  # if it's in the same folder
        # Or if it's in a parent folder: os.path.join(script_dir, "..", "Switcher_On.png")
        self.toggleButton_rs232.setPixmap(QPixmap(image_path))

        self.horizontalLayout_8.addWidget(self.toggleButton_rs232, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_rs232OnOff = QLabel(self.page4)
        self.label_rs232OnOff.setObjectName(u"label_rs232OnOff")
        self.label_rs232OnOff.setFont(font1)

        self.horizontalLayout_8.addWidget(self.label_rs232OnOff, 0, Qt.AlignmentFlag.AlignLeft)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_6)


        self.page4Layout.addLayout(self.horizontalLayout_8)

        self.verticalSpacer_11 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.page4Layout.addItem(self.verticalSpacer_11)

        self.line = QFrame(self.page4)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.page4Layout.addWidget(self.line)

        self.verticalSpacer_3 = QSpacerItem(20, 35, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.page4Layout.addItem(self.verticalSpacer_3)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_baudRate = QLabel(self.page4)
        self.label_baudRate.setObjectName(u"label_baudRate")
        self.label_baudRate.setFont(font)

        self.horizontalLayout_11.addWidget(self.label_baudRate, 0, Qt.AlignmentFlag.AlignRight)

        self.comboBox_baudRate = QComboBox(self.page4)
        self.comboBox_baudRate.addItem("")
        self.comboBox_baudRate.addItem("")
        self.comboBox_baudRate.addItem("")
        self.comboBox_baudRate.addItem("")
        self.comboBox_baudRate.addItem("")
        self.comboBox_baudRate.setObjectName(u"comboBox_baudRate")
        sizePolicy.setHeightForWidth(self.comboBox_baudRate.sizePolicy().hasHeightForWidth())
        self.comboBox_baudRate.setSizePolicy(sizePolicy)
        self.comboBox_baudRate.setMaximumSize(QSize(300, 16777215))
        self.comboBox_baudRate.setFont(font)

        self.horizontalLayout_11.addWidget(self.comboBox_baudRate)

        self.label_dataBits = QLabel(self.page4)
        self.label_dataBits.setObjectName(u"label_dataBits")
        self.label_dataBits.setFont(font)

        self.horizontalLayout_11.addWidget(self.label_dataBits, 0, Qt.AlignmentFlag.AlignRight)

        self.comboBox_dataBits = QComboBox(self.page4)
        self.comboBox_dataBits.addItem("")
        self.comboBox_dataBits.addItem("")
        self.comboBox_dataBits.addItem("")
        self.comboBox_dataBits.addItem("")
        self.comboBox_dataBits.setObjectName(u"comboBox_dataBits")
        self.comboBox_dataBits.setFont(font)

        self.horizontalLayout_11.addWidget(self.comboBox_dataBits)

        self.horizontalSpacer_2 = QSpacerItem(30, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_2)


        self.page4Layout.addLayout(self.horizontalLayout_11)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.page4Layout.addItem(self.verticalSpacer_4)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_parity = QLabel(self.page4)
        self.label_parity.setObjectName(u"label_parity")
        self.label_parity.setFont(font)

        self.horizontalLayout_12.addWidget(self.label_parity, 0, Qt.AlignmentFlag.AlignRight)

        self.comboBox_parity = QComboBox(self.page4)
        self.comboBox_parity.addItem("")
        self.comboBox_parity.addItem("")
        self.comboBox_parity.addItem("")
        self.comboBox_parity.addItem("")
        self.comboBox_parity.addItem("")
        self.comboBox_parity.setObjectName(u"comboBox_parity")
        self.comboBox_parity.setFont(font)

        self.horizontalLayout_12.addWidget(self.comboBox_parity)

        self.label_stopBits = QLabel(self.page4)
        self.label_stopBits.setObjectName(u"label_stopBits")
        self.label_stopBits.setFont(font)

        self.horizontalLayout_12.addWidget(self.label_stopBits, 0, Qt.AlignmentFlag.AlignRight)

        self.comboBox_stopBits = QComboBox(self.page4)
        self.comboBox_stopBits.addItem("")
        self.comboBox_stopBits.addItem("")
        self.comboBox_stopBits.addItem("")
        self.comboBox_stopBits.setObjectName(u"comboBox_stopBits")
        self.comboBox_stopBits.setFont(font)

        self.horizontalLayout_12.addWidget(self.comboBox_stopBits)

        self.horizontalSpacer_3 = QSpacerItem(30, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_3)


        self.page4Layout.addLayout(self.horizontalLayout_12)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.page4Layout.addItem(self.verticalSpacer_5)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_flowControl = QLabel(self.page4)
        self.label_flowControl.setObjectName(u"label_flowControl")
        self.label_flowControl.setFont(font)

        self.horizontalLayout_13.addWidget(self.label_flowControl, 0, Qt.AlignmentFlag.AlignRight)

        self.comboBox_flowControl = QComboBox(self.page4)
        self.comboBox_flowControl.addItem("")
        self.comboBox_flowControl.addItem("")
        self.comboBox_flowControl.addItem("")
        self.comboBox_flowControl.setObjectName(u"comboBox_flowControl")
        self.comboBox_flowControl.setFont(font)

        self.horizontalLayout_13.addWidget(self.comboBox_flowControl)

        self.label_portName = QLabel(self.page4)
        self.label_portName.setObjectName(u"label_portName")
        self.label_portName.setFont(font)

        self.horizontalLayout_13.addWidget(self.label_portName, 0, Qt.AlignmentFlag.AlignRight)

        self.lineEdit_portName = QLineEdit(self.page4)
        self.lineEdit_portName.setObjectName(u"lineEdit_portName")
        sizePolicy.setHeightForWidth(self.lineEdit_portName.sizePolicy().hasHeightForWidth())
        self.lineEdit_portName.setSizePolicy(sizePolicy)
        self.lineEdit_portName.setFont(font)

        self.horizontalLayout_13.addWidget(self.lineEdit_portName)

        self.horizontalSpacer_4 = QSpacerItem(30, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_4)


        self.page4Layout.addLayout(self.horizontalLayout_13)

        self.verticalSpacer_6 = QSpacerItem(20, 50, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.page4Layout.addItem(self.verticalSpacer_6)

        self.stackedWidget_main.addWidget(self.page4)
        self.page5 = QWidget()
        self.page5.setObjectName(u"page5")
        self.page5Layout = QVBoxLayout(self.page5)
        self.page5Layout.setObjectName(u"page5Layout")
        self.horizontalLayout_83 = QHBoxLayout()
        self.horizontalLayout_83.setObjectName(u"horizontalLayout_83")
        self.label_dimensionFormulaBar = QLabel(self.page5)
        self.label_dimensionFormulaBar.setObjectName(u"label_dimensionFormulaBar")
        self.label_dimensionFormulaBar.setMaximumSize(QSize(50, 16777215))
        self.label_dimensionFormulaBar.setFont(font1)

        self.horizontalLayout_83.addWidget(self.label_dimensionFormulaBar)

        self.lineEdit_formulaBar = QLineEdit(self.page5)
        self.lineEdit_formulaBar.setObjectName(u"lineEdit_formulaBar")
        sizePolicy.setHeightForWidth(self.lineEdit_formulaBar.sizePolicy().hasHeightForWidth())
        self.lineEdit_formulaBar.setSizePolicy(sizePolicy)
        self.lineEdit_formulaBar.setMinimumSize(QSize(0, 50))
        self.lineEdit_formulaBar.setFont(font1)

        self.horizontalLayout_83.addWidget(self.lineEdit_formulaBar)


        self.page5Layout.addLayout(self.horizontalLayout_83)

        self.line_2 = QFrame(self.page5)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.page5Layout.addWidget(self.line_2)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalSpacer_46 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_46)

        self.label_16 = QLabel(self.page5)
        self.label_16.setObjectName(u"label_16")
        font4 = QFont()
        font4.setPointSize(20)
        self.label_16.setFont(font4)

        self.horizontalLayout_15.addWidget(self.label_16)

        self.comboBox_probeFormulaBar = QComboBox(self.page5)
        self.comboBox_probeFormulaBar.addItem("")
        self.comboBox_probeFormulaBar.addItem("")
        self.comboBox_probeFormulaBar.setObjectName(u"comboBox_probeFormulaBar")
        self.comboBox_probeFormulaBar.setFont(font4)

        self.horizontalLayout_15.addWidget(self.comboBox_probeFormulaBar, 0, Qt.AlignmentFlag.AlignHCenter)

        self.button_addFormulaBar = QPushButton(self.page5)
        self.button_addFormulaBar.setObjectName(u"button_addFormulaBar")
        sizePolicy.setHeightForWidth(self.button_addFormulaBar.sizePolicy().hasHeightForWidth())
        self.button_addFormulaBar.setSizePolicy(sizePolicy)
        self.button_addFormulaBar.setFont(font4)

        self.horizontalLayout_15.addWidget(self.button_addFormulaBar)

        self.horizontalSpacer_47 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_47)


        self.page5Layout.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_7)

        self.button_plusFormulaBar = QPushButton(self.page5)
        self.button_plusFormulaBar.setObjectName(u"button_plusFormulaBar")
        sizePolicy.setHeightForWidth(self.button_plusFormulaBar.sizePolicy().hasHeightForWidth())
        self.button_plusFormulaBar.setSizePolicy(sizePolicy)
        self.button_plusFormulaBar.setMaximumSize(QSize(50, 50))
        self.button_plusFormulaBar.setFont(font4)

        self.horizontalLayout_14.addWidget(self.button_plusFormulaBar)

        self.button_minusFormulaBar = QPushButton(self.page5)
        self.button_minusFormulaBar.setObjectName(u"button_minusFormulaBar")
        sizePolicy.setHeightForWidth(self.button_minusFormulaBar.sizePolicy().hasHeightForWidth())
        self.button_minusFormulaBar.setSizePolicy(sizePolicy)
        self.button_minusFormulaBar.setMaximumSize(QSize(50, 50))
        self.button_minusFormulaBar.setFont(font4)

        self.horizontalLayout_14.addWidget(self.button_minusFormulaBar)

        self.button_multiplicationFormulaBar = QPushButton(self.page5)
        self.button_multiplicationFormulaBar.setObjectName(u"button_multiplicationFormulaBar")
        sizePolicy.setHeightForWidth(self.button_multiplicationFormulaBar.sizePolicy().hasHeightForWidth())
        self.button_multiplicationFormulaBar.setSizePolicy(sizePolicy)
        self.button_multiplicationFormulaBar.setMaximumSize(QSize(50, 50))
        self.button_multiplicationFormulaBar.setFont(font4)

        self.horizontalLayout_14.addWidget(self.button_multiplicationFormulaBar)

        self.button_divisionFormulaBar = QPushButton(self.page5)
        self.button_divisionFormulaBar.setObjectName(u"button_divisionFormulaBar")
        sizePolicy.setHeightForWidth(self.button_divisionFormulaBar.sizePolicy().hasHeightForWidth())
        self.button_divisionFormulaBar.setSizePolicy(sizePolicy)
        self.button_divisionFormulaBar.setMaximumSize(QSize(50, 50))
        self.button_divisionFormulaBar.setFont(font4)

        self.horizontalLayout_14.addWidget(self.button_divisionFormulaBar)

        self.button_modFormulaBar = QPushButton(self.page5)
        self.button_modFormulaBar.setObjectName(u"button_modFormulaBar")
        self.button_modFormulaBar.setMaximumSize(QSize(50, 50))
        self.button_modFormulaBar.setFont(font1)

        self.horizontalLayout_14.addWidget(self.button_modFormulaBar)

        self.button_commaFormulaBar = QPushButton(self.page5)
        self.button_commaFormulaBar.setObjectName(u"button_commaFormulaBar")
        self.button_commaFormulaBar.setMaximumSize(QSize(50, 50))
        self.button_commaFormulaBar.setFont(font4)

        self.horizontalLayout_14.addWidget(self.button_commaFormulaBar)

        self.button_backspaceFormulaBar = QPushButton(self.page5)
        self.button_backspaceFormulaBar.setObjectName(u"button_backspaceFormulaBar")
        self.button_backspaceFormulaBar.setMaximumSize(QSize(50, 50))
        self.button_backspaceFormulaBar.setFont(font1)

        self.horizontalLayout_14.addWidget(self.button_backspaceFormulaBar)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_8)


        self.page5Layout.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalSpacer_48 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_48)

        self.button_leftBraceFormulaBar = QPushButton(self.page5)
        self.button_leftBraceFormulaBar.setObjectName(u"button_leftBraceFormulaBar")
        self.button_leftBraceFormulaBar.setMaximumSize(QSize(50, 50))
        self.button_leftBraceFormulaBar.setFont(font1)

        self.horizontalLayout_16.addWidget(self.button_leftBraceFormulaBar)

        self.button_maxFormulaBar = QPushButton(self.page5)
        self.button_maxFormulaBar.setObjectName(u"button_maxFormulaBar")
        sizePolicy.setHeightForWidth(self.button_maxFormulaBar.sizePolicy().hasHeightForWidth())
        self.button_maxFormulaBar.setSizePolicy(sizePolicy)
        self.button_maxFormulaBar.setMaximumSize(QSize(50, 50))
        self.button_maxFormulaBar.setFont(font1)

        self.horizontalLayout_16.addWidget(self.button_maxFormulaBar)

        self.button_minFormulaBar = QPushButton(self.page5)
        self.button_minFormulaBar.setObjectName(u"button_minFormulaBar")
        self.button_minFormulaBar.setMaximumSize(QSize(50, 50))
        self.button_minFormulaBar.setFont(font1)

        self.horizontalLayout_16.addWidget(self.button_minFormulaBar)

        self.button_avgFormulaBar = QPushButton(self.page5)
        self.button_avgFormulaBar.setObjectName(u"button_avgFormulaBar")
        self.button_avgFormulaBar.setMaximumSize(QSize(50, 50))
        self.button_avgFormulaBar.setFont(font1)

        self.horizontalLayout_16.addWidget(self.button_avgFormulaBar)

        self.button_absFormulaBar = QPushButton(self.page5)
        self.button_absFormulaBar.setObjectName(u"button_absFormulaBar")
        self.button_absFormulaBar.setMaximumSize(QSize(55, 50))
        self.button_absFormulaBar.setFont(font1)

        self.horizontalLayout_16.addWidget(self.button_absFormulaBar)

        self.button_rightBraceFormulaBar = QPushButton(self.page5)
        self.button_rightBraceFormulaBar.setObjectName(u"button_rightBraceFormulaBar")
        self.button_rightBraceFormulaBar.setMaximumSize(QSize(50, 50))
        self.button_rightBraceFormulaBar.setFont(font1)

        self.horizontalLayout_16.addWidget(self.button_rightBraceFormulaBar)

        self.horizontalSpacer_49 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_49)


        self.page5Layout.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalSpacer_50 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_50)

        self.button_sinFormulaBar = QPushButton(self.page5)
        self.button_sinFormulaBar.setObjectName(u"button_sinFormulaBar")
        self.button_sinFormulaBar.setMaximumSize(QSize(50, 50))
        self.button_sinFormulaBar.setFont(font1)

        self.horizontalLayout_17.addWidget(self.button_sinFormulaBar)

        self.button_cosFormulaBar = QPushButton(self.page5)
        self.button_cosFormulaBar.setObjectName(u"button_cosFormulaBar")
        self.button_cosFormulaBar.setMaximumSize(QSize(50, 50))
        self.button_cosFormulaBar.setFont(font1)

        self.horizontalLayout_17.addWidget(self.button_cosFormulaBar)

        self.button_tanFormulaBar = QPushButton(self.page5)
        self.button_tanFormulaBar.setObjectName(u"button_tanFormulaBar")
        self.button_tanFormulaBar.setMaximumSize(QSize(50, 50))
        self.button_tanFormulaBar.setFont(font1)

        self.horizontalLayout_17.addWidget(self.button_tanFormulaBar)

        self.button_cosecFormulaBar = QPushButton(self.page5)
        self.button_cosecFormulaBar.setObjectName(u"button_cosecFormulaBar")
        self.button_cosecFormulaBar.setMaximumSize(QSize(60, 50))
        self.button_cosecFormulaBar.setFont(font1)

        self.horizontalLayout_17.addWidget(self.button_cosecFormulaBar)

        self.button_secFormulaBar = QPushButton(self.page5)
        self.button_secFormulaBar.setObjectName(u"button_secFormulaBar")
        self.button_secFormulaBar.setMaximumSize(QSize(50, 50))
        self.button_secFormulaBar.setFont(font1)

        self.horizontalLayout_17.addWidget(self.button_secFormulaBar)

        self.button_cotFormulaBar = QPushButton(self.page5)
        self.button_cotFormulaBar.setObjectName(u"button_cotFormulaBar")
        self.button_cotFormulaBar.setMaximumSize(QSize(50, 50))
        self.button_cotFormulaBar.setFont(font1)

        self.horizontalLayout_17.addWidget(self.button_cotFormulaBar)

        self.horizontalSpacer_51 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_51)


        self.page5Layout.addLayout(self.horizontalLayout_17)

        self.line_26 = QFrame(self.page5)
        self.line_26.setObjectName(u"line_26")
        self.line_26.setFrameShape(QFrame.Shape.HLine)
        self.line_26.setFrameShadow(QFrame.Shadow.Sunken)

        self.page5Layout.addWidget(self.line_26)

        self.horizontalLayout_94 = QHBoxLayout()
        self.horizontalLayout_94.setObjectName(u"horizontalLayout_94")
        self.button_saveSettingsFormulaBar = QPushButton(self.page5)
        self.button_saveSettingsFormulaBar.setObjectName(u"button_saveSettingsFormulaBar")
        sizePolicy.setHeightForWidth(self.button_saveSettingsFormulaBar.sizePolicy().hasHeightForWidth())
        self.button_saveSettingsFormulaBar.setSizePolicy(sizePolicy)
        self.button_saveSettingsFormulaBar.setMaximumSize(QSize(16777215, 50))
        self.button_saveSettingsFormulaBar.setFont(font1)

        self.horizontalLayout_94.addWidget(self.button_saveSettingsFormulaBar, 0, Qt.AlignmentFlag.AlignHCenter)


        self.page5Layout.addLayout(self.horizontalLayout_94)

        self.stackedWidget_main.addWidget(self.page5)
        self.page6 = QWidget()
        self.page6.setObjectName(u"page6")
        self.page6Layout = QVBoxLayout(self.page6)
        self.page6Layout.setObjectName(u"page6Layout")
        self.verticalSpacer_16 = QSpacerItem(20, 70, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.page6Layout.addItem(self.verticalSpacer_16)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_selfIp = QLabel(self.page6)
        self.label_selfIp.setObjectName(u"label_selfIp")
        self.label_selfIp.setFont(font)

        self.horizontalLayout_18.addWidget(self.label_selfIp, 0, Qt.AlignmentFlag.AlignRight)

        self.lineEdit_selfIp = QLineEdit(self.page6)
        self.lineEdit_selfIp.setObjectName(u"lineEdit_selfIp")
        sizePolicy.setHeightForWidth(self.lineEdit_selfIp.sizePolicy().hasHeightForWidth())
        self.lineEdit_selfIp.setSizePolicy(sizePolicy)
        self.lineEdit_selfIp.setMinimumSize(QSize(200, 0))
        self.lineEdit_selfIp.setFont(font)

        self.horizontalLayout_18.addWidget(self.lineEdit_selfIp, 0, Qt.AlignmentFlag.AlignLeft)


        self.page6Layout.addLayout(self.horizontalLayout_18)

        self.verticalSpacer_13 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.page6Layout.addItem(self.verticalSpacer_13)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_subnetMask = QLabel(self.page6)
        self.label_subnetMask.setObjectName(u"label_subnetMask")
        self.label_subnetMask.setFont(font)

        self.horizontalLayout_19.addWidget(self.label_subnetMask, 0, Qt.AlignmentFlag.AlignRight)

        self.lineEdit_subnetMask = QLineEdit(self.page6)
        self.lineEdit_subnetMask.setObjectName(u"lineEdit_subnetMask")
        sizePolicy.setHeightForWidth(self.lineEdit_subnetMask.sizePolicy().hasHeightForWidth())
        self.lineEdit_subnetMask.setSizePolicy(sizePolicy)
        self.lineEdit_subnetMask.setMinimumSize(QSize(200, 0))
        self.lineEdit_subnetMask.setFont(font)

        self.horizontalLayout_19.addWidget(self.lineEdit_subnetMask, 0, Qt.AlignmentFlag.AlignLeft)


        self.page6Layout.addLayout(self.horizontalLayout_19)

        self.verticalSpacer_14 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.page6Layout.addItem(self.verticalSpacer_14)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_defaultGateway = QLabel(self.page6)
        self.label_defaultGateway.setObjectName(u"label_defaultGateway")
        self.label_defaultGateway.setFont(font)

        self.horizontalLayout_20.addWidget(self.label_defaultGateway, 0, Qt.AlignmentFlag.AlignRight)

        self.lineEdit_defaultGateway = QLineEdit(self.page6)
        self.lineEdit_defaultGateway.setObjectName(u"lineEdit_defaultGateway")
        sizePolicy.setHeightForWidth(self.lineEdit_defaultGateway.sizePolicy().hasHeightForWidth())
        self.lineEdit_defaultGateway.setSizePolicy(sizePolicy)
        self.lineEdit_defaultGateway.setMinimumSize(QSize(200, 0))
        self.lineEdit_defaultGateway.setFont(font)

        self.horizontalLayout_20.addWidget(self.lineEdit_defaultGateway, 0, Qt.AlignmentFlag.AlignLeft)


        self.page6Layout.addLayout(self.horizontalLayout_20)

        self.verticalSpacer_15 = QSpacerItem(20, 50, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.page6Layout.addItem(self.verticalSpacer_15)

        self.stackedWidget_main.addWidget(self.page6)
        self.page7 = QWidget()
        self.page7.setObjectName(u"page7")
        self.page7Layout = QVBoxLayout(self.page7)
        self.page7Layout.setObjectName(u"page7Layout")
        self.verticalSpacer_18 = QSpacerItem(20, 70, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.page7Layout.addItem(self.verticalSpacer_18)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_wifiSsid = QLabel(self.page7)
        self.label_wifiSsid.setObjectName(u"label_wifiSsid")
        self.label_wifiSsid.setFont(font)

        self.horizontalLayout_21.addWidget(self.label_wifiSsid, 0, Qt.AlignmentFlag.AlignRight)

        self.lineEdit_wifiSsid = QLineEdit(self.page7)
        self.lineEdit_wifiSsid.setObjectName(u"lineEdit_wifiSsid")
        sizePolicy.setHeightForWidth(self.lineEdit_wifiSsid.sizePolicy().hasHeightForWidth())
        self.lineEdit_wifiSsid.setSizePolicy(sizePolicy)
        self.lineEdit_wifiSsid.setFont(font)

        self.horizontalLayout_21.addWidget(self.lineEdit_wifiSsid, 0, Qt.AlignmentFlag.AlignLeft)


        self.page7Layout.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_wifiPassword = QLabel(self.page7)
        self.label_wifiPassword.setObjectName(u"label_wifiPassword")
        self.label_wifiPassword.setFont(font)

        self.horizontalLayout_22.addWidget(self.label_wifiPassword, 0, Qt.AlignmentFlag.AlignRight)

        self.lineEdit_wifiPassword = QLineEdit(self.page7)
        self.lineEdit_wifiPassword.setObjectName(u"lineEdit_wifiPassword")
        sizePolicy.setHeightForWidth(self.lineEdit_wifiPassword.sizePolicy().hasHeightForWidth())
        self.lineEdit_wifiPassword.setSizePolicy(sizePolicy)
        self.lineEdit_wifiPassword.setFont(font)

        self.horizontalLayout_22.addWidget(self.lineEdit_wifiPassword, 0, Qt.AlignmentFlag.AlignLeft)


        self.page7Layout.addLayout(self.horizontalLayout_22)

        self.verticalSpacer_17 = QSpacerItem(20, 70, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.page7Layout.addItem(self.verticalSpacer_17)

        self.stackedWidget_main.addWidget(self.page7)
        self.page8 = QWidget()
        self.page8.setObjectName(u"page8")
        self.page8Layout = QVBoxLayout(self.page8)
        self.page8Layout.setObjectName(u"page8Layout")
        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_buzzer = QLabel(self.page8)
        self.label_buzzer.setObjectName(u"label_buzzer")
        self.label_buzzer.setFont(font)

        self.horizontalLayout_24.addWidget(self.label_buzzer, 0, Qt.AlignmentFlag.AlignLeft)

        self.toggleButton_buzzer = QLabel(self.page8)
        self.toggleButton_buzzer.setObjectName(u"toggleButton_buzzer")

        image_path = os.path.join(script_dir, "Switcher_On.png")  # if it's in the same folder
        self.toggleButton_buzzer.setPixmap(QPixmap(image_path))

        self.horizontalLayout_24.addWidget(self.toggleButton_buzzer, 0, Qt.AlignmentFlag.AlignLeft)

        self.label_buzzerOnOff = QLabel(self.page8)
        self.label_buzzerOnOff.setObjectName(u"label_buzzerOnOff")
        self.label_buzzerOnOff.setFont(font)

        self.horizontalLayout_24.addWidget(self.label_buzzerOnOff, 0, Qt.AlignmentFlag.AlignLeft)

        self.horizontalSpacer_171 = QSpacerItem(130, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_171)

        self.horizontalSpacer_9 = QSpacerItem(0, 0, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_9)

        self.radioButton_okBuzzer = QRadioButton(self.page8)
        self.buttonGroup = QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.radioButton_okBuzzer)
        self.radioButton_okBuzzer.setObjectName(u"radioButton_okBuzzer")
        self.radioButton_okBuzzer.setFont(font)

        self.horizontalLayout_24.addWidget(self.radioButton_okBuzzer, 0, Qt.AlignmentFlag.AlignLeft)

        self.radioButton_reworkNotokBuzzer = QRadioButton(self.page8)
        self.buttonGroup.addButton(self.radioButton_reworkNotokBuzzer)
        self.radioButton_reworkNotokBuzzer.setObjectName(u"radioButton_reworkNotokBuzzer")
        self.radioButton_reworkNotokBuzzer.setFont(font)

        self.horizontalLayout_24.addWidget(self.radioButton_reworkNotokBuzzer, 0, Qt.AlignmentFlag.AlignLeft)

        self.horizontalSpacer_15 = QSpacerItem(90, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_15)


        self.page8Layout.addLayout(self.horizontalLayout_24)

        self.line_3 = QFrame(self.page8)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.page8Layout.addWidget(self.line_3)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_relay = QLabel(self.page8)
        self.label_relay.setObjectName(u"label_relay")
        self.label_relay.setFont(font)

        self.horizontalLayout_25.addWidget(self.label_relay, 0, Qt.AlignmentFlag.AlignLeft)

        self.toggelButton_relay = QLabel(self.page8)
        self.toggelButton_relay.setObjectName(u"toggelButton_relay")
        self.toggelButton_relay.setFont(font)

        image_path = os.path.join(script_dir, "Switcher_On.png")  # if it's in the same folder
        self.toggelButton_relay.setPixmap(QPixmap(image_path))

        self.horizontalLayout_25.addWidget(self.toggelButton_relay, 0, Qt.AlignmentFlag.AlignRight)

        self.label_relayOnOff = QLabel(self.page8)
        self.label_relayOnOff.setObjectName(u"label_relayOnOff")
        self.label_relayOnOff.setFont(font)

        self.horizontalLayout_25.addWidget(self.label_relayOnOff)

        self.horizontalSpacer_10 = QSpacerItem(130, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_10)

        self.label_relayTime = QLabel(self.page8)
        self.label_relayTime.setObjectName(u"label_relayTime")
        self.label_relayTime.setFont(font)

        self.horizontalLayout_25.addWidget(self.label_relayTime)

        self.lineEdit_relayTime = QLineEdit(self.page8)
        self.lineEdit_relayTime.setObjectName(u"lineEdit_relayTime")
        sizePolicy.setHeightForWidth(self.lineEdit_relayTime.sizePolicy().hasHeightForWidth())
        self.lineEdit_relayTime.setSizePolicy(sizePolicy)
        self.lineEdit_relayTime.setFont(font)

        self.horizontalLayout_25.addWidget(self.lineEdit_relayTime)

        self.horizontalSpacer_16 = QSpacerItem(90, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_16)


        self.page8Layout.addLayout(self.horizontalLayout_25)

        self.line_4 = QFrame(self.page8)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.page8Layout.addWidget(self.line_4)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_cycleStopTimer = QLabel(self.page8)
        self.label_cycleStopTimer.setObjectName(u"label_cycleStopTimer")
        self.label_cycleStopTimer.setFont(font)

        self.horizontalLayout_26.addWidget(self.label_cycleStopTimer, 0, Qt.AlignmentFlag.AlignLeft)

        self.toggelButton_cycleStopTimer = QLabel(self.page8)
        self.toggelButton_cycleStopTimer.setObjectName(u"toggelButton_cycleStopTimer")
        self.toggelButton_cycleStopTimer.setFont(font)

        image_path = os.path.join(script_dir, "Switcher_On.png")  # if it's in the same folder
        self.toggelButton_cycleStopTimer.setPixmap(QPixmap(image_path))

        self.horizontalLayout_26.addWidget(self.toggelButton_cycleStopTimer)

        self.label_cycleStopTimerOnOff = QLabel(self.page8)
        self.label_cycleStopTimerOnOff.setObjectName(u"label_cycleStopTimerOnOff")
        self.label_cycleStopTimerOnOff.setFont(font)

        self.horizontalLayout_26.addWidget(self.label_cycleStopTimerOnOff)

        self.horizontalSpacer_11 = QSpacerItem(130, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_11)

        self.label_cycleTime = QLabel(self.page8)
        self.label_cycleTime.setObjectName(u"label_cycleTime")
        self.label_cycleTime.setFont(font)

        self.horizontalLayout_26.addWidget(self.label_cycleTime)

        self.lineEdit_cycleTime = QLineEdit(self.page8)
        self.lineEdit_cycleTime.setObjectName(u"lineEdit_cycleTime")
        sizePolicy.setHeightForWidth(self.lineEdit_cycleTime.sizePolicy().hasHeightForWidth())
        self.lineEdit_cycleTime.setSizePolicy(sizePolicy)
        self.lineEdit_cycleTime.setFont(font)

        self.horizontalLayout_26.addWidget(self.lineEdit_cycleTime)

        self.horizontalSpacer_17 = QSpacerItem(90, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_17)


        self.page8Layout.addLayout(self.horizontalLayout_26)

        self.line_5 = QFrame(self.page8)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.Shape.HLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.page8Layout.addWidget(self.line_5)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_autoSaveReading = QLabel(self.page8)
        self.label_autoSaveReading.setObjectName(u"label_autoSaveReading")
        self.label_autoSaveReading.setFont(font)

        self.horizontalLayout_27.addWidget(self.label_autoSaveReading, 0, Qt.AlignmentFlag.AlignLeft)

        self.toggelButton_autoSaveReading = QLabel(self.page8)
        self.toggelButton_autoSaveReading.setObjectName(u"toggelButton_autoSaveReading")
        self.toggelButton_autoSaveReading.setFont(font)

        image_path = os.path.join(script_dir, "Switcher_On.png")  # if it's in the same folder
        self.toggelButton_autoSaveReading.setPixmap(QPixmap(image_path))

        self.horizontalLayout_27.addWidget(self.toggelButton_autoSaveReading)

        self.label_autoSaveReadingOnOff = QLabel(self.page8)
        self.label_autoSaveReadingOnOff.setObjectName(u"label_autoSaveReadingOnOff")
        self.label_autoSaveReadingOnOff.setFont(font)

        self.horizontalLayout_27.addWidget(self.label_autoSaveReadingOnOff)

        self.horizontalSpacer_12 = QSpacerItem(430, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_12)


        self.page8Layout.addLayout(self.horizontalLayout_27)

        self.line_6 = QFrame(self.page8)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.Shape.HLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)

        self.page8Layout.addWidget(self.line_6)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.label_partTraceability = QLabel(self.page8)
        self.label_partTraceability.setObjectName(u"label_partTraceability")
        self.label_partTraceability.setFont(font)

        self.horizontalLayout_28.addWidget(self.label_partTraceability, 0, Qt.AlignmentFlag.AlignLeft)

        self.toggelButton_partTraceability = QLabel(self.page8)
        self.toggelButton_partTraceability.setObjectName(u"toggelButton_partTraceability")

        image_path = os.path.join(script_dir, "Switcher_On.png")  # if it's in the same folder
        self.toggelButton_partTraceability.setPixmap(QPixmap(image_path))

        self.horizontalLayout_28.addWidget(self.toggelButton_partTraceability)

        self.label_partTraceabilityOnOff = QLabel(self.page8)
        self.label_partTraceabilityOnOff.setObjectName(u"label_partTraceabilityOnOff")
        self.label_partTraceabilityOnOff.setFont(font)

        self.horizontalLayout_28.addWidget(self.label_partTraceabilityOnOff, 0, Qt.AlignmentFlag.AlignLeft)

        self.horizontalSpacer_13 = QSpacerItem(140, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_13)

        self.radioButton_manualPartTraceability = QRadioButton(self.page8)
        self.buttonGroup_2 = QButtonGroup(MainWindow)
        self.buttonGroup_2.setObjectName(u"buttonGroup_2")
        self.buttonGroup_2.addButton(self.radioButton_manualPartTraceability)
        self.radioButton_manualPartTraceability.setObjectName(u"radioButton_manualPartTraceability")
        self.radioButton_manualPartTraceability.setFont(font)

        self.horizontalLayout_28.addWidget(self.radioButton_manualPartTraceability)

        self.radioButton_autoPartTraceability = QRadioButton(self.page8)
        self.buttonGroup_2.addButton(self.radioButton_autoPartTraceability)
        self.radioButton_autoPartTraceability.setObjectName(u"radioButton_autoPartTraceability")
        self.radioButton_autoPartTraceability.setFont(font)

        self.horizontalLayout_28.addWidget(self.radioButton_autoPartTraceability)

        self.horizontalSpacer_18 = QSpacerItem(85, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_18)


        self.page8Layout.addLayout(self.horizontalLayout_28)

        self.line_7 = QFrame(self.page8)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.Shape.HLine)
        self.line_7.setFrameShadow(QFrame.Shadow.Sunken)

        self.page8Layout.addWidget(self.line_7)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.label_displayMode = QLabel(self.page8)
        self.label_displayMode.setObjectName(u"label_displayMode")
        self.label_displayMode.setFont(font)

        self.horizontalLayout_29.addWidget(self.label_displayMode)

        self.comboBox_displayMode = QComboBox(self.page8)
        self.comboBox_displayMode.addItem("")
        self.comboBox_displayMode.addItem("")
        self.comboBox_displayMode.addItem("")
        self.comboBox_displayMode.setObjectName(u"comboBox_displayMode")
        self.comboBox_displayMode.setMinimumSize(QSize(150, 0))
        self.comboBox_displayMode.setFont(font)

        self.horizontalLayout_29.addWidget(self.comboBox_displayMode, 0, Qt.AlignmentFlag.AlignLeft)

        self.horizontalSpacer_14 = QSpacerItem(425, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_29.addItem(self.horizontalSpacer_14)


        self.page8Layout.addLayout(self.horizontalLayout_29)

        self.stackedWidget_main.addWidget(self.page8)
        self.page9 = QWidget()
        self.page9.setObjectName(u"page9")
        self.page9Layout = QVBoxLayout(self.page9)
        self.page9Layout.setObjectName(u"page9Layout")
        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer_20 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_20)

        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.label_probeSensitivity = QLabel(self.page9)
        self.label_probeSensitivity.setObjectName(u"label_probeSensitivity")
        self.label_probeSensitivity.setFont(font)

        self.horizontalLayout_32.addWidget(self.label_probeSensitivity)

        self.lineEdit_probeSensitivity = QLineEdit(self.page9)
        self.lineEdit_probeSensitivity.setObjectName(u"lineEdit_probeSensitivity")
        sizePolicy.setHeightForWidth(self.lineEdit_probeSensitivity.sizePolicy().hasHeightForWidth())
        self.lineEdit_probeSensitivity.setSizePolicy(sizePolicy)
        self.lineEdit_probeSensitivity.setMaximumSize(QSize(75, 16777215))
        self.lineEdit_probeSensitivity.setFont(font)

        self.horizontalLayout_32.addWidget(self.lineEdit_probeSensitivity, 0, Qt.AlignmentFlag.AlignLeft)

        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_32.addItem(self.horizontalSpacer_21)


        self.verticalLayout_3.addLayout(self.horizontalLayout_32)

        self.verticalSpacer_24 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_24)

        self.line_11 = QFrame(self.page9)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setFrameShape(QFrame.Shape.HLine)
        self.line_11.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_3.addWidget(self.line_11)

        self.verticalSpacer_21 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_21)

        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.label_timeToMasterSet = QLabel(self.page9)
        self.label_timeToMasterSet.setObjectName(u"label_timeToMasterSet")
        self.label_timeToMasterSet.setFont(font)

        self.horizontalLayout_33.addWidget(self.label_timeToMasterSet)

        self.toggleButtontimeToSetMaster = QLabel(self.page9)
        self.toggleButtontimeToSetMaster.setObjectName(u"toggleButtontimeToSetMaster")

        image_path = os.path.join(script_dir, "Switcher_On.png")  # if it's in the same folder
        self.toggleButtontimeToSetMaster.setPixmap(QPixmap(image_path))

        self.horizontalLayout_33.addWidget(self.toggleButtontimeToSetMaster)

        self.label_28 = QLabel(self.page9)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font)

        self.horizontalLayout_33.addWidget(self.label_28)

        self.horizontalSpacer_22 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_33.addItem(self.horizontalSpacer_22)

        self.lineEdit_timeToMasterSet = QLineEdit(self.page9)
        self.lineEdit_timeToMasterSet.setObjectName(u"lineEdit_timeToMasterSet")
        sizePolicy.setHeightForWidth(self.lineEdit_timeToMasterSet.sizePolicy().hasHeightForWidth())
        self.lineEdit_timeToMasterSet.setSizePolicy(sizePolicy)
        self.lineEdit_timeToMasterSet.setMaximumSize(QSize(75, 16777215))
        self.lineEdit_timeToMasterSet.setFont(font)

        self.horizontalLayout_33.addWidget(self.lineEdit_timeToMasterSet)

        self.label_29 = QLabel(self.page9)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font)

        self.horizontalLayout_33.addWidget(self.label_29)

        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_33.addItem(self.horizontalSpacer_23)


        self.verticalLayout_3.addLayout(self.horizontalLayout_33)

        self.verticalSpacer_25 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_25)

        self.verticalSpacer_22 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_22)

        self.line_12 = QFrame(self.page9)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setFrameShape(QFrame.Shape.HLine)
        self.line_12.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_3.addWidget(self.line_12)

        self.verticalSpacer_27 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_27)

        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.label_masterGrouping = QLabel(self.page9)
        self.label_masterGrouping.setObjectName(u"label_masterGrouping")
        self.label_masterGrouping.setFont(font)

        self.horizontalLayout_34.addWidget(self.label_masterGrouping)

        self.toggleButton_masterGrouping = QLabel(self.page9)
        self.toggleButton_masterGrouping.setObjectName(u"toggleButton_masterGrouping")

        image_path = os.path.join(script_dir, "Switcher_On.png")  # if it's in the same folder
        self.toggleButton_masterGrouping.setPixmap(QPixmap(image_path))

        self.horizontalLayout_34.addWidget(self.toggleButton_masterGrouping)

        self.label_31 = QLabel(self.page9)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font)

        self.horizontalLayout_34.addWidget(self.label_31, 0, Qt.AlignmentFlag.AlignLeft)

        self.horizontalSpacer_19 = QSpacerItem(250, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_34.addItem(self.horizontalSpacer_19)


        self.verticalLayout_3.addLayout(self.horizontalLayout_34)

        self.verticalSpacer_26 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_26)

        self.horizontalLayout_35 = QHBoxLayout()
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalSpacer_20 = QSpacerItem(500, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_35.addItem(self.horizontalSpacer_20)


        self.verticalLayout_3.addLayout(self.horizontalLayout_35)

        self.line_13 = QFrame(self.page9)
        self.line_13.setObjectName(u"line_13")
        self.line_13.setFrameShape(QFrame.Shape.HLine)
        self.line_13.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_3.addWidget(self.line_13)


        self.horizontalLayout_23.addLayout(self.verticalLayout_3)

        self.line_14 = QFrame(self.page9)
        self.line_14.setObjectName(u"line_14")
        self.line_14.setFrameShape(QFrame.Shape.VLine)
        self.line_14.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_23.addWidget(self.line_14)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.button_factoryCalibration = QPushButton(self.page9)
        self.button_factoryCalibration.setObjectName(u"button_factoryCalibration")
        sizePolicy.setHeightForWidth(self.button_factoryCalibration.sizePolicy().hasHeightForWidth())
        self.button_factoryCalibration.setSizePolicy(sizePolicy)
        self.button_factoryCalibration.setMinimumSize(QSize(150, 0))
        self.button_factoryCalibration.setFont(font)

        self.verticalLayout_2.addWidget(self.button_factoryCalibration, 0, Qt.AlignmentFlag.AlignHCenter)

        self.button_touchCalibration = QPushButton(self.page9)
        self.button_touchCalibration.setObjectName(u"button_touchCalibration")
        sizePolicy.setHeightForWidth(self.button_touchCalibration.sizePolicy().hasHeightForWidth())
        self.button_touchCalibration.setSizePolicy(sizePolicy)
        self.button_touchCalibration.setMinimumSize(QSize(150, 0))
        self.button_touchCalibration.setFont(font)

        self.verticalLayout_2.addWidget(self.button_touchCalibration, 0, Qt.AlignmentFlag.AlignHCenter)

        self.button_databaseSettings = QPushButton(self.page9)
        self.button_databaseSettings.setObjectName(u"button_databaseSettings")
        sizePolicy.setHeightForWidth(self.button_databaseSettings.sizePolicy().hasHeightForWidth())
        self.button_databaseSettings.setSizePolicy(sizePolicy)
        self.button_databaseSettings.setMinimumSize(QSize(150, 0))
        self.button_databaseSettings.setFont(font)

        self.verticalLayout_2.addWidget(self.button_databaseSettings, 0, Qt.AlignmentFlag.AlignHCenter)

        self.button_rs232Settings = QPushButton(self.page9)
        self.button_rs232Settings.setObjectName(u"button_rs232Settings")
        sizePolicy.setHeightForWidth(self.button_rs232Settings.sizePolicy().hasHeightForWidth())
        self.button_rs232Settings.setSizePolicy(sizePolicy)
        self.button_rs232Settings.setMinimumSize(QSize(150, 0))
        self.button_rs232Settings.setFont(font)

        self.verticalLayout_2.addWidget(self.button_rs232Settings, 0, Qt.AlignmentFlag.AlignHCenter)

        self.button_factoryConfig = QPushButton(self.page9)
        self.button_factoryConfig.setObjectName(u"button_factoryConfig")
        sizePolicy.setHeightForWidth(self.button_factoryConfig.sizePolicy().hasHeightForWidth())
        self.button_factoryConfig.setSizePolicy(sizePolicy)
        self.button_factoryConfig.setMinimumSize(QSize(150, 0))
        self.button_factoryConfig.setFont(font)

        self.verticalLayout_2.addWidget(self.button_factoryConfig, 0, Qt.AlignmentFlag.AlignHCenter)

        self.button_airSaving = QPushButton(self.page9)
        self.button_airSaving.setObjectName(u"button_airSaving")
        sizePolicy.setHeightForWidth(self.button_airSaving.sizePolicy().hasHeightForWidth())
        self.button_airSaving.setSizePolicy(sizePolicy)
        self.button_airSaving.setMinimumSize(QSize(150, 0))
        self.button_airSaving.setFont(font)

        self.verticalLayout_2.addWidget(self.button_airSaving, 0, Qt.AlignmentFlag.AlignHCenter)

        self.button_ipSettings = QPushButton(self.page9)
        self.button_ipSettings.setObjectName(u"button_ipSettings")
        self.button_ipSettings.setFont(font)

        self.verticalLayout_2.addWidget(self.button_ipSettings)

        self.button_wifiSettings = QPushButton(self.page9)
        self.button_wifiSettings.setObjectName(u"button_wifiSettings")
        self.button_wifiSettings.setFont(font)

        self.verticalLayout_2.addWidget(self.button_wifiSettings)


        self.horizontalLayout_23.addLayout(self.verticalLayout_2)


        self.page9Layout.addLayout(self.horizontalLayout_23)

        self.stackedWidget_main.addWidget(self.page9)
        self.page10 = QWidget()
        self.page10.setObjectName(u"page10")
        self.page10Layout = QVBoxLayout(self.page10)
        self.page10Layout.setObjectName(u"page10Layout")
        self.horizontalLayout_44 = QHBoxLayout()
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.label_productHelp = QLabel(self.page10)
        self.label_productHelp.setObjectName(u"label_productHelp")
        font5 = QFont()
        font5.setPointSize(12)
        font5.setBold(True)
        self.label_productHelp.setFont(font5)

        self.horizontalLayout_44.addWidget(self.label_productHelp, 0, Qt.AlignmentFlag.AlignHCenter)


        self.page10Layout.addLayout(self.horizontalLayout_44)

        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.label_intersenseNameHelp = QLabel(self.page10)
        self.label_intersenseNameHelp.setObjectName(u"label_intersenseNameHelp")
        self.label_intersenseNameHelp.setFont(font5)

        self.horizontalLayout_31.addWidget(self.label_intersenseNameHelp, 0, Qt.AlignmentFlag.AlignHCenter)


        self.page10Layout.addLayout(self.horizontalLayout_31)

        self.horizontalLayout_37 = QHBoxLayout()
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.label_adressHelp = QLabel(self.page10)
        self.label_adressHelp.setObjectName(u"label_adressHelp")
        self.label_adressHelp.setFont(font5)

        self.horizontalLayout_37.addWidget(self.label_adressHelp, 0, Qt.AlignmentFlag.AlignHCenter)


        self.page10Layout.addLayout(self.horizontalLayout_37)

        self.horizontalLayout_38 = QHBoxLayout()
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.label_adressHelp_2 = QLabel(self.page10)
        self.label_adressHelp_2.setObjectName(u"label_adressHelp_2")
        self.label_adressHelp_2.setFont(font5)

        self.horizontalLayout_38.addWidget(self.label_adressHelp_2, 0, Qt.AlignmentFlag.AlignHCenter)


        self.page10Layout.addLayout(self.horizontalLayout_38)

        self.horizontalLayout_39 = QHBoxLayout()
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.label_emailHelp = QLabel(self.page10)
        self.label_emailHelp.setObjectName(u"label_emailHelp")
        self.label_emailHelp.setFont(font5)

        self.horizontalLayout_39.addWidget(self.label_emailHelp, 0, Qt.AlignmentFlag.AlignHCenter)


        self.page10Layout.addLayout(self.horizontalLayout_39)

        self.horizontalLayout_40 = QHBoxLayout()
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.label_supportHelp = QLabel(self.page10)
        self.label_supportHelp.setObjectName(u"label_supportHelp")
        self.label_supportHelp.setFont(font5)

        self.horizontalLayout_40.addWidget(self.label_supportHelp, 0, Qt.AlignmentFlag.AlignHCenter)


        self.page10Layout.addLayout(self.horizontalLayout_40)

        self.verticalSpacer_19 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.page10Layout.addItem(self.verticalSpacer_19)

        self.horizontalLayout_41 = QHBoxLayout()
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.label_modelNumberHelp = QLabel(self.page10)
        self.label_modelNumberHelp.setObjectName(u"label_modelNumberHelp")
        self.label_modelNumberHelp.setFont(font5)

        self.horizontalLayout_41.addWidget(self.label_modelNumberHelp, 0, Qt.AlignmentFlag.AlignHCenter)


        self.page10Layout.addLayout(self.horizontalLayout_41)

        self.horizontalLayout_42 = QHBoxLayout()
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.label_serialNoHelp = QLabel(self.page10)
        self.label_serialNoHelp.setObjectName(u"label_serialNoHelp")
        self.label_serialNoHelp.setFont(font5)

        self.horizontalLayout_42.addWidget(self.label_serialNoHelp, 0, Qt.AlignmentFlag.AlignHCenter)


        self.page10Layout.addLayout(self.horizontalLayout_42)

        self.horizontalLayout_43 = QHBoxLayout()
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.label_softwareVersionHelp = QLabel(self.page10)
        self.label_softwareVersionHelp.setObjectName(u"label_softwareVersionHelp")
        self.label_softwareVersionHelp.setFont(font5)

        self.horizontalLayout_43.addWidget(self.label_softwareVersionHelp, 0, Qt.AlignmentFlag.AlignHCenter)


        self.page10Layout.addLayout(self.horizontalLayout_43)

        self.stackedWidget_main.addWidget(self.page10)
        self.page11 = QWidget()
        self.page11.setObjectName(u"page11")
        self.page11Layout = QVBoxLayout(self.page11)
        self.page11Layout.setObjectName(u"page11Layout")
        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.page11Layout.addItem(self.verticalSpacer_8)

        self.horizontalLayout_45 = QHBoxLayout()
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.horizontalSpacer_152 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_45.addItem(self.horizontalSpacer_152)

        self.label_setDate = QLabel(self.page11)
        self.label_setDate.setObjectName(u"label_setDate")
        self.label_setDate.setFont(font)

        self.horizontalLayout_45.addWidget(self.label_setDate, 0, Qt.AlignmentFlag.AlignRight)

        self.lineEdit_day = QLineEdit(self.page11)
        self.lineEdit_day.setObjectName(u"lineEdit_day")
        sizePolicy.setHeightForWidth(self.lineEdit_day.sizePolicy().hasHeightForWidth())
        self.lineEdit_day.setSizePolicy(sizePolicy)
        self.lineEdit_day.setMinimumSize(QSize(70, 25))
        self.lineEdit_day.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_day.setFont(font)

        self.horizontalLayout_45.addWidget(self.lineEdit_day, 0, Qt.AlignmentFlag.AlignLeft)

        self.label_day = QLabel(self.page11)
        self.label_day.setObjectName(u"label_day")
        self.label_day.setFont(font)

        self.horizontalLayout_45.addWidget(self.label_day, 0, Qt.AlignmentFlag.AlignLeft)

        self.horizontalSpacer_160 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_45.addItem(self.horizontalSpacer_160)

        self.lineEdit_month = QLineEdit(self.page11)
        self.lineEdit_month.setObjectName(u"lineEdit_month")
        sizePolicy.setHeightForWidth(self.lineEdit_month.sizePolicy().hasHeightForWidth())
        self.lineEdit_month.setSizePolicy(sizePolicy)
        self.lineEdit_month.setMinimumSize(QSize(70, 25))
        self.lineEdit_month.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_month.setFont(font)

        self.horizontalLayout_45.addWidget(self.lineEdit_month, 0, Qt.AlignmentFlag.AlignLeft)

        self.label_month = QLabel(self.page11)
        self.label_month.setObjectName(u"label_month")
        self.label_month.setFont(font)

        self.horizontalLayout_45.addWidget(self.label_month, 0, Qt.AlignmentFlag.AlignLeft)

        self.horizontalSpacer_161 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_45.addItem(self.horizontalSpacer_161)

        self.lineEdit_year = QLineEdit(self.page11)
        self.lineEdit_year.setObjectName(u"lineEdit_year")
        sizePolicy.setHeightForWidth(self.lineEdit_year.sizePolicy().hasHeightForWidth())
        self.lineEdit_year.setSizePolicy(sizePolicy)
        self.lineEdit_year.setMinimumSize(QSize(70, 25))
        self.lineEdit_year.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_year.setFont(font)

        self.horizontalLayout_45.addWidget(self.lineEdit_year, 0, Qt.AlignmentFlag.AlignLeft)

        self.label_year = QLabel(self.page11)
        self.label_year.setObjectName(u"label_year")
        self.label_year.setFont(font)

        self.horizontalLayout_45.addWidget(self.label_year, 0, Qt.AlignmentFlag.AlignLeft)

        self.horizontalSpacer_159 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_45.addItem(self.horizontalSpacer_159)


        self.page11Layout.addLayout(self.horizontalLayout_45)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.page11Layout.addItem(self.verticalSpacer_9)

        self.horizontalLayout_46 = QHBoxLayout()
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.horizontalSpacer_149 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_46.addItem(self.horizontalSpacer_149)

        self.label_setTime = QLabel(self.page11)
        self.label_setTime.setObjectName(u"label_setTime")
        self.label_setTime.setFont(font)

        self.horizontalLayout_46.addWidget(self.label_setTime, 0, Qt.AlignmentFlag.AlignRight)

        self.lineEdit_hours = QLineEdit(self.page11)
        self.lineEdit_hours.setObjectName(u"lineEdit_hours")
        sizePolicy.setHeightForWidth(self.lineEdit_hours.sizePolicy().hasHeightForWidth())
        self.lineEdit_hours.setSizePolicy(sizePolicy)
        self.lineEdit_hours.setMinimumSize(QSize(70, 25))
        self.lineEdit_hours.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_hours.setFont(font)

        self.horizontalLayout_46.addWidget(self.lineEdit_hours, 0, Qt.AlignmentFlag.AlignLeft)

        self.label_hours = QLabel(self.page11)
        self.label_hours.setObjectName(u"label_hours")
        self.label_hours.setFont(font)

        self.horizontalLayout_46.addWidget(self.label_hours, 0, Qt.AlignmentFlag.AlignLeft)

        self.horizontalSpacer_167 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_46.addItem(self.horizontalSpacer_167)

        self.lineEdit_minutes = QLineEdit(self.page11)
        self.lineEdit_minutes.setObjectName(u"lineEdit_minutes")
        sizePolicy.setHeightForWidth(self.lineEdit_minutes.sizePolicy().hasHeightForWidth())
        self.lineEdit_minutes.setSizePolicy(sizePolicy)
        self.lineEdit_minutes.setMinimumSize(QSize(70, 25))
        self.lineEdit_minutes.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_minutes.setFont(font)

        self.horizontalLayout_46.addWidget(self.lineEdit_minutes, 0, Qt.AlignmentFlag.AlignLeft)

        self.label_minutes = QLabel(self.page11)
        self.label_minutes.setObjectName(u"label_minutes")
        self.label_minutes.setFont(font)

        self.horizontalLayout_46.addWidget(self.label_minutes, 0, Qt.AlignmentFlag.AlignLeft)

        self.horizontalSpacer_162 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_46.addItem(self.horizontalSpacer_162)


        self.page11Layout.addLayout(self.horizontalLayout_46)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.page11Layout.addItem(self.verticalSpacer_10)

        self.horizontalLayout_96 = QHBoxLayout()
        self.horizontalLayout_96.setObjectName(u"horizontalLayout_96")
        self.pushButton_setDateTime = QPushButton(self.page11)
        self.pushButton_setDateTime.setObjectName(u"pushButton_setDateTime")
        sizePolicy.setHeightForWidth(self.pushButton_setDateTime.sizePolicy().hasHeightForWidth())
        self.pushButton_setDateTime.setSizePolicy(sizePolicy)
        self.pushButton_setDateTime.setFont(font)

        self.horizontalLayout_96.addWidget(self.pushButton_setDateTime, 0, Qt.AlignmentFlag.AlignHCenter)


        self.page11Layout.addLayout(self.horizontalLayout_96)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.page11Layout.addItem(self.verticalSpacer_7)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.line_45 = QFrame(self.page11)
        self.line_45.setObjectName(u"line_45")
        self.line_45.setFrameShape(QFrame.Shape.VLine)
        self.line_45.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_45, 1, 4, 1, 1)

        self.line_53 = QFrame(self.page11)
        self.line_53.setObjectName(u"line_53")
        self.line_53.setFrameShape(QFrame.Shape.VLine)
        self.line_53.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_53, 4, 9, 1, 1)

        self.line_55 = QFrame(self.page11)
        self.line_55.setObjectName(u"line_55")
        self.line_55.setFrameShape(QFrame.Shape.VLine)
        self.line_55.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_55, 0, 9, 1, 1)

        self.line_32 = QFrame(self.page11)
        self.line_32.setObjectName(u"line_32")
        self.line_32.setFrameShape(QFrame.Shape.HLine)
        self.line_32.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_32, 1, 6, 1, 1)

        self.line_42 = QFrame(self.page11)
        self.line_42.setObjectName(u"line_42")
        self.line_42.setFrameShape(QFrame.Shape.VLine)
        self.line_42.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_42, 5, 4, 1, 1)

        self.horizontalLayout_103 = QHBoxLayout()
        self.horizontalLayout_103.setObjectName(u"horizontalLayout_103")
        self.horizontalSpacer_65 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_103.addItem(self.horizontalSpacer_65)

        self.lineEdit_shift3FromTime = QLineEdit(self.page11)
        self.lineEdit_shift3FromTime.setObjectName(u"lineEdit_shift3FromTime")
        sizePolicy.setHeightForWidth(self.lineEdit_shift3FromTime.sizePolicy().hasHeightForWidth())
        self.lineEdit_shift3FromTime.setSizePolicy(sizePolicy)
        self.lineEdit_shift3FromTime.setMinimumSize(QSize(90, 0))
        self.lineEdit_shift3FromTime.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_shift3FromTime.setFont(font)

        self.horizontalLayout_103.addWidget(self.lineEdit_shift3FromTime)

        self.comboBox_shift3FromTimeAmPm = QComboBox(self.page11)
        self.comboBox_shift3FromTimeAmPm.addItem("")
        self.comboBox_shift3FromTimeAmPm.addItem("")
        self.comboBox_shift3FromTimeAmPm.setObjectName(u"comboBox_shift3FromTimeAmPm")
        self.comboBox_shift3FromTimeAmPm.setMaximumSize(QSize(16777215, 16777215))
        self.comboBox_shift3FromTimeAmPm.setFont(font)

        self.horizontalLayout_103.addWidget(self.comboBox_shift3FromTimeAmPm)

        self.horizontalSpacer_69 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_103.addItem(self.horizontalSpacer_69)


        self.gridLayout.addLayout(self.horizontalLayout_103, 5, 5, 1, 1)

        self.line_28 = QFrame(self.page11)
        self.line_28.setObjectName(u"line_28")
        self.line_28.setFrameShape(QFrame.Shape.HLine)
        self.line_28.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_28, 1, 1, 1, 1)

        self.horizontalLayout_102 = QHBoxLayout()
        self.horizontalLayout_102.setObjectName(u"horizontalLayout_102")
        self.horizontalSpacer_64 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_102.addItem(self.horizontalSpacer_64)

        self.lineEdit_shift2FromTime = QLineEdit(self.page11)
        self.lineEdit_shift2FromTime.setObjectName(u"lineEdit_shift2FromTime")
        sizePolicy.setHeightForWidth(self.lineEdit_shift2FromTime.sizePolicy().hasHeightForWidth())
        self.lineEdit_shift2FromTime.setSizePolicy(sizePolicy)
        self.lineEdit_shift2FromTime.setMinimumSize(QSize(90, 0))
        self.lineEdit_shift2FromTime.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_shift2FromTime.setFont(font)

        self.horizontalLayout_102.addWidget(self.lineEdit_shift2FromTime)

        self.comboBox_shift2FromTimeAmPm = QComboBox(self.page11)
        self.comboBox_shift2FromTimeAmPm.addItem("")
        self.comboBox_shift2FromTimeAmPm.addItem("")
        self.comboBox_shift2FromTimeAmPm.setObjectName(u"comboBox_shift2FromTimeAmPm")
        self.comboBox_shift2FromTimeAmPm.setMaximumSize(QSize(16777215, 16777215))
        self.comboBox_shift2FromTimeAmPm.setFont(font)

        self.horizontalLayout_102.addWidget(self.comboBox_shift2FromTimeAmPm)

        self.horizontalSpacer_68 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_102.addItem(self.horizontalSpacer_68)


        self.gridLayout.addLayout(self.horizontalLayout_102, 4, 5, 1, 1)

        self.line_31 = QFrame(self.page11)
        self.line_31.setObjectName(u"line_31")
        self.line_31.setFrameShape(QFrame.Shape.HLine)
        self.line_31.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_31, 1, 5, 1, 1)

        self.line_52 = QFrame(self.page11)
        self.line_52.setObjectName(u"line_52")
        self.line_52.setFrameShape(QFrame.Shape.VLine)
        self.line_52.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_52, 3, 9, 1, 1)

        self.horizontalSpacer_60 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_60, 3, 1, 1, 1)

        self.line_56 = QFrame(self.page11)
        self.line_56.setObjectName(u"line_56")
        self.line_56.setFrameShape(QFrame.Shape.VLine)
        self.line_56.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_56, 2, 9, 1, 1)

        self.line_34 = QFrame(self.page11)
        self.line_34.setObjectName(u"line_34")
        self.line_34.setFrameShape(QFrame.Shape.HLine)
        self.line_34.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_34, 1, 9, 1, 1)

        self.line_46 = QFrame(self.page11)
        self.line_46.setObjectName(u"line_46")
        self.line_46.setFrameShape(QFrame.Shape.VLine)
        self.line_46.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_46, 1, 7, 1, 1)

        self.line_44 = QFrame(self.page11)
        self.line_44.setObjectName(u"line_44")
        self.line_44.setFrameShape(QFrame.Shape.HLine)
        self.line_44.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_44, 1, 3, 1, 1)

        self.horizontalLayout_99 = QHBoxLayout()
        self.horizontalLayout_99.setObjectName(u"horizontalLayout_99")
        self.horizontalSpacer_54 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_99.addItem(self.horizontalSpacer_54)

        self.label_shift2 = QLabel(self.page11)
        self.label_shift2.setObjectName(u"label_shift2")
        self.label_shift2.setFont(font)

        self.horizontalLayout_99.addWidget(self.label_shift2)

        self.checkBox_shift2 = QCheckBox(self.page11)
        self.checkBox_shift2.setObjectName(u"checkBox_shift2")
        self.checkBox_shift2.setMaximumSize(QSize(16777215, 16777215))
        self.checkBox_shift2.setFont(font)

        self.horizontalLayout_99.addWidget(self.checkBox_shift2)

        self.horizontalSpacer_55 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_99.addItem(self.horizontalSpacer_55)


        self.gridLayout.addLayout(self.horizontalLayout_99, 4, 2, 1, 1)

        self.horizontalSpacer_61 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_61, 3, 3, 1, 1)

        self.horizontalLayout_100 = QHBoxLayout()
        self.horizontalLayout_100.setObjectName(u"horizontalLayout_100")
        self.horizontalSpacer_56 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_100.addItem(self.horizontalSpacer_56)

        self.label_shift3 = QLabel(self.page11)
        self.label_shift3.setObjectName(u"label_shift3")
        self.label_shift3.setFont(font)

        self.horizontalLayout_100.addWidget(self.label_shift3)

        self.checkBox_shift3 = QCheckBox(self.page11)
        self.checkBox_shift3.setObjectName(u"checkBox_shift3")
        self.checkBox_shift3.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_100.addWidget(self.checkBox_shift3)

        self.line_27 = QFrame(self.page11)
        self.line_27.setObjectName(u"line_27")
        self.line_27.setFrameShape(QFrame.Shape.HLine)
        self.line_27.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_100.addWidget(self.line_27)

        self.horizontalSpacer_57 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_100.addItem(self.horizontalSpacer_57)


        self.gridLayout.addLayout(self.horizontalLayout_100, 5, 2, 1, 1)

        self.horizontalLayout_107 = QHBoxLayout()
        self.horizontalLayout_107.setObjectName(u"horizontalLayout_107")
        self.horizontalSpacer_67 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_107.addItem(self.horizontalSpacer_67)

        self.lineEdit_shift2ToTime_2 = QLineEdit(self.page11)
        self.lineEdit_shift2ToTime_2.setObjectName(u"lineEdit_shift2ToTime_2")
        sizePolicy.setHeightForWidth(self.lineEdit_shift2ToTime_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_shift2ToTime_2.setSizePolicy(sizePolicy)
        self.lineEdit_shift2ToTime_2.setMinimumSize(QSize(90, 0))
        self.lineEdit_shift2ToTime_2.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_shift2ToTime_2.setFont(font)

        self.horizontalLayout_107.addWidget(self.lineEdit_shift2ToTime_2)

        self.comboBox_shift3ToTimeAmPm = QComboBox(self.page11)
        self.comboBox_shift3ToTimeAmPm.addItem("")
        self.comboBox_shift3ToTimeAmPm.addItem("")
        self.comboBox_shift3ToTimeAmPm.setObjectName(u"comboBox_shift3ToTimeAmPm")
        self.comboBox_shift3ToTimeAmPm.setMaximumSize(QSize(16777215, 16777215))
        self.comboBox_shift3ToTimeAmPm.setFont(font)

        self.horizontalLayout_107.addWidget(self.comboBox_shift3ToTimeAmPm)

        self.horizontalSpacer_71 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_107.addItem(self.horizontalSpacer_71)


        self.gridLayout.addLayout(self.horizontalLayout_107, 5, 8, 1, 1)

        self.horizontalLayout_97 = QHBoxLayout()
        self.horizontalLayout_97.setObjectName(u"horizontalLayout_97")
        self.horizontalSpacer_62 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_97.addItem(self.horizontalSpacer_62)

        self.lineEdit_shift1FromTime = QLineEdit(self.page11)
        self.lineEdit_shift1FromTime.setObjectName(u"lineEdit_shift1FromTime")
        sizePolicy.setHeightForWidth(self.lineEdit_shift1FromTime.sizePolicy().hasHeightForWidth())
        self.lineEdit_shift1FromTime.setSizePolicy(sizePolicy)
        self.lineEdit_shift1FromTime.setMinimumSize(QSize(90, 0))
        self.lineEdit_shift1FromTime.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_shift1FromTime.setFont(font)

        self.horizontalLayout_97.addWidget(self.lineEdit_shift1FromTime)

        self.comboBox_shift1FromTimeAmPm = QComboBox(self.page11)
        self.comboBox_shift1FromTimeAmPm.addItem("")
        self.comboBox_shift1FromTimeAmPm.addItem("")
        self.comboBox_shift1FromTimeAmPm.setObjectName(u"comboBox_shift1FromTimeAmPm")
        self.comboBox_shift1FromTimeAmPm.setMaximumSize(QSize(16777215, 16777215))
        self.comboBox_shift1FromTimeAmPm.setFont(font)

        self.horizontalLayout_97.addWidget(self.comboBox_shift1FromTimeAmPm)

        self.horizontalSpacer_59 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_97.addItem(self.horizontalSpacer_59)


        self.gridLayout.addLayout(self.horizontalLayout_97, 3, 5, 1, 1)

        self.line_38 = QFrame(self.page11)
        self.line_38.setObjectName(u"line_38")
        self.line_38.setFrameShape(QFrame.Shape.VLine)
        self.line_38.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_38, 5, 0, 1, 1)

        self.line_40 = QFrame(self.page11)
        self.line_40.setObjectName(u"line_40")
        self.line_40.setFrameShape(QFrame.Shape.VLine)
        self.line_40.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_40, 1, 0, 1, 1)

        self.line_54 = QFrame(self.page11)
        self.line_54.setObjectName(u"line_54")
        self.line_54.setFrameShape(QFrame.Shape.VLine)
        self.line_54.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_54, 5, 9, 1, 1)

        self.line_50 = QFrame(self.page11)
        self.line_50.setObjectName(u"line_50")
        self.line_50.setFrameShape(QFrame.Shape.VLine)
        self.line_50.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_50, 0, 7, 1, 1)

        self.line_29 = QFrame(self.page11)
        self.line_29.setObjectName(u"line_29")
        self.line_29.setFrameShape(QFrame.Shape.HLine)
        self.line_29.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_29, 1, 2, 1, 1)

        self.horizontalLayout_106 = QHBoxLayout()
        self.horizontalLayout_106.setObjectName(u"horizontalLayout_106")
        self.horizontalSpacer_66 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_106.addItem(self.horizontalSpacer_66)

        self.lineEdit_shift2ToTime = QLineEdit(self.page11)
        self.lineEdit_shift2ToTime.setObjectName(u"lineEdit_shift2ToTime")
        sizePolicy.setHeightForWidth(self.lineEdit_shift2ToTime.sizePolicy().hasHeightForWidth())
        self.lineEdit_shift2ToTime.setSizePolicy(sizePolicy)
        self.lineEdit_shift2ToTime.setMinimumSize(QSize(90, 0))
        self.lineEdit_shift2ToTime.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_shift2ToTime.setFont(font)

        self.horizontalLayout_106.addWidget(self.lineEdit_shift2ToTime)

        self.comboBox_shift2ToTimeAmPm = QComboBox(self.page11)
        self.comboBox_shift2ToTimeAmPm.addItem("")
        self.comboBox_shift2ToTimeAmPm.addItem("")
        self.comboBox_shift2ToTimeAmPm.setObjectName(u"comboBox_shift2ToTimeAmPm")
        self.comboBox_shift2ToTimeAmPm.setMaximumSize(QSize(16777215, 16777215))
        self.comboBox_shift2ToTimeAmPm.setFont(font)

        self.horizontalLayout_106.addWidget(self.comboBox_shift2ToTimeAmPm)

        self.horizontalSpacer_70 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_106.addItem(self.horizontalSpacer_70)


        self.gridLayout.addLayout(self.horizontalLayout_106, 4, 8, 1, 1)

        self.line_47 = QFrame(self.page11)
        self.line_47.setObjectName(u"line_47")
        self.line_47.setFrameShape(QFrame.Shape.VLine)
        self.line_47.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_47, 3, 7, 1, 1)

        self.line_37 = QFrame(self.page11)
        self.line_37.setObjectName(u"line_37")
        self.line_37.setFrameShape(QFrame.Shape.VLine)
        self.line_37.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_37, 4, 0, 1, 1)

        self.label_shiftTo = QLabel(self.page11)
        self.label_shiftTo.setObjectName(u"label_shiftTo")
        self.label_shiftTo.setFont(font)

        self.gridLayout.addWidget(self.label_shiftTo, 0, 8, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.line_33 = QFrame(self.page11)
        self.line_33.setObjectName(u"line_33")
        self.line_33.setFrameShape(QFrame.Shape.HLine)
        self.line_33.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_33, 1, 8, 1, 1)

        self.line_43 = QFrame(self.page11)
        self.line_43.setObjectName(u"line_43")
        self.line_43.setFrameShape(QFrame.Shape.VLine)
        self.line_43.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_43, 0, 4, 1, 1)

        self.horizontalLayout_105 = QHBoxLayout()
        self.horizontalLayout_105.setObjectName(u"horizontalLayout_105")
        self.horizontalSpacer_63 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_105.addItem(self.horizontalSpacer_63)

        self.lineEdit_3_toShit1Time = QLineEdit(self.page11)
        self.lineEdit_3_toShit1Time.setObjectName(u"lineEdit_3_toShit1Time")
        sizePolicy.setHeightForWidth(self.lineEdit_3_toShit1Time.sizePolicy().hasHeightForWidth())
        self.lineEdit_3_toShit1Time.setSizePolicy(sizePolicy)
        self.lineEdit_3_toShit1Time.setMinimumSize(QSize(90, 0))
        self.lineEdit_3_toShit1Time.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_3_toShit1Time.setFont(font)

        self.horizontalLayout_105.addWidget(self.lineEdit_3_toShit1Time)

        self.comboBox_shift1ToTimeAmPm = QComboBox(self.page11)
        self.comboBox_shift1ToTimeAmPm.addItem("")
        self.comboBox_shift1ToTimeAmPm.addItem("")
        self.comboBox_shift1ToTimeAmPm.setObjectName(u"comboBox_shift1ToTimeAmPm")
        self.comboBox_shift1ToTimeAmPm.setMaximumSize(QSize(16777215, 16777215))
        self.comboBox_shift1ToTimeAmPm.setFont(font)

        self.horizontalLayout_105.addWidget(self.comboBox_shift1ToTimeAmPm)

        self.horizontalSpacer_58 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_105.addItem(self.horizontalSpacer_58)


        self.gridLayout.addLayout(self.horizontalLayout_105, 3, 8, 1, 1)

        self.line_49 = QFrame(self.page11)
        self.line_49.setObjectName(u"line_49")
        self.line_49.setFrameShape(QFrame.Shape.VLine)
        self.line_49.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_49, 5, 7, 1, 1)

        self.horizontalLayout_98 = QHBoxLayout()
        self.horizontalLayout_98.setObjectName(u"horizontalLayout_98")
        self.horizontalSpacer_52 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_98.addItem(self.horizontalSpacer_52)

        self.label_shift1 = QLabel(self.page11)
        self.label_shift1.setObjectName(u"label_shift1")
        self.label_shift1.setFont(font)

        self.horizontalLayout_98.addWidget(self.label_shift1)

        self.checkBox_shift1 = QCheckBox(self.page11)
        self.checkBox_shift1.setObjectName(u"checkBox_shift1")
        sizePolicy.setHeightForWidth(self.checkBox_shift1.sizePolicy().hasHeightForWidth())
        self.checkBox_shift1.setSizePolicy(sizePolicy)
        self.checkBox_shift1.setMinimumSize(QSize(0, 0))
        self.checkBox_shift1.setMaximumSize(QSize(16777215, 16777215))
        self.checkBox_shift1.setFont(font)

        self.horizontalLayout_98.addWidget(self.checkBox_shift1)

        self.horizontalSpacer_53 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_98.addItem(self.horizontalSpacer_53)


        self.gridLayout.addLayout(self.horizontalLayout_98, 3, 2, 1, 1)

        self.line_36 = QFrame(self.page11)
        self.line_36.setObjectName(u"line_36")
        self.line_36.setFrameShape(QFrame.Shape.VLine)
        self.line_36.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_36, 3, 0, 1, 1)

        self.line_41 = QFrame(self.page11)
        self.line_41.setObjectName(u"line_41")
        self.line_41.setFrameShape(QFrame.Shape.VLine)
        self.line_41.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_41, 4, 4, 1, 1)

        self.line_39 = QFrame(self.page11)
        self.line_39.setObjectName(u"line_39")
        self.line_39.setFrameShape(QFrame.Shape.VLine)
        self.line_39.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_39, 0, 0, 1, 1)

        self.line_30 = QFrame(self.page11)
        self.line_30.setObjectName(u"line_30")
        self.line_30.setFrameShape(QFrame.Shape.VLine)
        self.line_30.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_30, 3, 4, 1, 1)

        self.label_shiftFrom = QLabel(self.page11)
        self.label_shiftFrom.setObjectName(u"label_shiftFrom")
        self.label_shiftFrom.setFont(font)

        self.gridLayout.addWidget(self.label_shiftFrom, 0, 5, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.label_shiftSettings = QLabel(self.page11)
        self.label_shiftSettings.setObjectName(u"label_shiftSettings")
        self.label_shiftSettings.setFont(font)

        self.gridLayout.addWidget(self.label_shiftSettings, 0, 2, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.line_48 = QFrame(self.page11)
        self.line_48.setObjectName(u"line_48")
        self.line_48.setFrameShape(QFrame.Shape.VLine)
        self.line_48.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_48, 4, 7, 1, 1)


        self.page11Layout.addLayout(self.gridLayout)

        self.line_15 = QFrame(self.page11)
        self.line_15.setObjectName(u"line_15")
        self.line_15.setFrameShape(QFrame.Shape.HLine)
        self.line_15.setFrameShadow(QFrame.Shadow.Sunken)

        self.page11Layout.addWidget(self.line_15)

        self.horizontalLayout_110 = QHBoxLayout()
        self.horizontalLayout_110.setObjectName(u"horizontalLayout_110")
        self.pushButton_setShiftTiminggs = QPushButton(self.page11)
        self.pushButton_setShiftTiminggs.setObjectName(u"pushButton_setShiftTiminggs")
        self.pushButton_setShiftTiminggs.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_setShiftTiminggs.setFont(font)

        self.horizontalLayout_110.addWidget(self.pushButton_setShiftTiminggs, 0, Qt.AlignmentFlag.AlignHCenter)


        self.page11Layout.addLayout(self.horizontalLayout_110)

        self.stackedWidget_main.addWidget(self.page11)
        self.page12 = QWidget()
        self.page12.setObjectName(u"page12")
        self.page12Layout = QVBoxLayout(self.page12)
        self.page12Layout.setObjectName(u"page12Layout")
        self.horizontalLayout_47 = QHBoxLayout()
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.button_addMeasurementSettings = QPushButton(self.page12)
        self.button_addMeasurementSettings.setObjectName(u"button_addMeasurementSettings")
        sizePolicy.setHeightForWidth(self.button_addMeasurementSettings.sizePolicy().hasHeightForWidth())
        self.button_addMeasurementSettings.setSizePolicy(sizePolicy)
        self.button_addMeasurementSettings.setFont(font)

        self.horizontalLayout_47.addWidget(self.button_addMeasurementSettings, 0, Qt.AlignmentFlag.AlignHCenter)

        self.button_modifyMeasurementSettings = QPushButton(self.page12)
        self.button_modifyMeasurementSettings.setObjectName(u"button_modifyMeasurementSettings")
        sizePolicy.setHeightForWidth(self.button_modifyMeasurementSettings.sizePolicy().hasHeightForWidth())
        self.button_modifyMeasurementSettings.setSizePolicy(sizePolicy)
        self.button_modifyMeasurementSettings.setFont(font)

        self.horizontalLayout_47.addWidget(self.button_modifyMeasurementSettings, 0, Qt.AlignmentFlag.AlignHCenter)

        self.button_deleteMeasurementSettings = QPushButton(self.page12)
        self.button_deleteMeasurementSettings.setObjectName(u"button_deleteMeasurementSettings")
        sizePolicy.setHeightForWidth(self.button_deleteMeasurementSettings.sizePolicy().hasHeightForWidth())
        self.button_deleteMeasurementSettings.setSizePolicy(sizePolicy)
        self.button_deleteMeasurementSettings.setFont(font)

        self.horizontalLayout_47.addWidget(self.button_deleteMeasurementSettings, 0, Qt.AlignmentFlag.AlignHCenter)


        self.page12Layout.addLayout(self.horizontalLayout_47)

        self.line_16 = QFrame(self.page12)
        self.line_16.setObjectName(u"line_16")
        self.line_16.setFrameShape(QFrame.Shape.HLine)
        self.line_16.setFrameShadow(QFrame.Shadow.Sunken)

        self.page12Layout.addWidget(self.line_16)

        self.horizontalLayout_48 = QHBoxLayout()
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.label_activePartName = QLabel(self.page12)
        self.label_activePartName.setObjectName(u"label_activePartName")
        self.label_activePartName.setFont(font)

        self.horizontalLayout_48.addWidget(self.label_activePartName, 0, Qt.AlignmentFlag.AlignRight)

        self.comboBox_activeParName = QComboBox(self.page12)
        self.comboBox_activeParName.setObjectName(u"comboBox_activeParName")
        self.comboBox_activeParName.setMinimumSize(QSize(200, 0))
        self.comboBox_activeParName.setMaximumSize(QSize(1000, 16777215))
        self.comboBox_activeParName.setFont(font)

        self.horizontalLayout_48.addWidget(self.comboBox_activeParName, 0, Qt.AlignmentFlag.AlignLeft)


        self.page12Layout.addLayout(self.horizontalLayout_48)

        self.line_17 = QFrame(self.page12)
        self.line_17.setObjectName(u"line_17")
        self.line_17.setFrameShape(QFrame.Shape.HLine)
        self.line_17.setFrameShadow(QFrame.Shadow.Sunken)

        self.page12Layout.addWidget(self.line_17)

        self.tableWidget_measurementList = QTableWidget(self.page12)
        self.tableWidget_measurementList.setObjectName(u"tableWidget_measurementList")
        self.tableWidget_measurementList.setFont(font)

        self.page12Layout.addWidget(self.tableWidget_measurementList)

        self.stackedWidget_main.addWidget(self.page12)
        self.page13 = QWidget()
        self.page13.setObjectName(u"page13")
        self.page13Layout = QVBoxLayout(self.page13)
        self.page13Layout.setObjectName(u"page13Layout")
        self.horizontalLayout_49 = QHBoxLayout()
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.button_addCncSettings = QPushButton(self.page13)
        self.button_addCncSettings.setObjectName(u"button_addCncSettings")
        sizePolicy.setHeightForWidth(self.button_addCncSettings.sizePolicy().hasHeightForWidth())
        self.button_addCncSettings.setSizePolicy(sizePolicy)
        self.button_addCncSettings.setFont(font)

        self.horizontalLayout_49.addWidget(self.button_addCncSettings, 0, Qt.AlignmentFlag.AlignHCenter)

        self.button_modifyCncSettings = QPushButton(self.page13)
        self.button_modifyCncSettings.setObjectName(u"button_modifyCncSettings")
        sizePolicy.setHeightForWidth(self.button_modifyCncSettings.sizePolicy().hasHeightForWidth())
        self.button_modifyCncSettings.setSizePolicy(sizePolicy)
        self.button_modifyCncSettings.setFont(font)

        self.horizontalLayout_49.addWidget(self.button_modifyCncSettings, 0, Qt.AlignmentFlag.AlignHCenter)

        self.button_deleteCncSettings = QPushButton(self.page13)
        self.button_deleteCncSettings.setObjectName(u"button_deleteCncSettings")
        sizePolicy.setHeightForWidth(self.button_deleteCncSettings.sizePolicy().hasHeightForWidth())
        self.button_deleteCncSettings.setSizePolicy(sizePolicy)
        self.button_deleteCncSettings.setFont(font)

        self.horizontalLayout_49.addWidget(self.button_deleteCncSettings, 0, Qt.AlignmentFlag.AlignHCenter)


        self.page13Layout.addLayout(self.horizontalLayout_49)

        self.line_18 = QFrame(self.page13)
        self.line_18.setObjectName(u"line_18")
        self.line_18.setFrameShape(QFrame.Shape.HLine)
        self.line_18.setFrameShadow(QFrame.Shadow.Sunken)

        self.page13Layout.addWidget(self.line_18)

        self.tableWidget_cncList = QTableWidget(self.page13)
        self.tableWidget_cncList.setObjectName(u"tableWidget_cncList")
        self.tableWidget_cncList.setFont(font)

        self.page13Layout.addWidget(self.tableWidget_cncList)

        self.stackedWidget_main.addWidget(self.page13)
        self.page14 = QWidget()
        self.page14.setObjectName(u"page14")
        self.page14Layout = QVBoxLayout(self.page14)
        self.page14Layout.setObjectName(u"page14Layout")
        self.horizontalLayout_50 = QHBoxLayout()
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.label_cncName = QLabel(self.page14)
        self.label_cncName.setObjectName(u"label_cncName")
        self.label_cncName.setFont(font)

        self.horizontalLayout_50.addWidget(self.label_cncName, 0, Qt.AlignmentFlag.AlignRight)

        self.lineEdit_cncName = QLineEdit(self.page14)
        self.lineEdit_cncName.setObjectName(u"lineEdit_cncName")
        sizePolicy.setHeightForWidth(self.lineEdit_cncName.sizePolicy().hasHeightForWidth())
        self.lineEdit_cncName.setSizePolicy(sizePolicy)
        self.lineEdit_cncName.setFont(font)

        self.horizontalLayout_50.addWidget(self.lineEdit_cncName, 0, Qt.AlignmentFlag.AlignLeft)


        self.page14Layout.addLayout(self.horizontalLayout_50)

        self.horizontalLayout_51 = QHBoxLayout()
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.label_cncIpAddress = QLabel(self.page14)
        self.label_cncIpAddress.setObjectName(u"label_cncIpAddress")
        self.label_cncIpAddress.setFont(font)

        self.horizontalLayout_51.addWidget(self.label_cncIpAddress, 0, Qt.AlignmentFlag.AlignRight)

        self.lineEdit_cncIpAddress = QLineEdit(self.page14)
        self.lineEdit_cncIpAddress.setObjectName(u"lineEdit_cncIpAddress")
        sizePolicy.setHeightForWidth(self.lineEdit_cncIpAddress.sizePolicy().hasHeightForWidth())
        self.lineEdit_cncIpAddress.setSizePolicy(sizePolicy)
        self.lineEdit_cncIpAddress.setFont(font)

        self.horizontalLayout_51.addWidget(self.lineEdit_cncIpAddress, 0, Qt.AlignmentFlag.AlignLeft)


        self.page14Layout.addLayout(self.horizontalLayout_51)

        self.horizontalLayout_52 = QHBoxLayout()
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.label_cncPortNumber = QLabel(self.page14)
        self.label_cncPortNumber.setObjectName(u"label_cncPortNumber")
        self.label_cncPortNumber.setFont(font)

        self.horizontalLayout_52.addWidget(self.label_cncPortNumber, 0, Qt.AlignmentFlag.AlignRight)

        self.lineEdit_cncPortNumber = QLineEdit(self.page14)
        self.lineEdit_cncPortNumber.setObjectName(u"lineEdit_cncPortNumber")
        sizePolicy.setHeightForWidth(self.lineEdit_cncPortNumber.sizePolicy().hasHeightForWidth())
        self.lineEdit_cncPortNumber.setSizePolicy(sizePolicy)
        self.lineEdit_cncPortNumber.setFont(font)

        self.horizontalLayout_52.addWidget(self.lineEdit_cncPortNumber, 0, Qt.AlignmentFlag.AlignLeft)


        self.page14Layout.addLayout(self.horizontalLayout_52)

        self.horizontalLayout_53 = QHBoxLayout()
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.label_cncSelectionType = QLabel(self.page14)
        self.label_cncSelectionType.setObjectName(u"label_cncSelectionType")
        self.label_cncSelectionType.setFont(font)

        self.horizontalLayout_53.addWidget(self.label_cncSelectionType, 0, Qt.AlignmentFlag.AlignRight)

        self.comboBox_cncSelectionType = QComboBox(self.page14)
        self.comboBox_cncSelectionType.addItem("")
        self.comboBox_cncSelectionType.addItem("")
        self.comboBox_cncSelectionType.addItem("")
        self.comboBox_cncSelectionType.addItem("")
        self.comboBox_cncSelectionType.addItem("")
        self.comboBox_cncSelectionType.setObjectName(u"comboBox_cncSelectionType")
        self.comboBox_cncSelectionType.setMinimumSize(QSize(130, 0))
        self.comboBox_cncSelectionType.setFont(font)

        self.horizontalLayout_53.addWidget(self.comboBox_cncSelectionType, 0, Qt.AlignmentFlag.AlignLeft)


        self.page14Layout.addLayout(self.horizontalLayout_53)

        self.horizontalLayout_54 = QHBoxLayout()
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.label_cncController = QLabel(self.page14)
        self.label_cncController.setObjectName(u"label_cncController")
        self.label_cncController.setFont(font)

        self.horizontalLayout_54.addWidget(self.label_cncController, 0, Qt.AlignmentFlag.AlignRight)

        self.comboBox_cncController = QComboBox(self.page14)
        self.comboBox_cncController.addItem("")
        self.comboBox_cncController.addItem("")
        self.comboBox_cncController.addItem("")
        self.comboBox_cncController.setObjectName(u"comboBox_cncController")
        self.comboBox_cncController.setMinimumSize(QSize(140, 0))
        self.comboBox_cncController.setFont(font)

        self.horizontalLayout_54.addWidget(self.comboBox_cncController, 0, Qt.AlignmentFlag.AlignLeft)


        self.page14Layout.addLayout(self.horizontalLayout_54)

        self.stackedWidget_main.addWidget(self.page14)
        self.page15 = QWidget()
        self.page15.setObjectName(u"page15")
        self.page15Layout = QVBoxLayout(self.page15)
        self.page15Layout.setObjectName(u"page15Layout")
        self.horizontalLayout_55 = QHBoxLayout()
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.horizontalSpacer_25 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_55.addItem(self.horizontalSpacer_25)

        self.label_autoOffsetCorrection = QLabel(self.page15)
        self.label_autoOffsetCorrection.setObjectName(u"label_autoOffsetCorrection")
        self.label_autoOffsetCorrection.setFont(font1)

        self.horizontalLayout_55.addWidget(self.label_autoOffsetCorrection, 0, Qt.AlignmentFlag.AlignRight)

        self.toggleButton_aoc = QLabel(self.page15)
        self.toggleButton_aoc.setObjectName(u"toggleButton_aoc")

        image_path = os.path.join(script_dir, "Switcher_On.png")  # if it's in the same folder
        self.toggleButton_aoc.setPixmap(QPixmap(image_path))

        self.horizontalLayout_55.addWidget(self.toggleButton_aoc, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_aocOnOff = QLabel(self.page15)
        self.label_aocOnOff.setObjectName(u"label_aocOnOff")
        self.label_aocOnOff.setFont(font1)

        self.horizontalLayout_55.addWidget(self.label_aocOnOff, 0, Qt.AlignmentFlag.AlignLeft)

        self.horizontalSpacer_26 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_55.addItem(self.horizontalSpacer_26)


        self.page15Layout.addLayout(self.horizontalLayout_55)

        self.line_19 = QFrame(self.page15)
        self.line_19.setObjectName(u"line_19")
        self.line_19.setFrameShape(QFrame.Shape.HLine)
        self.line_19.setFrameShadow(QFrame.Shadow.Sunken)

        self.page15Layout.addWidget(self.line_19)

        self.verticalSpacer_31 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.page15Layout.addItem(self.verticalSpacer_31)

        self.horizontalLayout_56 = QHBoxLayout()
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.button_measurementListAoc = QPushButton(self.page15)
        self.button_measurementListAoc.setObjectName(u"button_measurementListAoc")
        sizePolicy.setHeightForWidth(self.button_measurementListAoc.sizePolicy().hasHeightForWidth())
        self.button_measurementListAoc.setSizePolicy(sizePolicy)
        self.button_measurementListAoc.setMinimumSize(QSize(150, 0))
        self.button_measurementListAoc.setFont(font)

        self.horizontalLayout_56.addWidget(self.button_measurementListAoc, 0, Qt.AlignmentFlag.AlignHCenter)


        self.page15Layout.addLayout(self.horizontalLayout_56)

        self.verticalSpacer_29 = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.page15Layout.addItem(self.verticalSpacer_29)

        self.horizontalLayout_57 = QHBoxLayout()
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.button_cncListAoc = QPushButton(self.page15)
        self.button_cncListAoc.setObjectName(u"button_cncListAoc")
        sizePolicy.setHeightForWidth(self.button_cncListAoc.sizePolicy().hasHeightForWidth())
        self.button_cncListAoc.setSizePolicy(sizePolicy)
        self.button_cncListAoc.setMinimumSize(QSize(150, 0))
        self.button_cncListAoc.setFont(font)

        self.horizontalLayout_57.addWidget(self.button_cncListAoc, 0, Qt.AlignmentFlag.AlignHCenter)


        self.page15Layout.addLayout(self.horizontalLayout_57)

        self.verticalSpacer_30 = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.page15Layout.addItem(self.verticalSpacer_30)

        self.horizontalLayout_58 = QHBoxLayout()
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.button_reportsAoc = QPushButton(self.page15)
        self.button_reportsAoc.setObjectName(u"button_reportsAoc")
        sizePolicy.setHeightForWidth(self.button_reportsAoc.sizePolicy().hasHeightForWidth())
        self.button_reportsAoc.setSizePolicy(sizePolicy)
        self.button_reportsAoc.setMinimumSize(QSize(150, 0))
        self.button_reportsAoc.setFont(font)

        self.horizontalLayout_58.addWidget(self.button_reportsAoc, 0, Qt.AlignmentFlag.AlignHCenter)


        self.page15Layout.addLayout(self.horizontalLayout_58)

        self.verticalSpacer_28 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.page15Layout.addItem(self.verticalSpacer_28)

        self.stackedWidget_main.addWidget(self.page15)
        self.page_16 = QWidget()
        self.page_16.setObjectName(u"page_16")
        self.verticalLayout_page16 = QVBoxLayout(self.page_16)
        self.verticalLayout_page16.setObjectName(u"verticalLayout_page16")
        self.horizontalLayout_60 = QHBoxLayout()
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.label_partNameAoc = QLabel(self.page_16)
        self.label_partNameAoc.setObjectName(u"label_partNameAoc")
        self.label_partNameAoc.setFont(font3)

        self.horizontalLayout_60.addWidget(self.label_partNameAoc, 0, Qt.AlignmentFlag.AlignRight)

        self.lineEdit_partNameAoc = QLineEdit(self.page_16)
        self.lineEdit_partNameAoc.setObjectName(u"lineEdit_partNameAoc")
        sizePolicy.setHeightForWidth(self.lineEdit_partNameAoc.sizePolicy().hasHeightForWidth())
        self.lineEdit_partNameAoc.setSizePolicy(sizePolicy)
        self.lineEdit_partNameAoc.setFont(font3)

        self.horizontalLayout_60.addWidget(self.lineEdit_partNameAoc, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_page16.addLayout(self.horizontalLayout_60)

        self.horizontalLayout_62 = QHBoxLayout()
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.label_dimensionNoAoc = QLabel(self.page_16)
        self.label_dimensionNoAoc.setObjectName(u"label_dimensionNoAoc")
        self.label_dimensionNoAoc.setFont(font3)

        self.horizontalLayout_62.addWidget(self.label_dimensionNoAoc, 0, Qt.AlignmentFlag.AlignRight)

        self.comboBox_dimensionNoAoc = QComboBox(self.page_16)
        self.comboBox_dimensionNoAoc.addItem("")
        self.comboBox_dimensionNoAoc.addItem("")
        self.comboBox_dimensionNoAoc.addItem("")
        self.comboBox_dimensionNoAoc.addItem("")
        self.comboBox_dimensionNoAoc.setObjectName(u"comboBox_dimensionNoAoc")
        self.comboBox_dimensionNoAoc.setMinimumSize(QSize(220, 0))
        self.comboBox_dimensionNoAoc.setFont(font)

        self.horizontalLayout_62.addWidget(self.comboBox_dimensionNoAoc, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_page16.addLayout(self.horizontalLayout_62)

        self.line_20 = QFrame(self.page_16)
        self.line_20.setObjectName(u"line_20")
        self.line_20.setFrameShape(QFrame.Shape.HLine)
        self.line_20.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_page16.addWidget(self.line_20)

        self.scrollArea_page16 = QScrollArea(self.page_16)
        self.scrollArea_page16.setObjectName(u"scrollArea_page16")
        self.scrollArea_page16.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scrollArea_page16.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea_page16.setWidgetResizable(True)
        self.scrollAreaWidgetContents_page16 = QWidget()
        self.scrollAreaWidgetContents_page16.setObjectName(u"scrollAreaWidgetContents_page16")
        self.scrollAreaWidgetContents_page16.setGeometry(QRect(0, 0, 249, 598))
        self.verticalLayout_scroll_page16 = QVBoxLayout(self.scrollAreaWidgetContents_page16)
        self.verticalLayout_scroll_page16.setObjectName(u"verticalLayout_scroll_page16")
        self.horizontalLayout_63 = QHBoxLayout()
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.label_uolAoc = QLabel(self.scrollAreaWidgetContents_page16)
        self.label_uolAoc.setObjectName(u"label_uolAoc")
        self.label_uolAoc.setFont(font)

        self.horizontalLayout_63.addWidget(self.label_uolAoc, 0, Qt.AlignmentFlag.AlignRight)

        self.lineEdit_uolAoc = QLineEdit(self.scrollAreaWidgetContents_page16)
        self.lineEdit_uolAoc.setObjectName(u"lineEdit_uolAoc")
        sizePolicy.setHeightForWidth(self.lineEdit_uolAoc.sizePolicy().hasHeightForWidth())
        self.lineEdit_uolAoc.setSizePolicy(sizePolicy)
        self.lineEdit_uolAoc.setFont(font)

        self.horizontalLayout_63.addWidget(self.lineEdit_uolAoc, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_scroll_page16.addLayout(self.horizontalLayout_63)

        self.horizontalLayout_64 = QHBoxLayout()
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.label_uslAoc = QLabel(self.scrollAreaWidgetContents_page16)
        self.label_uslAoc.setObjectName(u"label_uslAoc")
        self.label_uslAoc.setFont(font)

        self.horizontalLayout_64.addWidget(self.label_uslAoc, 0, Qt.AlignmentFlag.AlignRight)

        self.lineEdit_uslAoc = QLineEdit(self.scrollAreaWidgetContents_page16)
        self.lineEdit_uslAoc.setObjectName(u"lineEdit_uslAoc")
        sizePolicy.setHeightForWidth(self.lineEdit_uslAoc.sizePolicy().hasHeightForWidth())
        self.lineEdit_uslAoc.setSizePolicy(sizePolicy)
        self.lineEdit_uslAoc.setFont(font)

        self.horizontalLayout_64.addWidget(self.lineEdit_uslAoc, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_scroll_page16.addLayout(self.horizontalLayout_64)

        self.horizontalLayout_59 = QHBoxLayout()
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.label_uclAoc = QLabel(self.scrollAreaWidgetContents_page16)
        self.label_uclAoc.setObjectName(u"label_uclAoc")
        self.label_uclAoc.setFont(font)

        self.horizontalLayout_59.addWidget(self.label_uclAoc, 0, Qt.AlignmentFlag.AlignRight)

        self.lineEdit_uclAoc = QLineEdit(self.scrollAreaWidgetContents_page16)
        self.lineEdit_uclAoc.setObjectName(u"lineEdit_uclAoc")
        sizePolicy.setHeightForWidth(self.lineEdit_uclAoc.sizePolicy().hasHeightForWidth())
        self.lineEdit_uclAoc.setSizePolicy(sizePolicy)
        self.lineEdit_uclAoc.setFont(font)

        self.horizontalLayout_59.addWidget(self.lineEdit_uclAoc, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_scroll_page16.addLayout(self.horizontalLayout_59)

        self.horizontalLayout_65 = QHBoxLayout()
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.label_nominalAoc = QLabel(self.scrollAreaWidgetContents_page16)
        self.label_nominalAoc.setObjectName(u"label_nominalAoc")
        self.label_nominalAoc.setFont(font)

        self.horizontalLayout_65.addWidget(self.label_nominalAoc, 0, Qt.AlignmentFlag.AlignRight)

        self.lineEdit_nominalAoc = QLineEdit(self.scrollAreaWidgetContents_page16)
        self.lineEdit_nominalAoc.setObjectName(u"lineEdit_nominalAoc")
        sizePolicy.setHeightForWidth(self.lineEdit_nominalAoc.sizePolicy().hasHeightForWidth())
        self.lineEdit_nominalAoc.setSizePolicy(sizePolicy)
        self.lineEdit_nominalAoc.setFont(font)

        self.horizontalLayout_65.addWidget(self.lineEdit_nominalAoc, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_scroll_page16.addLayout(self.horizontalLayout_65)

        self.horizontalLayout_66 = QHBoxLayout()
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.label_lclAoc = QLabel(self.scrollAreaWidgetContents_page16)
        self.label_lclAoc.setObjectName(u"label_lclAoc")
        self.label_lclAoc.setFont(font)

        self.horizontalLayout_66.addWidget(self.label_lclAoc, 0, Qt.AlignmentFlag.AlignRight)

        self.lineEdit_lclAoc = QLineEdit(self.scrollAreaWidgetContents_page16)
        self.lineEdit_lclAoc.setObjectName(u"lineEdit_lclAoc")
        sizePolicy.setHeightForWidth(self.lineEdit_lclAoc.sizePolicy().hasHeightForWidth())
        self.lineEdit_lclAoc.setSizePolicy(sizePolicy)
        self.lineEdit_lclAoc.setFont(font)

        self.horizontalLayout_66.addWidget(self.lineEdit_lclAoc, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_scroll_page16.addLayout(self.horizontalLayout_66)

        self.horizontalLayout_67 = QHBoxLayout()
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.label_lslAoc = QLabel(self.scrollAreaWidgetContents_page16)
        self.label_lslAoc.setObjectName(u"label_lslAoc")
        self.label_lslAoc.setFont(font)

        self.horizontalLayout_67.addWidget(self.label_lslAoc, 0, Qt.AlignmentFlag.AlignRight)

        self.lineEdit_lslAoc = QLineEdit(self.scrollAreaWidgetContents_page16)
        self.lineEdit_lslAoc.setObjectName(u"lineEdit_lslAoc")
        sizePolicy.setHeightForWidth(self.lineEdit_lslAoc.sizePolicy().hasHeightForWidth())
        self.lineEdit_lslAoc.setSizePolicy(sizePolicy)
        self.lineEdit_lslAoc.setFont(font)

        self.horizontalLayout_67.addWidget(self.lineEdit_lslAoc, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_scroll_page16.addLayout(self.horizontalLayout_67)

        self.horizontalLayout_68 = QHBoxLayout()
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.label_lolAoc = QLabel(self.scrollAreaWidgetContents_page16)
        self.label_lolAoc.setObjectName(u"label_lolAoc")
        self.label_lolAoc.setFont(font)

        self.horizontalLayout_68.addWidget(self.label_lolAoc, 0, Qt.AlignmentFlag.AlignRight)

        self.lineEdit_lolAoc = QLineEdit(self.scrollAreaWidgetContents_page16)
        self.lineEdit_lolAoc.setObjectName(u"lineEdit_lolAoc")
        sizePolicy.setHeightForWidth(self.lineEdit_lolAoc.sizePolicy().hasHeightForWidth())
        self.lineEdit_lolAoc.setSizePolicy(sizePolicy)
        self.lineEdit_lolAoc.setFont(font)

        self.horizontalLayout_68.addWidget(self.lineEdit_lolAoc, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_scroll_page16.addLayout(self.horizontalLayout_68)

        self.horizontalLayout_69 = QHBoxLayout()
        self.horizontalLayout_69.setObjectName(u"horizontalLayout_69")
        self.label_axisAoc = QLabel(self.scrollAreaWidgetContents_page16)
        self.label_axisAoc.setObjectName(u"label_axisAoc")
        self.label_axisAoc.setFont(font)

        self.horizontalLayout_69.addWidget(self.label_axisAoc, 0, Qt.AlignmentFlag.AlignRight)

        self.comboBox_axisAoc = QComboBox(self.scrollAreaWidgetContents_page16)
        self.comboBox_axisAoc.addItem("")
        self.comboBox_axisAoc.addItem("")
        self.comboBox_axisAoc.addItem("")
        self.comboBox_axisAoc.setObjectName(u"comboBox_axisAoc")
        self.comboBox_axisAoc.setMinimumSize(QSize(150, 0))
        self.comboBox_axisAoc.setFont(font)

        self.horizontalLayout_69.addWidget(self.comboBox_axisAoc, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_scroll_page16.addLayout(self.horizontalLayout_69)

        self.horizontalLayout_70 = QHBoxLayout()
        self.horizontalLayout_70.setObjectName(u"horizontalLayout_70")
        self.label_offsetNoAoc = QLabel(self.scrollAreaWidgetContents_page16)
        self.label_offsetNoAoc.setObjectName(u"label_offsetNoAoc")
        self.label_offsetNoAoc.setFont(font)

        self.horizontalLayout_70.addWidget(self.label_offsetNoAoc, 0, Qt.AlignmentFlag.AlignRight)

        self.lineEdit_offsetNoAoc = QLineEdit(self.scrollAreaWidgetContents_page16)
        self.lineEdit_offsetNoAoc.setObjectName(u"lineEdit_offsetNoAoc")
        sizePolicy.setHeightForWidth(self.lineEdit_offsetNoAoc.sizePolicy().hasHeightForWidth())
        self.lineEdit_offsetNoAoc.setSizePolicy(sizePolicy)
        self.lineEdit_offsetNoAoc.setFont(font)

        self.horizontalLayout_70.addWidget(self.lineEdit_offsetNoAoc, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_scroll_page16.addLayout(self.horizontalLayout_70)

        self.horizontalLayout_71 = QHBoxLayout()
        self.horizontalLayout_71.setObjectName(u"horizontalLayout_71")
        self.label_machineAoc = QLabel(self.scrollAreaWidgetContents_page16)
        self.label_machineAoc.setObjectName(u"label_machineAoc")
        self.label_machineAoc.setFont(font)

        self.horizontalLayout_71.addWidget(self.label_machineAoc, 0, Qt.AlignmentFlag.AlignRight)

        self.comboBox_machineAoc = QComboBox(self.scrollAreaWidgetContents_page16)
        self.comboBox_machineAoc.setObjectName(u"comboBox_machineAoc")
        self.comboBox_machineAoc.setMinimumSize(QSize(150, 0))
        self.comboBox_machineAoc.setFont(font)

        self.horizontalLayout_71.addWidget(self.comboBox_machineAoc, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_scroll_page16.addLayout(self.horizontalLayout_71)

        self.horizontalLayout_72 = QHBoxLayout()
        self.horizontalLayout_72.setObjectName(u"horizontalLayout_72")
        self.label_nameOfIdentifierAoc = QLabel(self.scrollAreaWidgetContents_page16)
        self.label_nameOfIdentifierAoc.setObjectName(u"label_nameOfIdentifierAoc")
        self.label_nameOfIdentifierAoc.setFont(font)

        self.horizontalLayout_72.addWidget(self.label_nameOfIdentifierAoc, 0, Qt.AlignmentFlag.AlignRight)

        self.lineEdit_nameOfIdentifierAoc = QLineEdit(self.scrollAreaWidgetContents_page16)
        self.lineEdit_nameOfIdentifierAoc.setObjectName(u"lineEdit_nameOfIdentifierAoc")
        sizePolicy.setHeightForWidth(self.lineEdit_nameOfIdentifierAoc.sizePolicy().hasHeightForWidth())
        self.lineEdit_nameOfIdentifierAoc.setSizePolicy(sizePolicy)
        self.lineEdit_nameOfIdentifierAoc.setFont(font)

        self.horizontalLayout_72.addWidget(self.lineEdit_nameOfIdentifierAoc, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_scroll_page16.addLayout(self.horizontalLayout_72)

        self.horizontalLayout_73 = QHBoxLayout()
        self.horizontalLayout_73.setObjectName(u"horizontalLayout_73")
        self.label_startOfIdentifierAoc = QLabel(self.scrollAreaWidgetContents_page16)
        self.label_startOfIdentifierAoc.setObjectName(u"label_startOfIdentifierAoc")
        self.label_startOfIdentifierAoc.setFont(font)

        self.horizontalLayout_73.addWidget(self.label_startOfIdentifierAoc, 0, Qt.AlignmentFlag.AlignRight)

        self.lineEdit_startOfIdentifierAoc = QLineEdit(self.scrollAreaWidgetContents_page16)
        self.lineEdit_startOfIdentifierAoc.setObjectName(u"lineEdit_startOfIdentifierAoc")
        sizePolicy.setHeightForWidth(self.lineEdit_startOfIdentifierAoc.sizePolicy().hasHeightForWidth())
        self.lineEdit_startOfIdentifierAoc.setSizePolicy(sizePolicy)
        self.lineEdit_startOfIdentifierAoc.setFont(font)

        self.horizontalLayout_73.addWidget(self.lineEdit_startOfIdentifierAoc, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_scroll_page16.addLayout(self.horizontalLayout_73)

        self.horizontalLayout_74 = QHBoxLayout()
        self.horizontalLayout_74.setObjectName(u"horizontalLayout_74")
        self.label_endOfIdentifierAoc = QLabel(self.scrollAreaWidgetContents_page16)
        self.label_endOfIdentifierAoc.setObjectName(u"label_endOfIdentifierAoc")
        self.label_endOfIdentifierAoc.setFont(font)

        self.horizontalLayout_74.addWidget(self.label_endOfIdentifierAoc, 0, Qt.AlignmentFlag.AlignRight)

        self.lineEdit_endOfIdentifierAoc = QLineEdit(self.scrollAreaWidgetContents_page16)
        self.lineEdit_endOfIdentifierAoc.setObjectName(u"lineEdit_endOfIdentifierAoc")
        sizePolicy.setHeightForWidth(self.lineEdit_endOfIdentifierAoc.sizePolicy().hasHeightForWidth())
        self.lineEdit_endOfIdentifierAoc.setSizePolicy(sizePolicy)
        self.lineEdit_endOfIdentifierAoc.setFont(font)

        self.horizontalLayout_74.addWidget(self.lineEdit_endOfIdentifierAoc, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_scroll_page16.addLayout(self.horizontalLayout_74)

        self.horizontalLayout_75 = QHBoxLayout()
        self.horizontalLayout_75.setObjectName(u"horizontalLayout_75")
        self.label_startOfDataAoc = QLabel(self.scrollAreaWidgetContents_page16)
        self.label_startOfDataAoc.setObjectName(u"label_startOfDataAoc")
        self.label_startOfDataAoc.setFont(font)

        self.horizontalLayout_75.addWidget(self.label_startOfDataAoc, 0, Qt.AlignmentFlag.AlignRight)

        self.lineEdit_startOfDataAoc = QLineEdit(self.scrollAreaWidgetContents_page16)
        self.lineEdit_startOfDataAoc.setObjectName(u"lineEdit_startOfDataAoc")
        sizePolicy.setHeightForWidth(self.lineEdit_startOfDataAoc.sizePolicy().hasHeightForWidth())
        self.lineEdit_startOfDataAoc.setSizePolicy(sizePolicy)
        self.lineEdit_startOfDataAoc.setFont(font)

        self.horizontalLayout_75.addWidget(self.lineEdit_startOfDataAoc, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_scroll_page16.addLayout(self.horizontalLayout_75)

        self.horizontalLayout_76 = QHBoxLayout()
        self.horizontalLayout_76.setObjectName(u"horizontalLayout_76")
        self.label_endOfDataAoc = QLabel(self.scrollAreaWidgetContents_page16)
        self.label_endOfDataAoc.setObjectName(u"label_endOfDataAoc")
        self.label_endOfDataAoc.setFont(font)

        self.horizontalLayout_76.addWidget(self.label_endOfDataAoc, 0, Qt.AlignmentFlag.AlignRight)

        self.lineEdit_endOfDataAoc = QLineEdit(self.scrollAreaWidgetContents_page16)
        self.lineEdit_endOfDataAoc.setObjectName(u"lineEdit_endOfDataAoc")
        sizePolicy.setHeightForWidth(self.lineEdit_endOfDataAoc.sizePolicy().hasHeightForWidth())
        self.lineEdit_endOfDataAoc.setSizePolicy(sizePolicy)
        self.lineEdit_endOfDataAoc.setFont(font)

        self.horizontalLayout_76.addWidget(self.lineEdit_endOfDataAoc, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_scroll_page16.addLayout(self.horizontalLayout_76)

        self.horizontalLayout_77 = QHBoxLayout()
        self.horizontalLayout_77.setObjectName(u"horizontalLayout_77")
        self.label_directionAoc = QLabel(self.scrollAreaWidgetContents_page16)
        self.label_directionAoc.setObjectName(u"label_directionAoc")
        self.label_directionAoc.setFont(font)

        self.horizontalLayout_77.addWidget(self.label_directionAoc, 0, Qt.AlignmentFlag.AlignRight)

        self.lineEdit_directionAoc = QLineEdit(self.scrollAreaWidgetContents_page16)
        self.lineEdit_directionAoc.setObjectName(u"lineEdit_directionAoc")
        sizePolicy.setHeightForWidth(self.lineEdit_directionAoc.sizePolicy().hasHeightForWidth())
        self.lineEdit_directionAoc.setSizePolicy(sizePolicy)
        self.lineEdit_directionAoc.setFont(font)

        self.horizontalLayout_77.addWidget(self.lineEdit_directionAoc, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_scroll_page16.addLayout(self.horizontalLayout_77)

        self.horizontalLayout_78 = QHBoxLayout()
        self.horizontalLayout_78.setObjectName(u"horizontalLayout_78")
        self.label_turretNoAoc = QLabel(self.scrollAreaWidgetContents_page16)
        self.label_turretNoAoc.setObjectName(u"label_turretNoAoc")
        self.label_turretNoAoc.setFont(font)

        self.horizontalLayout_78.addWidget(self.label_turretNoAoc, 0, Qt.AlignmentFlag.AlignRight)

        self.lineEdit_turretNoAoc = QLineEdit(self.scrollAreaWidgetContents_page16)
        self.lineEdit_turretNoAoc.setObjectName(u"lineEdit_turretNoAoc")
        sizePolicy.setHeightForWidth(self.lineEdit_turretNoAoc.sizePolicy().hasHeightForWidth())
        self.lineEdit_turretNoAoc.setSizePolicy(sizePolicy)
        self.lineEdit_turretNoAoc.setFont(font)

        self.horizontalLayout_78.addWidget(self.lineEdit_turretNoAoc, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_scroll_page16.addLayout(self.horizontalLayout_78)

        self.scrollArea_page16.setWidget(self.scrollAreaWidgetContents_page16)

        self.verticalLayout_page16.addWidget(self.scrollArea_page16)

        self.stackedWidget_main.addWidget(self.page_16)
        self.page17 = QWidget()
        self.page17.setObjectName(u"page17")
        self.page17Layout = QVBoxLayout(self.page17)
        self.page17Layout.setObjectName(u"page17Layout")
        self.verticalSpacer_32 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.page17Layout.addItem(self.verticalSpacer_32)

        self.horizontalLayout_84 = QHBoxLayout()
        self.horizontalLayout_84.setObjectName(u"horizontalLayout_84")
        self.horizontalSpacer_27 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_84.addItem(self.horizontalSpacer_27)

        self.label_networkBasedDatabase = QLabel(self.page17)
        self.label_networkBasedDatabase.setObjectName(u"label_networkBasedDatabase")
        self.label_networkBasedDatabase.setFont(font1)

        self.horizontalLayout_84.addWidget(self.label_networkBasedDatabase)

        self.toggleButton_networkBasedDatabase = QLabel(self.page17)
        self.toggleButton_networkBasedDatabase.setObjectName(u"toggleButton_networkBasedDatabase")

        image_path = os.path.join(script_dir, "Switcher_On.png")  # if it's in the same folder
        self.toggleButton_networkBasedDatabase.setPixmap(QPixmap(image_path))

        self.horizontalLayout_84.addWidget(self.toggleButton_networkBasedDatabase)

        self.label_networkBasedDatabaseOnOff = QLabel(self.page17)
        self.label_networkBasedDatabaseOnOff.setObjectName(u"label_networkBasedDatabaseOnOff")
        self.label_networkBasedDatabaseOnOff.setFont(font1)

        self.horizontalLayout_84.addWidget(self.label_networkBasedDatabaseOnOff)

        self.horizontalSpacer_28 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_84.addItem(self.horizontalSpacer_28)


        self.page17Layout.addLayout(self.horizontalLayout_84)

        self.verticalSpacer_23 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.page17Layout.addItem(self.verticalSpacer_23)

        self.line_21 = QFrame(self.page17)
        self.line_21.setObjectName(u"line_21")
        self.line_21.setFrameShape(QFrame.Shape.HLine)
        self.line_21.setFrameShadow(QFrame.Shadow.Sunken)

        self.page17Layout.addWidget(self.line_21)

        self.verticalSpacer_34 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.page17Layout.addItem(self.verticalSpacer_34)

        self.horizontalLayout_61 = QHBoxLayout()
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.label_driverNameDb = QLabel(self.page17)
        self.label_driverNameDb.setObjectName(u"label_driverNameDb")
        self.label_driverNameDb.setFont(font)

        self.horizontalLayout_61.addWidget(self.label_driverNameDb, 0, Qt.AlignmentFlag.AlignRight)

        self.lineEdit_driverNameDb = QLineEdit(self.page17)
        self.lineEdit_driverNameDb.setObjectName(u"lineEdit_driverNameDb")
        sizePolicy.setHeightForWidth(self.lineEdit_driverNameDb.sizePolicy().hasHeightForWidth())
        self.lineEdit_driverNameDb.setSizePolicy(sizePolicy)
        self.lineEdit_driverNameDb.setMinimumSize(QSize(250, 0))
        self.lineEdit_driverNameDb.setFont(font)

        self.horizontalLayout_61.addWidget(self.lineEdit_driverNameDb, 0, Qt.AlignmentFlag.AlignLeft)


        self.page17Layout.addLayout(self.horizontalLayout_61)

        self.horizontalLayout_79 = QHBoxLayout()
        self.horizontalLayout_79.setObjectName(u"horizontalLayout_79")
        self.label_serverNameDb = QLabel(self.page17)
        self.label_serverNameDb.setObjectName(u"label_serverNameDb")
        self.label_serverNameDb.setFont(font)

        self.horizontalLayout_79.addWidget(self.label_serverNameDb, 0, Qt.AlignmentFlag.AlignRight)

        self.lineEdit_serverNameDb = QLineEdit(self.page17)
        self.lineEdit_serverNameDb.setObjectName(u"lineEdit_serverNameDb")
        sizePolicy.setHeightForWidth(self.lineEdit_serverNameDb.sizePolicy().hasHeightForWidth())
        self.lineEdit_serverNameDb.setSizePolicy(sizePolicy)
        self.lineEdit_serverNameDb.setMinimumSize(QSize(250, 0))
        self.lineEdit_serverNameDb.setFont(font)

        self.horizontalLayout_79.addWidget(self.lineEdit_serverNameDb, 0, Qt.AlignmentFlag.AlignLeft)


        self.page17Layout.addLayout(self.horizontalLayout_79)

        self.horizontalLayout_80 = QHBoxLayout()
        self.horizontalLayout_80.setObjectName(u"horizontalLayout_80")
        self.label_databaseNameDb = QLabel(self.page17)
        self.label_databaseNameDb.setObjectName(u"label_databaseNameDb")
        self.label_databaseNameDb.setFont(font)

        self.horizontalLayout_80.addWidget(self.label_databaseNameDb, 0, Qt.AlignmentFlag.AlignRight)

        self.lineEdit_databaseNameDb = QLineEdit(self.page17)
        self.lineEdit_databaseNameDb.setObjectName(u"lineEdit_databaseNameDb")
        self.lineEdit_databaseNameDb.setMinimumSize(QSize(250, 0))
        self.lineEdit_databaseNameDb.setFont(font)

        self.horizontalLayout_80.addWidget(self.lineEdit_databaseNameDb, 0, Qt.AlignmentFlag.AlignLeft)


        self.page17Layout.addLayout(self.horizontalLayout_80)

        self.horizontalLayout_81 = QHBoxLayout()
        self.horizontalLayout_81.setObjectName(u"horizontalLayout_81")
        self.label_username_Db = QLabel(self.page17)
        self.label_username_Db.setObjectName(u"label_username_Db")
        self.label_username_Db.setFont(font)

        self.horizontalLayout_81.addWidget(self.label_username_Db, 0, Qt.AlignmentFlag.AlignRight)

        self.lineEdit_usernameDb = QLineEdit(self.page17)
        self.lineEdit_usernameDb.setObjectName(u"lineEdit_usernameDb")
        sizePolicy.setHeightForWidth(self.lineEdit_usernameDb.sizePolicy().hasHeightForWidth())
        self.lineEdit_usernameDb.setSizePolicy(sizePolicy)
        self.lineEdit_usernameDb.setMinimumSize(QSize(250, 0))
        self.lineEdit_usernameDb.setFont(font)

        self.horizontalLayout_81.addWidget(self.lineEdit_usernameDb, 0, Qt.AlignmentFlag.AlignLeft)


        self.page17Layout.addLayout(self.horizontalLayout_81)

        self.horizontalLayout_82 = QHBoxLayout()
        self.horizontalLayout_82.setObjectName(u"horizontalLayout_82")
        self.label_passwordDb = QLabel(self.page17)
        self.label_passwordDb.setObjectName(u"label_passwordDb")
        self.label_passwordDb.setFont(font)

        self.horizontalLayout_82.addWidget(self.label_passwordDb, 0, Qt.AlignmentFlag.AlignRight)

        self.lineEdit_passwordDb = QLineEdit(self.page17)
        self.lineEdit_passwordDb.setObjectName(u"lineEdit_passwordDb")
        sizePolicy.setHeightForWidth(self.lineEdit_passwordDb.sizePolicy().hasHeightForWidth())
        self.lineEdit_passwordDb.setSizePolicy(sizePolicy)
        self.lineEdit_passwordDb.setMinimumSize(QSize(250, 0))
        self.lineEdit_passwordDb.setFont(font)

        self.horizontalLayout_82.addWidget(self.lineEdit_passwordDb, 0, Qt.AlignmentFlag.AlignLeft)


        self.page17Layout.addLayout(self.horizontalLayout_82)

        self.verticalSpacer_33 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.page17Layout.addItem(self.verticalSpacer_33)

        self.stackedWidget_main.addWidget(self.page17)
        self.page18 = QWidget()
        self.page18.setObjectName(u"page18")
        self.page18Layout = QVBoxLayout(self.page18)
        self.page18Layout.setObjectName(u"page18Layout")
        self.horizontalLayout_151 = QHBoxLayout()
        self.horizontalLayout_151.setObjectName(u"horizontalLayout_151")
        self.horizontalSpacer_141 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_151.addItem(self.horizontalSpacer_141)

        self.label_programIdforSettings = QLabel(self.page18)
        self.label_programIdforSettings.setObjectName(u"label_programIdforSettings")
        self.label_programIdforSettings.setFont(font)

        self.horizontalLayout_151.addWidget(self.label_programIdforSettings, 0, Qt.AlignmentFlag.AlignHCenter)

        self.comboBox_programIdSettings = QComboBox(self.page18)
        self.comboBox_programIdSettings.setObjectName(u"comboBox_programIdSettings")
        self.comboBox_programIdSettings.setFont(font)

        self.horizontalLayout_151.addWidget(self.comboBox_programIdSettings)

        self.horizontalSpacer_137 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_151.addItem(self.horizontalSpacer_137)

        self.label_programNameSettings = QLabel(self.page18)
        self.label_programNameSettings.setObjectName(u"label_programNameSettings")
        self.label_programNameSettings.setFont(font)

        self.horizontalLayout_151.addWidget(self.label_programNameSettings, 0, Qt.AlignmentFlag.AlignHCenter)

        self.lineEdit_programNameSettings = QLineEdit(self.page18)
        self.lineEdit_programNameSettings.setObjectName(u"lineEdit_programNameSettings")
        self.lineEdit_programNameSettings.setMinimumSize(QSize(200, 0))
        self.lineEdit_programNameSettings.setFont(font)

        self.horizontalLayout_151.addWidget(self.lineEdit_programNameSettings)

        self.horizontalSpacer_132 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_151.addItem(self.horizontalSpacer_132)

        self.button_staticSettingsForAll = QPushButton(self.page18)
        self.button_staticSettingsForAll.setObjectName(u"button_staticSettingsForAll")
        self.button_staticSettingsForAll.setFont(font)

        self.horizontalLayout_151.addWidget(self.button_staticSettingsForAll)

        self.horizontalSpacer_187 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_151.addItem(self.horizontalSpacer_187)


        self.page18Layout.addLayout(self.horizontalLayout_151)

        self.horizontalLayout_173 = QHBoxLayout()
        self.horizontalLayout_173.setObjectName(u"horizontalLayout_173")
        self.horizontalSpacer_146 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_173.addItem(self.horizontalSpacer_146)

        self.label_probeSetting = QLabel(self.page18)
        self.label_probeSetting.setObjectName(u"label_probeSetting")
        self.label_probeSetting.setFont(font)

        self.horizontalLayout_173.addWidget(self.label_probeSetting, 0, Qt.AlignmentFlag.AlignHCenter)

        self.comboBox_toselectProbe = QComboBox(self.page18)
        self.comboBox_toselectProbe.addItem("")
        self.comboBox_toselectProbe.addItem("")
        self.comboBox_toselectProbe.addItem("")
        self.comboBox_toselectProbe.addItem("")
        self.comboBox_toselectProbe.addItem("")
        self.comboBox_toselectProbe.addItem("")
        self.comboBox_toselectProbe.addItem("")
        self.comboBox_toselectProbe.addItem("")
        self.comboBox_toselectProbe.setObjectName(u"comboBox_toselectProbe")
        self.comboBox_toselectProbe.setFont(font)

        self.horizontalLayout_173.addWidget(self.comboBox_toselectProbe, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalSpacer_163 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_173.addItem(self.horizontalSpacer_163)


        self.page18Layout.addLayout(self.horizontalLayout_173)

        self.line_63 = QFrame(self.page18)
        self.line_63.setObjectName(u"line_63")
        self.line_63.setFrameShape(QFrame.Shape.HLine)
        self.line_63.setFrameShadow(QFrame.Shadow.Sunken)

        self.page18Layout.addWidget(self.line_63)

        self.tabWidget = QTabWidget(self.page18)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMinimumSize(QSize(0, 0))
        font6 = QFont()
        font6.setPointSize(11)
        font6.setBold(True)
        self.tabWidget.setFont(font6)
        self.tabWidget.setStyleSheet(u"\n"
"QTabBar::tab {\n"
"    height: 40px;  /* height of the tab itself */\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    border-bottom: 4px solid #fec222;  /* height of the indicator */\n"
"}\n"
"\n"
"")
        self.tabWidget.setTabShape(QTabWidget.TabShape.Rounded)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tab.setStyleSheet(u"QTabWidget::pane {\n"
"        background-color: black;\n"
"    }rgb(0, 0, 0)")
        self.scrollArea_2 = QScrollArea(self.tab)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setGeometry(QRect(0, -1, 761, 191))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 747, 625))
        self.verticalLayout_8 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalSpacer_176 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_30.addItem(self.horizontalSpacer_176)

        self.label_formula = QLabel(self.scrollAreaWidgetContents_2)
        self.label_formula.setObjectName(u"label_formula")
        self.label_formula.setFont(font)

        self.horizontalLayout_30.addWidget(self.label_formula, 0, Qt.AlignmentFlag.AlignLeft)

        self.label_formulaBar = QLabel(self.scrollAreaWidgetContents_2)
        self.label_formulaBar.setObjectName(u"label_formulaBar")
        self.label_formulaBar.setMinimumSize(QSize(400, 0))
        self.label_formulaBar.setFont(font)

        self.horizontalLayout_30.addWidget(self.label_formulaBar)

        self.horizontalSpacer_174 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_30.addItem(self.horizontalSpacer_174)

        self.button_setFormulaSettings = QPushButton(self.scrollAreaWidgetContents_2)
        self.button_setFormulaSettings.setObjectName(u"button_setFormulaSettings")
        sizePolicy.setHeightForWidth(self.button_setFormulaSettings.sizePolicy().hasHeightForWidth())
        self.button_setFormulaSettings.setSizePolicy(sizePolicy)
        self.button_setFormulaSettings.setFont(font)

        self.horizontalLayout_30.addWidget(self.button_setFormulaSettings)

        self.horizontalSpacer_175 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_30.addItem(self.horizontalSpacer_175)


        self.verticalLayout_8.addLayout(self.horizontalLayout_30)

        self.horizontalLayout_159 = QHBoxLayout()
        self.horizontalLayout_159.setObjectName(u"horizontalLayout_159")
        self.label_masterType = QLabel(self.scrollAreaWidgetContents_2)
        self.label_masterType.setObjectName(u"label_masterType")
        self.label_masterType.setFont(font)

        self.horizontalLayout_159.addWidget(self.label_masterType, 0, Qt.AlignmentFlag.AlignRight)

        self.comboBox_masterType = QComboBox(self.scrollAreaWidgetContents_2)
        self.comboBox_masterType.addItem("")
        self.comboBox_masterType.addItem("")
        self.comboBox_masterType.setObjectName(u"comboBox_masterType")
        self.comboBox_masterType.setMinimumSize(QSize(150, 0))
        self.comboBox_masterType.setFont(font)

        self.horizontalLayout_159.addWidget(self.comboBox_masterType, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_8.addLayout(self.horizontalLayout_159)

        self.horizontalLayout_122 = QHBoxLayout()
        self.horizontalLayout_122.setObjectName(u"horizontalLayout_122")
        self.label_masterLower = QLabel(self.scrollAreaWidgetContents_2)
        self.label_masterLower.setObjectName(u"label_masterLower")
        self.label_masterLower.setFont(font)

        self.horizontalLayout_122.addWidget(self.label_masterLower, 0, Qt.AlignmentFlag.AlignRight)

        self.lineEdit_masterLower = QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_masterLower.setObjectName(u"lineEdit_masterLower")
        self.lineEdit_masterLower.setFont(font)

        self.horizontalLayout_122.addWidget(self.lineEdit_masterLower, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_8.addLayout(self.horizontalLayout_122)

        self.horizontalLayout_132 = QHBoxLayout()
        self.horizontalLayout_132.setObjectName(u"horizontalLayout_132")
        self.label_master = QLabel(self.scrollAreaWidgetContents_2)
        self.label_master.setObjectName(u"label_master")
        self.label_master.setFont(font)

        self.horizontalLayout_132.addWidget(self.label_master, 0, Qt.AlignmentFlag.AlignRight)

        self.lineEdit_master = QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_master.setObjectName(u"lineEdit_master")
        self.lineEdit_master.setFont(font)

        self.horizontalLayout_132.addWidget(self.lineEdit_master, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_8.addLayout(self.horizontalLayout_132)

        self.horizontalLayout_123 = QHBoxLayout()
        self.horizontalLayout_123.setObjectName(u"horizontalLayout_123")
        self.label_masterHigher = QLabel(self.scrollAreaWidgetContents_2)
        self.label_masterHigher.setObjectName(u"label_masterHigher")
        self.label_masterHigher.setFont(font)

        self.horizontalLayout_123.addWidget(self.label_masterHigher, 0, Qt.AlignmentFlag.AlignRight)

        self.lineEdit_masterHigher = QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_masterHigher.setObjectName(u"lineEdit_masterHigher")
        self.lineEdit_masterHigher.setFont(font)

        self.horizontalLayout_123.addWidget(self.lineEdit_masterHigher, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_8.addLayout(self.horizontalLayout_123)

        self.horizontalLayout_157 = QHBoxLayout()
        self.horizontalLayout_157.setObjectName(u"horizontalLayout_157")
        self.label_upperOffsetLimit = QLabel(self.scrollAreaWidgetContents_2)
        self.label_upperOffsetLimit.setObjectName(u"label_upperOffsetLimit")
        self.label_upperOffsetLimit.setFont(font)

        self.horizontalLayout_157.addWidget(self.label_upperOffsetLimit, 0, Qt.AlignmentFlag.AlignRight)

        self.lineEdit_upperOffcetLimit = QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_upperOffcetLimit.setObjectName(u"lineEdit_upperOffcetLimit")
        self.lineEdit_upperOffcetLimit.setFont(font)

        self.horizontalLayout_157.addWidget(self.lineEdit_upperOffcetLimit, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_8.addLayout(self.horizontalLayout_157)

        self.horizontalLayout_130 = QHBoxLayout()
        self.horizontalLayout_130.setObjectName(u"horizontalLayout_130")
        self.label_usl = QLabel(self.scrollAreaWidgetContents_2)
        self.label_usl.setObjectName(u"label_usl")
        self.label_usl.setFont(font)

        self.horizontalLayout_130.addWidget(self.label_usl, 0, Qt.AlignmentFlag.AlignRight)

        self.lineEdit_usl = QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_usl.setObjectName(u"lineEdit_usl")
        self.lineEdit_usl.setFont(font)

        self.horizontalLayout_130.addWidget(self.lineEdit_usl, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_8.addLayout(self.horizontalLayout_130)

        self.horizontalLayout_134 = QHBoxLayout()
        self.horizontalLayout_134.setObjectName(u"horizontalLayout_134")
        self.label_ucl = QLabel(self.scrollAreaWidgetContents_2)
        self.label_ucl.setObjectName(u"label_ucl")
        self.label_ucl.setFont(font)

        self.horizontalLayout_134.addWidget(self.label_ucl, 0, Qt.AlignmentFlag.AlignRight)

        self.lineEdit_ucl = QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_ucl.setObjectName(u"lineEdit_ucl")
        self.lineEdit_ucl.setFont(font)

        self.horizontalLayout_134.addWidget(self.lineEdit_ucl, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_8.addLayout(self.horizontalLayout_134)

        self.horizontalLayout_128 = QHBoxLayout()
        self.horizontalLayout_128.setObjectName(u"horizontalLayout_128")
        self.label_nominalValue = QLabel(self.scrollAreaWidgetContents_2)
        self.label_nominalValue.setObjectName(u"label_nominalValue")
        self.label_nominalValue.setFont(font)

        self.horizontalLayout_128.addWidget(self.label_nominalValue, 0, Qt.AlignmentFlag.AlignRight)

        self.lineEdit_nominalValue = QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_nominalValue.setObjectName(u"lineEdit_nominalValue")
        self.lineEdit_nominalValue.setFont(font)

        self.horizontalLayout_128.addWidget(self.lineEdit_nominalValue, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_8.addLayout(self.horizontalLayout_128)

        self.horizontalLayout_136 = QHBoxLayout()
        self.horizontalLayout_136.setObjectName(u"horizontalLayout_136")
        self.label_lcl = QLabel(self.scrollAreaWidgetContents_2)
        self.label_lcl.setObjectName(u"label_lcl")
        self.label_lcl.setFont(font)

        self.horizontalLayout_136.addWidget(self.label_lcl, 0, Qt.AlignmentFlag.AlignRight)

        self.lineEdit_lcl = QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_lcl.setObjectName(u"lineEdit_lcl")
        self.lineEdit_lcl.setFont(font)

        self.horizontalLayout_136.addWidget(self.lineEdit_lcl, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_8.addLayout(self.horizontalLayout_136)

        self.horizontalLayout_124 = QHBoxLayout()
        self.horizontalLayout_124.setObjectName(u"horizontalLayout_124")
        self.label_lsl = QLabel(self.scrollAreaWidgetContents_2)
        self.label_lsl.setObjectName(u"label_lsl")
        self.label_lsl.setFont(font)

        self.horizontalLayout_124.addWidget(self.label_lsl, 0, Qt.AlignmentFlag.AlignRight)

        self.lineEdit_lsl = QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_lsl.setObjectName(u"lineEdit_lsl")
        self.lineEdit_lsl.setFont(font)

        self.horizontalLayout_124.addWidget(self.lineEdit_lsl, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_8.addLayout(self.horizontalLayout_124)

        self.horizontalLayout_158 = QHBoxLayout()
        self.horizontalLayout_158.setObjectName(u"horizontalLayout_158")
        self.label_lowerOffsetLimit = QLabel(self.scrollAreaWidgetContents_2)
        self.label_lowerOffsetLimit.setObjectName(u"label_lowerOffsetLimit")
        self.label_lowerOffsetLimit.setFont(font)

        self.horizontalLayout_158.addWidget(self.label_lowerOffsetLimit, 0, Qt.AlignmentFlag.AlignRight)

        self.lineEdit_lowerOffsetLimit = QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_lowerOffsetLimit.setObjectName(u"lineEdit_lowerOffsetLimit")
        self.lineEdit_lowerOffsetLimit.setFont(font)

        self.horizontalLayout_158.addWidget(self.lineEdit_lowerOffsetLimit, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_8.addLayout(self.horizontalLayout_158)

        self.horizontalLayout_160 = QHBoxLayout()
        self.horizontalLayout_160.setObjectName(u"horizontalLayout_160")
        self.label_ovality = QLabel(self.scrollAreaWidgetContents_2)
        self.label_ovality.setObjectName(u"label_ovality")
        self.label_ovality.setFont(font)

        self.horizontalLayout_160.addWidget(self.label_ovality, 0, Qt.AlignmentFlag.AlignRight)

        self.comboBox_ovalityOnOff = QComboBox(self.scrollAreaWidgetContents_2)
        self.comboBox_ovalityOnOff.addItem("")
        self.comboBox_ovalityOnOff.addItem("")
        self.comboBox_ovalityOnOff.setObjectName(u"comboBox_ovalityOnOff")
        self.comboBox_ovalityOnOff.setMinimumSize(QSize(150, 0))
        self.comboBox_ovalityOnOff.setFont(font)

        self.horizontalLayout_160.addWidget(self.comboBox_ovalityOnOff, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_8.addLayout(self.horizontalLayout_160)

        self.horizontalLayout_120 = QHBoxLayout()
        self.horizontalLayout_120.setObjectName(u"horizontalLayout_120")
        self.label_range = QLabel(self.scrollAreaWidgetContents_2)
        self.label_range.setObjectName(u"label_range")
        self.label_range.setFont(font)

        self.horizontalLayout_120.addWidget(self.label_range, 0, Qt.AlignmentFlag.AlignRight)

        self.comboBox_2 = QComboBox(self.scrollAreaWidgetContents_2)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setMinimumSize(QSize(150, 0))
        self.comboBox_2.setFont(font)

        self.horizontalLayout_120.addWidget(self.comboBox_2, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_8.addLayout(self.horizontalLayout_120)

        self.horizontalLayout_131 = QHBoxLayout()
        self.horizontalLayout_131.setObjectName(u"horizontalLayout_131")
        self.label_method = QLabel(self.scrollAreaWidgetContents_2)
        self.label_method.setObjectName(u"label_method")
        self.label_method.setFont(font)

        self.horizontalLayout_131.addWidget(self.label_method, 0, Qt.AlignmentFlag.AlignRight)

        self.comboBox_3 = QComboBox(self.scrollAreaWidgetContents_2)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setMinimumSize(QSize(150, 0))
        self.comboBox_3.setFont(font)

        self.horizontalLayout_131.addWidget(self.comboBox_3, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_8.addLayout(self.horizontalLayout_131)

        self.horizontalLayout_121 = QHBoxLayout()
        self.horizontalLayout_121.setObjectName(u"horizontalLayout_121")
        self.label_case = QLabel(self.scrollAreaWidgetContents_2)
        self.label_case.setObjectName(u"label_case")
        self.label_case.setFont(font)

        self.horizontalLayout_121.addWidget(self.label_case, 0, Qt.AlignmentFlag.AlignRight)

        self.comboBox_4 = QComboBox(self.scrollAreaWidgetContents_2)
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName(u"comboBox_4")
        self.comboBox_4.setMinimumSize(QSize(150, 0))
        self.comboBox_4.setFont(font)

        self.horizontalLayout_121.addWidget(self.comboBox_4, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_8.addLayout(self.horizontalLayout_121)

        self.horizontalLayout_119 = QHBoxLayout()
        self.horizontalLayout_119.setObjectName(u"horizontalLayout_119")
        self.label_caseT = QLabel(self.scrollAreaWidgetContents_2)
        self.label_caseT.setObjectName(u"label_caseT")
        self.label_caseT.setFont(font)

        self.horizontalLayout_119.addWidget(self.label_caseT, 0, Qt.AlignmentFlag.AlignRight)

        self.lineEdit_caseT = QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_caseT.setObjectName(u"lineEdit_caseT")
        self.lineEdit_caseT.setFont(font)

        self.horizontalLayout_119.addWidget(self.lineEdit_caseT, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_8.addLayout(self.horizontalLayout_119)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.scrollArea = QScrollArea(self.tab_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(0, 0, 761, 201))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 747, 228))
        self.verticalLayout_7 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_147 = QHBoxLayout()
        self.horizontalLayout_147.setObjectName(u"horizontalLayout_147")
        self.label_axis = QLabel(self.scrollAreaWidgetContents)
        self.label_axis.setObjectName(u"label_axis")
        self.label_axis.setFont(font)

        self.horizontalLayout_147.addWidget(self.label_axis, 0, Qt.AlignmentFlag.AlignRight)

        self.comboBox_axis = QComboBox(self.scrollAreaWidgetContents)
        self.comboBox_axis.addItem("")
        self.comboBox_axis.addItem("")
        self.comboBox_axis.addItem("")
        self.comboBox_axis.setObjectName(u"comboBox_axis")
        self.comboBox_axis.setMinimumSize(QSize(150, 0))
        self.comboBox_axis.setFont(font)

        self.horizontalLayout_147.addWidget(self.comboBox_axis, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_7.addLayout(self.horizontalLayout_147)

        self.horizontalLayout_146 = QHBoxLayout()
        self.horizontalLayout_146.setObjectName(u"horizontalLayout_146")
        self.label_offsetNo = QLabel(self.scrollAreaWidgetContents)
        self.label_offsetNo.setObjectName(u"label_offsetNo")
        self.label_offsetNo.setFont(font)

        self.horizontalLayout_146.addWidget(self.label_offsetNo, 0, Qt.AlignmentFlag.AlignRight)

        self.lineEdit_offsetNo = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_offsetNo.setObjectName(u"lineEdit_offsetNo")
        self.lineEdit_offsetNo.setFont(font)

        self.horizontalLayout_146.addWidget(self.lineEdit_offsetNo, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_7.addLayout(self.horizontalLayout_146)

        self.horizontalLayout_144 = QHBoxLayout()
        self.horizontalLayout_144.setObjectName(u"horizontalLayout_144")
        self.label_machine = QLabel(self.scrollAreaWidgetContents)
        self.label_machine.setObjectName(u"label_machine")
        self.label_machine.setFont(font)

        self.horizontalLayout_144.addWidget(self.label_machine, 0, Qt.AlignmentFlag.AlignRight)

        self.comboBox_machine = QComboBox(self.scrollAreaWidgetContents)
        self.comboBox_machine.setObjectName(u"comboBox_machine")
        self.comboBox_machine.setMinimumSize(QSize(150, 0))
        self.comboBox_machine.setFont(font)

        self.horizontalLayout_144.addWidget(self.comboBox_machine, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_7.addLayout(self.horizontalLayout_144)

        self.horizontalLayout_148 = QHBoxLayout()
        self.horizontalLayout_148.setObjectName(u"horizontalLayout_148")
        self.label_direction = QLabel(self.scrollAreaWidgetContents)
        self.label_direction.setObjectName(u"label_direction")
        self.label_direction.setFont(font)

        self.horizontalLayout_148.addWidget(self.label_direction, 0, Qt.AlignmentFlag.AlignRight)

        self.comboBox_direction = QComboBox(self.scrollAreaWidgetContents)
        self.comboBox_direction.addItem("")
        self.comboBox_direction.addItem("")
        self.comboBox_direction.setObjectName(u"comboBox_direction")
        self.comboBox_direction.setMinimumSize(QSize(150, 0))
        self.comboBox_direction.setFont(font)

        self.horizontalLayout_148.addWidget(self.comboBox_direction, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_7.addLayout(self.horizontalLayout_148)

        self.horizontalLayout_156 = QHBoxLayout()
        self.horizontalLayout_156.setObjectName(u"horizontalLayout_156")
        self.label_setPath = QLabel(self.scrollAreaWidgetContents)
        self.label_setPath.setObjectName(u"label_setPath")
        self.label_setPath.setFont(font)

        self.horizontalLayout_156.addWidget(self.label_setPath, 0, Qt.AlignmentFlag.AlignRight)

        self.lineEdit_setPath = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_setPath.setObjectName(u"lineEdit_setPath")
        self.lineEdit_setPath.setFont(font)

        self.horizontalLayout_156.addWidget(self.lineEdit_setPath, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_7.addLayout(self.horizontalLayout_156)

        self.horizontalLayout_139 = QHBoxLayout()
        self.horizontalLayout_139.setObjectName(u"horizontalLayout_139")
        self.label_buzzerAoc = QLabel(self.scrollAreaWidgetContents)
        self.label_buzzerAoc.setObjectName(u"label_buzzerAoc")
        self.label_buzzerAoc.setFont(font)

        self.horizontalLayout_139.addWidget(self.label_buzzerAoc, 0, Qt.AlignmentFlag.AlignRight)

        self.lineEdit_buzzerval = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_buzzerval.setObjectName(u"lineEdit_buzzerval")
        self.lineEdit_buzzerval.setFont(font)

        self.horizontalLayout_139.addWidget(self.lineEdit_buzzerval, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_7.addLayout(self.horizontalLayout_139)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.tabWidget.addTab(self.tab_2, "")

        self.page18Layout.addWidget(self.tabWidget)

        self.stackedWidget_main.addWidget(self.page18)
        self.page19 = QWidget()
        self.page19.setObjectName(u"page19")
        self.page19Layout = QVBoxLayout(self.page19)
        self.page19Layout.setObjectName(u"page19Layout")
        self.horizontalLayout_85 = QHBoxLayout()
        self.horizontalLayout_85.setObjectName(u"horizontalLayout_85")
        self.horizontalSpacer_29 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_85.addItem(self.horizontalSpacer_29)

        self.label_fromDate = QLabel(self.page19)
        self.label_fromDate.setObjectName(u"label_fromDate")
        self.label_fromDate.setFont(font)

        self.horizontalLayout_85.addWidget(self.label_fromDate)

        self.button_fromDate = QPushButton(self.page19)
        self.button_fromDate.setObjectName(u"button_fromDate")
        sizePolicy.setHeightForWidth(self.button_fromDate.sizePolicy().hasHeightForWidth())
        self.button_fromDate.setSizePolicy(sizePolicy)
        self.button_fromDate.setFont(font)

        self.horizontalLayout_85.addWidget(self.button_fromDate)

        self.horizontalSpacer_32 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_85.addItem(self.horizontalSpacer_32)

        self.label_toDate = QLabel(self.page19)
        self.label_toDate.setObjectName(u"label_toDate")
        self.label_toDate.setFont(font)

        self.horizontalLayout_85.addWidget(self.label_toDate)

        self.button_toDate = QPushButton(self.page19)
        self.button_toDate.setObjectName(u"button_toDate")
        sizePolicy.setHeightForWidth(self.button_toDate.sizePolicy().hasHeightForWidth())
        self.button_toDate.setSizePolicy(sizePolicy)
        self.button_toDate.setFont(font)

        self.horizontalLayout_85.addWidget(self.button_toDate)

        self.horizontalSpacer_31 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_85.addItem(self.horizontalSpacer_31)

        self.button_export = QPushButton(self.page19)
        self.button_export.setObjectName(u"button_export")
        self.button_export.setFont(font)

        self.horizontalLayout_85.addWidget(self.button_export)

        self.horizontalSpacer_30 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_85.addItem(self.horizontalSpacer_30)


        self.page19Layout.addLayout(self.horizontalLayout_85)

        self.line_22 = QFrame(self.page19)
        self.line_22.setObjectName(u"line_22")
        self.line_22.setFrameShape(QFrame.Shape.HLine)
        self.line_22.setFrameShadow(QFrame.Shadow.Sunken)

        self.page19Layout.addWidget(self.line_22)

        self.horizontalLayout_86 = QHBoxLayout()
        self.horizontalLayout_86.setObjectName(u"horizontalLayout_86")
        self.horizontalSpacer_33 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_86.addItem(self.horizontalSpacer_33)

        self.label_22 = QLabel(self.page19)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font)

        self.horizontalLayout_86.addWidget(self.label_22)

        self.lineEdit_spcDataCount = QLineEdit(self.page19)
        self.lineEdit_spcDataCount.setObjectName(u"lineEdit_spcDataCount")
        sizePolicy.setHeightForWidth(self.lineEdit_spcDataCount.sizePolicy().hasHeightForWidth())
        self.lineEdit_spcDataCount.setSizePolicy(sizePolicy)
        self.lineEdit_spcDataCount.setMinimumSize(QSize(0, 0))
        self.lineEdit_spcDataCount.setMaximumSize(QSize(75, 16777215))
        self.lineEdit_spcDataCount.setFont(font)

        self.horizontalLayout_86.addWidget(self.lineEdit_spcDataCount, 0, Qt.AlignmentFlag.AlignLeft)

        self.horizontalSpacer_34 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_86.addItem(self.horizontalSpacer_34)

        self.button_spcDataCount = QPushButton(self.page19)
        self.button_spcDataCount.setObjectName(u"button_spcDataCount")
        sizePolicy.setHeightForWidth(self.button_spcDataCount.sizePolicy().hasHeightForWidth())
        self.button_spcDataCount.setSizePolicy(sizePolicy)
        self.button_spcDataCount.setFont(font)

        self.horizontalLayout_86.addWidget(self.button_spcDataCount)

        self.horizontalSpacer_35 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_86.addItem(self.horizontalSpacer_35)


        self.page19Layout.addLayout(self.horizontalLayout_86)

        self.stackedWidget_main.addWidget(self.page19)
        self.page20 = QWidget()
        self.page20.setObjectName(u"page20")
        self.page20Layout = QVBoxLayout(self.page20)
        self.page20Layout.setObjectName(u"page20Layout")
        self.horizontalLayout_87 = QHBoxLayout()
        self.horizontalLayout_87.setObjectName(u"horizontalLayout_87")
        self.label_25 = QLabel(self.page20)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font)

        self.horizontalLayout_87.addWidget(self.label_25, 0, Qt.AlignmentFlag.AlignRight)

        self.comboBox_probeCalibrate = QComboBox(self.page20)
        self.comboBox_probeCalibrate.addItem("")
        self.comboBox_probeCalibrate.addItem("")
        self.comboBox_probeCalibrate.setObjectName(u"comboBox_probeCalibrate")
        self.comboBox_probeCalibrate.setFont(font)

        self.horizontalLayout_87.addWidget(self.comboBox_probeCalibrate, 0, Qt.AlignmentFlag.AlignLeft)


        self.page20Layout.addLayout(self.horizontalLayout_87)

        self.line_23 = QFrame(self.page20)
        self.line_23.setObjectName(u"line_23")
        self.line_23.setFrameShape(QFrame.Shape.HLine)
        self.line_23.setFrameShadow(QFrame.Shadow.Sunken)

        self.page20Layout.addWidget(self.line_23)

        self.horizontalLayout_88 = QHBoxLayout()
        self.horizontalLayout_88.setObjectName(u"horizontalLayout_88")
        self.horizontalSpacer_37 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_88.addItem(self.horizontalSpacer_37)

        self.label_lowerMasterCalibrate = QLabel(self.page20)
        self.label_lowerMasterCalibrate.setObjectName(u"label_lowerMasterCalibrate")
        self.label_lowerMasterCalibrate.setFont(font)

        self.horizontalLayout_88.addWidget(self.label_lowerMasterCalibrate)

        self.lineEdit_lowerMasterCalibrate = QLineEdit(self.page20)
        self.lineEdit_lowerMasterCalibrate.setObjectName(u"lineEdit_lowerMasterCalibrate")
        sizePolicy.setHeightForWidth(self.lineEdit_lowerMasterCalibrate.sizePolicy().hasHeightForWidth())
        self.lineEdit_lowerMasterCalibrate.setSizePolicy(sizePolicy)
        self.lineEdit_lowerMasterCalibrate.setFont(font)

        self.horizontalLayout_88.addWidget(self.lineEdit_lowerMasterCalibrate)

        self.horizontalSpacer_36 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_88.addItem(self.horizontalSpacer_36)

        self.label_higherMasterCalibrate = QLabel(self.page20)
        self.label_higherMasterCalibrate.setObjectName(u"label_higherMasterCalibrate")
        self.label_higherMasterCalibrate.setFont(font)

        self.horizontalLayout_88.addWidget(self.label_higherMasterCalibrate)

        self.lineEdit_higherMasterCalibrate = QLineEdit(self.page20)
        self.lineEdit_higherMasterCalibrate.setObjectName(u"lineEdit_higherMasterCalibrate")
        sizePolicy.setHeightForWidth(self.lineEdit_higherMasterCalibrate.sizePolicy().hasHeightForWidth())
        self.lineEdit_higherMasterCalibrate.setSizePolicy(sizePolicy)
        self.lineEdit_higherMasterCalibrate.setFont(font)

        self.horizontalLayout_88.addWidget(self.lineEdit_higherMasterCalibrate)

        self.horizontalSpacer_38 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_88.addItem(self.horizontalSpacer_38)


        self.page20Layout.addLayout(self.horizontalLayout_88)

        self.horizontalLayout_89 = QHBoxLayout()
        self.horizontalLayout_89.setObjectName(u"horizontalLayout_89")
        self.button_calibrateLower = QPushButton(self.page20)
        self.button_calibrateLower.setObjectName(u"button_calibrateLower")
        sizePolicy.setHeightForWidth(self.button_calibrateLower.sizePolicy().hasHeightForWidth())
        self.button_calibrateLower.setSizePolicy(sizePolicy)
        self.button_calibrateLower.setFont(font)

        self.horizontalLayout_89.addWidget(self.button_calibrateLower, 0, Qt.AlignmentFlag.AlignHCenter)

        self.button_calibrateHigher = QPushButton(self.page20)
        self.button_calibrateHigher.setObjectName(u"button_calibrateHigher")
        sizePolicy.setHeightForWidth(self.button_calibrateHigher.sizePolicy().hasHeightForWidth())
        self.button_calibrateHigher.setSizePolicy(sizePolicy)
        self.button_calibrateHigher.setFont(font)

        self.horizontalLayout_89.addWidget(self.button_calibrateHigher, 0, Qt.AlignmentFlag.AlignHCenter)


        self.page20Layout.addLayout(self.horizontalLayout_89)

        self.line_24 = QFrame(self.page20)
        self.line_24.setObjectName(u"line_24")
        self.line_24.setFrameShape(QFrame.Shape.HLine)
        self.line_24.setFrameShadow(QFrame.Shadow.Sunken)

        self.page20Layout.addWidget(self.line_24)

        self.horizontalLayout_90 = QHBoxLayout()
        self.horizontalLayout_90.setObjectName(u"horizontalLayout_90")
        self.horizontalSpacer_40 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_90.addItem(self.horizontalSpacer_40)

        self.button_setToFactorySettingsCalibration = QPushButton(self.page20)
        self.button_setToFactorySettingsCalibration.setObjectName(u"button_setToFactorySettingsCalibration")
        sizePolicy.setHeightForWidth(self.button_setToFactorySettingsCalibration.sizePolicy().hasHeightForWidth())
        self.button_setToFactorySettingsCalibration.setSizePolicy(sizePolicy)
        self.button_setToFactorySettingsCalibration.setFont(font)

        self.horizontalLayout_90.addWidget(self.button_setToFactorySettingsCalibration, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalSpacer_41 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_90.addItem(self.horizontalSpacer_41)

        self.button_resetToFactorySettingsCalibration = QPushButton(self.page20)
        self.button_resetToFactorySettingsCalibration.setObjectName(u"button_resetToFactorySettingsCalibration")
        sizePolicy.setHeightForWidth(self.button_resetToFactorySettingsCalibration.sizePolicy().hasHeightForWidth())
        self.button_resetToFactorySettingsCalibration.setSizePolicy(sizePolicy)
        self.button_resetToFactorySettingsCalibration.setFont(font)

        self.horizontalLayout_90.addWidget(self.button_resetToFactorySettingsCalibration, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalSpacer_39 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_90.addItem(self.horizontalSpacer_39)


        self.page20Layout.addLayout(self.horizontalLayout_90)

        self.stackedWidget_main.addWidget(self.page20)
        self.page21 = QWidget()
        self.page21.setObjectName(u"page21")
        self.page21Layout = QVBoxLayout(self.page21)
        self.page21Layout.setObjectName(u"page21Layout")
        self.verticalSpacer_35 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.page21Layout.addItem(self.verticalSpacer_35)

        self.horizontalLayout_91 = QHBoxLayout()
        self.horizontalLayout_91.setObjectName(u"horizontalLayout_91")
        self.horizontalSpacer_42 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_91.addItem(self.horizontalSpacer_42)

        self.label_airSavingMode = QLabel(self.page21)
        self.label_airSavingMode.setObjectName(u"label_airSavingMode")
        self.label_airSavingMode.setFont(font)

        self.horizontalLayout_91.addWidget(self.label_airSavingMode)

        self.toggleButton_airSavingMode = QLabel(self.page21)
        self.toggleButton_airSavingMode.setObjectName(u"toggleButton_airSavingMode")

        image_path = os.path.join(script_dir, "Switcher_On.png")  # if it's in the same folder
        self.toggleButton_airSavingMode.setPixmap(QPixmap(image_path))

        self.horizontalLayout_91.addWidget(self.toggleButton_airSavingMode)

        self.label_airSavingModeOnOff = QLabel(self.page21)
        self.label_airSavingModeOnOff.setObjectName(u"label_airSavingModeOnOff")
        self.label_airSavingModeOnOff.setFont(font)

        self.horizontalLayout_91.addWidget(self.label_airSavingModeOnOff)

        self.horizontalSpacer_43 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_91.addItem(self.horizontalSpacer_43)


        self.page21Layout.addLayout(self.horizontalLayout_91)

        self.verticalSpacer_36 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.page21Layout.addItem(self.verticalSpacer_36)

        self.line_25 = QFrame(self.page21)
        self.line_25.setObjectName(u"line_25")
        self.line_25.setFrameShape(QFrame.Shape.HLine)
        self.line_25.setFrameShadow(QFrame.Shadow.Sunken)

        self.page21Layout.addWidget(self.line_25)

        self.verticalSpacer_37 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.page21Layout.addItem(self.verticalSpacer_37)

        self.horizontalLayout_92 = QHBoxLayout()
        self.horizontalLayout_92.setObjectName(u"horizontalLayout_92")
        self.label_airChannel = QLabel(self.page21)
        self.label_airChannel.setObjectName(u"label_airChannel")
        self.label_airChannel.setFont(font)

        self.horizontalLayout_92.addWidget(self.label_airChannel, 0, Qt.AlignmentFlag.AlignRight)

        self.comboBox_airChannel = QComboBox(self.page21)
        self.comboBox_airChannel.addItem("")
        self.comboBox_airChannel.addItem("")
        self.comboBox_airChannel.setObjectName(u"comboBox_airChannel")
        self.comboBox_airChannel.setFont(font)

        self.horizontalLayout_92.addWidget(self.comboBox_airChannel, 0, Qt.AlignmentFlag.AlignLeft)


        self.page21Layout.addLayout(self.horizontalLayout_92)

        self.verticalSpacer_39 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.page21Layout.addItem(self.verticalSpacer_39)

        self.horizontalLayout_93 = QHBoxLayout()
        self.horizontalLayout_93.setObjectName(u"horizontalLayout_93")
        self.horizontalSpacer_44 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_93.addItem(self.horizontalSpacer_44)

        self.label_airSensesitivityQuotient = QLabel(self.page21)
        self.label_airSensesitivityQuotient.setObjectName(u"label_airSensesitivityQuotient")
        self.label_airSensesitivityQuotient.setFont(font)

        self.horizontalLayout_93.addWidget(self.label_airSensesitivityQuotient, 0, Qt.AlignmentFlag.AlignRight)

        self.lineEdit_airSensesitivityQuotient = QLineEdit(self.page21)
        self.lineEdit_airSensesitivityQuotient.setObjectName(u"lineEdit_airSensesitivityQuotient")
        sizePolicy.setHeightForWidth(self.lineEdit_airSensesitivityQuotient.sizePolicy().hasHeightForWidth())
        self.lineEdit_airSensesitivityQuotient.setSizePolicy(sizePolicy)
        self.lineEdit_airSensesitivityQuotient.setMinimumSize(QSize(0, 0))
        self.lineEdit_airSensesitivityQuotient.setMaximumSize(QSize(100, 16777215))
        self.lineEdit_airSensesitivityQuotient.setFont(font)

        self.horizontalLayout_93.addWidget(self.lineEdit_airSensesitivityQuotient, 0, Qt.AlignmentFlag.AlignLeft)

        self.horizontalSpacer_45 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_93.addItem(self.horizontalSpacer_45)


        self.page21Layout.addLayout(self.horizontalLayout_93)

        self.verticalSpacer_38 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.page21Layout.addItem(self.verticalSpacer_38)

        self.horizontalLayout_95 = QHBoxLayout()
        self.horizontalLayout_95.setObjectName(u"horizontalLayout_95")
        self.button_setAirSensitivity = QPushButton(self.page21)
        self.button_setAirSensitivity.setObjectName(u"button_setAirSensitivity")
        sizePolicy.setHeightForWidth(self.button_setAirSensitivity.sizePolicy().hasHeightForWidth())
        self.button_setAirSensitivity.setSizePolicy(sizePolicy)
        self.button_setAirSensitivity.setFont(font)

        self.horizontalLayout_95.addWidget(self.button_setAirSensitivity, 0, Qt.AlignmentFlag.AlignHCenter)


        self.page21Layout.addLayout(self.horizontalLayout_95)

        self.stackedWidget_main.addWidget(self.page21)
        self.page22 = QWidget()
        self.page22.setObjectName(u"page22")
        self.page22Layout = QVBoxLayout(self.page22)
        self.page22Layout.setObjectName(u"page22Layout")
        self.horizontalLayout_101 = QHBoxLayout()
        self.horizontalLayout_101.setObjectName(u"horizontalLayout_101")
        self.horizontalSpacer_74 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_101.addItem(self.horizontalSpacer_74)

        self.label_ReportfromDate = QLabel(self.page22)
        self.label_ReportfromDate.setObjectName(u"label_ReportfromDate")
        self.label_ReportfromDate.setFont(font)

        self.horizontalLayout_101.addWidget(self.label_ReportfromDate)

        self.label_ReportfromDateVal = QLabel(self.page22)
        self.label_ReportfromDateVal.setObjectName(u"label_ReportfromDateVal")
        self.label_ReportfromDateVal.setFont(font)

        self.horizontalLayout_101.addWidget(self.label_ReportfromDateVal, 0, Qt.AlignmentFlag.AlignRight)

        self.pushButton_selectFromDate = QPushButton(self.page22)
        self.pushButton_selectFromDate.setObjectName(u"pushButton_selectFromDate")
        sizePolicy.setHeightForWidth(self.pushButton_selectFromDate.sizePolicy().hasHeightForWidth())
        self.pushButton_selectFromDate.setSizePolicy(sizePolicy)
        self.pushButton_selectFromDate.setFont(font)

        self.horizontalLayout_101.addWidget(self.pushButton_selectFromDate)

        self.horizontalSpacer_72 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_101.addItem(self.horizontalSpacer_72)

        self.label_ReportToDate = QLabel(self.page22)
        self.label_ReportToDate.setObjectName(u"label_ReportToDate")
        self.label_ReportToDate.setFont(font)

        self.horizontalLayout_101.addWidget(self.label_ReportToDate)

        self.label_ReportToDateVal = QLabel(self.page22)
        self.label_ReportToDateVal.setObjectName(u"label_ReportToDateVal")
        self.label_ReportToDateVal.setFont(font)

        self.horizontalLayout_101.addWidget(self.label_ReportToDateVal)

        self.pushButton_SelectToDate = QPushButton(self.page22)
        self.pushButton_SelectToDate.setObjectName(u"pushButton_SelectToDate")
        sizePolicy.setHeightForWidth(self.pushButton_SelectToDate.sizePolicy().hasHeightForWidth())
        self.pushButton_SelectToDate.setSizePolicy(sizePolicy)
        self.pushButton_SelectToDate.setFont(font)

        self.horizontalLayout_101.addWidget(self.pushButton_SelectToDate)

        self.horizontalSpacer_73 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_101.addItem(self.horizontalSpacer_73)


        self.page22Layout.addLayout(self.horizontalLayout_101)

        self.line_51 = QFrame(self.page22)
        self.line_51.setObjectName(u"line_51")
        self.line_51.setFrameShape(QFrame.Shape.HLine)
        self.line_51.setFrameShadow(QFrame.Shadow.Sunken)

        self.page22Layout.addWidget(self.line_51)

        self.horizontalLayout_104 = QHBoxLayout()
        self.horizontalLayout_104.setObjectName(u"horizontalLayout_104")
        self.horizontalSpacer_76 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_104.addItem(self.horizontalSpacer_76)

        self.label_programId = QLabel(self.page22)
        self.label_programId.setObjectName(u"label_programId")
        self.label_programId.setFont(font)

        self.horizontalLayout_104.addWidget(self.label_programId)

        self.comboBox_programId = QComboBox(self.page22)
        self.comboBox_programId.setObjectName(u"comboBox_programId")
        self.comboBox_programId.setFont(font)

        self.horizontalLayout_104.addWidget(self.comboBox_programId)

        self.horizontalSpacer_75 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_104.addItem(self.horizontalSpacer_75)

        self.label_dimension = QLabel(self.page22)
        self.label_dimension.setObjectName(u"label_dimension")
        self.label_dimension.setFont(font)

        self.horizontalLayout_104.addWidget(self.label_dimension)

        self.comboBox_dimension = QComboBox(self.page22)
        self.comboBox_dimension.setObjectName(u"comboBox_dimension")
        self.comboBox_dimension.setFont(font)

        self.horizontalLayout_104.addWidget(self.comboBox_dimension)

        self.horizontalSpacer_77 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_104.addItem(self.horizontalSpacer_77)


        self.page22Layout.addLayout(self.horizontalLayout_104)

        self.line_57 = QFrame(self.page22)
        self.line_57.setObjectName(u"line_57")
        self.line_57.setFrameShape(QFrame.Shape.HLine)
        self.line_57.setFrameShadow(QFrame.Shadow.Sunken)

        self.page22Layout.addWidget(self.line_57)

        self.horizontalLayout_108 = QHBoxLayout()
        self.horizontalLayout_108.setObjectName(u"horizontalLayout_108")
        self.button_viewData = QPushButton(self.page22)
        self.button_viewData.setObjectName(u"button_viewData")
        sizePolicy.setHeightForWidth(self.button_viewData.sizePolicy().hasHeightForWidth())
        self.button_viewData.setSizePolicy(sizePolicy)
        self.button_viewData.setFont(font)

        self.horizontalLayout_108.addWidget(self.button_viewData, 0, Qt.AlignmentFlag.AlignHCenter)

        self.button_exportData = QPushButton(self.page22)
        self.button_exportData.setObjectName(u"button_exportData")
        sizePolicy.setHeightForWidth(self.button_exportData.sizePolicy().hasHeightForWidth())
        self.button_exportData.setSizePolicy(sizePolicy)
        self.button_exportData.setFont(font)

        self.horizontalLayout_108.addWidget(self.button_exportData, 0, Qt.AlignmentFlag.AlignHCenter)

        self.button_deleteData = QPushButton(self.page22)
        self.button_deleteData.setObjectName(u"button_deleteData")
        sizePolicy.setHeightForWidth(self.button_deleteData.sizePolicy().hasHeightForWidth())
        self.button_deleteData.setSizePolicy(sizePolicy)
        self.button_deleteData.setFont(font)

        self.horizontalLayout_108.addWidget(self.button_deleteData, 0, Qt.AlignmentFlag.AlignHCenter)


        self.page22Layout.addLayout(self.horizontalLayout_108)

        self.stackedWidget_main.addWidget(self.page22)
        self.page23 = QWidget()
        self.page23.setObjectName(u"page23")
        self.page23Layout = QVBoxLayout(self.page23)
        self.page23Layout.setObjectName(u"page23Layout")
        self.horizontalLayout_111 = QHBoxLayout()
        self.horizontalLayout_111.setObjectName(u"horizontalLayout_111")
        self.horizontalSpacer_79 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_111.addItem(self.horizontalSpacer_79)

        self.label_dateselectReport = QLabel(self.page23)
        self.label_dateselectReport.setObjectName(u"label_dateselectReport")
        self.label_dateselectReport.setFont(font)

        self.horizontalLayout_111.addWidget(self.label_dateselectReport)

        self.label_reportshowdate = QLabel(self.page23)
        self.label_reportshowdate.setObjectName(u"label_reportshowdate")
        self.label_reportshowdate.setFont(font)

        self.horizontalLayout_111.addWidget(self.label_reportshowdate, 0, Qt.AlignmentFlag.AlignRight)

        self.horizontalSpacer_78 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_111.addItem(self.horizontalSpacer_78)

        self.label_programIdreport = QLabel(self.page23)
        self.label_programIdreport.setObjectName(u"label_programIdreport")
        self.label_programIdreport.setFont(font)

        self.horizontalLayout_111.addWidget(self.label_programIdreport)

        self.label_IdProgramReport = QLabel(self.page23)
        self.label_IdProgramReport.setObjectName(u"label_IdProgramReport")
        self.label_IdProgramReport.setFont(font)

        self.horizontalLayout_111.addWidget(self.label_IdProgramReport)

        self.horizontalSpacer_81 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_111.addItem(self.horizontalSpacer_81)

        self.label_DimensionForReport = QLabel(self.page23)
        self.label_DimensionForReport.setObjectName(u"label_DimensionForReport")
        self.label_DimensionForReport.setFont(font)

        self.horizontalLayout_111.addWidget(self.label_DimensionForReport)

        self.label_DimensionIdForReport = QLabel(self.page23)
        self.label_DimensionIdForReport.setObjectName(u"label_DimensionIdForReport")
        self.label_DimensionIdForReport.setFont(font)

        self.horizontalLayout_111.addWidget(self.label_DimensionIdForReport)

        self.horizontalSpacer_80 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_111.addItem(self.horizontalSpacer_80)


        self.page23Layout.addLayout(self.horizontalLayout_111)

        self.line_58 = QFrame(self.page23)
        self.line_58.setObjectName(u"line_58")
        self.line_58.setFrameShape(QFrame.Shape.HLine)
        self.line_58.setFrameShadow(QFrame.Shadow.Sunken)

        self.page23Layout.addWidget(self.line_58)

        self.stackedWidget = QStackedWidget(self.page23)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayoutWidget = QWidget(self.page)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 771, 291))
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.verticalLayoutWidget)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout_4.addWidget(self.tableWidget)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayoutWidget_2 = QWidget(self.page_2)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(0, 0, 771, 291))
        self.verticalLayout_5 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.verticalLayoutWidget_2)
        self.widget.setObjectName(u"widget")

        self.verticalLayout_5.addWidget(self.widget)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayoutWidget_3 = QWidget(self.page_3)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(-1, -1, 771, 291))
        self.verticalLayout_6 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.verticalLayoutWidget_3)
        self.widget_2.setObjectName(u"widget_2")

        self.verticalLayout_6.addWidget(self.widget_2)

        self.stackedWidget.addWidget(self.page_3)

        self.page23Layout.addWidget(self.stackedWidget)

        self.line_59 = QFrame(self.page23)
        self.line_59.setObjectName(u"line_59")
        self.line_59.setFrameShape(QFrame.Shape.HLine)
        self.line_59.setFrameShadow(QFrame.Shadow.Sunken)

        self.page23Layout.addWidget(self.line_59)

        self.horizontalLayout_113 = QHBoxLayout()
        self.horizontalLayout_113.setObjectName(u"horizontalLayout_113")
        self.button_ListView = QPushButton(self.page23)
        self.button_ListView.setObjectName(u"button_ListView")
        self.button_ListView.setFont(font)

        self.horizontalLayout_113.addWidget(self.button_ListView, 0, Qt.AlignmentFlag.AlignHCenter)

        self.button_ChartView = QPushButton(self.page23)
        self.button_ChartView.setObjectName(u"button_ChartView")
        self.button_ChartView.setFont(font)

        self.horizontalLayout_113.addWidget(self.button_ChartView, 0, Qt.AlignmentFlag.AlignHCenter)

        self.button_HistogramChart = QPushButton(self.page23)
        self.button_HistogramChart.setObjectName(u"button_HistogramChart")
        self.button_HistogramChart.setFont(font)

        self.horizontalLayout_113.addWidget(self.button_HistogramChart, 0, Qt.AlignmentFlag.AlignHCenter)


        self.page23Layout.addLayout(self.horizontalLayout_113)

        self.stackedWidget_main.addWidget(self.page23)
        self.page24 = QWidget()
        self.page24.setObjectName(u"page24")
        self.page24Layout = QVBoxLayout(self.page24)
        self.page24Layout.setObjectName(u"page24Layout")
        self.verticalSpacer_40 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.page24Layout.addItem(self.verticalSpacer_40)

        self.horizontalLayout_114 = QHBoxLayout()
        self.horizontalLayout_114.setObjectName(u"horizontalLayout_114")
        self.horizontalSpacer_87 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_114.addItem(self.horizontalSpacer_87)

        self.label_dialIndicatorPage = QLabel(self.page24)
        self.label_dialIndicatorPage.setObjectName(u"label_dialIndicatorPage")
        self.label_dialIndicatorPage.setMinimumSize(QSize(130, 130))
        self.label_dialIndicatorPage.setMaximumSize(QSize(16777215, 16777215))

        image_path = os.path.join(script_dir, "indicator.png")  # if it's in the same folder
        self.label_dialIndicatorPage.setPixmap(QPixmap(image_path))

        self.horizontalLayout_114.addWidget(self.label_dialIndicatorPage)

        self.horizontalSpacer_83 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_114.addItem(self.horizontalSpacer_83)

        self.label_settingsPage = QLabel(self.page24)
        self.label_settingsPage.setObjectName(u"label_settingsPage")
        self.label_settingsPage.setMinimumSize(QSize(130, 130))
        self.label_settingsPage.setMaximumSize(QSize(16777215, 16777215))

        image_path = os.path.join(script_dir, "settings.png")
        self.label_settingsPage.setPixmap(QPixmap(image_path))

        self.horizontalLayout_114.addWidget(self.label_settingsPage)

        self.horizontalSpacer_84 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_114.addItem(self.horizontalSpacer_84)

        self.label_ioSettingPage = QLabel(self.page24)
        self.label_ioSettingPage.setObjectName(u"label_ioSettingPage")
        self.label_ioSettingPage.setMinimumSize(QSize(130, 130))
        self.label_ioSettingPage.setMaximumSize(QSize(16777215, 16777215))

        image_path = os.path.join(script_dir, "Buzzer.png")
        self.label_ioSettingPage.setPixmap(QPixmap(image_path))

        self.horizontalLayout_114.addWidget(self.label_ioSettingPage)

        self.horizontalSpacer_85 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_114.addItem(self.horizontalSpacer_85)

        self.label_autoOffsetSettingPage = QLabel(self.page24)
        self.label_autoOffsetSettingPage.setObjectName(u"label_autoOffsetSettingPage")
        self.label_autoOffsetSettingPage.setMinimumSize(QSize(110, 130))
        self.label_autoOffsetSettingPage.setMaximumSize(QSize(16777215, 16777215))

        image_path = os.path.join(script_dir, "autooffset.png")
        self.label_autoOffsetSettingPage.setPixmap(QPixmap(image_path))

        self.horizontalLayout_114.addWidget(self.label_autoOffsetSettingPage)

        self.horizontalSpacer_86 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_114.addItem(self.horizontalSpacer_86)


        self.page24Layout.addLayout(self.horizontalLayout_114)

        self.verticalSpacer_41 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.page24Layout.addItem(self.verticalSpacer_41)

        self.horizontalLayout_112 = QHBoxLayout()
        self.horizontalLayout_112.setObjectName(u"horizontalLayout_112")
        self.horizontalSpacer_88 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_112.addItem(self.horizontalSpacer_88)

        self.label_clockSettingsPage = QLabel(self.page24)
        self.label_clockSettingsPage.setObjectName(u"label_clockSettingsPage")
        self.label_clockSettingsPage.setMinimumSize(QSize(130, 130))
        self.label_clockSettingsPage.setMaximumSize(QSize(16777215, 16777215))

        image_path = os.path.join(script_dir, "clock.png")
        self.label_clockSettingsPage.setPixmap(QPixmap(image_path))

        self.horizontalLayout_112.addWidget(self.label_clockSettingsPage)

        self.horizontalSpacer_82 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_112.addItem(self.horizontalSpacer_82)

        self.label_userManagementPage = QLabel(self.page24)
        self.label_userManagementPage.setObjectName(u"label_userManagementPage")
        self.label_userManagementPage.setMinimumSize(QSize(110, 130))
        self.label_userManagementPage.setMaximumSize(QSize(130, 130))
        self.label_userManagementPage.setFont(font)

        image_path = os.path.join(script_dir, "userman12.png")
        self.label_userManagementPage.setPixmap(QPixmap(image_path))

        self.horizontalLayout_112.addWidget(self.label_userManagementPage)

        self.horizontalSpacer_89 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_112.addItem(self.horizontalSpacer_89)

        self.label_reportPage = QLabel(self.page24)
        self.label_reportPage.setObjectName(u"label_reportPage")
        self.label_reportPage.setMinimumSize(QSize(130, 130))
        self.label_reportPage.setMaximumSize(QSize(16777215, 16777215))
        self.label_reportPage.setFont(font)

        image_path = os.path.join(script_dir, "Report.png")
        self.label_reportPage.setPixmap(QPixmap(image_path))

        self.horizontalLayout_112.addWidget(self.label_reportPage)

        self.horizontalSpacer_91 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_112.addItem(self.horizontalSpacer_91)

        self.label_aboutLogoPage = QLabel(self.page24)
        self.label_aboutLogoPage.setObjectName(u"label_aboutLogoPage")
        self.label_aboutLogoPage.setMinimumSize(QSize(130, 130))
        self.label_aboutLogoPage.setMaximumSize(QSize(16777215, 16777215))

        image_path = os.path.join(script_dir, "help130.png")
        self.label_aboutLogoPage.setPixmap(QPixmap(image_path))

        self.horizontalLayout_112.addWidget(self.label_aboutLogoPage)

        self.horizontalSpacer_92 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_112.addItem(self.horizontalSpacer_92)


        self.page24Layout.addLayout(self.horizontalLayout_112)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.page24Layout.addItem(self.verticalSpacer_12)

        self.stackedWidget_main.addWidget(self.page24)
        self.page25 = QWidget()
        self.page25.setObjectName(u"page25")
        self.page25Layout = QVBoxLayout(self.page25)
        self.page25Layout.setObjectName(u"page25Layout")
        self.line_60 = QFrame(self.page25)
        self.line_60.setObjectName(u"line_60")
        self.line_60.setFrameShape(QFrame.Shape.HLine)
        self.line_60.setFrameShadow(QFrame.Shadow.Sunken)

        self.page25Layout.addWidget(self.line_60)

        self.horizontalLayout_117 = QHBoxLayout()
        self.horizontalLayout_117.setObjectName(u"horizontalLayout_117")
        self.line_62 = QFrame(self.page25)
        self.line_62.setObjectName(u"line_62")
        self.line_62.setFrameShape(QFrame.Shape.VLine)
        self.line_62.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_117.addWidget(self.line_62)

        self.comboBox = QComboBox(self.page25)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(0, 0))
        self.comboBox.setMaximumSize(QSize(50, 16777215))
        self.comboBox.setFont(font)

        self.horizontalLayout_117.addWidget(self.comboBox)

        self.line_70 = QFrame(self.page25)
        self.line_70.setObjectName(u"line_70")
        self.line_70.setFrameShape(QFrame.Shape.VLine)
        self.line_70.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_117.addWidget(self.line_70)


        self.page25Layout.addLayout(self.horizontalLayout_117)

        self.horizontalLayout_118 = QHBoxLayout()
        self.horizontalLayout_118.setObjectName(u"horizontalLayout_118")
        self.line_71 = QFrame(self.page25)
        self.line_71.setObjectName(u"line_71")
        self.line_71.setFrameShape(QFrame.Shape.VLine)
        self.line_71.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_118.addWidget(self.line_71)

        self.pushButton_2 = QPushButton(self.page25)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMaximumSize(QSize(50, 16777215))
        self.pushButton_2.setFont(font)

        self.horizontalLayout_118.addWidget(self.pushButton_2)

        self.line_80 = QFrame(self.page25)
        self.line_80.setObjectName(u"line_80")
        self.line_80.setFrameShape(QFrame.Shape.VLine)
        self.line_80.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_118.addWidget(self.line_80)


        self.page25Layout.addLayout(self.horizontalLayout_118)

        self.line_61 = QFrame(self.page25)
        self.line_61.setObjectName(u"line_61")
        self.line_61.setFrameShape(QFrame.Shape.HLine)
        self.line_61.setFrameShadow(QFrame.Shadow.Sunken)

        self.page25Layout.addWidget(self.line_61)

        self.stackedWidget_main.addWidget(self.page25)
        self.page26 = QWidget()
        self.page26.setObjectName(u"page26")
        self.page26Layout = QVBoxLayout(self.page26)
        self.page26Layout.setObjectName(u"page26Layout")
        self.horizontalLayout_116 = QHBoxLayout()
        self.horizontalLayout_116.setObjectName(u"horizontalLayout_116")

        self.page26Layout.addLayout(self.horizontalLayout_116)

        self.line_77 = QFrame(self.page26)
        self.line_77.setObjectName(u"line_77")
        self.line_77.setFrameShape(QFrame.Shape.HLine)
        self.line_77.setFrameShadow(QFrame.Shadow.Sunken)

        self.page26Layout.addWidget(self.line_77)

        self.stackedWidget_main.addWidget(self.page26)
        self.page27 = QWidget()
        self.page27.setObjectName(u"page27")
        self.page27Layout = QVBoxLayout(self.page27)
        self.page27Layout.setObjectName(u"page27Layout")
        self.verticalSpacer_68 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.page27Layout.addItem(self.verticalSpacer_68)

        self.horizontalLayout_135 = QHBoxLayout()
        self.horizontalLayout_135.setObjectName(u"horizontalLayout_135")
        self.horizontalSpacer_128 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_135.addItem(self.horizontalSpacer_128)

        self.button_angleCalculationSetting = QPushButton(self.page27)
        self.button_angleCalculationSetting.setObjectName(u"button_angleCalculationSetting")
        self.button_angleCalculationSetting.setFont(font)

        self.horizontalLayout_135.addWidget(self.button_angleCalculationSetting)

        self.horizontalSpacer_129 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_135.addItem(self.horizontalSpacer_129)


        self.page27Layout.addLayout(self.horizontalLayout_135)

        self.verticalSpacer_42 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.page27Layout.addItem(self.verticalSpacer_42)

        self.horizontalLayout_152 = QHBoxLayout()
        self.horizontalLayout_152.setObjectName(u"horizontalLayout_152")
        self.horizontalSpacer_90 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_152.addItem(self.horizontalSpacer_90)

        self.label_modeForCombineIndividual = QLabel(self.page27)
        self.label_modeForCombineIndividual.setObjectName(u"label_modeForCombineIndividual")
        self.label_modeForCombineIndividual.setFont(font)

        self.horizontalLayout_152.addWidget(self.label_modeForCombineIndividual)

        self.radioButton_modeCombine = QRadioButton(self.page27)
        self.buttonGroup_4 = QButtonGroup(MainWindow)
        self.buttonGroup_4.setObjectName(u"buttonGroup_4")
        self.buttonGroup_4.addButton(self.radioButton_modeCombine)
        self.radioButton_modeCombine.setObjectName(u"radioButton_modeCombine")
        self.radioButton_modeCombine.setFont(font)

        self.horizontalLayout_152.addWidget(self.radioButton_modeCombine)

        self.radioButton_modeIndividual = QRadioButton(self.page27)
        self.buttonGroup_4.addButton(self.radioButton_modeIndividual)
        self.radioButton_modeIndividual.setObjectName(u"radioButton_modeIndividual")
        self.radioButton_modeIndividual.setFont(font)

        self.horizontalLayout_152.addWidget(self.radioButton_modeIndividual)

        self.horizontalSpacer_93 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_152.addItem(self.horizontalSpacer_93)


        self.page27Layout.addLayout(self.horizontalLayout_152)

        self.verticalSpacer_62 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.page27Layout.addItem(self.verticalSpacer_62)

        self.horizontalLayout_115 = QHBoxLayout()
        self.horizontalLayout_115.setObjectName(u"horizontalLayout_115")
        self.horizontalSpacer_177 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_115.addItem(self.horizontalSpacer_177)

        self.label_7 = QLabel(self.page27)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)

        self.horizontalLayout_115.addWidget(self.label_7)

        self.radioButton = QRadioButton(self.page27)
        self.buttonGroup_3 = QButtonGroup(MainWindow)
        self.buttonGroup_3.setObjectName(u"buttonGroup_3")
        self.buttonGroup_3.addButton(self.radioButton)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setFont(font)

        self.horizontalLayout_115.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.page27)
        self.buttonGroup_3.addButton(self.radioButton_2)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setFont(font)

        self.horizontalLayout_115.addWidget(self.radioButton_2)

        self.horizontalSpacer_178 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_115.addItem(self.horizontalSpacer_178)


        self.page27Layout.addLayout(self.horizontalLayout_115)

        self.verticalSpacer_48 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.page27Layout.addItem(self.verticalSpacer_48)

        self.horizontalLayout_140 = QHBoxLayout()
        self.horizontalLayout_140.setObjectName(u"horizontalLayout_140")
        self.horizontalSpacer_133 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_140.addItem(self.horizontalSpacer_133)

        self.label_DurationForAutosave = QLabel(self.page27)
        self.label_DurationForAutosave.setObjectName(u"label_DurationForAutosave")
        self.label_DurationForAutosave.setFont(font)

        self.horizontalLayout_140.addWidget(self.label_DurationForAutosave)

        self.lineEdit_DurationAutosave = QLineEdit(self.page27)
        self.lineEdit_DurationAutosave.setObjectName(u"lineEdit_DurationAutosave")
        self.lineEdit_DurationAutosave.setMaximumSize(QSize(70, 16777215))
        self.lineEdit_DurationAutosave.setFont(font)

        self.horizontalLayout_140.addWidget(self.lineEdit_DurationAutosave, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalSpacer_134 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_140.addItem(self.horizontalSpacer_134)


        self.page27Layout.addLayout(self.horizontalLayout_140)

        self.verticalSpacer_43 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.page27Layout.addItem(self.verticalSpacer_43)

        self.horizontalLayout_133 = QHBoxLayout()
        self.horizontalLayout_133.setObjectName(u"horizontalLayout_133")
        self.horizontalSpacer_138 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_133.addItem(self.horizontalSpacer_138)

        self.pushButton_autosenseRange = QPushButton(self.page27)
        self.pushButton_autosenseRange.setObjectName(u"pushButton_autosenseRange")
        self.pushButton_autosenseRange.setFont(font)

        self.horizontalLayout_133.addWidget(self.pushButton_autosenseRange)

        self.horizontalSpacer_139 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_133.addItem(self.horizontalSpacer_139)


        self.page27Layout.addLayout(self.horizontalLayout_133)

        self.verticalSpacer_67 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.page27Layout.addItem(self.verticalSpacer_67)

        self.stackedWidget_main.addWidget(self.page27)
        self.page28 = QWidget()
        self.page28.setObjectName(u"page28")
        self.page28Layout = QVBoxLayout(self.page28)
        self.page28Layout.setObjectName(u"page28Layout")
        self.horizontalLayout_137 = QHBoxLayout()
        self.horizontalLayout_137.setObjectName(u"horizontalLayout_137")
        self.horizontalSpacer_143 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_137.addItem(self.horizontalSpacer_143)

        self.label_angleCalculation = QLabel(self.page28)
        self.label_angleCalculation.setObjectName(u"label_angleCalculation")
        self.label_angleCalculation.setFont(font)

        self.horizontalLayout_137.addWidget(self.label_angleCalculation)

        self.toggelButton_angleCalculation = QLabel(self.page28)
        self.toggelButton_angleCalculation.setObjectName(u"toggelButton_angleCalculation")
        self.toggelButton_angleCalculation.setFont(font)

        image_path = os.path.join(script_dir, "Switcher_On.png")
        self.toggelButton_angleCalculation.setPixmap(QPixmap(image_path))

        self.horizontalLayout_137.addWidget(self.toggelButton_angleCalculation)

        self.label_angleCalculationONOff = QLabel(self.page28)
        self.label_angleCalculationONOff.setObjectName(u"label_angleCalculationONOff")
        self.label_angleCalculationONOff.setFont(font)

        self.horizontalLayout_137.addWidget(self.label_angleCalculationONOff)

        self.horizontalSpacer_144 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_137.addItem(self.horizontalSpacer_144)


        self.page28Layout.addLayout(self.horizontalLayout_137)

        self.horizontalLayout_138 = QHBoxLayout()
        self.horizontalLayout_138.setObjectName(u"horizontalLayout_138")
        self.horizontalSpacer_145 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_138.addItem(self.horizontalSpacer_145)

        self.label_angleCalculationMasterAngle = QLabel(self.page28)
        self.label_angleCalculationMasterAngle.setObjectName(u"label_angleCalculationMasterAngle")
        self.label_angleCalculationMasterAngle.setFont(font)

        self.horizontalLayout_138.addWidget(self.label_angleCalculationMasterAngle)

        self.lineEdit_angleDegree = QLineEdit(self.page28)
        self.lineEdit_angleDegree.setObjectName(u"lineEdit_angleDegree")
        self.lineEdit_angleDegree.setMaximumSize(QSize(70, 16777215))
        self.lineEdit_angleDegree.setFont(font)

        self.horizontalLayout_138.addWidget(self.lineEdit_angleDegree, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_80 = QLabel(self.page28)
        self.label_80.setObjectName(u"label_80")
        self.label_80.setMaximumSize(QSize(16777215, 50))
        self.label_80.setFont(font4)
        self.label_80.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.horizontalLayout_138.addWidget(self.label_80)

        self.lineEdit_angleMinutes = QLineEdit(self.page28)
        self.lineEdit_angleMinutes.setObjectName(u"lineEdit_angleMinutes")
        self.lineEdit_angleMinutes.setMaximumSize(QSize(70, 16777215))
        self.lineEdit_angleMinutes.setFont(font)

        self.horizontalLayout_138.addWidget(self.lineEdit_angleMinutes, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_81 = QLabel(self.page28)
        self.label_81.setObjectName(u"label_81")
        self.label_81.setMaximumSize(QSize(16777215, 50))
        self.label_81.setFont(font4)
        self.label_81.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.horizontalLayout_138.addWidget(self.label_81)

        self.lineEdit_angleSeconds = QLineEdit(self.page28)
        self.lineEdit_angleSeconds.setObjectName(u"lineEdit_angleSeconds")
        self.lineEdit_angleSeconds.setMaximumSize(QSize(70, 16777215))
        self.lineEdit_angleSeconds.setFont(font)

        self.horizontalLayout_138.addWidget(self.lineEdit_angleSeconds, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_82 = QLabel(self.page28)
        self.label_82.setObjectName(u"label_82")
        self.label_82.setMaximumSize(QSize(16777215, 50))
        self.label_82.setFont(font4)
        self.label_82.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.horizontalLayout_138.addWidget(self.label_82)

        self.horizontalSpacer_147 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_138.addItem(self.horizontalSpacer_147)


        self.page28Layout.addLayout(self.horizontalLayout_138)

        self.horizontalLayout_141 = QHBoxLayout()
        self.horizontalLayout_141.setObjectName(u"horizontalLayout_141")
        self.horizontalSpacer_150 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_141.addItem(self.horizontalSpacer_150)

        self.label_positiveTol = QLabel(self.page28)
        self.label_positiveTol.setObjectName(u"label_positiveTol")
        self.label_positiveTol.setFont(font)

        self.horizontalLayout_141.addWidget(self.label_positiveTol)

        self.lineEdit_toleranceMin = QLineEdit(self.page28)
        self.lineEdit_toleranceMin.setObjectName(u"lineEdit_toleranceMin")
        self.lineEdit_toleranceMin.setMaximumSize(QSize(70, 16777215))
        self.lineEdit_toleranceMin.setFont(font)

        self.horizontalLayout_141.addWidget(self.lineEdit_toleranceMin)

        self.label_83 = QLabel(self.page28)
        self.label_83.setObjectName(u"label_83")
        self.label_83.setFont(font4)
        self.label_83.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.horizontalLayout_141.addWidget(self.label_83)

        self.lineEdit_toleranceSec = QLineEdit(self.page28)
        self.lineEdit_toleranceSec.setObjectName(u"lineEdit_toleranceSec")
        self.lineEdit_toleranceSec.setMaximumSize(QSize(70, 16777215))
        self.lineEdit_toleranceSec.setFont(font)

        self.horizontalLayout_141.addWidget(self.lineEdit_toleranceSec)

        self.label_84 = QLabel(self.page28)
        self.label_84.setObjectName(u"label_84")
        self.label_84.setFont(font4)
        self.label_84.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.horizontalLayout_141.addWidget(self.label_84)

        self.horizontalSpacer_151 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_141.addItem(self.horizontalSpacer_151)


        self.page28Layout.addLayout(self.horizontalLayout_141)

        self.horizontalLayout_142 = QHBoxLayout()
        self.horizontalLayout_142.setObjectName(u"horizontalLayout_142")
        self.horizontalSpacer_153 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_142.addItem(self.horizontalSpacer_153)

        self.label_negativeTol = QLabel(self.page28)
        self.label_negativeTol.setObjectName(u"label_negativeTol")
        self.label_negativeTol.setFont(font)

        self.horizontalLayout_142.addWidget(self.label_negativeTol)

        self.lineEdit_negativeTolMin = QLineEdit(self.page28)
        self.lineEdit_negativeTolMin.setObjectName(u"lineEdit_negativeTolMin")
        self.lineEdit_negativeTolMin.setMaximumSize(QSize(70, 16777215))
        self.lineEdit_negativeTolMin.setFont(font)

        self.horizontalLayout_142.addWidget(self.lineEdit_negativeTolMin)

        self.label_85 = QLabel(self.page28)
        self.label_85.setObjectName(u"label_85")
        self.label_85.setFont(font4)
        self.label_85.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.horizontalLayout_142.addWidget(self.label_85)

        self.lineEdit_negativeTolSec = QLineEdit(self.page28)
        self.lineEdit_negativeTolSec.setObjectName(u"lineEdit_negativeTolSec")
        self.lineEdit_negativeTolSec.setMaximumSize(QSize(70, 16777215))
        self.lineEdit_negativeTolSec.setFont(font)

        self.horizontalLayout_142.addWidget(self.lineEdit_negativeTolSec)

        self.label_86 = QLabel(self.page28)
        self.label_86.setObjectName(u"label_86")
        self.label_86.setFont(font4)
        self.label_86.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.horizontalLayout_142.addWidget(self.label_86)

        self.horizontalSpacer_154 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_142.addItem(self.horizontalSpacer_154)


        self.page28Layout.addLayout(self.horizontalLayout_142)

        self.horizontalLayout_143 = QHBoxLayout()
        self.horizontalLayout_143.setObjectName(u"horizontalLayout_143")
        self.horizontalSpacer_155 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_143.addItem(self.horizontalSpacer_155)

        self.label_Distance = QLabel(self.page28)
        self.label_Distance.setObjectName(u"label_Distance")
        self.label_Distance.setFont(font)

        self.horizontalLayout_143.addWidget(self.label_Distance)

        self.lineEdit_distanceMm = QLineEdit(self.page28)
        self.lineEdit_distanceMm.setObjectName(u"lineEdit_distanceMm")
        self.lineEdit_distanceMm.setMaximumSize(QSize(70, 16777215))
        self.lineEdit_distanceMm.setFont(font)

        self.horizontalLayout_143.addWidget(self.lineEdit_distanceMm, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_distanceInMm = QLabel(self.page28)
        self.label_distanceInMm.setObjectName(u"label_distanceInMm")
        self.label_distanceInMm.setFont(font)

        self.horizontalLayout_143.addWidget(self.label_distanceInMm)

        self.horizontalSpacer_156 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_143.addItem(self.horizontalSpacer_156)


        self.page28Layout.addLayout(self.horizontalLayout_143)

        self.horizontalLayout_145 = QHBoxLayout()
        self.horizontalLayout_145.setObjectName(u"horizontalLayout_145")
        self.horizontalSpacer_157 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_145.addItem(self.horizontalSpacer_157)

        self.label_Angle = QLabel(self.page28)
        self.label_Angle.setObjectName(u"label_Angle")
        self.label_Angle.setFont(font)

        self.horizontalLayout_145.addWidget(self.label_Angle)

        self.radioButton_halfAngle = QRadioButton(self.page28)
        self.radioButton_halfAngle.setObjectName(u"radioButton_halfAngle")
        self.radioButton_halfAngle.setFont(font)

        self.horizontalLayout_145.addWidget(self.radioButton_halfAngle)

        self.radioButton_2_fullAngle = QRadioButton(self.page28)
        self.radioButton_2_fullAngle.setObjectName(u"radioButton_2_fullAngle")
        self.radioButton_2_fullAngle.setFont(font)

        self.horizontalLayout_145.addWidget(self.radioButton_2_fullAngle)

        self.horizontalSpacer_158 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_145.addItem(self.horizontalSpacer_158)


        self.page28Layout.addLayout(self.horizontalLayout_145)

        self.stackedWidget_main.addWidget(self.page28)
        self.page29 = QWidget()
        self.page29.setObjectName(u"page29")
        self.page29Layout = QVBoxLayout(self.page29)
        self.page29Layout.setObjectName(u"page29Layout")
        self.horizontalLayout_162 = QHBoxLayout()
        self.horizontalLayout_162.setObjectName(u"horizontalLayout_162")
        self.horizontalSpacer_95 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_162.addItem(self.horizontalSpacer_95)

        self.label_programIdOnSetMaster = QLabel(self.page29)
        self.label_programIdOnSetMaster.setObjectName(u"label_programIdOnSetMaster")
        self.label_programIdOnSetMaster.setFont(font)

        self.horizontalLayout_162.addWidget(self.label_programIdOnSetMaster)

        self.comboBox_7 = QComboBox(self.page29)
        self.comboBox_7.setObjectName(u"comboBox_7")
        self.comboBox_7.setFont(font)

        self.horizontalLayout_162.addWidget(self.comboBox_7)

        self.horizontalSpacer_94 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_162.addItem(self.horizontalSpacer_94)

        self.label_programNamOnSetMAster = QLabel(self.page29)
        self.label_programNamOnSetMAster.setObjectName(u"label_programNamOnSetMAster")
        self.label_programNamOnSetMAster.setFont(font)

        self.horizontalLayout_162.addWidget(self.label_programNamOnSetMAster)

        self.label_programName = QLabel(self.page29)
        self.label_programName.setObjectName(u"label_programName")
        self.label_programName.setFont(font)

        self.horizontalLayout_162.addWidget(self.label_programName)

        self.horizontalSpacer_96 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_162.addItem(self.horizontalSpacer_96)


        self.page29Layout.addLayout(self.horizontalLayout_162)

        self.verticalSpacer_44 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.page29Layout.addItem(self.verticalSpacer_44)

        self.line_81 = QFrame(self.page29)
        self.line_81.setObjectName(u"line_81")
        self.line_81.setFrameShape(QFrame.Shape.HLine)
        self.line_81.setFrameShadow(QFrame.Shadow.Sunken)

        self.page29Layout.addWidget(self.line_81)

        self.horizontalLayout_163 = QHBoxLayout()
        self.horizontalLayout_163.setObjectName(u"horizontalLayout_163")
        self.horizontalSpacer_136 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_163.addItem(self.horizontalSpacer_136)

        self.label_43 = QLabel(self.page29)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setFont(font)

        self.horizontalLayout_163.addWidget(self.label_43)

        self.horizontalSpacer_140 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_163.addItem(self.horizontalSpacer_140)


        self.page29Layout.addLayout(self.horizontalLayout_163)

        self.verticalSpacer_45 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.page29Layout.addItem(self.verticalSpacer_45)

        self.line_82 = QFrame(self.page29)
        self.line_82.setObjectName(u"line_82")
        self.line_82.setFrameShape(QFrame.Shape.HLine)
        self.line_82.setFrameShadow(QFrame.Shadow.Sunken)

        self.page29Layout.addWidget(self.line_82)

        self.horizontalLayout_164 = QHBoxLayout()
        self.horizontalLayout_164.setObjectName(u"horizontalLayout_164")
        self.horizontalSpacer_97 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_164.addItem(self.horizontalSpacer_97)

        self.label_masterSetting = QLabel(self.page29)
        self.label_masterSetting.setObjectName(u"label_masterSetting")
        self.label_masterSetting.setFont(font)

        self.horizontalLayout_164.addWidget(self.label_masterSetting)

        self.button_setMaster = QPushButton(self.page29)
        self.button_setMaster.setObjectName(u"button_setMaster")
        sizePolicy.setHeightForWidth(self.button_setMaster.sizePolicy().hasHeightForWidth())
        self.button_setMaster.setSizePolicy(sizePolicy)
        self.button_setMaster.setMinimumSize(QSize(0, 0))
        self.button_setMaster.setMaximumSize(QSize(16777215, 16777215))
        self.button_setMaster.setFont(font)

        self.horizontalLayout_164.addWidget(self.button_setMaster)

        self.horizontalSpacer_98 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_164.addItem(self.horizontalSpacer_98)

        self.button_programList = QPushButton(self.page29)
        self.button_programList.setObjectName(u"button_programList")
        sizePolicy.setHeightForWidth(self.button_programList.sizePolicy().hasHeightForWidth())
        self.button_programList.setSizePolicy(sizePolicy)
        self.button_programList.setMinimumSize(QSize(0, 0))
        self.button_programList.setMaximumSize(QSize(16777215, 16777215))
        self.button_programList.setFont(font)

        self.horizontalLayout_164.addWidget(self.button_programList)

        self.horizontalSpacer_148 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_164.addItem(self.horizontalSpacer_148)

        self.button_partSettings = QPushButton(self.page29)
        self.button_partSettings.setObjectName(u"button_partSettings")
        sizePolicy.setHeightForWidth(self.button_partSettings.sizePolicy().hasHeightForWidth())
        self.button_partSettings.setSizePolicy(sizePolicy)
        self.button_partSettings.setMinimumSize(QSize(0, 20))
        self.button_partSettings.setFont(font)

        self.horizontalLayout_164.addWidget(self.button_partSettings)

        self.horizontalSpacer_142 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_164.addItem(self.horizontalSpacer_142)


        self.page29Layout.addLayout(self.horizontalLayout_164)

        self.verticalSpacer_46 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.page29Layout.addItem(self.verticalSpacer_46)

        self.line_83 = QFrame(self.page29)
        self.line_83.setObjectName(u"line_83")
        self.line_83.setFrameShape(QFrame.Shape.HLine)
        self.line_83.setFrameShadow(QFrame.Shadow.Sunken)

        self.page29Layout.addWidget(self.line_83)

        self.horizontalLayout_175 = QHBoxLayout()
        self.horizontalLayout_175.setObjectName(u"horizontalLayout_175")
        self.horizontalSpacer_101 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_175.addItem(self.horizontalSpacer_101)

        self.label_liveD1Val = QLabel(self.page29)
        self.label_liveD1Val.setObjectName(u"label_liveD1Val")
        self.label_liveD1Val.setFont(font)

        self.horizontalLayout_175.addWidget(self.label_liveD1Val)

        self.horizontalSpacer_164 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_175.addItem(self.horizontalSpacer_164)

        self.line_84 = QFrame(self.page29)
        self.line_84.setObjectName(u"line_84")
        self.line_84.setFrameShape(QFrame.Shape.VLine)
        self.line_84.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_175.addWidget(self.line_84)

        self.horizontalSpacer_103 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_175.addItem(self.horizontalSpacer_103)

        self.label_masterD1_1 = QLabel(self.page29)
        self.label_masterD1_1.setObjectName(u"label_masterD1_1")
        self.label_masterD1_1.setFont(font)

        self.horizontalLayout_175.addWidget(self.label_masterD1_1)

        self.label_valMasterD1_1 = QLabel(self.page29)
        self.label_valMasterD1_1.setObjectName(u"label_valMasterD1_1")
        self.label_valMasterD1_1.setFont(font)

        self.horizontalLayout_175.addWidget(self.label_valMasterD1_1)

        self.horizontalSpacer_104 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_175.addItem(self.horizontalSpacer_104)

        self.label_masterD1_2 = QLabel(self.page29)
        self.label_masterD1_2.setObjectName(u"label_masterD1_2")
        self.label_masterD1_2.setFont(font)

        self.horizontalLayout_175.addWidget(self.label_masterD1_2)

        self.label_valMasterD1_2 = QLabel(self.page29)
        self.label_valMasterD1_2.setObjectName(u"label_valMasterD1_2")
        self.label_valMasterD1_2.setFont(font)

        self.horizontalLayout_175.addWidget(self.label_valMasterD1_2)

        self.horizontalSpacer_102 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_175.addItem(self.horizontalSpacer_102)


        self.page29Layout.addLayout(self.horizontalLayout_175)

        self.horizontalLayout_174 = QHBoxLayout()
        self.horizontalLayout_174.setObjectName(u"horizontalLayout_174")
        self.horizontalSpacer_99 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_174.addItem(self.horizontalSpacer_99)

        self.label_liveD2Val = QLabel(self.page29)
        self.label_liveD2Val.setObjectName(u"label_liveD2Val")
        self.label_liveD2Val.setFont(font)

        self.horizontalLayout_174.addWidget(self.label_liveD2Val)

        self.horizontalSpacer_165 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_174.addItem(self.horizontalSpacer_165)

        self.line_85 = QFrame(self.page29)
        self.line_85.setObjectName(u"line_85")
        self.line_85.setFrameShape(QFrame.Shape.VLine)
        self.line_85.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_174.addWidget(self.line_85)

        self.horizontalSpacer_106 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_174.addItem(self.horizontalSpacer_106)

        self.label_masterD2_1 = QLabel(self.page29)
        self.label_masterD2_1.setObjectName(u"label_masterD2_1")
        self.label_masterD2_1.setFont(font)

        self.horizontalLayout_174.addWidget(self.label_masterD2_1)

        self.label_valMasterD2_1 = QLabel(self.page29)
        self.label_valMasterD2_1.setObjectName(u"label_valMasterD2_1")
        self.label_valMasterD2_1.setFont(font)

        self.horizontalLayout_174.addWidget(self.label_valMasterD2_1)

        self.horizontalSpacer_105 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_174.addItem(self.horizontalSpacer_105)

        self.label_masterD2_2 = QLabel(self.page29)
        self.label_masterD2_2.setObjectName(u"label_masterD2_2")
        self.label_masterD2_2.setFont(font)

        self.horizontalLayout_174.addWidget(self.label_masterD2_2)

        self.label_valMasterD2_2 = QLabel(self.page29)
        self.label_valMasterD2_2.setObjectName(u"label_valMasterD2_2")
        self.label_valMasterD2_2.setFont(font)

        self.horizontalLayout_174.addWidget(self.label_valMasterD2_2)

        self.horizontalSpacer_100 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_174.addItem(self.horizontalSpacer_100)


        self.page29Layout.addLayout(self.horizontalLayout_174)

        self.horizontalLayout_169 = QHBoxLayout()
        self.horizontalLayout_169.setObjectName(u"horizontalLayout_169")
        self.horizontalSpacer_107 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_169.addItem(self.horizontalSpacer_107)

        self.label_liveD3Val = QLabel(self.page29)
        self.label_liveD3Val.setObjectName(u"label_liveD3Val")
        self.label_liveD3Val.setFont(font)

        self.horizontalLayout_169.addWidget(self.label_liveD3Val)

        self.horizontalSpacer_166 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_169.addItem(self.horizontalSpacer_166)

        self.line_86 = QFrame(self.page29)
        self.line_86.setObjectName(u"line_86")
        self.line_86.setFrameShape(QFrame.Shape.VLine)
        self.line_86.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_169.addWidget(self.line_86)

        self.horizontalSpacer_109 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_169.addItem(self.horizontalSpacer_109)

        self.label_masterD3_1 = QLabel(self.page29)
        self.label_masterD3_1.setObjectName(u"label_masterD3_1")
        self.label_masterD3_1.setFont(font)

        self.horizontalLayout_169.addWidget(self.label_masterD3_1)

        self.label_valMasterD3_1 = QLabel(self.page29)
        self.label_valMasterD3_1.setObjectName(u"label_valMasterD3_1")
        self.label_valMasterD3_1.setFont(font)

        self.horizontalLayout_169.addWidget(self.label_valMasterD3_1)

        self.horizontalSpacer_110 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_169.addItem(self.horizontalSpacer_110)

        self.label_masterD3_2 = QLabel(self.page29)
        self.label_masterD3_2.setObjectName(u"label_masterD3_2")
        self.label_masterD3_2.setFont(font)

        self.horizontalLayout_169.addWidget(self.label_masterD3_2)

        self.label_valMasterD3_2 = QLabel(self.page29)
        self.label_valMasterD3_2.setObjectName(u"label_valMasterD3_2")
        self.label_valMasterD3_2.setFont(font)

        self.horizontalLayout_169.addWidget(self.label_valMasterD3_2)

        self.horizontalSpacer_108 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_169.addItem(self.horizontalSpacer_108)


        self.page29Layout.addLayout(self.horizontalLayout_169)

        self.horizontalLayout_170 = QHBoxLayout()
        self.horizontalLayout_170.setObjectName(u"horizontalLayout_170")
        self.horizontalSpacer_111 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_170.addItem(self.horizontalSpacer_111)

        self.label_liveD4val = QLabel(self.page29)
        self.label_liveD4val.setObjectName(u"label_liveD4val")
        self.label_liveD4val.setFont(font)

        self.horizontalLayout_170.addWidget(self.label_liveD4val)

        self.horizontalSpacer_168 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_170.addItem(self.horizontalSpacer_168)

        self.line_87 = QFrame(self.page29)
        self.line_87.setObjectName(u"line_87")
        self.line_87.setFrameShape(QFrame.Shape.VLine)
        self.line_87.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_170.addWidget(self.line_87)

        self.horizontalSpacer_113 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_170.addItem(self.horizontalSpacer_113)

        self.label_masterD4_1 = QLabel(self.page29)
        self.label_masterD4_1.setObjectName(u"label_masterD4_1")
        self.label_masterD4_1.setFont(font)

        self.horizontalLayout_170.addWidget(self.label_masterD4_1)

        self.label_valMasterD4_1 = QLabel(self.page29)
        self.label_valMasterD4_1.setObjectName(u"label_valMasterD4_1")
        self.label_valMasterD4_1.setFont(font)

        self.horizontalLayout_170.addWidget(self.label_valMasterD4_1)

        self.horizontalSpacer_114 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_170.addItem(self.horizontalSpacer_114)

        self.label_masterD4_2 = QLabel(self.page29)
        self.label_masterD4_2.setObjectName(u"label_masterD4_2")
        self.label_masterD4_2.setFont(font)

        self.horizontalLayout_170.addWidget(self.label_masterD4_2)

        self.label_valMasterD4_2 = QLabel(self.page29)
        self.label_valMasterD4_2.setObjectName(u"label_valMasterD4_2")
        self.label_valMasterD4_2.setFont(font)

        self.horizontalLayout_170.addWidget(self.label_valMasterD4_2)

        self.horizontalSpacer_112 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_170.addItem(self.horizontalSpacer_112)


        self.page29Layout.addLayout(self.horizontalLayout_170)

        self.horizontalLayout_167 = QHBoxLayout()
        self.horizontalLayout_167.setObjectName(u"horizontalLayout_167")
        self.horizontalSpacer_115 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_167.addItem(self.horizontalSpacer_115)

        self.label_liveD5Val = QLabel(self.page29)
        self.label_liveD5Val.setObjectName(u"label_liveD5Val")
        self.label_liveD5Val.setFont(font)

        self.horizontalLayout_167.addWidget(self.label_liveD5Val)

        self.horizontalSpacer_169 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_167.addItem(self.horizontalSpacer_169)

        self.line_88 = QFrame(self.page29)
        self.line_88.setObjectName(u"line_88")
        self.line_88.setFrameShape(QFrame.Shape.VLine)
        self.line_88.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_167.addWidget(self.line_88)

        self.horizontalSpacer_116 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_167.addItem(self.horizontalSpacer_116)

        self.label_masterD5_1 = QLabel(self.page29)
        self.label_masterD5_1.setObjectName(u"label_masterD5_1")
        self.label_masterD5_1.setFont(font)

        self.horizontalLayout_167.addWidget(self.label_masterD5_1)

        self.label_valMasterD5_1 = QLabel(self.page29)
        self.label_valMasterD5_1.setObjectName(u"label_valMasterD5_1")
        self.label_valMasterD5_1.setFont(font)

        self.horizontalLayout_167.addWidget(self.label_valMasterD5_1)

        self.horizontalSpacer_117 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_167.addItem(self.horizontalSpacer_117)

        self.label_masterD5_2 = QLabel(self.page29)
        self.label_masterD5_2.setObjectName(u"label_masterD5_2")
        self.label_masterD5_2.setFont(font)

        self.horizontalLayout_167.addWidget(self.label_masterD5_2)

        self.label_valMasterD5_2 = QLabel(self.page29)
        self.label_valMasterD5_2.setObjectName(u"label_valMasterD5_2")
        self.label_valMasterD5_2.setFont(font)

        self.horizontalLayout_167.addWidget(self.label_valMasterD5_2)

        self.horizontalSpacer_118 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_167.addItem(self.horizontalSpacer_118)


        self.page29Layout.addLayout(self.horizontalLayout_167)

        self.horizontalLayout_166 = QHBoxLayout()
        self.horizontalLayout_166.setObjectName(u"horizontalLayout_166")
        self.horizontalSpacer_119 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_166.addItem(self.horizontalSpacer_119)

        self.label_liveD6Val = QLabel(self.page29)
        self.label_liveD6Val.setObjectName(u"label_liveD6Val")
        self.label_liveD6Val.setFont(font)

        self.horizontalLayout_166.addWidget(self.label_liveD6Val)

        self.horizontalSpacer_170 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_166.addItem(self.horizontalSpacer_170)

        self.line_89 = QFrame(self.page29)
        self.line_89.setObjectName(u"line_89")
        self.line_89.setFrameShape(QFrame.Shape.VLine)
        self.line_89.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_166.addWidget(self.line_89)

        self.horizontalSpacer_120 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_166.addItem(self.horizontalSpacer_120)

        self.label_masterD6_1 = QLabel(self.page29)
        self.label_masterD6_1.setObjectName(u"label_masterD6_1")
        self.label_masterD6_1.setFont(font)

        self.horizontalLayout_166.addWidget(self.label_masterD6_1)

        self.label_valMasterD6_1 = QLabel(self.page29)
        self.label_valMasterD6_1.setObjectName(u"label_valMasterD6_1")
        self.label_valMasterD6_1.setFont(font)

        self.horizontalLayout_166.addWidget(self.label_valMasterD6_1)

        self.horizontalSpacer_121 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_166.addItem(self.horizontalSpacer_121)

        self.label_masterD6_2 = QLabel(self.page29)
        self.label_masterD6_2.setObjectName(u"label_masterD6_2")
        self.label_masterD6_2.setFont(font)

        self.horizontalLayout_166.addWidget(self.label_masterD6_2)

        self.label_valMasterD6_2 = QLabel(self.page29)
        self.label_valMasterD6_2.setObjectName(u"label_valMasterD6_2")
        self.label_valMasterD6_2.setFont(font)

        self.horizontalLayout_166.addWidget(self.label_valMasterD6_2)

        self.horizontalSpacer_122 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_166.addItem(self.horizontalSpacer_122)


        self.page29Layout.addLayout(self.horizontalLayout_166)

        self.horizontalLayout_176 = QHBoxLayout()
        self.horizontalLayout_176.setObjectName(u"horizontalLayout_176")
        self.horizontalSpacer_123 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_176.addItem(self.horizontalSpacer_123)

        self.label_liveD7val = QLabel(self.page29)
        self.label_liveD7val.setObjectName(u"label_liveD7val")
        self.label_liveD7val.setFont(font)

        self.horizontalLayout_176.addWidget(self.label_liveD7val)

        self.horizontalSpacer_172 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_176.addItem(self.horizontalSpacer_172)

        self.line_90 = QFrame(self.page29)
        self.line_90.setObjectName(u"line_90")
        self.line_90.setFrameShape(QFrame.Shape.VLine)
        self.line_90.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_176.addWidget(self.line_90)

        self.horizontalSpacer_124 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_176.addItem(self.horizontalSpacer_124)

        self.label_masterD7_1 = QLabel(self.page29)
        self.label_masterD7_1.setObjectName(u"label_masterD7_1")
        self.label_masterD7_1.setFont(font)

        self.horizontalLayout_176.addWidget(self.label_masterD7_1)

        self.label_valMasterD7_1 = QLabel(self.page29)
        self.label_valMasterD7_1.setObjectName(u"label_valMasterD7_1")
        self.label_valMasterD7_1.setFont(font)

        self.horizontalLayout_176.addWidget(self.label_valMasterD7_1)

        self.horizontalSpacer_125 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_176.addItem(self.horizontalSpacer_125)

        self.label_masterD7_2 = QLabel(self.page29)
        self.label_masterD7_2.setObjectName(u"label_masterD7_2")
        self.label_masterD7_2.setFont(font)

        self.horizontalLayout_176.addWidget(self.label_masterD7_2)

        self.label_valMasterD7_2 = QLabel(self.page29)
        self.label_valMasterD7_2.setObjectName(u"label_valMasterD7_2")
        self.label_valMasterD7_2.setFont(font)

        self.horizontalLayout_176.addWidget(self.label_valMasterD7_2)

        self.horizontalSpacer_126 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_176.addItem(self.horizontalSpacer_126)


        self.page29Layout.addLayout(self.horizontalLayout_176)

        self.horizontalLayout_165 = QHBoxLayout()
        self.horizontalLayout_165.setObjectName(u"horizontalLayout_165")
        self.horizontalSpacer_127 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_165.addItem(self.horizontalSpacer_127)

        self.label_liveD8Val = QLabel(self.page29)
        self.label_liveD8Val.setObjectName(u"label_liveD8Val")
        self.label_liveD8Val.setFont(font)

        self.horizontalLayout_165.addWidget(self.label_liveD8Val)

        self.horizontalSpacer_173 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_165.addItem(self.horizontalSpacer_173)

        self.line_91 = QFrame(self.page29)
        self.line_91.setObjectName(u"line_91")
        self.line_91.setFrameShape(QFrame.Shape.VLine)
        self.line_91.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_165.addWidget(self.line_91)

        self.horizontalSpacer_130 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_165.addItem(self.horizontalSpacer_130)

        self.label_masterD8_1 = QLabel(self.page29)
        self.label_masterD8_1.setObjectName(u"label_masterD8_1")
        self.label_masterD8_1.setFont(font)

        self.horizontalLayout_165.addWidget(self.label_masterD8_1)

        self.label_valMasterD8_1 = QLabel(self.page29)
        self.label_valMasterD8_1.setObjectName(u"label_valMasterD8_1")
        self.label_valMasterD8_1.setFont(font)

        self.horizontalLayout_165.addWidget(self.label_valMasterD8_1)

        self.horizontalSpacer_131 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_165.addItem(self.horizontalSpacer_131)

        self.label_masterD8_2 = QLabel(self.page29)
        self.label_masterD8_2.setObjectName(u"label_masterD8_2")
        self.label_masterD8_2.setFont(font)

        self.horizontalLayout_165.addWidget(self.label_masterD8_2)

        self.label_valMasterD8_2 = QLabel(self.page29)
        self.label_valMasterD8_2.setObjectName(u"label_valMasterD8_2")
        self.label_valMasterD8_2.setFont(font)

        self.horizontalLayout_165.addWidget(self.label_valMasterD8_2)

        self.horizontalSpacer_135 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_165.addItem(self.horizontalSpacer_135)


        self.page29Layout.addLayout(self.horizontalLayout_165)

        self.verticalSpacer_47 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.page29Layout.addItem(self.verticalSpacer_47)

        self.stackedWidget_main.addWidget(self.page29)
        self.page30 = QWidget()
        self.page30.setObjectName(u"page30")
        self.page30Layout = QVBoxLayout(self.page30)
        self.page30Layout.setObjectName(u"page30Layout")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.tableWidget_2 = QTableWidget(self.page30)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setFont(font)

        self.verticalLayout_9.addWidget(self.tableWidget_2)


        self.page30Layout.addLayout(self.verticalLayout_9)

        self.stackedWidget_main.addWidget(self.page30)

        self.verticalLayout.addWidget(self.stackedWidget_main)

        self.verticalSpacer_63 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_63)

        self.horizontalLayout_109 = QHBoxLayout()
        self.horizontalLayout_109.setObjectName(u"horizontalLayout_109")

        self.verticalLayout.addLayout(self.horizontalLayout_109)

        self.line_footer = QFrame(self.centralwidget)
        self.line_footer.setObjectName(u"line_footer")
        self.line_footer.setFrameShape(QFrame.Shape.HLine)
        self.line_footer.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_footer)

        self.bottomLayout = QHBoxLayout()
        self.bottomLayout.setObjectName(u"bottomLayout")
        self.button_shutdown = QToolButton(self.centralwidget)
        self.button_shutdown.setObjectName(u"button_shutdown")
        icon = QIcon()
        icon.addFile(u"../../../QuadPreciGo/Ui/Images/power-button.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_shutdown.setIcon(icon)
        self.button_shutdown.setIconSize(QSize(60, 30))
        self.button_shutdown.setPopupMode(QToolButton.ToolButtonPopupMode.DelayedPopup)

        self.bottomLayout.addWidget(self.button_shutdown)

        self.button_back = QPushButton(self.centralwidget)
        self.button_back.setObjectName(u"button_back")
        self.button_back.setFont(font)
        icon1 = QIcon()
        icon1.addFile(u"../../../QuadPreciGo/Ui/Images/Back_Yellow.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_back.setIcon(icon1)
        self.button_back.setIconSize(QSize(60, 30))

        self.bottomLayout.addWidget(self.button_back, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.bottomLayout.addItem(self.horizontalSpacer)

        self.button_save = QPushButton(self.centralwidget)
        self.button_save.setObjectName(u"button_save")
        icon2 = QIcon()
        icon2.addFile(u"../../../QuadPreciGo/Ui/Images/Save_Icon_Yellow.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_save.setIcon(icon2)
        self.button_save.setIconSize(QSize(60, 30))

        self.bottomLayout.addWidget(self.button_save, 0, Qt.AlignmentFlag.AlignHCenter)

        self.button_forward = QToolButton(self.centralwidget)
        self.button_forward.setObjectName(u"button_forward")
        icon3 = QIcon()
        icon3.addFile(u"../../../QuadPreciGo/Ui/Images/forward_Yellow.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_forward.setIcon(icon3)
        self.button_forward.setIconSize(QSize(60, 30))

        self.bottomLayout.addWidget(self.button_forward)

        self.button_home = QToolButton(self.centralwidget)
        self.button_home.setObjectName(u"button_home")
        icon4 = QIcon()
        icon4.addFile(u"../../../QuadPreciGo/Ui/Images/Home_Icon_Yellow.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_home.setIcon(icon4)
        self.button_home.setIconSize(QSize(60, 30))

        self.bottomLayout.addWidget(self.button_home)


        self.verticalLayout.addLayout(self.bottomLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget_main.setCurrentIndex(17)
        self.tabWidget.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Quad-PreciGo", None))
        self.label_pageName.setText(QCoreApplication.translate("MainWindow", u"Octo-PreciGo", None))
        self.label_time.setText(QCoreApplication.translate("MainWindow", u"10:10:10", None))
        self.label_date.setText(QCoreApplication.translate("MainWindow", u"14-08-2025", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Status Bar :", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"IO Settings Saved Successfully...!!!", None))
        self.label_5.setText("")
        self.label_2.setText("")
        self.label_4.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"    Welcome To Octo-PreciGo !!!", None))
        self.label_username.setText(QCoreApplication.translate("MainWindow", u"  Username   :  ", None))
        self.label_password.setText(QCoreApplication.translate("MainWindow", u"  Password   :  ", None))
        self.button_login.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.button_addUpdateLogin.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.button_modifyLogin.setText(QCoreApplication.translate("MainWindow", u"Modify", None))
        self.button_deleteLogin.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.label_setUsernameLogin.setText(QCoreApplication.translate("MainWindow", u"Set Username  :", None))
        self.label_setPasswordLogin.setText(QCoreApplication.translate("MainWindow", u"  Set Password :", None))
        self.label_setAccessLogin.setText(QCoreApplication.translate("MainWindow", u"   Set Access Type :", None))
        self.comboBox_setAccessCombo.setItemText(0, QCoreApplication.translate("MainWindow", u"Super Admin", None))
        self.comboBox_setAccessCombo.setItemText(1, QCoreApplication.translate("MainWindow", u"Admin", None))
        self.comboBox_setAccessCombo.setItemText(2, QCoreApplication.translate("MainWindow", u"Guest", None))

        self.button_addUpdateLogin_2.setText(QCoreApplication.translate("MainWindow", u"Add/Modify", None))
        self.label_rs232.setText(QCoreApplication.translate("MainWindow", u"RS232  :", None))
        self.toggleButton_rs232.setText("")
        self.label_rs232OnOff.setText(QCoreApplication.translate("MainWindow", u"ON", None))
        self.label_baudRate.setText(QCoreApplication.translate("MainWindow", u"Baud Rate  :", None))
        self.comboBox_baudRate.setItemText(0, QCoreApplication.translate("MainWindow", u"4800", None))
        self.comboBox_baudRate.setItemText(1, QCoreApplication.translate("MainWindow", u"9600", None))
        self.comboBox_baudRate.setItemText(2, QCoreApplication.translate("MainWindow", u"19200", None))
        self.comboBox_baudRate.setItemText(3, QCoreApplication.translate("MainWindow", u"56000", None))
        self.comboBox_baudRate.setItemText(4, QCoreApplication.translate("MainWindow", u"115200", None))

        self.label_dataBits.setText(QCoreApplication.translate("MainWindow", u"Data Bits  :", None))
        self.comboBox_dataBits.setItemText(0, QCoreApplication.translate("MainWindow", u"5", None))
        self.comboBox_dataBits.setItemText(1, QCoreApplication.translate("MainWindow", u"6", None))
        self.comboBox_dataBits.setItemText(2, QCoreApplication.translate("MainWindow", u"7", None))
        self.comboBox_dataBits.setItemText(3, QCoreApplication.translate("MainWindow", u"8", None))

        self.label_parity.setText(QCoreApplication.translate("MainWindow", u"Parity  :", None))
        self.comboBox_parity.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))
        self.comboBox_parity.setItemText(1, QCoreApplication.translate("MainWindow", u"Odd", None))
        self.comboBox_parity.setItemText(2, QCoreApplication.translate("MainWindow", u"Even", None))
        self.comboBox_parity.setItemText(3, QCoreApplication.translate("MainWindow", u"Mark", None))
        self.comboBox_parity.setItemText(4, QCoreApplication.translate("MainWindow", u"Space", None))

        self.label_stopBits.setText(QCoreApplication.translate("MainWindow", u"Stop Bits  :", None))
        self.comboBox_stopBits.setItemText(0, QCoreApplication.translate("MainWindow", u"One", None))
        self.comboBox_stopBits.setItemText(1, QCoreApplication.translate("MainWindow", u"Two", None))
        self.comboBox_stopBits.setItemText(2, QCoreApplication.translate("MainWindow", u"OnePointFive", None))

        self.label_flowControl.setText(QCoreApplication.translate("MainWindow", u"Flow Control  :", None))
        self.comboBox_flowControl.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))
        self.comboBox_flowControl.setItemText(1, QCoreApplication.translate("MainWindow", u"RTS/CTS", None))
        self.comboBox_flowControl.setItemText(2, QCoreApplication.translate("MainWindow", u"XOnXOff", None))

        self.label_portName.setText(QCoreApplication.translate("MainWindow", u"Port Name  :", None))
        self.label_dimensionFormulaBar.setText(QCoreApplication.translate("MainWindow", u"D1  :", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Probe To Add :", None))
        self.comboBox_probeFormulaBar.setItemText(0, QCoreApplication.translate("MainWindow", u"P1", None))
        self.comboBox_probeFormulaBar.setItemText(1, QCoreApplication.translate("MainWindow", u"P2", None))

        self.button_addFormulaBar.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.button_plusFormulaBar.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.button_minusFormulaBar.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.button_multiplicationFormulaBar.setText(QCoreApplication.translate("MainWindow", u"*", None))
        self.button_divisionFormulaBar.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.button_modFormulaBar.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.button_commaFormulaBar.setText(QCoreApplication.translate("MainWindow", u",", None))
        self.button_backspaceFormulaBar.setText(QCoreApplication.translate("MainWindow", u"<-", None))
        self.button_leftBraceFormulaBar.setText(QCoreApplication.translate("MainWindow", u"(", None))
        self.button_maxFormulaBar.setText(QCoreApplication.translate("MainWindow", u"max", None))
        self.button_minFormulaBar.setText(QCoreApplication.translate("MainWindow", u"min", None))
        self.button_avgFormulaBar.setText(QCoreApplication.translate("MainWindow", u"avg", None))
        self.button_absFormulaBar.setText(QCoreApplication.translate("MainWindow", u"abs", None))
        self.button_rightBraceFormulaBar.setText(QCoreApplication.translate("MainWindow", u")", None))
        self.button_sinFormulaBar.setText(QCoreApplication.translate("MainWindow", u"sin", None))
        self.button_cosFormulaBar.setText(QCoreApplication.translate("MainWindow", u"cos", None))
        self.button_tanFormulaBar.setText(QCoreApplication.translate("MainWindow", u"tan", None))
        self.button_cosecFormulaBar.setText(QCoreApplication.translate("MainWindow", u"cosec", None))
        self.button_secFormulaBar.setText(QCoreApplication.translate("MainWindow", u"sec", None))
        self.button_cotFormulaBar.setText(QCoreApplication.translate("MainWindow", u"cot", None))
        self.button_saveSettingsFormulaBar.setText(QCoreApplication.translate("MainWindow", u"Save Settings", None))
        self.label_selfIp.setText(QCoreApplication.translate("MainWindow", u"Self IP Address  :", None))
        self.label_subnetMask.setText(QCoreApplication.translate("MainWindow", u"Subnet Mask  :", None))
        self.label_defaultGateway.setText(QCoreApplication.translate("MainWindow", u"Default Gateway  :", None))
        self.label_wifiSsid.setText(QCoreApplication.translate("MainWindow", u"Wifi SSID  :", None))
        self.label_wifiPassword.setText(QCoreApplication.translate("MainWindow", u"Wifi Password  :", None))
        self.label_buzzer.setText(QCoreApplication.translate("MainWindow", u"Buzzer  :                   ", None))
        self.toggleButton_buzzer.setText("")
        self.label_buzzerOnOff.setText(QCoreApplication.translate("MainWindow", u"OFF", None))
        self.radioButton_okBuzzer.setText(QCoreApplication.translate("MainWindow", u"Ok", None))
        self.radioButton_reworkNotokBuzzer.setText(QCoreApplication.translate("MainWindow", u"Rework / Not Ok", None))
        self.label_relay.setText(QCoreApplication.translate("MainWindow", u"Relay  :                     ", None))
        self.toggelButton_relay.setText("")
        self.label_relayOnOff.setText(QCoreApplication.translate("MainWindow", u"OFF", None))
        self.label_relayTime.setText(QCoreApplication.translate("MainWindow", u"Relay Time  :", None))
        self.label_cycleStopTimer.setText(QCoreApplication.translate("MainWindow", u"Cycle Stop Timer  :   ", None))
        self.toggelButton_cycleStopTimer.setText("")
        self.label_cycleStopTimerOnOff.setText(QCoreApplication.translate("MainWindow", u"OFF", None))
        self.label_cycleTime.setText(QCoreApplication.translate("MainWindow", u"Cycle Time  :", None))
        self.label_autoSaveReading.setText(QCoreApplication.translate("MainWindow", u"Auto Save Reading  :", None))
        self.toggelButton_autoSaveReading.setText("")
        self.label_autoSaveReadingOnOff.setText(QCoreApplication.translate("MainWindow", u"OFF", None))
        self.label_partTraceability.setText(QCoreApplication.translate("MainWindow", u"Part Traceability  :     ", None))
        self.toggelButton_partTraceability.setText("")
        self.label_partTraceabilityOnOff.setText(QCoreApplication.translate("MainWindow", u"OFF", None))
        self.radioButton_manualPartTraceability.setText(QCoreApplication.translate("MainWindow", u"Manual Reset", None))
        self.radioButton_autoPartTraceability.setText(QCoreApplication.translate("MainWindow", u"Auto Reset", None))
        self.label_displayMode.setText(QCoreApplication.translate("MainWindow", u"Display Mode  :", None))
        self.comboBox_displayMode.setItemText(0, QCoreApplication.translate("MainWindow", u"Digit", None))
        self.comboBox_displayMode.setItemText(1, QCoreApplication.translate("MainWindow", u"Dial", None))
        self.comboBox_displayMode.setItemText(2, QCoreApplication.translate("MainWindow", u"Graph", None))

        self.label_probeSensitivity.setText(QCoreApplication.translate("MainWindow", u"Probe Sensitivity  :", None))
        self.label_timeToMasterSet.setText(QCoreApplication.translate("MainWindow", u"Time To Master Set  :", None))
        self.toggleButtontimeToSetMaster.setText("")
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"OFF", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Hrs", None))
        self.label_masterGrouping.setText(QCoreApplication.translate("MainWindow", u"Master Grouping  :   ", None))
        self.toggleButton_masterGrouping.setText("")
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"OFF", None))
        self.button_factoryCalibration.setText(QCoreApplication.translate("MainWindow", u"Factory Calibration", None))
        self.button_touchCalibration.setText(QCoreApplication.translate("MainWindow", u"Touch Calibration", None))
        self.button_databaseSettings.setText(QCoreApplication.translate("MainWindow", u"Database Settings", None))
        self.button_rs232Settings.setText(QCoreApplication.translate("MainWindow", u"RS 232 Settings", None))
        self.button_factoryConfig.setText(QCoreApplication.translate("MainWindow", u"Factory Config", None))
        self.button_airSaving.setText(QCoreApplication.translate("MainWindow", u"Air Saving Settings", None))
        self.button_ipSettings.setText(QCoreApplication.translate("MainWindow", u"IP Settings", None))
        self.button_wifiSettings.setText(QCoreApplication.translate("MainWindow", u"Wifi Settings", None))
        self.label_productHelp.setText(QCoreApplication.translate("MainWindow", u"Product : Quad-PreciGo", None))
        self.label_intersenseNameHelp.setText(QCoreApplication.translate("MainWindow", u"INTERSENSE TECHNOLOGIES LLP", None))
        self.label_adressHelp.setText(QCoreApplication.translate("MainWindow", u"K-122/2,MIDC Waluj,", None))
        self.label_adressHelp_2.setText(QCoreApplication.translate("MainWindow", u"Aurangabad-431136(M.S.) India", None))
        self.label_emailHelp.setText(QCoreApplication.translate("MainWindow", u"Email : sales@intersense.in", None))
        self.label_supportHelp.setText(QCoreApplication.translate("MainWindow", u"Support : +91 8956029090", None))
        self.label_modelNumberHelp.setText(QCoreApplication.translate("MainWindow", u"Model Number : AG07-P3", None))
        self.label_serialNoHelp.setText(QCoreApplication.translate("MainWindow", u"Serial Number : 232", None))
        self.label_softwareVersionHelp.setText(QCoreApplication.translate("MainWindow", u"Software Version : 0.0", None))
        self.label_setDate.setText(QCoreApplication.translate("MainWindow", u"Date  :", None))
        self.label_day.setText(QCoreApplication.translate("MainWindow", u"Day", None))
        self.label_month.setText(QCoreApplication.translate("MainWindow", u"Month ", None))
        self.label_year.setText(QCoreApplication.translate("MainWindow", u"Year", None))
        self.label_setTime.setText(QCoreApplication.translate("MainWindow", u"Time  :", None))
        self.label_hours.setText(QCoreApplication.translate("MainWindow", u"Hours", None))
        self.label_minutes.setText(QCoreApplication.translate("MainWindow", u"Minutes", None))
        self.pushButton_setDateTime.setText(QCoreApplication.translate("MainWindow", u"Set Date Time", None))
        self.comboBox_shift3FromTimeAmPm.setItemText(0, QCoreApplication.translate("MainWindow", u"AM", None))
        self.comboBox_shift3FromTimeAmPm.setItemText(1, QCoreApplication.translate("MainWindow", u"PM", None))

        self.comboBox_shift2FromTimeAmPm.setItemText(0, QCoreApplication.translate("MainWindow", u"AM", None))
        self.comboBox_shift2FromTimeAmPm.setItemText(1, QCoreApplication.translate("MainWindow", u"PM", None))

        self.label_shift2.setText(QCoreApplication.translate("MainWindow", u"Shift 2", None))
        self.checkBox_shift2.setText("")
        self.label_shift3.setText(QCoreApplication.translate("MainWindow", u" Shift 3", None))
        self.checkBox_shift3.setText("")
        self.comboBox_shift3ToTimeAmPm.setItemText(0, QCoreApplication.translate("MainWindow", u"AM", None))
        self.comboBox_shift3ToTimeAmPm.setItemText(1, QCoreApplication.translate("MainWindow", u"PM", None))

        self.comboBox_shift1FromTimeAmPm.setItemText(0, QCoreApplication.translate("MainWindow", u"AM", None))
        self.comboBox_shift1FromTimeAmPm.setItemText(1, QCoreApplication.translate("MainWindow", u"PM", None))

        self.comboBox_shift2ToTimeAmPm.setItemText(0, QCoreApplication.translate("MainWindow", u"AM", None))
        self.comboBox_shift2ToTimeAmPm.setItemText(1, QCoreApplication.translate("MainWindow", u"PM", None))

        self.label_shiftTo.setText(QCoreApplication.translate("MainWindow", u"To", None))
        self.comboBox_shift1ToTimeAmPm.setItemText(0, QCoreApplication.translate("MainWindow", u"AM", None))
        self.comboBox_shift1ToTimeAmPm.setItemText(1, QCoreApplication.translate("MainWindow", u"PM", None))

        self.label_shift1.setText(QCoreApplication.translate("MainWindow", u"Shift 1", None))
        self.checkBox_shift1.setText("")
        self.label_shiftFrom.setText(QCoreApplication.translate("MainWindow", u"From", None))
        self.label_shiftSettings.setText(QCoreApplication.translate("MainWindow", u"Shift Settings", None))
        self.pushButton_setShiftTiminggs.setText(QCoreApplication.translate("MainWindow", u"Set Shift Timings", None))
        self.button_addMeasurementSettings.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.button_modifyMeasurementSettings.setText(QCoreApplication.translate("MainWindow", u"Modify", None))
        self.button_deleteMeasurementSettings.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.label_activePartName.setText(QCoreApplication.translate("MainWindow", u"Active Part Name  :", None))
        self.button_addCncSettings.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.button_modifyCncSettings.setText(QCoreApplication.translate("MainWindow", u"Modify", None))
        self.button_deleteCncSettings.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.label_cncName.setText(QCoreApplication.translate("MainWindow", u"CNC Name  :", None))
        self.label_cncIpAddress.setText(QCoreApplication.translate("MainWindow", u"IP Address  :", None))
        self.label_cncPortNumber.setText(QCoreApplication.translate("MainWindow", u"Port Number  :", None))
        self.label_cncSelectionType.setText(QCoreApplication.translate("MainWindow", u"CNC Selection  :", None))
        self.comboBox_cncSelectionType.setItemText(0, QCoreApplication.translate("MainWindow", u"Not Applicable", None))
        self.comboBox_cncSelectionType.setItemText(1, QCoreApplication.translate("MainWindow", u"IN1", None))
        self.comboBox_cncSelectionType.setItemText(2, QCoreApplication.translate("MainWindow", u"IN2", None))
        self.comboBox_cncSelectionType.setItemText(3, QCoreApplication.translate("MainWindow", u"IN3", None))
        self.comboBox_cncSelectionType.setItemText(4, QCoreApplication.translate("MainWindow", u"IN4", None))

        self.label_cncController.setText(QCoreApplication.translate("MainWindow", u"Controller  :", None))
        self.comboBox_cncController.setItemText(0, QCoreApplication.translate("MainWindow", u"HAAS", None))
        self.comboBox_cncController.setItemText(1, QCoreApplication.translate("MainWindow", u"FANUC", None))
        self.comboBox_cncController.setItemText(2, QCoreApplication.translate("MainWindow", u"SIEMENS", None))

        self.label_autoOffsetCorrection.setText(QCoreApplication.translate("MainWindow", u"Auto Offset Correction  :", None))
        self.toggleButton_aoc.setText("")
        self.label_aocOnOff.setText(QCoreApplication.translate("MainWindow", u"ON", None))
        self.button_measurementListAoc.setText(QCoreApplication.translate("MainWindow", u"Measurement List", None))
        self.button_cncListAoc.setText(QCoreApplication.translate("MainWindow", u"CNC List", None))
        self.button_reportsAoc.setText(QCoreApplication.translate("MainWindow", u"Reports", None))
        self.label_partNameAoc.setText(QCoreApplication.translate("MainWindow", u"Part Name  :", None))
        self.label_dimensionNoAoc.setText(QCoreApplication.translate("MainWindow", u"Dimension No.  :", None))
        self.comboBox_dimensionNoAoc.setItemText(0, QCoreApplication.translate("MainWindow", u"D1", None))
        self.comboBox_dimensionNoAoc.setItemText(1, QCoreApplication.translate("MainWindow", u"D2", None))
        self.comboBox_dimensionNoAoc.setItemText(2, QCoreApplication.translate("MainWindow", u"D3", None))
        self.comboBox_dimensionNoAoc.setItemText(3, QCoreApplication.translate("MainWindow", u"D4", None))

        self.label_uolAoc.setText(QCoreApplication.translate("MainWindow", u"Upper Offset Limit  :", None))
        self.label_uslAoc.setText(QCoreApplication.translate("MainWindow", u"USL  :", None))
        self.label_uclAoc.setText(QCoreApplication.translate("MainWindow", u"UCL  :", None))
        self.label_nominalAoc.setText(QCoreApplication.translate("MainWindow", u"Nominal Value  :", None))
        self.label_lclAoc.setText(QCoreApplication.translate("MainWindow", u"LCL  :", None))
        self.label_lslAoc.setText(QCoreApplication.translate("MainWindow", u"LSL  :", None))
        self.label_lolAoc.setText(QCoreApplication.translate("MainWindow", u"Lower Offset Limit  :", None))
        self.label_axisAoc.setText(QCoreApplication.translate("MainWindow", u"Axis  :", None))
        self.comboBox_axisAoc.setItemText(0, QCoreApplication.translate("MainWindow", u"x", None))
        self.comboBox_axisAoc.setItemText(1, QCoreApplication.translate("MainWindow", u"y", None))
        self.comboBox_axisAoc.setItemText(2, QCoreApplication.translate("MainWindow", u"z", None))

        self.label_offsetNoAoc.setText(QCoreApplication.translate("MainWindow", u"Offset No.  :", None))
        self.label_machineAoc.setText(QCoreApplication.translate("MainWindow", u"Machine  :", None))
        self.label_nameOfIdentifierAoc.setText(QCoreApplication.translate("MainWindow", u"Name Of Identifier  :", None))
        self.label_startOfIdentifierAoc.setText(QCoreApplication.translate("MainWindow", u"Start Of Identifier  :", None))
        self.label_endOfIdentifierAoc.setText(QCoreApplication.translate("MainWindow", u"End Of Identifier  :", None))
        self.label_startOfDataAoc.setText(QCoreApplication.translate("MainWindow", u"Start Of Data  :", None))
        self.label_endOfDataAoc.setText(QCoreApplication.translate("MainWindow", u"End Of Data  :", None))
        self.label_directionAoc.setText(QCoreApplication.translate("MainWindow", u"Direction  :", None))
        self.label_turretNoAoc.setText(QCoreApplication.translate("MainWindow", u"Turret No.  :", None))
        self.label_networkBasedDatabase.setText(QCoreApplication.translate("MainWindow", u"Network Based Database  :", None))
        self.toggleButton_networkBasedDatabase.setText("")
        self.label_networkBasedDatabaseOnOff.setText(QCoreApplication.translate("MainWindow", u"ON", None))
        self.label_driverNameDb.setText(QCoreApplication.translate("MainWindow", u"MS SQL Driver Name  :", None))
        self.label_serverNameDb.setText(QCoreApplication.translate("MainWindow", u"MS SQL Server Name  :", None))
        self.label_databaseNameDb.setText(QCoreApplication.translate("MainWindow", u"MS SQL Database Name  :", None))
        self.label_username_Db.setText(QCoreApplication.translate("MainWindow", u"MS SQL Username  :", None))
        self.label_passwordDb.setText(QCoreApplication.translate("MainWindow", u"MS SQL Password  :", None))
        self.label_programIdforSettings.setText(QCoreApplication.translate("MainWindow", u"Program ID :", None))
        self.label_programNameSettings.setText(QCoreApplication.translate("MainWindow", u"Program Name :", None))
        self.button_staticSettingsForAll.setText(QCoreApplication.translate("MainWindow", u"Setting", None))
        self.label_probeSetting.setText(QCoreApplication.translate("MainWindow", u"Probe Setting : ", None))
        self.comboBox_toselectProbe.setItemText(0, QCoreApplication.translate("MainWindow", u"D1", None))
        self.comboBox_toselectProbe.setItemText(1, QCoreApplication.translate("MainWindow", u"D2", None))
        self.comboBox_toselectProbe.setItemText(2, QCoreApplication.translate("MainWindow", u"D3", None))
        self.comboBox_toselectProbe.setItemText(3, QCoreApplication.translate("MainWindow", u"D4", None))
        self.comboBox_toselectProbe.setItemText(4, QCoreApplication.translate("MainWindow", u"D5", None))
        self.comboBox_toselectProbe.setItemText(5, QCoreApplication.translate("MainWindow", u"D6", None))
        self.comboBox_toselectProbe.setItemText(6, QCoreApplication.translate("MainWindow", u"D7", None))
        self.comboBox_toselectProbe.setItemText(7, QCoreApplication.translate("MainWindow", u"D8", None))

        self.label_formula.setText(QCoreApplication.translate("MainWindow", u"Formula :", None))
        self.label_formulaBar.setText(QCoreApplication.translate("MainWindow", u"Formula Bar", None))
        self.button_setFormulaSettings.setText(QCoreApplication.translate("MainWindow", u"Set Formula", None))
        self.label_masterType.setText(QCoreApplication.translate("MainWindow", u"Master Type :", None))
        self.comboBox_masterType.setItemText(0, QCoreApplication.translate("MainWindow", u"Single Master", None))
        self.comboBox_masterType.setItemText(1, QCoreApplication.translate("MainWindow", u"Double Master", None))

        self.label_masterLower.setText(QCoreApplication.translate("MainWindow", u"Master Lower :", None))
        self.label_master.setText(QCoreApplication.translate("MainWindow", u"Master :", None))
        self.label_masterHigher.setText(QCoreApplication.translate("MainWindow", u"Master Higher :", None))
        self.label_upperOffsetLimit.setText(QCoreApplication.translate("MainWindow", u"Upper Offset Limit  :", None))
        self.label_usl.setText(QCoreApplication.translate("MainWindow", u"USL :", None))
        self.label_ucl.setText(QCoreApplication.translate("MainWindow", u"UCL :", None))
        self.label_nominalValue.setText(QCoreApplication.translate("MainWindow", u"Nominal Value :", None))
        self.label_lcl.setText(QCoreApplication.translate("MainWindow", u"LCL :", None))
        self.label_lsl.setText(QCoreApplication.translate("MainWindow", u"LSL :", None))
        self.label_lowerOffsetLimit.setText(QCoreApplication.translate("MainWindow", u"Lower Offset Limit :", None))
        self.label_ovality.setText(QCoreApplication.translate("MainWindow", u"Ovality :", None))
        self.comboBox_ovalityOnOff.setItemText(0, QCoreApplication.translate("MainWindow", u"On", None))
        self.comboBox_ovalityOnOff.setItemText(1, QCoreApplication.translate("MainWindow", u"Off", None))

        self.label_range.setText(QCoreApplication.translate("MainWindow", u"Range :", None))
        self.label_method.setText(QCoreApplication.translate("MainWindow", u"Method :", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("MainWindow", u"OD", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("MainWindow", u"ID", None))

        self.label_case.setText(QCoreApplication.translate("MainWindow", u"Case :", None))
        self.comboBox_4.setItemText(0, QCoreApplication.translate("MainWindow", u"Delta", None))
        self.comboBox_4.setItemText(1, QCoreApplication.translate("MainWindow", u"Min", None))
        self.comboBox_4.setItemText(2, QCoreApplication.translate("MainWindow", u"Max", None))

        self.label_caseT.setText(QCoreApplication.translate("MainWindow", u"CaseT :", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"                            Probe Based Settings                            ", None))
        self.label_axis.setText(QCoreApplication.translate("MainWindow", u"Axis : ", None))
        self.comboBox_axis.setItemText(0, QCoreApplication.translate("MainWindow", u"x", None))
        self.comboBox_axis.setItemText(1, QCoreApplication.translate("MainWindow", u"y", None))
        self.comboBox_axis.setItemText(2, QCoreApplication.translate("MainWindow", u"z", None))

        self.label_offsetNo.setText(QCoreApplication.translate("MainWindow", u"Offset No :", None))
        self.label_machine.setText(QCoreApplication.translate("MainWindow", u"Machine :", None))
        self.label_direction.setText(QCoreApplication.translate("MainWindow", u"Direction :", None))
        self.comboBox_direction.setItemText(0, QCoreApplication.translate("MainWindow", u"p", None))
        self.comboBox_direction.setItemText(1, QCoreApplication.translate("MainWindow", u"n", None))

        self.label_setPath.setText(QCoreApplication.translate("MainWindow", u"Turret No :", None))
        self.label_buzzerAoc.setText(QCoreApplication.translate("MainWindow", u"Buffer Part No  :", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"                                   AOC Settings                             ", None))
        self.label_fromDate.setText(QCoreApplication.translate("MainWindow", u"01/01/2025", None))
        self.button_fromDate.setText(QCoreApplication.translate("MainWindow", u"Set From Date", None))
        self.label_toDate.setText(QCoreApplication.translate("MainWindow", u"01/09/2025", None))
        self.button_toDate.setText(QCoreApplication.translate("MainWindow", u"Set To Date", None))
        self.button_export.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"SPC Data Count  :", None))
        self.button_spcDataCount.setText(QCoreApplication.translate("MainWindow", u"Set SPC Data Count", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Probe  :", None))
        self.comboBox_probeCalibrate.setItemText(0, QCoreApplication.translate("MainWindow", u"P1", None))
        self.comboBox_probeCalibrate.setItemText(1, QCoreApplication.translate("MainWindow", u"P2", None))

        self.label_lowerMasterCalibrate.setText(QCoreApplication.translate("MainWindow", u"Lower Master  :", None))
        self.label_higherMasterCalibrate.setText(QCoreApplication.translate("MainWindow", u"Higher Master  :", None))
        self.button_calibrateLower.setText(QCoreApplication.translate("MainWindow", u"Calibrate Lower", None))
        self.button_calibrateHigher.setText(QCoreApplication.translate("MainWindow", u"Calibrate Higher", None))
        self.button_setToFactorySettingsCalibration.setText(QCoreApplication.translate("MainWindow", u"Set To Factory Settings", None))
        self.button_resetToFactorySettingsCalibration.setText(QCoreApplication.translate("MainWindow", u"Reset To Factory Settings", None))
        self.label_airSavingMode.setText(QCoreApplication.translate("MainWindow", u"Air Saving Mode  :", None))
        self.toggleButton_airSavingMode.setText("")
        self.label_airSavingModeOnOff.setText(QCoreApplication.translate("MainWindow", u"ON", None))
        self.label_airChannel.setText(QCoreApplication.translate("MainWindow", u"Air Channel  :", None))
        self.comboBox_airChannel.setItemText(0, QCoreApplication.translate("MainWindow", u"A1", None))
        self.comboBox_airChannel.setItemText(1, QCoreApplication.translate("MainWindow", u"A2", None))

        self.label_airSensesitivityQuotient.setText(QCoreApplication.translate("MainWindow", u"Air Sensitivity Quotient For Air Channel  :", None))
        self.button_setAirSensitivity.setText(QCoreApplication.translate("MainWindow", u"Set", None))
        self.label_ReportfromDate.setText(QCoreApplication.translate("MainWindow", u"From Date  :", None))
        self.label_ReportfromDateVal.setText(QCoreApplication.translate("MainWindow", u"01-01-2025", None))
        self.pushButton_selectFromDate.setText(QCoreApplication.translate("MainWindow", u"Select From Date", None))
        self.label_ReportToDate.setText(QCoreApplication.translate("MainWindow", u"To Date  :", None))
        self.label_ReportToDateVal.setText(QCoreApplication.translate("MainWindow", u"01-01-2025", None))
        self.pushButton_SelectToDate.setText(QCoreApplication.translate("MainWindow", u"Select To Date", None))
        self.label_programId.setText(QCoreApplication.translate("MainWindow", u"Program ID :", None))
        self.label_dimension.setText(QCoreApplication.translate("MainWindow", u"Dimension : ", None))
        self.button_viewData.setText(QCoreApplication.translate("MainWindow", u"View Data", None))
        self.button_exportData.setText(QCoreApplication.translate("MainWindow", u"Export Data", None))
        self.button_deleteData.setText(QCoreApplication.translate("MainWindow", u"Delete Data", None))
        self.label_dateselectReport.setText(QCoreApplication.translate("MainWindow", u"Date :", None))
        self.label_reportshowdate.setText(QCoreApplication.translate("MainWindow", u"01-01-2025  TO  01-01-2025", None))
        self.label_programIdreport.setText(QCoreApplication.translate("MainWindow", u"Program ID :", None))
        self.label_IdProgramReport.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_DimensionForReport.setText(QCoreApplication.translate("MainWindow", u"Dimension :", None))
        self.label_DimensionIdForReport.setText(QCoreApplication.translate("MainWindow", u"D1", None))
        self.button_ListView.setText(QCoreApplication.translate("MainWindow", u"List View", None))
        self.button_ChartView.setText(QCoreApplication.translate("MainWindow", u"Chart View", None))
        self.button_HistogramChart.setText(QCoreApplication.translate("MainWindow", u"Histogram Chart", None))
        self.label_dialIndicatorPage.setText("")
        self.label_settingsPage.setText("")
        self.label_ioSettingPage.setText("")
        self.label_autoOffsetSettingPage.setText("")
        self.label_clockSettingsPage.setText("")
        self.label_userManagementPage.setText("")
        self.label_reportPage.setText("")
        self.label_aboutLogoPage.setText("")
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"A", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"B", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"C", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"D", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"E", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"F", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"G", None))
        self.comboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"H", None))

        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.button_angleCalculationSetting.setText(QCoreApplication.translate("MainWindow", u"Angle Calculation ", None))
        self.label_modeForCombineIndividual.setText(QCoreApplication.translate("MainWindow", u"Mode :", None))
        self.radioButton_modeCombine.setText(QCoreApplication.translate("MainWindow", u"Combine", None))
        self.radioButton_modeIndividual.setText(QCoreApplication.translate("MainWindow", u"Individual", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"UOM :", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"Inch", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"MM", None))
        self.label_DurationForAutosave.setText(QCoreApplication.translate("MainWindow", u"Duration For Autosave :", None))
        self.pushButton_autosenseRange.setText(QCoreApplication.translate("MainWindow", u"Autosense Range ", None))
        self.label_angleCalculation.setText(QCoreApplication.translate("MainWindow", u"Angle Calculation :", None))
        self.toggelButton_angleCalculation.setText("")
        self.label_angleCalculationONOff.setText(QCoreApplication.translate("MainWindow", u"ON", None))
        self.label_angleCalculationMasterAngle.setText(QCoreApplication.translate("MainWindow", u"Master Angle :", None))
        self.label_80.setText(QCoreApplication.translate("MainWindow", u"\u00b0", None))
        self.label_81.setText(QCoreApplication.translate("MainWindow", u"'", None))
        self.label_82.setText(QCoreApplication.translate("MainWindow", u"\"", None))
        self.label_positiveTol.setText(QCoreApplication.translate("MainWindow", u"+ Tolerance :", None))
        self.label_83.setText(QCoreApplication.translate("MainWindow", u"'", None))
        self.label_84.setText(QCoreApplication.translate("MainWindow", u"\"", None))
        self.label_negativeTol.setText(QCoreApplication.translate("MainWindow", u"-Tolerance :", None))
        self.label_85.setText(QCoreApplication.translate("MainWindow", u"'", None))
        self.label_86.setText(QCoreApplication.translate("MainWindow", u"\"", None))
        self.label_Distance.setText(QCoreApplication.translate("MainWindow", u"Distance :", None))
        self.label_distanceInMm.setText(QCoreApplication.translate("MainWindow", u"mm", None))
        self.label_Angle.setText(QCoreApplication.translate("MainWindow", u"Angle :", None))
        self.radioButton_halfAngle.setText(QCoreApplication.translate("MainWindow", u"Half Angle ", None))
        self.radioButton_2_fullAngle.setText(QCoreApplication.translate("MainWindow", u" Full Angle", None))
        self.label_programIdOnSetMaster.setText(QCoreApplication.translate("MainWindow", u"Program Id :", None))
        self.label_programNamOnSetMAster.setText(QCoreApplication.translate("MainWindow", u"Program Name :", None))
        self.label_programName.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_masterSetting.setText(QCoreApplication.translate("MainWindow", u"Master Setting :", None))
        self.button_setMaster.setText(QCoreApplication.translate("MainWindow", u"Set Master", None))
        self.button_programList.setText(QCoreApplication.translate("MainWindow", u"Program List", None))
        self.button_partSettings.setText(QCoreApplication.translate("MainWindow", u"Part Settings ", None))
        self.label_liveD1Val.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_masterD1_1.setText(QCoreApplication.translate("MainWindow", u"Master Lower D1 :", None))
        self.label_valMasterD1_1.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_masterD1_2.setText(QCoreApplication.translate("MainWindow", u"Master Higher D1 :", None))
        self.label_valMasterD1_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_liveD2Val.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_masterD2_1.setText(QCoreApplication.translate("MainWindow", u"Master Lower D2 :", None))
        self.label_valMasterD2_1.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_masterD2_2.setText(QCoreApplication.translate("MainWindow", u"Master Higher D2 :", None))
        self.label_valMasterD2_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_liveD3Val.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_masterD3_1.setText(QCoreApplication.translate("MainWindow", u"Master Lower D3 :", None))
        self.label_valMasterD3_1.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_masterD3_2.setText(QCoreApplication.translate("MainWindow", u"Master Higher D3 :", None))
        self.label_valMasterD3_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_liveD4val.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_masterD4_1.setText(QCoreApplication.translate("MainWindow", u"Master Lower D4 :", None))
        self.label_valMasterD4_1.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_masterD4_2.setText(QCoreApplication.translate("MainWindow", u"Master Higher D4 :", None))
        self.label_valMasterD4_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_liveD5Val.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_masterD5_1.setText(QCoreApplication.translate("MainWindow", u"Master Lower D5 :", None))
        self.label_valMasterD5_1.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_masterD5_2.setText(QCoreApplication.translate("MainWindow", u"Master Higher D5 :", None))
        self.label_valMasterD5_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_liveD6Val.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_masterD6_1.setText(QCoreApplication.translate("MainWindow", u"Master Lower D6 :", None))
        self.label_valMasterD6_1.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_masterD6_2.setText(QCoreApplication.translate("MainWindow", u"Master Higher D6 :", None))
        self.label_valMasterD6_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_liveD7val.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_masterD7_1.setText(QCoreApplication.translate("MainWindow", u"Master Lower D7 :", None))
        self.label_valMasterD7_1.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_masterD7_2.setText(QCoreApplication.translate("MainWindow", u"Master Higher D7 :", None))
        self.label_valMasterD7_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_liveD8Val.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_masterD8_1.setText(QCoreApplication.translate("MainWindow", u"Master Lower D8 :", None))
        self.label_valMasterD8_1.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_masterD8_2.setText(QCoreApplication.translate("MainWindow", u"Master Higher D8 :", None))
        self.label_valMasterD8_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.button_back.setText("")
        self.button_save.setText("")
        self.button_forward.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.button_home.setText(QCoreApplication.translate("MainWindow", u"...", None))
    # retranslateUi

