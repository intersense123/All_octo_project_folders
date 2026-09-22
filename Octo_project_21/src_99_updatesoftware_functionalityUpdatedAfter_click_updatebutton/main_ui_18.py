import resources_rc
# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_ui_23_new_aoc_new4_withoutstatusbar_2_new_workinglatest.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
    QSpacerItem, QStackedWidget, QTabWidget, QTableView,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 481)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(800, 480))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        MainWindow.setSizeIncrement(QSize(0, 0))
        font = QFont()
        font.setFamilies([u"MS Shell Dlg 2"])
        font.setPointSize(12)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"\n"
"QWidget {\n"
"    background-color: black;\n"
"    color: #ffffff;\n"
"	 font-family: \"MS Shell Dlg 2\";\n"
"}\n"
"QLabel{\n"
"	 font-size: 13pt;\n"
"     min-height:35px;\n"
"}\n"
"QLineEdit{\n"
"	 font-size: 13pt;\n"
"	 min-height:33px;\n"
"	 border: 1px solid #888888;\n"
"	 border-radius: 1px;\n"
"\n"
"}\n"
"QComboBox{\n"
"	 font-size: 13pt;\n"
"	 min-height:33px;\n"
"	 border: 1px solid #888888;\n"
"     border-radius: 1px;\n"
"\n"
"}\n"
"/* All push buttons */\n"
"QPushButton {\n"
"    background-color: #444444;   /* grey background */\n"
"    color: white;                /* text color */\n"
"    font-size: 13pt;\n"
"    border: 1px solid #888888;   /* grey border */\n"
"    border-radius: 2px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #666666;\n"
"	\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #222222;\n"
"}\n"
"\n"
"QFrame[orientation=\"Horizontal\"] {\n"
"    background-color: #555555;\n"
"     height: 2px;\n"
"\n"
"}\n"
"\n"
"QFrame[orientation=\"Vertical\"] {\n"
"    "
                        "background-color: #555555;\n"
"    width: 2px;\n"
" \n"
"}\n"
"\n"
"/* Radio buttons */\n"
"QRadioButton {\n"
"    font-size: 13pt;          /* text size */\n"
"    color: #ffffff;           /* text color */\n"
"    spacing: 5px;             /* space between circle and text */\n"
"}\n"
"\n"
"/* Circle size */\n"
"QRadioButton::indicator {\n"
"    width: 20px;\n"
"    height: 25px;\n"
"    border-radius: 11px;\n"
"    border: 2px solid #aaaaaa;\n"
"    background-color: black;  /* outer circle background */\n"
"}\n"
"\n"
"/* Unchecked circle */\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color: black;\n"
"}\n"
"\n"
"/* Checked circle: use radial gradient to simulate inner dot */\n"
"QRadioButton::indicator:checked {\n"
"    background-color: qradialgradient(\n"
"        cx:0.5, cy:0.5, radius:0.5,\n"
"        fx:0.5, fy:0.5,\n"
"        stop:0 #fec222,       /* inner dot color */\n"
"        stop:0.6 #2b2b2b      /* outer circle color */\n"
"    );\n"
"}\n"
"QWidget:disabled {\n"
"    color: #777"
                        "777;\n"
"    background-color: black;\n"
"}\n"
"\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Headerwidget = QWidget(self.centralwidget)
        self.Headerwidget.setObjectName(u"Headerwidget")
        self.Headerwidget.setMinimumSize(QSize(0, 30))
        self.Headerwidget.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setFamilies([u"MS Shell Dlg 2"])
        font1.setPointSize(13)
        self.Headerwidget.setFont(font1)
        self.horizontalLayout_62 = QHBoxLayout(self.Headerwidget)
        self.horizontalLayout_62.setSpacing(4)
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.horizontalLayout_62.setContentsMargins(0, 0, 0, 0)
        self.label_pageName = QLabel(self.Headerwidget)
        self.label_pageName.setObjectName(u"label_pageName")
        sizePolicy.setHeightForWidth(self.label_pageName.sizePolicy().hasHeightForWidth())
        self.label_pageName.setSizePolicy(sizePolicy)
        self.label_pageName.setMinimumSize(QSize(165, 35))
        self.label_pageName.setMaximumSize(QSize(16777215, 16777215))
        self.label_pageName.setFont(font1)

        self.horizontalLayout_62.addWidget(self.label_pageName, 0, Qt.AlignmentFlag.AlignHCenter)

        self.line_17 = QFrame(self.Headerwidget)
        self.line_17.setObjectName(u"line_17")
        self.line_17.setMinimumSize(QSize(0, 20))
        self.line_17.setFrameShape(QFrame.Shape.VLine)
        self.line_17.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_62.addWidget(self.line_17)

        self.label_statusBar = QLabel(self.Headerwidget)
        self.label_statusBar.setObjectName(u"label_statusBar")
        self.label_statusBar.setMinimumSize(QSize(390, 35))
        self.label_statusBar.setMaximumSize(QSize(16777215, 16777215))
        font2 = QFont()
        font2.setFamilies([u"MS Shell Dlg 2"])
        font2.setPointSize(13)
        font2.setBold(True)
        font2.setItalic(False)
        font2.setUnderline(False)
        font2.setStrikeOut(False)
        font2.setKerning(True)
        self.label_statusBar.setFont(font2)
        self.label_statusBar.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_statusBar.setWordWrap(False)

        self.horizontalLayout_62.addWidget(self.label_statusBar)

        self.line_20 = QFrame(self.Headerwidget)
        self.line_20.setObjectName(u"line_20")
        self.line_20.setMinimumSize(QSize(0, 15))
        self.line_20.setFrameShape(QFrame.Shape.VLine)
        self.line_20.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_62.addWidget(self.line_20)

        self.label_date = QLabel(self.Headerwidget)
        self.label_date.setObjectName(u"label_date")
        sizePolicy.setHeightForWidth(self.label_date.sizePolicy().hasHeightForWidth())
        self.label_date.setSizePolicy(sizePolicy)
        self.label_date.setMinimumSize(QSize(0, 35))
        self.label_date.setMaximumSize(QSize(16777215, 16777215))
        self.label_date.setFont(font1)

        self.horizontalLayout_62.addWidget(self.label_date)

        self.line_13 = QFrame(self.Headerwidget)
        self.line_13.setObjectName(u"line_13")
        self.line_13.setFrameShape(QFrame.Shape.VLine)
        self.line_13.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_62.addWidget(self.line_13)

        self.label_time = QLabel(self.Headerwidget)
        self.label_time.setObjectName(u"label_time")
        sizePolicy.setHeightForWidth(self.label_time.sizePolicy().hasHeightForWidth())
        self.label_time.setSizePolicy(sizePolicy)
        self.label_time.setMinimumSize(QSize(0, 35))
        self.label_time.setMaximumSize(QSize(16777215, 16777215))
        self.label_time.setFont(font1)

        self.horizontalLayout_62.addWidget(self.label_time)


        self.verticalLayout.addWidget(self.Headerwidget)

        self.line_9 = QFrame(self.centralwidget)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setMinimumSize(QSize(0, 2))
        self.line_9.setMaximumSize(QSize(16777215, 16777215))
        font3 = QFont()
        font3.setFamilies([u"MS Shell Dlg 2"])
        font3.setPointSize(5)
        self.line_9.setFont(font3)
        self.line_9.setFrameShape(QFrame.Shape.HLine)
        self.line_9.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_9)

        self.stackedWidget_main = QStackedWidget(self.centralwidget)
        self.stackedWidget_main.setObjectName(u"stackedWidget_main")
        self.stackedWidget_main.setMinimumSize(QSize(0, 370))
        self.stackedWidget_main.setMaximumSize(QSize(16777215, 16777215))
        self.stackedWidget_main.setFont(font)
        self.page1 = QWidget()
        self.page1.setObjectName(u"page1")
        self.page1Layout = QVBoxLayout(self.page1)
        self.page1Layout.setObjectName(u"page1Layout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.page1)
        self.label_3.setObjectName(u"label_3")
        font4 = QFont()
        font4.setFamilies([u"MS Shell Dlg 2"])
        font4.setPointSize(13)
        font4.setBold(True)
        self.label_3.setFont(font4)

        self.horizontalLayout_4.addWidget(self.label_3, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignBottom)


        self.page1Layout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_username = QLabel(self.page1)
        self.label_username.setObjectName(u"label_username")
        self.label_username.setFont(font4)

        self.horizontalLayout.addWidget(self.label_username, 0, Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignBottom)

        self.lineEdit_usernameLogin = QLineEdit(self.page1)
        self.lineEdit_usernameLogin.setObjectName(u"lineEdit_usernameLogin")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEdit_usernameLogin.sizePolicy().hasHeightForWidth())
        self.lineEdit_usernameLogin.setSizePolicy(sizePolicy1)
        self.lineEdit_usernameLogin.setFont(font1)

        self.horizontalLayout.addWidget(self.lineEdit_usernameLogin, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignBottom)


        self.page1Layout.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 25, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.page1Layout.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_password = QLabel(self.page1)
        self.label_password.setObjectName(u"label_password")
        self.label_password.setFont(font4)

        self.horizontalLayout_2.addWidget(self.label_password, 0, Qt.AlignmentFlag.AlignRight)

        self.lineEdit_passwordLogin = QLineEdit(self.page1)
        self.lineEdit_passwordLogin.setObjectName(u"lineEdit_passwordLogin")
        sizePolicy1.setHeightForWidth(self.lineEdit_passwordLogin.sizePolicy().hasHeightForWidth())
        self.lineEdit_passwordLogin.setSizePolicy(sizePolicy1)
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
        self.button_login.setMinimumSize(QSize(90, 40))
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
        self.button_addLoginDetails = QPushButton(self.page2)
        self.button_addLoginDetails.setObjectName(u"button_addLoginDetails")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.button_addLoginDetails.sizePolicy().hasHeightForWidth())
        self.button_addLoginDetails.setSizePolicy(sizePolicy2)
        self.button_addLoginDetails.setMinimumSize(QSize(80, 40))
        self.button_addLoginDetails.setFont(font1)

        self.horizontalLayout_5.addWidget(self.button_addLoginDetails, 0, Qt.AlignmentFlag.AlignHCenter)

        self.button_modifyLogin = QPushButton(self.page2)
        self.button_modifyLogin.setObjectName(u"button_modifyLogin")
        self.button_modifyLogin.setMinimumSize(QSize(80, 40))
        self.button_modifyLogin.setFont(font1)

        self.horizontalLayout_5.addWidget(self.button_modifyLogin, 0, Qt.AlignmentFlag.AlignHCenter)

        self.button_deleteLogin = QPushButton(self.page2)
        self.button_deleteLogin.setObjectName(u"button_deleteLogin")
        self.button_deleteLogin.setMinimumSize(QSize(80, 40))
        self.button_deleteLogin.setFont(font1)

        self.horizontalLayout_5.addWidget(self.button_deleteLogin, 0, Qt.AlignmentFlag.AlignHCenter)


        self.page2Layout.addLayout(self.horizontalLayout_5)

        self.verticalSpacer_59 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.page2Layout.addItem(self.verticalSpacer_59)

        self.tableview_loginList = QTableView(self.page2)
        self.tableview_loginList.setObjectName(u"tableview_loginList")
        self.tableview_loginList.setMinimumSize(QSize(0, 0))

        self.page2Layout.addWidget(self.tableview_loginList)

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
        sizePolicy1.setHeightForWidth(self.lineEdit_setUsernameLogin.sizePolicy().hasHeightForWidth())
        self.lineEdit_setUsernameLogin.setSizePolicy(sizePolicy1)
        self.lineEdit_setUsernameLogin.setMinimumSize(QSize(180, 35))
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
        sizePolicy1.setHeightForWidth(self.lineEdit_setPasswordLogin.sizePolicy().hasHeightForWidth())
        self.lineEdit_setPasswordLogin.setSizePolicy(sizePolicy1)
        self.lineEdit_setPasswordLogin.setMinimumSize(QSize(180, 35))
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
        self.comboBox_setAccessCombo.setObjectName(u"comboBox_setAccessCombo")
        self.comboBox_setAccessCombo.setMinimumSize(QSize(180, 35))
        self.comboBox_setAccessCombo.setFont(font1)

        self.horizontalLayout_9.addWidget(self.comboBox_setAccessCombo, 0, Qt.AlignmentFlag.AlignLeft)


        self.page3Layout.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.button_addUpdateLogin = QPushButton(self.page3)
        self.button_addUpdateLogin.setObjectName(u"button_addUpdateLogin")
        self.button_addUpdateLogin.setMinimumSize(QSize(140, 30))
        self.button_addUpdateLogin.setMaximumSize(QSize(16777215, 40))
        self.button_addUpdateLogin.setFont(font1)

        self.horizontalLayout_10.addWidget(self.button_addUpdateLogin, 0, Qt.AlignmentFlag.AlignHCenter)


        self.page3Layout.addLayout(self.horizontalLayout_10)

        self.stackedWidget_main.addWidget(self.page3)
        self.page4 = QWidget()
        self.page4.setObjectName(u"page4")
        self.page4Layout = QVBoxLayout(self.page4)
        self.page4Layout.setObjectName(u"page4Layout")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_5 = QSpacerItem(40, 40, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_5)

        self.label_rs232 = QLabel(self.page4)
        self.label_rs232.setObjectName(u"label_rs232")
        self.label_rs232.setMinimumSize(QSize(0, 35))
        self.label_rs232.setFont(font1)

        self.horizontalLayout_8.addWidget(self.label_rs232, 0, Qt.AlignmentFlag.AlignRight)

        self.toggleButton_rs232 = QLabel(self.page4)
        self.toggleButton_rs232.setObjectName(u"toggleButton_rs232")
        self.toggleButton_rs232.setMinimumSize(QSize(60, 35))
        self.toggleButton_rs232.setPixmap(QPixmap(u"../home/torizon/app/src/Switcher_On.png"))

        self.horizontalLayout_8.addWidget(self.toggleButton_rs232, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalSpacer_6 = QSpacerItem(40, 40, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_6)


        self.page4Layout.addLayout(self.horizontalLayout_8)

        self.line = QFrame(self.page4)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.page4Layout.addWidget(self.line)

        self.verticalSpacer_3 = QSpacerItem(20, 35, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.page4Layout.addItem(self.verticalSpacer_3)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalSpacer_182 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_182)

        self.label_baudRate = QLabel(self.page4)
        self.label_baudRate.setObjectName(u"label_baudRate")
        self.label_baudRate.setFont(font1)

        self.horizontalLayout_11.addWidget(self.label_baudRate, 0, Qt.AlignmentFlag.AlignRight)

        self.comboBox_baudRate = QComboBox(self.page4)
        self.comboBox_baudRate.addItem("")
        self.comboBox_baudRate.addItem("")
        self.comboBox_baudRate.addItem("")
        self.comboBox_baudRate.addItem("")
        self.comboBox_baudRate.addItem("")
        self.comboBox_baudRate.setObjectName(u"comboBox_baudRate")
        sizePolicy1.setHeightForWidth(self.comboBox_baudRate.sizePolicy().hasHeightForWidth())
        self.comboBox_baudRate.setSizePolicy(sizePolicy1)
        self.comboBox_baudRate.setMinimumSize(QSize(150, 35))
        self.comboBox_baudRate.setMaximumSize(QSize(16777215, 16777215))
        self.comboBox_baudRate.setFont(font1)

        self.horizontalLayout_11.addWidget(self.comboBox_baudRate, 0, Qt.AlignmentFlag.AlignLeft)

        self.horizontalSpacer_183 = QSpacerItem(70, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_183)

        self.label_dataBits = QLabel(self.page4)
        self.label_dataBits.setObjectName(u"label_dataBits")
        self.label_dataBits.setFont(font1)

        self.horizontalLayout_11.addWidget(self.label_dataBits, 0, Qt.AlignmentFlag.AlignRight)

        self.comboBox_dataBits = QComboBox(self.page4)
        self.comboBox_dataBits.addItem("")
        self.comboBox_dataBits.addItem("")
        self.comboBox_dataBits.addItem("")
        self.comboBox_dataBits.addItem("")
        self.comboBox_dataBits.setObjectName(u"comboBox_dataBits")
        self.comboBox_dataBits.setMinimumSize(QSize(150, 35))
        self.comboBox_dataBits.setMaximumSize(QSize(16777215, 16777215))
        self.comboBox_dataBits.setFont(font1)

        self.horizontalLayout_11.addWidget(self.comboBox_dataBits, 0, Qt.AlignmentFlag.AlignLeft)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_2)


        self.page4Layout.addLayout(self.horizontalLayout_11)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.page4Layout.addItem(self.verticalSpacer_4)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalSpacer_180 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_180)

        self.label_parity = QLabel(self.page4)
        self.label_parity.setObjectName(u"label_parity")
        self.label_parity.setFont(font1)

        self.horizontalLayout_12.addWidget(self.label_parity, 0, Qt.AlignmentFlag.AlignRight)

        self.comboBox_parity = QComboBox(self.page4)
        self.comboBox_parity.addItem("")
        self.comboBox_parity.addItem("")
        self.comboBox_parity.addItem("")
        self.comboBox_parity.addItem("")
        self.comboBox_parity.addItem("")
        self.comboBox_parity.setObjectName(u"comboBox_parity")
        self.comboBox_parity.setMinimumSize(QSize(150, 35))
        self.comboBox_parity.setMaximumSize(QSize(16777215, 16777215))
        self.comboBox_parity.setFont(font1)

        self.horizontalLayout_12.addWidget(self.comboBox_parity, 0, Qt.AlignmentFlag.AlignLeft)

        self.horizontalSpacer_181 = QSpacerItem(70, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_181)

        self.label_stopBits = QLabel(self.page4)
        self.label_stopBits.setObjectName(u"label_stopBits")
        self.label_stopBits.setFont(font1)

        self.horizontalLayout_12.addWidget(self.label_stopBits, 0, Qt.AlignmentFlag.AlignRight)

        self.comboBox_stopBits = QComboBox(self.page4)
        self.comboBox_stopBits.addItem("")
        self.comboBox_stopBits.addItem("")
        self.comboBox_stopBits.addItem("")
        self.comboBox_stopBits.setObjectName(u"comboBox_stopBits")
        self.comboBox_stopBits.setMinimumSize(QSize(150, 35))
        self.comboBox_stopBits.setMaximumSize(QSize(16777215, 16777215))
        self.comboBox_stopBits.setFont(font1)

        self.horizontalLayout_12.addWidget(self.comboBox_stopBits, 0, Qt.AlignmentFlag.AlignLeft)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_3)


        self.page4Layout.addLayout(self.horizontalLayout_12)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.page4Layout.addItem(self.verticalSpacer_5)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalSpacer_140 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_140)

        self.label_flowControl = QLabel(self.page4)
        self.label_flowControl.setObjectName(u"label_flowControl")
        self.label_flowControl.setFont(font1)

        self.horizontalLayout_13.addWidget(self.label_flowControl, 0, Qt.AlignmentFlag.AlignRight)

        self.comboBox_flowControl = QComboBox(self.page4)
        self.comboBox_flowControl.addItem("")
        self.comboBox_flowControl.addItem("")
        self.comboBox_flowControl.addItem("")
        self.comboBox_flowControl.setObjectName(u"comboBox_flowControl")
        self.comboBox_flowControl.setMinimumSize(QSize(150, 35))
        self.comboBox_flowControl.setMaximumSize(QSize(16777215, 16777215))
        self.comboBox_flowControl.setFont(font1)

        self.horizontalLayout_13.addWidget(self.comboBox_flowControl, 0, Qt.AlignmentFlag.AlignLeft)

        self.horizontalSpacer_136 = QSpacerItem(70, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_136)

        self.label_portName = QLabel(self.page4)
        self.label_portName.setObjectName(u"label_portName")
        self.label_portName.setFont(font1)

        self.horizontalLayout_13.addWidget(self.label_portName, 0, Qt.AlignmentFlag.AlignRight)

        self.lineEdit_portName = QLineEdit(self.page4)
        self.lineEdit_portName.setObjectName(u"lineEdit_portName")
        sizePolicy1.setHeightForWidth(self.lineEdit_portName.sizePolicy().hasHeightForWidth())
        self.lineEdit_portName.setSizePolicy(sizePolicy1)
        self.lineEdit_portName.setMaximumSize(QSize(150, 16777215))
        self.lineEdit_portName.setFont(font1)

        self.horizontalLayout_13.addWidget(self.lineEdit_portName, 0, Qt.AlignmentFlag.AlignLeft)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_4)


        self.page4Layout.addLayout(self.horizontalLayout_13)

        self.verticalSpacer_6 = QSpacerItem(20, 50, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.page4Layout.addItem(self.verticalSpacer_6)

        self.stackedWidget_main.addWidget(self.page4)
        self.page5 = QWidget()
        self.page5.setObjectName(u"page5")
        self.page5Layout = QVBoxLayout(self.page5)
        self.page5Layout.setObjectName(u"page5Layout")
        self.horizontalLayout_83 = QHBoxLayout()
        self.horizontalLayout_83.setObjectName(u"horizontalLayout_83")
        self.horizontalSpacer_117 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_83.addItem(self.horizontalSpacer_117)

        self.label_dimensionFormulaBar = QLabel(self.page5)
        self.label_dimensionFormulaBar.setObjectName(u"label_dimensionFormulaBar")
        self.label_dimensionFormulaBar.setMaximumSize(QSize(50, 16777215))
        self.label_dimensionFormulaBar.setFont(font1)

        self.horizontalLayout_83.addWidget(self.label_dimensionFormulaBar, 0, Qt.AlignmentFlag.AlignHCenter)

        self.lineEdit_formulaBar = QLineEdit(self.page5)
        self.lineEdit_formulaBar.setObjectName(u"lineEdit_formulaBar")
        sizePolicy1.setHeightForWidth(self.lineEdit_formulaBar.sizePolicy().hasHeightForWidth())
        self.lineEdit_formulaBar.setSizePolicy(sizePolicy1)
        self.lineEdit_formulaBar.setMinimumSize(QSize(350, 35))
        self.lineEdit_formulaBar.setFont(font1)

        self.horizontalLayout_83.addWidget(self.lineEdit_formulaBar, 0, Qt.AlignmentFlag.AlignLeft)

        self.horizontalSpacer_116 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_83.addItem(self.horizontalSpacer_116)


        self.page5Layout.addLayout(self.horizontalLayout_83)

        self.line_2 = QFrame(self.page5)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setStyleSheet(u"QFrame#line {\n"
"    background-color: grey;    /* fill */\n"
"    color: grey;               /* sometimes needed */\n"
"    border: 1px solid grey;    /* thickness + color */\n"
"}")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.page5Layout.addWidget(self.line_2)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalSpacer_46 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_46)

        self.label_16 = QLabel(self.page5)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font1)

        self.horizontalLayout_15.addWidget(self.label_16)

        self.comboBox_probeFormulaBar = QComboBox(self.page5)
        self.comboBox_probeFormulaBar.addItem("")
        self.comboBox_probeFormulaBar.addItem("")
        self.comboBox_probeFormulaBar.addItem("")
        self.comboBox_probeFormulaBar.addItem("")
        self.comboBox_probeFormulaBar.addItem("")
        self.comboBox_probeFormulaBar.addItem("")
        self.comboBox_probeFormulaBar.addItem("")
        self.comboBox_probeFormulaBar.addItem("")
        self.comboBox_probeFormulaBar.setObjectName(u"comboBox_probeFormulaBar")
        self.comboBox_probeFormulaBar.setMinimumSize(QSize(80, 35))
        self.comboBox_probeFormulaBar.setMaximumSize(QSize(90, 16777215))
        self.comboBox_probeFormulaBar.setFont(font1)

        self.horizontalLayout_15.addWidget(self.comboBox_probeFormulaBar, 0, Qt.AlignmentFlag.AlignHCenter)

        self.comboBox_dimenstionFormulaBar = QComboBox(self.page5)
        self.comboBox_dimenstionFormulaBar.addItem("")
        self.comboBox_dimenstionFormulaBar.addItem("")
        self.comboBox_dimenstionFormulaBar.addItem("")
        self.comboBox_dimenstionFormulaBar.addItem("")
        self.comboBox_dimenstionFormulaBar.addItem("")
        self.comboBox_dimenstionFormulaBar.addItem("")
        self.comboBox_dimenstionFormulaBar.addItem("")
        self.comboBox_dimenstionFormulaBar.addItem("")
        self.comboBox_dimenstionFormulaBar.setObjectName(u"comboBox_dimenstionFormulaBar")
        self.comboBox_dimenstionFormulaBar.setMinimumSize(QSize(80, 35))

        self.horizontalLayout_15.addWidget(self.comboBox_dimenstionFormulaBar)

        self.button_addFormulaBar = QPushButton(self.page5)
        self.button_addFormulaBar.setObjectName(u"button_addFormulaBar")
        sizePolicy1.setHeightForWidth(self.button_addFormulaBar.sizePolicy().hasHeightForWidth())
        self.button_addFormulaBar.setSizePolicy(sizePolicy1)
        self.button_addFormulaBar.setMinimumSize(QSize(90, 40))
        self.button_addFormulaBar.setFont(font1)

        self.horizontalLayout_15.addWidget(self.button_addFormulaBar)

        self.button_featureModeFormulaBar = QPushButton(self.page5)
        self.button_featureModeFormulaBar.setObjectName(u"button_featureModeFormulaBar")
        self.button_featureModeFormulaBar.setMinimumSize(QSize(90, 40))

        self.horizontalLayout_15.addWidget(self.button_featureModeFormulaBar)

        self.horizontalSpacer_47 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_47)


        self.page5Layout.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_7)

        self.button_plusFormulaBar = QPushButton(self.page5)
        self.button_plusFormulaBar.setObjectName(u"button_plusFormulaBar")
        sizePolicy1.setHeightForWidth(self.button_plusFormulaBar.sizePolicy().hasHeightForWidth())
        self.button_plusFormulaBar.setSizePolicy(sizePolicy1)
        self.button_plusFormulaBar.setMinimumSize(QSize(60, 50))
        self.button_plusFormulaBar.setMaximumSize(QSize(16777215, 16777215))
        self.button_plusFormulaBar.setFont(font1)

        self.horizontalLayout_14.addWidget(self.button_plusFormulaBar)

        self.button_minusFormulaBar = QPushButton(self.page5)
        self.button_minusFormulaBar.setObjectName(u"button_minusFormulaBar")
        sizePolicy1.setHeightForWidth(self.button_minusFormulaBar.sizePolicy().hasHeightForWidth())
        self.button_minusFormulaBar.setSizePolicy(sizePolicy1)
        self.button_minusFormulaBar.setMinimumSize(QSize(60, 50))
        self.button_minusFormulaBar.setMaximumSize(QSize(16777215, 16777215))
        self.button_minusFormulaBar.setFont(font1)

        self.horizontalLayout_14.addWidget(self.button_minusFormulaBar)

        self.button_multiplicationFormulaBar = QPushButton(self.page5)
        self.button_multiplicationFormulaBar.setObjectName(u"button_multiplicationFormulaBar")
        sizePolicy1.setHeightForWidth(self.button_multiplicationFormulaBar.sizePolicy().hasHeightForWidth())
        self.button_multiplicationFormulaBar.setSizePolicy(sizePolicy1)
        self.button_multiplicationFormulaBar.setMinimumSize(QSize(60, 50))
        self.button_multiplicationFormulaBar.setMaximumSize(QSize(16777215, 16777215))
        self.button_multiplicationFormulaBar.setFont(font1)

        self.horizontalLayout_14.addWidget(self.button_multiplicationFormulaBar)

        self.button_divisionFormulaBar = QPushButton(self.page5)
        self.button_divisionFormulaBar.setObjectName(u"button_divisionFormulaBar")
        sizePolicy1.setHeightForWidth(self.button_divisionFormulaBar.sizePolicy().hasHeightForWidth())
        self.button_divisionFormulaBar.setSizePolicy(sizePolicy1)
        self.button_divisionFormulaBar.setMinimumSize(QSize(60, 50))
        self.button_divisionFormulaBar.setMaximumSize(QSize(16777215, 16777215))
        self.button_divisionFormulaBar.setFont(font1)

        self.horizontalLayout_14.addWidget(self.button_divisionFormulaBar)

        self.button_modFormulaBar = QPushButton(self.page5)
        self.button_modFormulaBar.setObjectName(u"button_modFormulaBar")
        self.button_modFormulaBar.setMinimumSize(QSize(60, 50))
        self.button_modFormulaBar.setMaximumSize(QSize(16777215, 16777215))
        self.button_modFormulaBar.setFont(font1)

        self.horizontalLayout_14.addWidget(self.button_modFormulaBar)

        self.button_commaFormulaBar = QPushButton(self.page5)
        self.button_commaFormulaBar.setObjectName(u"button_commaFormulaBar")
        self.button_commaFormulaBar.setMinimumSize(QSize(60, 50))
        self.button_commaFormulaBar.setMaximumSize(QSize(16777215, 16777215))
        self.button_commaFormulaBar.setFont(font1)

        self.horizontalLayout_14.addWidget(self.button_commaFormulaBar)

        self.button_backspaceFormulaBar = QPushButton(self.page5)
        self.button_backspaceFormulaBar.setObjectName(u"button_backspaceFormulaBar")
        self.button_backspaceFormulaBar.setMinimumSize(QSize(60, 50))
        self.button_backspaceFormulaBar.setMaximumSize(QSize(16777215, 16777215))
        self.button_backspaceFormulaBar.setFont(font1)

        self.horizontalLayout_14.addWidget(self.button_backspaceFormulaBar)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_8)


        self.page5Layout.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_68 = QHBoxLayout()
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.horizontalSpacer_118 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_68.addItem(self.horizontalSpacer_118)

        self.button_1FormulaBar = QPushButton(self.page5)
        self.button_1FormulaBar.setObjectName(u"button_1FormulaBar")
        sizePolicy1.setHeightForWidth(self.button_1FormulaBar.sizePolicy().hasHeightForWidth())
        self.button_1FormulaBar.setSizePolicy(sizePolicy1)
        self.button_1FormulaBar.setMinimumSize(QSize(60, 50))
        self.button_1FormulaBar.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_68.addWidget(self.button_1FormulaBar)

        self.button_2FormulaBar = QPushButton(self.page5)
        self.button_2FormulaBar.setObjectName(u"button_2FormulaBar")
        sizePolicy1.setHeightForWidth(self.button_2FormulaBar.sizePolicy().hasHeightForWidth())
        self.button_2FormulaBar.setSizePolicy(sizePolicy1)
        self.button_2FormulaBar.setMinimumSize(QSize(60, 50))
        self.button_2FormulaBar.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_68.addWidget(self.button_2FormulaBar)

        self.button_3FormulaBar = QPushButton(self.page5)
        self.button_3FormulaBar.setObjectName(u"button_3FormulaBar")
        self.button_3FormulaBar.setMinimumSize(QSize(60, 50))
        self.button_3FormulaBar.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_68.addWidget(self.button_3FormulaBar)

        self.button_4FormulaBar = QPushButton(self.page5)
        self.button_4FormulaBar.setObjectName(u"button_4FormulaBar")
        self.button_4FormulaBar.setMinimumSize(QSize(60, 50))
        self.button_4FormulaBar.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_68.addWidget(self.button_4FormulaBar)

        self.button_5FormulaBar = QPushButton(self.page5)
        self.button_5FormulaBar.setObjectName(u"button_5FormulaBar")
        self.button_5FormulaBar.setMinimumSize(QSize(60, 50))
        self.button_5FormulaBar.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_68.addWidget(self.button_5FormulaBar)

        self.button_6FormulaBar = QPushButton(self.page5)
        self.button_6FormulaBar.setObjectName(u"button_6FormulaBar")
        self.button_6FormulaBar.setMinimumSize(QSize(60, 50))
        self.button_6FormulaBar.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_68.addWidget(self.button_6FormulaBar)

        self.button_7FormulaBar = QPushButton(self.page5)
        self.button_7FormulaBar.setObjectName(u"button_7FormulaBar")
        self.button_7FormulaBar.setMinimumSize(QSize(60, 50))
        self.button_7FormulaBar.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_68.addWidget(self.button_7FormulaBar)

        self.button_8FormulaBar = QPushButton(self.page5)
        self.button_8FormulaBar.setObjectName(u"button_8FormulaBar")
        self.button_8FormulaBar.setMinimumSize(QSize(60, 50))
        self.button_8FormulaBar.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_68.addWidget(self.button_8FormulaBar)

        self.button_9FormulaBar = QPushButton(self.page5)
        self.button_9FormulaBar.setObjectName(u"button_9FormulaBar")
        self.button_9FormulaBar.setMinimumSize(QSize(60, 50))
        self.button_9FormulaBar.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_68.addWidget(self.button_9FormulaBar)

        self.button_0FormulaBar = QPushButton(self.page5)
        self.button_0FormulaBar.setObjectName(u"button_0FormulaBar")
        self.button_0FormulaBar.setMinimumSize(QSize(60, 50))
        self.button_0FormulaBar.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_68.addWidget(self.button_0FormulaBar)

        self.horizontalSpacer_119 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_68.addItem(self.horizontalSpacer_119)


        self.page5Layout.addLayout(self.horizontalLayout_68)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalSpacer_48 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_48)

        self.button_leftBraceFormulaBar = QPushButton(self.page5)
        self.button_leftBraceFormulaBar.setObjectName(u"button_leftBraceFormulaBar")
        self.button_leftBraceFormulaBar.setMinimumSize(QSize(60, 50))
        self.button_leftBraceFormulaBar.setMaximumSize(QSize(16777215, 16777215))
        self.button_leftBraceFormulaBar.setFont(font1)

        self.horizontalLayout_16.addWidget(self.button_leftBraceFormulaBar)

        self.button_maxFormulaBar = QPushButton(self.page5)
        self.button_maxFormulaBar.setObjectName(u"button_maxFormulaBar")
        sizePolicy1.setHeightForWidth(self.button_maxFormulaBar.sizePolicy().hasHeightForWidth())
        self.button_maxFormulaBar.setSizePolicy(sizePolicy1)
        self.button_maxFormulaBar.setMinimumSize(QSize(60, 50))
        self.button_maxFormulaBar.setMaximumSize(QSize(16777215, 16777215))
        self.button_maxFormulaBar.setFont(font1)

        self.horizontalLayout_16.addWidget(self.button_maxFormulaBar)

        self.button_minFormulaBar = QPushButton(self.page5)
        self.button_minFormulaBar.setObjectName(u"button_minFormulaBar")
        self.button_minFormulaBar.setMinimumSize(QSize(60, 50))
        self.button_minFormulaBar.setMaximumSize(QSize(16777215, 16777215))
        self.button_minFormulaBar.setFont(font1)

        self.horizontalLayout_16.addWidget(self.button_minFormulaBar)

        self.button_avgFormulaBar = QPushButton(self.page5)
        self.button_avgFormulaBar.setObjectName(u"button_avgFormulaBar")
        self.button_avgFormulaBar.setMinimumSize(QSize(80, 50))
        self.button_avgFormulaBar.setMaximumSize(QSize(16777215, 16777215))
        self.button_avgFormulaBar.setFont(font1)

        self.horizontalLayout_16.addWidget(self.button_avgFormulaBar)

        self.button_absFormulaBar = QPushButton(self.page5)
        self.button_absFormulaBar.setObjectName(u"button_absFormulaBar")
        self.button_absFormulaBar.setMinimumSize(QSize(60, 50))
        self.button_absFormulaBar.setMaximumSize(QSize(16777215, 16777215))
        self.button_absFormulaBar.setFont(font1)

        self.horizontalLayout_16.addWidget(self.button_absFormulaBar)

        self.button_rightBraceFormulaBar = QPushButton(self.page5)
        self.button_rightBraceFormulaBar.setObjectName(u"button_rightBraceFormulaBar")
        self.button_rightBraceFormulaBar.setMinimumSize(QSize(60, 50))
        self.button_rightBraceFormulaBar.setMaximumSize(QSize(16777215, 16777215))
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
        self.button_sinFormulaBar.setMinimumSize(QSize(60, 50))
        self.button_sinFormulaBar.setMaximumSize(QSize(16777215, 16777215))
        self.button_sinFormulaBar.setFont(font1)

        self.horizontalLayout_17.addWidget(self.button_sinFormulaBar)

        self.button_cosFormulaBar = QPushButton(self.page5)
        self.button_cosFormulaBar.setObjectName(u"button_cosFormulaBar")
        self.button_cosFormulaBar.setMinimumSize(QSize(60, 50))
        self.button_cosFormulaBar.setMaximumSize(QSize(16777215, 16777215))
        self.button_cosFormulaBar.setFont(font1)

        self.horizontalLayout_17.addWidget(self.button_cosFormulaBar)

        self.button_tanFormulaBar = QPushButton(self.page5)
        self.button_tanFormulaBar.setObjectName(u"button_tanFormulaBar")
        self.button_tanFormulaBar.setMinimumSize(QSize(60, 50))
        self.button_tanFormulaBar.setMaximumSize(QSize(16777215, 16777215))
        self.button_tanFormulaBar.setFont(font1)

        self.horizontalLayout_17.addWidget(self.button_tanFormulaBar)

        self.button_cosecFormulaBar = QPushButton(self.page5)
        self.button_cosecFormulaBar.setObjectName(u"button_cosecFormulaBar")
        self.button_cosecFormulaBar.setMinimumSize(QSize(80, 50))
        self.button_cosecFormulaBar.setMaximumSize(QSize(16777215, 16777215))
        self.button_cosecFormulaBar.setFont(font1)

        self.horizontalLayout_17.addWidget(self.button_cosecFormulaBar)

        self.button_secFormulaBar = QPushButton(self.page5)
        self.button_secFormulaBar.setObjectName(u"button_secFormulaBar")
        self.button_secFormulaBar.setMinimumSize(QSize(60, 50))
        self.button_secFormulaBar.setMaximumSize(QSize(16777215, 16777215))
        self.button_secFormulaBar.setFont(font1)

        self.horizontalLayout_17.addWidget(self.button_secFormulaBar)

        self.button_cotFormulaBar = QPushButton(self.page5)
        self.button_cotFormulaBar.setObjectName(u"button_cotFormulaBar")
        self.button_cotFormulaBar.setMinimumSize(QSize(60, 50))
        self.button_cotFormulaBar.setMaximumSize(QSize(16777215, 16777215))
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
        sizePolicy1.setHeightForWidth(self.button_saveSettingsFormulaBar.sizePolicy().hasHeightForWidth())
        self.button_saveSettingsFormulaBar.setSizePolicy(sizePolicy1)
        self.button_saveSettingsFormulaBar.setMinimumSize(QSize(150, 40))
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
        self.label_selfIp.setFont(font1)
        self.label_selfIp.setStyleSheet(u"")

        self.horizontalLayout_18.addWidget(self.label_selfIp, 0, Qt.AlignmentFlag.AlignRight)

        self.lineEdit_selfIp = QLineEdit(self.page6)
        self.lineEdit_selfIp.setObjectName(u"lineEdit_selfIp")
        sizePolicy1.setHeightForWidth(self.lineEdit_selfIp.sizePolicy().hasHeightForWidth())
        self.lineEdit_selfIp.setSizePolicy(sizePolicy1)
        self.lineEdit_selfIp.setMinimumSize(QSize(300, 35))
        self.lineEdit_selfIp.setFont(font1)

        self.horizontalLayout_18.addWidget(self.lineEdit_selfIp, 0, Qt.AlignmentFlag.AlignLeft)


        self.page6Layout.addLayout(self.horizontalLayout_18)

        self.verticalSpacer_13 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.page6Layout.addItem(self.verticalSpacer_13)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_subnetMask = QLabel(self.page6)
        self.label_subnetMask.setObjectName(u"label_subnetMask")
        self.label_subnetMask.setFont(font1)

        self.horizontalLayout_19.addWidget(self.label_subnetMask, 0, Qt.AlignmentFlag.AlignRight)

        self.lineEdit_subnetMask = QLineEdit(self.page6)
        self.lineEdit_subnetMask.setObjectName(u"lineEdit_subnetMask")
        sizePolicy1.setHeightForWidth(self.lineEdit_subnetMask.sizePolicy().hasHeightForWidth())
        self.lineEdit_subnetMask.setSizePolicy(sizePolicy1)
        self.lineEdit_subnetMask.setMinimumSize(QSize(300, 35))
        self.lineEdit_subnetMask.setFont(font1)

        self.horizontalLayout_19.addWidget(self.lineEdit_subnetMask, 0, Qt.AlignmentFlag.AlignLeft)


        self.page6Layout.addLayout(self.horizontalLayout_19)

        self.verticalSpacer_14 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.page6Layout.addItem(self.verticalSpacer_14)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_defaultGateway = QLabel(self.page6)
        self.label_defaultGateway.setObjectName(u"label_defaultGateway")
        self.label_defaultGateway.setFont(font1)

        self.horizontalLayout_20.addWidget(self.label_defaultGateway, 0, Qt.AlignmentFlag.AlignRight)

        self.lineEdit_defaultGateway = QLineEdit(self.page6)
        self.lineEdit_defaultGateway.setObjectName(u"lineEdit_defaultGateway")
        sizePolicy1.setHeightForWidth(self.lineEdit_defaultGateway.sizePolicy().hasHeightForWidth())
        self.lineEdit_defaultGateway.setSizePolicy(sizePolicy1)
        self.lineEdit_defaultGateway.setMinimumSize(QSize(300, 35))
        self.lineEdit_defaultGateway.setFont(font1)

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
        self.label_wifiSsid.setFont(font1)

        self.horizontalLayout_21.addWidget(self.label_wifiSsid, 0, Qt.AlignmentFlag.AlignRight)

        self.lineEdit_wifiSsid = QLineEdit(self.page7)
        self.lineEdit_wifiSsid.setObjectName(u"lineEdit_wifiSsid")
        sizePolicy1.setHeightForWidth(self.lineEdit_wifiSsid.sizePolicy().hasHeightForWidth())
        self.lineEdit_wifiSsid.setSizePolicy(sizePolicy1)
        self.lineEdit_wifiSsid.setMinimumSize(QSize(200, 35))
        self.lineEdit_wifiSsid.setFont(font1)

        self.horizontalLayout_21.addWidget(self.lineEdit_wifiSsid, 0, Qt.AlignmentFlag.AlignLeft)


        self.page7Layout.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_wifiPassword = QLabel(self.page7)
        self.label_wifiPassword.setObjectName(u"label_wifiPassword")
        self.label_wifiPassword.setFont(font1)

        self.horizontalLayout_22.addWidget(self.label_wifiPassword, 0, Qt.AlignmentFlag.AlignRight)

        self.lineEdit_wifiPassword = QLineEdit(self.page7)
        self.lineEdit_wifiPassword.setObjectName(u"lineEdit_wifiPassword")
        sizePolicy1.setHeightForWidth(self.lineEdit_wifiPassword.sizePolicy().hasHeightForWidth())
        self.lineEdit_wifiPassword.setSizePolicy(sizePolicy1)
        self.lineEdit_wifiPassword.setMinimumSize(QSize(200, 35))
        self.lineEdit_wifiPassword.setFont(font1)

        self.horizontalLayout_22.addWidget(self.lineEdit_wifiPassword, 0, Qt.AlignmentFlag.AlignLeft)


        self.page7Layout.addLayout(self.horizontalLayout_22)

        self.verticalSpacer_17 = QSpacerItem(20, 70, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.page7Layout.addItem(self.verticalSpacer_17)

        self.stackedWidget_main.addWidget(self.page7)
        self.page8 = QWidget()
        self.page8.setObjectName(u"page8")
        self.page8Layout = QVBoxLayout(self.page8)
        self.page8Layout.setObjectName(u"page8Layout")
        self.verticalSpacer_19 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.page8Layout.addItem(self.verticalSpacer_19)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_buzzer = QLabel(self.page8)
        self.label_buzzer.setObjectName(u"label_buzzer")
        self.label_buzzer.setMinimumSize(QSize(0, 35))
        self.label_buzzer.setFont(font1)

        self.horizontalLayout_24.addWidget(self.label_buzzer, 0, Qt.AlignmentFlag.AlignLeft)

        self.toggleButton_buzzer = QLabel(self.page8)
        self.toggleButton_buzzer.setObjectName(u"toggleButton_buzzer")
        self.toggleButton_buzzer.setMinimumSize(QSize(60, 35))
        self.toggleButton_buzzer.setFont(font1)
        self.toggleButton_buzzer.setPixmap(QPixmap(u"/home/torizon/app/src/images/Switcher_OFF.png"))

        self.horizontalLayout_24.addWidget(self.toggleButton_buzzer, 0, Qt.AlignmentFlag.AlignRight)

        self.horizontalSpacer_171 = QSpacerItem(130, 50, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_171)

        self.horizontalSpacer_9 = QSpacerItem(0, 0, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_9)

        self.radioButton_okBuzzer = QRadioButton(self.page8)
        self.buttonGroup = QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.radioButton_okBuzzer)
        self.radioButton_okBuzzer.setObjectName(u"radioButton_okBuzzer")
        sizePolicy2.setHeightForWidth(self.radioButton_okBuzzer.sizePolicy().hasHeightForWidth())
        self.radioButton_okBuzzer.setSizePolicy(sizePolicy2)
        self.radioButton_okBuzzer.setMinimumSize(QSize(0, 50))
        self.radioButton_okBuzzer.setFont(font1)

        self.horizontalLayout_24.addWidget(self.radioButton_okBuzzer)

        self.horizontalSpacer_179 = QSpacerItem(40, 50, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_179)

        self.radioButton_reworkNotokBuzzer = QRadioButton(self.page8)
        self.buttonGroup.addButton(self.radioButton_reworkNotokBuzzer)
        self.radioButton_reworkNotokBuzzer.setObjectName(u"radioButton_reworkNotokBuzzer")
        self.radioButton_reworkNotokBuzzer.setMinimumSize(QSize(0, 50))
        self.radioButton_reworkNotokBuzzer.setFont(font1)

        self.horizontalLayout_24.addWidget(self.radioButton_reworkNotokBuzzer)

        self.horizontalSpacer_15 = QSpacerItem(60, 40, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

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
        self.label_relay.setMinimumSize(QSize(0, 35))
        self.label_relay.setFont(font1)

        self.horizontalLayout_25.addWidget(self.label_relay, 0, Qt.AlignmentFlag.AlignLeft)

        self.toggelButton_relay = QLabel(self.page8)
        self.toggelButton_relay.setObjectName(u"toggelButton_relay")
        self.toggelButton_relay.setMinimumSize(QSize(90, 35))
        self.toggelButton_relay.setFont(font1)
        self.toggelButton_relay.setPixmap(QPixmap(u"/home/torizon/app/src/images/Switcher_OFF.png"))

        self.horizontalLayout_25.addWidget(self.toggelButton_relay, 0, Qt.AlignmentFlag.AlignRight)

        self.horizontalSpacer_10 = QSpacerItem(130, 50, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_10)

        self.label_relayTime = QLabel(self.page8)
        self.label_relayTime.setObjectName(u"label_relayTime")
        self.label_relayTime.setMinimumSize(QSize(0, 35))
        self.label_relayTime.setFont(font1)

        self.horizontalLayout_25.addWidget(self.label_relayTime)

        self.lineEdit_relayTime = QLineEdit(self.page8)
        self.lineEdit_relayTime.setObjectName(u"lineEdit_relayTime")
        sizePolicy1.setHeightForWidth(self.lineEdit_relayTime.sizePolicy().hasHeightForWidth())
        self.lineEdit_relayTime.setSizePolicy(sizePolicy1)
        self.lineEdit_relayTime.setMinimumSize(QSize(0, 35))
        self.lineEdit_relayTime.setFont(font1)

        self.horizontalLayout_25.addWidget(self.lineEdit_relayTime)

        self.horizontalSpacer_16 = QSpacerItem(90, 50, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

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
        self.label_cycleStopTimer.setMinimumSize(QSize(0, 35))
        self.label_cycleStopTimer.setFont(font1)

        self.horizontalLayout_26.addWidget(self.label_cycleStopTimer, 0, Qt.AlignmentFlag.AlignLeft)

        self.toggelButton_cycleStopTimer = QLabel(self.page8)
        self.toggelButton_cycleStopTimer.setObjectName(u"toggelButton_cycleStopTimer")
        self.toggelButton_cycleStopTimer.setMinimumSize(QSize(90, 35))
        self.toggelButton_cycleStopTimer.setFont(font1)
        self.toggelButton_cycleStopTimer.setPixmap(QPixmap(u"/home/torizon/app/src/images/Switcher_OFF.png"))

        self.horizontalLayout_26.addWidget(self.toggelButton_cycleStopTimer)

        self.horizontalSpacer_11 = QSpacerItem(130, 50, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_11)

        self.label_cycleTime = QLabel(self.page8)
        self.label_cycleTime.setObjectName(u"label_cycleTime")
        self.label_cycleTime.setMinimumSize(QSize(0, 35))
        self.label_cycleTime.setFont(font1)

        self.horizontalLayout_26.addWidget(self.label_cycleTime)

        self.lineEdit_cycleTime = QLineEdit(self.page8)
        self.lineEdit_cycleTime.setObjectName(u"lineEdit_cycleTime")
        sizePolicy1.setHeightForWidth(self.lineEdit_cycleTime.sizePolicy().hasHeightForWidth())
        self.lineEdit_cycleTime.setSizePolicy(sizePolicy1)
        self.lineEdit_cycleTime.setMinimumSize(QSize(0, 35))
        self.lineEdit_cycleTime.setFont(font1)

        self.horizontalLayout_26.addWidget(self.lineEdit_cycleTime)

        self.horizontalSpacer_17 = QSpacerItem(90, 50, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

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
        self.label_autoSaveReading.setMinimumSize(QSize(0, 35))
        self.label_autoSaveReading.setFont(font1)

        self.horizontalLayout_27.addWidget(self.label_autoSaveReading, 0, Qt.AlignmentFlag.AlignLeft)

        self.toggelButton_autoSaveReading = QLabel(self.page8)
        self.toggelButton_autoSaveReading.setObjectName(u"toggelButton_autoSaveReading")
        self.toggelButton_autoSaveReading.setMinimumSize(QSize(60, 35))
        self.toggelButton_autoSaveReading.setFont(font1)
        self.toggelButton_autoSaveReading.setPixmap(QPixmap(u"/home/torizon/app/src/images/Switcher_OFF.png"))

        self.horizontalLayout_27.addWidget(self.toggelButton_autoSaveReading)

        self.horizontalSpacer_12 = QSpacerItem(430, 50, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

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
        self.label_partTraceability.setMinimumSize(QSize(0, 35))
        self.label_partTraceability.setFont(font1)

        self.horizontalLayout_28.addWidget(self.label_partTraceability, 0, Qt.AlignmentFlag.AlignLeft)

        self.toggelButton_partTraceability = QLabel(self.page8)
        self.toggelButton_partTraceability.setObjectName(u"toggelButton_partTraceability")
        self.toggelButton_partTraceability.setMinimumSize(QSize(90, 35))
        self.toggelButton_partTraceability.setFont(font1)
        self.toggelButton_partTraceability.setPixmap(QPixmap(u"/home/torizon/app/src/images/Switcher_OFF.png"))

        self.horizontalLayout_28.addWidget(self.toggelButton_partTraceability)

        self.horizontalSpacer_13 = QSpacerItem(140, 50, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_13)

        self.radioButton_manualPartTraceability = QRadioButton(self.page8)
        self.buttonGroup_2 = QButtonGroup(MainWindow)
        self.buttonGroup_2.setObjectName(u"buttonGroup_2")
        self.buttonGroup_2.addButton(self.radioButton_manualPartTraceability)
        self.radioButton_manualPartTraceability.setObjectName(u"radioButton_manualPartTraceability")
        self.radioButton_manualPartTraceability.setMinimumSize(QSize(0, 50))
        self.radioButton_manualPartTraceability.setFont(font1)

        self.horizontalLayout_28.addWidget(self.radioButton_manualPartTraceability)

        self.radioButton_autoPartTraceability = QRadioButton(self.page8)
        self.buttonGroup_2.addButton(self.radioButton_autoPartTraceability)
        self.radioButton_autoPartTraceability.setObjectName(u"radioButton_autoPartTraceability")
        self.radioButton_autoPartTraceability.setMinimumSize(QSize(0, 50))
        self.radioButton_autoPartTraceability.setFont(font1)

        self.horizontalLayout_28.addWidget(self.radioButton_autoPartTraceability)

        self.horizontalSpacer_18 = QSpacerItem(85, 50, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_18)


        self.page8Layout.addLayout(self.horizontalLayout_28)

        self.line_7 = QFrame(self.page8)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.Shape.HLine)
        self.line_7.setFrameShadow(QFrame.Shadow.Sunken)

        self.page8Layout.addWidget(self.line_7)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.page8Layout.addItem(self.verticalSpacer_12)

        self.stackedWidget_main.addWidget(self.page8)
        self.page9 = QWidget()
        self.page9.setObjectName(u"page9")
        self.page9Layout = QVBoxLayout(self.page9)
        self.page9Layout.setObjectName(u"page9Layout")
        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")

        self.verticalLayout_3.addLayout(self.horizontalLayout_32)

        self.verticalSpacer_22 = QSpacerItem(10, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer_22)

        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.label_timeToMasterSet = QLabel(self.page9)
        self.label_timeToMasterSet.setObjectName(u"label_timeToMasterSet")
        self.label_timeToMasterSet.setMinimumSize(QSize(0, 35))
        self.label_timeToMasterSet.setFont(font1)

        self.horizontalLayout_33.addWidget(self.label_timeToMasterSet)

        self.toggleButtontimeToSetMaster = QLabel(self.page9)
        self.toggleButtontimeToSetMaster.setObjectName(u"toggleButtontimeToSetMaster")
        self.toggleButtontimeToSetMaster.setMinimumSize(QSize(60, 35))
        self.toggleButtontimeToSetMaster.setPixmap(QPixmap(u"/home/torizon/app/src/images/Switcher_OFF.png"))

        self.horizontalLayout_33.addWidget(self.toggleButtontimeToSetMaster)

        self.lineEdit_timeToMasterSet = QLineEdit(self.page9)
        self.lineEdit_timeToMasterSet.setObjectName(u"lineEdit_timeToMasterSet")
        sizePolicy1.setHeightForWidth(self.lineEdit_timeToMasterSet.sizePolicy().hasHeightForWidth())
        self.lineEdit_timeToMasterSet.setSizePolicy(sizePolicy1)
        self.lineEdit_timeToMasterSet.setMinimumSize(QSize(0, 35))
        self.lineEdit_timeToMasterSet.setMaximumSize(QSize(75, 16777215))
        self.lineEdit_timeToMasterSet.setFont(font1)

        self.horizontalLayout_33.addWidget(self.lineEdit_timeToMasterSet)

        self.label_hrs = QLabel(self.page9)
        self.label_hrs.setObjectName(u"label_hrs")
        self.label_hrs.setMinimumSize(QSize(0, 35))
        self.label_hrs.setFont(font1)

        self.horizontalLayout_33.addWidget(self.label_hrs)

        self.horizontalSpacer_23 = QSpacerItem(40, 50, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_33.addItem(self.horizontalSpacer_23)


        self.verticalLayout_3.addLayout(self.horizontalLayout_33)

        self.verticalSpacer_33 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer_33)

        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.label_masterGrouping = QLabel(self.page9)
        self.label_masterGrouping.setObjectName(u"label_masterGrouping")
        self.label_masterGrouping.setMinimumSize(QSize(0, 35))
        self.label_masterGrouping.setFont(font1)

        self.horizontalLayout_34.addWidget(self.label_masterGrouping, 0, Qt.AlignmentFlag.AlignLeft)

        self.toggleButton_masterGrouping = QLabel(self.page9)
        self.toggleButton_masterGrouping.setObjectName(u"toggleButton_masterGrouping")
        self.toggleButton_masterGrouping.setMinimumSize(QSize(70, 35))
        self.toggleButton_masterGrouping.setPixmap(QPixmap(u"/home/torizon/app/src/images/Switcher_OFF.png"))
        self.toggleButton_masterGrouping.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_34.addWidget(self.toggleButton_masterGrouping, 0, Qt.AlignmentFlag.AlignLeft)

        self.horizontalSpacer_120 = QSpacerItem(40, 50, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_34.addItem(self.horizontalSpacer_120)


        self.verticalLayout_3.addLayout(self.horizontalLayout_34)

        self.verticalSpacer_21 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_21)

        self.verticalSpacer_70 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer_70)

        self.horizontalLayout_35 = QHBoxLayout()
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.label_SaveMasterCalibration = QLabel(self.page9)
        self.label_SaveMasterCalibration.setObjectName(u"label_SaveMasterCalibration")

        self.horizontalLayout_35.addWidget(self.label_SaveMasterCalibration)

        self.horizontalSpacer_84 = QSpacerItem(7, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_35.addItem(self.horizontalSpacer_84)

        self.toggleButtonSaveMasterCalibration = QLabel(self.page9)
        self.toggleButtonSaveMasterCalibration.setObjectName(u"toggleButtonSaveMasterCalibration")
        self.toggleButtonSaveMasterCalibration.setMinimumSize(QSize(70, 35))
        self.toggleButtonSaveMasterCalibration.setPixmap(QPixmap(u"/home/torizon/app/src/images/Switcher_OFF.png"))

        self.horizontalLayout_35.addWidget(self.toggleButtonSaveMasterCalibration, 0, Qt.AlignmentFlag.AlignLeft)

        self.horizontalSpacer_85 = QSpacerItem(60, 50, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_35.addItem(self.horizontalSpacer_85)


        self.verticalLayout_3.addLayout(self.horizontalLayout_35)

        self.verticalSpacer_20 = QSpacerItem(20, 220, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer_20)


        self.horizontalLayout_23.addLayout(self.verticalLayout_3)

        self.line_14 = QFrame(self.page9)
        self.line_14.setObjectName(u"line_14")
        self.line_14.setFrameShape(QFrame.Shape.VLine)
        self.line_14.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_23.addWidget(self.line_14)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.button_factoryCalibration = QPushButton(self.page9)
        self.button_factoryCalibration.setObjectName(u"button_factoryCalibration")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.button_factoryCalibration.sizePolicy().hasHeightForWidth())
        self.button_factoryCalibration.setSizePolicy(sizePolicy3)
        self.button_factoryCalibration.setMinimumSize(QSize(200, 30))
        self.button_factoryCalibration.setMaximumSize(QSize(16777215, 40))
        self.button_factoryCalibration.setFont(font1)

        self.verticalLayout_2.addWidget(self.button_factoryCalibration, 0, Qt.AlignmentFlag.AlignHCenter)

        self.button_touchCalibration = QPushButton(self.page9)
        self.button_touchCalibration.setObjectName(u"button_touchCalibration")
        sizePolicy3.setHeightForWidth(self.button_touchCalibration.sizePolicy().hasHeightForWidth())
        self.button_touchCalibration.setSizePolicy(sizePolicy3)
        self.button_touchCalibration.setMinimumSize(QSize(200, 30))
        self.button_touchCalibration.setMaximumSize(QSize(16777215, 40))
        self.button_touchCalibration.setFont(font1)

        self.verticalLayout_2.addWidget(self.button_touchCalibration, 0, Qt.AlignmentFlag.AlignHCenter)

        self.button_databaseSettings = QPushButton(self.page9)
        self.button_databaseSettings.setObjectName(u"button_databaseSettings")
        sizePolicy3.setHeightForWidth(self.button_databaseSettings.sizePolicy().hasHeightForWidth())
        self.button_databaseSettings.setSizePolicy(sizePolicy3)
        self.button_databaseSettings.setMinimumSize(QSize(200, 30))
        self.button_databaseSettings.setMaximumSize(QSize(16777215, 40))
        self.button_databaseSettings.setFont(font1)

        self.verticalLayout_2.addWidget(self.button_databaseSettings, 0, Qt.AlignmentFlag.AlignHCenter)

        self.button_rs232Settings = QPushButton(self.page9)
        self.button_rs232Settings.setObjectName(u"button_rs232Settings")
        sizePolicy3.setHeightForWidth(self.button_rs232Settings.sizePolicy().hasHeightForWidth())
        self.button_rs232Settings.setSizePolicy(sizePolicy3)
        self.button_rs232Settings.setMinimumSize(QSize(200, 30))
        self.button_rs232Settings.setMaximumSize(QSize(16777215, 40))
        self.button_rs232Settings.setFont(font1)

        self.verticalLayout_2.addWidget(self.button_rs232Settings, 0, Qt.AlignmentFlag.AlignHCenter)

        self.button_factoryConfig = QPushButton(self.page9)
        self.button_factoryConfig.setObjectName(u"button_factoryConfig")
        sizePolicy3.setHeightForWidth(self.button_factoryConfig.sizePolicy().hasHeightForWidth())
        self.button_factoryConfig.setSizePolicy(sizePolicy3)
        self.button_factoryConfig.setMinimumSize(QSize(200, 30))
        self.button_factoryConfig.setMaximumSize(QSize(16777215, 40))
        self.button_factoryConfig.setFont(font1)

        self.verticalLayout_2.addWidget(self.button_factoryConfig, 0, Qt.AlignmentFlag.AlignHCenter)

        self.button_ipSettings = QPushButton(self.page9)
        self.button_ipSettings.setObjectName(u"button_ipSettings")
        sizePolicy3.setHeightForWidth(self.button_ipSettings.sizePolicy().hasHeightForWidth())
        self.button_ipSettings.setSizePolicy(sizePolicy3)
        self.button_ipSettings.setMinimumSize(QSize(200, 30))
        self.button_ipSettings.setMaximumSize(QSize(16777215, 40))
        self.button_ipSettings.setFont(font1)

        self.verticalLayout_2.addWidget(self.button_ipSettings, 0, Qt.AlignmentFlag.AlignHCenter)

        self.button_wifiSettings = QPushButton(self.page9)
        self.button_wifiSettings.setObjectName(u"button_wifiSettings")
        sizePolicy3.setHeightForWidth(self.button_wifiSettings.sizePolicy().hasHeightForWidth())
        self.button_wifiSettings.setSizePolicy(sizePolicy3)
        self.button_wifiSettings.setMinimumSize(QSize(200, 30))
        self.button_wifiSettings.setMaximumSize(QSize(16777215, 40))
        self.button_wifiSettings.setFont(font1)

        self.verticalLayout_2.addWidget(self.button_wifiSettings, 0, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout_23.addLayout(self.verticalLayout_2)


        self.page9Layout.addLayout(self.horizontalLayout_23)

        self.stackedWidget_main.addWidget(self.page9)
        self.page10 = QWidget()
        self.page10.setObjectName(u"page10")
        self.label_productHelp = QLabel(self.page10)
        self.label_productHelp.setObjectName(u"label_productHelp")
        self.label_productHelp.setGeometry(QRect(29, 0, 721, 35))
        self.label_productHelp.setFont(font4)
        self.label_productHelp.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_intersenseNameHelp = QLabel(self.page10)
        self.label_intersenseNameHelp.setObjectName(u"label_intersenseNameHelp")
        self.label_intersenseNameHelp.setGeometry(QRect(29, 40, 721, 35))
        self.label_intersenseNameHelp.setFont(font4)
        self.label_intersenseNameHelp.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_adressHelp = QLabel(self.page10)
        self.label_adressHelp.setObjectName(u"label_adressHelp")
        self.label_adressHelp.setGeometry(QRect(29, 75, 721, 35))
        self.label_adressHelp.setFont(font4)
        self.label_adressHelp.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_adressHelp_2 = QLabel(self.page10)
        self.label_adressHelp_2.setObjectName(u"label_adressHelp_2")
        self.label_adressHelp_2.setGeometry(QRect(29, 110, 741, 35))
        self.label_adressHelp_2.setFont(font4)
        self.label_adressHelp_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_emailHelp = QLabel(self.page10)
        self.label_emailHelp.setObjectName(u"label_emailHelp")
        self.label_emailHelp.setGeometry(QRect(29, 145, 725, 35))
        self.label_emailHelp.setFont(font4)
        self.label_emailHelp.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_supportHelp = QLabel(self.page10)
        self.label_supportHelp.setObjectName(u"label_supportHelp")
        self.label_supportHelp.setGeometry(QRect(29, 180, 725, 35))
        self.label_supportHelp.setFont(font4)
        self.label_supportHelp.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label = QLabel(self.page10)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 220, 381, 35))
        self.label.setFont(font4)
        self.label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.label_ModelNumber = QLabel(self.page10)
        self.label_ModelNumber.setObjectName(u"label_ModelNumber")
        self.label_ModelNumber.setGeometry(QRect(420, 220, 90, 35))
        self.label_ModelNumber.setMinimumSize(QSize(0, 35))
        self.label_ModelNumber.setMaximumSize(QSize(16777215, 16777215))
        self.label_ModelNumber.setFont(font4)
        self.label_ModelNumber.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_6 = QLabel(self.page10)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(50, 260, 371, 35))
        self.label_6.setFont(font4)
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.label_SerialNumber = QLabel(self.page10)
        self.label_SerialNumber.setObjectName(u"label_SerialNumber")
        self.label_SerialNumber.setGeometry(QRect(430, 260, 50, 35))
        self.label_SerialNumber.setMinimumSize(QSize(50, 35))
        self.label_SerialNumber.setFont(font4)
        self.label_SerialNumber.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_12 = QLabel(self.page10)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(50, 300, 391, 35))
        self.label_12.setFont(font4)
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.label_VersionNumber = QLabel(self.page10)
        self.label_VersionNumber.setObjectName(u"label_VersionNumber")
        self.label_VersionNumber.setGeometry(QRect(440, 300, 50, 35))
        self.label_VersionNumber.setFont(font4)
        self.label_VersionNumber.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.button_update = QPushButton(self.page10)
        self.button_update.setObjectName(u"button_update")
        self.button_update.setGeometry(QRect(610, 300, 160, 36))
        self.stackedWidget_main.addWidget(self.page10)
        self.page11 = QWidget()
        self.page11.setObjectName(u"page11")
        self.page11Layout = QVBoxLayout(self.page11)
        self.page11Layout.setObjectName(u"page11Layout")
        self.horizontalLayout_45 = QHBoxLayout()
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.horizontalSpacer_152 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_45.addItem(self.horizontalSpacer_152)

        self.label_setDate = QLabel(self.page11)
        self.label_setDate.setObjectName(u"label_setDate")
        self.label_setDate.setFont(font1)

        self.horizontalLayout_45.addWidget(self.label_setDate, 0, Qt.AlignmentFlag.AlignRight)

        self.lineEdit_day = QLineEdit(self.page11)
        self.lineEdit_day.setObjectName(u"lineEdit_day")
        sizePolicy1.setHeightForWidth(self.lineEdit_day.sizePolicy().hasHeightForWidth())
        self.lineEdit_day.setSizePolicy(sizePolicy1)
        self.lineEdit_day.setMinimumSize(QSize(0, 35))
        self.lineEdit_day.setMaximumSize(QSize(70, 16777215))
        self.lineEdit_day.setFont(font1)
        self.lineEdit_day.setStyleSheet(u"")

        self.horizontalLayout_45.addWidget(self.lineEdit_day, 0, Qt.AlignmentFlag.AlignLeft)

        self.label_day = QLabel(self.page11)
        self.label_day.setObjectName(u"label_day")
        self.label_day.setFont(font1)

        self.horizontalLayout_45.addWidget(self.label_day, 0, Qt.AlignmentFlag.AlignLeft)

        self.horizontalSpacer_160 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_45.addItem(self.horizontalSpacer_160)

        self.lineEdit_month = QLineEdit(self.page11)
        self.lineEdit_month.setObjectName(u"lineEdit_month")
        sizePolicy1.setHeightForWidth(self.lineEdit_month.sizePolicy().hasHeightForWidth())
        self.lineEdit_month.setSizePolicy(sizePolicy1)
        self.lineEdit_month.setMinimumSize(QSize(70, 35))
        self.lineEdit_month.setMaximumSize(QSize(70, 16777215))
        self.lineEdit_month.setFont(font1)
        self.lineEdit_month.setStyleSheet(u"")

        self.horizontalLayout_45.addWidget(self.lineEdit_month, 0, Qt.AlignmentFlag.AlignLeft)

        self.label_month = QLabel(self.page11)
        self.label_month.setObjectName(u"label_month")
        self.label_month.setFont(font1)

        self.horizontalLayout_45.addWidget(self.label_month, 0, Qt.AlignmentFlag.AlignLeft)

        self.horizontalSpacer_161 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_45.addItem(self.horizontalSpacer_161)

        self.lineEdit_year = QLineEdit(self.page11)
        self.lineEdit_year.setObjectName(u"lineEdit_year")
        sizePolicy1.setHeightForWidth(self.lineEdit_year.sizePolicy().hasHeightForWidth())
        self.lineEdit_year.setSizePolicy(sizePolicy1)
        self.lineEdit_year.setMinimumSize(QSize(0, 35))
        self.lineEdit_year.setMaximumSize(QSize(70, 16777215))
        self.lineEdit_year.setFont(font1)
        self.lineEdit_year.setStyleSheet(u"")

        self.horizontalLayout_45.addWidget(self.lineEdit_year, 0, Qt.AlignmentFlag.AlignLeft)

        self.label_year = QLabel(self.page11)
        self.label_year.setObjectName(u"label_year")
        self.label_year.setFont(font1)

        self.horizontalLayout_45.addWidget(self.label_year, 0, Qt.AlignmentFlag.AlignLeft)

        self.horizontalSpacer_159 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_45.addItem(self.horizontalSpacer_159)


        self.page11Layout.addLayout(self.horizontalLayout_45)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.page11Layout.addItem(self.verticalSpacer_9)

        self.horizontalLayout_46 = QHBoxLayout()
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.horizontalSpacer_149 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_46.addItem(self.horizontalSpacer_149)

        self.label_setTime = QLabel(self.page11)
        self.label_setTime.setObjectName(u"label_setTime")
        self.label_setTime.setFont(font1)

        self.horizontalLayout_46.addWidget(self.label_setTime, 0, Qt.AlignmentFlag.AlignRight)

        self.lineEdit_hours = QLineEdit(self.page11)
        self.lineEdit_hours.setObjectName(u"lineEdit_hours")
        sizePolicy1.setHeightForWidth(self.lineEdit_hours.sizePolicy().hasHeightForWidth())
        self.lineEdit_hours.setSizePolicy(sizePolicy1)
        self.lineEdit_hours.setMinimumSize(QSize(0, 35))
        self.lineEdit_hours.setMaximumSize(QSize(70, 16777215))
        self.lineEdit_hours.setFont(font1)
        self.lineEdit_hours.setStyleSheet(u"")

        self.horizontalLayout_46.addWidget(self.lineEdit_hours, 0, Qt.AlignmentFlag.AlignLeft)

        self.label_hours = QLabel(self.page11)
        self.label_hours.setObjectName(u"label_hours")
        self.label_hours.setFont(font1)

        self.horizontalLayout_46.addWidget(self.label_hours, 0, Qt.AlignmentFlag.AlignLeft)

        self.horizontalSpacer_167 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_46.addItem(self.horizontalSpacer_167)

        self.lineEdit_minutes = QLineEdit(self.page11)
        self.lineEdit_minutes.setObjectName(u"lineEdit_minutes")
        sizePolicy1.setHeightForWidth(self.lineEdit_minutes.sizePolicy().hasHeightForWidth())
        self.lineEdit_minutes.setSizePolicy(sizePolicy1)
        self.lineEdit_minutes.setMinimumSize(QSize(0, 35))
        self.lineEdit_minutes.setMaximumSize(QSize(70, 16777215))
        self.lineEdit_minutes.setFont(font1)
        self.lineEdit_minutes.setStyleSheet(u"")

        self.horizontalLayout_46.addWidget(self.lineEdit_minutes, 0, Qt.AlignmentFlag.AlignLeft)

        self.label_minutes = QLabel(self.page11)
        self.label_minutes.setObjectName(u"label_minutes")
        self.label_minutes.setFont(font1)

        self.horizontalLayout_46.addWidget(self.label_minutes, 0, Qt.AlignmentFlag.AlignLeft)

        self.horizontalSpacer_162 = QSpacerItem(40, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_46.addItem(self.horizontalSpacer_162)


        self.page11Layout.addLayout(self.horizontalLayout_46)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.page11Layout.addItem(self.verticalSpacer_10)

        self.horizontalLayout_96 = QHBoxLayout()
        self.horizontalLayout_96.setObjectName(u"horizontalLayout_96")
        self.button_setDateTime = QPushButton(self.page11)
        self.button_setDateTime.setObjectName(u"button_setDateTime")
        sizePolicy1.setHeightForWidth(self.button_setDateTime.sizePolicy().hasHeightForWidth())
        self.button_setDateTime.setSizePolicy(sizePolicy1)
        self.button_setDateTime.setMinimumSize(QSize(150, 35))
        self.button_setDateTime.setMaximumSize(QSize(16777215, 40))
        self.button_setDateTime.setFont(font1)

        self.horizontalLayout_96.addWidget(self.button_setDateTime, 0, Qt.AlignmentFlag.AlignHCenter)


        self.page11Layout.addLayout(self.horizontalLayout_96)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.page11Layout.addItem(self.verticalSpacer_7)

        self.line_8 = QFrame(self.page11)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.Shape.HLine)
        self.line_8.setFrameShadow(QFrame.Shadow.Sunken)

        self.page11Layout.addWidget(self.line_8)

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
        self.horizontalSpacer_65 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_103.addItem(self.horizontalSpacer_65)

        self.lineEdit_shift3FromTime = QLineEdit(self.page11)
        self.lineEdit_shift3FromTime.setObjectName(u"lineEdit_shift3FromTime")
        sizePolicy1.setHeightForWidth(self.lineEdit_shift3FromTime.sizePolicy().hasHeightForWidth())
        self.lineEdit_shift3FromTime.setSizePolicy(sizePolicy1)
        self.lineEdit_shift3FromTime.setMinimumSize(QSize(0, 35))
        self.lineEdit_shift3FromTime.setMaximumSize(QSize(90, 16777215))
        self.lineEdit_shift3FromTime.setFont(font1)
        self.lineEdit_shift3FromTime.setStyleSheet(u"")

        self.horizontalLayout_103.addWidget(self.lineEdit_shift3FromTime)

        self.comboBox_shift3FromTimeAmPm = QComboBox(self.page11)
        self.comboBox_shift3FromTimeAmPm.addItem("")
        self.comboBox_shift3FromTimeAmPm.addItem("")
        self.comboBox_shift3FromTimeAmPm.setObjectName(u"comboBox_shift3FromTimeAmPm")
        self.comboBox_shift3FromTimeAmPm.setMinimumSize(QSize(65, 35))
        self.comboBox_shift3FromTimeAmPm.setMaximumSize(QSize(16777215, 16777215))
        self.comboBox_shift3FromTimeAmPm.setFont(font1)

        self.horizontalLayout_103.addWidget(self.comboBox_shift3FromTimeAmPm)

        self.horizontalSpacer_69 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_103.addItem(self.horizontalSpacer_69)


        self.gridLayout.addLayout(self.horizontalLayout_103, 5, 5, 1, 1)

        self.line_28 = QFrame(self.page11)
        self.line_28.setObjectName(u"line_28")
        self.line_28.setFrameShape(QFrame.Shape.HLine)
        self.line_28.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_28, 1, 1, 1, 1)

        self.horizontalLayout_102 = QHBoxLayout()
        self.horizontalLayout_102.setObjectName(u"horizontalLayout_102")
        self.horizontalSpacer_64 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_102.addItem(self.horizontalSpacer_64)

        self.lineEdit_shift2FromTime = QLineEdit(self.page11)
        self.lineEdit_shift2FromTime.setObjectName(u"lineEdit_shift2FromTime")
        sizePolicy1.setHeightForWidth(self.lineEdit_shift2FromTime.sizePolicy().hasHeightForWidth())
        self.lineEdit_shift2FromTime.setSizePolicy(sizePolicy1)
        self.lineEdit_shift2FromTime.setMinimumSize(QSize(0, 35))
        self.lineEdit_shift2FromTime.setMaximumSize(QSize(90, 16777215))
        self.lineEdit_shift2FromTime.setFont(font1)
        self.lineEdit_shift2FromTime.setStyleSheet(u"")

        self.horizontalLayout_102.addWidget(self.lineEdit_shift2FromTime)

        self.comboBox_shift2FromTimeAmPm = QComboBox(self.page11)
        self.comboBox_shift2FromTimeAmPm.addItem("")
        self.comboBox_shift2FromTimeAmPm.addItem("")
        self.comboBox_shift2FromTimeAmPm.setObjectName(u"comboBox_shift2FromTimeAmPm")
        self.comboBox_shift2FromTimeAmPm.setMinimumSize(QSize(65, 35))
        self.comboBox_shift2FromTimeAmPm.setMaximumSize(QSize(16777215, 16777215))
        self.comboBox_shift2FromTimeAmPm.setFont(font1)

        self.horizontalLayout_102.addWidget(self.comboBox_shift2FromTimeAmPm)

        self.horizontalSpacer_68 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

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
        self.horizontalSpacer_54 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_99.addItem(self.horizontalSpacer_54)

        self.label_shift2 = QLabel(self.page11)
        self.label_shift2.setObjectName(u"label_shift2")
        self.label_shift2.setFont(font1)

        self.horizontalLayout_99.addWidget(self.label_shift2)

        self.checkBox_shift2 = QCheckBox(self.page11)
        self.checkBox_shift2.setObjectName(u"checkBox_shift2")
        self.checkBox_shift2.setMaximumSize(QSize(16777215, 16777215))
        font5 = QFont()
        font5.setFamilies([u"MS Shell Dlg 2"])
        font5.setPointSize(12)
        font5.setBold(True)
        self.checkBox_shift2.setFont(font5)

        self.horizontalLayout_99.addWidget(self.checkBox_shift2)

        self.horizontalSpacer_55 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_99.addItem(self.horizontalSpacer_55)


        self.gridLayout.addLayout(self.horizontalLayout_99, 4, 2, 1, 1)

        self.horizontalLayout_100 = QHBoxLayout()
        self.horizontalLayout_100.setObjectName(u"horizontalLayout_100")
        self.horizontalSpacer_56 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_100.addItem(self.horizontalSpacer_56)

        self.label_shift3 = QLabel(self.page11)
        self.label_shift3.setObjectName(u"label_shift3")
        self.label_shift3.setFont(font1)

        self.horizontalLayout_100.addWidget(self.label_shift3)

        self.checkBox_shift3 = QCheckBox(self.page11)
        self.checkBox_shift3.setObjectName(u"checkBox_shift3")
        self.checkBox_shift3.setMaximumSize(QSize(16777215, 16777215))
        self.checkBox_shift3.setFont(font5)

        self.horizontalLayout_100.addWidget(self.checkBox_shift3)

        self.line_27 = QFrame(self.page11)
        self.line_27.setObjectName(u"line_27")
        self.line_27.setFrameShape(QFrame.Shape.HLine)
        self.line_27.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_100.addWidget(self.line_27)

        self.horizontalSpacer_57 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_100.addItem(self.horizontalSpacer_57)


        self.gridLayout.addLayout(self.horizontalLayout_100, 5, 2, 1, 1)

        self.horizontalLayout_107 = QHBoxLayout()
        self.horizontalLayout_107.setObjectName(u"horizontalLayout_107")
        self.horizontalSpacer_67 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_107.addItem(self.horizontalSpacer_67)

        self.lineEdit_shift3ToTime = QLineEdit(self.page11)
        self.lineEdit_shift3ToTime.setObjectName(u"lineEdit_shift3ToTime")
        sizePolicy1.setHeightForWidth(self.lineEdit_shift3ToTime.sizePolicy().hasHeightForWidth())
        self.lineEdit_shift3ToTime.setSizePolicy(sizePolicy1)
        self.lineEdit_shift3ToTime.setMinimumSize(QSize(0, 35))
        self.lineEdit_shift3ToTime.setMaximumSize(QSize(90, 16777215))
        self.lineEdit_shift3ToTime.setFont(font1)
        self.lineEdit_shift3ToTime.setStyleSheet(u"")

        self.horizontalLayout_107.addWidget(self.lineEdit_shift3ToTime)

        self.comboBox_shift3ToTimeAmPm = QComboBox(self.page11)
        self.comboBox_shift3ToTimeAmPm.addItem("")
        self.comboBox_shift3ToTimeAmPm.addItem("")
        self.comboBox_shift3ToTimeAmPm.setObjectName(u"comboBox_shift3ToTimeAmPm")
        self.comboBox_shift3ToTimeAmPm.setMinimumSize(QSize(65, 35))
        self.comboBox_shift3ToTimeAmPm.setMaximumSize(QSize(16777215, 16777215))
        self.comboBox_shift3ToTimeAmPm.setFont(font1)

        self.horizontalLayout_107.addWidget(self.comboBox_shift3ToTimeAmPm)

        self.horizontalSpacer_71 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_107.addItem(self.horizontalSpacer_71)


        self.gridLayout.addLayout(self.horizontalLayout_107, 5, 8, 1, 1)

        self.horizontalLayout_97 = QHBoxLayout()
        self.horizontalLayout_97.setObjectName(u"horizontalLayout_97")
        self.horizontalSpacer_62 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_97.addItem(self.horizontalSpacer_62)

        self.lineEdit_shift1FromTime = QLineEdit(self.page11)
        self.lineEdit_shift1FromTime.setObjectName(u"lineEdit_shift1FromTime")
        sizePolicy1.setHeightForWidth(self.lineEdit_shift1FromTime.sizePolicy().hasHeightForWidth())
        self.lineEdit_shift1FromTime.setSizePolicy(sizePolicy1)
        self.lineEdit_shift1FromTime.setMinimumSize(QSize(0, 35))
        self.lineEdit_shift1FromTime.setMaximumSize(QSize(90, 16777215))
        self.lineEdit_shift1FromTime.setFont(font1)
        self.lineEdit_shift1FromTime.setStyleSheet(u"")

        self.horizontalLayout_97.addWidget(self.lineEdit_shift1FromTime)

        self.comboBox_shift1FromTimeAmPm = QComboBox(self.page11)
        self.comboBox_shift1FromTimeAmPm.addItem("")
        self.comboBox_shift1FromTimeAmPm.addItem("")
        self.comboBox_shift1FromTimeAmPm.setObjectName(u"comboBox_shift1FromTimeAmPm")
        self.comboBox_shift1FromTimeAmPm.setMinimumSize(QSize(65, 35))
        self.comboBox_shift1FromTimeAmPm.setMaximumSize(QSize(16777215, 16777215))
        self.comboBox_shift1FromTimeAmPm.setFont(font1)

        self.horizontalLayout_97.addWidget(self.comboBox_shift1FromTimeAmPm)

        self.horizontalSpacer_59 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

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
        self.horizontalSpacer_66 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_106.addItem(self.horizontalSpacer_66)

        self.lineEdit_shift2ToTime = QLineEdit(self.page11)
        self.lineEdit_shift2ToTime.setObjectName(u"lineEdit_shift2ToTime")
        sizePolicy1.setHeightForWidth(self.lineEdit_shift2ToTime.sizePolicy().hasHeightForWidth())
        self.lineEdit_shift2ToTime.setSizePolicy(sizePolicy1)
        self.lineEdit_shift2ToTime.setMinimumSize(QSize(0, 35))
        self.lineEdit_shift2ToTime.setMaximumSize(QSize(90, 16777215))
        self.lineEdit_shift2ToTime.setFont(font1)
        self.lineEdit_shift2ToTime.setStyleSheet(u"")

        self.horizontalLayout_106.addWidget(self.lineEdit_shift2ToTime)

        self.comboBox_shift2ToTimeAmPm = QComboBox(self.page11)
        self.comboBox_shift2ToTimeAmPm.addItem("")
        self.comboBox_shift2ToTimeAmPm.addItem("")
        self.comboBox_shift2ToTimeAmPm.setObjectName(u"comboBox_shift2ToTimeAmPm")
        self.comboBox_shift2ToTimeAmPm.setMinimumSize(QSize(65, 35))
        self.comboBox_shift2ToTimeAmPm.setMaximumSize(QSize(16777215, 16777215))
        self.comboBox_shift2ToTimeAmPm.setFont(font1)

        self.horizontalLayout_106.addWidget(self.comboBox_shift2ToTimeAmPm)

        self.horizontalSpacer_70 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

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
        self.label_shiftTo.setFont(font1)

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
        self.horizontalSpacer_63 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_105.addItem(self.horizontalSpacer_63)

        self.lineEdit_shift1ToTime = QLineEdit(self.page11)
        self.lineEdit_shift1ToTime.setObjectName(u"lineEdit_shift1ToTime")
        sizePolicy1.setHeightForWidth(self.lineEdit_shift1ToTime.sizePolicy().hasHeightForWidth())
        self.lineEdit_shift1ToTime.setSizePolicy(sizePolicy1)
        self.lineEdit_shift1ToTime.setMinimumSize(QSize(0, 35))
        self.lineEdit_shift1ToTime.setMaximumSize(QSize(90, 16777215))
        self.lineEdit_shift1ToTime.setFont(font1)
        self.lineEdit_shift1ToTime.setStyleSheet(u"")

        self.horizontalLayout_105.addWidget(self.lineEdit_shift1ToTime)

        self.comboBox_shift1ToTimeAmPm = QComboBox(self.page11)
        self.comboBox_shift1ToTimeAmPm.addItem("")
        self.comboBox_shift1ToTimeAmPm.addItem("")
        self.comboBox_shift1ToTimeAmPm.setObjectName(u"comboBox_shift1ToTimeAmPm")
        self.comboBox_shift1ToTimeAmPm.setMinimumSize(QSize(65, 35))
        self.comboBox_shift1ToTimeAmPm.setMaximumSize(QSize(16777215, 16777215))
        self.comboBox_shift1ToTimeAmPm.setFont(font1)

        self.horizontalLayout_105.addWidget(self.comboBox_shift1ToTimeAmPm)

        self.horizontalSpacer_58 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_105.addItem(self.horizontalSpacer_58)


        self.gridLayout.addLayout(self.horizontalLayout_105, 3, 8, 1, 1)

        self.line_49 = QFrame(self.page11)
        self.line_49.setObjectName(u"line_49")
        self.line_49.setFrameShape(QFrame.Shape.VLine)
        self.line_49.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_49, 5, 7, 1, 1)

        self.horizontalLayout_98 = QHBoxLayout()
        self.horizontalLayout_98.setObjectName(u"horizontalLayout_98")
        self.horizontalSpacer_52 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_98.addItem(self.horizontalSpacer_52)

        self.label_shift1 = QLabel(self.page11)
        self.label_shift1.setObjectName(u"label_shift1")
        self.label_shift1.setFont(font1)

        self.horizontalLayout_98.addWidget(self.label_shift1)

        self.checkBox_shift1 = QCheckBox(self.page11)
        self.checkBox_shift1.setObjectName(u"checkBox_shift1")
        sizePolicy1.setHeightForWidth(self.checkBox_shift1.sizePolicy().hasHeightForWidth())
        self.checkBox_shift1.setSizePolicy(sizePolicy1)
        self.checkBox_shift1.setMinimumSize(QSize(0, 0))
        self.checkBox_shift1.setMaximumSize(QSize(16777215, 16777215))
        self.checkBox_shift1.setFont(font5)

        self.horizontalLayout_98.addWidget(self.checkBox_shift1)

        self.horizontalSpacer_53 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

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
        self.label_shiftFrom.setFont(font1)

        self.gridLayout.addWidget(self.label_shiftFrom, 0, 5, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.label_shiftSettings = QLabel(self.page11)
        self.label_shiftSettings.setObjectName(u"label_shiftSettings")
        self.label_shiftSettings.setFont(font1)

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

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.page11Layout.addItem(self.verticalSpacer_8)

        self.horizontalLayout_110 = QHBoxLayout()
        self.horizontalLayout_110.setSpacing(0)
        self.horizontalLayout_110.setObjectName(u"horizontalLayout_110")
        self.button_setShiftTimings = QPushButton(self.page11)
        self.button_setShiftTimings.setObjectName(u"button_setShiftTimings")
        self.button_setShiftTimings.setMinimumSize(QSize(150, 35))
        self.button_setShiftTimings.setMaximumSize(QSize(16777215, 40))
        self.button_setShiftTimings.setFont(font1)

        self.horizontalLayout_110.addWidget(self.button_setShiftTimings, 0, Qt.AlignmentFlag.AlignHCenter)


        self.page11Layout.addLayout(self.horizontalLayout_110)

        self.stackedWidget_main.addWidget(self.page11)
        self.page12 = QWidget()
        self.page12.setObjectName(u"page12")
        self.page12Layout = QVBoxLayout(self.page12)
        self.page12Layout.setObjectName(u"page12Layout")
        self.horizontalLayout_47 = QHBoxLayout()
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.label_digitVal1 = QLabel(self.page12)
        self.label_digitVal1.setObjectName(u"label_digitVal1")
        self.label_digitVal1.setMinimumSize(QSize(150, 49))
        self.label_digitVal1.setMaximumSize(QSize(150, 80))
        self.label_digitVal1.setStyleSheet(u"border: 2px solid #ffffff;\n"
"border-radius: 10px;\n"
"padding: 5px;")

        self.horizontalLayout_47.addWidget(self.label_digitVal1, 0, Qt.AlignmentFlag.AlignRight)

        self.label_digitStatus1 = QLabel(self.page12)
        self.label_digitStatus1.setObjectName(u"label_digitStatus1")
        self.label_digitStatus1.setMinimumSize(QSize(150, 49))
        self.label_digitStatus1.setMaximumSize(QSize(800, 80))
        self.label_digitStatus1.setStyleSheet(u"border: 2px solid #ffffff;\n"
"border-radius: 10px;\n"
"padding: 5px;")

        self.horizontalLayout_47.addWidget(self.label_digitStatus1, 0, Qt.AlignmentFlag.AlignLeft)

        self.label_digitVal2 = QLabel(self.page12)
        self.label_digitVal2.setObjectName(u"label_digitVal2")
        self.label_digitVal2.setMinimumSize(QSize(150, 49))
        self.label_digitVal2.setMaximumSize(QSize(800, 80))
        self.label_digitVal2.setStyleSheet(u"border: 2px solid #ffffff;\n"
"border-radius: 10px;\n"
"padding: 5px;")

        self.horizontalLayout_47.addWidget(self.label_digitVal2, 0, Qt.AlignmentFlag.AlignRight)

        self.label_digitStatus2 = QLabel(self.page12)
        self.label_digitStatus2.setObjectName(u"label_digitStatus2")
        self.label_digitStatus2.setMinimumSize(QSize(150, 49))
        self.label_digitStatus2.setMaximumSize(QSize(800, 80))
        self.label_digitStatus2.setStyleSheet(u"border: 2px solid #ffffff;\n"
"border-radius: 10px;\n"
"padding: 5px;")

        self.horizontalLayout_47.addWidget(self.label_digitStatus2, 0, Qt.AlignmentFlag.AlignLeft)


        self.page12Layout.addLayout(self.horizontalLayout_47)

        self.horizontalLayout_48 = QHBoxLayout()
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.label_digitVal3 = QLabel(self.page12)
        self.label_digitVal3.setObjectName(u"label_digitVal3")
        self.label_digitVal3.setMinimumSize(QSize(150, 49))
        self.label_digitVal3.setMaximumSize(QSize(800, 80))
        self.label_digitVal3.setStyleSheet(u"border: 2px solid #ffffff;\n"
"border-radius: 10px;\n"
"padding: 5px;")

        self.horizontalLayout_48.addWidget(self.label_digitVal3, 0, Qt.AlignmentFlag.AlignRight)

        self.label_digitStatus3 = QLabel(self.page12)
        self.label_digitStatus3.setObjectName(u"label_digitStatus3")
        self.label_digitStatus3.setMinimumSize(QSize(150, 49))
        self.label_digitStatus3.setMaximumSize(QSize(150, 80))
        self.label_digitStatus3.setStyleSheet(u"border: 2px solid #ffffff;\n"
"border-radius: 10px;\n"
"padding: 5px;")

        self.horizontalLayout_48.addWidget(self.label_digitStatus3, 0, Qt.AlignmentFlag.AlignLeft)

        self.label_digitVal4 = QLabel(self.page12)
        self.label_digitVal4.setObjectName(u"label_digitVal4")
        self.label_digitVal4.setMinimumSize(QSize(150, 49))
        self.label_digitVal4.setMaximumSize(QSize(800, 80))
        self.label_digitVal4.setStyleSheet(u"border: 2px solid #ffffff;\n"
"border-radius: 10px;\n"
"padding: 5px;")

        self.horizontalLayout_48.addWidget(self.label_digitVal4, 0, Qt.AlignmentFlag.AlignRight)

        self.label_digitStatus4 = QLabel(self.page12)
        self.label_digitStatus4.setObjectName(u"label_digitStatus4")
        self.label_digitStatus4.setMinimumSize(QSize(150, 49))
        self.label_digitStatus4.setMaximumSize(QSize(800, 80))
        self.label_digitStatus4.setStyleSheet(u"border: 2px solid #ffffff;\n"
"border-radius: 10px;\n"
"padding: 5px;")

        self.horizontalLayout_48.addWidget(self.label_digitStatus4, 0, Qt.AlignmentFlag.AlignLeft)


        self.page12Layout.addLayout(self.horizontalLayout_48)

        self.stackedWidget_main.addWidget(self.page12)
        self.page13 = QWidget()
        self.page13.setObjectName(u"page13")
        self.page13Layout = QVBoxLayout(self.page13)
        self.page13Layout.setObjectName(u"page13Layout")
        self.horizontalLayout_49 = QHBoxLayout()
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.button_addCncSettings = QPushButton(self.page13)
        self.button_addCncSettings.setObjectName(u"button_addCncSettings")
        sizePolicy1.setHeightForWidth(self.button_addCncSettings.sizePolicy().hasHeightForWidth())
        self.button_addCncSettings.setSizePolicy(sizePolicy1)
        self.button_addCncSettings.setMinimumSize(QSize(90, 40))
        self.button_addCncSettings.setMaximumSize(QSize(16777215, 40))
        self.button_addCncSettings.setFont(font1)

        self.horizontalLayout_49.addWidget(self.button_addCncSettings, 0, Qt.AlignmentFlag.AlignHCenter)

        self.button_modifyCncSettings = QPushButton(self.page13)
        self.button_modifyCncSettings.setObjectName(u"button_modifyCncSettings")
        sizePolicy1.setHeightForWidth(self.button_modifyCncSettings.sizePolicy().hasHeightForWidth())
        self.button_modifyCncSettings.setSizePolicy(sizePolicy1)
        self.button_modifyCncSettings.setMinimumSize(QSize(90, 40))
        self.button_modifyCncSettings.setMaximumSize(QSize(16777215, 40))
        self.button_modifyCncSettings.setFont(font1)

        self.horizontalLayout_49.addWidget(self.button_modifyCncSettings, 0, Qt.AlignmentFlag.AlignHCenter)

        self.button_deleteCncSettings = QPushButton(self.page13)
        self.button_deleteCncSettings.setObjectName(u"button_deleteCncSettings")
        sizePolicy1.setHeightForWidth(self.button_deleteCncSettings.sizePolicy().hasHeightForWidth())
        self.button_deleteCncSettings.setSizePolicy(sizePolicy1)
        self.button_deleteCncSettings.setMinimumSize(QSize(90, 40))
        self.button_deleteCncSettings.setMaximumSize(QSize(16777215, 40))
        self.button_deleteCncSettings.setFont(font1)

        self.horizontalLayout_49.addWidget(self.button_deleteCncSettings, 0, Qt.AlignmentFlag.AlignHCenter)


        self.page13Layout.addLayout(self.horizontalLayout_49)

        self.verticalSpacer_60 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.page13Layout.addItem(self.verticalSpacer_60)

        self.tableView_cncList = QTableView(self.page13)
        self.tableView_cncList.setObjectName(u"tableView_cncList")

        self.page13Layout.addWidget(self.tableView_cncList)

        self.stackedWidget_main.addWidget(self.page13)
        self.page14 = QWidget()
        self.page14.setObjectName(u"page14")
        self.page14Layout = QVBoxLayout(self.page14)
        self.page14Layout.setObjectName(u"page14Layout")
        self.horizontalLayout_50 = QHBoxLayout()
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.label_cncName = QLabel(self.page14)
        self.label_cncName.setObjectName(u"label_cncName")
        self.label_cncName.setFont(font1)

        self.horizontalLayout_50.addWidget(self.label_cncName, 0, Qt.AlignmentFlag.AlignRight)

        self.lineEdit_cncName = QLineEdit(self.page14)
        self.lineEdit_cncName.setObjectName(u"lineEdit_cncName")
        sizePolicy1.setHeightForWidth(self.lineEdit_cncName.sizePolicy().hasHeightForWidth())
        self.lineEdit_cncName.setSizePolicy(sizePolicy1)
        self.lineEdit_cncName.setMinimumSize(QSize(250, 35))
        self.lineEdit_cncName.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_cncName.setFont(font1)
        self.lineEdit_cncName.setStyleSheet(u"")

        self.horizontalLayout_50.addWidget(self.lineEdit_cncName, 0, Qt.AlignmentFlag.AlignLeft)


        self.page14Layout.addLayout(self.horizontalLayout_50)

        self.horizontalLayout_51 = QHBoxLayout()
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.label_cncIpAddress = QLabel(self.page14)
        self.label_cncIpAddress.setObjectName(u"label_cncIpAddress")
        self.label_cncIpAddress.setFont(font1)

        self.horizontalLayout_51.addWidget(self.label_cncIpAddress, 0, Qt.AlignmentFlag.AlignRight)

        self.lineEdit_cncIpAddress = QLineEdit(self.page14)
        self.lineEdit_cncIpAddress.setObjectName(u"lineEdit_cncIpAddress")
        sizePolicy1.setHeightForWidth(self.lineEdit_cncIpAddress.sizePolicy().hasHeightForWidth())
        self.lineEdit_cncIpAddress.setSizePolicy(sizePolicy1)
        self.lineEdit_cncIpAddress.setMinimumSize(QSize(250, 35))
        self.lineEdit_cncIpAddress.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_cncIpAddress.setFont(font1)
        self.lineEdit_cncIpAddress.setStyleSheet(u"")

        self.horizontalLayout_51.addWidget(self.lineEdit_cncIpAddress, 0, Qt.AlignmentFlag.AlignLeft)


        self.page14Layout.addLayout(self.horizontalLayout_51)

        self.horizontalLayout_52 = QHBoxLayout()
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.label_cncPortNumber = QLabel(self.page14)
        self.label_cncPortNumber.setObjectName(u"label_cncPortNumber")
        self.label_cncPortNumber.setFont(font1)

        self.horizontalLayout_52.addWidget(self.label_cncPortNumber, 0, Qt.AlignmentFlag.AlignRight)

        self.lineEdit_cncPortNumber = QLineEdit(self.page14)
        self.lineEdit_cncPortNumber.setObjectName(u"lineEdit_cncPortNumber")
        sizePolicy1.setHeightForWidth(self.lineEdit_cncPortNumber.sizePolicy().hasHeightForWidth())
        self.lineEdit_cncPortNumber.setSizePolicy(sizePolicy1)
        self.lineEdit_cncPortNumber.setMinimumSize(QSize(250, 35))
        self.lineEdit_cncPortNumber.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_cncPortNumber.setFont(font1)
        self.lineEdit_cncPortNumber.setStyleSheet(u"")

        self.horizontalLayout_52.addWidget(self.lineEdit_cncPortNumber, 0, Qt.AlignmentFlag.AlignLeft)


        self.page14Layout.addLayout(self.horizontalLayout_52)

        self.horizontalLayout_53 = QHBoxLayout()
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.label_cncSelectionType = QLabel(self.page14)
        self.label_cncSelectionType.setObjectName(u"label_cncSelectionType")
        self.label_cncSelectionType.setFont(font1)

        self.horizontalLayout_53.addWidget(self.label_cncSelectionType, 0, Qt.AlignmentFlag.AlignRight)

        self.comboBox_cncSelectionType = QComboBox(self.page14)
        self.comboBox_cncSelectionType.addItem("")
        self.comboBox_cncSelectionType.addItem("")
        self.comboBox_cncSelectionType.addItem("")
        self.comboBox_cncSelectionType.addItem("")
        self.comboBox_cncSelectionType.addItem("")
        self.comboBox_cncSelectionType.setObjectName(u"comboBox_cncSelectionType")
        self.comboBox_cncSelectionType.setMinimumSize(QSize(250, 35))
        self.comboBox_cncSelectionType.setMaximumSize(QSize(16777215, 16777215))
        self.comboBox_cncSelectionType.setFont(font1)
        self.comboBox_cncSelectionType.setStyleSheet(u"")

        self.horizontalLayout_53.addWidget(self.comboBox_cncSelectionType, 0, Qt.AlignmentFlag.AlignLeft)


        self.page14Layout.addLayout(self.horizontalLayout_53)

        self.horizontalLayout_54 = QHBoxLayout()
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.label_cncController = QLabel(self.page14)
        self.label_cncController.setObjectName(u"label_cncController")
        self.label_cncController.setFont(font1)

        self.horizontalLayout_54.addWidget(self.label_cncController, 0, Qt.AlignmentFlag.AlignRight)

        self.comboBox_cncController = QComboBox(self.page14)
        self.comboBox_cncController.addItem("")
        self.comboBox_cncController.addItem("")
        self.comboBox_cncController.addItem("")
        self.comboBox_cncController.setObjectName(u"comboBox_cncController")
        self.comboBox_cncController.setMinimumSize(QSize(250, 35))
        self.comboBox_cncController.setMaximumSize(QSize(16777215, 16777215))
        self.comboBox_cncController.setFont(font1)
        self.comboBox_cncController.setStyleSheet(u"")

        self.horizontalLayout_54.addWidget(self.comboBox_cncController, 0, Qt.AlignmentFlag.AlignLeft)


        self.page14Layout.addLayout(self.horizontalLayout_54)

        self.stackedWidget_main.addWidget(self.page14)
        self.page15 = QWidget()
        self.page15.setObjectName(u"page15")
        self.page15Layout = QVBoxLayout(self.page15)
        self.page15Layout.setObjectName(u"page15Layout")
        self.horizontalLayout_55 = QHBoxLayout()
        self.horizontalLayout_55.setSpacing(3)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.horizontalSpacer_25 = QSpacerItem(40, 35, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_55.addItem(self.horizontalSpacer_25)

        self.label_autoOffsetCorrection = QLabel(self.page15)
        self.label_autoOffsetCorrection.setObjectName(u"label_autoOffsetCorrection")
        self.label_autoOffsetCorrection.setMinimumSize(QSize(0, 35))
        self.label_autoOffsetCorrection.setFont(font1)

        self.horizontalLayout_55.addWidget(self.label_autoOffsetCorrection, 0, Qt.AlignmentFlag.AlignRight)

        self.toggleButton_aoc = QLabel(self.page15)
        self.toggleButton_aoc.setObjectName(u"toggleButton_aoc")
        self.toggleButton_aoc.setMinimumSize(QSize(0, 35))
        self.toggleButton_aoc.setPixmap(QPixmap(u"../home/torizon/app/src/Switcher_On.png"))

        self.horizontalLayout_55.addWidget(self.toggleButton_aoc, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalSpacer_26 = QSpacerItem(40, 35, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_55.addItem(self.horizontalSpacer_26)


        self.page15Layout.addLayout(self.horizontalLayout_55)

        self.line_19 = QFrame(self.page15)
        self.line_19.setObjectName(u"line_19")
        self.line_19.setFrameShape(QFrame.Shape.HLine)
        self.line_19.setFrameShadow(QFrame.Shadow.Sunken)

        self.page15Layout.addWidget(self.line_19)

        self.verticalSpacer_29 = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.page15Layout.addItem(self.verticalSpacer_29)

        self.horizontalLayout_57 = QHBoxLayout()
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.button_cncListAoc = QPushButton(self.page15)
        self.button_cncListAoc.setObjectName(u"button_cncListAoc")
        sizePolicy1.setHeightForWidth(self.button_cncListAoc.sizePolicy().hasHeightForWidth())
        self.button_cncListAoc.setSizePolicy(sizePolicy1)
        self.button_cncListAoc.setMinimumSize(QSize(150, 40))
        self.button_cncListAoc.setMaximumSize(QSize(16777215, 40))
        self.button_cncListAoc.setFont(font1)

        self.horizontalLayout_57.addWidget(self.button_cncListAoc, 0, Qt.AlignmentFlag.AlignHCenter)


        self.page15Layout.addLayout(self.horizontalLayout_57)

        self.verticalSpacer_30 = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.page15Layout.addItem(self.verticalSpacer_30)

        self.horizontalLayout_58 = QHBoxLayout()
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.button_reportsAoc = QPushButton(self.page15)
        self.button_reportsAoc.setObjectName(u"button_reportsAoc")
        sizePolicy1.setHeightForWidth(self.button_reportsAoc.sizePolicy().hasHeightForWidth())
        self.button_reportsAoc.setSizePolicy(sizePolicy1)
        self.button_reportsAoc.setMinimumSize(QSize(150, 40))
        self.button_reportsAoc.setMaximumSize(QSize(16777215, 40))
        self.button_reportsAoc.setFont(font1)

        self.horizontalLayout_58.addWidget(self.button_reportsAoc, 0, Qt.AlignmentFlag.AlignHCenter)


        self.page15Layout.addLayout(self.horizontalLayout_58)

        self.verticalSpacer_28 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.page15Layout.addItem(self.verticalSpacer_28)

        self.stackedWidget_main.addWidget(self.page15)
        self.page_16 = QWidget()
        self.page_16.setObjectName(u"page_16")
        self.verticalLayout_page16 = QVBoxLayout(self.page_16)
        self.verticalLayout_page16.setObjectName(u"verticalLayout_page16")
        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.label_modelNo = QLabel(self.page_16)
        self.label_modelNo.setObjectName(u"label_modelNo")

        self.horizontalLayout_31.addWidget(self.label_modelNo, 0, Qt.AlignmentFlag.AlignRight)

        self.lineEdit_modelNo = QLineEdit(self.page_16)
        self.lineEdit_modelNo.setObjectName(u"lineEdit_modelNo")
        self.lineEdit_modelNo.setMinimumSize(QSize(0, 35))

        self.horizontalLayout_31.addWidget(self.lineEdit_modelNo, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_page16.addLayout(self.horizontalLayout_31)

        self.horizontalLayout_37 = QHBoxLayout()
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.label_serialNo = QLabel(self.page_16)
        self.label_serialNo.setObjectName(u"label_serialNo")

        self.horizontalLayout_37.addWidget(self.label_serialNo, 0, Qt.AlignmentFlag.AlignRight)

        self.lineEdit_serialNo = QLineEdit(self.page_16)
        self.lineEdit_serialNo.setObjectName(u"lineEdit_serialNo")

        self.horizontalLayout_37.addWidget(self.lineEdit_serialNo, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_page16.addLayout(self.horizontalLayout_37)

        self.stackedWidget_main.addWidget(self.page_16)
        self.page17 = QWidget()
        self.page17.setObjectName(u"page17")
        self.page17Layout = QVBoxLayout(self.page17)
        self.page17Layout.setObjectName(u"page17Layout")
        self.verticalSpacer_32 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.page17Layout.addItem(self.verticalSpacer_32)

        self.horizontalLayout_84 = QHBoxLayout()
        self.horizontalLayout_84.setObjectName(u"horizontalLayout_84")
        self.horizontalSpacer_27 = QSpacerItem(40, 40, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_84.addItem(self.horizontalSpacer_27)

        self.label_networkBasedDatabase = QLabel(self.page17)
        self.label_networkBasedDatabase.setObjectName(u"label_networkBasedDatabase")
        self.label_networkBasedDatabase.setMinimumSize(QSize(0, 35))
        self.label_networkBasedDatabase.setFont(font1)

        self.horizontalLayout_84.addWidget(self.label_networkBasedDatabase)

        self.toggleButton_networkBasedDatabase = QLabel(self.page17)
        self.toggleButton_networkBasedDatabase.setObjectName(u"toggleButton_networkBasedDatabase")
        self.toggleButton_networkBasedDatabase.setMinimumSize(QSize(60, 35))
        self.toggleButton_networkBasedDatabase.setPixmap(QPixmap(u"../Switcher_On.png"))

        self.horizontalLayout_84.addWidget(self.toggleButton_networkBasedDatabase)

        self.horizontalSpacer_28 = QSpacerItem(40, 40, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_84.addItem(self.horizontalSpacer_28)


        self.page17Layout.addLayout(self.horizontalLayout_84)

        self.line_21 = QFrame(self.page17)
        self.line_21.setObjectName(u"line_21")
        self.line_21.setFrameShape(QFrame.Shape.HLine)
        self.line_21.setFrameShadow(QFrame.Shadow.Sunken)

        self.page17Layout.addWidget(self.line_21)

        self.verticalSpacer_34 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.page17Layout.addItem(self.verticalSpacer_34)

        self.horizontalLayout_61 = QHBoxLayout()
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.label_driverNameDb = QLabel(self.page17)
        self.label_driverNameDb.setObjectName(u"label_driverNameDb")
        self.label_driverNameDb.setFont(font1)

        self.horizontalLayout_61.addWidget(self.label_driverNameDb, 0, Qt.AlignmentFlag.AlignRight)

        self.lineEdit_driverNameDb = QLineEdit(self.page17)
        self.lineEdit_driverNameDb.setObjectName(u"lineEdit_driverNameDb")
        sizePolicy1.setHeightForWidth(self.lineEdit_driverNameDb.sizePolicy().hasHeightForWidth())
        self.lineEdit_driverNameDb.setSizePolicy(sizePolicy1)
        self.lineEdit_driverNameDb.setMinimumSize(QSize(250, 35))
        self.lineEdit_driverNameDb.setFont(font1)
        self.lineEdit_driverNameDb.setStyleSheet(u"")

        self.horizontalLayout_61.addWidget(self.lineEdit_driverNameDb, 0, Qt.AlignmentFlag.AlignLeft)


        self.page17Layout.addLayout(self.horizontalLayout_61)

        self.horizontalLayout_79 = QHBoxLayout()
        self.horizontalLayout_79.setObjectName(u"horizontalLayout_79")
        self.label_serverNameDb = QLabel(self.page17)
        self.label_serverNameDb.setObjectName(u"label_serverNameDb")
        self.label_serverNameDb.setFont(font1)

        self.horizontalLayout_79.addWidget(self.label_serverNameDb, 0, Qt.AlignmentFlag.AlignRight)

        self.lineEdit_serverNameDb = QLineEdit(self.page17)
        self.lineEdit_serverNameDb.setObjectName(u"lineEdit_serverNameDb")
        sizePolicy1.setHeightForWidth(self.lineEdit_serverNameDb.sizePolicy().hasHeightForWidth())
        self.lineEdit_serverNameDb.setSizePolicy(sizePolicy1)
        self.lineEdit_serverNameDb.setMinimumSize(QSize(250, 35))
        self.lineEdit_serverNameDb.setFont(font1)
        self.lineEdit_serverNameDb.setStyleSheet(u"")

        self.horizontalLayout_79.addWidget(self.lineEdit_serverNameDb, 0, Qt.AlignmentFlag.AlignLeft)


        self.page17Layout.addLayout(self.horizontalLayout_79)

        self.horizontalLayout_80 = QHBoxLayout()
        self.horizontalLayout_80.setObjectName(u"horizontalLayout_80")
        self.label_databaseNameDb = QLabel(self.page17)
        self.label_databaseNameDb.setObjectName(u"label_databaseNameDb")
        self.label_databaseNameDb.setFont(font1)

        self.horizontalLayout_80.addWidget(self.label_databaseNameDb, 0, Qt.AlignmentFlag.AlignRight)

        self.lineEdit_databaseNameDb = QLineEdit(self.page17)
        self.lineEdit_databaseNameDb.setObjectName(u"lineEdit_databaseNameDb")
        self.lineEdit_databaseNameDb.setMinimumSize(QSize(250, 35))
        self.lineEdit_databaseNameDb.setFont(font1)
        self.lineEdit_databaseNameDb.setStyleSheet(u"")

        self.horizontalLayout_80.addWidget(self.lineEdit_databaseNameDb, 0, Qt.AlignmentFlag.AlignLeft)


        self.page17Layout.addLayout(self.horizontalLayout_80)

        self.horizontalLayout_81 = QHBoxLayout()
        self.horizontalLayout_81.setObjectName(u"horizontalLayout_81")
        self.label_username_Db = QLabel(self.page17)
        self.label_username_Db.setObjectName(u"label_username_Db")
        self.label_username_Db.setFont(font1)

        self.horizontalLayout_81.addWidget(self.label_username_Db, 0, Qt.AlignmentFlag.AlignRight)

        self.lineEdit_usernameDb = QLineEdit(self.page17)
        self.lineEdit_usernameDb.setObjectName(u"lineEdit_usernameDb")
        sizePolicy1.setHeightForWidth(self.lineEdit_usernameDb.sizePolicy().hasHeightForWidth())
        self.lineEdit_usernameDb.setSizePolicy(sizePolicy1)
        self.lineEdit_usernameDb.setMinimumSize(QSize(250, 35))
        self.lineEdit_usernameDb.setFont(font1)
        self.lineEdit_usernameDb.setStyleSheet(u"")

        self.horizontalLayout_81.addWidget(self.lineEdit_usernameDb, 0, Qt.AlignmentFlag.AlignLeft)


        self.page17Layout.addLayout(self.horizontalLayout_81)

        self.horizontalLayout_82 = QHBoxLayout()
        self.horizontalLayout_82.setObjectName(u"horizontalLayout_82")
        self.label_passwordDb = QLabel(self.page17)
        self.label_passwordDb.setObjectName(u"label_passwordDb")
        self.label_passwordDb.setFont(font1)

        self.horizontalLayout_82.addWidget(self.label_passwordDb, 0, Qt.AlignmentFlag.AlignRight)

        self.lineEdit_passwordDb = QLineEdit(self.page17)
        self.lineEdit_passwordDb.setObjectName(u"lineEdit_passwordDb")
        sizePolicy1.setHeightForWidth(self.lineEdit_passwordDb.sizePolicy().hasHeightForWidth())
        self.lineEdit_passwordDb.setSizePolicy(sizePolicy1)
        self.lineEdit_passwordDb.setMinimumSize(QSize(250, 35))
        self.lineEdit_passwordDb.setFont(font1)
        self.lineEdit_passwordDb.setStyleSheet(u"")

        self.horizontalLayout_82.addWidget(self.lineEdit_passwordDb, 0, Qt.AlignmentFlag.AlignLeft)


        self.page17Layout.addLayout(self.horizontalLayout_82)

        self.horizontalLayout_56 = QHBoxLayout()
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.label_deviceName = QLabel(self.page17)
        self.label_deviceName.setObjectName(u"label_deviceName")

        self.horizontalLayout_56.addWidget(self.label_deviceName, 0, Qt.AlignmentFlag.AlignRight)

        self.lineEdit_deviceName = QLineEdit(self.page17)
        self.lineEdit_deviceName.setObjectName(u"lineEdit_deviceName")
        self.lineEdit_deviceName.setMinimumSize(QSize(250, 35))

        self.horizontalLayout_56.addWidget(self.lineEdit_deviceName, 0, Qt.AlignmentFlag.AlignLeft)


        self.page17Layout.addLayout(self.horizontalLayout_56)

        self.stackedWidget_main.addWidget(self.page17)
        self.page18 = QWidget()
        self.page18.setObjectName(u"page18")
        self.page18Layout = QVBoxLayout(self.page18)
        self.page18Layout.setObjectName(u"page18Layout")
        self.horizontalLayout_151 = QHBoxLayout()
        self.horizontalLayout_151.setObjectName(u"horizontalLayout_151")
        self.horizontalSpacer_185 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_151.addItem(self.horizontalSpacer_185)

        self.label_programIdforSettings_1 = QLabel(self.page18)
        self.label_programIdforSettings_1.setObjectName(u"label_programIdforSettings_1")
        sizePolicy1.setHeightForWidth(self.label_programIdforSettings_1.sizePolicy().hasHeightForWidth())
        self.label_programIdforSettings_1.setSizePolicy(sizePolicy1)
        self.label_programIdforSettings_1.setMinimumSize(QSize(0, 35))
        self.label_programIdforSettings_1.setMaximumSize(QSize(120, 16777215))
        self.label_programIdforSettings_1.setFont(font1)

        self.horizontalLayout_151.addWidget(self.label_programIdforSettings_1)

        self.comboBox_programIdSettings_1 = QComboBox(self.page18)
        self.comboBox_programIdSettings_1.setObjectName(u"comboBox_programIdSettings_1")
        sizePolicy1.setHeightForWidth(self.comboBox_programIdSettings_1.sizePolicy().hasHeightForWidth())
        self.comboBox_programIdSettings_1.setSizePolicy(sizePolicy1)
        self.comboBox_programIdSettings_1.setMinimumSize(QSize(20, 35))
        self.comboBox_programIdSettings_1.setMaximumSize(QSize(70, 16777215))
        self.comboBox_programIdSettings_1.setFont(font1)

        self.horizontalLayout_151.addWidget(self.comboBox_programIdSettings_1)

        self.horizontalSpacer_132 = QSpacerItem(20, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_151.addItem(self.horizontalSpacer_132)

        self.label_programNameSettings_1 = QLabel(self.page18)
        self.label_programNameSettings_1.setObjectName(u"label_programNameSettings_1")
        sizePolicy1.setHeightForWidth(self.label_programNameSettings_1.sizePolicy().hasHeightForWidth())
        self.label_programNameSettings_1.setSizePolicy(sizePolicy1)
        self.label_programNameSettings_1.setFont(font1)

        self.horizontalLayout_151.addWidget(self.label_programNameSettings_1)

        self.lineEdit_programNameSettings_1 = QLineEdit(self.page18)
        self.lineEdit_programNameSettings_1.setObjectName(u"lineEdit_programNameSettings_1")
        sizePolicy1.setHeightForWidth(self.lineEdit_programNameSettings_1.sizePolicy().hasHeightForWidth())
        self.lineEdit_programNameSettings_1.setSizePolicy(sizePolicy1)
        self.lineEdit_programNameSettings_1.setMinimumSize(QSize(270, 35))
        self.lineEdit_programNameSettings_1.setFont(font1)

        self.horizontalLayout_151.addWidget(self.lineEdit_programNameSettings_1)

        self.horizontalSpacer_137 = QSpacerItem(20, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_151.addItem(self.horizontalSpacer_137)

        self.button_staticSettingsForAll_1 = QPushButton(self.page18)
        self.button_staticSettingsForAll_1.setObjectName(u"button_staticSettingsForAll_1")
        sizePolicy1.setHeightForWidth(self.button_staticSettingsForAll_1.sizePolicy().hasHeightForWidth())
        self.button_staticSettingsForAll_1.setSizePolicy(sizePolicy1)
        self.button_staticSettingsForAll_1.setMinimumSize(QSize(100, 40))
        self.button_staticSettingsForAll_1.setFont(font1)

        self.horizontalLayout_151.addWidget(self.button_staticSettingsForAll_1)

        self.horizontalSpacer_141 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_151.addItem(self.horizontalSpacer_141)


        self.page18Layout.addLayout(self.horizontalLayout_151)

        self.horizontalLayout_173 = QHBoxLayout()
        self.horizontalLayout_173.setObjectName(u"horizontalLayout_173")
        self.horizontalSpacer_146 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_173.addItem(self.horizontalSpacer_146)

        self.label_probeSetting_1 = QLabel(self.page18)
        self.label_probeSetting_1.setObjectName(u"label_probeSetting_1")
        sizePolicy1.setHeightForWidth(self.label_probeSetting_1.sizePolicy().hasHeightForWidth())
        self.label_probeSetting_1.setSizePolicy(sizePolicy1)
        self.label_probeSetting_1.setFont(font1)

        self.horizontalLayout_173.addWidget(self.label_probeSetting_1, 0, Qt.AlignmentFlag.AlignHCenter)

        self.comboBox_toselectProbe_1 = QComboBox(self.page18)
        self.comboBox_toselectProbe_1.addItem("")
        self.comboBox_toselectProbe_1.addItem("")
        self.comboBox_toselectProbe_1.addItem("")
        self.comboBox_toselectProbe_1.addItem("")
        self.comboBox_toselectProbe_1.addItem("")
        self.comboBox_toselectProbe_1.addItem("")
        self.comboBox_toselectProbe_1.addItem("")
        self.comboBox_toselectProbe_1.addItem("")
        self.comboBox_toselectProbe_1.setObjectName(u"comboBox_toselectProbe_1")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.comboBox_toselectProbe_1.sizePolicy().hasHeightForWidth())
        self.comboBox_toselectProbe_1.setSizePolicy(sizePolicy4)
        self.comboBox_toselectProbe_1.setMinimumSize(QSize(110, 35))
        self.comboBox_toselectProbe_1.setFont(font1)

        self.horizontalLayout_173.addWidget(self.comboBox_toselectProbe_1, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalSpacer_163 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_173.addItem(self.horizontalSpacer_163)


        self.page18Layout.addLayout(self.horizontalLayout_173)

        self.line_63 = QFrame(self.page18)
        self.line_63.setObjectName(u"line_63")
        self.line_63.setFrameShape(QFrame.Shape.HLine)
        self.line_63.setFrameShadow(QFrame.Shadow.Sunken)

        self.page18Layout.addWidget(self.line_63)

        self.tabWidget = QTabWidget(self.page18)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy1.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy1)
        self.tabWidget.setMinimumSize(QSize(0, 50))
        self.tabWidget.setMaximumSize(QSize(900, 16777215))
        font6 = QFont()
        font6.setFamilies([u"MS Shell Dlg 2"])
        font6.setPointSize(10)
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
        self.verticalLayout_10 = QVBoxLayout(self.tab)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.scrollArea_2 = QScrollArea(self.tab)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setMinimumSize(QSize(0, 30))
        self.scrollArea_2.setStyleSheet(u"QScrollBar:vertical {\n"
"        width: 30px;              /* set scrollbar width */\n"
"    }")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 331, 829))
        self.verticalLayout_8 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.label_formula_1 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_formula_1.setObjectName(u"label_formula_1")
        sizePolicy1.setHeightForWidth(self.label_formula_1.sizePolicy().hasHeightForWidth())
        self.label_formula_1.setSizePolicy(sizePolicy1)
        self.label_formula_1.setFont(font1)

        self.horizontalLayout_30.addWidget(self.label_formula_1, 0, Qt.AlignmentFlag.AlignRight)

        self.label_formulaBar_1 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_formulaBar_1.setObjectName(u"label_formulaBar_1")
        self.label_formulaBar_1.setMinimumSize(QSize(0, 35))
        self.label_formulaBar_1.setFont(font1)

        self.horizontalLayout_30.addWidget(self.label_formulaBar_1)

        self.button_setFormulaSettings_1 = QPushButton(self.scrollAreaWidgetContents_2)
        self.button_setFormulaSettings_1.setObjectName(u"button_setFormulaSettings_1")
        sizePolicy1.setHeightForWidth(self.button_setFormulaSettings_1.sizePolicy().hasHeightForWidth())
        self.button_setFormulaSettings_1.setSizePolicy(sizePolicy1)
        self.button_setFormulaSettings_1.setMinimumSize(QSize(150, 30))
        self.button_setFormulaSettings_1.setMaximumSize(QSize(16777215, 40))
        self.button_setFormulaSettings_1.setFont(font1)

        self.horizontalLayout_30.addWidget(self.button_setFormulaSettings_1)

        self.horizontalSpacer_175 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_30.addItem(self.horizontalSpacer_175)


        self.verticalLayout_8.addLayout(self.horizontalLayout_30)

        self.horizontalLayout_159 = QHBoxLayout()
        self.horizontalLayout_159.setObjectName(u"horizontalLayout_159")
        self.label_masterType_1 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_masterType_1.setObjectName(u"label_masterType_1")
        sizePolicy1.setHeightForWidth(self.label_masterType_1.sizePolicy().hasHeightForWidth())
        self.label_masterType_1.setSizePolicy(sizePolicy1)
        self.label_masterType_1.setFont(font1)

        self.horizontalLayout_159.addWidget(self.label_masterType_1, 0, Qt.AlignmentFlag.AlignRight)

        self.comboBox_masterType_1 = QComboBox(self.scrollAreaWidgetContents_2)
        self.comboBox_masterType_1.addItem("")
        self.comboBox_masterType_1.addItem("")
        self.comboBox_masterType_1.setObjectName(u"comboBox_masterType_1")
        self.comboBox_masterType_1.setMinimumSize(QSize(160, 35))
        self.comboBox_masterType_1.setMaximumSize(QSize(180, 16777215))
        self.comboBox_masterType_1.setFont(font1)

        self.horizontalLayout_159.addWidget(self.comboBox_masterType_1, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_8.addLayout(self.horizontalLayout_159)

        self.horizontalLayout_122 = QHBoxLayout()
        self.horizontalLayout_122.setObjectName(u"horizontalLayout_122")
        self.label_masterLower_1 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_masterLower_1.setObjectName(u"label_masterLower_1")
        sizePolicy1.setHeightForWidth(self.label_masterLower_1.sizePolicy().hasHeightForWidth())
        self.label_masterLower_1.setSizePolicy(sizePolicy1)
        self.label_masterLower_1.setFont(font1)

        self.horizontalLayout_122.addWidget(self.label_masterLower_1, 0, Qt.AlignmentFlag.AlignRight)

        self.lineEdit_masterLower_1 = QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_masterLower_1.setObjectName(u"lineEdit_masterLower_1")
        sizePolicy1.setHeightForWidth(self.lineEdit_masterLower_1.sizePolicy().hasHeightForWidth())
        self.lineEdit_masterLower_1.setSizePolicy(sizePolicy1)
        self.lineEdit_masterLower_1.setMinimumSize(QSize(0, 35))
        self.lineEdit_masterLower_1.setMaximumSize(QSize(180, 16777215))
        self.lineEdit_masterLower_1.setFont(font1)

        self.horizontalLayout_122.addWidget(self.lineEdit_masterLower_1, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_8.addLayout(self.horizontalLayout_122)

        self.horizontalLayout_132 = QHBoxLayout()
        self.horizontalLayout_132.setObjectName(u"horizontalLayout_132")
        self.label_master_1 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_master_1.setObjectName(u"label_master_1")
        sizePolicy1.setHeightForWidth(self.label_master_1.sizePolicy().hasHeightForWidth())
        self.label_master_1.setSizePolicy(sizePolicy1)
        self.label_master_1.setFont(font1)

        self.horizontalLayout_132.addWidget(self.label_master_1, 0, Qt.AlignmentFlag.AlignRight)

        self.lineEdit_master_1 = QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_master_1.setObjectName(u"lineEdit_master_1")
        sizePolicy1.setHeightForWidth(self.lineEdit_master_1.sizePolicy().hasHeightForWidth())
        self.lineEdit_master_1.setSizePolicy(sizePolicy1)
        self.lineEdit_master_1.setMinimumSize(QSize(150, 35))
        self.lineEdit_master_1.setMaximumSize(QSize(180, 16777215))
        self.lineEdit_master_1.setFont(font1)

        self.horizontalLayout_132.addWidget(self.lineEdit_master_1, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_8.addLayout(self.horizontalLayout_132)

        self.horizontalLayout_123 = QHBoxLayout()
        self.horizontalLayout_123.setObjectName(u"horizontalLayout_123")
        self.label_masterHigher_1 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_masterHigher_1.setObjectName(u"label_masterHigher_1")
        sizePolicy1.setHeightForWidth(self.label_masterHigher_1.sizePolicy().hasHeightForWidth())
        self.label_masterHigher_1.setSizePolicy(sizePolicy1)
        self.label_masterHigher_1.setFont(font1)

        self.horizontalLayout_123.addWidget(self.label_masterHigher_1, 0, Qt.AlignmentFlag.AlignRight)

        self.lineEdit_masterHigher_1 = QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_masterHigher_1.setObjectName(u"lineEdit_masterHigher_1")
        sizePolicy1.setHeightForWidth(self.lineEdit_masterHigher_1.sizePolicy().hasHeightForWidth())
        self.lineEdit_masterHigher_1.setSizePolicy(sizePolicy1)
        self.lineEdit_masterHigher_1.setMaximumSize(QSize(180, 16777215))
        self.lineEdit_masterHigher_1.setFont(font1)

        self.horizontalLayout_123.addWidget(self.lineEdit_masterHigher_1, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_8.addLayout(self.horizontalLayout_123)

        self.horizontalLayout_157 = QHBoxLayout()
        self.horizontalLayout_157.setObjectName(u"horizontalLayout_157")
        self.label_upperOffsetLimit_1 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_upperOffsetLimit_1.setObjectName(u"label_upperOffsetLimit_1")
        sizePolicy1.setHeightForWidth(self.label_upperOffsetLimit_1.sizePolicy().hasHeightForWidth())
        self.label_upperOffsetLimit_1.setSizePolicy(sizePolicy1)
        self.label_upperOffsetLimit_1.setMaximumSize(QSize(16777215, 16777215))
        self.label_upperOffsetLimit_1.setFont(font1)

        self.horizontalLayout_157.addWidget(self.label_upperOffsetLimit_1, 0, Qt.AlignmentFlag.AlignRight)

        self.lineEdit_upperOffcetLimit_1 = QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_upperOffcetLimit_1.setObjectName(u"lineEdit_upperOffcetLimit_1")
        sizePolicy1.setHeightForWidth(self.lineEdit_upperOffcetLimit_1.sizePolicy().hasHeightForWidth())
        self.lineEdit_upperOffcetLimit_1.setSizePolicy(sizePolicy1)
        self.lineEdit_upperOffcetLimit_1.setMaximumSize(QSize(180, 16777215))
        self.lineEdit_upperOffcetLimit_1.setFont(font1)

        self.horizontalLayout_157.addWidget(self.lineEdit_upperOffcetLimit_1, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_8.addLayout(self.horizontalLayout_157)

        self.horizontalLayout_130 = QHBoxLayout()
        self.horizontalLayout_130.setObjectName(u"horizontalLayout_130")
        self.label_usl_1 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_usl_1.setObjectName(u"label_usl_1")
        sizePolicy4.setHeightForWidth(self.label_usl_1.sizePolicy().hasHeightForWidth())
        self.label_usl_1.setSizePolicy(sizePolicy4)
        self.label_usl_1.setFont(font1)

        self.horizontalLayout_130.addWidget(self.label_usl_1, 0, Qt.AlignmentFlag.AlignRight)

        self.lineEdit_usl_1 = QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_usl_1.setObjectName(u"lineEdit_usl_1")
        sizePolicy4.setHeightForWidth(self.lineEdit_usl_1.sizePolicy().hasHeightForWidth())
        self.lineEdit_usl_1.setSizePolicy(sizePolicy4)
        self.lineEdit_usl_1.setMaximumSize(QSize(180, 16777215))
        self.lineEdit_usl_1.setFont(font1)

        self.horizontalLayout_130.addWidget(self.lineEdit_usl_1, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_8.addLayout(self.horizontalLayout_130)

        self.horizontalLayout_134 = QHBoxLayout()
        self.horizontalLayout_134.setObjectName(u"horizontalLayout_134")
        self.label_ucl_1 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_ucl_1.setObjectName(u"label_ucl_1")
        sizePolicy4.setHeightForWidth(self.label_ucl_1.sizePolicy().hasHeightForWidth())
        self.label_ucl_1.setSizePolicy(sizePolicy4)
        self.label_ucl_1.setMaximumSize(QSize(16777215, 16777215))
        self.label_ucl_1.setFont(font1)

        self.horizontalLayout_134.addWidget(self.label_ucl_1, 0, Qt.AlignmentFlag.AlignRight)

        self.lineEdit_ucl_1 = QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_ucl_1.setObjectName(u"lineEdit_ucl_1")
        sizePolicy4.setHeightForWidth(self.lineEdit_ucl_1.sizePolicy().hasHeightForWidth())
        self.lineEdit_ucl_1.setSizePolicy(sizePolicy4)
        self.lineEdit_ucl_1.setMaximumSize(QSize(180, 16777215))
        self.lineEdit_ucl_1.setFont(font1)

        self.horizontalLayout_134.addWidget(self.lineEdit_ucl_1, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_8.addLayout(self.horizontalLayout_134)

        self.horizontalLayout_128 = QHBoxLayout()
        self.horizontalLayout_128.setObjectName(u"horizontalLayout_128")
        self.label_nominalValue_1 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_nominalValue_1.setObjectName(u"label_nominalValue_1")
        sizePolicy1.setHeightForWidth(self.label_nominalValue_1.sizePolicy().hasHeightForWidth())
        self.label_nominalValue_1.setSizePolicy(sizePolicy1)
        self.label_nominalValue_1.setFont(font1)

        self.horizontalLayout_128.addWidget(self.label_nominalValue_1, 0, Qt.AlignmentFlag.AlignRight)

        self.lineEdit_nominalValue_1 = QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_nominalValue_1.setObjectName(u"lineEdit_nominalValue_1")
        sizePolicy4.setHeightForWidth(self.lineEdit_nominalValue_1.sizePolicy().hasHeightForWidth())
        self.lineEdit_nominalValue_1.setSizePolicy(sizePolicy4)
        self.lineEdit_nominalValue_1.setMaximumSize(QSize(180, 16777215))
        self.lineEdit_nominalValue_1.setFont(font1)

        self.horizontalLayout_128.addWidget(self.lineEdit_nominalValue_1, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_8.addLayout(self.horizontalLayout_128)

        self.horizontalLayout_136 = QHBoxLayout()
        self.horizontalLayout_136.setObjectName(u"horizontalLayout_136")
        self.label_lcl_1 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_lcl_1.setObjectName(u"label_lcl_1")
        sizePolicy1.setHeightForWidth(self.label_lcl_1.sizePolicy().hasHeightForWidth())
        self.label_lcl_1.setSizePolicy(sizePolicy1)
        self.label_lcl_1.setFont(font1)

        self.horizontalLayout_136.addWidget(self.label_lcl_1, 0, Qt.AlignmentFlag.AlignRight)

        self.lineEdit_lcl_1 = QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_lcl_1.setObjectName(u"lineEdit_lcl_1")
        sizePolicy4.setHeightForWidth(self.lineEdit_lcl_1.sizePolicy().hasHeightForWidth())
        self.lineEdit_lcl_1.setSizePolicy(sizePolicy4)
        self.lineEdit_lcl_1.setMaximumSize(QSize(180, 16777215))
        self.lineEdit_lcl_1.setFont(font1)

        self.horizontalLayout_136.addWidget(self.lineEdit_lcl_1, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_8.addLayout(self.horizontalLayout_136)

        self.horizontalLayout_124 = QHBoxLayout()
        self.horizontalLayout_124.setObjectName(u"horizontalLayout_124")
        self.label_lsl_1 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_lsl_1.setObjectName(u"label_lsl_1")
        sizePolicy1.setHeightForWidth(self.label_lsl_1.sizePolicy().hasHeightForWidth())
        self.label_lsl_1.setSizePolicy(sizePolicy1)
        self.label_lsl_1.setFont(font1)

        self.horizontalLayout_124.addWidget(self.label_lsl_1, 0, Qt.AlignmentFlag.AlignRight)

        self.lineEdit_lsl_1 = QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_lsl_1.setObjectName(u"lineEdit_lsl_1")
        sizePolicy1.setHeightForWidth(self.lineEdit_lsl_1.sizePolicy().hasHeightForWidth())
        self.lineEdit_lsl_1.setSizePolicy(sizePolicy1)
        self.lineEdit_lsl_1.setMaximumSize(QSize(180, 16777215))
        self.lineEdit_lsl_1.setFont(font1)

        self.horizontalLayout_124.addWidget(self.lineEdit_lsl_1, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_8.addLayout(self.horizontalLayout_124)

        self.horizontalLayout_158 = QHBoxLayout()
        self.horizontalLayout_158.setObjectName(u"horizontalLayout_158")
        self.label_lowerOffsetLimit_1 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_lowerOffsetLimit_1.setObjectName(u"label_lowerOffsetLimit_1")
        sizePolicy1.setHeightForWidth(self.label_lowerOffsetLimit_1.sizePolicy().hasHeightForWidth())
        self.label_lowerOffsetLimit_1.setSizePolicy(sizePolicy1)
        self.label_lowerOffsetLimit_1.setFont(font1)

        self.horizontalLayout_158.addWidget(self.label_lowerOffsetLimit_1, 0, Qt.AlignmentFlag.AlignRight)

        self.lineEdit_lowerOffsetLimit_1 = QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_lowerOffsetLimit_1.setObjectName(u"lineEdit_lowerOffsetLimit_1")
        sizePolicy1.setHeightForWidth(self.lineEdit_lowerOffsetLimit_1.sizePolicy().hasHeightForWidth())
        self.lineEdit_lowerOffsetLimit_1.setSizePolicy(sizePolicy1)
        self.lineEdit_lowerOffsetLimit_1.setMaximumSize(QSize(180, 16777215))
        self.lineEdit_lowerOffsetLimit_1.setFont(font1)

        self.horizontalLayout_158.addWidget(self.lineEdit_lowerOffsetLimit_1, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_8.addLayout(self.horizontalLayout_158)

        self.horizontalLayout_160 = QHBoxLayout()
        self.horizontalLayout_160.setObjectName(u"horizontalLayout_160")
        self.label_ovality_1 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_ovality_1.setObjectName(u"label_ovality_1")
        sizePolicy1.setHeightForWidth(self.label_ovality_1.sizePolicy().hasHeightForWidth())
        self.label_ovality_1.setSizePolicy(sizePolicy1)
        self.label_ovality_1.setFont(font1)

        self.horizontalLayout_160.addWidget(self.label_ovality_1, 0, Qt.AlignmentFlag.AlignRight)

        self.comboBox_ovalityOnOff_1 = QComboBox(self.scrollAreaWidgetContents_2)
        self.comboBox_ovalityOnOff_1.addItem("")
        self.comboBox_ovalityOnOff_1.addItem("")
        self.comboBox_ovalityOnOff_1.setObjectName(u"comboBox_ovalityOnOff_1")
        self.comboBox_ovalityOnOff_1.setMinimumSize(QSize(180, 35))
        self.comboBox_ovalityOnOff_1.setMaximumSize(QSize(16777215, 16777215))
        self.comboBox_ovalityOnOff_1.setFont(font1)

        self.horizontalLayout_160.addWidget(self.comboBox_ovalityOnOff_1, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_8.addLayout(self.horizontalLayout_160)

        self.horizontalLayout_120 = QHBoxLayout()
        self.horizontalLayout_120.setObjectName(u"horizontalLayout_120")
        self.label_range_1 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_range_1.setObjectName(u"label_range_1")
        sizePolicy1.setHeightForWidth(self.label_range_1.sizePolicy().hasHeightForWidth())
        self.label_range_1.setSizePolicy(sizePolicy1)
        self.label_range_1.setFont(font1)

        self.horizontalLayout_120.addWidget(self.label_range_1, 0, Qt.AlignmentFlag.AlignRight)

        self.comboBox_rangeProbe_1 = QComboBox(self.scrollAreaWidgetContents_2)
        self.comboBox_rangeProbe_1.setObjectName(u"comboBox_rangeProbe_1")
        self.comboBox_rangeProbe_1.setMinimumSize(QSize(180, 35))
        self.comboBox_rangeProbe_1.setMaximumSize(QSize(16777215, 16777215))
        self.comboBox_rangeProbe_1.setFont(font1)

        self.horizontalLayout_120.addWidget(self.comboBox_rangeProbe_1, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_8.addLayout(self.horizontalLayout_120)

        self.horizontalLayout_131 = QHBoxLayout()
        self.horizontalLayout_131.setObjectName(u"horizontalLayout_131")
        self.label_method_1 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_method_1.setObjectName(u"label_method_1")
        sizePolicy1.setHeightForWidth(self.label_method_1.sizePolicy().hasHeightForWidth())
        self.label_method_1.setSizePolicy(sizePolicy1)
        self.label_method_1.setFont(font1)

        self.horizontalLayout_131.addWidget(self.label_method_1, 0, Qt.AlignmentFlag.AlignRight)

        self.comboBox_methodProbe_1 = QComboBox(self.scrollAreaWidgetContents_2)
        self.comboBox_methodProbe_1.addItem("")
        self.comboBox_methodProbe_1.addItem("")
        self.comboBox_methodProbe_1.setObjectName(u"comboBox_methodProbe_1")
        self.comboBox_methodProbe_1.setMinimumSize(QSize(180, 35))
        self.comboBox_methodProbe_1.setMaximumSize(QSize(16777215, 16777215))
        self.comboBox_methodProbe_1.setFont(font1)

        self.horizontalLayout_131.addWidget(self.comboBox_methodProbe_1, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_8.addLayout(self.horizontalLayout_131)

        self.horizontalLayout_121 = QHBoxLayout()
        self.horizontalLayout_121.setObjectName(u"horizontalLayout_121")
        self.label_case_1 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_case_1.setObjectName(u"label_case_1")
        sizePolicy1.setHeightForWidth(self.label_case_1.sizePolicy().hasHeightForWidth())
        self.label_case_1.setSizePolicy(sizePolicy1)
        self.label_case_1.setFont(font1)

        self.horizontalLayout_121.addWidget(self.label_case_1, 0, Qt.AlignmentFlag.AlignRight)

        self.comboBox_caseProbe_1 = QComboBox(self.scrollAreaWidgetContents_2)
        self.comboBox_caseProbe_1.addItem("")
        self.comboBox_caseProbe_1.addItem("")
        self.comboBox_caseProbe_1.addItem("")
        self.comboBox_caseProbe_1.setObjectName(u"comboBox_caseProbe_1")
        self.comboBox_caseProbe_1.setMinimumSize(QSize(180, 35))
        self.comboBox_caseProbe_1.setFont(font1)

        self.horizontalLayout_121.addWidget(self.comboBox_caseProbe_1, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_8.addLayout(self.horizontalLayout_121)

        self.horizontalLayout_119 = QHBoxLayout()
        self.horizontalLayout_119.setObjectName(u"horizontalLayout_119")
        self.label_caseT_1 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_caseT_1.setObjectName(u"label_caseT_1")
        self.label_caseT_1.setFont(font1)

        self.horizontalLayout_119.addWidget(self.label_caseT_1, 0, Qt.AlignmentFlag.AlignRight)

        self.lineEdit_caseT_1 = QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_caseT_1.setObjectName(u"lineEdit_caseT_1")
        self.lineEdit_caseT_1.setMaximumSize(QSize(180, 16777215))
        self.lineEdit_caseT_1.setFont(font1)

        self.horizontalLayout_119.addWidget(self.lineEdit_caseT_1, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_8.addLayout(self.horizontalLayout_119)

        self.horizontalLayout_127 = QHBoxLayout()
        self.horizontalLayout_127.setObjectName(u"horizontalLayout_127")
        self.label_probeSensitivity_1 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_probeSensitivity_1.setObjectName(u"label_probeSensitivity_1")
        self.label_probeSensitivity_1.setFont(font1)

        self.horizontalLayout_127.addWidget(self.label_probeSensitivity_1, 0, Qt.AlignmentFlag.AlignRight)

        self.lineEdit_probeSensitivity_1 = QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_probeSensitivity_1.setObjectName(u"lineEdit_probeSensitivity_1")
        self.lineEdit_probeSensitivity_1.setMaximumSize(QSize(180, 16777215))
        self.lineEdit_probeSensitivity_1.setFont(font1)

        self.horizontalLayout_127.addWidget(self.lineEdit_probeSensitivity_1, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_8.addLayout(self.horizontalLayout_127)

        self.horizontalLayout_126 = QHBoxLayout()
        self.horizontalLayout_126.setObjectName(u"horizontalLayout_126")
        self.label_airSensitivityQuotient_1 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_airSensitivityQuotient_1.setObjectName(u"label_airSensitivityQuotient_1")
        self.label_airSensitivityQuotient_1.setFont(font1)

        self.horizontalLayout_126.addWidget(self.label_airSensitivityQuotient_1, 0, Qt.AlignmentFlag.AlignRight)

        self.lineEdit_airSensitivityQuotient_1 = QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_airSensitivityQuotient_1.setObjectName(u"lineEdit_airSensitivityQuotient_1")
        self.lineEdit_airSensitivityQuotient_1.setMaximumSize(QSize(180, 16777215))
        self.lineEdit_airSensitivityQuotient_1.setFont(font1)

        self.horizontalLayout_126.addWidget(self.lineEdit_airSensitivityQuotient_1, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_8.addLayout(self.horizontalLayout_126)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_10.addWidget(self.scrollArea_2)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_11 = QVBoxLayout(self.tab_2)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.scrollArea = QScrollArea(self.tab_2)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy1.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy1)
        font7 = QFont()
        font7.setFamilies([u"MS Shell Dlg 2"])
        font7.setPointSize(20)
        self.scrollArea.setFont(font7)
        self.scrollArea.setStyleSheet(u"QScrollBar:vertical {\n"
"        width: 30px;              /* set scrollbar width */\n"
"        }")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 708, 270))
        self.verticalLayout_7 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_147 = QHBoxLayout()
        self.horizontalLayout_147.setObjectName(u"horizontalLayout_147")
        self.label_axis_1 = QLabel(self.scrollAreaWidgetContents)
        self.label_axis_1.setObjectName(u"label_axis_1")
        sizePolicy1.setHeightForWidth(self.label_axis_1.sizePolicy().hasHeightForWidth())
        self.label_axis_1.setSizePolicy(sizePolicy1)
        self.label_axis_1.setFont(font1)

        self.horizontalLayout_147.addWidget(self.label_axis_1, 0, Qt.AlignmentFlag.AlignRight)

        self.comboBox_axis_1 = QComboBox(self.scrollAreaWidgetContents)
        self.comboBox_axis_1.addItem("")
        self.comboBox_axis_1.addItem("")
        self.comboBox_axis_1.addItem("")
        self.comboBox_axis_1.setObjectName(u"comboBox_axis_1")
        sizePolicy4.setHeightForWidth(self.comboBox_axis_1.sizePolicy().hasHeightForWidth())
        self.comboBox_axis_1.setSizePolicy(sizePolicy4)
        self.comboBox_axis_1.setMinimumSize(QSize(150, 35))
        self.comboBox_axis_1.setMaximumSize(QSize(16777215, 16777215))
        self.comboBox_axis_1.setFont(font1)

        self.horizontalLayout_147.addWidget(self.comboBox_axis_1, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_7.addLayout(self.horizontalLayout_147)

        self.horizontalLayout_146 = QHBoxLayout()
        self.horizontalLayout_146.setObjectName(u"horizontalLayout_146")
        self.label_offsetNo_1 = QLabel(self.scrollAreaWidgetContents)
        self.label_offsetNo_1.setObjectName(u"label_offsetNo_1")
        sizePolicy1.setHeightForWidth(self.label_offsetNo_1.sizePolicy().hasHeightForWidth())
        self.label_offsetNo_1.setSizePolicy(sizePolicy1)
        self.label_offsetNo_1.setFont(font1)

        self.horizontalLayout_146.addWidget(self.label_offsetNo_1, 0, Qt.AlignmentFlag.AlignRight)

        self.lineEdit_offsetNo_1 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_offsetNo_1.setObjectName(u"lineEdit_offsetNo_1")
        sizePolicy4.setHeightForWidth(self.lineEdit_offsetNo_1.sizePolicy().hasHeightForWidth())
        self.lineEdit_offsetNo_1.setSizePolicy(sizePolicy4)
        self.lineEdit_offsetNo_1.setMinimumSize(QSize(0, 35))
        self.lineEdit_offsetNo_1.setMaximumSize(QSize(150, 16777215))
        self.lineEdit_offsetNo_1.setFont(font1)

        self.horizontalLayout_146.addWidget(self.lineEdit_offsetNo_1, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_7.addLayout(self.horizontalLayout_146)

        self.horizontalLayout_144 = QHBoxLayout()
        self.horizontalLayout_144.setObjectName(u"horizontalLayout_144")
        self.label_machine_1 = QLabel(self.scrollAreaWidgetContents)
        self.label_machine_1.setObjectName(u"label_machine_1")
        sizePolicy1.setHeightForWidth(self.label_machine_1.sizePolicy().hasHeightForWidth())
        self.label_machine_1.setSizePolicy(sizePolicy1)
        self.label_machine_1.setFont(font1)

        self.horizontalLayout_144.addWidget(self.label_machine_1, 0, Qt.AlignmentFlag.AlignRight)

        self.comboBox_machine_1 = QComboBox(self.scrollAreaWidgetContents)
        self.comboBox_machine_1.setObjectName(u"comboBox_machine_1")
        sizePolicy4.setHeightForWidth(self.comboBox_machine_1.sizePolicy().hasHeightForWidth())
        self.comboBox_machine_1.setSizePolicy(sizePolicy4)
        self.comboBox_machine_1.setMinimumSize(QSize(150, 35))
        self.comboBox_machine_1.setMaximumSize(QSize(16777215, 16777215))
        self.comboBox_machine_1.setFont(font1)

        self.horizontalLayout_144.addWidget(self.comboBox_machine_1, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_7.addLayout(self.horizontalLayout_144)

        self.horizontalLayout_148 = QHBoxLayout()
        self.horizontalLayout_148.setObjectName(u"horizontalLayout_148")
        self.label_direction_1 = QLabel(self.scrollAreaWidgetContents)
        self.label_direction_1.setObjectName(u"label_direction_1")
        sizePolicy1.setHeightForWidth(self.label_direction_1.sizePolicy().hasHeightForWidth())
        self.label_direction_1.setSizePolicy(sizePolicy1)
        self.label_direction_1.setFont(font1)

        self.horizontalLayout_148.addWidget(self.label_direction_1, 0, Qt.AlignmentFlag.AlignRight)

        self.comboBox_direction_1 = QComboBox(self.scrollAreaWidgetContents)
        self.comboBox_direction_1.addItem("")
        self.comboBox_direction_1.addItem("")
        self.comboBox_direction_1.setObjectName(u"comboBox_direction_1")
        sizePolicy4.setHeightForWidth(self.comboBox_direction_1.sizePolicy().hasHeightForWidth())
        self.comboBox_direction_1.setSizePolicy(sizePolicy4)
        self.comboBox_direction_1.setMinimumSize(QSize(150, 35))
        self.comboBox_direction_1.setMaximumSize(QSize(16777215, 16777215))
        self.comboBox_direction_1.setFont(font1)

        self.horizontalLayout_148.addWidget(self.comboBox_direction_1, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_7.addLayout(self.horizontalLayout_148)

        self.horizontalLayout_125 = QHBoxLayout()
        self.horizontalLayout_125.setObjectName(u"horizontalLayout_125")
        self.label_turretNo_1 = QLabel(self.scrollAreaWidgetContents)
        self.label_turretNo_1.setObjectName(u"label_turretNo_1")
        self.label_turretNo_1.setFont(font1)

        self.horizontalLayout_125.addWidget(self.label_turretNo_1, 0, Qt.AlignmentFlag.AlignRight)

        self.lineEdit_turretNo_1 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_turretNo_1.setObjectName(u"lineEdit_turretNo_1")
        sizePolicy4.setHeightForWidth(self.lineEdit_turretNo_1.sizePolicy().hasHeightForWidth())
        self.lineEdit_turretNo_1.setSizePolicy(sizePolicy4)
        self.lineEdit_turretNo_1.setMaximumSize(QSize(150, 16777215))
        self.lineEdit_turretNo_1.setFont(font1)

        self.horizontalLayout_125.addWidget(self.lineEdit_turretNo_1, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_7.addLayout(self.horizontalLayout_125)

        self.horizontalLayout_156 = QHBoxLayout()
        self.horizontalLayout_156.setObjectName(u"horizontalLayout_156")
        self.label_bufferpartNo_1 = QLabel(self.scrollAreaWidgetContents)
        self.label_bufferpartNo_1.setObjectName(u"label_bufferpartNo_1")
        sizePolicy1.setHeightForWidth(self.label_bufferpartNo_1.sizePolicy().hasHeightForWidth())
        self.label_bufferpartNo_1.setSizePolicy(sizePolicy1)
        self.label_bufferpartNo_1.setFont(font1)

        self.horizontalLayout_156.addWidget(self.label_bufferpartNo_1, 0, Qt.AlignmentFlag.AlignRight)

        self.lineEdit_bufferPartNo_1 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_bufferPartNo_1.setObjectName(u"lineEdit_bufferPartNo_1")
        sizePolicy4.setHeightForWidth(self.lineEdit_bufferPartNo_1.sizePolicy().hasHeightForWidth())
        self.lineEdit_bufferPartNo_1.setSizePolicy(sizePolicy4)
        self.lineEdit_bufferPartNo_1.setMaximumSize(QSize(150, 16777215))
        self.lineEdit_bufferPartNo_1.setFont(font1)

        self.horizontalLayout_156.addWidget(self.lineEdit_bufferPartNo_1, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_7.addLayout(self.horizontalLayout_156)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_11.addWidget(self.scrollArea)

        self.tabWidget.addTab(self.tab_2, "")

        self.page18Layout.addWidget(self.tabWidget)

        self.stackedWidget_main.addWidget(self.page18)
        self.page19 = QWidget()
        self.page19.setObjectName(u"page19")
        self.page19Layout = QVBoxLayout(self.page19)
        self.page19Layout.setObjectName(u"page19Layout")
        self.horizontalLayout_85 = QHBoxLayout()
        self.horizontalLayout_85.setObjectName(u"horizontalLayout_85")
        self.horizontalSpacer_29 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_85.addItem(self.horizontalSpacer_29)

        self.label_fromDate = QLabel(self.page19)
        self.label_fromDate.setObjectName(u"label_fromDate")
        sizePolicy1.setHeightForWidth(self.label_fromDate.sizePolicy().hasHeightForWidth())
        self.label_fromDate.setSizePolicy(sizePolicy1)
        self.label_fromDate.setMaximumSize(QSize(16777215, 40))
        self.label_fromDate.setFont(font1)

        self.horizontalLayout_85.addWidget(self.label_fromDate)

        self.button_fromDate = QPushButton(self.page19)
        self.button_fromDate.setObjectName(u"button_fromDate")
        sizePolicy1.setHeightForWidth(self.button_fromDate.sizePolicy().hasHeightForWidth())
        self.button_fromDate.setSizePolicy(sizePolicy1)
        self.button_fromDate.setMinimumSize(QSize(130, 40))
        self.button_fromDate.setMaximumSize(QSize(16777215, 40))
        self.button_fromDate.setFont(font1)

        self.horizontalLayout_85.addWidget(self.button_fromDate)

        self.horizontalSpacer_32 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_85.addItem(self.horizontalSpacer_32)

        self.label_toDate = QLabel(self.page19)
        self.label_toDate.setObjectName(u"label_toDate")
        sizePolicy1.setHeightForWidth(self.label_toDate.sizePolicy().hasHeightForWidth())
        self.label_toDate.setSizePolicy(sizePolicy1)
        self.label_toDate.setMaximumSize(QSize(16777215, 40))
        self.label_toDate.setFont(font1)

        self.horizontalLayout_85.addWidget(self.label_toDate)

        self.button_toDate = QPushButton(self.page19)
        self.button_toDate.setObjectName(u"button_toDate")
        sizePolicy1.setHeightForWidth(self.button_toDate.sizePolicy().hasHeightForWidth())
        self.button_toDate.setSizePolicy(sizePolicy1)
        self.button_toDate.setMinimumSize(QSize(130, 40))
        self.button_toDate.setMaximumSize(QSize(16777215, 40))
        self.button_toDate.setFont(font1)

        self.horizontalLayout_85.addWidget(self.button_toDate)

        self.horizontalSpacer_31 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_85.addItem(self.horizontalSpacer_31)

        self.button_export = QPushButton(self.page19)
        self.button_export.setObjectName(u"button_export")
        sizePolicy1.setHeightForWidth(self.button_export.sizePolicy().hasHeightForWidth())
        self.button_export.setSizePolicy(sizePolicy1)
        self.button_export.setMinimumSize(QSize(0, 40))
        self.button_export.setMaximumSize(QSize(16777215, 40))
        self.button_export.setFont(font1)

        self.horizontalLayout_85.addWidget(self.button_export)

        self.horizontalSpacer_30 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_85.addItem(self.horizontalSpacer_30)


        self.page19Layout.addLayout(self.horizontalLayout_85)

        self.line_22 = QFrame(self.page19)
        self.line_22.setObjectName(u"line_22")
        self.line_22.setFrameShape(QFrame.Shape.HLine)
        self.line_22.setFrameShadow(QFrame.Shadow.Sunken)

        self.page19Layout.addWidget(self.line_22)

        self.horizontalLayout_86 = QHBoxLayout()
        self.horizontalLayout_86.setObjectName(u"horizontalLayout_86")
        self.horizontalSpacer_33 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_86.addItem(self.horizontalSpacer_33)

        self.label_22 = QLabel(self.page19)
        self.label_22.setObjectName(u"label_22")
        sizePolicy1.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy1)
        self.label_22.setMaximumSize(QSize(16777215, 40))
        self.label_22.setFont(font1)

        self.horizontalLayout_86.addWidget(self.label_22)

        self.lineEdit_spcDataCount = QLineEdit(self.page19)
        self.lineEdit_spcDataCount.setObjectName(u"lineEdit_spcDataCount")
        sizePolicy1.setHeightForWidth(self.lineEdit_spcDataCount.sizePolicy().hasHeightForWidth())
        self.lineEdit_spcDataCount.setSizePolicy(sizePolicy1)
        self.lineEdit_spcDataCount.setMinimumSize(QSize(0, 35))
        self.lineEdit_spcDataCount.setMaximumSize(QSize(75, 40))
        self.lineEdit_spcDataCount.setFont(font1)

        self.horizontalLayout_86.addWidget(self.lineEdit_spcDataCount, 0, Qt.AlignmentFlag.AlignLeft)

        self.horizontalSpacer_34 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_86.addItem(self.horizontalSpacer_34)

        self.button_spcDataCount = QPushButton(self.page19)
        self.button_spcDataCount.setObjectName(u"button_spcDataCount")
        sizePolicy1.setHeightForWidth(self.button_spcDataCount.sizePolicy().hasHeightForWidth())
        self.button_spcDataCount.setSizePolicy(sizePolicy1)
        self.button_spcDataCount.setMinimumSize(QSize(160, 40))
        self.button_spcDataCount.setMaximumSize(QSize(16777215, 40))
        self.button_spcDataCount.setFont(font1)

        self.horizontalLayout_86.addWidget(self.button_spcDataCount)

        self.horizontalSpacer_35 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

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
        sizePolicy1.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy1)
        self.label_25.setMinimumSize(QSize(0, 35))
        self.label_25.setFont(font1)

        self.horizontalLayout_87.addWidget(self.label_25, 0, Qt.AlignmentFlag.AlignRight)

        self.comboBox_probeCalibrate = QComboBox(self.page20)
        self.comboBox_probeCalibrate.addItem("")
        self.comboBox_probeCalibrate.addItem("")
        self.comboBox_probeCalibrate.addItem("")
        self.comboBox_probeCalibrate.addItem("")
        self.comboBox_probeCalibrate.addItem("")
        self.comboBox_probeCalibrate.addItem("")
        self.comboBox_probeCalibrate.addItem("")
        self.comboBox_probeCalibrate.addItem("")
        self.comboBox_probeCalibrate.setObjectName(u"comboBox_probeCalibrate")
        self.comboBox_probeCalibrate.setMinimumSize(QSize(90, 35))
        self.comboBox_probeCalibrate.setFont(font1)
        self.comboBox_probeCalibrate.setStyleSheet(u"")

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
        sizePolicy1.setHeightForWidth(self.label_lowerMasterCalibrate.sizePolicy().hasHeightForWidth())
        self.label_lowerMasterCalibrate.setSizePolicy(sizePolicy1)
        self.label_lowerMasterCalibrate.setMinimumSize(QSize(0, 35))
        self.label_lowerMasterCalibrate.setFont(font1)

        self.horizontalLayout_88.addWidget(self.label_lowerMasterCalibrate)

        self.lineEdit_lowerMasterCalibrate = QLineEdit(self.page20)
        self.lineEdit_lowerMasterCalibrate.setObjectName(u"lineEdit_lowerMasterCalibrate")
        sizePolicy1.setHeightForWidth(self.lineEdit_lowerMasterCalibrate.sizePolicy().hasHeightForWidth())
        self.lineEdit_lowerMasterCalibrate.setSizePolicy(sizePolicy1)
        self.lineEdit_lowerMasterCalibrate.setMinimumSize(QSize(0, 35))
        self.lineEdit_lowerMasterCalibrate.setFont(font1)
        self.lineEdit_lowerMasterCalibrate.setStyleSheet(u"")

        self.horizontalLayout_88.addWidget(self.lineEdit_lowerMasterCalibrate)

        self.horizontalSpacer_36 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_88.addItem(self.horizontalSpacer_36)

        self.label_higherMasterCalibrate = QLabel(self.page20)
        self.label_higherMasterCalibrate.setObjectName(u"label_higherMasterCalibrate")
        sizePolicy1.setHeightForWidth(self.label_higherMasterCalibrate.sizePolicy().hasHeightForWidth())
        self.label_higherMasterCalibrate.setSizePolicy(sizePolicy1)
        self.label_higherMasterCalibrate.setMinimumSize(QSize(0, 35))
        self.label_higherMasterCalibrate.setFont(font1)

        self.horizontalLayout_88.addWidget(self.label_higherMasterCalibrate)

        self.lineEdit_higherMasterCalibrate = QLineEdit(self.page20)
        self.lineEdit_higherMasterCalibrate.setObjectName(u"lineEdit_higherMasterCalibrate")
        sizePolicy1.setHeightForWidth(self.lineEdit_higherMasterCalibrate.sizePolicy().hasHeightForWidth())
        self.lineEdit_higherMasterCalibrate.setSizePolicy(sizePolicy1)
        self.lineEdit_higherMasterCalibrate.setMinimumSize(QSize(0, 35))
        self.lineEdit_higherMasterCalibrate.setFont(font1)
        self.lineEdit_higherMasterCalibrate.setStyleSheet(u"")

        self.horizontalLayout_88.addWidget(self.lineEdit_higherMasterCalibrate)

        self.horizontalSpacer_38 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_88.addItem(self.horizontalSpacer_38)


        self.page20Layout.addLayout(self.horizontalLayout_88)

        self.horizontalLayout_89 = QHBoxLayout()
        self.horizontalLayout_89.setObjectName(u"horizontalLayout_89")
        self.button_calibrateLower = QPushButton(self.page20)
        self.button_calibrateLower.setObjectName(u"button_calibrateLower")
        sizePolicy1.setHeightForWidth(self.button_calibrateLower.sizePolicy().hasHeightForWidth())
        self.button_calibrateLower.setSizePolicy(sizePolicy1)
        self.button_calibrateLower.setMinimumSize(QSize(0, 40))
        self.button_calibrateLower.setMaximumSize(QSize(180, 40))
        self.button_calibrateLower.setFont(font1)

        self.horizontalLayout_89.addWidget(self.button_calibrateLower)

        self.button_calibrateHigher = QPushButton(self.page20)
        self.button_calibrateHigher.setObjectName(u"button_calibrateHigher")
        sizePolicy1.setHeightForWidth(self.button_calibrateHigher.sizePolicy().hasHeightForWidth())
        self.button_calibrateHigher.setSizePolicy(sizePolicy1)
        self.button_calibrateHigher.setMinimumSize(QSize(0, 40))
        self.button_calibrateHigher.setMaximumSize(QSize(180, 40))
        self.button_calibrateHigher.setFont(font1)

        self.horizontalLayout_89.addWidget(self.button_calibrateHigher)


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
        sizePolicy1.setHeightForWidth(self.button_setToFactorySettingsCalibration.sizePolicy().hasHeightForWidth())
        self.button_setToFactorySettingsCalibration.setSizePolicy(sizePolicy1)
        self.button_setToFactorySettingsCalibration.setMinimumSize(QSize(200, 40))
        self.button_setToFactorySettingsCalibration.setMaximumSize(QSize(300, 40))
        self.button_setToFactorySettingsCalibration.setFont(font1)

        self.horizontalLayout_90.addWidget(self.button_setToFactorySettingsCalibration, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalSpacer_41 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_90.addItem(self.horizontalSpacer_41)

        self.button_resetToFactorySettingsCalibration = QPushButton(self.page20)
        self.button_resetToFactorySettingsCalibration.setObjectName(u"button_resetToFactorySettingsCalibration")
        sizePolicy1.setHeightForWidth(self.button_resetToFactorySettingsCalibration.sizePolicy().hasHeightForWidth())
        self.button_resetToFactorySettingsCalibration.setSizePolicy(sizePolicy1)
        self.button_resetToFactorySettingsCalibration.setMinimumSize(QSize(200, 40))
        self.button_resetToFactorySettingsCalibration.setMaximumSize(QSize(300, 40))
        self.button_resetToFactorySettingsCalibration.setFont(font1)

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
        sizePolicy1.setHeightForWidth(self.label_airSavingMode.sizePolicy().hasHeightForWidth())
        self.label_airSavingMode.setSizePolicy(sizePolicy1)
        self.label_airSavingMode.setFont(font1)

        self.horizontalLayout_91.addWidget(self.label_airSavingMode)

        self.toggleButton_airSavingMode = QLabel(self.page21)
        self.toggleButton_airSavingMode.setObjectName(u"toggleButton_airSavingMode")
        sizePolicy1.setHeightForWidth(self.toggleButton_airSavingMode.sizePolicy().hasHeightForWidth())
        self.toggleButton_airSavingMode.setSizePolicy(sizePolicy1)
        self.toggleButton_airSavingMode.setMinimumSize(QSize(60, 35))
        self.toggleButton_airSavingMode.setPixmap(QPixmap(u"../Images/Precigo/Switcher_On.png"))

        self.horizontalLayout_91.addWidget(self.toggleButton_airSavingMode)

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
        sizePolicy1.setHeightForWidth(self.label_airChannel.sizePolicy().hasHeightForWidth())
        self.label_airChannel.setSizePolicy(sizePolicy1)
        self.label_airChannel.setFont(font1)

        self.horizontalLayout_92.addWidget(self.label_airChannel, 0, Qt.AlignmentFlag.AlignRight)

        self.comboBox_airChannel = QComboBox(self.page21)
        self.comboBox_airChannel.addItem("")
        self.comboBox_airChannel.addItem("")
        self.comboBox_airChannel.setObjectName(u"comboBox_airChannel")
        self.comboBox_airChannel.setMinimumSize(QSize(90, 35))
        self.comboBox_airChannel.setFont(font1)

        self.horizontalLayout_92.addWidget(self.comboBox_airChannel, 0, Qt.AlignmentFlag.AlignLeft)


        self.page21Layout.addLayout(self.horizontalLayout_92)

        self.verticalSpacer_39 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.page21Layout.addItem(self.verticalSpacer_39)

        self.horizontalLayout_95 = QHBoxLayout()
        self.horizontalLayout_95.setObjectName(u"horizontalLayout_95")
        self.button_setAirSensitivity = QPushButton(self.page21)
        self.button_setAirSensitivity.setObjectName(u"button_setAirSensitivity")
        sizePolicy1.setHeightForWidth(self.button_setAirSensitivity.sizePolicy().hasHeightForWidth())
        self.button_setAirSensitivity.setSizePolicy(sizePolicy1)
        self.button_setAirSensitivity.setMinimumSize(QSize(90, 0))
        self.button_setAirSensitivity.setFont(font1)

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
        sizePolicy1.setHeightForWidth(self.label_ReportfromDate.sizePolicy().hasHeightForWidth())
        self.label_ReportfromDate.setSizePolicy(sizePolicy1)
        self.label_ReportfromDate.setMinimumSize(QSize(0, 35))
        self.label_ReportfromDate.setMaximumSize(QSize(16777215, 16777215))
        self.label_ReportfromDate.setFont(font1)

        self.horizontalLayout_101.addWidget(self.label_ReportfromDate)

        self.label_ReportfromDateVal = QLabel(self.page22)
        self.label_ReportfromDateVal.setObjectName(u"label_ReportfromDateVal")
        sizePolicy1.setHeightForWidth(self.label_ReportfromDateVal.sizePolicy().hasHeightForWidth())
        self.label_ReportfromDateVal.setSizePolicy(sizePolicy1)
        self.label_ReportfromDateVal.setMinimumSize(QSize(0, 35))
        self.label_ReportfromDateVal.setMaximumSize(QSize(16777215, 16777215))
        self.label_ReportfromDateVal.setFont(font1)

        self.horizontalLayout_101.addWidget(self.label_ReportfromDateVal, 0, Qt.AlignmentFlag.AlignRight)

        self.pushButton_selectFromDate = QPushButton(self.page22)
        self.pushButton_selectFromDate.setObjectName(u"pushButton_selectFromDate")
        sizePolicy1.setHeightForWidth(self.pushButton_selectFromDate.sizePolicy().hasHeightForWidth())
        self.pushButton_selectFromDate.setSizePolicy(sizePolicy1)
        self.pushButton_selectFromDate.setMinimumSize(QSize(140, 40))
        self.pushButton_selectFromDate.setMaximumSize(QSize(16777215, 40))
        self.pushButton_selectFromDate.setFont(font1)

        self.horizontalLayout_101.addWidget(self.pushButton_selectFromDate)

        self.horizontalSpacer_72 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_101.addItem(self.horizontalSpacer_72)

        self.label_ReportToDate = QLabel(self.page22)
        self.label_ReportToDate.setObjectName(u"label_ReportToDate")
        sizePolicy1.setHeightForWidth(self.label_ReportToDate.sizePolicy().hasHeightForWidth())
        self.label_ReportToDate.setSizePolicy(sizePolicy1)
        self.label_ReportToDate.setMinimumSize(QSize(0, 35))
        self.label_ReportToDate.setMaximumSize(QSize(16777215, 16777215))
        self.label_ReportToDate.setFont(font1)

        self.horizontalLayout_101.addWidget(self.label_ReportToDate)

        self.label_ReportToDateVal = QLabel(self.page22)
        self.label_ReportToDateVal.setObjectName(u"label_ReportToDateVal")
        sizePolicy1.setHeightForWidth(self.label_ReportToDateVal.sizePolicy().hasHeightForWidth())
        self.label_ReportToDateVal.setSizePolicy(sizePolicy1)
        self.label_ReportToDateVal.setMinimumSize(QSize(0, 35))
        self.label_ReportToDateVal.setMaximumSize(QSize(16777215, 16777215))
        self.label_ReportToDateVal.setFont(font1)

        self.horizontalLayout_101.addWidget(self.label_ReportToDateVal)

        self.pushButton_SelectToDate = QPushButton(self.page22)
        self.pushButton_SelectToDate.setObjectName(u"pushButton_SelectToDate")
        sizePolicy1.setHeightForWidth(self.pushButton_SelectToDate.sizePolicy().hasHeightForWidth())
        self.pushButton_SelectToDate.setSizePolicy(sizePolicy1)
        self.pushButton_SelectToDate.setMinimumSize(QSize(140, 40))
        self.pushButton_SelectToDate.setMaximumSize(QSize(16777215, 40))
        self.pushButton_SelectToDate.setFont(font1)

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
        sizePolicy1.setHeightForWidth(self.label_programId.sizePolicy().hasHeightForWidth())
        self.label_programId.setSizePolicy(sizePolicy1)
        self.label_programId.setMinimumSize(QSize(0, 35))
        self.label_programId.setFont(font1)

        self.horizontalLayout_104.addWidget(self.label_programId)

        self.comboBox_programId = QComboBox(self.page22)
        self.comboBox_programId.setObjectName(u"comboBox_programId")
        self.comboBox_programId.setMinimumSize(QSize(50, 35))
        self.comboBox_programId.setMaximumSize(QSize(90, 16777215))
        self.comboBox_programId.setFont(font1)

        self.horizontalLayout_104.addWidget(self.comboBox_programId)

        self.horizontalSpacer_75 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_104.addItem(self.horizontalSpacer_75)

        self.label_dimension = QLabel(self.page22)
        self.label_dimension.setObjectName(u"label_dimension")
        sizePolicy1.setHeightForWidth(self.label_dimension.sizePolicy().hasHeightForWidth())
        self.label_dimension.setSizePolicy(sizePolicy1)
        self.label_dimension.setMinimumSize(QSize(0, 35))
        self.label_dimension.setFont(font1)

        self.horizontalLayout_104.addWidget(self.label_dimension)

        self.comboBox_dimension = QComboBox(self.page22)
        self.comboBox_dimension.setObjectName(u"comboBox_dimension")
        self.comboBox_dimension.setMinimumSize(QSize(0, 35))
        self.comboBox_dimension.setMaximumSize(QSize(90, 16777215))
        self.comboBox_dimension.setFont(font1)

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
        sizePolicy1.setHeightForWidth(self.button_viewData.sizePolicy().hasHeightForWidth())
        self.button_viewData.setSizePolicy(sizePolicy1)
        self.button_viewData.setMinimumSize(QSize(100, 40))
        self.button_viewData.setMaximumSize(QSize(16777215, 40))
        self.button_viewData.setFont(font1)

        self.horizontalLayout_108.addWidget(self.button_viewData, 0, Qt.AlignmentFlag.AlignHCenter)

        self.button_exportData = QPushButton(self.page22)
        self.button_exportData.setObjectName(u"button_exportData")
        sizePolicy1.setHeightForWidth(self.button_exportData.sizePolicy().hasHeightForWidth())
        self.button_exportData.setSizePolicy(sizePolicy1)
        self.button_exportData.setMinimumSize(QSize(100, 40))
        self.button_exportData.setMaximumSize(QSize(16777215, 40))
        self.button_exportData.setFont(font1)

        self.horizontalLayout_108.addWidget(self.button_exportData, 0, Qt.AlignmentFlag.AlignHCenter)

        self.button_deleteData = QPushButton(self.page22)
        self.button_deleteData.setObjectName(u"button_deleteData")
        sizePolicy1.setHeightForWidth(self.button_deleteData.sizePolicy().hasHeightForWidth())
        self.button_deleteData.setSizePolicy(sizePolicy1)
        self.button_deleteData.setMinimumSize(QSize(100, 40))
        self.button_deleteData.setMaximumSize(QSize(16777215, 40))
        self.button_deleteData.setFont(font1)

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
        sizePolicy1.setHeightForWidth(self.label_dateselectReport.sizePolicy().hasHeightForWidth())
        self.label_dateselectReport.setSizePolicy(sizePolicy1)
        self.label_dateselectReport.setMinimumSize(QSize(0, 35))
        self.label_dateselectReport.setFont(font1)

        self.horizontalLayout_111.addWidget(self.label_dateselectReport)

        self.label_reportshowdate = QLabel(self.page23)
        self.label_reportshowdate.setObjectName(u"label_reportshowdate")
        sizePolicy1.setHeightForWidth(self.label_reportshowdate.sizePolicy().hasHeightForWidth())
        self.label_reportshowdate.setSizePolicy(sizePolicy1)
        self.label_reportshowdate.setMinimumSize(QSize(0, 35))
        self.label_reportshowdate.setFont(font1)

        self.horizontalLayout_111.addWidget(self.label_reportshowdate, 0, Qt.AlignmentFlag.AlignRight)

        self.horizontalSpacer_78 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_111.addItem(self.horizontalSpacer_78)

        self.label_programIdreport = QLabel(self.page23)
        self.label_programIdreport.setObjectName(u"label_programIdreport")
        sizePolicy1.setHeightForWidth(self.label_programIdreport.sizePolicy().hasHeightForWidth())
        self.label_programIdreport.setSizePolicy(sizePolicy1)
        self.label_programIdreport.setMinimumSize(QSize(0, 35))
        self.label_programIdreport.setFont(font1)

        self.horizontalLayout_111.addWidget(self.label_programIdreport)

        self.label_IdProgramReport = QLabel(self.page23)
        self.label_IdProgramReport.setObjectName(u"label_IdProgramReport")
        sizePolicy1.setHeightForWidth(self.label_IdProgramReport.sizePolicy().hasHeightForWidth())
        self.label_IdProgramReport.setSizePolicy(sizePolicy1)
        self.label_IdProgramReport.setMinimumSize(QSize(0, 35))
        self.label_IdProgramReport.setFont(font1)

        self.horizontalLayout_111.addWidget(self.label_IdProgramReport)

        self.horizontalSpacer_81 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_111.addItem(self.horizontalSpacer_81)

        self.label_DimensionForReport = QLabel(self.page23)
        self.label_DimensionForReport.setObjectName(u"label_DimensionForReport")
        sizePolicy1.setHeightForWidth(self.label_DimensionForReport.sizePolicy().hasHeightForWidth())
        self.label_DimensionForReport.setSizePolicy(sizePolicy1)
        self.label_DimensionForReport.setMinimumSize(QSize(0, 35))
        self.label_DimensionForReport.setFont(font1)

        self.horizontalLayout_111.addWidget(self.label_DimensionForReport)

        self.label_DimensionIdForReport = QLabel(self.page23)
        self.label_DimensionIdForReport.setObjectName(u"label_DimensionIdForReport")
        sizePolicy1.setHeightForWidth(self.label_DimensionIdForReport.sizePolicy().hasHeightForWidth())
        self.label_DimensionIdForReport.setSizePolicy(sizePolicy1)
        self.label_DimensionIdForReport.setMinimumSize(QSize(0, 35))
        self.label_DimensionIdForReport.setFont(font1)

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
        self.button_ListView.setMinimumSize(QSize(0, 30))
        self.button_ListView.setMaximumSize(QSize(160, 40))
        self.button_ListView.setFont(font1)

        self.horizontalLayout_113.addWidget(self.button_ListView)

        self.button_ChartView = QPushButton(self.page23)
        self.button_ChartView.setObjectName(u"button_ChartView")
        self.button_ChartView.setMinimumSize(QSize(0, 30))
        self.button_ChartView.setMaximumSize(QSize(160, 40))
        self.button_ChartView.setFont(font1)

        self.horizontalLayout_113.addWidget(self.button_ChartView)

        self.button_HistogramChart = QPushButton(self.page23)
        self.button_HistogramChart.setObjectName(u"button_HistogramChart")
        self.button_HistogramChart.setMinimumSize(QSize(0, 30))
        self.button_HistogramChart.setMaximumSize(QSize(160, 40))
        self.button_HistogramChart.setFont(font1)

        self.horizontalLayout_113.addWidget(self.button_HistogramChart)


        self.page23Layout.addLayout(self.horizontalLayout_113)

        self.stackedWidget_main.addWidget(self.page23)
        self.page24 = QWidget()
        self.page24.setObjectName(u"page24")
        self.page24.setStyleSheet(u"QPushButton {\n"
"    background-color: black;\n"
"	border: none;\n"
"}\n"
"")
        self.label_ioSettingPage = QPushButton(self.page24)
        self.label_ioSettingPage.setObjectName(u"label_ioSettingPage")
        self.label_ioSettingPage.setGeometry(QRect(430, 20, 102, 131))
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_ioSettingPage.sizePolicy().hasHeightForWidth())
        self.label_ioSettingPage.setSizePolicy(sizePolicy5)
        icon = QIcon()
        icon.addFile(u":/images/Buzzer.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.label_ioSettingPage.setIcon(icon)
        self.label_ioSettingPage.setIconSize(QSize(98, 130))
        self.label_ioSettingPage.setFlat(True)
        self.label_autoOffsetSettingPage = QPushButton(self.page24)
        self.label_autoOffsetSettingPage.setObjectName(u"label_autoOffsetSettingPage")
        self.label_autoOffsetSettingPage.setGeometry(QRect(620, 20, 102, 131))
        sizePolicy5.setHeightForWidth(self.label_autoOffsetSettingPage.sizePolicy().hasHeightForWidth())
        self.label_autoOffsetSettingPage.setSizePolicy(sizePolicy5)
        icon1 = QIcon()
        icon1.addFile(u"/home/torizon/app/src/images/offset-image-icon_2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.label_autoOffsetSettingPage.setIcon(icon1)
        self.label_autoOffsetSettingPage.setIconSize(QSize(110, 130))
        self.label_autoOffsetSettingPage.setFlat(True)
        self.label_dialIndicatorPage = QPushButton(self.page24)
        self.label_dialIndicatorPage.setObjectName(u"label_dialIndicatorPage")
        self.label_dialIndicatorPage.setGeometry(QRect(40, 20, 121, 131))
        sizePolicy5.setHeightForWidth(self.label_dialIndicatorPage.sizePolicy().hasHeightForWidth())
        self.label_dialIndicatorPage.setSizePolicy(sizePolicy5)
        self.label_dialIndicatorPage.setAutoFillBackground(False)
        self.label_dialIndicatorPage.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/images/indicator.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.label_dialIndicatorPage.setIcon(icon2)
        self.label_dialIndicatorPage.setIconSize(QSize(104, 126))
        self.label_dialIndicatorPage.setFlat(True)
        self.label_settingsPage = QPushButton(self.page24)
        self.label_settingsPage.setObjectName(u"label_settingsPage")
        self.label_settingsPage.setGeometry(QRect(230, 20, 109, 131))
        sizePolicy5.setHeightForWidth(self.label_settingsPage.sizePolicy().hasHeightForWidth())
        self.label_settingsPage.setSizePolicy(sizePolicy5)
        icon3 = QIcon()
        icon3.addFile(u":/images/settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.label_settingsPage.setIcon(icon3)
        self.label_settingsPage.setIconSize(QSize(98, 129))
        self.label_settingsPage.setFlat(True)
        self.label_reportPage = QPushButton(self.page24)
        self.label_reportPage.setObjectName(u"label_reportPage")
        self.label_reportPage.setGeometry(QRect(440, 220, 102, 131))
        sizePolicy5.setHeightForWidth(self.label_reportPage.sizePolicy().hasHeightForWidth())
        self.label_reportPage.setSizePolicy(sizePolicy5)
        icon4 = QIcon()
        icon4.addFile(u":/images/Report.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.label_reportPage.setIcon(icon4)
        self.label_reportPage.setIconSize(QSize(98, 129))
        self.label_reportPage.setFlat(True)
        self.label_clockSettingsPage = QPushButton(self.page24)
        self.label_clockSettingsPage.setObjectName(u"label_clockSettingsPage")
        self.label_clockSettingsPage.setGeometry(QRect(50, 220, 111, 131))
        sizePolicy5.setHeightForWidth(self.label_clockSettingsPage.sizePolicy().hasHeightForWidth())
        self.label_clockSettingsPage.setSizePolicy(sizePolicy5)
        icon5 = QIcon()
        icon5.addFile(u":/images/clock.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.label_clockSettingsPage.setIcon(icon5)
        self.label_clockSettingsPage.setIconSize(QSize(110, 130))
        self.label_clockSettingsPage.setFlat(True)
        self.label_userManagementPage = QPushButton(self.page24)
        self.label_userManagementPage.setObjectName(u"label_userManagementPage")
        self.label_userManagementPage.setGeometry(QRect(230, 220, 121, 131))
        sizePolicy5.setHeightForWidth(self.label_userManagementPage.sizePolicy().hasHeightForWidth())
        self.label_userManagementPage.setSizePolicy(sizePolicy5)
        icon6 = QIcon()
        icon6.addFile(u"/home/torizon/app/src/images/user-management_12.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.label_userManagementPage.setIcon(icon6)
        self.label_userManagementPage.setIconSize(QSize(137, 135))
        self.label_userManagementPage.setFlat(True)
        self.label_aboutLogoPage = QPushButton(self.page24)
        self.label_aboutLogoPage.setObjectName(u"label_aboutLogoPage")
        self.label_aboutLogoPage.setGeometry(QRect(600, 210, 141, 131))
        sizePolicy5.setHeightForWidth(self.label_aboutLogoPage.sizePolicy().hasHeightForWidth())
        self.label_aboutLogoPage.setSizePolicy(sizePolicy5)
        icon7 = QIcon()
        icon7.addFile(u"/home/torizon/app/src/images/help.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.label_aboutLogoPage.setIcon(icon7)
        self.label_aboutLogoPage.setIconSize(QSize(140, 85))
        self.label_aboutLogoPage.setFlat(True)
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
        self.comboBox.setMinimumSize(QSize(0, 35))
        self.comboBox.setMaximumSize(QSize(50, 16777215))
        self.comboBox.setFont(font1)

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
        self.pushButton_2.setFont(font1)

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
        self.widget_3 = QWidget(self.page26)
        self.widget_3.setObjectName(u"widget_3")
        self.label_value1 = QLabel(self.widget_3)
        self.label_value1.setObjectName(u"label_value1")
        self.label_value1.setGeometry(QRect(0, 130, 171, 41))
        self.label_value1.setMinimumSize(QSize(0, 37))
        self.label_value1.setStyleSheet(u"border: 1px solid #888888;\n"
"border-radius: 1px;")
        self.label_value1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.button_mode1 = QPushButton(self.widget_3)
        self.button_mode1.setObjectName(u"button_mode1")
        self.button_mode1.setGeometry(QRect(305, 130, 70, 41))
        self.label_value2 = QLabel(self.widget_3)
        self.label_value2.setObjectName(u"label_value2")
        self.label_value2.setGeometry(QRect(390, 130, 171, 41))
        self.label_value2.setMinimumSize(QSize(0, 37))
        self.label_value2.setStyleSheet(u"border: 1px solid #888888;\n"
"border-radius: 1px;")
        self.label_value2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_status2 = QLabel(self.widget_3)
        self.label_status2.setObjectName(u"label_status2")
        self.label_status2.setGeometry(QRect(570, 130, 111, 41))
        self.label_status2.setMinimumSize(QSize(0, 37))
        self.label_status2.setStyleSheet(u"border: 1px solid #888888;\n"
"border-radius: 1px;")
        self.label_status2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.button_mode2 = QPushButton(self.widget_3)
        self.button_mode2.setObjectName(u"button_mode2")
        self.button_mode2.setGeometry(QRect(690, 130, 70, 41))
        self.widget_spc3 = QWidget(self.widget_3)
        self.widget_spc3.setObjectName(u"widget_spc3")
        self.widget_spc3.setGeometry(QRect(10, 180, 371, 5))
        self.widget_spc4 = QWidget(self.widget_3)
        self.widget_spc4.setObjectName(u"widget_spc4")
        self.widget_spc4.setGeometry(QRect(390, 180, 371, 21))
        self.label_value3 = QLabel(self.widget_3)
        self.label_value3.setObjectName(u"label_value3")
        self.label_value3.setGeometry(QRect(0, 310, 171, 41))
        self.label_value3.setMinimumSize(QSize(0, 37))
        self.label_value3.setStyleSheet(u"border: 1px solid #888888;\n"
"border-radius: 1px;")
        self.label_value3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_value4 = QLabel(self.widget_3)
        self.label_value4.setObjectName(u"label_value4")
        self.label_value4.setGeometry(QRect(390, 310, 171, 41))
        self.label_value4.setMinimumSize(QSize(0, 37))
        self.label_value4.setStyleSheet(u"border: 1px solid #888888;\n"
"border-radius: 1px;")
        self.label_value4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.button_mode3 = QPushButton(self.widget_3)
        self.button_mode3.setObjectName(u"button_mode3")
        self.button_mode3.setGeometry(QRect(305, 310, 70, 41))
        self.label_dial1 = QLabel(self.widget_3)
        self.label_dial1.setObjectName(u"label_dial1")
        self.label_dial1.setGeometry(QRect(50, -1, 261, 130))
        self.label_dial1.setPixmap(QPixmap(u"Images/New yellow images/dial-img-yellow-260.png"))
        self.label_needle1 = QLabel(self.widget_3)
        self.label_needle1.setObjectName(u"label_needle1")
        self.label_needle1.setGeometry(QRect(164, 44, 28, 80))
        self.label_needle1.setPixmap(QPixmap(u"Images/needle_withdot_90.png"))
        self.label_needle1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_dial2 = QLabel(self.widget_3)
        self.label_dial2.setObjectName(u"label_dial2")
        self.label_dial2.setGeometry(QRect(460, -1, 261, 130))
        self.label_dial2.setPixmap(QPixmap(u"Images/New yellow images/dial-img-yellow-260.png"))
        self.label_needle2 = QLabel(self.widget_3)
        self.label_needle2.setObjectName(u"label_needle2")
        self.label_needle2.setGeometry(QRect(575, 44, 28, 80))
        self.label_needle2.setPixmap(QPixmap(u"Images/needle_withdot_90.png"))
        self.label_needle2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_dial3 = QLabel(self.widget_3)
        self.label_dial3.setObjectName(u"label_dial3")
        self.label_dial3.setGeometry(QRect(50, 180, 261, 130))
        self.label_dial3.setPixmap(QPixmap(u"Images/New yellow images/dial-img-yellow-260.png"))
        self.label_dial3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_needle3 = QLabel(self.widget_3)
        self.label_needle3.setObjectName(u"label_needle3")
        self.label_needle3.setGeometry(QRect(164, 229, 28, 80))
        self.label_needle3.setPixmap(QPixmap(u"Images/needle_withdot_90.png"))
        self.label_needle3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_dial4 = QLabel(self.widget_3)
        self.label_dial4.setObjectName(u"label_dial4")
        self.label_dial4.setGeometry(QRect(460, 180, 261, 130))
        self.label_dial4.setPixmap(QPixmap(u"Images/New yellow images/dial-img-yellow-260.png"))
        self.label_needle4 = QLabel(self.widget_3)
        self.label_needle4.setObjectName(u"label_needle4")
        self.label_needle4.setGeometry(QRect(575, 229, 28, 80))
        self.label_needle4.setPixmap(QPixmap(u"Images/needle_withdot_90.png"))
        self.label_needle4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.widget_spc1 = QWidget(self.widget_3)
        self.widget_spc1.setObjectName(u"widget_spc1")
        self.widget_spc1.setGeometry(QRect(10, 0, 371, 5))
        self.widget_spc2 = QWidget(self.widget_3)
        self.widget_spc2.setObjectName(u"widget_spc2")
        self.widget_spc2.setGeometry(QRect(360, 0, 371, 5))
        self.label_status1 = QLabel(self.widget_3)
        self.label_status1.setObjectName(u"label_status1")
        self.label_status1.setGeometry(QRect(180, 130, 111, 41))
        self.label_status1.setMinimumSize(QSize(0, 37))
        self.label_status1.setStyleSheet(u"border: 1px solid #888888;\n"
"border-radius: 1px;")
        self.label_status1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_status3 = QLabel(self.widget_3)
        self.label_status3.setObjectName(u"label_status3")
        self.label_status3.setGeometry(QRect(180, 310, 111, 41))
        self.label_status3.setMinimumSize(QSize(0, 37))
        self.label_status3.setStyleSheet(u"border: 1px solid #888888;\n"
"border-radius: 1px;")
        self.label_status3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_status4 = QLabel(self.widget_3)
        self.label_status4.setObjectName(u"label_status4")
        self.label_status4.setGeometry(QRect(570, 310, 111, 41))
        self.label_status4.setMinimumSize(QSize(0, 37))
        self.label_status4.setStyleSheet(u"border: 1px solid #888888;\n"
"border-radius: 1px;")
        self.label_status4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.button_mode4 = QPushButton(self.widget_3)
        self.button_mode4.setObjectName(u"button_mode4")
        self.button_mode4.setGeometry(QRect(690, 310, 70, 41))

        self.page26Layout.addWidget(self.widget_3)

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
        sizePolicy1.setHeightForWidth(self.button_angleCalculationSetting.sizePolicy().hasHeightForWidth())
        self.button_angleCalculationSetting.setSizePolicy(sizePolicy1)
        self.button_angleCalculationSetting.setMinimumSize(QSize(150, 40))
        self.button_angleCalculationSetting.setMaximumSize(QSize(16777215, 40))
        self.button_angleCalculationSetting.setFont(font1)

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
        sizePolicy1.setHeightForWidth(self.label_modeForCombineIndividual.sizePolicy().hasHeightForWidth())
        self.label_modeForCombineIndividual.setSizePolicy(sizePolicy1)
        self.label_modeForCombineIndividual.setMinimumSize(QSize(0, 35))
        self.label_modeForCombineIndividual.setFont(font1)

        self.horizontalLayout_152.addWidget(self.label_modeForCombineIndividual)

        self.radioButton_modeCombine = QRadioButton(self.page27)
        self.buttonGroup_4 = QButtonGroup(MainWindow)
        self.buttonGroup_4.setObjectName(u"buttonGroup_4")
        self.buttonGroup_4.addButton(self.radioButton_modeCombine)
        self.radioButton_modeCombine.setObjectName(u"radioButton_modeCombine")
        sizePolicy1.setHeightForWidth(self.radioButton_modeCombine.sizePolicy().hasHeightForWidth())
        self.radioButton_modeCombine.setSizePolicy(sizePolicy1)
        self.radioButton_modeCombine.setMinimumSize(QSize(0, 30))
        self.radioButton_modeCombine.setFont(font1)

        self.horizontalLayout_152.addWidget(self.radioButton_modeCombine)

        self.radioButton_modeIndividual = QRadioButton(self.page27)
        self.buttonGroup_4.addButton(self.radioButton_modeIndividual)
        self.radioButton_modeIndividual.setObjectName(u"radioButton_modeIndividual")
        sizePolicy1.setHeightForWidth(self.radioButton_modeIndividual.sizePolicy().hasHeightForWidth())
        self.radioButton_modeIndividual.setSizePolicy(sizePolicy1)
        self.radioButton_modeIndividual.setMinimumSize(QSize(0, 30))
        self.radioButton_modeIndividual.setFont(font1)

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

        self.label_unitOfMeasurement = QLabel(self.page27)
        self.label_unitOfMeasurement.setObjectName(u"label_unitOfMeasurement")
        sizePolicy1.setHeightForWidth(self.label_unitOfMeasurement.sizePolicy().hasHeightForWidth())
        self.label_unitOfMeasurement.setSizePolicy(sizePolicy1)
        self.label_unitOfMeasurement.setMinimumSize(QSize(0, 35))
        self.label_unitOfMeasurement.setFont(font1)

        self.horizontalLayout_115.addWidget(self.label_unitOfMeasurement)

        self.radioButton_inch = QRadioButton(self.page27)
        self.buttonGroup_3 = QButtonGroup(MainWindow)
        self.buttonGroup_3.setObjectName(u"buttonGroup_3")
        self.buttonGroup_3.addButton(self.radioButton_inch)
        self.radioButton_inch.setObjectName(u"radioButton_inch")
        sizePolicy1.setHeightForWidth(self.radioButton_inch.sizePolicy().hasHeightForWidth())
        self.radioButton_inch.setSizePolicy(sizePolicy1)
        self.radioButton_inch.setMinimumSize(QSize(0, 30))
        self.radioButton_inch.setFont(font1)

        self.horizontalLayout_115.addWidget(self.radioButton_inch)

        self.radioButton_mm = QRadioButton(self.page27)
        self.buttonGroup_3.addButton(self.radioButton_mm)
        self.radioButton_mm.setObjectName(u"radioButton_mm")
        sizePolicy1.setHeightForWidth(self.radioButton_mm.sizePolicy().hasHeightForWidth())
        self.radioButton_mm.setSizePolicy(sizePolicy1)
        self.radioButton_mm.setMinimumSize(QSize(0, 30))
        self.radioButton_mm.setFont(font1)

        self.horizontalLayout_115.addWidget(self.radioButton_mm)

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
        sizePolicy1.setHeightForWidth(self.label_DurationForAutosave.sizePolicy().hasHeightForWidth())
        self.label_DurationForAutosave.setSizePolicy(sizePolicy1)
        self.label_DurationForAutosave.setMinimumSize(QSize(0, 35))
        self.label_DurationForAutosave.setFont(font1)

        self.horizontalLayout_140.addWidget(self.label_DurationForAutosave)

        self.lineEdit_DurationAutosave = QLineEdit(self.page27)
        self.lineEdit_DurationAutosave.setObjectName(u"lineEdit_DurationAutosave")
        sizePolicy1.setHeightForWidth(self.lineEdit_DurationAutosave.sizePolicy().hasHeightForWidth())
        self.lineEdit_DurationAutosave.setSizePolicy(sizePolicy1)
        self.lineEdit_DurationAutosave.setMinimumSize(QSize(0, 35))
        self.lineEdit_DurationAutosave.setMaximumSize(QSize(70, 16777215))
        self.lineEdit_DurationAutosave.setFont(font1)

        self.horizontalLayout_140.addWidget(self.lineEdit_DurationAutosave, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalSpacer_134 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_140.addItem(self.horizontalSpacer_134)


        self.page27Layout.addLayout(self.horizontalLayout_140)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.page27Layout.addItem(self.verticalSpacer_11)

        self.horizontalLayout_72 = QHBoxLayout()
        self.horizontalLayout_72.setObjectName(u"horizontalLayout_72")
        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_72.addItem(self.horizontalSpacer_20)

        self.label_Responsiveness = QLabel(self.page27)
        self.label_Responsiveness.setObjectName(u"label_Responsiveness")

        self.horizontalLayout_72.addWidget(self.label_Responsiveness)

        self.lineEdit_Responsiveness = QLineEdit(self.page27)
        self.lineEdit_Responsiveness.setObjectName(u"lineEdit_Responsiveness")
        self.lineEdit_Responsiveness.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_72.addWidget(self.lineEdit_Responsiveness, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalSpacer_82 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_72.addItem(self.horizontalSpacer_82)


        self.page27Layout.addLayout(self.horizontalLayout_72)

        self.verticalSpacer_43 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.page27Layout.addItem(self.verticalSpacer_43)

        self.horizontalLayout_133 = QHBoxLayout()
        self.horizontalLayout_133.setObjectName(u"horizontalLayout_133")
        self.horizontalSpacer_138 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_133.addItem(self.horizontalSpacer_138)

        self.pushButton_autosenseRange = QPushButton(self.page27)
        self.pushButton_autosenseRange.setObjectName(u"pushButton_autosenseRange")
        sizePolicy1.setHeightForWidth(self.pushButton_autosenseRange.sizePolicy().hasHeightForWidth())
        self.pushButton_autosenseRange.setSizePolicy(sizePolicy1)
        self.pushButton_autosenseRange.setMinimumSize(QSize(150, 40))
        self.pushButton_autosenseRange.setMaximumSize(QSize(16777215, 40))
        self.pushButton_autosenseRange.setFont(font1)

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
        sizePolicy1.setHeightForWidth(self.label_angleCalculation.sizePolicy().hasHeightForWidth())
        self.label_angleCalculation.setSizePolicy(sizePolicy1)
        self.label_angleCalculation.setFont(font1)

        self.horizontalLayout_137.addWidget(self.label_angleCalculation)

        self.toggelButton_angleCalculation = QLabel(self.page28)
        self.toggelButton_angleCalculation.setObjectName(u"toggelButton_angleCalculation")
        sizePolicy1.setHeightForWidth(self.toggelButton_angleCalculation.sizePolicy().hasHeightForWidth())
        self.toggelButton_angleCalculation.setSizePolicy(sizePolicy1)
        self.toggelButton_angleCalculation.setMinimumSize(QSize(60, 35))
        self.toggelButton_angleCalculation.setFont(font1)
        self.toggelButton_angleCalculation.setPixmap(QPixmap(u"../Images/Precigo/Switcher_On.png"))

        self.horizontalLayout_137.addWidget(self.toggelButton_angleCalculation)

        self.horizontalSpacer_144 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_137.addItem(self.horizontalSpacer_144)


        self.page28Layout.addLayout(self.horizontalLayout_137)

        self.horizontalLayout_138 = QHBoxLayout()
        self.horizontalLayout_138.setObjectName(u"horizontalLayout_138")
        self.horizontalSpacer_145 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_138.addItem(self.horizontalSpacer_145)

        self.label_angleCalculationMasterAngle = QLabel(self.page28)
        self.label_angleCalculationMasterAngle.setObjectName(u"label_angleCalculationMasterAngle")
        sizePolicy1.setHeightForWidth(self.label_angleCalculationMasterAngle.sizePolicy().hasHeightForWidth())
        self.label_angleCalculationMasterAngle.setSizePolicy(sizePolicy1)
        self.label_angleCalculationMasterAngle.setMinimumSize(QSize(0, 35))
        self.label_angleCalculationMasterAngle.setFont(font1)

        self.horizontalLayout_138.addWidget(self.label_angleCalculationMasterAngle)

        self.lineEdit_angleDegree = QLineEdit(self.page28)
        self.lineEdit_angleDegree.setObjectName(u"lineEdit_angleDegree")
        sizePolicy1.setHeightForWidth(self.lineEdit_angleDegree.sizePolicy().hasHeightForWidth())
        self.lineEdit_angleDegree.setSizePolicy(sizePolicy1)
        self.lineEdit_angleDegree.setMinimumSize(QSize(0, 35))
        self.lineEdit_angleDegree.setMaximumSize(QSize(65, 16777215))
        self.lineEdit_angleDegree.setFont(font1)

        self.horizontalLayout_138.addWidget(self.lineEdit_angleDegree, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_angleDegree = QLabel(self.page28)
        self.label_angleDegree.setObjectName(u"label_angleDegree")
        self.label_angleDegree.setMaximumSize(QSize(16777215, 50))
        self.label_angleDegree.setFont(font1)
        self.label_angleDegree.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.horizontalLayout_138.addWidget(self.label_angleDegree)

        self.lineEdit_angleMinutes = QLineEdit(self.page28)
        self.lineEdit_angleMinutes.setObjectName(u"lineEdit_angleMinutes")
        sizePolicy1.setHeightForWidth(self.lineEdit_angleMinutes.sizePolicy().hasHeightForWidth())
        self.lineEdit_angleMinutes.setSizePolicy(sizePolicy1)
        self.lineEdit_angleMinutes.setMaximumSize(QSize(65, 16777215))
        self.lineEdit_angleMinutes.setFont(font1)

        self.horizontalLayout_138.addWidget(self.lineEdit_angleMinutes, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_angleMin = QLabel(self.page28)
        self.label_angleMin.setObjectName(u"label_angleMin")
        self.label_angleMin.setMaximumSize(QSize(16777215, 50))
        self.label_angleMin.setFont(font1)
        self.label_angleMin.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.horizontalLayout_138.addWidget(self.label_angleMin)

        self.lineEdit_angleSeconds = QLineEdit(self.page28)
        self.lineEdit_angleSeconds.setObjectName(u"lineEdit_angleSeconds")
        sizePolicy1.setHeightForWidth(self.lineEdit_angleSeconds.sizePolicy().hasHeightForWidth())
        self.lineEdit_angleSeconds.setSizePolicy(sizePolicy1)
        self.lineEdit_angleSeconds.setMaximumSize(QSize(65, 16777215))
        self.lineEdit_angleSeconds.setFont(font1)

        self.horizontalLayout_138.addWidget(self.lineEdit_angleSeconds, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_angleSec = QLabel(self.page28)
        self.label_angleSec.setObjectName(u"label_angleSec")
        self.label_angleSec.setMaximumSize(QSize(16777215, 50))
        self.label_angleSec.setFont(font1)
        self.label_angleSec.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.horizontalLayout_138.addWidget(self.label_angleSec)

        self.horizontalSpacer_147 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_138.addItem(self.horizontalSpacer_147)


        self.page28Layout.addLayout(self.horizontalLayout_138)

        self.horizontalLayout_141 = QHBoxLayout()
        self.horizontalLayout_141.setObjectName(u"horizontalLayout_141")
        self.horizontalSpacer_150 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_141.addItem(self.horizontalSpacer_150)

        self.label_positiveTol = QLabel(self.page28)
        self.label_positiveTol.setObjectName(u"label_positiveTol")
        sizePolicy1.setHeightForWidth(self.label_positiveTol.sizePolicy().hasHeightForWidth())
        self.label_positiveTol.setSizePolicy(sizePolicy1)
        self.label_positiveTol.setFont(font1)

        self.horizontalLayout_141.addWidget(self.label_positiveTol)

        self.lineEdit_toleranceMin = QLineEdit(self.page28)
        self.lineEdit_toleranceMin.setObjectName(u"lineEdit_toleranceMin")
        sizePolicy1.setHeightForWidth(self.lineEdit_toleranceMin.sizePolicy().hasHeightForWidth())
        self.lineEdit_toleranceMin.setSizePolicy(sizePolicy1)
        self.lineEdit_toleranceMin.setMinimumSize(QSize(0, 35))
        self.lineEdit_toleranceMin.setMaximumSize(QSize(100, 16777215))
        self.lineEdit_toleranceMin.setFont(font1)

        self.horizontalLayout_141.addWidget(self.lineEdit_toleranceMin)

        self.label_tolMin = QLabel(self.page28)
        self.label_tolMin.setObjectName(u"label_tolMin")
        self.label_tolMin.setMinimumSize(QSize(10, 35))
        self.label_tolMin.setMaximumSize(QSize(16777215, 50))
        self.label_tolMin.setSizeIncrement(QSize(0, 0))
        self.label_tolMin.setFont(font1)
        self.label_tolMin.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.horizontalLayout_141.addWidget(self.label_tolMin)

        self.lineEdit_toleranceSec = QLineEdit(self.page28)
        self.lineEdit_toleranceSec.setObjectName(u"lineEdit_toleranceSec")
        sizePolicy1.setHeightForWidth(self.lineEdit_toleranceSec.sizePolicy().hasHeightForWidth())
        self.lineEdit_toleranceSec.setSizePolicy(sizePolicy1)
        self.lineEdit_toleranceSec.setMinimumSize(QSize(0, 35))
        self.lineEdit_toleranceSec.setMaximumSize(QSize(100, 16777215))
        self.lineEdit_toleranceSec.setFont(font1)

        self.horizontalLayout_141.addWidget(self.lineEdit_toleranceSec)

        self.label_tolSec = QLabel(self.page28)
        self.label_tolSec.setObjectName(u"label_tolSec")
        self.label_tolSec.setMinimumSize(QSize(10, 35))
        self.label_tolSec.setMaximumSize(QSize(16777215, 50))
        self.label_tolSec.setFont(font1)
        self.label_tolSec.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.horizontalLayout_141.addWidget(self.label_tolSec)

        self.horizontalSpacer_151 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_141.addItem(self.horizontalSpacer_151)


        self.page28Layout.addLayout(self.horizontalLayout_141)

        self.horizontalLayout_142 = QHBoxLayout()
        self.horizontalLayout_142.setObjectName(u"horizontalLayout_142")
        self.horizontalSpacer_153 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_142.addItem(self.horizontalSpacer_153)

        self.label_negativeTol = QLabel(self.page28)
        self.label_negativeTol.setObjectName(u"label_negativeTol")
        sizePolicy1.setHeightForWidth(self.label_negativeTol.sizePolicy().hasHeightForWidth())
        self.label_negativeTol.setSizePolicy(sizePolicy1)
        self.label_negativeTol.setFont(font1)

        self.horizontalLayout_142.addWidget(self.label_negativeTol)

        self.lineEdit_negativeTolMin = QLineEdit(self.page28)
        self.lineEdit_negativeTolMin.setObjectName(u"lineEdit_negativeTolMin")
        sizePolicy1.setHeightForWidth(self.lineEdit_negativeTolMin.sizePolicy().hasHeightForWidth())
        self.lineEdit_negativeTolMin.setSizePolicy(sizePolicy1)
        self.lineEdit_negativeTolMin.setMaximumSize(QSize(100, 16777215))
        self.lineEdit_negativeTolMin.setFont(font1)

        self.horizontalLayout_142.addWidget(self.lineEdit_negativeTolMin)

        self.label_tolPositiveMin = QLabel(self.page28)
        self.label_tolPositiveMin.setObjectName(u"label_tolPositiveMin")
        self.label_tolPositiveMin.setMinimumSize(QSize(10, 35))
        self.label_tolPositiveMin.setMaximumSize(QSize(16777215, 50))
        self.label_tolPositiveMin.setFont(font1)
        self.label_tolPositiveMin.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.horizontalLayout_142.addWidget(self.label_tolPositiveMin)

        self.lineEdit_negativeTolSec = QLineEdit(self.page28)
        self.lineEdit_negativeTolSec.setObjectName(u"lineEdit_negativeTolSec")
        sizePolicy1.setHeightForWidth(self.lineEdit_negativeTolSec.sizePolicy().hasHeightForWidth())
        self.lineEdit_negativeTolSec.setSizePolicy(sizePolicy1)
        self.lineEdit_negativeTolSec.setMaximumSize(QSize(100, 16777215))
        self.lineEdit_negativeTolSec.setFont(font1)

        self.horizontalLayout_142.addWidget(self.lineEdit_negativeTolSec)

        self.label_tolPositiveSec = QLabel(self.page28)
        self.label_tolPositiveSec.setObjectName(u"label_tolPositiveSec")
        self.label_tolPositiveSec.setMinimumSize(QSize(10, 35))
        self.label_tolPositiveSec.setMaximumSize(QSize(16777215, 50))
        self.label_tolPositiveSec.setFont(font1)
        self.label_tolPositiveSec.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.horizontalLayout_142.addWidget(self.label_tolPositiveSec)

        self.horizontalSpacer_154 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_142.addItem(self.horizontalSpacer_154)


        self.page28Layout.addLayout(self.horizontalLayout_142)

        self.horizontalLayout_143 = QHBoxLayout()
        self.horizontalLayout_143.setObjectName(u"horizontalLayout_143")
        self.horizontalSpacer_155 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_143.addItem(self.horizontalSpacer_155)

        self.label_Distance = QLabel(self.page28)
        self.label_Distance.setObjectName(u"label_Distance")
        sizePolicy1.setHeightForWidth(self.label_Distance.sizePolicy().hasHeightForWidth())
        self.label_Distance.setSizePolicy(sizePolicy1)
        self.label_Distance.setFont(font1)

        self.horizontalLayout_143.addWidget(self.label_Distance)

        self.lineEdit_distanceMm = QLineEdit(self.page28)
        self.lineEdit_distanceMm.setObjectName(u"lineEdit_distanceMm")
        sizePolicy1.setHeightForWidth(self.lineEdit_distanceMm.sizePolicy().hasHeightForWidth())
        self.lineEdit_distanceMm.setSizePolicy(sizePolicy1)
        self.lineEdit_distanceMm.setMinimumSize(QSize(170, 35))
        self.lineEdit_distanceMm.setMaximumSize(QSize(160, 16777215))
        self.lineEdit_distanceMm.setFont(font1)

        self.horizontalLayout_143.addWidget(self.lineEdit_distanceMm, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_distanceInMm = QLabel(self.page28)
        self.label_distanceInMm.setObjectName(u"label_distanceInMm")
        sizePolicy1.setHeightForWidth(self.label_distanceInMm.sizePolicy().hasHeightForWidth())
        self.label_distanceInMm.setSizePolicy(sizePolicy1)
        self.label_distanceInMm.setMinimumSize(QSize(40, 35))
        self.label_distanceInMm.setMaximumSize(QSize(60, 16777215))
        self.label_distanceInMm.setFont(font1)

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
        sizePolicy1.setHeightForWidth(self.label_Angle.sizePolicy().hasHeightForWidth())
        self.label_Angle.setSizePolicy(sizePolicy1)
        self.label_Angle.setFont(font1)

        self.horizontalLayout_145.addWidget(self.label_Angle)

        self.radioButton_halfAngle = QRadioButton(self.page28)
        self.radioButton_halfAngle.setObjectName(u"radioButton_halfAngle")
        sizePolicy1.setHeightForWidth(self.radioButton_halfAngle.sizePolicy().hasHeightForWidth())
        self.radioButton_halfAngle.setSizePolicy(sizePolicy1)
        self.radioButton_halfAngle.setFont(font1)

        self.horizontalLayout_145.addWidget(self.radioButton_halfAngle)

        self.radioButton_2_fullAngle = QRadioButton(self.page28)
        self.radioButton_2_fullAngle.setObjectName(u"radioButton_2_fullAngle")
        sizePolicy1.setHeightForWidth(self.radioButton_2_fullAngle.sizePolicy().hasHeightForWidth())
        self.radioButton_2_fullAngle.setSizePolicy(sizePolicy1)
        self.radioButton_2_fullAngle.setFont(font1)

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
        self.horizontalLayout_162.setSpacing(0)
        self.horizontalLayout_162.setObjectName(u"horizontalLayout_162")
        self.horizontalLayout_162.setContentsMargins(-1, 0, -1, 0)
        self.label_programIdOnSetMaster = QLabel(self.page29)
        self.label_programIdOnSetMaster.setObjectName(u"label_programIdOnSetMaster")
        sizePolicy5.setHeightForWidth(self.label_programIdOnSetMaster.sizePolicy().hasHeightForWidth())
        self.label_programIdOnSetMaster.setSizePolicy(sizePolicy5)
        self.label_programIdOnSetMaster.setMinimumSize(QSize(110, 35))
        self.label_programIdOnSetMaster.setMaximumSize(QSize(150, 16777215))
        self.label_programIdOnSetMaster.setFont(font1)

        self.horizontalLayout_162.addWidget(self.label_programIdOnSetMaster)

        self.comboBox_programIdSetting_outer = QComboBox(self.page29)
        self.comboBox_programIdSetting_outer.addItem("")
        self.comboBox_programIdSetting_outer.addItem("")
        self.comboBox_programIdSetting_outer.addItem("")
        self.comboBox_programIdSetting_outer.addItem("")
        self.comboBox_programIdSetting_outer.setObjectName(u"comboBox_programIdSetting_outer")
        sizePolicy5.setHeightForWidth(self.comboBox_programIdSetting_outer.sizePolicy().hasHeightForWidth())
        self.comboBox_programIdSetting_outer.setSizePolicy(sizePolicy5)
        self.comboBox_programIdSetting_outer.setMinimumSize(QSize(80, 35))
        self.comboBox_programIdSetting_outer.setMaximumSize(QSize(80, 35))
        self.comboBox_programIdSetting_outer.setFont(font1)

        self.horizontalLayout_162.addWidget(self.comboBox_programIdSetting_outer)

        self.horizontalSpacer_83 = QSpacerItem(40, 35, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_162.addItem(self.horizontalSpacer_83)

        self.label_programNamOnSetMAster = QLabel(self.page29)
        self.label_programNamOnSetMAster.setObjectName(u"label_programNamOnSetMAster")
        sizePolicy5.setHeightForWidth(self.label_programNamOnSetMAster.sizePolicy().hasHeightForWidth())
        self.label_programNamOnSetMAster.setSizePolicy(sizePolicy5)
        self.label_programNamOnSetMAster.setMinimumSize(QSize(140, 35))
        self.label_programNamOnSetMAster.setMaximumSize(QSize(150, 16777215))
        self.label_programNamOnSetMAster.setFont(font1)

        self.horizontalLayout_162.addWidget(self.label_programNamOnSetMAster)

        self.label_programName = QLabel(self.page29)
        self.label_programName.setObjectName(u"label_programName")
        sizePolicy5.setHeightForWidth(self.label_programName.sizePolicy().hasHeightForWidth())
        self.label_programName.setSizePolicy(sizePolicy5)
        self.label_programName.setMinimumSize(QSize(400, 35))
        self.label_programName.setMaximumSize(QSize(400, 16777215))
        self.label_programName.setFont(font1)

        self.horizontalLayout_162.addWidget(self.label_programName, 0, Qt.AlignmentFlag.AlignLeft)


        self.page29Layout.addLayout(self.horizontalLayout_162)

        self.line_81 = QFrame(self.page29)
        self.line_81.setObjectName(u"line_81")
        self.line_81.setMinimumSize(QSize(0, 0))
        self.line_81.setMaximumSize(QSize(16777215, 16777215))
        self.line_81.setFont(font3)
        self.line_81.setFrameShape(QFrame.Shape.HLine)
        self.line_81.setFrameShadow(QFrame.Shadow.Sunken)

        self.page29Layout.addWidget(self.line_81)

        self.horizontalLayout_164 = QHBoxLayout()
        self.horizontalLayout_164.setSpacing(0)
        self.horizontalLayout_164.setObjectName(u"horizontalLayout_164")
        self.label_masterSetting = QLabel(self.page29)
        self.label_masterSetting.setObjectName(u"label_masterSetting")
        sizePolicy5.setHeightForWidth(self.label_masterSetting.sizePolicy().hasHeightForWidth())
        self.label_masterSetting.setSizePolicy(sizePolicy5)
        self.label_masterSetting.setMinimumSize(QSize(130, 35))
        self.label_masterSetting.setMaximumSize(QSize(140, 16777215))
        self.label_masterSetting.setFont(font1)

        self.horizontalLayout_164.addWidget(self.label_masterSetting)

        self.button_setMaster = QPushButton(self.page29)
        self.button_setMaster.setObjectName(u"button_setMaster")
        sizePolicy5.setHeightForWidth(self.button_setMaster.sizePolicy().hasHeightForWidth())
        self.button_setMaster.setSizePolicy(sizePolicy5)
        self.button_setMaster.setMinimumSize(QSize(120, 45))
        self.button_setMaster.setMaximumSize(QSize(16777215, 40))
        self.button_setMaster.setFont(font1)

        self.horizontalLayout_164.addWidget(self.button_setMaster)

        self.horizontalSpacer_98 = QSpacerItem(50, 45, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_164.addItem(self.horizontalSpacer_98)

        self.button_programList = QPushButton(self.page29)
        self.button_programList.setObjectName(u"button_programList")
        sizePolicy2.setHeightForWidth(self.button_programList.sizePolicy().hasHeightForWidth())
        self.button_programList.setSizePolicy(sizePolicy2)
        self.button_programList.setMinimumSize(QSize(110, 45))
        self.button_programList.setMaximumSize(QSize(16777215, 40))
        self.button_programList.setFont(font1)

        self.horizontalLayout_164.addWidget(self.button_programList)

        self.horizontalSpacer_148 = QSpacerItem(50, 45, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_164.addItem(self.horizontalSpacer_148)

        self.button_partSettings = QPushButton(self.page29)
        self.button_partSettings.setObjectName(u"button_partSettings")
        sizePolicy2.setHeightForWidth(self.button_partSettings.sizePolicy().hasHeightForWidth())
        self.button_partSettings.setSizePolicy(sizePolicy2)
        self.button_partSettings.setMinimumSize(QSize(110, 45))
        self.button_partSettings.setMaximumSize(QSize(16777215, 40))
        self.button_partSettings.setFont(font1)

        self.horizontalLayout_164.addWidget(self.button_partSettings)

        self.horizontalSpacer_142 = QSpacerItem(30, 45, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_164.addItem(self.horizontalSpacer_142)


        self.page29Layout.addLayout(self.horizontalLayout_164)

        self.line_83 = QFrame(self.page29)
        self.line_83.setObjectName(u"line_83")
        sizePolicy2.setHeightForWidth(self.line_83.sizePolicy().hasHeightForWidth())
        self.line_83.setSizePolicy(sizePolicy2)
        self.line_83.setMinimumSize(QSize(0, 1))
        self.line_83.setMaximumSize(QSize(16777215, 16777215))
        self.line_83.setFont(font3)
        self.line_83.setFrameShape(QFrame.Shape.HLine)
        self.line_83.setFrameShadow(QFrame.Shadow.Sunken)

        self.page29Layout.addWidget(self.line_83)

        self.horizontalLayout_175 = QHBoxLayout()
        self.horizontalLayout_175.setSpacing(0)
        self.horizontalLayout_175.setObjectName(u"horizontalLayout_175")
        self.horizontalSpacer_101 = QSpacerItem(20, 35, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_175.addItem(self.horizontalSpacer_101)

        self.label_liveD1Val = QLabel(self.page29)
        self.label_liveD1Val.setObjectName(u"label_liveD1Val")
        sizePolicy1.setHeightForWidth(self.label_liveD1Val.sizePolicy().hasHeightForWidth())
        self.label_liveD1Val.setSizePolicy(sizePolicy1)
        self.label_liveD1Val.setMinimumSize(QSize(0, 35))
        self.label_liveD1Val.setFont(font1)

        self.horizontalLayout_175.addWidget(self.label_liveD1Val)

        self.horizontalSpacer_164 = QSpacerItem(20, 35, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_175.addItem(self.horizontalSpacer_164)

        self.line_84 = QFrame(self.page29)
        self.line_84.setObjectName(u"line_84")
        sizePolicy5.setHeightForWidth(self.line_84.sizePolicy().hasHeightForWidth())
        self.line_84.setSizePolicy(sizePolicy5)
        self.line_84.setMinimumSize(QSize(0, 35))
        self.line_84.setMaximumSize(QSize(16777215, 16777215))
        self.line_84.setSizeIncrement(QSize(0, 0))
        self.line_84.setFrameShape(QFrame.Shape.VLine)
        self.line_84.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_175.addWidget(self.line_84)

        self.horizontalSpacer_103 = QSpacerItem(40, 35, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_175.addItem(self.horizontalSpacer_103)

        self.label_masterD1_1 = QLabel(self.page29)
        self.label_masterD1_1.setObjectName(u"label_masterD1_1")
        sizePolicy1.setHeightForWidth(self.label_masterD1_1.sizePolicy().hasHeightForWidth())
        self.label_masterD1_1.setSizePolicy(sizePolicy1)
        self.label_masterD1_1.setMinimumSize(QSize(0, 35))
        self.label_masterD1_1.setFont(font1)
        self.label_masterD1_1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_175.addWidget(self.label_masterD1_1)

        self.label_valMasterD1_1 = QLabel(self.page29)
        self.label_valMasterD1_1.setObjectName(u"label_valMasterD1_1")
        sizePolicy1.setHeightForWidth(self.label_valMasterD1_1.sizePolicy().hasHeightForWidth())
        self.label_valMasterD1_1.setSizePolicy(sizePolicy1)
        self.label_valMasterD1_1.setMinimumSize(QSize(0, 35))
        self.label_valMasterD1_1.setFont(font1)
        self.label_valMasterD1_1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_175.addWidget(self.label_valMasterD1_1)

        self.horizontalSpacer_104 = QSpacerItem(40, 35, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_175.addItem(self.horizontalSpacer_104)

        self.label_masterD1_2 = QLabel(self.page29)
        self.label_masterD1_2.setObjectName(u"label_masterD1_2")
        sizePolicy1.setHeightForWidth(self.label_masterD1_2.sizePolicy().hasHeightForWidth())
        self.label_masterD1_2.setSizePolicy(sizePolicy1)
        self.label_masterD1_2.setMinimumSize(QSize(0, 35))
        self.label_masterD1_2.setFont(font1)
        self.label_masterD1_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_175.addWidget(self.label_masterD1_2)

        self.label_valMasterD1_2 = QLabel(self.page29)
        self.label_valMasterD1_2.setObjectName(u"label_valMasterD1_2")
        sizePolicy1.setHeightForWidth(self.label_valMasterD1_2.sizePolicy().hasHeightForWidth())
        self.label_valMasterD1_2.setSizePolicy(sizePolicy1)
        self.label_valMasterD1_2.setMinimumSize(QSize(0, 35))
        self.label_valMasterD1_2.setFont(font1)
        self.label_valMasterD1_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_175.addWidget(self.label_valMasterD1_2)

        self.horizontalSpacer_102 = QSpacerItem(40, 35, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_175.addItem(self.horizontalSpacer_102)

        self.masterGroupingChannel_1 = QPushButton(self.page29)
        self.masterGroupingChannel_1.setObjectName(u"masterGroupingChannel_1")
        sizePolicy5.setHeightForWidth(self.masterGroupingChannel_1.sizePolicy().hasHeightForWidth())
        self.masterGroupingChannel_1.setSizePolicy(sizePolicy5)
        self.masterGroupingChannel_1.setMinimumSize(QSize(50, 45))

        self.horizontalLayout_175.addWidget(self.masterGroupingChannel_1)


        self.page29Layout.addLayout(self.horizontalLayout_175)

        self.line_10 = QFrame(self.page29)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setMinimumSize(QSize(0, 0))
        self.line_10.setMaximumSize(QSize(16777215, 16777215))
        self.line_10.setFrameShape(QFrame.Shape.HLine)
        self.line_10.setFrameShadow(QFrame.Shadow.Sunken)

        self.page29Layout.addWidget(self.line_10)

        self.horizontalLayout_174 = QHBoxLayout()
        self.horizontalLayout_174.setSpacing(0)
        self.horizontalLayout_174.setObjectName(u"horizontalLayout_174")
        self.horizontalSpacer_99 = QSpacerItem(20, 35, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_174.addItem(self.horizontalSpacer_99)

        self.label_liveD2Val = QLabel(self.page29)
        self.label_liveD2Val.setObjectName(u"label_liveD2Val")
        sizePolicy1.setHeightForWidth(self.label_liveD2Val.sizePolicy().hasHeightForWidth())
        self.label_liveD2Val.setSizePolicy(sizePolicy1)
        self.label_liveD2Val.setMinimumSize(QSize(0, 35))
        self.label_liveD2Val.setFont(font1)

        self.horizontalLayout_174.addWidget(self.label_liveD2Val)

        self.horizontalSpacer_165 = QSpacerItem(20, 35, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_174.addItem(self.horizontalSpacer_165)

        self.line_85 = QFrame(self.page29)
        self.line_85.setObjectName(u"line_85")
        sizePolicy5.setHeightForWidth(self.line_85.sizePolicy().hasHeightForWidth())
        self.line_85.setSizePolicy(sizePolicy5)
        self.line_85.setMinimumSize(QSize(0, 35))
        self.line_85.setMaximumSize(QSize(16777215, 16777215))
        self.line_85.setFrameShape(QFrame.Shape.VLine)
        self.line_85.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_174.addWidget(self.line_85)

        self.horizontalSpacer_106 = QSpacerItem(40, 35, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_174.addItem(self.horizontalSpacer_106)

        self.label_masterD2_1 = QLabel(self.page29)
        self.label_masterD2_1.setObjectName(u"label_masterD2_1")
        self.label_masterD2_1.setEnabled(True)
        self.label_masterD2_1.setMinimumSize(QSize(0, 35))
        self.label_masterD2_1.setFont(font1)
        self.label_masterD2_1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_174.addWidget(self.label_masterD2_1)

        self.label_valMasterD2_1 = QLabel(self.page29)
        self.label_valMasterD2_1.setObjectName(u"label_valMasterD2_1")
        sizePolicy1.setHeightForWidth(self.label_valMasterD2_1.sizePolicy().hasHeightForWidth())
        self.label_valMasterD2_1.setSizePolicy(sizePolicy1)
        self.label_valMasterD2_1.setMinimumSize(QSize(0, 35))
        self.label_valMasterD2_1.setFont(font1)
        self.label_valMasterD2_1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_174.addWidget(self.label_valMasterD2_1)

        self.horizontalSpacer_105 = QSpacerItem(40, 35, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_174.addItem(self.horizontalSpacer_105)

        self.label_masterD2_2 = QLabel(self.page29)
        self.label_masterD2_2.setObjectName(u"label_masterD2_2")
        sizePolicy1.setHeightForWidth(self.label_masterD2_2.sizePolicy().hasHeightForWidth())
        self.label_masterD2_2.setSizePolicy(sizePolicy1)
        self.label_masterD2_2.setMinimumSize(QSize(0, 35))
        self.label_masterD2_2.setFont(font1)
        self.label_masterD2_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_174.addWidget(self.label_masterD2_2)

        self.label_valMasterD2_2 = QLabel(self.page29)
        self.label_valMasterD2_2.setObjectName(u"label_valMasterD2_2")
        sizePolicy1.setHeightForWidth(self.label_valMasterD2_2.sizePolicy().hasHeightForWidth())
        self.label_valMasterD2_2.setSizePolicy(sizePolicy1)
        self.label_valMasterD2_2.setMinimumSize(QSize(0, 35))
        self.label_valMasterD2_2.setFont(font1)
        self.label_valMasterD2_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_174.addWidget(self.label_valMasterD2_2)

        self.horizontalSpacer_100 = QSpacerItem(40, 35, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_174.addItem(self.horizontalSpacer_100)

        self.masterGroupingChannel_2 = QPushButton(self.page29)
        self.masterGroupingChannel_2.setObjectName(u"masterGroupingChannel_2")
        sizePolicy5.setHeightForWidth(self.masterGroupingChannel_2.sizePolicy().hasHeightForWidth())
        self.masterGroupingChannel_2.setSizePolicy(sizePolicy5)
        self.masterGroupingChannel_2.setMinimumSize(QSize(50, 45))

        self.horizontalLayout_174.addWidget(self.masterGroupingChannel_2)


        self.page29Layout.addLayout(self.horizontalLayout_174)

        self.line_11 = QFrame(self.page29)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setMinimumSize(QSize(0, 0))
        self.line_11.setMaximumSize(QSize(16777215, 16777215))
        self.line_11.setFrameShape(QFrame.Shape.HLine)
        self.line_11.setFrameShadow(QFrame.Shadow.Sunken)

        self.page29Layout.addWidget(self.line_11)

        self.horizontalLayout_169 = QHBoxLayout()
        self.horizontalLayout_169.setSpacing(0)
        self.horizontalLayout_169.setObjectName(u"horizontalLayout_169")
        self.horizontalSpacer_107 = QSpacerItem(20, 35, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_169.addItem(self.horizontalSpacer_107)

        self.label_liveD3Val = QLabel(self.page29)
        self.label_liveD3Val.setObjectName(u"label_liveD3Val")
        sizePolicy1.setHeightForWidth(self.label_liveD3Val.sizePolicy().hasHeightForWidth())
        self.label_liveD3Val.setSizePolicy(sizePolicy1)
        self.label_liveD3Val.setMinimumSize(QSize(0, 35))
        self.label_liveD3Val.setFont(font1)

        self.horizontalLayout_169.addWidget(self.label_liveD3Val)

        self.horizontalSpacer_166 = QSpacerItem(20, 35, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_169.addItem(self.horizontalSpacer_166)

        self.line_86 = QFrame(self.page29)
        self.line_86.setObjectName(u"line_86")
        sizePolicy5.setHeightForWidth(self.line_86.sizePolicy().hasHeightForWidth())
        self.line_86.setSizePolicy(sizePolicy5)
        self.line_86.setMinimumSize(QSize(0, 35))
        self.line_86.setMaximumSize(QSize(16777215, 16777215))
        self.line_86.setFrameShape(QFrame.Shape.VLine)
        self.line_86.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_169.addWidget(self.line_86)

        self.horizontalSpacer_109 = QSpacerItem(40, 35, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_169.addItem(self.horizontalSpacer_109)

        self.label_masterD3_1 = QLabel(self.page29)
        self.label_masterD3_1.setObjectName(u"label_masterD3_1")
        sizePolicy1.setHeightForWidth(self.label_masterD3_1.sizePolicy().hasHeightForWidth())
        self.label_masterD3_1.setSizePolicy(sizePolicy1)
        self.label_masterD3_1.setMinimumSize(QSize(0, 35))
        self.label_masterD3_1.setFont(font1)
        self.label_masterD3_1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_169.addWidget(self.label_masterD3_1)

        self.label_valMasterD3_1 = QLabel(self.page29)
        self.label_valMasterD3_1.setObjectName(u"label_valMasterD3_1")
        sizePolicy1.setHeightForWidth(self.label_valMasterD3_1.sizePolicy().hasHeightForWidth())
        self.label_valMasterD3_1.setSizePolicy(sizePolicy1)
        self.label_valMasterD3_1.setMinimumSize(QSize(0, 35))
        self.label_valMasterD3_1.setFont(font1)
        self.label_valMasterD3_1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_169.addWidget(self.label_valMasterD3_1)

        self.horizontalSpacer_110 = QSpacerItem(40, 35, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_169.addItem(self.horizontalSpacer_110)

        self.label_masterD3_2 = QLabel(self.page29)
        self.label_masterD3_2.setObjectName(u"label_masterD3_2")
        sizePolicy1.setHeightForWidth(self.label_masterD3_2.sizePolicy().hasHeightForWidth())
        self.label_masterD3_2.setSizePolicy(sizePolicy1)
        self.label_masterD3_2.setMinimumSize(QSize(0, 35))
        self.label_masterD3_2.setFont(font1)
        self.label_masterD3_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_169.addWidget(self.label_masterD3_2)

        self.label_valMasterD3_2 = QLabel(self.page29)
        self.label_valMasterD3_2.setObjectName(u"label_valMasterD3_2")
        sizePolicy1.setHeightForWidth(self.label_valMasterD3_2.sizePolicy().hasHeightForWidth())
        self.label_valMasterD3_2.setSizePolicy(sizePolicy1)
        self.label_valMasterD3_2.setMinimumSize(QSize(0, 35))
        self.label_valMasterD3_2.setFont(font1)
        self.label_valMasterD3_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_169.addWidget(self.label_valMasterD3_2)

        self.horizontalSpacer_108 = QSpacerItem(40, 35, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_169.addItem(self.horizontalSpacer_108)

        self.masterGroupingChannel_3 = QPushButton(self.page29)
        self.masterGroupingChannel_3.setObjectName(u"masterGroupingChannel_3")
        sizePolicy5.setHeightForWidth(self.masterGroupingChannel_3.sizePolicy().hasHeightForWidth())
        self.masterGroupingChannel_3.setSizePolicy(sizePolicy5)
        self.masterGroupingChannel_3.setMinimumSize(QSize(50, 45))

        self.horizontalLayout_169.addWidget(self.masterGroupingChannel_3)


        self.page29Layout.addLayout(self.horizontalLayout_169)

        self.line_12 = QFrame(self.page29)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setMinimumSize(QSize(0, 0))
        self.line_12.setMaximumSize(QSize(16777215, 16777215))
        self.line_12.setFrameShape(QFrame.Shape.HLine)
        self.line_12.setFrameShadow(QFrame.Shadow.Sunken)

        self.page29Layout.addWidget(self.line_12)

        self.horizontalLayout_170 = QHBoxLayout()
        self.horizontalLayout_170.setSpacing(0)
        self.horizontalLayout_170.setObjectName(u"horizontalLayout_170")
        self.horizontalSpacer_111 = QSpacerItem(20, 35, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_170.addItem(self.horizontalSpacer_111)

        self.label_liveD4val = QLabel(self.page29)
        self.label_liveD4val.setObjectName(u"label_liveD4val")
        self.label_liveD4val.setMinimumSize(QSize(0, 35))
        self.label_liveD4val.setFont(font1)

        self.horizontalLayout_170.addWidget(self.label_liveD4val)

        self.horizontalSpacer_168 = QSpacerItem(20, 35, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_170.addItem(self.horizontalSpacer_168)

        self.line_87 = QFrame(self.page29)
        self.line_87.setObjectName(u"line_87")
        sizePolicy5.setHeightForWidth(self.line_87.sizePolicy().hasHeightForWidth())
        self.line_87.setSizePolicy(sizePolicy5)
        self.line_87.setMinimumSize(QSize(0, 35))
        self.line_87.setMaximumSize(QSize(16777215, 16777215))
        self.line_87.setFrameShape(QFrame.Shape.VLine)
        self.line_87.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_170.addWidget(self.line_87)

        self.horizontalSpacer_113 = QSpacerItem(40, 35, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_170.addItem(self.horizontalSpacer_113)

        self.label_masterD4_1 = QLabel(self.page29)
        self.label_masterD4_1.setObjectName(u"label_masterD4_1")
        self.label_masterD4_1.setMinimumSize(QSize(0, 35))
        self.label_masterD4_1.setFont(font1)
        self.label_masterD4_1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_170.addWidget(self.label_masterD4_1)

        self.label_valMasterD4_1 = QLabel(self.page29)
        self.label_valMasterD4_1.setObjectName(u"label_valMasterD4_1")
        self.label_valMasterD4_1.setMinimumSize(QSize(0, 35))
        self.label_valMasterD4_1.setFont(font1)
        self.label_valMasterD4_1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_170.addWidget(self.label_valMasterD4_1)

        self.horizontalSpacer_114 = QSpacerItem(40, 35, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_170.addItem(self.horizontalSpacer_114)

        self.label_masterD4_2 = QLabel(self.page29)
        self.label_masterD4_2.setObjectName(u"label_masterD4_2")
        self.label_masterD4_2.setMinimumSize(QSize(0, 35))
        self.label_masterD4_2.setFont(font1)
        self.label_masterD4_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_170.addWidget(self.label_masterD4_2)

        self.label_valMasterD4_2 = QLabel(self.page29)
        self.label_valMasterD4_2.setObjectName(u"label_valMasterD4_2")
        self.label_valMasterD4_2.setMinimumSize(QSize(0, 35))
        self.label_valMasterD4_2.setFont(font1)
        self.label_valMasterD4_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_170.addWidget(self.label_valMasterD4_2)

        self.horizontalSpacer_112 = QSpacerItem(40, 35, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_170.addItem(self.horizontalSpacer_112)

        self.masterGroupingChannel_4 = QPushButton(self.page29)
        self.masterGroupingChannel_4.setObjectName(u"masterGroupingChannel_4")
        sizePolicy5.setHeightForWidth(self.masterGroupingChannel_4.sizePolicy().hasHeightForWidth())
        self.masterGroupingChannel_4.setSizePolicy(sizePolicy5)
        self.masterGroupingChannel_4.setMinimumSize(QSize(50, 45))

        self.horizontalLayout_170.addWidget(self.masterGroupingChannel_4)


        self.page29Layout.addLayout(self.horizontalLayout_170)

        self.stackedWidget_main.addWidget(self.page29)
        self.page30 = QWidget()
        self.page30.setObjectName(u"page30")
        self.page30Layout = QVBoxLayout(self.page30)
        self.page30Layout.setObjectName(u"page30Layout")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.ProgramList_TableView = QTableView(self.page30)
        self.ProgramList_TableView.setObjectName(u"ProgramList_TableView")

        self.verticalLayout_9.addWidget(self.ProgramList_TableView)


        self.page30Layout.addLayout(self.verticalLayout_9)

        self.stackedWidget_main.addWidget(self.page30)
        self.page31 = QWidget()
        self.page31.setObjectName(u"page31")
        self.page31Layout = QVBoxLayout(self.page31)
        self.page31Layout.setObjectName(u"page31Layout")
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.horizontalLayout_36 = QHBoxLayout()
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.label_programIdforSettings = QLabel(self.page31)
        self.label_programIdforSettings.setObjectName(u"label_programIdforSettings")
        self.label_programIdforSettings.setMinimumSize(QSize(0, 35))
        self.label_programIdforSettings.setFont(font1)

        self.horizontalLayout_36.addWidget(self.label_programIdforSettings)

        self.comboBox_programIdSetting_Inner = QComboBox(self.page31)
        self.comboBox_programIdSetting_Inner.setObjectName(u"comboBox_programIdSetting_Inner")
        self.comboBox_programIdSetting_Inner.setMinimumSize(QSize(100, 35))
        self.comboBox_programIdSetting_Inner.setMaximumSize(QSize(16777215, 16777215))
        self.comboBox_programIdSetting_Inner.setFont(font1)

        self.horizontalLayout_36.addWidget(self.comboBox_programIdSetting_Inner)

        self.label_programNameSettings = QLabel(self.page31)
        self.label_programNameSettings.setObjectName(u"label_programNameSettings")
        self.label_programNameSettings.setMinimumSize(QSize(0, 35))
        self.label_programNameSettings.setFont(font1)

        self.horizontalLayout_36.addWidget(self.label_programNameSettings)

        self.lineEdit_programNameSettings = QLineEdit(self.page31)
        self.lineEdit_programNameSettings.setObjectName(u"lineEdit_programNameSettings")
        self.lineEdit_programNameSettings.setMinimumSize(QSize(0, 35))
        self.lineEdit_programNameSettings.setFont(font1)

        self.horizontalLayout_36.addWidget(self.lineEdit_programNameSettings)

        self.button_staticSettingsForAll = QPushButton(self.page31)
        self.button_staticSettingsForAll.setObjectName(u"button_staticSettingsForAll")
        sizePolicy1.setHeightForWidth(self.button_staticSettingsForAll.sizePolicy().hasHeightForWidth())
        self.button_staticSettingsForAll.setSizePolicy(sizePolicy1)
        self.button_staticSettingsForAll.setMinimumSize(QSize(90, 32))

        self.horizontalLayout_36.addWidget(self.button_staticSettingsForAll)


        self.verticalLayout_12.addLayout(self.horizontalLayout_36)

        self.horizontalLayout_93 = QHBoxLayout()
        self.horizontalLayout_93.setObjectName(u"horizontalLayout_93")
        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_93.addItem(self.horizontalSpacer_19)

        self.label_probeSetting = QLabel(self.page31)
        self.label_probeSetting.setObjectName(u"label_probeSetting")
        self.label_probeSetting.setMinimumSize(QSize(0, 35))
        self.label_probeSetting.setFont(font1)

        self.horizontalLayout_93.addWidget(self.label_probeSetting)

        self.comboBox_toselectProbe = QComboBox(self.page31)
        self.comboBox_toselectProbe.addItem("")
        self.comboBox_toselectProbe.addItem("")
        self.comboBox_toselectProbe.addItem("")
        self.comboBox_toselectProbe.addItem("")
        self.comboBox_toselectProbe.addItem("")
        self.comboBox_toselectProbe.addItem("")
        self.comboBox_toselectProbe.addItem("")
        self.comboBox_toselectProbe.addItem("")
        self.comboBox_toselectProbe.setObjectName(u"comboBox_toselectProbe")
        self.comboBox_toselectProbe.setMinimumSize(QSize(70, 35))
        self.comboBox_toselectProbe.setMaximumSize(QSize(16777215, 16777215))
        self.comboBox_toselectProbe.setFont(font1)

        self.horizontalLayout_93.addWidget(self.comboBox_toselectProbe, 0, Qt.AlignmentFlag.AlignHCenter)

        self.button_delete = QPushButton(self.page31)
        self.button_delete.setObjectName(u"button_delete")
        self.button_delete.setMinimumSize(QSize(70, 35))

        self.horizontalLayout_93.addWidget(self.button_delete)

        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_93.addItem(self.horizontalSpacer_21)


        self.verticalLayout_12.addLayout(self.horizontalLayout_93)

        self.tabWidget_2 = QTabWidget(self.page31)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        sizePolicy.setHeightForWidth(self.tabWidget_2.sizePolicy().hasHeightForWidth())
        self.tabWidget_2.setSizePolicy(sizePolicy)
        self.tabWidget_2.setMinimumSize(QSize(0, 120))
        self.tabWidget_2.setMaximumSize(QSize(16777215, 280))
        self.tabWidget_2.setFont(font4)
        self.tabWidget_2.setStyleSheet(u"\n"
"QTabBar::tab {\n"
"    height: 30px;  /* height of the tab itself */\n"
"    width:380px\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    border-bottom: 4px solid #fec222;  /* height of the indicator */\n"
"}\n"
"\n"
"")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        font8 = QFont()
        font8.setFamilies([u"MS Shell Dlg 2"])
        font8.setPointSize(9)
        font8.setBold(False)
        font8.setItalic(False)
        self.tab_3.setFont(font8)
        self.tab_3.setStyleSheet(u"")
        self.verticalLayout_14 = QVBoxLayout(self.tab_3)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.stackedWidget_2 = QStackedWidget(self.tab_3)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.stackedWidget_2.setMinimumSize(QSize(0, 240))
        self.stackedWidget_2.setMaximumSize(QSize(16777215, 16777215))
        font9 = QFont()
        font9.setFamilies([u"MS Shell Dlg 2"])
        font9.setPointSize(11)
        self.stackedWidget_2.setFont(font9)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_13 = QVBoxLayout(self.page_4)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.horizontalLayout_149 = QHBoxLayout()
        self.horizontalLayout_149.setObjectName(u"horizontalLayout_149")
        self.horizontalLayout_161 = QHBoxLayout()
        self.horizontalLayout_161.setObjectName(u"horizontalLayout_161")
        self.label_formula = QLabel(self.page_4)
        self.label_formula.setObjectName(u"label_formula")
        self.label_formula.setMinimumSize(QSize(0, 35))
        self.label_formula.setMaximumSize(QSize(16777215, 16777215))
        self.label_formula.setFont(font1)

        self.horizontalLayout_161.addWidget(self.label_formula)

        self.label_formulaBar = QLabel(self.page_4)
        self.label_formulaBar.setObjectName(u"label_formulaBar")
        self.label_formulaBar.setMinimumSize(QSize(0, 35))
        self.label_formulaBar.setMaximumSize(QSize(16777215, 16777215))
        self.label_formulaBar.setFont(font1)

        self.horizontalLayout_161.addWidget(self.label_formulaBar, 0, Qt.AlignmentFlag.AlignLeft)

        self.button_setFormulaSettings = QPushButton(self.page_4)
        self.button_setFormulaSettings.setObjectName(u"button_setFormulaSettings")
        sizePolicy1.setHeightForWidth(self.button_setFormulaSettings.sizePolicy().hasHeightForWidth())
        self.button_setFormulaSettings.setSizePolicy(sizePolicy1)
        self.button_setFormulaSettings.setMinimumSize(QSize(150, 32))
        self.button_setFormulaSettings.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_161.addWidget(self.button_setFormulaSettings)


        self.horizontalLayout_149.addLayout(self.horizontalLayout_161)


        self.verticalLayout_13.addLayout(self.horizontalLayout_149)

        self.horizontalLayout_155 = QHBoxLayout()
        self.horizontalLayout_155.setObjectName(u"horizontalLayout_155")
        self.label_masterType = QLabel(self.page_4)
        self.label_masterType.setObjectName(u"label_masterType")
        self.label_masterType.setMinimumSize(QSize(0, 35))
        self.label_masterType.setMaximumSize(QSize(16777215, 16777215))
        self.label_masterType.setFont(font1)

        self.horizontalLayout_155.addWidget(self.label_masterType, 0, Qt.AlignmentFlag.AlignRight)

        self.comboBox_masterType = QComboBox(self.page_4)
        self.comboBox_masterType.addItem("")
        self.comboBox_masterType.addItem("")
        self.comboBox_masterType.addItem("")
        self.comboBox_masterType.setObjectName(u"comboBox_masterType")
        self.comboBox_masterType.setMinimumSize(QSize(170, 35))
        self.comboBox_masterType.setMaximumSize(QSize(16777215, 16777215))
        self.comboBox_masterType.setFont(font1)

        self.horizontalLayout_155.addWidget(self.comboBox_masterType, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_13.addLayout(self.horizontalLayout_155)

        self.verticalSpacer_50 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_50)

        self.horizontalLayout_154 = QHBoxLayout()
        self.horizontalLayout_154.setObjectName(u"horizontalLayout_154")
        self.label_masterLower = QLabel(self.page_4)
        self.label_masterLower.setObjectName(u"label_masterLower")
        self.label_masterLower.setMinimumSize(QSize(0, 35))
        self.label_masterLower.setMaximumSize(QSize(16777215, 16777215))
        self.label_masterLower.setFont(font1)

        self.horizontalLayout_154.addWidget(self.label_masterLower, 0, Qt.AlignmentFlag.AlignRight)

        self.lineEdit_masterLower = QLineEdit(self.page_4)
        self.lineEdit_masterLower.setObjectName(u"lineEdit_masterLower")
        sizePolicy1.setHeightForWidth(self.lineEdit_masterLower.sizePolicy().hasHeightForWidth())
        self.lineEdit_masterLower.setSizePolicy(sizePolicy1)
        self.lineEdit_masterLower.setMinimumSize(QSize(170, 35))
        self.lineEdit_masterLower.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_masterLower.setFont(font1)

        self.horizontalLayout_154.addWidget(self.lineEdit_masterLower, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_13.addLayout(self.horizontalLayout_154)

        self.verticalSpacer_53 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_53)

        self.horizontalLayout_153 = QHBoxLayout()
        self.horizontalLayout_153.setObjectName(u"horizontalLayout_153")
        self.label_master = QLabel(self.page_4)
        self.label_master.setObjectName(u"label_master")
        self.label_master.setMinimumSize(QSize(0, 35))
        self.label_master.setMaximumSize(QSize(16777215, 16777215))
        self.label_master.setFont(font1)

        self.horizontalLayout_153.addWidget(self.label_master, 0, Qt.AlignmentFlag.AlignRight)

        self.lineEdit_master = QLineEdit(self.page_4)
        self.lineEdit_master.setObjectName(u"lineEdit_master")
        sizePolicy1.setHeightForWidth(self.lineEdit_master.sizePolicy().hasHeightForWidth())
        self.lineEdit_master.setSizePolicy(sizePolicy1)
        self.lineEdit_master.setMinimumSize(QSize(170, 35))
        self.lineEdit_master.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_master.setFont(font1)

        self.horizontalLayout_153.addWidget(self.lineEdit_master, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_13.addLayout(self.horizontalLayout_153)

        self.horizontalLayout_163 = QHBoxLayout()
        self.horizontalLayout_163.setObjectName(u"horizontalLayout_163")
        self.horizontalSpacer_176 = QSpacerItem(230, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_163.addItem(self.horizontalSpacer_176)

        self.label_masterHigher = QLabel(self.page_4)
        self.label_masterHigher.setObjectName(u"label_masterHigher")
        self.label_masterHigher.setMinimumSize(QSize(0, 35))
        self.label_masterHigher.setMaximumSize(QSize(16777215, 16777215))
        self.label_masterHigher.setFont(font1)

        self.horizontalLayout_163.addWidget(self.label_masterHigher, 0, Qt.AlignmentFlag.AlignRight)

        self.lineEdit_masterHigher = QLineEdit(self.page_4)
        self.lineEdit_masterHigher.setObjectName(u"lineEdit_masterHigher")
        sizePolicy1.setHeightForWidth(self.lineEdit_masterHigher.sizePolicy().hasHeightForWidth())
        self.lineEdit_masterHigher.setSizePolicy(sizePolicy1)
        self.lineEdit_masterHigher.setMinimumSize(QSize(170, 35))
        self.lineEdit_masterHigher.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_masterHigher.setFont(font1)

        self.horizontalLayout_163.addWidget(self.lineEdit_masterHigher, 0, Qt.AlignmentFlag.AlignLeft)

        self.horizontalSpacer_184 = QSpacerItem(90, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_163.addItem(self.horizontalSpacer_184)

        self.label_4 = QLabel(self.page_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 35))
        self.label_4.setMaximumSize(QSize(95, 16777215))
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_163.addWidget(self.label_4)


        self.verticalLayout_13.addLayout(self.horizontalLayout_163)

        self.verticalSpacer_64 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_64)

        self.stackedWidget_2.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.verticalLayout_16 = QVBoxLayout(self.page_5)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalSpacer_51 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_16.addItem(self.verticalSpacer_51)

        self.horizontalLayout_171 = QHBoxLayout()
        self.horizontalLayout_171.setObjectName(u"horizontalLayout_171")
        self.label_usl = QLabel(self.page_5)
        self.label_usl.setObjectName(u"label_usl")
        self.label_usl.setMinimumSize(QSize(0, 35))
        self.label_usl.setMaximumSize(QSize(16777215, 16777215))
        self.label_usl.setFont(font1)

        self.horizontalLayout_171.addWidget(self.label_usl, 0, Qt.AlignmentFlag.AlignRight)

        self.lineEdit_usl = QLineEdit(self.page_5)
        self.lineEdit_usl.setObjectName(u"lineEdit_usl")
        self.lineEdit_usl.setMinimumSize(QSize(170, 35))
        self.lineEdit_usl.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_usl.setFont(font1)

        self.horizontalLayout_171.addWidget(self.lineEdit_usl, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_16.addLayout(self.horizontalLayout_171)

        self.verticalSpacer_54 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_16.addItem(self.verticalSpacer_54)

        self.horizontalLayout_172 = QHBoxLayout()
        self.horizontalLayout_172.setObjectName(u"horizontalLayout_172")
        self.label_ucl = QLabel(self.page_5)
        self.label_ucl.setObjectName(u"label_ucl")
        self.label_ucl.setMinimumSize(QSize(0, 35))
        self.label_ucl.setMaximumSize(QSize(16777215, 16777215))
        self.label_ucl.setFont(font1)

        self.horizontalLayout_172.addWidget(self.label_ucl, 0, Qt.AlignmentFlag.AlignRight)

        self.lineEdit_ucl = QLineEdit(self.page_5)
        self.lineEdit_ucl.setObjectName(u"lineEdit_ucl")
        self.lineEdit_ucl.setMinimumSize(QSize(170, 35))
        self.lineEdit_ucl.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_ucl.setFont(font1)

        self.horizontalLayout_172.addWidget(self.lineEdit_ucl, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_16.addLayout(self.horizontalLayout_172)

        self.verticalSpacer_55 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_16.addItem(self.verticalSpacer_55)

        self.horizontalLayout_177 = QHBoxLayout()
        self.horizontalLayout_177.setObjectName(u"horizontalLayout_177")
        self.horizontalSpacer_24 = QSpacerItem(230, 30, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_177.addItem(self.horizontalSpacer_24)

        self.label_nominalValue = QLabel(self.page_5)
        self.label_nominalValue.setObjectName(u"label_nominalValue")
        self.label_nominalValue.setMinimumSize(QSize(0, 35))
        self.label_nominalValue.setMaximumSize(QSize(16777215, 16777215))
        self.label_nominalValue.setFont(font1)

        self.horizontalLayout_177.addWidget(self.label_nominalValue, 0, Qt.AlignmentFlag.AlignRight)

        self.lineEdit_nominalValue = QLineEdit(self.page_5)
        self.lineEdit_nominalValue.setObjectName(u"lineEdit_nominalValue")
        self.lineEdit_nominalValue.setMinimumSize(QSize(170, 35))
        self.lineEdit_nominalValue.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_nominalValue.setFont(font1)

        self.horizontalLayout_177.addWidget(self.lineEdit_nominalValue, 0, Qt.AlignmentFlag.AlignLeft)

        self.horizontalSpacer_44 = QSpacerItem(100, 30, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_177.addItem(self.horizontalSpacer_44)

        self.label_pageNo = QLabel(self.page_5)
        self.label_pageNo.setObjectName(u"label_pageNo")
        self.label_pageNo.setMinimumSize(QSize(0, 35))
        self.label_pageNo.setMaximumSize(QSize(95, 16777215))
        self.label_pageNo.setFont(font1)
        self.label_pageNo.setStyleSheet(u"QLabel#label_pageNo {\n"
"    qproperty-alignment: 'AlignCenter';   /* center text horizontally and vertically */\n"
"}\n"
"")
        self.label_pageNo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_177.addWidget(self.label_pageNo, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_16.addLayout(self.horizontalLayout_177)

        self.verticalSpacer_65 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_16.addItem(self.verticalSpacer_65)

        self.stackedWidget_2.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.verticalLayout_17 = QVBoxLayout(self.page_6)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalSpacer_46 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer_46)

        self.horizontalLayout_182 = QHBoxLayout()
        self.horizontalLayout_182.setObjectName(u"horizontalLayout_182")
        self.label_lcl = QLabel(self.page_6)
        self.label_lcl.setObjectName(u"label_lcl")
        self.label_lcl.setMinimumSize(QSize(0, 35))
        self.label_lcl.setMaximumSize(QSize(16777215, 16777215))
        self.label_lcl.setFont(font1)

        self.horizontalLayout_182.addWidget(self.label_lcl, 0, Qt.AlignmentFlag.AlignRight)

        self.lineEdit_lcl = QLineEdit(self.page_6)
        self.lineEdit_lcl.setObjectName(u"lineEdit_lcl")
        self.lineEdit_lcl.setMinimumSize(QSize(170, 35))

        self.horizontalLayout_182.addWidget(self.lineEdit_lcl, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_17.addLayout(self.horizontalLayout_182)

        self.verticalSpacer_47 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer_47)

        self.horizontalLayout_183 = QHBoxLayout()
        self.horizontalLayout_183.setObjectName(u"horizontalLayout_183")
        self.label_lsl = QLabel(self.page_6)
        self.label_lsl.setObjectName(u"label_lsl")
        self.label_lsl.setMinimumSize(QSize(0, 35))
        self.label_lsl.setMaximumSize(QSize(16777215, 16777215))
        self.label_lsl.setFont(font1)

        self.horizontalLayout_183.addWidget(self.label_lsl, 0, Qt.AlignmentFlag.AlignRight)

        self.lineEdit_lsl = QLineEdit(self.page_6)
        self.lineEdit_lsl.setObjectName(u"lineEdit_lsl")
        self.lineEdit_lsl.setMinimumSize(QSize(170, 35))

        self.horizontalLayout_183.addWidget(self.lineEdit_lsl, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_17.addLayout(self.horizontalLayout_183)

        self.verticalSpacer_49 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer_49)

        self.horizontalLayout_165 = QHBoxLayout()
        self.horizontalLayout_165.setObjectName(u"horizontalLayout_165")
        self.horizontalSpacer_61 = QSpacerItem(260, 30, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_165.addItem(self.horizontalSpacer_61)

        self.label_method = QLabel(self.page_6)
        self.label_method.setObjectName(u"label_method")

        self.horizontalLayout_165.addWidget(self.label_method, 0, Qt.AlignmentFlag.AlignRight)

        self.comboBox_methodProbe = QComboBox(self.page_6)
        self.comboBox_methodProbe.addItem("")
        self.comboBox_methodProbe.addItem("")
        self.comboBox_methodProbe.setObjectName(u"comboBox_methodProbe")
        self.comboBox_methodProbe.setMinimumSize(QSize(170, 35))

        self.horizontalLayout_165.addWidget(self.comboBox_methodProbe, 0, Qt.AlignmentFlag.AlignLeft)

        self.horizontalSpacer_174 = QSpacerItem(80, 30, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_165.addItem(self.horizontalSpacer_174)

        self.label_2 = QLabel(self.page_6)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 35))
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_165.addWidget(self.label_2)


        self.verticalLayout_17.addLayout(self.horizontalLayout_165)

        self.verticalSpacer_66 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer_66)

        self.stackedWidget_2.addWidget(self.page_6)
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.verticalLayout_18 = QVBoxLayout(self.page_7)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.horizontalLayout_186 = QHBoxLayout()
        self.horizontalLayout_186.setObjectName(u"horizontalLayout_186")
        self.label_range = QLabel(self.page_7)
        self.label_range.setObjectName(u"label_range")
        self.label_range.setMinimumSize(QSize(0, 35))

        self.horizontalLayout_186.addWidget(self.label_range, 0, Qt.AlignmentFlag.AlignRight)

        self.comboBox_rangeProbe = QComboBox(self.page_7)
        self.comboBox_rangeProbe.addItem("")
        self.comboBox_rangeProbe.addItem("")
        self.comboBox_rangeProbe.addItem("")
        self.comboBox_rangeProbe.addItem("")
        self.comboBox_rangeProbe.addItem("")
        self.comboBox_rangeProbe.addItem("")
        self.comboBox_rangeProbe.setObjectName(u"comboBox_rangeProbe")
        self.comboBox_rangeProbe.setMinimumSize(QSize(170, 35))

        self.horizontalLayout_186.addWidget(self.comboBox_rangeProbe, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_18.addLayout(self.horizontalLayout_186)

        self.verticalSpacer_41 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_18.addItem(self.verticalSpacer_41)

        self.horizontalLayout_129 = QHBoxLayout()
        self.horizontalLayout_129.setObjectName(u"horizontalLayout_129")
        self.label_ovality = QLabel(self.page_7)
        self.label_ovality.setObjectName(u"label_ovality")

        self.horizontalLayout_129.addWidget(self.label_ovality, 0, Qt.AlignmentFlag.AlignRight)

        self.comboBox_ovalityOnOff = QComboBox(self.page_7)
        self.comboBox_ovalityOnOff.addItem("")
        self.comboBox_ovalityOnOff.addItem("")
        self.comboBox_ovalityOnOff.setObjectName(u"comboBox_ovalityOnOff")
        self.comboBox_ovalityOnOff.setMinimumSize(QSize(170, 35))

        self.horizontalLayout_129.addWidget(self.comboBox_ovalityOnOff, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_18.addLayout(self.horizontalLayout_129)

        self.verticalSpacer_44 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_18.addItem(self.verticalSpacer_44)

        self.horizontalLayout_196 = QHBoxLayout()
        self.horizontalLayout_196.setObjectName(u"horizontalLayout_196")
        self.label_case = QLabel(self.page_7)
        self.label_case.setObjectName(u"label_case")
        self.label_case.setMinimumSize(QSize(0, 35))

        self.horizontalLayout_196.addWidget(self.label_case, 0, Qt.AlignmentFlag.AlignRight)

        self.comboBox_caseProbe = QComboBox(self.page_7)
        self.comboBox_caseProbe.addItem("")
        self.comboBox_caseProbe.addItem("")
        self.comboBox_caseProbe.addItem("")
        self.comboBox_caseProbe.setObjectName(u"comboBox_caseProbe")
        self.comboBox_caseProbe.setMinimumSize(QSize(170, 35))

        self.horizontalLayout_196.addWidget(self.comboBox_caseProbe, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_18.addLayout(self.horizontalLayout_196)

        self.verticalSpacer_45 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_18.addItem(self.verticalSpacer_45)

        self.horizontalLayout_187 = QHBoxLayout()
        self.horizontalLayout_187.setObjectName(u"horizontalLayout_187")
        self.horizontalSpacer_60 = QSpacerItem(255, 30, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_187.addItem(self.horizontalSpacer_60)

        self.label_caseT = QLabel(self.page_7)
        self.label_caseT.setObjectName(u"label_caseT")
        self.label_caseT.setMinimumSize(QSize(0, 35))

        self.horizontalLayout_187.addWidget(self.label_caseT, 0, Qt.AlignmentFlag.AlignRight)

        self.lineEdit_caseT = QLineEdit(self.page_7)
        self.lineEdit_caseT.setObjectName(u"lineEdit_caseT")
        self.lineEdit_caseT.setMinimumSize(QSize(170, 35))

        self.horizontalLayout_187.addWidget(self.lineEdit_caseT, 0, Qt.AlignmentFlag.AlignLeft)

        self.horizontalSpacer_45 = QSpacerItem(80, 30, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_187.addItem(self.horizontalSpacer_45)

        self.label_page4 = QLabel(self.page_7)
        self.label_page4.setObjectName(u"label_page4")
        self.label_page4.setMinimumSize(QSize(0, 35))
        self.label_page4.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_187.addWidget(self.label_page4)


        self.verticalLayout_18.addLayout(self.horizontalLayout_187)

        self.verticalSpacer_69 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_18.addItem(self.verticalSpacer_69)

        self.stackedWidget_2.addWidget(self.page_7)
        self.page_8 = QWidget()
        self.page_8.setObjectName(u"page_8")
        self.page8Layout1 = QVBoxLayout(self.page_8)
        self.page8Layout1.setObjectName(u"page8Layout1")
        self.verticalSpacer_23 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.page8Layout1.addItem(self.verticalSpacer_23)

        self.horizontalLayout_139 = QHBoxLayout()
        self.horizontalLayout_139.setObjectName(u"horizontalLayout_139")
        self.label_leastCount = QLabel(self.page_8)
        self.label_leastCount.setObjectName(u"label_leastCount")
        self.label_leastCount.setMinimumSize(QSize(0, 35))

        self.horizontalLayout_139.addWidget(self.label_leastCount, 0, Qt.AlignmentFlag.AlignRight)

        self.lineEdit_leastCount = QComboBox(self.page_8)
        self.lineEdit_leastCount.addItem("")
        self.lineEdit_leastCount.addItem("")
        self.lineEdit_leastCount.addItem("")
        self.lineEdit_leastCount.addItem("")
        self.lineEdit_leastCount.addItem("")
        self.lineEdit_leastCount.addItem("")
        self.lineEdit_leastCount.setObjectName(u"lineEdit_leastCount")
        sizePolicy4.setHeightForWidth(self.lineEdit_leastCount.sizePolicy().hasHeightForWidth())
        self.lineEdit_leastCount.setSizePolicy(sizePolicy4)
        self.lineEdit_leastCount.setMinimumSize(QSize(170, 35))

        self.horizontalLayout_139.addWidget(self.lineEdit_leastCount, 0, Qt.AlignmentFlag.AlignLeft)


        self.page8Layout1.addLayout(self.horizontalLayout_139)

        self.verticalSpacer_25 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.page8Layout1.addItem(self.verticalSpacer_25)

        self.horizontalLayout_150 = QHBoxLayout()
        self.horizontalLayout_150.setObjectName(u"horizontalLayout_150")
        self.label_probeSensitivity = QLabel(self.page_8)
        self.label_probeSensitivity.setObjectName(u"label_probeSensitivity")
        self.label_probeSensitivity.setMinimumSize(QSize(0, 35))

        self.horizontalLayout_150.addWidget(self.label_probeSensitivity, 0, Qt.AlignmentFlag.AlignRight)

        self.lineEdit_probeSensitivity = QLineEdit(self.page_8)
        self.lineEdit_probeSensitivity.setObjectName(u"lineEdit_probeSensitivity")
        self.lineEdit_probeSensitivity.setMinimumSize(QSize(170, 35))

        self.horizontalLayout_150.addWidget(self.lineEdit_probeSensitivity, 0, Qt.AlignmentFlag.AlignLeft)


        self.page8Layout1.addLayout(self.horizontalLayout_150)

        self.verticalSpacer_26 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.page8Layout1.addItem(self.verticalSpacer_26)

        self.horizontalLayout_194 = QHBoxLayout()
        self.horizontalLayout_194.setObjectName(u"horizontalLayout_194")
        self.horizontalSpacer_186 = QSpacerItem(156, 30, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_194.addItem(self.horizontalSpacer_186)

        self.label_airSensitivityQuotient = QLabel(self.page_8)
        self.label_airSensitivityQuotient.setObjectName(u"label_airSensitivityQuotient")
        self.label_airSensitivityQuotient.setMinimumSize(QSize(0, 35))

        self.horizontalLayout_194.addWidget(self.label_airSensitivityQuotient, 0, Qt.AlignmentFlag.AlignRight)

        self.lineEdit_airSensitivityQuotient = QLineEdit(self.page_8)
        self.lineEdit_airSensitivityQuotient.setObjectName(u"lineEdit_airSensitivityQuotient")
        self.lineEdit_airSensitivityQuotient.setMinimumSize(QSize(170, 35))

        self.horizontalLayout_194.addWidget(self.lineEdit_airSensitivityQuotient, 0, Qt.AlignmentFlag.AlignLeft)

        self.horizontalSpacer_187 = QSpacerItem(80, 30, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_194.addItem(self.horizontalSpacer_187)

        self.label_5 = QLabel(self.page_8)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 35))

        self.horizontalLayout_194.addWidget(self.label_5, 0, Qt.AlignmentFlag.AlignRight)


        self.page8Layout1.addLayout(self.horizontalLayout_194)

        self.verticalSpacer_24 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.page8Layout1.addItem(self.verticalSpacer_24)

        self.stackedWidget_2.addWidget(self.page_8)
        self.page_9 = QWidget()
        self.page_9.setObjectName(u"page_9")
        self.page9Layout1 = QVBoxLayout(self.page_9)
        self.page9Layout1.setObjectName(u"page9Layout1")
        self.page9Label1 = QLabel(self.page_9)
        self.page9Label1.setObjectName(u"page9Label1")
        self.page9Label1.setFont(font1)

        self.page9Layout1.addWidget(self.page9Label1)

        self.stackedWidget_2.addWidget(self.page_9)

        self.verticalLayout_14.addWidget(self.stackedWidget_2)

        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        font10 = QFont()
        font10.setFamilies([u"MS Shell Dlg 2"])
        font10.setPointSize(20)
        font10.setBold(True)
        self.tab_4.setFont(font10)
        self.verticalLayout_15 = QVBoxLayout(self.tab_4)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.stackedWidget_3 = QStackedWidget(self.tab_4)
        self.stackedWidget_3.setObjectName(u"stackedWidget_3")
        self.page_10 = QWidget()
        self.page_10.setObjectName(u"page_10")
        self.verticalLayout_19 = QVBoxLayout(self.page_10)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalSpacer_38 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_19.addItem(self.verticalSpacer_38)

        self.horizontalLayout_59 = QHBoxLayout()
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.label_axis = QLabel(self.page_10)
        self.label_axis.setObjectName(u"label_axis")

        self.horizontalLayout_59.addWidget(self.label_axis, 0, Qt.AlignmentFlag.AlignRight)

        self.comboBox_axis = QComboBox(self.page_10)
        self.comboBox_axis.setObjectName(u"comboBox_axis")
        sizePolicy4.setHeightForWidth(self.comboBox_axis.sizePolicy().hasHeightForWidth())
        self.comboBox_axis.setSizePolicy(sizePolicy4)
        self.comboBox_axis.setMinimumSize(QSize(170, 35))

        self.horizontalLayout_59.addWidget(self.comboBox_axis, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_19.addLayout(self.horizontalLayout_59)

        self.verticalSpacer_31 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_19.addItem(self.verticalSpacer_31)

        self.horizontalLayout_60 = QHBoxLayout()
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.label_offsetNo = QLabel(self.page_10)
        self.label_offsetNo.setObjectName(u"label_offsetNo")

        self.horizontalLayout_60.addWidget(self.label_offsetNo, 0, Qt.AlignmentFlag.AlignRight)

        self.lineEdit_offsetNo = QLineEdit(self.page_10)
        self.lineEdit_offsetNo.setObjectName(u"lineEdit_offsetNo")
        self.lineEdit_offsetNo.setMinimumSize(QSize(170, 35))

        self.horizontalLayout_60.addWidget(self.lineEdit_offsetNo, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_19.addLayout(self.horizontalLayout_60)

        self.verticalSpacer_57 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_19.addItem(self.verticalSpacer_57)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.label_upperOffsetLimit = QLabel(self.page_10)
        self.label_upperOffsetLimit.setObjectName(u"label_upperOffsetLimit")

        self.horizontalLayout_29.addWidget(self.label_upperOffsetLimit, 0, Qt.AlignmentFlag.AlignRight)

        self.lineEdit_upperOffcetLimit = QLineEdit(self.page_10)
        self.lineEdit_upperOffcetLimit.setObjectName(u"lineEdit_upperOffcetLimit")
        self.lineEdit_upperOffcetLimit.setMinimumSize(QSize(170, 35))

        self.horizontalLayout_29.addWidget(self.lineEdit_upperOffcetLimit, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_19.addLayout(self.horizontalLayout_29)

        self.verticalSpacer_40 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_19.addItem(self.verticalSpacer_40)

        self.horizontalLayout_64 = QHBoxLayout()
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.horizontalSpacer_22 = QSpacerItem(195, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_64.addItem(self.horizontalSpacer_22)

        self.label_lowerOffsetLimit = QLabel(self.page_10)
        self.label_lowerOffsetLimit.setObjectName(u"label_lowerOffsetLimit")

        self.horizontalLayout_64.addWidget(self.label_lowerOffsetLimit, 0, Qt.AlignmentFlag.AlignRight)

        self.lineEdit_lowerOffsetLimit = QLineEdit(self.page_10)
        self.lineEdit_lowerOffsetLimit.setObjectName(u"lineEdit_lowerOffsetLimit")
        self.lineEdit_lowerOffsetLimit.setMinimumSize(QSize(170, 35))

        self.horizontalLayout_64.addWidget(self.lineEdit_lowerOffsetLimit)

        self.horizontalSpacer_94 = QSpacerItem(80, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_64.addItem(self.horizontalSpacer_94)

        self.label_7 = QLabel(self.page_10)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(55, 16777215))
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_64.addWidget(self.label_7, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_19.addLayout(self.horizontalLayout_64)

        self.verticalSpacer_27 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_19.addItem(self.verticalSpacer_27)

        self.stackedWidget_3.addWidget(self.page_10)
        self.page_11 = QWidget()
        self.page_11.setObjectName(u"page_11")
        self.verticalLayout_20 = QVBoxLayout(self.page_11)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalSpacer_52 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_20.addItem(self.verticalSpacer_52)

        self.horizontalLayout_71 = QHBoxLayout()
        self.horizontalLayout_71.setObjectName(u"horizontalLayout_71")
        self.label_machine = QLabel(self.page_11)
        self.label_machine.setObjectName(u"label_machine")

        self.horizontalLayout_71.addWidget(self.label_machine, 0, Qt.AlignmentFlag.AlignRight)

        self.comboBox_machine = QComboBox(self.page_11)
        self.comboBox_machine.setObjectName(u"comboBox_machine")
        self.comboBox_machine.setMinimumSize(QSize(170, 35))

        self.horizontalLayout_71.addWidget(self.comboBox_machine, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_20.addLayout(self.horizontalLayout_71)

        self.verticalSpacer_58 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_20.addItem(self.verticalSpacer_58)

        self.horizontalLayout_65 = QHBoxLayout()
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.label_direction = QLabel(self.page_11)
        self.label_direction.setObjectName(u"label_direction")

        self.horizontalLayout_65.addWidget(self.label_direction, 0, Qt.AlignmentFlag.AlignRight)

        self.comboBox_direction = QComboBox(self.page_11)
        self.comboBox_direction.addItem("")
        self.comboBox_direction.addItem("")
        self.comboBox_direction.setObjectName(u"comboBox_direction")
        sizePolicy4.setHeightForWidth(self.comboBox_direction.sizePolicy().hasHeightForWidth())
        self.comboBox_direction.setSizePolicy(sizePolicy4)
        self.comboBox_direction.setMinimumSize(QSize(170, 35))

        self.horizontalLayout_65.addWidget(self.comboBox_direction, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_20.addLayout(self.horizontalLayout_65)

        self.verticalSpacer_61 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_20.addItem(self.verticalSpacer_61)

        self.horizontalLayout_66 = QHBoxLayout()
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.label_turretNo = QLabel(self.page_11)
        self.label_turretNo.setObjectName(u"label_turretNo")

        self.horizontalLayout_66.addWidget(self.label_turretNo, 0, Qt.AlignmentFlag.AlignRight)

        self.lineEdit_turretNo = QLineEdit(self.page_11)
        self.lineEdit_turretNo.setObjectName(u"lineEdit_turretNo")
        self.lineEdit_turretNo.setMinimumSize(QSize(170, 35))

        self.horizontalLayout_66.addWidget(self.lineEdit_turretNo, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_20.addLayout(self.horizontalLayout_66)

        self.verticalSpacer_63 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_20.addItem(self.verticalSpacer_63)

        self.horizontalLayout_67 = QHBoxLayout()
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.horizontalSpacer_95 = QSpacerItem(223, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_67.addItem(self.horizontalSpacer_95)

        self.label_bufferpartNo = QLabel(self.page_11)
        self.label_bufferpartNo.setObjectName(u"label_bufferpartNo")

        self.horizontalLayout_67.addWidget(self.label_bufferpartNo, 0, Qt.AlignmentFlag.AlignRight)

        self.lineEdit_bufferPartNo = QLineEdit(self.page_11)
        self.lineEdit_bufferPartNo.setObjectName(u"lineEdit_bufferPartNo")
        self.lineEdit_bufferPartNo.setMinimumSize(QSize(170, 35))

        self.horizontalLayout_67.addWidget(self.lineEdit_bufferPartNo, 0, Qt.AlignmentFlag.AlignLeft)

        self.horizontalSpacer_96 = QSpacerItem(50, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_67.addItem(self.horizontalSpacer_96)

        self.label_11 = QLabel(self.page_11)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMaximumSize(QSize(80, 16777215))
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_67.addWidget(self.label_11, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_20.addLayout(self.horizontalLayout_67)

        self.verticalSpacer_56 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_20.addItem(self.verticalSpacer_56)

        self.stackedWidget_3.addWidget(self.page_11)

        self.verticalLayout_15.addWidget(self.stackedWidget_3)

        self.tabWidget_2.addTab(self.tab_4, "")

        self.verticalLayout_12.addWidget(self.tabWidget_2)


        self.page31Layout.addLayout(self.verticalLayout_12)

        self.stackedWidget_main.addWidget(self.page31)
        self.page_12 = QWidget()
        self.page_12.setObjectName(u"page_12")
        self.verticalLayout_21 = QVBoxLayout(self.page_12)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.horizontalLayout_69 = QHBoxLayout()
        self.horizontalLayout_69.setObjectName(u"horizontalLayout_69")
        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.label_8 = QLabel(self.page_12)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_22.addWidget(self.label_8, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.horizontalLayout_69.addLayout(self.verticalLayout_22)

        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")

        self.horizontalLayout_69.addLayout(self.verticalLayout_23)


        self.verticalLayout_21.addLayout(self.horizontalLayout_69)

        self.horizontalLayout_70 = QHBoxLayout()
        self.horizontalLayout_70.setObjectName(u"horizontalLayout_70")
        self.verticalLayout_27 = QVBoxLayout()
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")

        self.horizontalLayout_70.addLayout(self.verticalLayout_27)

        self.verticalLayout_26 = QVBoxLayout()
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")

        self.horizontalLayout_70.addLayout(self.verticalLayout_26)


        self.verticalLayout_21.addLayout(self.horizontalLayout_70)

        self.stackedWidget_main.addWidget(self.page_12)

        self.verticalLayout.addWidget(self.stackedWidget_main)

        self.line_header = QFrame(self.centralwidget)
        self.line_header.setObjectName(u"line_header")
        self.line_header.setMinimumSize(QSize(0, 2))
        self.line_header.setMaximumSize(QSize(16777215, 16777215))
        self.line_header.setFrameShape(QFrame.Shape.HLine)
        self.line_header.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_header)

        self.Footerwidget = QWidget(self.centralwidget)
        self.Footerwidget.setObjectName(u"Footerwidget")
        self.Footerwidget.setMinimumSize(QSize(0, 40))
        self.Footerwidget.setMaximumSize(QSize(16777215, 16777215))
        self.Footerwidget.setFont(font1)
        self.horizontalLayout_63 = QHBoxLayout(self.Footerwidget)
        self.horizontalLayout_63.setSpacing(4)
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.horizontalLayout_63.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_14 = QSpacerItem(20, 35, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_63.addItem(self.horizontalSpacer_14)

        self.button_shutdown = QPushButton(self.Footerwidget)
        self.button_shutdown.setObjectName(u"button_shutdown")
        sizePolicy3.setHeightForWidth(self.button_shutdown.sizePolicy().hasHeightForWidth())
        self.button_shutdown.setSizePolicy(sizePolicy3)
        self.button_shutdown.setMinimumSize(QSize(0, 35))
        self.button_shutdown.setMaximumSize(QSize(16777215, 16777215))
        icon8 = QIcon()
        icon8.addFile(u"/home/torizon/app/src/images/power-button.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_shutdown.setIcon(icon8)
        self.button_shutdown.setIconSize(QSize(50, 30))

        self.horizontalLayout_63.addWidget(self.button_shutdown)

        self.horizontalSpacer_88 = QSpacerItem(5, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_63.addItem(self.horizontalSpacer_88)

        self.button_back = QPushButton(self.Footerwidget)
        self.button_back.setObjectName(u"button_back")
        sizePolicy.setHeightForWidth(self.button_back.sizePolicy().hasHeightForWidth())
        self.button_back.setSizePolicy(sizePolicy)
        self.button_back.setMinimumSize(QSize(50, 35))
        self.button_back.setMaximumSize(QSize(16777215, 16777215))
        self.button_back.setFont(font1)
        icon9 = QIcon()
        icon9.addFile(u"/home/torizon/app/src/images/Back_Yellow.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_back.setIcon(icon9)
        self.button_back.setIconSize(QSize(50, 30))

        self.horizontalLayout_63.addWidget(self.button_back)

        self.horizontalSpacer_89 = QSpacerItem(5, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_63.addItem(self.horizontalSpacer_89)

        self.button_spcReset = QPushButton(self.Footerwidget)
        self.button_spcReset.setObjectName(u"button_spcReset")
        sizePolicy3.setHeightForWidth(self.button_spcReset.sizePolicy().hasHeightForWidth())
        self.button_spcReset.setSizePolicy(sizePolicy3)
        self.button_spcReset.setMinimumSize(QSize(60, 35))
        self.button_spcReset.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_63.addWidget(self.button_spcReset)

        self.horizontalSpacer_91 = QSpacerItem(5, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_63.addItem(self.horizontalSpacer_91)

        self.label_savesignal = QLabel(self.Footerwidget)
        self.label_savesignal.setObjectName(u"label_savesignal")
        self.label_savesignal.setPixmap(QPixmap(u"/home/torizon/app/src/images/green35.png"))

        self.horizontalLayout_63.addWidget(self.label_savesignal)

        self.horizontalSpacer = QSpacerItem(20, 35, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_63.addItem(self.horizontalSpacer)

        self.button_forward = QPushButton(self.Footerwidget)
        self.button_forward.setObjectName(u"button_forward")
        sizePolicy3.setHeightForWidth(self.button_forward.sizePolicy().hasHeightForWidth())
        self.button_forward.setSizePolicy(sizePolicy3)
        self.button_forward.setMinimumSize(QSize(0, 35))
        self.button_forward.setMaximumSize(QSize(16777215, 16777215))
        icon10 = QIcon()
        icon10.addFile(u"/home/torizon/app/src/images/forward_Yellow.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_forward.setIcon(icon10)
        self.button_forward.setIconSize(QSize(50, 30))

        self.horizontalLayout_63.addWidget(self.button_forward)

        self.horizontalSpacer_87 = QSpacerItem(5, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_63.addItem(self.horizontalSpacer_87)

        self.button_save = QPushButton(self.Footerwidget)
        self.button_save.setObjectName(u"button_save")
        sizePolicy.setHeightForWidth(self.button_save.sizePolicy().hasHeightForWidth())
        self.button_save.setSizePolicy(sizePolicy)
        self.button_save.setMinimumSize(QSize(50, 35))
        self.button_save.setMaximumSize(QSize(16777215, 16777215))
        self.button_save.setFont(font1)
        icon11 = QIcon()
        icon11.addFile(u"/home/torizon/app/src/images/Save_Icon_Yellow.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_save.setIcon(icon11)
        self.button_save.setIconSize(QSize(50, 30))

        self.horizontalLayout_63.addWidget(self.button_save)

        self.horizontalSpacer_86 = QSpacerItem(5, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_63.addItem(self.horizontalSpacer_86)

        self.button_home = QPushButton(self.Footerwidget)
        self.button_home.setObjectName(u"button_home")
        sizePolicy3.setHeightForWidth(self.button_home.sizePolicy().hasHeightForWidth())
        self.button_home.setSizePolicy(sizePolicy3)
        self.button_home.setMinimumSize(QSize(50, 35))
        self.button_home.setMaximumSize(QSize(16777215, 16777215))
        icon12 = QIcon()
        icon12.addFile(u"/home/torizon/app/src/images/Home_Icon_Yellow.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_home.setIcon(icon12)
        self.button_home.setIconSize(QSize(50, 30))

        self.horizontalLayout_63.addWidget(self.button_home)

        self.horizontalSpacer_121 = QSpacerItem(20, 35, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_63.addItem(self.horizontalSpacer_121)


        self.verticalLayout.addWidget(self.Footerwidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget_main.setCurrentIndex(12)
        self.tabWidget.setCurrentIndex(1)
        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(4)
        self.stackedWidget_3.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Quad-PreciGo", None))
        self.label_pageName.setText(QCoreApplication.translate("MainWindow", u"Octo-PreciGo", None))
        self.label_statusBar.setText(QCoreApplication.translate("MainWindow", u"........Saving........", None))
        self.label_date.setText(QCoreApplication.translate("MainWindow", u"14-08-2025", None))
        self.label_time.setText(QCoreApplication.translate("MainWindow", u"10:10:10", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"    Welcome To Octo-PreciGo !!!", None))
        self.label_username.setText(QCoreApplication.translate("MainWindow", u"  Username   :  ", None))
        self.label_password.setText(QCoreApplication.translate("MainWindow", u"  Password   :  ", None))
        self.button_login.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.button_addLoginDetails.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.button_modifyLogin.setText(QCoreApplication.translate("MainWindow", u"Modify", None))
        self.button_deleteLogin.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.label_setUsernameLogin.setText(QCoreApplication.translate("MainWindow", u"Set Username :", None))
        self.label_setPasswordLogin.setText(QCoreApplication.translate("MainWindow", u"  Set Password :", None))
        self.label_setAccessLogin.setText(QCoreApplication.translate("MainWindow", u"   Set Access Type :", None))
        self.comboBox_setAccessCombo.setItemText(0, QCoreApplication.translate("MainWindow", u"Admin", None))
        self.comboBox_setAccessCombo.setItemText(1, QCoreApplication.translate("MainWindow", u"Guest", None))

        self.button_addUpdateLogin.setText(QCoreApplication.translate("MainWindow", u"Add/Modify", None))
        self.label_rs232.setText(QCoreApplication.translate("MainWindow", u"RS232  :", None))
        self.toggleButton_rs232.setText("")
        self.label_baudRate.setText(QCoreApplication.translate("MainWindow", u" Baud Rate  :", None))
        self.comboBox_baudRate.setItemText(0, QCoreApplication.translate("MainWindow", u"4800", None))
        self.comboBox_baudRate.setItemText(1, QCoreApplication.translate("MainWindow", u"9600", None))
        self.comboBox_baudRate.setItemText(2, QCoreApplication.translate("MainWindow", u"19200", None))
        self.comboBox_baudRate.setItemText(3, QCoreApplication.translate("MainWindow", u"56000", None))
        self.comboBox_baudRate.setItemText(4, QCoreApplication.translate("MainWindow", u"115200", None))

        self.label_dataBits.setText(QCoreApplication.translate("MainWindow", u"    Data Bits  :", None))
        self.comboBox_dataBits.setItemText(0, QCoreApplication.translate("MainWindow", u"5", None))
        self.comboBox_dataBits.setItemText(1, QCoreApplication.translate("MainWindow", u"6", None))
        self.comboBox_dataBits.setItemText(2, QCoreApplication.translate("MainWindow", u"7", None))
        self.comboBox_dataBits.setItemText(3, QCoreApplication.translate("MainWindow", u"8", None))

        self.label_parity.setText(QCoreApplication.translate("MainWindow", u"           Parity  :", None))
        self.comboBox_parity.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))
        self.comboBox_parity.setItemText(1, QCoreApplication.translate("MainWindow", u"Odd", None))
        self.comboBox_parity.setItemText(2, QCoreApplication.translate("MainWindow", u"Even", None))
        self.comboBox_parity.setItemText(3, QCoreApplication.translate("MainWindow", u"Mark", None))
        self.comboBox_parity.setItemText(4, QCoreApplication.translate("MainWindow", u"Space", None))

        self.label_stopBits.setText(QCoreApplication.translate("MainWindow", u"   Stop Bits  :", None))
        self.comboBox_stopBits.setItemText(0, QCoreApplication.translate("MainWindow", u"One", None))
        self.comboBox_stopBits.setItemText(1, QCoreApplication.translate("MainWindow", u"Two", None))
        self.comboBox_stopBits.setItemText(2, QCoreApplication.translate("MainWindow", u"OnePointFive", None))

        self.label_flowControl.setText(QCoreApplication.translate("MainWindow", u"Flow Control  :", None))
        self.comboBox_flowControl.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))
        self.comboBox_flowControl.setItemText(1, QCoreApplication.translate("MainWindow", u"RTS/CTS", None))
        self.comboBox_flowControl.setItemText(2, QCoreApplication.translate("MainWindow", u"XOnXOff", None))

        self.label_portName.setText(QCoreApplication.translate("MainWindow", u"  Port Name  :", None))
        self.label_dimensionFormulaBar.setText(QCoreApplication.translate("MainWindow", u"D1  :", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Probe To Add :", None))
        self.comboBox_probeFormulaBar.setItemText(0, QCoreApplication.translate("MainWindow", u"P1", None))
        self.comboBox_probeFormulaBar.setItemText(1, QCoreApplication.translate("MainWindow", u"P2", None))
        self.comboBox_probeFormulaBar.setItemText(2, QCoreApplication.translate("MainWindow", u"P3", None))
        self.comboBox_probeFormulaBar.setItemText(3, QCoreApplication.translate("MainWindow", u"P4", None))
        self.comboBox_probeFormulaBar.setItemText(4, QCoreApplication.translate("MainWindow", u"P5", None))
        self.comboBox_probeFormulaBar.setItemText(5, QCoreApplication.translate("MainWindow", u"P6", None))
        self.comboBox_probeFormulaBar.setItemText(6, QCoreApplication.translate("MainWindow", u"P7", None))
        self.comboBox_probeFormulaBar.setItemText(7, QCoreApplication.translate("MainWindow", u"P8", None))

        self.comboBox_dimenstionFormulaBar.setItemText(0, QCoreApplication.translate("MainWindow", u"D1", None))
        self.comboBox_dimenstionFormulaBar.setItemText(1, QCoreApplication.translate("MainWindow", u"D2", None))
        self.comboBox_dimenstionFormulaBar.setItemText(2, QCoreApplication.translate("MainWindow", u"D3", None))
        self.comboBox_dimenstionFormulaBar.setItemText(3, QCoreApplication.translate("MainWindow", u"D4", None))
        self.comboBox_dimenstionFormulaBar.setItemText(4, QCoreApplication.translate("MainWindow", u"D5", None))
        self.comboBox_dimenstionFormulaBar.setItemText(5, QCoreApplication.translate("MainWindow", u"D6", None))
        self.comboBox_dimenstionFormulaBar.setItemText(6, QCoreApplication.translate("MainWindow", u"D7", None))
        self.comboBox_dimenstionFormulaBar.setItemText(7, QCoreApplication.translate("MainWindow", u"D8", None))

        self.button_addFormulaBar.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.button_featureModeFormulaBar.setText(QCoreApplication.translate("MainWindow", u"Advanced", None))
        self.button_plusFormulaBar.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.button_minusFormulaBar.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.button_multiplicationFormulaBar.setText(QCoreApplication.translate("MainWindow", u"*", None))
        self.button_divisionFormulaBar.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.button_modFormulaBar.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.button_commaFormulaBar.setText(QCoreApplication.translate("MainWindow", u",", None))
        self.button_backspaceFormulaBar.setText(QCoreApplication.translate("MainWindow", u"<-", None))
        self.button_1FormulaBar.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.button_2FormulaBar.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.button_3FormulaBar.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.button_4FormulaBar.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.button_5FormulaBar.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.button_6FormulaBar.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.button_7FormulaBar.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.button_8FormulaBar.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.button_9FormulaBar.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.button_0FormulaBar.setText(QCoreApplication.translate("MainWindow", u"0", None))
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
        self.radioButton_okBuzzer.setText(QCoreApplication.translate("MainWindow", u"Ok", None))
        self.radioButton_reworkNotokBuzzer.setText(QCoreApplication.translate("MainWindow", u"Rework / Not Ok", None))
        self.label_relay.setText(QCoreApplication.translate("MainWindow", u"Relay  :                     ", None))
        self.toggelButton_relay.setText("")
        self.label_relayTime.setText(QCoreApplication.translate("MainWindow", u"   Relay Time  :", None))
        self.label_cycleStopTimer.setText(QCoreApplication.translate("MainWindow", u"Cycle Stop Timer  :   ", None))
        self.toggelButton_cycleStopTimer.setText("")
        self.label_cycleTime.setText(QCoreApplication.translate("MainWindow", u"    Cycle Time  :", None))
        self.label_autoSaveReading.setText(QCoreApplication.translate("MainWindow", u"Auto Save Reading  :", None))
        self.toggelButton_autoSaveReading.setText("")
        self.label_partTraceability.setText(QCoreApplication.translate("MainWindow", u"Part Traceability  :     ", None))
        self.toggelButton_partTraceability.setText("")
        self.radioButton_manualPartTraceability.setText(QCoreApplication.translate("MainWindow", u"Manual Reset", None))
        self.radioButton_autoPartTraceability.setText(QCoreApplication.translate("MainWindow", u"Auto Reset", None))
        self.label_timeToMasterSet.setText(QCoreApplication.translate("MainWindow", u"Time To Master Set  :", None))
        self.toggleButtontimeToSetMaster.setText("")
        self.label_hrs.setText(QCoreApplication.translate("MainWindow", u"Sec", None))
        self.label_masterGrouping.setText(QCoreApplication.translate("MainWindow", u"Master Grouping  :   ", None))
        self.toggleButton_masterGrouping.setText("")
        self.label_SaveMasterCalibration.setText(QCoreApplication.translate("MainWindow", u"Save Master Calibration :", None))
        self.toggleButtonSaveMasterCalibration.setText("")
        self.button_factoryCalibration.setText(QCoreApplication.translate("MainWindow", u"Factory Calibration", None))
        self.button_touchCalibration.setText(QCoreApplication.translate("MainWindow", u"Touch Calibration", None))
        self.button_databaseSettings.setText(QCoreApplication.translate("MainWindow", u"Database Settings", None))
        self.button_rs232Settings.setText(QCoreApplication.translate("MainWindow", u"RS 232 Settings", None))
        self.button_factoryConfig.setText(QCoreApplication.translate("MainWindow", u"Factory Config", None))
        self.button_ipSettings.setText(QCoreApplication.translate("MainWindow", u"IP Settings", None))
        self.button_wifiSettings.setText(QCoreApplication.translate("MainWindow", u"Wifi Settings", None))
        self.label_productHelp.setText(QCoreApplication.translate("MainWindow", u"Product : Quad-PreciGo", None))
        self.label_intersenseNameHelp.setText(QCoreApplication.translate("MainWindow", u"INTERSENSE TECHNOLOGIES LLP", None))
        self.label_adressHelp.setText(QCoreApplication.translate("MainWindow", u"K-122/2,MIDC Waluj,", None))
        self.label_adressHelp_2.setText(QCoreApplication.translate("MainWindow", u"Chh. Sambhajinagar-431136(M.S.) India", None))
        self.label_emailHelp.setText(QCoreApplication.translate("MainWindow", u"Email : sales@intersense.in", None))
        self.label_supportHelp.setText(QCoreApplication.translate("MainWindow", u"Support : +91 8956029090", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Model Number :", None))
        self.label_ModelNumber.setText(QCoreApplication.translate("MainWindow", u"AG07-P2", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Serial Number :", None))
        self.label_SerialNumber.setText(QCoreApplication.translate("MainWindow", u"310", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Software Version :", None))
        self.label_VersionNumber.setText(QCoreApplication.translate("MainWindow", u"1.0", None))
        self.button_update.setText(QCoreApplication.translate("MainWindow", u"Update Version", None))
        self.label_setDate.setText(QCoreApplication.translate("MainWindow", u"Date  :", None))
        self.label_day.setText(QCoreApplication.translate("MainWindow", u"Day", None))
        self.label_month.setText(QCoreApplication.translate("MainWindow", u"Month", None))
        self.label_year.setText(QCoreApplication.translate("MainWindow", u"Year", None))
        self.label_setTime.setText(QCoreApplication.translate("MainWindow", u"Time  :", None))
        self.label_hours.setText(QCoreApplication.translate("MainWindow", u"Hours", None))
        self.label_minutes.setText(QCoreApplication.translate("MainWindow", u"Minutes", None))
        self.button_setDateTime.setText(QCoreApplication.translate("MainWindow", u"Set Date Time", None))
        self.comboBox_shift3FromTimeAmPm.setItemText(0, QCoreApplication.translate("MainWindow", u"AM", None))
        self.comboBox_shift3FromTimeAmPm.setItemText(1, QCoreApplication.translate("MainWindow", u"PM", None))

        self.comboBox_shift2FromTimeAmPm.setItemText(0, QCoreApplication.translate("MainWindow", u"AM", None))
        self.comboBox_shift2FromTimeAmPm.setItemText(1, QCoreApplication.translate("MainWindow", u"PM", None))

        self.label_shift2.setText(QCoreApplication.translate("MainWindow", u"Shift 2", None))
        self.checkBox_shift2.setText("")
        self.label_shift3.setText(QCoreApplication.translate("MainWindow", u"Shift 3", None))
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
        self.button_setShiftTimings.setText(QCoreApplication.translate("MainWindow", u"Set Shift Timings", None))
        self.label_digitVal1.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_digitStatus1.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_digitVal2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_digitStatus2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_digitVal3.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_digitStatus3.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_digitVal4.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_digitStatus4.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
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
        self.button_cncListAoc.setText(QCoreApplication.translate("MainWindow", u"CNC List", None))
        self.button_reportsAoc.setText(QCoreApplication.translate("MainWindow", u"Reports", None))
        self.label_modelNo.setText(QCoreApplication.translate("MainWindow", u"Model No :", None))
        self.label_serialNo.setText(QCoreApplication.translate("MainWindow", u"Serial No :", None))
        self.label_networkBasedDatabase.setText(QCoreApplication.translate("MainWindow", u"Network Based Database  :", None))
        self.toggleButton_networkBasedDatabase.setText("")
        self.label_driverNameDb.setText(QCoreApplication.translate("MainWindow", u"MS SQL Driver Name  :", None))
        self.label_serverNameDb.setText(QCoreApplication.translate("MainWindow", u"MS SQL Server Name  :", None))
        self.label_databaseNameDb.setText(QCoreApplication.translate("MainWindow", u"MS SQL Database Name  :", None))
        self.label_username_Db.setText(QCoreApplication.translate("MainWindow", u"MS SQL Username  :", None))
        self.label_passwordDb.setText(QCoreApplication.translate("MainWindow", u"MS SQL Password  :", None))
        self.label_deviceName.setText(QCoreApplication.translate("MainWindow", u"Device Name :", None))
        self.label_programIdforSettings_1.setText(QCoreApplication.translate("MainWindow", u"Program Id :", None))
        self.label_programNameSettings_1.setText(QCoreApplication.translate("MainWindow", u"Program Name :", None))
        self.button_staticSettingsForAll_1.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label_probeSetting_1.setText(QCoreApplication.translate("MainWindow", u"Dimension  :", None))
        self.comboBox_toselectProbe_1.setItemText(0, QCoreApplication.translate("MainWindow", u"D1", None))
        self.comboBox_toselectProbe_1.setItemText(1, QCoreApplication.translate("MainWindow", u"D2", None))
        self.comboBox_toselectProbe_1.setItemText(2, QCoreApplication.translate("MainWindow", u"D3", None))
        self.comboBox_toselectProbe_1.setItemText(3, QCoreApplication.translate("MainWindow", u"D4", None))
        self.comboBox_toselectProbe_1.setItemText(4, QCoreApplication.translate("MainWindow", u"D5", None))
        self.comboBox_toselectProbe_1.setItemText(5, QCoreApplication.translate("MainWindow", u"D6", None))
        self.comboBox_toselectProbe_1.setItemText(6, QCoreApplication.translate("MainWindow", u"D7", None))
        self.comboBox_toselectProbe_1.setItemText(7, QCoreApplication.translate("MainWindow", u"D8", None))

        self.label_formula_1.setText(QCoreApplication.translate("MainWindow", u"Formula :", None))
        self.label_formulaBar_1.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.button_setFormulaSettings_1.setText(QCoreApplication.translate("MainWindow", u"Set Formula", None))
        self.label_masterType_1.setText(QCoreApplication.translate("MainWindow", u"Master Type :", None))
        self.comboBox_masterType_1.setItemText(0, QCoreApplication.translate("MainWindow", u"Single Master", None))
        self.comboBox_masterType_1.setItemText(1, QCoreApplication.translate("MainWindow", u"Double Master", None))

        self.label_masterLower_1.setText(QCoreApplication.translate("MainWindow", u"Master Lower :", None))
        self.label_master_1.setText(QCoreApplication.translate("MainWindow", u"Master :", None))
        self.label_masterHigher_1.setText(QCoreApplication.translate("MainWindow", u"Master Higher :", None))
        self.label_upperOffsetLimit_1.setText(QCoreApplication.translate("MainWindow", u"Upper Offset Limit  :", None))
        self.label_usl_1.setText(QCoreApplication.translate("MainWindow", u"USL :", None))
        self.label_ucl_1.setText(QCoreApplication.translate("MainWindow", u"UCL :", None))
        self.label_nominalValue_1.setText(QCoreApplication.translate("MainWindow", u"Nominal Value :", None))
        self.label_lcl_1.setText(QCoreApplication.translate("MainWindow", u"LCL :", None))
        self.label_lsl_1.setText(QCoreApplication.translate("MainWindow", u"LSL :", None))
        self.label_lowerOffsetLimit_1.setText(QCoreApplication.translate("MainWindow", u"Lower Offset Limit :", None))
        self.label_ovality_1.setText(QCoreApplication.translate("MainWindow", u"Ovality :", None))
        self.comboBox_ovalityOnOff_1.setItemText(0, QCoreApplication.translate("MainWindow", u"On", None))
        self.comboBox_ovalityOnOff_1.setItemText(1, QCoreApplication.translate("MainWindow", u"Off", None))

        self.label_range_1.setText(QCoreApplication.translate("MainWindow", u"Range :", None))
        self.label_method_1.setText(QCoreApplication.translate("MainWindow", u"Method :", None))
        self.comboBox_methodProbe_1.setItemText(0, QCoreApplication.translate("MainWindow", u"OD", None))
        self.comboBox_methodProbe_1.setItemText(1, QCoreApplication.translate("MainWindow", u"ID", None))

        self.label_case_1.setText(QCoreApplication.translate("MainWindow", u"Case :", None))
        self.comboBox_caseProbe_1.setItemText(0, QCoreApplication.translate("MainWindow", u"Delta", None))
        self.comboBox_caseProbe_1.setItemText(1, QCoreApplication.translate("MainWindow", u"Min", None))
        self.comboBox_caseProbe_1.setItemText(2, QCoreApplication.translate("MainWindow", u"Max", None))

        self.label_caseT_1.setText(QCoreApplication.translate("MainWindow", u"CaseT :", None))
        self.label_probeSensitivity_1.setText(QCoreApplication.translate("MainWindow", u"Probe Sensitivity :", None))
        self.label_airSensitivityQuotient_1.setText(QCoreApplication.translate("MainWindow", u"Air Sensitivity Quotient  :", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"                            Measurement Settings                           ", None))
        self.label_axis_1.setText(QCoreApplication.translate("MainWindow", u"Axis : ", None))
        self.comboBox_axis_1.setItemText(0, QCoreApplication.translate("MainWindow", u"x", None))
        self.comboBox_axis_1.setItemText(1, QCoreApplication.translate("MainWindow", u"y", None))
        self.comboBox_axis_1.setItemText(2, QCoreApplication.translate("MainWindow", u"z", None))

        self.label_offsetNo_1.setText(QCoreApplication.translate("MainWindow", u"Offset No :", None))
        self.label_machine_1.setText(QCoreApplication.translate("MainWindow", u"Machine :", None))
        self.label_direction_1.setText(QCoreApplication.translate("MainWindow", u"Direction :", None))
        self.comboBox_direction_1.setItemText(0, QCoreApplication.translate("MainWindow", u"p", None))
        self.comboBox_direction_1.setItemText(1, QCoreApplication.translate("MainWindow", u"n", None))

        self.label_turretNo_1.setText(QCoreApplication.translate("MainWindow", u"Turret No :", None))
        self.label_bufferpartNo_1.setText(QCoreApplication.translate("MainWindow", u"Buffer Part No :", None))
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
        self.comboBox_probeCalibrate.setItemText(2, QCoreApplication.translate("MainWindow", u"P3", None))
        self.comboBox_probeCalibrate.setItemText(3, QCoreApplication.translate("MainWindow", u"P4", None))
        self.comboBox_probeCalibrate.setItemText(4, QCoreApplication.translate("MainWindow", u"P5", None))
        self.comboBox_probeCalibrate.setItemText(5, QCoreApplication.translate("MainWindow", u"P6", None))
        self.comboBox_probeCalibrate.setItemText(6, QCoreApplication.translate("MainWindow", u"P7", None))
        self.comboBox_probeCalibrate.setItemText(7, QCoreApplication.translate("MainWindow", u"P8", None))

        self.label_lowerMasterCalibrate.setText(QCoreApplication.translate("MainWindow", u"Lower Master  :", None))
        self.label_higherMasterCalibrate.setText(QCoreApplication.translate("MainWindow", u"Higher Master  :", None))
        self.button_calibrateLower.setText(QCoreApplication.translate("MainWindow", u"Calibrate Lower", None))
        self.button_calibrateHigher.setText(QCoreApplication.translate("MainWindow", u"Calibrate Higher", None))
        self.button_setToFactorySettingsCalibration.setText(QCoreApplication.translate("MainWindow", u"Set To Factory Settings", None))
        self.button_resetToFactorySettingsCalibration.setText(QCoreApplication.translate("MainWindow", u"Reset To Factory Settings", None))
        self.label_airSavingMode.setText(QCoreApplication.translate("MainWindow", u"Air Saving Mode  :", None))
        self.toggleButton_airSavingMode.setText("")
        self.label_airChannel.setText(QCoreApplication.translate("MainWindow", u"Air Channel  :", None))
        self.comboBox_airChannel.setItemText(0, QCoreApplication.translate("MainWindow", u"A1", None))
        self.comboBox_airChannel.setItemText(1, QCoreApplication.translate("MainWindow", u"A2", None))

        self.button_setAirSensitivity.setText(QCoreApplication.translate("MainWindow", u"Set", None))
        self.label_ReportfromDate.setText(QCoreApplication.translate("MainWindow", u"From Date  :", None))
        self.label_ReportfromDateVal.setText(QCoreApplication.translate("MainWindow", u"01-01-2025", None))
        self.pushButton_selectFromDate.setText(QCoreApplication.translate("MainWindow", u"From Date", None))
        self.label_ReportToDate.setText(QCoreApplication.translate("MainWindow", u"  To Date  :", None))
        self.label_ReportToDateVal.setText(QCoreApplication.translate("MainWindow", u"01-01-2025", None))
        self.pushButton_SelectToDate.setText(QCoreApplication.translate("MainWindow", u"To Date", None))
        self.label_programId.setText(QCoreApplication.translate("MainWindow", u"Program Id :", None))
        self.label_dimension.setText(QCoreApplication.translate("MainWindow", u"Dimension : ", None))
        self.button_viewData.setText(QCoreApplication.translate("MainWindow", u"View Data", None))
        self.button_exportData.setText(QCoreApplication.translate("MainWindow", u"Export Data", None))
        self.button_deleteData.setText(QCoreApplication.translate("MainWindow", u"Delete Data", None))
        self.label_dateselectReport.setText(QCoreApplication.translate("MainWindow", u"Date :", None))
        self.label_reportshowdate.setText(QCoreApplication.translate("MainWindow", u"01-01-2025  TO  01-01-2025", None))
        self.label_programIdreport.setText(QCoreApplication.translate("MainWindow", u"Program Id :", None))
        self.label_IdProgramReport.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_DimensionForReport.setText(QCoreApplication.translate("MainWindow", u"Dimension :", None))
        self.label_DimensionIdForReport.setText(QCoreApplication.translate("MainWindow", u"D1", None))
        self.button_ListView.setText(QCoreApplication.translate("MainWindow", u"List View", None))
        self.button_ChartView.setText(QCoreApplication.translate("MainWindow", u"Chart View", None))
        self.button_HistogramChart.setText(QCoreApplication.translate("MainWindow", u"Histogram Chart", None))
        self.label_ioSettingPage.setText("")
        self.label_autoOffsetSettingPage.setText("")
        self.label_dialIndicatorPage.setText("")
        self.label_settingsPage.setText("")
        self.label_reportPage.setText("")
        self.label_clockSettingsPage.setText("")
        self.label_userManagementPage.setText("")
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
        self.label_value1.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.button_mode1.setText(QCoreApplication.translate("MainWindow", u"Dial", None))
        self.label_value2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_status2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.button_mode2.setText(QCoreApplication.translate("MainWindow", u"Dial", None))
        self.label_value3.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_value4.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.button_mode3.setText(QCoreApplication.translate("MainWindow", u"Dial", None))
        self.label_dial1.setText("")
        self.label_needle1.setText("")
        self.label_dial2.setText("")
        self.label_needle2.setText("")
        self.label_dial3.setText("")
        self.label_needle3.setText("")
        self.label_dial4.setText("")
        self.label_needle4.setText("")
        self.label_status1.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_status3.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_status4.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.button_mode4.setText(QCoreApplication.translate("MainWindow", u"Dial", None))
        self.button_angleCalculationSetting.setText(QCoreApplication.translate("MainWindow", u"Angle Calculation ", None))
        self.label_modeForCombineIndividual.setText(QCoreApplication.translate("MainWindow", u"Mode :", None))
        self.radioButton_modeCombine.setText(QCoreApplication.translate("MainWindow", u"Combine", None))
        self.radioButton_modeIndividual.setText(QCoreApplication.translate("MainWindow", u"Individual", None))
        self.label_unitOfMeasurement.setText(QCoreApplication.translate("MainWindow", u"Unit Of Measurement :", None))
        self.radioButton_inch.setText(QCoreApplication.translate("MainWindow", u"inch", None))
        self.radioButton_mm.setText(QCoreApplication.translate("MainWindow", u"mm", None))
        self.label_DurationForAutosave.setText(QCoreApplication.translate("MainWindow", u"Duration For Autosave :", None))
        self.label_Responsiveness.setText(QCoreApplication.translate("MainWindow", u"Responsiveness :", None))
        self.pushButton_autosenseRange.setText(QCoreApplication.translate("MainWindow", u"Autosense Range ", None))
        self.label_angleCalculation.setText(QCoreApplication.translate("MainWindow", u"Angle Calculation :", None))
        self.toggelButton_angleCalculation.setText("")
        self.label_angleCalculationMasterAngle.setText(QCoreApplication.translate("MainWindow", u"Master Angle :", None))
        self.label_angleDegree.setText(QCoreApplication.translate("MainWindow", u"\u00b0", None))
        self.label_angleMin.setText(QCoreApplication.translate("MainWindow", u"'", None))
        self.label_angleSec.setText(QCoreApplication.translate("MainWindow", u"\"", None))
        self.label_positiveTol.setText(QCoreApplication.translate("MainWindow", u"+ Tolerance :", None))
        self.label_tolMin.setText(QCoreApplication.translate("MainWindow", u"'", None))
        self.label_tolSec.setText(QCoreApplication.translate("MainWindow", u"\"", None))
        self.label_negativeTol.setText(QCoreApplication.translate("MainWindow", u"- Tolerance :", None))
        self.label_tolPositiveMin.setText(QCoreApplication.translate("MainWindow", u"'", None))
        self.label_tolPositiveSec.setText(QCoreApplication.translate("MainWindow", u"\"", None))
        self.label_Distance.setText(QCoreApplication.translate("MainWindow", u"Distance :", None))
        self.label_distanceInMm.setText(QCoreApplication.translate("MainWindow", u"mm", None))
        self.label_Angle.setText(QCoreApplication.translate("MainWindow", u"  Angle  :", None))
        self.radioButton_halfAngle.setText(QCoreApplication.translate("MainWindow", u"Half Angle ", None))
        self.radioButton_2_fullAngle.setText(QCoreApplication.translate("MainWindow", u"Full Angle", None))
        self.label_programIdOnSetMaster.setText(QCoreApplication.translate("MainWindow", u"Program Id :", None))
        self.comboBox_programIdSetting_outer.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.comboBox_programIdSetting_outer.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))
        self.comboBox_programIdSetting_outer.setItemText(2, QCoreApplication.translate("MainWindow", u"3", None))
        self.comboBox_programIdSetting_outer.setItemText(3, QCoreApplication.translate("MainWindow", u"4", None))

        self.label_programNamOnSetMAster.setText(QCoreApplication.translate("MainWindow", u"Program Name :    ", None))
        self.label_programName.setText(QCoreApplication.translate("MainWindow", u"DIA 20", None))
        self.label_masterSetting.setText(QCoreApplication.translate("MainWindow", u"Master Setting :", None))
        self.button_setMaster.setText(QCoreApplication.translate("MainWindow", u"Set Master", None))
        self.button_programList.setText(QCoreApplication.translate("MainWindow", u"Program List", None))
        self.button_partSettings.setText(QCoreApplication.translate("MainWindow", u"Part Settings ", None))
        self.label_liveD1Val.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_masterD1_1.setText(QCoreApplication.translate("MainWindow", u"MasterLower D1 :", None))
        self.label_valMasterD1_1.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_masterD1_2.setText(QCoreApplication.translate("MainWindow", u"MasterHigher D1 :", None))
        self.label_valMasterD1_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.masterGroupingChannel_1.setText(QCoreApplication.translate("MainWindow", u"D1", None))
        self.label_liveD2Val.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_masterD2_1.setText(QCoreApplication.translate("MainWindow", u"MasterLower D2 :", None))
        self.label_valMasterD2_1.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_masterD2_2.setText(QCoreApplication.translate("MainWindow", u"MasterHigher D2 :", None))
        self.label_valMasterD2_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.masterGroupingChannel_2.setText(QCoreApplication.translate("MainWindow", u"D2", None))
        self.label_liveD3Val.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_masterD3_1.setText(QCoreApplication.translate("MainWindow", u"MasterLower D3 :", None))
        self.label_valMasterD3_1.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_masterD3_2.setText(QCoreApplication.translate("MainWindow", u"MasterHigher D3 :", None))
        self.label_valMasterD3_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.masterGroupingChannel_3.setText(QCoreApplication.translate("MainWindow", u"D3", None))
        self.label_liveD4val.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_masterD4_1.setText(QCoreApplication.translate("MainWindow", u"MasterLower D4 :", None))
        self.label_valMasterD4_1.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_masterD4_2.setText(QCoreApplication.translate("MainWindow", u"MasterHigher D4 :", None))
        self.label_valMasterD4_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.masterGroupingChannel_4.setText(QCoreApplication.translate("MainWindow", u"D4", None))
        self.label_programIdforSettings.setText(QCoreApplication.translate("MainWindow", u"Program Id:", None))
        self.label_programNameSettings.setText(QCoreApplication.translate("MainWindow", u"Program Name:", None))
        self.button_staticSettingsForAll.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label_probeSetting.setText(QCoreApplication.translate("MainWindow", u"Dimension :", None))
        self.comboBox_toselectProbe.setItemText(0, QCoreApplication.translate("MainWindow", u"D1", None))
        self.comboBox_toselectProbe.setItemText(1, QCoreApplication.translate("MainWindow", u"D2", None))
        self.comboBox_toselectProbe.setItemText(2, QCoreApplication.translate("MainWindow", u"D3", None))
        self.comboBox_toselectProbe.setItemText(3, QCoreApplication.translate("MainWindow", u"D4", None))
        self.comboBox_toselectProbe.setItemText(4, QCoreApplication.translate("MainWindow", u"D5", None))
        self.comboBox_toselectProbe.setItemText(5, QCoreApplication.translate("MainWindow", u"D6", None))
        self.comboBox_toselectProbe.setItemText(6, QCoreApplication.translate("MainWindow", u"D7", None))
        self.comboBox_toselectProbe.setItemText(7, QCoreApplication.translate("MainWindow", u"D8", None))

        self.button_delete.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.label_formula.setText(QCoreApplication.translate("MainWindow", u"Formula :", None))
        self.label_formulaBar.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.button_setFormulaSettings.setText(QCoreApplication.translate("MainWindow", u"Set Formula", None))
        self.label_masterType.setText(QCoreApplication.translate("MainWindow", u"Master Type :", None))
        self.comboBox_masterType.setItemText(0, QCoreApplication.translate("MainWindow", u"Single Master", None))
        self.comboBox_masterType.setItemText(1, QCoreApplication.translate("MainWindow", u"Double Master", None))
        self.comboBox_masterType.setItemText(2, QCoreApplication.translate("MainWindow", u"No Master", None))

        self.label_masterLower.setText(QCoreApplication.translate("MainWindow", u"Master Lower :", None))
        self.label_master.setText(QCoreApplication.translate("MainWindow", u"Master :", None))
        self.label_masterHigher.setText(QCoreApplication.translate("MainWindow", u"Master Higher :", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"1 of 5", None))
        self.label_usl.setText(QCoreApplication.translate("MainWindow", u"USL :", None))
        self.label_ucl.setText(QCoreApplication.translate("MainWindow", u"UCL :", None))
        self.label_nominalValue.setText(QCoreApplication.translate("MainWindow", u"Nominal Value :", None))
        self.label_pageNo.setText(QCoreApplication.translate("MainWindow", u"2 of 5", None))
        self.label_lcl.setText(QCoreApplication.translate("MainWindow", u"LCL :", None))
        self.label_lsl.setText(QCoreApplication.translate("MainWindow", u"LSL :", None))
        self.label_method.setText(QCoreApplication.translate("MainWindow", u"Method :", None))
        self.comboBox_methodProbe.setItemText(0, QCoreApplication.translate("MainWindow", u"ID", None))
        self.comboBox_methodProbe.setItemText(1, QCoreApplication.translate("MainWindow", u"OD", None))

        self.label_2.setText(QCoreApplication.translate("MainWindow", u"3 of 5", None))
        self.label_range.setText(QCoreApplication.translate("MainWindow", u"Dial Range :", None))
        self.comboBox_rangeProbe.setItemText(0, QCoreApplication.translate("MainWindow", u"0.3", None))
        self.comboBox_rangeProbe.setItemText(1, QCoreApplication.translate("MainWindow", u"0.03", None))
        self.comboBox_rangeProbe.setItemText(2, QCoreApplication.translate("MainWindow", u"0.003", None))
        self.comboBox_rangeProbe.setItemText(3, QCoreApplication.translate("MainWindow", u"0.6", None))
        self.comboBox_rangeProbe.setItemText(4, QCoreApplication.translate("MainWindow", u"0.06", None))
        self.comboBox_rangeProbe.setItemText(5, QCoreApplication.translate("MainWindow", u"0.006", None))

        self.label_ovality.setText(QCoreApplication.translate("MainWindow", u"Ovality :", None))
        self.comboBox_ovalityOnOff.setItemText(0, QCoreApplication.translate("MainWindow", u"ON", None))
        self.comboBox_ovalityOnOff.setItemText(1, QCoreApplication.translate("MainWindow", u"OFF", None))

        self.label_case.setText(QCoreApplication.translate("MainWindow", u"Case :", None))
        self.comboBox_caseProbe.setItemText(0, QCoreApplication.translate("MainWindow", u"Delta", None))
        self.comboBox_caseProbe.setItemText(1, QCoreApplication.translate("MainWindow", u"Min", None))
        self.comboBox_caseProbe.setItemText(2, QCoreApplication.translate("MainWindow", u"Max", None))

        self.label_caseT.setText(QCoreApplication.translate("MainWindow", u"CaseT :", None))
        self.label_page4.setText(QCoreApplication.translate("MainWindow", u"4 of 5", None))
        self.label_leastCount.setText(QCoreApplication.translate("MainWindow", u"Least Count :", None))
        self.lineEdit_leastCount.setItemText(0, QCoreApplication.translate("MainWindow", u"0.01", None))
        self.lineEdit_leastCount.setItemText(1, QCoreApplication.translate("MainWindow", u"0.001", None))
        self.lineEdit_leastCount.setItemText(2, QCoreApplication.translate("MainWindow", u"0.0001", None))
        self.lineEdit_leastCount.setItemText(3, QCoreApplication.translate("MainWindow", u"0.00001", None))
        self.lineEdit_leastCount.setItemText(4, QCoreApplication.translate("MainWindow", u"0.005", None))
        self.lineEdit_leastCount.setItemText(5, QCoreApplication.translate("MainWindow", u"0.0005", None))

        self.label_probeSensitivity.setText(QCoreApplication.translate("MainWindow", u"Probe Sensitivity :", None))
        self.label_airSensitivityQuotient.setText(QCoreApplication.translate("MainWindow", u"Air Sensitivity Quotient :", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"5 of 5", None))
        self.page9Label1.setText(QCoreApplication.translate("MainWindow", u"Page 9", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"                            Measurement Settings                           ", None))
        self.label_axis.setText(QCoreApplication.translate("MainWindow", u"Axis :", None))
        self.label_offsetNo.setText(QCoreApplication.translate("MainWindow", u"Offset No. :", None))
        self.label_upperOffsetLimit.setText(QCoreApplication.translate("MainWindow", u"Upper Offset Limit :", None))
        self.label_lowerOffsetLimit.setText(QCoreApplication.translate("MainWindow", u"Lower Offset Limit :", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"1 of 2", None))
        self.label_machine.setText(QCoreApplication.translate("MainWindow", u"Machine :", None))
        self.label_direction.setText(QCoreApplication.translate("MainWindow", u"Direction :", None))
        self.comboBox_direction.setItemText(0, QCoreApplication.translate("MainWindow", u"P (ID)", None))
        self.comboBox_direction.setItemText(1, QCoreApplication.translate("MainWindow", u"N (OD)", None))

        self.label_turretNo.setText(QCoreApplication.translate("MainWindow", u"Turret No. :", None))
        self.label_bufferpartNo.setText(QCoreApplication.translate("MainWindow", u"Buffer Part No. :", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"2 of 2", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"                            AutoCorrection Setting                            ", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Value", None))
        self.button_shutdown.setText("")
        self.button_back.setText("")
        self.button_spcReset.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.label_savesignal.setText("")
        self.button_forward.setText("")
        self.button_save.setText("")
        self.button_home.setText("")
    # retranslateUi

