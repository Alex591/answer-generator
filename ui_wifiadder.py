# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerRCnnyH.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import wificonfig

class Ui_Dialog(object):

    def connectthings(self):
        self.comboBox.addItems(wificonfig.WifiNetwork.protocols())

    def wifinetwork(self)->wificonfig.WifiNetwork:
        wifiN = wificonfig.WifiNetwork(networkname=self.lineEdit.text(), encryption="AES",
                                       protocol=self.comboBox.currentText(), password=self.lineEdit_3.text())
        return wifiN

    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(386, 369)
        Dialog.setMinimumSize(QSize(386, 369))
        Dialog.setMaximumSize(QSize(386, 369))
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(30, 320, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.Welcomelabel = QLabel(Dialog)
        self.Welcomelabel.setObjectName(u"Welcomelabel")
        self.Welcomelabel.setGeometry(QRect(0, 20, 381, 20))
        font = QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.Welcomelabel.setFont(font)
        self.Welcomelabel.setAlignment(Qt.AlignCenter)
        self.label_7 = QLabel(Dialog)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 40, 341, 71))
        font1 = QFont()
        self.label_7.setFont(font1)
        self.label_7.setAlignment(Qt.AlignCenter)
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(40, 10, 311, 111))
        self.groupBox.setStyleSheet(u".QGroupBox {\n"
"border: 1px solid #e5e5e5;\n"
"border-radius: 6px;\n"
"background-color: #fbfbfb\n"
"}\n"
"")
        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(170, 170, 151, 21))
        self.groupBox_2 = QGroupBox(Dialog)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(40, 150, 311, 141))
        self.groupBox_2.setStyleSheet(u".QGroupBox {\n"
"border: 1px solid #e5e5e5;\n"
"border-radius: 6px;\n"
"background-color: #fbfbfb\n"
"}\n"
"")
        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 90, 81, 21))
        self.comboBox = QComboBox(self.groupBox_2)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(130, 90, 151, 22))
        self.lineEdit_3 = QLineEdit(self.groupBox_2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(130, 60, 151, 21))
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 60, 81, 16))
        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 91, 21))
        self.groupBox_2.raise_()
        self.groupBox.raise_()
        self.buttonBox.raise_()
        self.Welcomelabel.raise_()
        self.label_7.raise_()
        self.lineEdit.raise_()

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.accepted.connect(self.wifinetwork)
        self.buttonBox.rejected.connect(Dialog.reject)
        self.connectthings()
        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.Welcomelabel.setText(QCoreApplication.translate("Dialog", u"Add a new WIFI Network", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"Use this form to add a new Wifi network . \n"
" Note: The first network added will be \n"
" automatically connected to.", None))
        self.groupBox.setTitle("")
        self.groupBox_2.setTitle("")
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Protocol", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Password", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Network Name", None))
    # retranslateUi

