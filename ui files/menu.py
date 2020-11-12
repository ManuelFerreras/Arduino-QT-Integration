# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menu.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(791, 396)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lbl_atm = QLabel(self.centralwidget)
        self.lbl_atm.setObjectName(u"lbl_atm")
        self.lbl_atm.setGeometry(QRect(350, 0, 161, 51))
        font = QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setKerning(True)
        self.lbl_atm.setFont(font)
        self.btn_deposit = QPushButton(self.centralwidget)
        self.btn_deposit.setObjectName(u"btn_deposit")
        self.btn_deposit.setGeometry(QRect(230, 90, 331, 41))
        self.btn_withdraw = QPushButton(self.centralwidget)
        self.btn_withdraw.setObjectName(u"btn_withdraw")
        self.btn_withdraw.setGeometry(QRect(230, 140, 331, 41))
        self.btn_generate = QPushButton(self.centralwidget)
        self.btn_generate.setObjectName(u"btn_generate")
        self.btn_generate.setGeometry(QRect(230, 210, 331, 41))
        self.btn_cheque = QPushButton(self.centralwidget)
        self.btn_cheque.setObjectName(u"btn_cheque")
        self.btn_cheque.setGeometry(QRect(230, 260, 331, 41))
        self.lbl_copyright = QLabel(self.centralwidget)
        self.lbl_copyright.setObjectName(u"lbl_copyright")
        self.lbl_copyright.setGeometry(QRect(0, 0, 101, 21))
        self.btn_close_session = QPushButton(self.centralwidget)
        self.btn_close_session.setObjectName(u"btn_close_session")
        self.btn_close_session.setGeometry(QRect(230, 330, 331, 41))
        self.btn_tutorial = QPushButton(self.centralwidget)
        self.btn_tutorial.setObjectName(u"btn_tutorial")
        self.btn_tutorial.setGeometry(QRect(20, 330, 171, 41))
        self.btn_exit = QPushButton(self.centralwidget)
        self.btn_exit.setObjectName(u"btn_exit")
        self.btn_exit.setGeometry(QRect(600, 330, 171, 41))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lbl_atm.setText(QCoreApplication.translate("MainWindow", u"ATM", None))
        self.btn_deposit.setText(QCoreApplication.translate("MainWindow", u"Ingresar Dinero", None))
        self.btn_withdraw.setText(QCoreApplication.translate("MainWindow", u"Retirar Dinero", None))
        self.btn_generate.setText(QCoreApplication.translate("MainWindow", u"Generar Cheque", None))
        self.btn_cheque.setText(QCoreApplication.translate("MainWindow", u"Canjear Cheque", None))
        self.lbl_copyright.setText(QCoreApplication.translate("MainWindow", u"ManunelFerreras\u00ae ", None))
        self.btn_close_session.setText(QCoreApplication.translate("MainWindow", u"Cerrar Sesion", None))
        self.btn_tutorial.setText(QCoreApplication.translate("MainWindow", u"TUTORIAL", None))
        self.btn_exit.setText(QCoreApplication.translate("MainWindow", u"SALIR", None))
    # retranslateUi

