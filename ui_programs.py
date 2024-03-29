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
                               QDialogButtonBox, QFrame, QGroupBox, QLabel,
                               QSizePolicy, QWidget)

import powershellwriter
class Ui_Dialog(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.program_list=[]
    def accept_function(self):
        for x in self.programs():
            if x.isChecked():
                varname=f"{x=}".split("=")[2]
                varname=varname.split(")")[0]
                self.program_list.append(powershellwriter.Program(varname.replace('"','')))
        for x in self.program_list:
            print(x)
        self.close()





    def programs(self) -> list[QCheckBox]:
        """
        Puts all the checkboxes in a list to iterate over and to get them connected
        :return: List of program variables of type QCheckBox
        """
        return [self.opera, self.googlechrome, self.firefox, self.pycharm, self.vscode, self.oraclejdk, self.python,
                self.notepadplusplus, self.putty, self.eclipse, self.oracle1sql1developer, self.jre8, self.qbittorent,
                self.transmission, self.zoom, self.discord, self.skype, self.msteams, self.discord, self.skype,
                self.instagram, self.whatsapp, self.office, self.netflix, self.spotify, self.disneyplus,
                self.ubisoft1connect, self.origin, self.epicgameslauncher, self.Steam, self.winrar, self.itunes,
                self.vlc, self.plex, self.powertoys]

    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Add or remove programs")
        Dialog.resize(518, 657)
        Dialog.setMinimumSize(QSize(518, 657))
        Dialog.setMaximumSize(QSize(518, 657))
        Dialog.setStyleSheet(u".QCheckBox::indicator {\n"
                             "     width: 12px;\n"
                             "     height: 12px;\n"
                             " }")
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(40, 620, 451, 32))
        self.buttonBox.setLayoutDirection(Qt.LeftToRight)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 160, 101, 21))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label.setFont(font)
        self.googlechrome = QCheckBox(Dialog)
        self.googlechrome.setObjectName(u"googlechrome")
        self.googlechrome.setGeometry(QRect(30, 200, 91, 17))
        font1 = QFont()
        self.googlechrome.setFont(font1)
        self.firefox = QCheckBox(Dialog)
        self.firefox.setObjectName(u"firefox")
        self.firefox.setGeometry(QRect(30, 220, 91, 17))
        font2 = QFont()
        font2.setPointSize(8)
        self.firefox.setFont(font2)
        self.opera = QCheckBox(Dialog)
        self.opera.setObjectName(u"opera")
        self.opera.setGeometry(QRect(30, 240, 91, 17))
        self.opera.setFont(font1)
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(-20, 10, 531, 41))
        font3 = QFont()
        font3.setPointSize(20)
        font3.setBold(True)
        self.label_4.setFont(font3)
        self.label_4.setAlignment(Qt.AlignCenter)
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 501, 131))
        self.groupBox.setStyleSheet(u".QGroupBox {\n"
                                    "border: 1px solid #e5e5e5;\n"
                                    "border-radius: 6px;\n"
                                    "background-color: #fbfbfb\n"
                                    "}\n"
                                    "")
        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 90, 471, 31))
        font4 = QFont()
        font4.setPointSize(9)
        self.label_6.setFont(font4)
        self.label_6.setStyleSheet(u".QLabel {\n"
                                   "background-color: #fbfbfb;\n"
                                   "	color: rgb(0, 70, 124);\n"
                                   "}\n"
                                   "")
        self.label_6.setFrameShape(QFrame.NoFrame)
        self.label_6.setFrameShadow(QFrame.Plain)
        self.label_6.setTextFormat(Qt.RichText)
        self.label_6.setScaledContents(True)
        self.label_6.setAlignment(Qt.AlignCenter)
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 50, 481, 31))
        font5 = QFont()
        font5.setFamilies([u"Segoe UI Variable Display"])
        font5.setPointSize(8)
        self.label_5.setFont(font5)
        self.label_5.setStyleSheet(u".QLabel {\n"
                                   "background-color: #fbfbfb;\n"
                                   "}\n"
                                   "")
        self.label_5.setFrameShape(QFrame.NoFrame)
        self.label_5.setFrameShadow(QFrame.Plain)
        self.label_5.setTextFormat(Qt.RichText)
        self.label_5.setScaledContents(True)
        self.label_5.setAlignment(Qt.AlignCenter)
        self.groupBox_2 = QGroupBox(Dialog)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 150, 131, 121))
        self.groupBox_2.setStyleSheet(u".QGroupBox {\n"
                                      "border: 1px solid #e5e5e5;\n"
                                      "border-radius: 6px;\n"
                                      "background-color: #fbfbfb\n"
                                      "}\n"
                                      "")
        self.groupBox_3 = QGroupBox(Dialog)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(10, 280, 131, 231))
        self.groupBox_3.setStyleSheet(u".QGroupBox {\n"
                                      "border: 1px solid #e5e5e5;\n"
                                      "border-radius: 6px;\n"
                                      "background-color: #fbfbfb\n"
                                      "}\n"
                                      "")
        self.label_2 = QLabel(self.groupBox_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 10, 111, 16))
        self.label_2.setFont(font)
        self.python = QCheckBox(self.groupBox_3)
        self.python.setObjectName(u"python")
        self.python.setGeometry(QRect(20, 100, 111, 17))
        self.python.setFont(font1)
        self.pycharm = QCheckBox(self.groupBox_3)
        self.pycharm.setObjectName(u"pycharm")
        self.pycharm.setGeometry(QRect(20, 40, 101, 17))
        self.pycharm.setFont(font1)
        self.vscode = QCheckBox(self.groupBox_3)
        self.vscode.setObjectName(u"vscode")
        self.vscode.setGeometry(QRect(20, 60, 111, 17))
        self.vscode.setFont(font1)
        self.oraclejdk = QCheckBox(self.groupBox_3)
        self.oraclejdk.setObjectName(u"oraclejdk")
        self.oraclejdk.setGeometry(QRect(20, 80, 111, 17))
        self.oraclejdk.setFont(font1)
        self.notepadplusplus = QCheckBox(self.groupBox_3)
        self.notepadplusplus.setObjectName(u"notepadplusplus")
        self.notepadplusplus.setGeometry(QRect(20, 120, 111, 17))
        self.notepadplusplus.setFont(font1)
        self.putty = QCheckBox(self.groupBox_3)
        self.putty.setObjectName(u"putty")
        self.putty.setGeometry(QRect(20, 140, 111, 17))
        self.putty.setFont(font1)
        self.eclipse = QCheckBox(self.groupBox_3)
        self.eclipse.setObjectName(u"eclipse")
        self.eclipse.setGeometry(QRect(20, 160, 111, 17))
        self.eclipse.setFont(font1)
        self.oracle1sql1developer = QCheckBox(self.groupBox_3)
        self.oracle1sql1developer.setObjectName(u"oracle1sql1developer")
        self.oracle1sql1developer.setGeometry(QRect(20, 180, 111, 17))
        self.oracle1sql1developer.setFont(font1)
        self.jre8 = QCheckBox(self.groupBox_3)
        self.jre8.setObjectName(u"jre8")
        self.jre8.setGeometry(QRect(20, 200, 111, 17))
        self.jre8.setFont(font1)
        self.groupBox_4 = QGroupBox(Dialog)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(190, 150, 131, 121))
        self.groupBox_4.setStyleSheet(u".QGroupBox {\n"
                                      "border: 1px solid #e5e5e5;\n"
                                      "border-radius: 6px;\n"
                                      "background-color: #fbfbfb\n"
                                      "}\n"
                                      "")
        self.transmission = QCheckBox(self.groupBox_4)
        self.transmission.setObjectName(u"transmission")
        self.transmission.setGeometry(QRect(20, 60, 111, 17))
        self.transmission.setFont(font1)
        self.label_3 = QLabel(self.groupBox_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 10, 131, 20))
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.qbittorent = QCheckBox(self.groupBox_4)
        self.qbittorent.setObjectName(u"qbittorent")
        self.qbittorent.setGeometry(QRect(20, 40, 111, 17))
        self.qbittorent.setFont(font1)
        self.groupBox_5 = QGroupBox(Dialog)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(190, 280, 131, 171))
        self.groupBox_5.setStyleSheet(u".QGroupBox {\n"
                                      "border: 1px solid #e5e5e5;\n"
                                      "border-radius: 6px;\n"
                                      "background-color: #fbfbfb\n"
                                      "}\n"
                                      "")
        self.label_7 = QLabel(self.groupBox_5)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(0, 10, 131, 20))
        self.label_7.setFont(font)
        self.label_7.setAlignment(Qt.AlignCenter)
        self.zoom = QCheckBox(self.groupBox_5)
        self.zoom.setObjectName(u"zoom")
        self.zoom.setGeometry(QRect(20, 40, 101, 17))
        self.zoom.setFont(font1)
        self.discord = QCheckBox(self.groupBox_5)
        self.discord.setObjectName(u"discord")
        self.discord.setGeometry(QRect(20, 60, 101, 17))
        self.discord.setFont(font1)
        self.skype = QCheckBox(self.groupBox_5)
        self.skype.setObjectName(u"skype")
        self.skype.setGeometry(QRect(20, 80, 101, 17))
        self.skype.setFont(font1)
        self.msteams = QCheckBox(self.groupBox_5)
        self.msteams.setObjectName(u"msteams")
        self.msteams.setGeometry(QRect(20, 100, 101, 17))
        self.msteams.setFont(font1)
        self.instagram = QCheckBox(self.groupBox_5)
        self.instagram.setObjectName(u"instagram")
        self.instagram.setGeometry(QRect(20, 120, 101, 17))
        self.instagram.setFont(font1)
        self.whatsapp = QCheckBox(self.groupBox_5)
        self.whatsapp.setObjectName(u"whatsapp")
        self.whatsapp.setGeometry(QRect(20, 140, 101, 17))
        self.whatsapp.setFont(font1)
        self.groupBox_6 = QGroupBox(Dialog)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setGeometry(QRect(370, 150, 120, 121))
        self.groupBox_6.setStyleSheet(u".QGroupBox {\n"
                                      "border: 1px solid #e5e5e5;\n"
                                      "border-radius: 6px;\n"
                                      "background-color: #fbfbfb\n"
                                      "}\n"
                                      "")
        self.label_8 = QLabel(self.groupBox_6)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(0, 10, 121, 20))
        self.label_8.setFont(font)
        self.label_8.setAlignment(Qt.AlignCenter)
        self.netflix = QCheckBox(self.groupBox_6)
        self.netflix.setObjectName(u"netflix")
        self.netflix.setGeometry(QRect(20, 40, 91, 17))
        self.netflix.setFont(font1)
        self.spotify = QCheckBox(self.groupBox_6)
        self.spotify.setObjectName(u"spotify")
        self.spotify.setGeometry(QRect(20, 60, 91, 17))
        self.spotify.setFont(font1)
        self.disneyplus = QCheckBox(self.groupBox_6)
        self.disneyplus.setObjectName(u"disneyplus")
        self.disneyplus.setGeometry(QRect(20, 80, 91, 17))
        self.disneyplus.setFont(font1)
        self.groupBox_7 = QGroupBox(Dialog)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setGeometry(QRect(370, 280, 121, 131))
        self.groupBox_7.setStyleSheet(u".QGroupBox {\n"
                                      "border: 1px solid #e5e5e5;\n"
                                      "border-radius: 6px;\n"
                                      "background-color: #fbfbfb\n"
                                      "}\n"
                                      "")
        self.label_9 = QLabel(self.groupBox_7)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(0, 10, 121, 20))
        self.label_9.setFont(font)
        self.label_9.setAlignment(Qt.AlignCenter)
        self.ubisoft1connect = QCheckBox(self.groupBox_7)
        self.ubisoft1connect.setObjectName(u"ubisoft1connect")
        self.ubisoft1connect.setGeometry(QRect(20, 40, 101, 17))
        self.ubisoft1connect.setFont(font2)
        self.origin = QCheckBox(self.groupBox_7)
        self.origin.setObjectName(u"origin")
        self.origin.setGeometry(QRect(20, 60, 91, 17))
        self.origin.setFont(font1)
        self.epicgameslauncher = QCheckBox(self.groupBox_7)
        self.epicgameslauncher.setObjectName(u"epicgameslauncher")
        self.epicgameslauncher.setGeometry(QRect(20, 80, 91, 17))
        self.epicgameslauncher.setFont(font1)
        self.Steam = QCheckBox(self.groupBox_7)
        self.Steam.setObjectName(u"Steam")
        self.Steam.setGeometry(QRect(20, 100, 91, 17))
        self.Steam.setFont(font1)
        self.groupBox_8 = QGroupBox(Dialog)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.groupBox_8.setGeometry(QRect(190, 460, 131, 80))
        self.groupBox_8.setStyleSheet(u".QGroupBox {\n"
                                      "border: 1px solid #e5e5e5;\n"
                                      "border-radius: 6px;\n"
                                      "background-color: #fbfbfb\n"
                                      "}\n"
                                      "")
        self.label_10 = QLabel(self.groupBox_8)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(0, 10, 131, 20))
        self.label_10.setFont(font)
        self.label_10.setAlignment(Qt.AlignCenter)
        self.office = QCheckBox(self.groupBox_8)
        self.office.setObjectName(u"office")
        self.office.setGeometry(QRect(20, 40, 101, 17))
        self.office.setFont(font1)
        self.groupBox_9 = QGroupBox(Dialog)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.groupBox_9.setGeometry(QRect(370, 420, 120, 151))
        self.groupBox_9.setStyleSheet(u".QGroupBox {\n"
                                      "border: 1px solid #e5e5e5;\n"
                                      "border-radius: 6px;\n"
                                      "background-color: #fbfbfb\n"
                                      "}\n"
                                      "")
        self.label_11 = QLabel(self.groupBox_9)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(0, 10, 121, 20))
        self.label_11.setFont(font)
        self.label_11.setAlignment(Qt.AlignCenter)
        self.winrar = QCheckBox(self.groupBox_9)
        self.winrar.setObjectName(u"winrar")
        self.winrar.setGeometry(QRect(20, 40, 91, 17))
        self.winrar.setFont(font1)
        self.itunes = QCheckBox(self.groupBox_9)
        self.itunes.setObjectName(u"itunes")
        self.itunes.setGeometry(QRect(20, 60, 91, 17))
        self.itunes.setFont(font1)
        self.vlc = QCheckBox(self.groupBox_9)
        self.vlc.setObjectName(u"vlc")
        self.vlc.setGeometry(QRect(20, 80, 91, 17))
        self.vlc.setFont(font1)
        self.plex = QCheckBox(self.groupBox_9)
        self.plex.setObjectName(u"plex")
        self.plex.setGeometry(QRect(20, 100, 91, 17))
        self.plex.setFont(font1)
        self.powertoys = QCheckBox(self.groupBox_9)
        self.powertoys.setObjectName(u"powertoys")
        self.powertoys.setGeometry(QRect(20, 120, 91, 17))
        self.powertoys.setFont(font1)
        self.groupBox_3.raise_()
        self.groupBox_2.raise_()
        self.groupBox.raise_()
        self.buttonBox.raise_()
        self.label.raise_()
        self.googlechrome.raise_()
        self.firefox.raise_()
        self.opera.raise_()
        self.label_4.raise_()
        self.groupBox_4.raise_()
        self.groupBox_5.raise_()
        self.groupBox_6.raise_()
        self.groupBox_7.raise_()
        self.groupBox_8.raise_()
        self.groupBox_9.raise_()
        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(self.accept_function)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)

    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Web Browsers", None))
        # if QT_CONFIG(tooltip)
        self.googlechrome.setToolTip(QCoreApplication.translate("Dialog", u"Web Browser by Google", None))
        # endif // QT_CONFIG(tooltip)
        self.googlechrome.setText(QCoreApplication.translate("Dialog", u"Chrome", None))
        # if QT_CONFIG(tooltip)
        self.firefox.setToolTip(QCoreApplication.translate("Dialog", u"Privacy focused Browser", None))
        # endif // QT_CONFIG(tooltip)
        self.firefox.setText(QCoreApplication.translate("Dialog", u"Mozilla Firefox", None))
        # if QT_CONFIG(tooltip)
        self.opera.setToolTip(QCoreApplication.translate("Dialog", u"Browser with built-in VPN", None))
        # endif // QT_CONFIG(tooltip)
        self.opera.setText(QCoreApplication.translate("Dialog", u"Opera", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Programs", None))
        self.groupBox.setTitle("")
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Note: Requires an Internet connection", None))
        self.label_5.setText(QCoreApplication.translate("Dialog",
                                                        u"You can add programs the with a help of a startup script will be preinstalled on your device.",
                                                        None))
        self.groupBox_2.setTitle("")
        self.groupBox_3.setTitle("")
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Developer Tools", None))
        # if QT_CONFIG(tooltip)
        self.python.setToolTip(QCoreApplication.translate("Dialog", u"Programming Language", None))
        # endif // QT_CONFIG(tooltip)
        self.python.setText(QCoreApplication.translate("Dialog", u"Python", None))
        # if QT_CONFIG(tooltip)
        self.pycharm.setToolTip(QCoreApplication.translate("Dialog", u"Python IDE", None))
        # endif // QT_CONFIG(tooltip)
        self.pycharm.setText(QCoreApplication.translate("Dialog", u"Pycharm", None))
        # if QT_CONFIG(tooltip)
        self.vscode.setToolTip(QCoreApplication.translate("Dialog", u"Free code editor by Microsoft", None))
        # endif // QT_CONFIG(tooltip)
        self.vscode.setText(QCoreApplication.translate("Dialog", u"VS Code", None))
        # if QT_CONFIG(tooltip)
        self.oraclejdk.setToolTip(QCoreApplication.translate("Dialog", u"Java Development Kit", None))
        # endif // QT_CONFIG(tooltip)
        self.oraclejdk.setText(QCoreApplication.translate("Dialog", u"Java JDK", None))
        # if QT_CONFIG(tooltip)
        self.notepadplusplus.setToolTip(QCoreApplication.translate("Dialog", u"Programming Language", None))
        # endif // QT_CONFIG(tooltip)
        self.notepadplusplus.setText(QCoreApplication.translate("Dialog", u"Notepad++", None))
        # if QT_CONFIG(tooltip)
        self.putty.setToolTip(QCoreApplication.translate("Dialog", u"Programming Language", None))
        # endif // QT_CONFIG(tooltip)
        self.putty.setText(QCoreApplication.translate("Dialog", u"PuTTY", None))
        # if QT_CONFIG(tooltip)
        self.eclipse.setToolTip(QCoreApplication.translate("Dialog", u"Programming Language", None))
        # endif // QT_CONFIG(tooltip)
        self.eclipse.setText(QCoreApplication.translate("Dialog", u"Eclipse", None))
        # if QT_CONFIG(tooltip)
        self.oracle1sql1developer.setToolTip(QCoreApplication.translate("Dialog", u"Programming Language", None))
        # endif // QT_CONFIG(tooltip)
        self.oracle1sql1developer.setText(QCoreApplication.translate("Dialog", u"SQL Developer", None))
        # if QT_CONFIG(tooltip)
        self.jre8.setToolTip(QCoreApplication.translate("Dialog", u"Programming Language", None))
        # endif // QT_CONFIG(tooltip)
        self.jre8.setText(QCoreApplication.translate("Dialog", u"Java Runtime", None))
        self.groupBox_4.setTitle("")
        self.transmission.setText(QCoreApplication.translate("Dialog", u"Transmission", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"File Sharing", None))
        self.qbittorent.setText(QCoreApplication.translate("Dialog", u"qbittorent", None))
        self.groupBox_5.setTitle("")
        self.label_7.setText(QCoreApplication.translate("Dialog", u"Socials", None))
        # if QT_CONFIG(tooltip)
        self.zoom.setToolTip(QCoreApplication.translate("Dialog", u"Python IDE", None))
        # endif // QT_CONFIG(tooltip)
        self.zoom.setText(QCoreApplication.translate("Dialog", u"Zoom", None))
        # if QT_CONFIG(tooltip)
        self.discord.setToolTip(QCoreApplication.translate("Dialog", u"Python IDE", None))
        # endif // QT_CONFIG(tooltip)
        self.discord.setText(QCoreApplication.translate("Dialog", u"Discord", None))
        # if QT_CONFIG(tooltip)
        self.skype.setToolTip(QCoreApplication.translate("Dialog", u"Python IDE", None))
        # endif // QT_CONFIG(tooltip)
        self.skype.setText(QCoreApplication.translate("Dialog", u"Skype", None))
        # if QT_CONFIG(tooltip)
        self.msteams.setToolTip(QCoreApplication.translate("Dialog", u"Python IDE", None))
        # endif // QT_CONFIG(tooltip)
        self.msteams.setText(QCoreApplication.translate("Dialog", u"Teams", None))
        # if QT_CONFIG(tooltip)
        self.instagram.setToolTip(QCoreApplication.translate("Dialog", u"Python IDE", None))
        # endif // QT_CONFIG(tooltip)
        self.instagram.setText(QCoreApplication.translate("Dialog", u"Instagram", None))
        # if QT_CONFIG(tooltip)
        self.whatsapp.setToolTip(QCoreApplication.translate("Dialog", u"Python IDE", None))
        # endif // QT_CONFIG(tooltip)
        self.whatsapp.setText(QCoreApplication.translate("Dialog", u"Whatsapp", None))
        self.groupBox_6.setTitle("")
        self.label_8.setText(QCoreApplication.translate("Dialog", u"Streaming", None))
        self.netflix.setText(QCoreApplication.translate("Dialog", u"Netflix", None))
        self.spotify.setText(QCoreApplication.translate("Dialog", u"Spotify", None))
        self.disneyplus.setText(QCoreApplication.translate("Dialog", u"Disney+", None))
        self.groupBox_7.setTitle("")
        self.label_9.setText(QCoreApplication.translate("Dialog", u"Gaming", None))
        self.ubisoft1connect.setText(QCoreApplication.translate("Dialog", u"Ubisoft Connect", None))
        self.origin.setText(QCoreApplication.translate("Dialog", u"Origin", None))
        self.epicgameslauncher.setText(QCoreApplication.translate("Dialog", u"Epic Games", None))
        self.Steam.setText(QCoreApplication.translate("Dialog", u"Steam", None))
        self.groupBox_8.setTitle("")
        self.label_10.setText(QCoreApplication.translate("Dialog", u"Office", None))
        # if QT_CONFIG(tooltip)
        self.office.setToolTip(QCoreApplication.translate("Dialog", u"Python IDE", None))
        # endif // QT_CONFIG(tooltip)
        self.office.setText(QCoreApplication.translate("Dialog", u"Office 365", None))
        self.groupBox_9.setTitle("")
        self.label_11.setText(QCoreApplication.translate("Dialog", u"Other", None))
        self.winrar.setText(QCoreApplication.translate("Dialog", u"WinRAR", None))
        self.itunes.setText(QCoreApplication.translate("Dialog", u"iTunes", None))
        self.vlc.setText(QCoreApplication.translate("Dialog", u"VLC", None))
        self.plex.setText(QCoreApplication.translate("Dialog", u"Plex", None))
        self.powertoys.setText(QCoreApplication.translate("Dialog", u"PowerToys", None))
    # retranslateUi
