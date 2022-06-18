# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_aboutxVsaQh.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(361, 230)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(150, 20, 54, 21))
        self.label.setStyleSheet(u"font: 63 10pt \"Bahnschrift SemiBold\";\n"
"text-decoration: underline;")
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(41, 59, 284, 16))
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 102, 85, 17))
        self.label_3.setStyleSheet(u"font: 9pt \"Baskerville Old Face\";")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(40, 125, 54, 17))
        self.label_4.setStyleSheet(u"font: 9pt \"Baskerville Old Face\";")
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(40, 148, 49, 17))
        self.label_5.setStyleSheet(u"font: 9pt \"Baskerville Old Face\";")
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(39, 190, 281, 16))
        self.label_6.setStyleSheet(u"color: rgb(0, 0, 255);\n"
"font: 8pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"About !", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"This software was built as a demo project using :", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"+ Qt Designer", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"+ Python", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"+ PyQt5", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"https://github.com/oron-sinaa/", None))
    # retranslateUi

