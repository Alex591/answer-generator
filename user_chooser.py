# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'useradderkOVecE.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

import helper


class Ui_UserAdder(object):

    def addaccounttypes(self,combobox:QComboBox)->None:
        """
        Adds Account types :Administrator or normal user
        """
        accounttypes=["Administrators","Users"]
        combobox.addItems(accounttypes)
    def createduser(self)->helper.User:
        return helper.User(self.role_dropdown.currentText(),self.username_field.text(),self.password_field.text(),self.lineEdit.text(),self.autologon_checkbox.isChecked())



    def setupUi(self, UserAdder):
        if not UserAdder.objectName():
            UserAdder.setObjectName(u"UserAdder")
        UserAdder.resize(361, 394)
        UserAdder.setMinimumSize(QSize(361, 394))
        UserAdder.setMaximumSize(QSize(361, 394))
        UserAdder.setStyleSheet(u".QGroupBox {\n"
                                "border: 1px solid #e5e5e5;\n"
                                "border-radius: 6px;\n"
                                "background-color: #fbfbfb\n"
                                "}\n"
                                "")
        self.buttonBox = QDialogButtonBox(UserAdder)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(80, 350, 261, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        self.label = QLabel(UserAdder)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 180, 91, 21))
        self.label_2 = QLabel(UserAdder)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 140, 71, 21))
        self.label_3 = QLabel(UserAdder)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(50, 220, 61, 21))
        self.label_4 = QLabel(UserAdder)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(50, 260, 81, 21))
        self.label_5 = QLabel(UserAdder)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(50, 300, 81, 16))
        self.lineEdit = QLineEdit(UserAdder)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(160, 140, 151, 22))
        self.username_field = QLineEdit(UserAdder)
        self.username_field.setObjectName(u"username_field")
        self.username_field.setGeometry(QRect(160, 180, 151, 22))
        self.password_field = QLineEdit(UserAdder)
        self.password_field.setObjectName(u"password_field")
        self.password_field.setGeometry(QRect(160, 220, 151, 22))
        self.role_dropdown = QComboBox(UserAdder)
        self.role_dropdown.setObjectName(u"role_dropdown")
        self.role_dropdown.setGeometry(QRect(160, 260, 151, 22))
        self.autologon_checkbox = QCheckBox(UserAdder)
        self.autologon_checkbox.setObjectName(u"autologon_checkbox")
        self.autologon_checkbox.setGeometry(QRect(160, 300, 76, 20))
        self.Welcomelabel = QLabel(UserAdder)
        self.Welcomelabel.setObjectName(u"Welcomelabel")
        self.Welcomelabel.setGeometry(QRect(0, 20, 361, 20))
        font = QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.Welcomelabel.setFont(font)
        self.Welcomelabel.setAlignment(Qt.AlignCenter)
        self.label_6 = QLabel(UserAdder)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 40, 341, 61))
        font1 = QFont()
        self.label_6.setFont(font1)
        self.label_6.setAlignment(Qt.AlignCenter)
        self.groupBox = QGroupBox(UserAdder)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(40, 10, 281, 101))
        self.groupBox.setStyleSheet(u".QGroupBox {\n"
                                    "border: 1px solid #e5e5e5;\n"
                                    "border-radius: 6px;\n"
                                    "background-color: #fbfbfb\n"
                                    "}\n"
                                    "")
        self.groupBox_2 = QGroupBox(UserAdder)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(40, 120, 281, 211))
        self.groupBox_2.raise_()
        self.groupBox.raise_()
        self.buttonBox.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.lineEdit.raise_()
        self.username_field.raise_()
        self.password_field.raise_()
        self.role_dropdown.raise_()
        self.autologon_checkbox.raise_()
        self.Welcomelabel.raise_()
        self.label_6.raise_()

        self.retranslateUi(UserAdder)
        self.buttonBox.accepted.connect(UserAdder.accept)
        self.buttonBox.rejected.connect(UserAdder.reject)
        self.addaccounttypes(self.role_dropdown)
        QMetaObject.connectSlotsByName(UserAdder)

    # setupUi

    def retranslateUi(self, UserAdder):
        UserAdder.setWindowTitle(QCoreApplication.translate("UserAdder", u"Dialog", None))
        # if QT_CONFIG(whatsthis)
        UserAdder.setWhatsThis("")
        # endif // QT_CONFIG(whatsthis)
        self.label.setText(QCoreApplication.translate("UserAdder", u"Username", None))
        self.label_2.setText(QCoreApplication.translate("UserAdder", u"Name", None))
        self.label_3.setText(QCoreApplication.translate("UserAdder", u"Password", None))
        self.label_4.setText(QCoreApplication.translate("UserAdder", u"Account type", None))
        self.label_5.setText(QCoreApplication.translate("UserAdder", u"Auto Log-on", None))
        self.autologon_checkbox.setText(QCoreApplication.translate("UserAdder", u"Enable", None))
        self.Welcomelabel.setText(QCoreApplication.translate("UserAdder", u"Add a new user", None))
        self.label_6.setText(
            QCoreApplication.translate("UserAdder", u"Use this form to add new users to the system. \n"
                                                    " Note: \n"
                                                    " The username should only include ASCII characters.", None))
        self.groupBox.setTitle("")
        self.groupBox_2.setTitle("")
    # retranslateUi

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QDialog()
    ui = Ui_UserAdder()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())