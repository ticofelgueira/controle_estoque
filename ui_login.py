# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_login(object):
    def setupUi(self, login):
        if not login.objectName():
            login.setObjectName(u"login")
        login.resize(750, 610)
        login.setCursor(QCursor(Qt.ArrowCursor))
        login.setStyleSheet(u"background-color: rgb(0, 80, 121);")
        self.frame = QFrame(login)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(110, 240, 521, 311))
        self.frame.setCursor(QCursor(Qt.ArrowCursor))
        self.frame.setMouseTracking(True)
        self.frame.setStyleSheet(u"background-color: rgba(0, 0, 0, 0.2);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.txt_login = QLineEdit(self.frame)
        self.txt_login.setObjectName(u"txt_login")
        self.txt_login.setGeometry(QRect(140, 60, 231, 31))
        font = QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.txt_login.setFont(font)
        self.txt_login.setStyleSheet(u"background-color: rgb(217, 217, 217);\n"
"border-top-color: rgb(0, 0, 0);")
        self.txt_login.setAlignment(Qt.AlignCenter)
        self.btn_login = QPushButton(self.frame)
        self.btn_login.setObjectName(u"btn_login")
        self.btn_login.setGeometry(QRect(200, 200, 111, 31))
        font1 = QFont()
        font1.setPointSize(10)
        self.btn_login.setFont(font1)
        self.btn_login.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_login.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"\n"
"	background-color: rgb(255, 255, 255);	\n"
"	color: rgb(59, 59, 59);\n"
"	border-radius: 10px;\n"
"\n"
"}")
        self.txt_password = QLineEdit(self.frame)
        self.txt_password.setObjectName(u"txt_password")
        self.txt_password.setGeometry(QRect(140, 130, 231, 31))
        font2 = QFont()
        font2.setPointSize(11)
        self.txt_password.setFont(font2)
        self.txt_password.setStyleSheet(u"background-color: rgb(217, 217, 217);")
        self.txt_password.setText(u"")
        self.txt_password.setFrame(True)
        self.txt_password.setEchoMode(QLineEdit.Password)
        self.txt_password.setAlignment(Qt.AlignCenter)
        self.label = QLabel(login)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(220, 40, 271, 201))
        self.label.setPixmap(QPixmap(u"_imgs/icon_title.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignCenter)

        self.retranslateUi(login)

        QMetaObject.connectSlotsByName(login)
    # setupUi

    def retranslateUi(self, login):
        login.setWindowTitle(QCoreApplication.translate("login", u"Form", None))
        self.txt_login.setInputMask("")
        self.txt_login.setText("")
        self.txt_login.setPlaceholderText(QCoreApplication.translate("login", u"USU\u00c1RIO", None))
        self.btn_login.setText(QCoreApplication.translate("login", u"LOGIN", None))
        self.txt_password.setInputMask("")
        self.txt_password.setPlaceholderText(QCoreApplication.translate("login", u"SENHA", None))
        self.label.setText("")
    # retranslateUi

