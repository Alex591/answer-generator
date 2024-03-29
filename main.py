# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow - untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect, QSize, Qt,
                            QTime, QUrl)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                           QFontDatabase, QGradient, QIcon, QImage,
                           QKeySequence, QLinearGradient, QPainter, QPalette,
                           QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGroupBox,
                               QLabel, QLineEdit, QMainWindow, QPushButton,
                               QSizePolicy, QStatusBar, QWidget, QDialog, QInputDialog)

import random

import diskoperations
import powershellwriter
import ui_wifiadder
import wificonfig
# HELPER IMPORTS
import xmlwriter
import handler
import helper
# UI IMPORTS
import ui_programs
import user_chooser
import ui_drivesave


class Ui_WindowsAnswerfile(object):
    def __init__(self) -> None:
        """
        Initalizes the necessary object for Answer File Genereation.
        This includes program returns from QDialog objects
        Main QDialog


        :return: None
        """
        self.programlist = []
        self.drivetosave = ""
        self.users = []
        self.firstlogoncommands = []
        self.wifi = []
        pass

    def filloptions(self) -> None:
        """
        Fills all the Combobox items with options provided in handler.py

        :return: None
        """
        self.win_edition_combo.addItems(handler.getwindowseditions().keys())
        self.win_language_combobox.addItems(handler.alllanguages())
        self.sys_locale_combobox.addItems(handler.alllanguages())
        self.privacy_combobox.addItems(handler.privacysettings())

    def connectbuttons(self) -> None:
        # wifi
        self.program_edit_button_2.clicked.connect(self.openwifi)
        # programs
        self.program_edit_button.clicked.connect(self.openprograms)
        # main generate function
        self.pushButton.clicked.connect(self.opendiskchooser)
        # users
        self.user_edit_button.clicked.connect(self.openusers)

    def generateuser(self) -> None:
        """
        Generates a new random user and appends it to the self.users list

        :return: None
        """
        admin_fullname_list = ["Bob", "Not Admin", "The Boss", "Limitless Power", "Luke Skywalker", "Chili Cheese",
                               "Nikola Tesla", "Cool Admin"]
        randomuser = helper.User("Administrators", "Admin", "admin", random.choice(admin_fullname_list), False)
        self.users.append(randomuser)

    def getfullname(self) -> str:
        # if the user list is empty, wee need to generate a new admin user
        if len(self.users) == 0:
            self.generateuser()
        return self.users[0].fullname

    def setfirstlogoncommands(self) -> None:
        """
        Sets the First logon commands according to if a wifi or preinstalled programs have been added or not
        :return:
        """
        if self.wifi:
            sleep_connect = "cmd.exe C:\connectandsleep.cmd"
            addprofile = "cmd.exe C:\wifi.cmd"
            self.firstlogoncommands.append(addprofile)
            self.firstlogoncommands.append(sleep_connect)

        if self.programlist:
            commandtoadd = "powershell -executionpolicy unrestricted -command Unblock-File C:\chocoinstall.ps1; powershell -command C:\chocoinstall.ps1"
            self.firstlogoncommands.append(commandtoadd)

    def generate_answer_file(self):
        answerfile = xmlwriter.Writer()
        # if HDD checkbox is checked then we need to create a windows partition HDD
        language_code_win = handler.langcode(self.win_language_combobox.currentText())
        language_code_syslocale = handler.langcode(self.sys_locale_combobox.currentText())
        win_edition = self.win_edition_combo.currentText()
        org_name = self.lineEdit_2.text()
        computer_name = self.lineEdit.text()
        if not computer_name:
            computer_name="PENGUIN-PC"
        # For convinience, if the user language and system lang differ,assuming the user wants both keyboard inputs
        if language_code_syslocale != language_code_win:
            input_locale = [language_code_win, language_code_syslocale]
        else:
            input_locale = [language_code_win]

        if self.hdd_checkbox.isChecked():
            winhdd = [helper.HardDrive(wipedisk=True, windowspartition=True)]
            answerfile.add_win_pe_pass(harddrive=winhdd, setuplang=language_code_win, inputlocale=input_locale,
                                       systemlocale=language_code_syslocale, userlocale=language_code_syslocale,
                                       windowsedition=win_edition, fullname=computer_name, organization=org_name,
                                       virtual_machine=self.vm_checkBox.isChecked())
        else:
            answerfile.add_win_pe_pass(setuplang=language_code_win, inputlocale=input_locale,
                                       systemlocale=language_code_syslocale, userlocale=language_code_syslocale,
                                       windowsedition=win_edition, fullname=self.getfullname(), organization=org_name,
                                       virtual_machine=self.vm_checkBox.isChecked())

        answerfile.add_offlineservicing_pass(self.uac_checkbox.isChecked(),self.codeintegrity_checkbox.isChecked())
        self.setfirstlogoncommands()
        if self.wifi:
            wificonfig.WifiNetwork.createcmd(self.wifi)
        powershellwriter.make_and_move(self.programlist)
        protect_diag_level = 3 if self.privacy_combobox.currentText() == "Basic Diagnostics" else 1
        answerfile.add_oobe_pass(users=self.users, do_autologin=self.users[0].autologon, inputlocale=input_locale,
                                 systemlocale=language_code_syslocale, userlocale=language_code_syslocale,
                                 setuplang=language_code_win, firstlogoncommands=self.firstlogoncommands,protectourpc=protect_diag_level)
        answerfile.write()

    def opendiskchooser(self):
        self.generate_answer_file()
        self.window = QDialog()
        self.ui = ui_drivesave.Ui_Dialog()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()
        if self.window.exec() == QDialog.Accepted:
            self.drivetosave = self.ui.drivetosave
            diskoperations.copy_to_oem_folder(self.drivetosave)
            diskoperations.copy_to_sources_folder(f"{self.drivetosave}/")

    # opens the User adder window
    def openusers(self) -> None:
        self.window = QDialog()
        self.ui = user_chooser.Ui_UserAdder()
        self.ui.setupUi(self.window)
        self.window.show()
        if self.window.exec() == QDialog.Accepted:
            self.users.append(self.ui.createduser())
            print(self.ui.createduser())

    # opens the wifi adder window
    def openwifi(self) -> None:
        self.window = QDialog()
        self.ui = ui_wifiadder.Ui_Dialog()
        self.ui.setupUi(self.window)
        self.window.show()
        if self.window.exec() == QDialog.Accepted:
            wifiN=self.ui.wifinetwork()
            wifiN.write()


    # opens the thing
    def openprograms(self) -> None:
        self.window = QDialog()
        self.ui = ui_programs.Ui_Dialog()
        self.ui.setupUi(self.window)
        self.window.show()
        if self.window.exec() == QDialog.Accepted:
            self.programlist = self.ui.program_list

        pass

    def setupUi(self, WindowsAnswerfile):
        if not WindowsAnswerfile.objectName():
            WindowsAnswerfile.setObjectName(u"WindowsAnswerfile")
        WindowsAnswerfile.resize(478, 665)
        WindowsAnswerfile.setMinimumSize(QSize(478, 660))
        WindowsAnswerfile.setMaximumSize(QSize(16777215, 16777215))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        brush1 = QBrush(QColor(240, 240, 240, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        WindowsAnswerfile.setPalette(palette)
        font = QFont()
        WindowsAnswerfile.setFont(font)
        WindowsAnswerfile.setFocusPolicy(Qt.ClickFocus)
        WindowsAnswerfile.setToolTipDuration(3)
        WindowsAnswerfile.setStyleSheet(u".QCheckBox::indicator {\n"
                                        "     width: 14px;\n"
                                        "     height: 14px;\n"
                                        " }")
        self.centralwidget = QWidget(WindowsAnswerfile)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(243, 243, 243);")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(150, 580, 181, 61))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Variable"])
        font1.setUnderline(False)
        font1.setStrikeOut(False)
        self.pushButton.setFont(font1)
        self.pushButton.setStyleSheet(u".QPushButton {\n"
                                      "	background-color:#0069ba;\n"
                                      "	border-radius:9px;\n"
                                      "	border:1px solid #ffffff;\n"
                                      "	display:inline-block;\n"
                                      "	cursor:pointer;\n"
                                      "	color:#ffffff;\n"
                                      "	font-family:Segoe UI Variable;\n"
                                      "	font-size:21px;\n"
                                      "	padding:16px 31px;\n"
                                      "	text-decoration:none;\n"
                                      "}\n"
                                      ".QPushButton:hover {\n"
                                      "	background-color:#1a79c1;\n"
                                      "}\n"
                                      ".QPushButton:active {\n"
                                      "	position:relative;\n"
                                      "	top:1px;\n"
                                      "}\n"
                                      "")
        self.user_edit_button = QPushButton(self.centralwidget)
        self.user_edit_button.setObjectName(u"user_edit_button")
        self.user_edit_button.setGeometry(QRect(250, 510, 181, 31))
        self.user_edit_button.setStyleSheet(u".QPushButton {\n"
                                            "	background-color:#ffffff;\n"
                                            "	border-radius:4px;\n"
                                            "	border:1px solid #8a8886;\n"
                                            "	display:inline-block;\n"
                                            "	cursor:pointer;\n"
                                            "	color:#565555;\n"
                                            "	font-family:Segoe UI Variable;\n"
                                            "	font-weight:bold;\n"
                                            "	font-size:13px;\n"
                                            "	text-decoration:none;\n"
                                            "}\n"
                                            ".QPushButton:hover {\n"
                                            "	background-color:#f3f2f1;\n"
                                            "}\n"
                                            ".QPushButton:active {\n"
                                            "	position:relative;\n"
                                            "	top:1px;\n"
                                            "}")
        self.program_edit_button = QPushButton(self.centralwidget)
        self.program_edit_button.setObjectName(u"program_edit_button")
        self.program_edit_button.setGeometry(QRect(40, 510, 181, 31))
        self.program_edit_button.setStyleSheet(u".QPushButton {\n"
                                               "	background-color:#ffffff;\n"
                                               "	border-radius:4px;\n"
                                               "	border:1px solid #8a8886;\n"
                                               "	display:inline-block;\n"
                                               "	cursor:pointer;\n"
                                               "	color:#565555;\n"
                                               "	font-family:Segoe UI Variable;\n"
                                               "	font-weight:bold;\n"
                                               "	font-size:13px;\n"
                                               "	text-decoration:none;\n"
                                               "}\n"
                                               ".QPushButton:hover {\n"
                                               "	background-color:#f3f2f1;\n"
                                               "}\n"
                                               ".QPushButton:active {\n"
                                               "	position:relative;\n"
                                               "	top:1px;\n"
                                               "}")
        self.vm_checkBox = QCheckBox(self.centralwidget)
        self.vm_checkBox.setObjectName(u"vm_checkBox")
        self.vm_checkBox.setGeometry(QRect(260, 400, 171, 20))
        self.vm_checkBox.setMinimumSize(QSize(0, 0))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI Variable Display Semib"])
        font2.setPointSize(9)
        font2.setBold(True)
        self.vm_checkBox.setFont(font2)
        self.vm_checkBox.setMouseTracking(True)
        # if QT_CONFIG(whatsthis)
        self.vm_checkBox.setWhatsThis(u"")
        # endif // QT_CONFIG(whatsthis)
        self.vm_checkBox.setStyleSheet(u".QCheckBox {\n"
                                       "background-color: #fbfbfb\n"
                                       "}\n"
                                       "")
        self.vm_checkBox.setTristate(False)
        self.win_edition_combo = QComboBox(self.centralwidget)
        self.win_edition_combo.setObjectName(u"win_edition_combo")
        self.win_edition_combo.setGeometry(QRect(170, 50, 241, 22))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI Variable Display"])
        font3.setBold(False)
        self.win_edition_combo.setFont(font3)
        self.win_edition_combo.setStyleSheet(u"/* Main ComboBox Style */\n"
                                             "#win_edition_combo {\n"
                                             "border: 1px solid #d3d3d3;\n"
                                             "border-radius: 4px;\n"
                                             "padding-left: 10px;\n"
                                             "background-color: rgb(254, 254, 254)\n"
                                             "}\n"
                                             "#win_edition_combo:hover{\n"
                                             "background-color: rgb(250, 250, 250)\n"
                                             "}\n"
                                             "/*Dropdown area */\n"
                                             "#win_edition_combo::drop-down{\n"
                                             "	border:0px\n"
                                             "}\n"
                                             "#win_edition_combo::down-arrow{\n"
                                             "image: url('icons/img dark/ComboBoxDisabled.png')\n"
                                             "\n"
                                             "}\n"
                                             "\n"
                                             "#win_edition_combo::on{\n"
                                             "border: 2px solid #c2dbfe\n"
                                             "}\n"
                                             "\n"
                                             "/*listitems*/\n"
                                             "#win_edition_combo QListView{\n"
                                             "	font-size: 9px;\n"
                                             "	padding: 5px;\n"
                                             "	border: 1px solid #d3d3d3;\n"
                                             "	background-color: rgb(250, 250, 250);\n"
                                             "	outline: 0px;\n"
                                             "\n"
                                             "}\n"
                                             "#win_edition_combo QListView::item{\n"
                                             "	padding-left: 10px;\n"
                                             "	background-color: rgb(250, 250, 250);\n"
                                             "}\n"
                                             "#wwin_edition_combo QListView:item:hover{\n"
                                             "	background-color: #1e90ff\n"
                                             "}"
                                             "#win_edition_combo QListView:item:selected{\n"
                                             "	background-color: #1e90ff\n"
                                             "}")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 50, 111, 16))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI Variable Display Semib"])
        font4.setBold(True)
        self.label.setFont(font4)
        self.label.setStyleSheet(u".QLabel {\n"
                                 "background-color: #fbfbfb\n"
                                 "}\n"
                                 "")
        self.hdd_checkbox = QCheckBox(self.centralwidget)
        self.hdd_checkbox.setObjectName(u"hdd_checkbox")
        self.hdd_checkbox.setGeometry(QRect(260, 370, 181, 20))
        self.hdd_checkbox.setFont(font4)
        self.hdd_checkbox.setStyleSheet(u".QCheckBox {\n"
                                        "background-color: #fbfbfb\n"
                                        "}\n"
                                        "")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 90, 111, 16))
        self.label_2.setFont(font4)
        self.label_2.setStyleSheet(u".QLabel {\n"
                                   "background-color: #fbfbfb\n"
                                   "}\n"
                                   "")
        self.win_language_combobox = QComboBox(self.centralwidget)
        self.win_language_combobox.setObjectName(u"win_language_combobox")
        self.win_language_combobox.setGeometry(QRect(170, 90, 241, 22))
        font5 = QFont()
        font5.setFamilies([u"Segoe UI Variable Display"])
        self.win_language_combobox.setFont(font5)
        self.win_language_combobox.setStyleSheet(u"/* Main ComboBox Style */\n"
                                                 "#win_language_combobox {\n"
                                                 "border: 1px solid #d3d3d3;\n"
                                                 "border-radius: 4px;\n"
                                                 "padding-left: 10px;\n"
                                                 "background-color: rgb(254, 254, 254)\n"
                                                 "}\n"
                                                 "#win_language_combobox:hover{\n"
                                                 "background-color: rgb(250, 250, 250)\n"
                                                 "}\n"
                                                 "/*Dropdown area */\n"
                                                 "#win_language_combobox::drop-down{\n"
                                                 "	border:0px\n"
                                                 "}\n"
                                                 "#win_language_combobox::down-arrow{\n"
                                                 "image: url('icons/img dark/ComboBoxDisabled.png')\n"
                                                 "\n"
                                                 "}\n"
                                                 "\n"
                                                 "#win_language_combobox::on{\n"
                                                 "border: 2px solid #c2dbfe\n"
                                                 "}\n"
                                                 "\n"
                                                 "/*listitems*/\n"
                                                 "#win_language_combobox QListView{\n"
                                                 "	font-size: 9px;\n"
                                                 "	padding: 5px;\n"
                                                 "	border: 1px solid #d3d3d3;\n"
                                                 "	background-color: rgb(250, 250, 250);\n"
                                                 "	outline: 0px;\n"
                                                 "\n"
                                                 "}\n"
                                                 "#win_language_combobox QListView::item{\n"
                                                 "	padding-left: 10px;\n"
                                                 "	background-color: rgb(250, 250, 250);\n"
                                                 "}\n"
                                                 "#win_language_combobox QListView:item:hover{\n"
                                                 "	background-color: #1e90ff\n"
                                                 "}"
                                                 "#win_language_combobox QListView:item:selected{\n"
                                                 "	background-color: #1e90ff\n"
                                                 "}")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(40, 370, 101, 16))
        self.label_4.setFont(font4)
        self.label_4.setStyleSheet(u".QLabel {\n"
                                   "background-color: #fbfbfb\n"
                                   "}\n"
                                   "")
        self.uac_checkbox = QCheckBox(self.centralwidget)
        self.uac_checkbox.setObjectName(u"uac_checkbox")
        self.uac_checkbox.setGeometry(QRect(170, 370, 31, 20))
        self.uac_checkbox.setMouseTracking(True)
        # if QT_CONFIG(whatsthis)
        self.uac_checkbox.setWhatsThis(u"")
        # endif // QT_CONFIG(whatsthis)
        self.uac_checkbox.setStyleSheet(u".QCheckBox {\n"
                                        "background-color: #fbfbfb\n"
                                        "}\n"
                                        "")
        self.uac_checkbox.setTristate(False)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(40, 400, 121, 16))
        self.label_5.setFont(font4)
        self.label_5.setStyleSheet(u".QLabel {\n"
                                   "background-color: #fbfbfb\n"
                                   "}\n"
                                   "")
        self.codeintegrity_checkbox = QCheckBox(self.centralwidget)
        self.codeintegrity_checkbox.setObjectName(u"codeintegrity_checkbox")
        self.codeintegrity_checkbox.setGeometry(QRect(170, 400, 31, 20))
        self.codeintegrity_checkbox.setMouseTracking(True)
        # if QT_CONFIG(whatsthis)
        self.codeintegrity_checkbox.setWhatsThis(u"")
        # endif // QT_CONFIG(whatsthis)
        self.codeintegrity_checkbox.setStyleSheet(u".QCheckBox {\n"
                                                  "background-color: #fbfbfb\n"
                                                  "}\n"
                                                  "")
        self.codeintegrity_checkbox.setTristate(False)
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(30, 20, 421, 281))
        self.groupBox.setStyleSheet(u".QGroupBox {\n"
                                    "border: 1px solid #e5e5e5;\n"
                                    "border-radius: 6px;\n"
                                    "background-color: #fbfbfb\n"
                                    "}\n"
                                    "")
        self.lineEdit_2 = QLineEdit(self.groupBox)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(140, 200, 241, 22))
        self.lineEdit_2.setFont(font5)
        self.lineEdit_2.setStyleSheet(u".QLineEdit {\n"
                                      "border: 1px solid #d3d3d3;\n"
                                      "border-radius: 4px;\n"
                                      "padding-left: 10px;\n"
                                      "background-color: rgb(254, 254, 254)\n"
                                      "}\n"
                                      ".QLineEdit:hover{\n"
                                      "background-color: rgb(250, 250, 250)\n"
                                      "}")
        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 160, 101, 16))
        self.label_6.setFont(font4)
        self.label_6.setStyleSheet(u".QLabel {\n"
                                   "background-color: #fbfbfb\n"
                                   "}\n"
                                   "")
        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 200, 111, 16))
        self.label_7.setFont(font4)
        self.label_7.setStyleSheet(u".QLabel {\n"
                                   "background-color: #fbfbfb\n"
                                   "}\n"
                                   "")
        self.lineEdit = QLineEdit(self.groupBox)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(140, 160, 241, 22))
        self.lineEdit.setFont(font5)
        self.lineEdit.setStyleSheet(u".QLineEdit {\n"
                                    "border: 1px solid #d3d3d3;\n"
                                    "border-radius: 4px;\n"
                                    "padding-left: 10px;\n"
                                    "background-color: rgb(254, 254, 254)\n"
                                    "}\n"
                                    ".QLineEdit:hover{\n"
                                    "background-color: rgb(250, 250, 250)\n"
                                    "}")
        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(20, 120, 111, 16))
        self.label_8.setFont(font4)
        self.label_8.setStyleSheet(u".QLabel {\n"
                                   "background-color: #fbfbfb\n"
                                   "}\n"
                                   "")
        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(20, 240, 101, 16))
        self.label_9.setFont(font4)
        self.label_9.setStyleSheet(u".QLabel {\n"
                                   "background-color: #fbfbfb\n"
                                   "}\n"
                                   "")
        self.privacy_combobox = QComboBox(self.groupBox)
        self.privacy_combobox.setObjectName(u"privacy_combobox")
        self.privacy_combobox.setGeometry(QRect(140, 240, 241, 22))
        self.privacy_combobox.setFont(font5)
        self.privacy_combobox.setStyleSheet(u"/* Main ComboBox Style */\n"
                                            "#privacy_combobox {\n"
                                            "border: 1px solid #d3d3d3;\n"
                                            "border-radius: 4px;\n"
                                            "padding-left: 10px;\n"
                                            "background-color: rgb(254, 254, 254)\n"
                                            "}\n"
                                            "#privacy_combobox:hover{\n"
                                            "background-color: rgb(250, 250, 250)\n"
                                            "}\n"
                                            "/*Dropdown area */\n"
                                            "#privacy_combobox::drop-down{\n"
                                            "	border:0px\n"
                                            "}\n"
                                            "#privacy_combobox::down-arrow{\n"
                                            "image: url('icons/img dark/ComboBoxDisabled.png')\n"
                                            "\n"
                                            "}\n"
                                            "\n"
                                            "#privacy_combobox::on{\n"
                                            "border: 2px solid #c2dbfe\n"
                                            "}\n"
                                            "\n"
                                            "/*listitems*/\n"
                                            "#privacy_combobox QListView{\n"
                                            "	font-size: 9px;\n"
                                            "	padding: 5px;\n"
                                            "	border: 1px solid #d3d3d3;\n"
                                            "	background-color: rgb(250, 250, 250);\n"
                                            "	outline: 0px;\n"
                                            "\n"
                                            "}\n"
                                            "#privacy_combobox QListView::item{\n"
                                            "	padding-left: 10px;\n"
                                            "	background-color: rgb(250, 250, 250);\n"
                                            "}\n"
                                            "#privacy_combobox QListView:item:hover{\n"
                                            "	background-color: #1e90ff\n"
                                            "}"
                                            "#privacy_combobox QListView:item:selected{\n"
                                            "	background-color: #1e90ff\n"
                                            "}")
        self.sys_locale_combobox = QComboBox(self.groupBox)
        self.sys_locale_combobox.setObjectName(u"sys_locale_combobox")
        self.sys_locale_combobox.setGeometry(QRect(140, 110, 241, 22))
        self.sys_locale_combobox.setFont(font5)
        self.sys_locale_combobox.setStyleSheet(u"/* Main ComboBox Style */\n"
                                               "#sys_locale_combobox {\n"
                                               "border: 1px solid #d3d3d3;\n"
                                               "border-radius: 4px;\n"
                                               "padding-left: 10px;\n"
                                               "background-color: rgb(254, 254, 254)\n"
                                               "}\n"
                                               "#sys_locale_combobox:hover{\n"
                                               "background-color: rgb(250, 250, 250)\n"
                                               "}\n"
                                               "/*Dropdown area */\n"
                                               "#sys_locale_combobox::drop-down{\n"
                                               "	border:0px\n"
                                               "}\n"
                                               "#sys_locale_combobox::down-arrow{\n"
                                               "image: url('icons/img dark/ComboBoxDisabled.png')\n"
                                               "\n"
                                               "}\n"
                                               "\n"
                                               "#sys_locale_combobox::on{\n"
                                               "border: 2px solid #c2dbfe\n"
                                               "}\n"
                                               "\n"
                                               "/*listitems*/\n"
                                               "#sys_locale_combobox QListView{\n"
                                               "	font-size: 9px;\n"
                                               "	padding: 5px;\n"
                                               "	border: 1px solid #d3d3d3;\n"
                                               "	background-color: rgb(250, 250, 250);\n"
                                               "	outline: 0px;\n"
                                               "\n"
                                               "}\n"
                                               "#sys_locale_combobox QListView::item{\n"
                                               "	padding-left: 10px;\n"
                                               "	background-color: rgb(250, 250, 250);\n"
                                               "}\n"
                                               "#sys_locale_combobox QListView:item:hover{\n"
                                               "	background-color: #1e90ff\n"
                                               "}"
                                               "#sys_locale_combobox QListView:item:selected{\n"
                                               "	background-color: #1e90ff\n"
                                               "}")
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(30, 350, 421, 80))
        self.groupBox_2.setStyleSheet(u".QGroupBox {\n"
                                      "border: 1px solid #e5e5e5;\n"
                                      "border-radius: 6px;\n"
                                      "background-color: #fbfbfb\n"
                                      "}\n"
                                      "")
        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(30, 450, 421, 111))
        self.groupBox_3.setStyleSheet(u".QGroupBox {\n"
                                      "border: 1px solid #e5e5e5;\n"
                                      "border-radius: 6px;\n"
                                      "background-color: #fbfbfb\n"
                                      "}\n"
                                      "")
        self.program_edit_button_2 = QPushButton(self.groupBox_3)
        self.program_edit_button_2.setObjectName(u"program_edit_button_2")
        self.program_edit_button_2.setGeometry(QRect(120, 20, 181, 31))
        self.program_edit_button_2.setStyleSheet(u".QPushButton {\n"
                                                 "	background-color:#ffffff;\n"
                                                 "	border-radius:4px;\n"
                                                 "	border:1px solid #8a8886;\n"
                                                 "	display:inline-block;\n"
                                                 "	cursor:pointer;\n"
                                                 "	color:#565555;\n"
                                                 "	font-family:Segoe UI Variable;\n"
                                                 "	font-weight:bold;\n"
                                                 "	font-size:13px;\n"
                                                 "	text-decoration:none;\n"
                                                 "}\n"
                                                 ".QPushButton:hover {\n"
                                                 "	background-color:#f3f2f1;\n"
                                                 "}\n"
                                                 ".QPushButton:active {\n"
                                                 "	position:relative;\n"
                                                 "	top:1px;\n"
                                                 "}")
        WindowsAnswerfile.setCentralWidget(self.centralwidget)
        self.groupBox_3.raise_()
        self.groupBox_2.raise_()
        self.groupBox.raise_()
        self.pushButton.raise_()
        self.user_edit_button.raise_()
        self.program_edit_button.raise_()
        self.vm_checkBox.raise_()
        self.win_edition_combo.raise_()
        self.label.raise_()
        self.hdd_checkbox.raise_()
        self.label_2.raise_()
        self.win_language_combobox.raise_()
        self.label_4.raise_()
        self.uac_checkbox.raise_()
        self.label_5.raise_()
        self.codeintegrity_checkbox.raise_()
        self.statusbar = QStatusBar(WindowsAnswerfile)
        self.statusbar.setObjectName(u"statusbar")
        WindowsAnswerfile.setStatusBar(self.statusbar)

        self.retranslateUi(WindowsAnswerfile)

        self.filloptions()
        self.connectbuttons()

        QMetaObject.connectSlotsByName(WindowsAnswerfile)

    # setupUi

    def retranslateUi(self, WindowsAnswerfile):
        WindowsAnswerfile.setWindowTitle(
            QCoreApplication.translate("WindowsAnswerfile", u"Windows Answer File Generator", None))
        # if QT_CONFIG(tooltip)
        WindowsAnswerfile.setToolTip("")
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        WindowsAnswerfile.setStatusTip("")
        # endif // QT_CONFIG(statustip)
        self.pushButton.setText(QCoreApplication.translate("WindowsAnswerfile", u"Generate", None))
        self.user_edit_button.setText(QCoreApplication.translate("WindowsAnswerfile", u"Add User", None))
        self.program_edit_button.setText(
            QCoreApplication.translate("WindowsAnswerfile", u"Edit Preinstalled Programs", None))
        # if QT_CONFIG(tooltip)
        self.vm_checkBox.setToolTip("")
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.vm_checkBox.setStatusTip(QCoreApplication.translate("WindowsAnswerfile",
                                                                 u"[For Windows 11] Adds the bypasses necessary to install it in a virtual machine",
                                                                 None))
        # endif // QT_CONFIG(statustip)
        self.vm_checkBox.setText(QCoreApplication.translate("WindowsAnswerfile", u"Virtual Machine", None))
        self.win_edition_combo.setCurrentText("")
        self.label.setText(QCoreApplication.translate("WindowsAnswerfile", u"Windows Edition", None))
        self.hdd_checkbox.setText(QCoreApplication.translate("WindowsAnswerfile", u"Automatic HDD assignment", None))
        self.label_2.setText(QCoreApplication.translate("WindowsAnswerfile", u"Windows Language", None))
        self.label_4.setText(QCoreApplication.translate("WindowsAnswerfile", u"Enable UAC", None))
        # if QT_CONFIG(tooltip)
        self.uac_checkbox.setToolTip("")
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.uac_checkbox.setStatusTip(QCoreApplication.translate("WindowsAnswerfile",
                                                                  u"Enables or disables User Account control. Recommended to be turned on.",
                                                                  None))
        # endif // QT_CONFIG(statustip)
        self.uac_checkbox.setText("")
        self.label_5.setText(QCoreApplication.translate("WindowsAnswerfile", u"Enable Code Integrity", None))
        # if QT_CONFIG(tooltip)
        self.codeintegrity_checkbox.setToolTip("")
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.codeintegrity_checkbox.setStatusTip(
            QCoreApplication.translate("WindowsAnswerfile", u"Enables Windows S mode.", None))
        # endif // QT_CONFIG(statustip)
        self.codeintegrity_checkbox.setText("")
        self.groupBox.setTitle("")
        self.label_6.setText(QCoreApplication.translate("WindowsAnswerfile", u"Computer Name", None))
        self.label_7.setText(QCoreApplication.translate("WindowsAnswerfile", u"Organization Name", None))
        self.label_8.setText(QCoreApplication.translate("WindowsAnswerfile", u"System Locale", None))
        self.label_9.setText(QCoreApplication.translate("WindowsAnswerfile", u"Privacy Settings", None))
        self.groupBox_2.setTitle("")
        self.groupBox_3.setTitle("")
        self.program_edit_button_2.setText(QCoreApplication.translate("WindowsAnswerfile", u"Add Wi-Fi Network", None))
    # retranslateUi


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_WindowsAnswerfile()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
