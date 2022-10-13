# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'programs.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QDialog,
    QDialogButtonBox, QLabel, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(513, 399)
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(10, 360, 451, 32))
        self.buttonBox.setLayoutDirection(Qt.LeftToRight)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 40, 81, 16))
        self.googlechrome = QCheckBox(Dialog)
        self.googlechrome.setObjectName(u"googlechrome")
        self.googlechrome.setGeometry(QRect(20, 70, 91, 17))
        font = QFont()
        font.setFamilies([u"Segoe UI Variable Display"])
        self.googlechrome.setFont(font)
        self.firefox = QCheckBox(Dialog)
        self.firefox.setObjectName(u"firefox")
        self.firefox.setGeometry(QRect(20, 90, 91, 17))
        self.firefox.setFont(font)
        self.opera = QCheckBox(Dialog)
        self.opera.setObjectName(u"opera")
        self.opera.setGeometry(QRect(20, 110, 91, 17))
        self.opera.setFont(font)
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 140, 81, 16))
        self.pycharm = QCheckBox(Dialog)
        self.pycharm.setObjectName(u"pycharm")
        self.pycharm.setGeometry(QRect(20, 170, 101, 17))
        self.pycharm.setFont(font)
        self.vscode = QCheckBox(Dialog)
        self.vscode.setObjectName(u"vscode")
        self.vscode.setGeometry(QRect(20, 190, 111, 17))
        self.vscode.setFont(font)
        self.opera_4 = QCheckBox(Dialog)
        self.opera_4.setObjectName(u"opera_4")
        self.opera_4.setGeometry(QRect(20, 210, 111, 17))
        self.opera_4.setFont(font)
        self.python = QCheckBox(Dialog)
        self.python.setObjectName(u"python")
        self.python.setGeometry(QRect(20, 230, 111, 17))
        self.python.setFont(font)
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 260, 81, 16))
        self.qbittorent = QCheckBox(Dialog)
        self.qbittorent.setObjectName(u"qbittorent")
        self.qbittorent.setGeometry(QRect(20, 290, 111, 17))
        self.qbittorent.setFont(font)
        self.transmission = QCheckBox(Dialog)
        self.transmission.setObjectName(u"transmission")
        self.transmission.setGeometry(QRect(20, 310, 111, 17))
        self.transmission.setFont(font)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Web Browsers", None))
        self.googlechrome.setText(QCoreApplication.translate("Dialog", u"Google Chrome", None))
        self.firefox.setText(QCoreApplication.translate("Dialog", u"Mozilla Firefox", None))
        self.opera.setText(QCoreApplication.translate("Dialog", u"Opera", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Developer Tools", None))
        self.pycharm.setText(QCoreApplication.translate("Dialog", u"Jetbrains Pycharm", None))
        self.vscode.setText(QCoreApplication.translate("Dialog", u"Visual Studion Code", None))
        self.opera_4.setText(QCoreApplication.translate("Dialog", u"Java JDK", None))
        self.python.setText(QCoreApplication.translate("Dialog", u"Python", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"File Sharing", None))
        self.qbittorent.setText(QCoreApplication.translate("Dialog", u"qbittorent", None))
        self.transmission.setText(QCoreApplication.translate("Dialog", u"Transmission", None))
    # retranslateUi

