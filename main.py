# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow - untitledExVehK.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from cgitb import handler
from fileinput import filename
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import helper
import handler
import xmlwriter






# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow - untitledZjjxtc.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################


class Ui_WindowsAnswerfile(object):

    def make(self,edition:str):
        pass
        
    def switchstate(self,button:QPushButton)->None:
        """
        Switches a QButton's state to enabled/disabled
        """
        if button.isEnabled():
            self.hdd_edit_button.setEnabled(False)
        else:
           self.hdd_edit_button.setEnabled(True) 

    def addwineditions(self,combobox:QComboBox)->None:
        editions=["Windows 10","Windows 11"]
        variations=handler.getwindowseditions().keys()
        for edition in editions:
            for variation in variations:
                combobox.addItem(f"{edition} {variation}")
    def addwinlanguages(self,combobox:QComboBox)->None:
        langs=handler.alllanguages()
        for lang in langs:
            combobox.addItem(lang)


    def run(self):
        pass



    def setupUi(self, WindowsAnswerfile):
        if not WindowsAnswerfile.objectName():
            WindowsAnswerfile.setObjectName(u"WindowsAnswerfile")
        WindowsAnswerfile.resize(503, 528)
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(240, 240, 240, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(255, 255, 255, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(227, 227, 227, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(160, 160, 160, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush4)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush5 = QBrush(QColor(105, 105, 105, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        brush6 = QBrush(QColor(0, 120, 215, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Highlight, brush6)
        palette.setBrush(QPalette.Active, QPalette.HighlightedText, brush2)
        brush7 = QBrush(QColor(0, 0, 255, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Link, brush7)
        brush8 = QBrush(QColor(255, 0, 255, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.LinkVisited, brush8)
        brush9 = QBrush(QColor(245, 245, 245, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush9)
        brush10 = QBrush(QColor(0, 0, 0, 255))
        brush10.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Active, QPalette.NoRole, brush10)
        brush11 = QBrush(QColor(255, 255, 220, 255))
        brush11.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush11)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Highlight, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Link, brush7)
        palette.setBrush(QPalette.Inactive, QPalette.LinkVisited, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush9)
        brush12 = QBrush(QColor(0, 0, 0, 255))
        brush12.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Inactive, QPalette.NoRole, brush12)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush11)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
        brush13 = QBrush(QColor(120, 120, 120, 255))
        brush13.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush13)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        brush14 = QBrush(QColor(247, 247, 247, 255))
        brush14.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush14)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush13)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush13)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Highlight, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Link, brush7)
        palette.setBrush(QPalette.Disabled, QPalette.LinkVisited, brush8)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
        brush15 = QBrush(QColor(0, 0, 0, 255))
        brush15.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Disabled, QPalette.NoRole, brush15)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush11)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
        WindowsAnswerfile.setPalette(palette)
        WindowsAnswerfile.setFocusPolicy(Qt.ClickFocus)
        WindowsAnswerfile.setToolTipDuration(3)
        self.centralwidget = QWidget(WindowsAnswerfile)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(160, 430, 181, 61))
        self.pushButton.setStyleSheet(u"")
        self.user_label = QLabel(self.centralwidget)
        self.user_label.setObjectName(u"user_label")
        self.user_label.setGeometry(QRect(50, 370, 71, 21))
        self.user_edit_button = QPushButton(self.centralwidget)
        self.user_edit_button.setObjectName(u"user_edit_button")
        self.user_edit_button.setGeometry(QRect(110, 370, 75, 24))
        self.hdd_edit_button = QPushButton(self.centralwidget)
        self.hdd_edit_button.setObjectName(u"hdd_edit_button")
        self.hdd_edit_button.setEnabled(False)
        self.hdd_edit_button.setGeometry(QRect(280, 290, 131, 24))
        self.user_label_3 = QLabel(self.centralwidget)
        self.user_label_3.setObjectName(u"user_label_3")
        self.user_label_3.setGeometry(QRect(50, 330, 71, 21))
        self.program_edit_button = QPushButton(self.centralwidget)
        self.program_edit_button.setObjectName(u"program_edit_button")
        self.program_edit_button.setGeometry(QRect(110, 330, 75, 24))
        self.vm_checkBox = QCheckBox(self.centralwidget)
        self.vm_checkBox.setObjectName(u"vm_checkBox")
        self.vm_checkBox.setGeometry(QRect(170, 80, 151, 20))
        self.vm_checkBox.setMouseTracking(True)
#if QT_CONFIG(whatsthis)
        self.vm_checkBox.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
        self.vm_checkBox.setTristate(False)
        self.win_edition_combo = QComboBox(self.centralwidget)
        self.win_edition_combo.setObjectName(u"win_edition_combo")
        self.win_edition_combo.setGeometry(QRect(170, 50, 231, 22))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 50, 111, 16))
        self.hdd_checkbox = QCheckBox(self.centralwidget)
        self.hdd_checkbox.setObjectName(u"hdd_checkbox")
        self.hdd_checkbox.setGeometry(QRect(280, 260, 211, 20))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 120, 111, 16))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(50, 80, 91, 16))
        self.win_language_combobox = QComboBox(self.centralwidget)
        self.win_language_combobox.setObjectName(u"win_language_combobox")
        self.win_language_combobox.setGeometry(QRect(170, 120, 231, 22))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(50, 260, 101, 16))
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
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(170, 200, 231, 22))
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(50, 200, 111, 16))
        WindowsAnswerfile.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(WindowsAnswerfile)
        self.statusbar.setObjectName(u"statusbar")
        WindowsAnswerfile.setStatusBar(self.statusbar)

        self.retranslateUi(WindowsAnswerfile)


        self.addwineditions(self.win_edition_combo)
        self.addwinlanguages(self.win_language_combobox)
        self.hdd_checkbox.stateChanged.connect(self.switchstate(self.hdd_edit_button))

        

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
        self.user_label.setText(QCoreApplication.translate("WindowsAnswerfile", u"Users", None))
        self.user_edit_button.setText(QCoreApplication.translate("WindowsAnswerfile", u"Edit", None))
        self.hdd_edit_button.setText(QCoreApplication.translate("WindowsAnswerfile", u"Edit HDD Partitions", None))
        self.user_label_3.setText(QCoreApplication.translate("WindowsAnswerfile", u"Programs", None))
        self.program_edit_button.setText(QCoreApplication.translate("WindowsAnswerfile", u"Edit", None))
#if QT_CONFIG(tooltip)
        self.vm_checkBox.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.vm_checkBox.setStatusTip(QCoreApplication.translate("WindowsAnswerfile", u"[For Windows 11] Adds the bypasses necessary to install it in a virtual machine", None))
#endif // QT_CONFIG(statustip)
        self.vm_checkBox.setText("")
        self.label.setText(QCoreApplication.translate("WindowsAnswerfile", u"Windows Edition", None))
        self.hdd_checkbox.setText(QCoreApplication.translate("WindowsAnswerfile", u"Manual HDD partitions", None))
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




if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_WindowsAnswerfile()
    ui.setupUi(MainWindow)
    #apply_stylesheet(app, theme='dark_teal.xml')
    MainWindow.show()
    sys.exit(app.exec())