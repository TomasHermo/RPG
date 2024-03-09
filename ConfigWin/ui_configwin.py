# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ConfigJsxAeJ.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(302, 339)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMaximumSize(QSize(302, 339))
        Dialog.setStyleSheet(u"QDialog{\n"
"border: 2px solid rgb(120, 120, 120);\n"
"}\n"
"\n"
"*{\n"
"background-color: rgb(40,40, 32);\n"
"}\n"
"")
        self.verticalLayout_7 = QVBoxLayout(Dialog)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(5, 5, 5, 5)
        self.tab = QWidget(Dialog)
        self.tab.setObjectName(u"tab")
        self.tab.setMinimumSize(QSize(120, 60))
        self.tab.setMaximumSize(QSize(16777215, 40))
        self.tab.setStyleSheet(u"border-bottom: 2px solid rgb(120, 120, 120);")
        self.verticalLayout = QVBoxLayout(self.tab)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(1, 0, 0, 5)
        self.label_3 = QLabel(self.tab)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"border: none;\n"
"font: 8pt \"Eight Bit Dragon\";")

        self.verticalLayout.addWidget(self.label_3, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_7.addWidget(self.tab, 0, Qt.AlignTop)

        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"color: rgb(238, 238, 236);\n"
"font: 12pt \"Eight Bit Dragon\";")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.center_label = QLabel(self.frame)
        self.center_label.setObjectName(u"center_label")

        self.gridLayout.addWidget(self.center_label, 0, 0, 1, 1)

        self.centerx_box = QSpinBox(self.frame)
        self.centerx_box.setObjectName(u"centerx_box")
        self.centerx_box.setMinimumSize(QSize(0, 0))
        self.centerx_box.setMaximumSize(QSize(16000000, 16000000))
        self.centerx_box.setSizeIncrement(QSize(0, 0))
        font = QFont()
        font.setFamily(u"Eight Bit Dragon")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.centerx_box.setFont(font)
        self.centerx_box.setMinimum(-1000)
        self.centerx_box.setMaximum(1000)

        self.gridLayout.addWidget(self.centerx_box, 0, 1, 1, 1)

        self.center_label_2 = QLabel(self.frame)
        self.center_label_2.setObjectName(u"center_label_2")

        self.gridLayout.addWidget(self.center_label_2, 1, 0, 1, 1)

        self.centery_box_2 = QSpinBox(self.frame)
        self.centery_box_2.setObjectName(u"centery_box_2")
        self.centery_box_2.setMaximumSize(QSize(60, 30))
        self.centery_box_2.setMinimum(-1000)
        self.centery_box_2.setMaximum(1000)

        self.gridLayout.addWidget(self.centery_box_2, 1, 1, 1, 1)

        self.center_label_6 = QLabel(self.frame)
        self.center_label_6.setObjectName(u"center_label_6")

        self.gridLayout.addWidget(self.center_label_6, 2, 0, 1, 1)

        self.centerx_box_3 = QSpinBox(self.frame)
        self.centerx_box_3.setObjectName(u"centerx_box_3")
        self.centerx_box_3.setMaximumSize(QSize(60, 30))
        self.centerx_box_3.setMinimum(-1000)
        self.centerx_box_3.setMaximum(1000)

        self.gridLayout.addWidget(self.centerx_box_3, 2, 1, 1, 1)

        self.center_label_3 = QLabel(self.frame)
        self.center_label_3.setObjectName(u"center_label_3")

        self.gridLayout.addWidget(self.center_label_3, 3, 0, 1, 1)

        self.sizeX_box = QSpinBox(self.frame)
        self.sizeX_box.setObjectName(u"sizeX_box")
        self.sizeX_box.setMaximumSize(QSize(60, 30))
        self.sizeX_box.setMinimum(-1000)
        self.sizeX_box.setMaximum(1000)
        self.sizeX_box.setValue(60)

        self.gridLayout.addWidget(self.sizeX_box, 3, 1, 1, 1)

        self.center_label_4 = QLabel(self.frame)
        self.center_label_4.setObjectName(u"center_label_4")

        self.gridLayout.addWidget(self.center_label_4, 4, 0, 1, 1)

        self.sizey_box = QSpinBox(self.frame)
        self.sizey_box.setObjectName(u"sizey_box")
        self.sizey_box.setMaximumSize(QSize(60, 30))
        self.sizey_box.setMaximum(1000)
        self.sizey_box.setValue(60)

        self.gridLayout.addWidget(self.sizey_box, 4, 1, 1, 1)

        self.center_label_5 = QLabel(self.frame)
        self.center_label_5.setObjectName(u"center_label_5")

        self.gridLayout.addWidget(self.center_label_5, 5, 0, 1, 1)

        self.sizeZ_box = QSpinBox(self.frame)
        self.sizeZ_box.setObjectName(u"sizeZ_box")
        self.sizeZ_box.setMaximumSize(QSize(60, 30))
        self.sizeZ_box.setMaximum(1000)
        self.sizeZ_box.setValue(60)

        self.gridLayout.addWidget(self.sizeZ_box, 5, 1, 1, 1)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 6, 0, 1, 1)

        self.Exhaustivness_box = QSpinBox(self.frame)
        self.Exhaustivness_box.setObjectName(u"Exhaustivness_box")
        self.Exhaustivness_box.setMaximumSize(QSize(60, 30))
        self.Exhaustivness_box.setMaximum(200)
        self.Exhaustivness_box.setValue(10)
        self.Exhaustivness_box.setDisplayIntegerBase(10)

        self.gridLayout.addWidget(self.Exhaustivness_box, 6, 1, 1, 1)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 7, 0, 1, 1)


        self.verticalLayout_7.addWidget(self.frame, 0, Qt.AlignHCenter)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 10, -1, -1)
        self.saveButton = QPushButton(Dialog)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setMaximumSize(QSize(16777215, 40))
        self.saveButton.setStyleSheet(u"QPushButton{\n"
"font: 10pt \"Eight Bit Dragon\";\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid black;\n"
"background-color: rgb(40,40, 32);\n"
"border-color: rgb(100, 100, 100);\n"
"border-radius: 12px;\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid;\n"
"background-color: rgb(80, 80, 80);\n"
"border-color: rgb(64, 64, 64);\n"
"border-radius: 12px;\n"
"}")

        self.horizontalLayout_2.addWidget(self.saveButton)

        self.resetButton = QPushButton(Dialog)
        self.resetButton.setObjectName(u"resetButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.resetButton.sizePolicy().hasHeightForWidth())
        self.resetButton.setSizePolicy(sizePolicy1)
        self.resetButton.setMinimumSize(QSize(80, 40))
        self.resetButton.setStyleSheet(u"QPushButton{\n"
"font: 10pt \"Eight Bit Dragon\";\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid black;\n"
"background-color: rgb(40,40, 32);\n"
"border-color: rgb(100, 100, 100);\n"
"border-radius: 12px;\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid;\n"
"background-color: rgb(80, 80, 80);\n"
"border-color: rgb(64, 64, 64);\n"
"border-radius: 12px;\n"
"}")

        self.horizontalLayout_2.addWidget(self.resetButton)


        self.verticalLayout_7.addLayout(self.horizontalLayout_2)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"RPG_Peptide-Selection", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#eeeeec;\">AutoDock Vina Parameters</span></p></body></html>", None))
        self.center_label.setText(QCoreApplication.translate("Dialog", u"Center X", None))
        self.center_label_2.setText(QCoreApplication.translate("Dialog", u"Center Y", None))
        self.center_label_6.setText(QCoreApplication.translate("Dialog", u"Center Z", None))
        self.center_label_3.setText(QCoreApplication.translate("Dialog", u"Size X", None))
        self.center_label_4.setText(QCoreApplication.translate("Dialog", u"Size Y", None))
        self.center_label_5.setText(QCoreApplication.translate("Dialog", u"Size Z", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Exhaustiveness ", None))
        self.label.setText("")
        self.saveButton.setText(QCoreApplication.translate("Dialog", u"Save", None))
        self.resetButton.setText(QCoreApplication.translate("Dialog", u"Reset", None))
    # retranslateUi

