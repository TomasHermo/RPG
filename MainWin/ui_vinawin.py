# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vinawinNLiNQx.ui'
##
## Created by: Qt User Interface Compiler version 5.15.6
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *  # type: ignore
from PyQt5.QtGui import *  # type: ignore
from PyQt5.QtWidgets import *  # type: ignore


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(600, 600)
        Dialog.setMinimumSize(QSize(600, 600))
        Dialog.setMaximumSize(QSize(600, 600))
        Dialog.setStyleSheet(u"\n"
"*{\n"
"	background-color: rgb(100, 100,100);\n"
"	font: 8pt \"Eight Bit Dragon\";\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(40,40, 32);\n"
"\n"
"}\n"
"QDialog{\n"
"border: 5px solid black;\n"
"}")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(220, 40))
        self.label.setStyleSheet(u"font: 18pt \"Eight Bit Dragon\";")

        self.horizontalLayout.addWidget(self.label)

        self.textEdit_2 = QTextEdit(self.frame)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setMaximumSize(QSize(100, 50))
        self.textEdit_2.setStyleSheet(u"*{\n"
"border: None;\n"
"font: 20pt \"Eight Bit Dragon\";\n"
"}")

        self.horizontalLayout.addWidget(self.textEdit_2)


        self.verticalLayout.addWidget(self.frame, 0, Qt.AlignTop)

        self.peptideText = QTextEdit(Dialog)
        self.peptideText.setObjectName(u"peptideText")

        self.verticalLayout.addWidget(self.peptideText)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Progress : ", None))
        self.textEdit_2.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Eight Bit Dragon'; font-size:20pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
    # retranslateUi

