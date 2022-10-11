# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow - untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QStatusBar, QWidget)
import styledark_rc

class Ui_WindowsAnswerfile(object):
    def setupUi(self, WindowsAnswerfile):
        if not WindowsAnswerfile.objectName():
            WindowsAnswerfile.setObjectName(u"WindowsAnswerfile")
        WindowsAnswerfile.resize(478, 578)
        WindowsAnswerfile.setMinimumSize(QSize(478, 578))
        WindowsAnswerfile.setMaximumSize(QSize(478, 578))
        palette = QPalette()
        WindowsAnswerfile.setPalette(palette)
        font = QFont()
        WindowsAnswerfile.setFont(font)
        WindowsAnswerfile.setFocusPolicy(Qt.ClickFocus)
        WindowsAnswerfile.setToolTipDuration(3)
        WindowsAnswerfile.setStyleSheet(u"")
        self.centralwidget = QWidget(WindowsAnswerfile)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(243, 243, 243);")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(150, 430, 181, 61))
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
        self.user_edit_button.setGeometry(QRect(250, 350, 181, 31))
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
        self.program_edit_button.setGeometry(QRect(40, 350, 181, 31))
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
        self.vm_checkBox.setGeometry(QRect(170, 80, 151, 20))
        self.vm_checkBox.setMouseTracking(True)
#if QT_CONFIG(whatsthis)
        self.vm_checkBox.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
        self.vm_checkBox.setTristate(False)
        self.win_edition_combo = QComboBox(self.centralwidget)
        self.win_edition_combo.addItem("")
        self.win_edition_combo.addItem("")
        self.win_edition_combo.setObjectName(u"win_edition_combo")
        self.win_edition_combo.setGeometry(QRect(170, 50, 231, 22))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI Variable Display Semib"])
        font2.setBold(True)
        self.win_edition_combo.setFont(font2)
        self.win_edition_combo.setStyleSheet(u"/* Main ComboBox Style */\n"
"#win_edition_combo {\n"
"border: 1px solid #d3d3d3;\n"
"border-radius: 4px;\n"
"padding-left: 10px;\n"
"background-color: rgb(250, 250, 250);\n"
"}\n"
"/*Dropdown area */\n"
"#win_edition_combo::drop-down{\n"
"	border:0px\n"
"}\n"
"#win_edition_combo::down-arrow{\n"
"image: url(:/ComboBox/img dark/ComboBoxDisabled.png)\n"
"\n"
"}\n"
"\n"
"#win_edition_combo::on{\n"
"border: 2px solid #c2dbfe\n"
"}\n"
"\n"
"")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 50, 111, 16))
        self.label.setFont(font2)
        self.hdd_checkbox = QCheckBox(self.centralwidget)
        self.hdd_checkbox.setObjectName(u"hdd_checkbox")
        self.hdd_checkbox.setGeometry(QRect(270, 260, 211, 20))
        self.hdd_checkbox.setFont(font2)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 120, 111, 16))
        self.label_2.setFont(font2)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(50, 80, 91, 16))
        self.label_3.setFont(font2)
        self.win_language_combobox = QComboBox(self.centralwidget)
        self.win_language_combobox.setObjectName(u"win_language_combobox")
        self.win_language_combobox.setGeometry(QRect(170, 120, 231, 22))
        self.win_language_combobox.setStyleSheet(u"/* Main ComboBox Style */\n"
"#win_language_combobox {\n"
"border: 1px solid #d3d3d3;\n"
"border-radius: 4px;\n"
"padding-left: 10px;\n"
"background-color: rgb(250, 250, 250);\n"
"}\n"
"/*Dropdown area */\n"
"#win_language_combobox::drop-down{\n"
"	border:0px\n"
"}\n"
"#win_language_combobox::down-arrow{\n"
"image: url(:/ComboBox/img dark/ComboBoxDisabled.png)\n"
"\n"
"}\n"
"\n"
"#win_language_combobox::on{\n"
"border: 2px solid #c2dbfe\n"
"}\n"
"\n"
"")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(50, 260, 101, 16))
        self.label_4.setFont(font2)
        self.uac_checkbox = QCheckBox(self.centralwidget)
        self.uac_checkbox.setObjectName(u"uac_checkbox")
        self.uac_checkbox.setGeometry(QRect(180, 260, 31, 20))
        self.uac_checkbox.setMouseTracking(True)
