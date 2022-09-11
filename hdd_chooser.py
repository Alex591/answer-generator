# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'hddadderTFKIsP.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from string import ascii_uppercase as characters

class Ui_Dialog(object):

    def addletters(self,combobox:QComboBox)->None:
        """
        Adds drive letters
        """
        combobox.addItems(characters)

    def addnumbers(self,combobox:QComboBox)->None:
        """
        Adds drive numbers
        """
        for num in range(1,11):
            combobox.addItem(str(num))





    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(480, 304)
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(0, 250, 461, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 111, 21))
        self.checkBox = QCheckBox(Dialog)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(170, 20, 76, 20))
        self.checkBox.setChecked(True)
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 60, 91, 16))
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 100, 81, 16))
        self.comboBox = QComboBox(Dialog)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(170, 100, 69, 22))
        self.driveletter_dropdown = QComboBox(Dialog)
        self.driveletter_dropdown.setObjectName(u"driveletter_dropdown")
        self.driveletter_dropdown.setGeometry(QRect(170, 60, 69, 22))
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 140, 121, 16))
        self.checkBox_2 = QCheckBox(Dialog)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setGeometry(QRect(170, 140, 76, 20))
        self.checkBox_2.setChecked(True)
        self.manual_size = QLineEdit(Dialog)
        self.manual_size.setObjectName(u"manual_size")
        self.manual_size.setGeometry(QRect(170, 170, 113, 22))
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 170, 121, 16))

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)


        self.addletters(self.driveletter_dropdown)
        self.addnumbers(self.comboBox)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Windows Partition", None))
        self.checkBox.setText("")
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Drive Letter", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"HDD number", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Automatically set size", None))
        self.checkBox_2.setText("")
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Size", None))
    # retranslateUi

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QDialog()
    ui = Ui_Dialog()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())