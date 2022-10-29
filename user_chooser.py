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
        #return helper.User(self.role_dropdown.currentText(),self.username_field.text(),self.passowrd_field.text(),self.)
        pass







    def setupUi(self, UserAdder):
        if not UserAdder.objectName():
            UserAdder.setObjectName(u"UserAdder")
        UserAdder.resize(491, 279)
        self.buttonBox = QDialogButtonBox(UserAdder)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(60, 240, 411, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.label = QLabel(UserAdder)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 70, 91, 21))
        self.label_2 = QLabel(UserAdder)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 30, 71, 21))
        self.label_3 = QLabel(UserAdder)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 110, 61, 21))
        self.label_4 = QLabel(UserAdder)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 150, 81, 21))
        self.label_5 = QLabel(UserAdder)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 190, 81, 16))
        self.lineEdit = QLineEdit(UserAdder)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(140, 30, 151, 22))
        self.username_field = QLineEdit(UserAdder)
        self.username_field.setObjectName(u"username_field")
        self.username_field.setGeometry(QRect(140, 70, 151, 22))
        self.passowrd_field = QLineEdit(UserAdder)
        self.passowrd_field.setObjectName(u"passowrd_field")
        self.passowrd_field.setGeometry(QRect(140, 110, 151, 22))
        self.role_dropdown = QComboBox(UserAdder)
        self.role_dropdown.setObjectName(u"role_dropdown")
        self.role_dropdown.setGeometry(QRect(140, 150, 151, 22))
        self.autologon_checkbox = QCheckBox(UserAdder)
        self.autologon_checkbox.setObjectName(u"autologon_checkbox")
        self.autologon_checkbox.setGeometry(QRect(140, 190, 76, 20))

        self.retranslateUi(UserAdder)
        self.buttonBox.accepted.connect(UserAdder.accept)
        self.buttonBox.rejected.connect(UserAdder.reject)

        self.addaccounttypes(self.role_dropdown)




        QMetaObject.connectSlotsByName(UserAdder)
    # setupUi

    def retranslateUi(self, UserAdder):
        UserAdder.setWindowTitle(QCoreApplication.translate("UserAdder", u"Dialog", None))
#if QT_CONFIG(whatsthis)
        UserAdder.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.label.setText(QCoreApplication.translate("UserAdder", u"Username", None))
        self.label_2.setText(QCoreApplication.translate("UserAdder", u"Name", None))
        self.label_3.setText(QCoreApplication.translate("UserAdder", u"Password", None))
        self.label_4.setText(QCoreApplication.translate("UserAdder", u"Account type", None))
        self.label_5.setText(QCoreApplication.translate("UserAdder", u"Auto Log-on", None))
        self.autologon_checkbox.setText(QCoreApplication.translate("UserAdder", u"Enable", None))
    # retranslateUi

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QDialog()
    ui = Ui_UserAdder()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())