#if QT_CONFIG(whatsthis)
        self.uac_checkbox.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
        self.uac_checkbox.setTristate(False)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(50, 290, 121, 16))
        self.label_5.setFont(font2)
        self.codeintegrity_checkbox = QCheckBox(self.centralwidget)
        self.codeintegrity_checkbox.setObjectName(u"codeintegrity_checkbox")
        self.codeintegrity_checkbox.setGeometry(QRect(180, 290, 31, 20))
        self.codeintegrity_checkbox.setMouseTracking(True)
#if QT_CONFIG(whatsthis)
        self.codeintegrity_checkbox.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
        self.codeintegrity_checkbox.setTristate(False)
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(170, 160, 231, 22))
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(50, 160, 101, 16))
        self.label_6.setFont(font2)
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(170, 200, 231, 22))
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(50, 200, 111, 16))
        self.label_7.setFont(font2)
        WindowsAnswerfile.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(WindowsAnswerfile)
        self.statusbar.setObjectName(u"statusbar")
        WindowsAnswerfile.setStatusBar(self.statusbar)

        self.retranslateUi(WindowsAnswerfile)

        QMetaObject.connectSlotsByName(WindowsAnswerfile)
    # setupUi

    def retranslateUi(self, WindowsAnswerfile):
        WindowsAnswerfile.setWindowTitle(QCoreApplication.translate("WindowsAnswerfile", u"Windows Answer File Generator", None))
#if QT_CONFIG(tooltip)
        WindowsAnswerfile.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        WindowsAnswerfile.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.pushButton.setText(QCoreApplication.translate("WindowsAnswerfile", u"Generate", None))
        self.user_edit_button.setText(QCoreApplication.translate("WindowsAnswerfile", u"Edit Users", None))
        self.program_edit_button.setText(QCoreApplication.translate("WindowsAnswerfile", u"Edit Preinstalled Programs", None))
#if QT_CONFIG(tooltip)
        self.vm_checkBox.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.vm_checkBox.setStatusTip(QCoreApplication.translate("WindowsAnswerfile", u"[For Windows 11] Adds the bypasses necessary to install it in a virtual machine", None))
#endif // QT_CONFIG(statustip)
        self.vm_checkBox.setText("")
        self.win_edition_combo.setItemText(0, QCoreApplication.translate("WindowsAnswerfile", u"Windows 10", None))
        self.win_edition_combo.setItemText(1, QCoreApplication.translate("WindowsAnswerfile", u"Windows 11", None))

        self.win_edition_combo.setProperty("placeholderText", QCoreApplication.translate("WindowsAnswerfile", u"Windows 11 Pro", None))
        self.label.setText(QCoreApplication.translate("WindowsAnswerfile", u"Windows Edition", None))
        self.hdd_checkbox.setText(QCoreApplication.translate("WindowsAnswerfile", u"Automatic HDD assignment", None))
        self.label_2.setText(QCoreApplication.translate("WindowsAnswerfile", u"Windows Language", None))
        self.label_3.setText(QCoreApplication.translate("WindowsAnswerfile", u"Virtual Machine", None))
        self.label_4.setText(QCoreApplication.translate("WindowsAnswerfile", u"Enable UAC", None))
#if QT_CONFIG(tooltip)
        self.uac_checkbox.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.uac_checkbox.setStatusTip(QCoreApplication.translate("WindowsAnswerfile", u"Checks the drivers and system files on your device for signs of corruption or malicious software.", None))
#endif // QT_CONFIG(statustip)
        self.uac_checkbox.setText("")
        self.label_5.setText(QCoreApplication.translate("WindowsAnswerfile", u"Enable Code Integrity", None))
#if QT_CONFIG(tooltip)
        self.codeintegrity_checkbox.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.codeintegrity_checkbox.setStatusTip(QCoreApplication.translate("WindowsAnswerfile", u"Enables or disables User Account control. This option is strongly recommended to be turned on.", None))
#endif // QT_CONFIG(statustip)
        self.codeintegrity_checkbox.setText("")
        self.label_6.setText(QCoreApplication.translate("WindowsAnswerfile", u"Computer Name", None))
        self.label_7.setText(QCoreApplication.translate("WindowsAnswerfile", u"Organization Name", None))
    # retranslateUi

