# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PeptidepYTXFg.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import resources_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(572, 646)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
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
        self.tab.setMinimumSize(QSize(120, 30))
        self.tab.setMaximumSize(QSize(16777215, 40))
        self.tab.setStyleSheet(u"border-bottom: 2px solid rgb(120, 120, 120);")
        self.horizontalLayout_4 = QHBoxLayout(self.tab)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 0, 0, 5)
        self.tab_bar_widget = QFrame(self.tab)
        self.tab_bar_widget.setObjectName(u"tab_bar_widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tab_bar_widget.sizePolicy().hasHeightForWidth())
        self.tab_bar_widget.setSizePolicy(sizePolicy1)
        self.tab_bar_widget.setMinimumSize(QSize(0, 30))
        self.tab_bar_widget.setMaximumSize(QSize(12000, 30))
        self.tab_bar_widget.setBaseSize(QSize(0, 0))
        self.tab_bar_widget.setStyleSheet(u"border-bottom: none;")
        self.tab_bar_widget.setFrameShape(QFrame.StyledPanel)
        self.tab_bar_widget.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.tab_bar_widget)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.minimizeButton = QPushButton(self.tab_bar_widget)
        self.minimizeButton.setObjectName(u"minimizeButton")
        self.minimizeButton.setFocusPolicy(Qt.NoFocus)
        self.minimizeButton.setStyleSheet(u"QPushButton:hover{\n"
"	\n"
"	\n"
"	icon: url(:/icons-hover/icons-hover/minus.svg);\n"
"	\n"
"	\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/icons/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeButton.setIcon(icon)
        self.minimizeButton.setIconSize(QSize(18, 18))

        self.horizontalLayout_3.addWidget(self.minimizeButton)

        self.xButton = QPushButton(self.tab_bar_widget)
        self.xButton.setObjectName(u"xButton")
        self.xButton.setFocusPolicy(Qt.NoFocus)
        self.xButton.setStyleSheet(u"QPushButton:hover{\n"
"	\n"
"	\n"
"	icon: url(:/icons-hover/icons-hover/x.svg);\n"
"	\n"
"	\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.xButton.setIcon(icon1)
        self.xButton.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.xButton)


        self.horizontalLayout_4.addWidget(self.tab_bar_widget, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout_7.addWidget(self.tab)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(7)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 50))
        font = QFont()
        font.setFamily(u"Eight Bit Dragon")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet(u"font: 15pt \"Eight Bit Dragon\";\n"
"color: rgb(255, 255, 255);")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(7)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 10)
        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(320, 30))
        self.lineEdit.setMaximumSize(QSize(320, 16777215))
        self.lineEdit.setFocusPolicy(Qt.StrongFocus)
        self.lineEdit.setStyleSheet(u"font: 8pt \"Eight Bit Dragon\";\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid white;\n"
"border-radius: 10px;")

        self.horizontalLayout.addWidget(self.lineEdit)

        self.generateButton = QPushButton(Dialog)
        self.generateButton.setObjectName(u"generateButton")
        self.generateButton.setMinimumSize(QSize(150, 40))
        self.generateButton.setMaximumSize(QSize(150, 16777215))
        self.generateButton.setFocusPolicy(Qt.NoFocus)
        self.generateButton.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout.addWidget(self.generateButton)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.tabWidget = QTabWidget(Dialog)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy2)
        palette = QPalette()
        brush = QBrush(QColor(255, 185, 139, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.tabWidget.setPalette(palette)
        self.tabWidget.setCursor(QCursor(Qt.PointingHandCursor))
        self.tabWidget.setTabletTracking(False)
        self.tabWidget.setFocusPolicy(Qt.NoFocus)
        self.tabWidget.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.tabWidget.setAcceptDrops(False)
        self.tabWidget.setToolTipDuration(-2)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet(u"QTabBar::tab {\n"
"	background-color: rgb(40,40, 32);\n"
"	color: white;\n"
"	font: 8pt \"Eight Bit Dragon\";\n"
"	border: 2px solid black;\n"
"	border-color: rgb(64, 64, 64);\n"
"	border-top-left-radius: 8px;\n"
"	border-top-right-radius: 8px;\n"
"	width: 30px;\n"
"	height: 30px;\n"
"	\n"
"\n"
"	\n"
"}\n"
"QTabBar::tab::hover {\n"
"	background-color: rgb(80, 80, 80);\n"
"	color: white;\n"
"	font: 8pt \"Eight Bit Dragon\";\n"
"	border: 2px solid black;\n"
"	\n"
"	\n"
"	\n"
"}\n"
"\n"
"QTabBar::tab::selected {\n"
"\n"
"	background-color: rgb(255, 129, 60);\n"
"	color: white;\n"
"	font: 8pt \"Eight Bit Dragon\";\n"
"	border: 2px solid black;\n"
"	\n"
"	\n"
"	\n"
"}\n"
"\n"
"*{\n"
"border: none;\n"
"font: 10pt \"Eight Bit Dragon\";\n"
"background-color: rgb(255, 185, 139);\n"
"}\n"
"\n"
"")
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setTabBarAutoHide(False)

        self.verticalLayout_2.addWidget(self.tabWidget)


        self.verticalLayout_7.addLayout(self.verticalLayout_2)

        self.selectallLayout = QHBoxLayout()
        self.selectallLayout.setSpacing(0)
        self.selectallLayout.setObjectName(u"selectallLayout")
        self.widget_2 = QWidget(Dialog)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMaximumSize(QSize(16777215, 40))
        self.widget_2.setStyleSheet(u"\n"
"background-color: rgb(255, 185, 139);")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 5, 0, 5)
        self.selectButton = QPushButton(self.widget_2)
        self.selectButton.setObjectName(u"selectButton")
        self.selectButton.setMinimumSize(QSize(120, 30))
        self.selectButton.setMaximumSize(QSize(120, 50))
        font1 = QFont()
        font1.setFamily(u"Eight Bit Dragon")
        font1.setPointSize(8)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(50)
        self.selectButton.setFont(font1)
        self.selectButton.setStyleSheet(u"QPushButton{\n"
"font: 8pt \"Eight Bit Dragon\";\n"
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

        self.horizontalLayout_5.addWidget(self.selectButton, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.selectallLayout.addWidget(self.widget_2)


        self.verticalLayout_7.addLayout(self.selectallLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 10, -1, -1)
        self.listoButton = QPushButton(Dialog)
        self.listoButton.setObjectName(u"listoButton")
        self.listoButton.setMaximumSize(QSize(16777215, 40))
        self.listoButton.setFocusPolicy(Qt.NoFocus)
        self.listoButton.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout_2.addWidget(self.listoButton)

        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.resetButton = QPushButton(self.frame)
        self.resetButton.setObjectName(u"resetButton")
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.resetButton.sizePolicy().hasHeightForWidth())
        self.resetButton.setSizePolicy(sizePolicy3)
        self.resetButton.setMinimumSize(QSize(80, 40))
        self.resetButton.setFocusPolicy(Qt.NoFocus)
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

        self.horizontalLayout_6.addWidget(self.resetButton)

        self.resetButton_2 = QPushButton(self.frame)
        self.resetButton_2.setObjectName(u"resetButton_2")
        sizePolicy3.setHeightForWidth(self.resetButton_2.sizePolicy().hasHeightForWidth())
        self.resetButton_2.setSizePolicy(sizePolicy3)
        self.resetButton_2.setMinimumSize(QSize(80, 40))
        self.resetButton_2.setFocusPolicy(Qt.NoFocus)
        self.resetButton_2.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout_6.addWidget(self.resetButton_2)


        self.horizontalLayout_2.addWidget(self.frame)


        self.verticalLayout_7.addLayout(self.horizontalLayout_2)


        self.retranslateUi(Dialog)

        self.tabWidget.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"RPG_Peptide-Selection", None))
#if QT_CONFIG(tooltip)
        self.minimizeButton.setToolTip(QCoreApplication.translate("Dialog", u"Minimize Window", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeButton.setText("")
#if QT_CONFIG(tooltip)
        self.xButton.setToolTip(QCoreApplication.translate("Dialog", u"Close Window", None))
#endif // QT_CONFIG(tooltip)
        self.xButton.setText("")
        self.label.setText(QCoreApplication.translate("Dialog", u"Insert  Length of your Peptide", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"Insert any number between 2-12", None))
        self.generateButton.setText(QCoreApplication.translate("Dialog", u"Generate", None))
        self.selectButton.setText(QCoreApplication.translate("Dialog", u"Select All", None))
        self.listoButton.setText(QCoreApplication.translate("Dialog", u"Ready!", None))
        self.resetButton.setText(QCoreApplication.translate("Dialog", u"Reset", None))
        self.resetButton_2.setText(QCoreApplication.translate("Dialog", u"Check", None))
    # retranslateUi

