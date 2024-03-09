# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'windowkKhbhb.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import resources
class Ui_Window(object):
    def setupUi(self, Window):
        if not Window.objectName():
            Window.setObjectName(u"Window")
        Window.resize(1000, 985)
        Window.setStyleSheet(u"\n"
"*{\n"
"	background-color: rgb(100, 100,100);\n"
"\n"
"}")
        self.centralwidget = QWidget(Window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(1000, 800))
        self.centralwidget.setStyleSheet(u"QFrame {\n"
"\n"
"			border: none;\n"
"\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 30))
        self.widget.setMaximumSize(QSize(16777215, 30))
        self.widget.setStyleSheet(u"background-color: rgb(30, 30, 20);")
        self.horizontalLayout_3 = QHBoxLayout(self.widget)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.tab_bar_widget = QFrame(self.widget)
        self.tab_bar_widget.setObjectName(u"tab_bar_widget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_bar_widget.sizePolicy().hasHeightForWidth())
        self.tab_bar_widget.setSizePolicy(sizePolicy)
        self.tab_bar_widget.setMinimumSize(QSize(120, 30))
        self.tab_bar_widget.setMaximumSize(QSize(16777215, 30))
        self.tab_bar_widget.setBaseSize(QSize(0, 0))
        self.tab_bar_widget.setStyleSheet(u"")
        self.tab_bar_widget.setFrameShape(QFrame.StyledPanel)
        self.tab_bar_widget.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.tab_bar_widget)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
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

        self.horizontalLayout_2.addWidget(self.minimizeButton)

        self.squareButton = QPushButton(self.tab_bar_widget)
        self.squareButton.setObjectName(u"squareButton")
        self.squareButton.setFocusPolicy(Qt.NoFocus)
        self.squareButton.setStyleSheet(u"QPushButton:hover{\n"
"	\n"
"	\n"
"	icon: url(:/icons-hover/icons-hover/square.svg);\n"
"	\n"
"	\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.squareButton.setIcon(icon1)
        self.squareButton.setIconSize(QSize(14, 14))

        self.horizontalLayout_2.addWidget(self.squareButton)

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
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.xButton.setIcon(icon2)
        self.xButton.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.xButton)


        self.horizontalLayout_3.addWidget(self.tab_bar_widget, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.widget)

        self.RPG_tab_widget = QWidget(self.centralwidget)
        self.RPG_tab_widget.setObjectName(u"RPG_tab_widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.RPG_tab_widget.sizePolicy().hasHeightForWidth())
        self.RPG_tab_widget.setSizePolicy(sizePolicy1)
        self.RPG_tab_widget.setMinimumSize(QSize(0, 80))
        self.RPG_tab_widget.setMaximumSize(QSize(16777215, 150))
        self.RPG_tab_widget.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(11, 11, 0);\n"
"	background-color: rgb(255, 185, 139);\n"
"	border-style: solid;\n"
"	border-color: white;\n"
"	border-bottom-width: 0px;\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.RPG_tab_widget)
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.RPG_title = QLabel(self.RPG_tab_widget)
        self.RPG_title.setObjectName(u"RPG_title")
        self.RPG_title.setMinimumSize(QSize(0, 70))
        font = QFont()
        font.setFamily(u"Eight Bit Dragon")
        font.setPointSize(40)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.RPG_title.setFont(font)
        self.RPG_title.setLayoutDirection(Qt.LeftToRight)
        self.RPG_title.setStyleSheet(u"font: 40pt \"Eight Bit Dragon\";\n"
"color: rgb(255, 255, 255);\n"
"border: none;\n"
"background-color: transparent;")
        self.RPG_title.setAlignment(Qt.AlignCenter)
        self.RPG_title.setWordWrap(False)
        self.RPG_title.setMargin(0)

        self.horizontalLayout.addWidget(self.RPG_title, 0, Qt.AlignLeft)

        self.title = QLabel(self.RPG_tab_widget)
        self.title.setObjectName(u"title")
        font1 = QFont()
        font1.setFamily(u"Eight Bit Dragon")
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(50)
        self.title.setFont(font1)
        self.title.setStyleSheet(u"font: 10pt \"Eight Bit Dragon\";\n"
"border: none;\n"
"background-color: transparent;")

        self.horizontalLayout.addWidget(self.title)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.helpButton = QPushButton(self.RPG_tab_widget)
        self.helpButton.setObjectName(u"helpButton")
        self.helpButton.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(50)
        sizePolicy2.setVerticalStretch(50)
        sizePolicy2.setHeightForWidth(self.helpButton.sizePolicy().hasHeightForWidth())
        self.helpButton.setSizePolicy(sizePolicy2)
        self.helpButton.setMinimumSize(QSize(50, 50))
        self.helpButton.setMaximumSize(QSize(50, 50))
        self.helpButton.setBaseSize(QSize(50, 50))
        self.helpButton.setFocusPolicy(Qt.NoFocus)
#if QT_CONFIG(tooltip)
        self.helpButton.setToolTip(u"About the App")
#endif // QT_CONFIG(tooltip)
        self.helpButton.setAutoFillBackground(False)
        self.helpButton.setStyleSheet(u"*{\n"
"	border: none;\n"
"	background-color: transparent;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	icon: url(:/icons-hover/icons-hover/help-circle.svg);\n"
"\n"
"	\n"
"	\n"
"}")
        self.helpButton.setText(u"")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/help-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.helpButton.setIcon(icon3)
        self.helpButton.setIconSize(QSize(24, 24))
#if QT_CONFIG(shortcut)
        self.helpButton.setShortcut(u"")
#endif // QT_CONFIG(shortcut)
        self.helpButton.setCheckable(False)

        self.horizontalLayout.addWidget(self.helpButton)


        self.verticalLayout_2.addWidget(self.RPG_tab_widget)

        self.general_frame = QFrame(self.centralwidget)
        self.general_frame.setObjectName(u"general_frame")
        self.general_frame.setMinimumSize(QSize(500, 300))
        self.general_frame.setStyleSheet(u"font: 12pt \"Eight Bit Dragon\";")
        self.horizontalLayout_4 = QHBoxLayout(self.general_frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.tab_frame = QFrame(self.general_frame)
        self.tab_frame.setObjectName(u"tab_frame")
        self.tab_frame.setMinimumSize(QSize(90, 0))
        self.tab_frame.setMaximumSize(QSize(40, 16777215))
        self.tab_frame.setAutoFillBackground(False)
        self.tab_frame.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: white;")
        self.tab_frame.setFrameShape(QFrame.StyledPanel)
        self.tab_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.tab_frame)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.tab_frame_cont = QFrame(self.tab_frame)
        self.tab_frame_cont.setObjectName(u"tab_frame_cont")
        self.tab_frame_cont.setMinimumSize(QSize(90, 300))
        self.tab_frame_cont.setStyleSheet(u"QPushButton {\n"
"\n"
"font: 14pt \"VT323\";\n"
"\n"
"}\n"
"QLabel {\n"
"\n"
"font: 8pt \"VT323\";\n"
"\n"
"}")
        self.tab_frame_cont.setFrameShape(QFrame.StyledPanel)
        self.tab_frame_cont.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.tab_frame_cont)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(8, 0, 0, 0)
        self.homeButton = QPushButton(self.tab_frame_cont)
        self.homeButton.setObjectName(u"homeButton")
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.homeButton.sizePolicy().hasHeightForWidth())
        self.homeButton.setSizePolicy(sizePolicy3)
        self.homeButton.setMinimumSize(QSize(70, 0))
        self.homeButton.setMaximumSize(QSize(40, 40))
        self.homeButton.setFocusPolicy(Qt.NoFocus)
        self.homeButton.setStyleSheet(u"QPushButton:hover{\n"
"	\n"
"	\n"
"	icon: url(:/icons-hover/icons-hover/home.svg);\n"
"	\n"
"	\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon4.addFile(u":/icons/icons/home.svg", QSize(), QIcon.Normal, QIcon.On)
        icon4.addFile(u":/icons-hover/icons-hover/home.svg", QSize(), QIcon.Selected, QIcon.On)
        self.homeButton.setIcon(icon4)
        self.homeButton.setIconSize(QSize(30, 30))

        self.verticalLayout_12.addWidget(self.homeButton)

        self.stage1Button = QPushButton(self.tab_frame_cont)
        self.stage1Button.setObjectName(u"stage1Button")
        sizePolicy.setHeightForWidth(self.stage1Button.sizePolicy().hasHeightForWidth())
        self.stage1Button.setSizePolicy(sizePolicy)
        self.stage1Button.setMinimumSize(QSize(70, 40))
        self.stage1Button.setMaximumSize(QSize(50, 40))
        font2 = QFont()
        font2.setFamily(u"Eight Bit Dragon")
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setWeight(50)
        font2.setKerning(False)
        font2.setStyleStrategy(QFont.PreferDefault)
        self.stage1Button.setFont(font2)
        self.stage1Button.setFocusPolicy(Qt.NoFocus)
        self.stage1Button.setStyleSheet(u"QPushButton{\n"
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
        self.stage1Button.setText(u"Stage 1")

        self.verticalLayout_12.addWidget(self.stage1Button)

        self.stage2Button = QPushButton(self.tab_frame_cont)
        self.stage2Button.setObjectName(u"stage2Button")
        sizePolicy.setHeightForWidth(self.stage2Button.sizePolicy().hasHeightForWidth())
        self.stage2Button.setSizePolicy(sizePolicy)
        self.stage2Button.setMinimumSize(QSize(70, 40))
        self.stage2Button.setMaximumSize(QSize(50, 40))
        self.stage2Button.setFocusPolicy(Qt.NoFocus)
        self.stage2Button.setStyleSheet(u"QPushButton{\n"
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

        self.verticalLayout_12.addWidget(self.stage2Button)

        self.stage3Button = QPushButton(self.tab_frame_cont)
        self.stage3Button.setObjectName(u"stage3Button")
        sizePolicy.setHeightForWidth(self.stage3Button.sizePolicy().hasHeightForWidth())
        self.stage3Button.setSizePolicy(sizePolicy)
        self.stage3Button.setMinimumSize(QSize(70, 40))
        self.stage3Button.setMaximumSize(QSize(50, 40))
        self.stage3Button.setFocusPolicy(Qt.NoFocus)
        self.stage3Button.setStyleSheet(u"QPushButton{\n"
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

        self.verticalLayout_12.addWidget(self.stage3Button)

        self.stage4Button = QPushButton(self.tab_frame_cont)
        self.stage4Button.setObjectName(u"stage4Button")
        sizePolicy.setHeightForWidth(self.stage4Button.sizePolicy().hasHeightForWidth())
        self.stage4Button.setSizePolicy(sizePolicy)
        self.stage4Button.setMinimumSize(QSize(70, 40))
        self.stage4Button.setMaximumSize(QSize(50, 40))
        self.stage4Button.setFocusPolicy(Qt.NoFocus)
        self.stage4Button.setStyleSheet(u"QPushButton{\n"
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

        self.verticalLayout_12.addWidget(self.stage4Button)


        self.horizontalLayout_5.addWidget(self.tab_frame_cont, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.horizontalLayout_4.addWidget(self.tab_frame)

        self.main_frame = QFrame(self.general_frame)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setMinimumSize(QSize(0, 0))
        self.main_frame.setMaximumSize(QSize(16777215, 16777215))
        self.main_frame.setAutoFillBackground(False)
        self.main_frame.setStyleSheet(u"*{\n"
"background-color: rgb(40,40, 32);\n"
"color: white;\n"
"}\n"
"\n"
"\n"
"")
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.main_frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 10, 0, 0)
        self.stackedWidget = QStackedWidget(self.main_frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(0, 0))
        self.stackedWidget.setAutoFillBackground(False)
        self.stackedWidget.setStyleSheet(u"")
        self.stackedWidget.setLineWidth(0)
        self.homePage = QWidget()
        self.homePage.setObjectName(u"homePage")
        self.verticalLayout_6 = QVBoxLayout(self.homePage)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 20)
        self.top_frame_home = QFrame(self.homePage)
        self.top_frame_home.setObjectName(u"top_frame_home")
        self.top_frame_home.setMaximumSize(QSize(1000, 130))
        self.top_frame_home.setFrameShape(QFrame.StyledPanel)
        self.top_frame_home.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.top_frame_home)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(-1, 20, -1, 30)
        self.top_label_2 = QLabel(self.top_frame_home)
        self.top_label_2.setObjectName(u"top_label_2")
        self.top_label_2.setMinimumSize(QSize(0, 100))
        self.top_label_2.setMaximumSize(QSize(16777215, 100))

        self.verticalLayout_7.addWidget(self.top_label_2, 0, Qt.AlignTop)


        self.verticalLayout_6.addWidget(self.top_frame_home, 0, Qt.AlignHCenter)

        self.label_9 = QLabel(self.homePage)
        self.label_9.setObjectName(u"label_9")
        font3 = QFont()
        font3.setFamily(u"Eight Bit Dragon")
        font3.setPointSize(16)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setWeight(50)
        self.label_9.setFont(font3)
        self.label_9.setStyleSheet(u"font: 16pt \"Eight Bit Dragon\";")

        self.verticalLayout_6.addWidget(self.label_9)

        self.mid_frame_home = QFrame(self.homePage)
        self.mid_frame_home.setObjectName(u"mid_frame_home")
        sizePolicy3.setHeightForWidth(self.mid_frame_home.sizePolicy().hasHeightForWidth())
        self.mid_frame_home.setSizePolicy(sizePolicy3)
        self.mid_frame_home.setMinimumSize(QSize(905, 180))
        self.mid_frame_home.setStyleSheet(u"QPushButton{\n"
"font: 14pt \"Eight Bit Dragon\";\n"
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
        self.mid_frame_home.setFrameShape(QFrame.StyledPanel)
        self.mid_frame_home.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.mid_frame_home)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(-1, 0, -1, -1)
        self.newgameButton = QPushButton(self.mid_frame_home)
        self.newgameButton.setObjectName(u"newgameButton")
        self.newgameButton.setMaximumSize(QSize(160, 80))

        self.horizontalLayout_8.addWidget(self.newgameButton)

        self.continueButton = QPushButton(self.mid_frame_home)
        self.continueButton.setObjectName(u"continueButton")
        self.continueButton.setMaximumSize(QSize(160, 80))

        self.horizontalLayout_8.addWidget(self.continueButton)


        self.verticalLayout_6.addWidget(self.mid_frame_home)

        self.frame = QFrame(self.homePage)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(-1, 30, -1, -1)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        font4 = QFont()
        font4.setFamily(u"Eight Bit Dragon")
        font4.setPointSize(12)
        font4.setBold(False)
        font4.setItalic(False)
        font4.setWeight(50)
        self.label_2.setFont(font4)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_2)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")

        self.horizontalLayout_9.addWidget(self.label)

        self.pushButton_2 = QPushButton(self.frame_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"border: none;")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/external-link.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon5)

        self.horizontalLayout_9.addWidget(self.pushButton_2)


        self.verticalLayout_8.addWidget(self.frame_2, 0, Qt.AlignHCenter)


        self.verticalLayout_6.addWidget(self.frame, 0, Qt.AlignTop)

        self.labicon_frame = QFrame(self.homePage)
        self.labicon_frame.setObjectName(u"labicon_frame")
        self.labicon_frame.setFrameShape(QFrame.StyledPanel)
        self.labicon_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.labicon_frame)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.labiconButton = QPushButton(self.labicon_frame)
        self.labiconButton.setObjectName(u"labiconButton")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.labiconButton.sizePolicy().hasHeightForWidth())
        self.labiconButton.setSizePolicy(sizePolicy4)
        self.labiconButton.setMinimumSize(QSize(300, 300))
        self.labiconButton.setMaximumSize(QSize(200, 200))
        self.labiconButton.setStyleSheet(u"*{\n"
"background-color: transparent;\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	\n"
"	icon: url(:/logo/icons/Lab2.png);\n"
"	\n"
"	\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/logo/Lab1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.labiconButton.setIcon(icon6)
        self.labiconButton.setIconSize(QSize(720, 300))

        self.verticalLayout_16.addWidget(self.labiconButton, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.verticalLayout_6.addWidget(self.labicon_frame)

        self.stackedWidget.addWidget(self.homePage)
        self.stage1 = QWidget()
        self.stage1.setObjectName(u"stage1")
        self.stage1.setStyleSheet(u"QFrame#mid_frame,#top_frame {\n"
"\n"
"			border-bottom: 2px solid white;\n"
"\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.stage1)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.top_frame = QFrame(self.stage1)
        self.top_frame.setObjectName(u"top_frame")
        self.top_frame.setMinimumSize(QSize(950, 200))
        self.top_frame.setMaximumSize(QSize(1800, 200))
        self.top_frame.setFrameShape(QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.top_frame)
        self.horizontalLayout_6.setSpacing(80)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 9, 0)
        self.label_3 = QLabel(self.top_frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(150, 30))
        self.label_3.setMaximumSize(QSize(150, 16777215))
        self.label_3.setStyleSheet(u"font:bold 12pt \"Eight Bit Dragon\";\n"
"color: rgb(255, 185, 139);")

        self.horizontalLayout_6.addWidget(self.label_3, 0, Qt.AlignVCenter)

        self.label_4 = QLabel(self.top_frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(350, 200))
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"font: 10pt \"Eight Bit Dragon\";\n"
"background-color:transparent;")
        self.label_4.setMargin(5)

        self.horizontalLayout_6.addWidget(self.label_4)

        self.setpepButton = QPushButton(self.top_frame)
        self.setpepButton.setObjectName(u"setpepButton")
        sizePolicy.setHeightForWidth(self.setpepButton.sizePolicy().hasHeightForWidth())
        self.setpepButton.setSizePolicy(sizePolicy)
        self.setpepButton.setMinimumSize(QSize(150, 150))
        self.setpepButton.setMaximumSize(QSize(150, 150))
        self.setpepButton.setFocusPolicy(Qt.NoFocus)
        self.setpepButton.setStyleSheet(u"#setpepButton{\n"
"border: 1px solid grey;\n"
"border-radius: 75px;\n"
"background-color: rgb(80, 80, 80);\n"
"border: 0px solid;\n"
"border-bottom: 2px solid shadow;\n"
"border-left: 2px solid;\n"
"border-right: 2px solid;\n"
"background-color: rgb(86, 86, 86);\n"
"border-color: rgb(64, 64, 64);\n"
"\n"
"}\n"
"#setpepButton:hover{\n"
"border: 1px solid grey;\n"
"border-radius: 75px;\n"
"background-color: rgb(0, 0, 0);\n"
"border: 0px solid;\n"
"border-bottom: 2px solid shadow;\n"
"border-left: 2px solid;\n"
"border-right: 2px solid;\n"
"background-color: rgb(120, 120, 120);\n"
"border-color: rgb(64, 64, 64);\n"
"}\n"
"")
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/atoms-white.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.setpepButton.setIcon(icon7)
        self.setpepButton.setIconSize(QSize(120, 120))

        self.horizontalLayout_6.addWidget(self.setpepButton)


        self.verticalLayout_3.addWidget(self.top_frame, 0, Qt.AlignLeft|Qt.AlignTop)

        self.mid_frame = QFrame(self.stage1)
        self.mid_frame.setObjectName(u"mid_frame")
        self.mid_frame.setEnabled(True)
        sizePolicy.setHeightForWidth(self.mid_frame.sizePolicy().hasHeightForWidth())
        self.mid_frame.setSizePolicy(sizePolicy)
        self.mid_frame.setMinimumSize(QSize(0, 200))
        self.mid_frame.setMaximumSize(QSize(1800, 200))
        self.mid_frame.setFrameShape(QFrame.StyledPanel)
        self.mid_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.mid_frame)
        self.verticalLayout_4.setSpacing(30)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 40, 0, 30)
        self.listnameFrame = QFrame(self.mid_frame)
        self.listnameFrame.setObjectName(u"listnameFrame")
        self.listnameFrame.setMinimumSize(QSize(0, 50))
        self.listnameFrame.setMaximumSize(QSize(16777215, 50))
        self.listnameFrame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_7 = QHBoxLayout(self.listnameFrame)
        self.horizontalLayout_7.setSpacing(40)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(30, -1, 20, -1)
        self.label_6 = QLabel(self.listnameFrame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(200, 16777215))
        self.label_6.setStyleSheet(u"font:bold 12pt \"Eight Bit Dragon\";\n"
"color: rgb(255, 185, 139);")

        self.horizontalLayout_7.addWidget(self.label_6)

        self.horizontalSpacer_3 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_3)

        self.directoryButton = QPushButton(self.listnameFrame)
        self.directoryButton.setObjectName(u"directoryButton")
        self.directoryButton.setMinimumSize(QSize(280, 40))
        self.directoryButton.setMaximumSize(QSize(320, 16777215))
        self.directoryButton.setFocusPolicy(Qt.NoFocus)
        self.directoryButton.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout_7.addWidget(self.directoryButton)


        self.verticalLayout_4.addWidget(self.listnameFrame, 0, Qt.AlignLeft)


        self.verticalLayout_3.addWidget(self.mid_frame)

        self.bottom_frame = QFrame(self.stage1)
        self.bottom_frame.setObjectName(u"bottom_frame")
        self.bottom_frame.setMinimumSize(QSize(0, 350))
        self.bottom_frame.setMaximumSize(QSize(16777215, 400))
        self.bottom_frame.setFrameShape(QFrame.StyledPanel)
        self.bottom_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.bottom_frame)
        self.verticalLayout_5.setSpacing(20)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(25, 9, 20, 9)
        self.label_7 = QLabel(self.bottom_frame)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_5.addWidget(self.label_7)

        self.textEdit = QTextEdit(self.bottom_frame)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(0, 50))
        self.textEdit.setMaximumSize(QSize(16777215, 50))

        self.verticalLayout_5.addWidget(self.textEdit, 0, Qt.AlignTop)

        self.gotostage2Button = QPushButton(self.bottom_frame)
        self.gotostage2Button.setObjectName(u"gotostage2Button")
        self.gotostage2Button.setMinimumSize(QSize(200, 40))
        self.gotostage2Button.setMaximumSize(QSize(200, 40))
        self.gotostage2Button.setFocusPolicy(Qt.NoFocus)
        self.gotostage2Button.setStyleSheet(u"QPushButton{\n"
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

        self.verticalLayout_5.addWidget(self.gotostage2Button, 0, Qt.AlignHCenter)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)


        self.verticalLayout_3.addWidget(self.bottom_frame)

        self.stackedWidget.addWidget(self.stage1)
        self.stage2 = QWidget()
        self.stage2.setObjectName(u"stage2")
        self.verticalLayout_9 = QVBoxLayout(self.stage2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_3 = QFrame(self.stage2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.frame_newgame = QFrame(self.frame_3)
        self.frame_newgame.setObjectName(u"frame_newgame")
        self.frame_newgame.setFrameShape(QFrame.StyledPanel)
        self.frame_newgame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_newgame)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_stage2_newgame = QLabel(self.frame_newgame)
        self.label_stage2_newgame.setObjectName(u"label_stage2_newgame")
        self.label_stage2_newgame.setEnabled(True)

        self.verticalLayout_13.addWidget(self.label_stage2_newgame)

        self.label_5 = QLabel(self.frame_newgame)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_13.addWidget(self.label_5)

        self.frame_8 = QFrame(self.frame_newgame)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.stage2_selectButton = QPushButton(self.frame_8)
        self.stage2_selectButton.setObjectName(u"stage2_selectButton")
        self.stage2_selectButton.setMinimumSize(QSize(200, 40))
        self.stage2_selectButton.setMaximumSize(QSize(200, 40))
        self.stage2_selectButton.setFocusPolicy(Qt.NoFocus)
        self.stage2_selectButton.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout_14.addWidget(self.stage2_selectButton)


        self.verticalLayout_13.addWidget(self.frame_8)

        self.frame_7 = QFrame(self.frame_newgame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_8 = QLabel(self.frame_7)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_13.addWidget(self.label_8)

        self.spinBox = QSpinBox(self.frame_7)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMinimumSize(QSize(70, 30))
        self.spinBox.setMaximumSize(QSize(60, 30))
        self.spinBox.setStyleSheet(u"font: 10pt \"Eight Bit Dragon\";\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid black;\n"
"background-color: rgb(40,40, 32);\n"
"border-color: rgb(100, 100, 100);\n"
"")
        self.spinBox.setMaximum(10000)
        self.spinBox.setValue(10)

        self.horizontalLayout_13.addWidget(self.spinBox)


        self.verticalLayout_13.addWidget(self.frame_7)

        self.runchimButton = QPushButton(self.frame_newgame)
        self.runchimButton.setObjectName(u"runchimButton")
        self.runchimButton.setMinimumSize(QSize(200, 40))
        self.runchimButton.setMaximumSize(QSize(200, 40))
        self.runchimButton.setFocusPolicy(Qt.NoFocus)
        self.runchimButton.setStyleSheet(u"QPushButton{\n"
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

        self.verticalLayout_13.addWidget(self.runchimButton, 0, Qt.AlignHCenter)


        self.horizontalLayout_10.addWidget(self.frame_newgame)


        self.verticalLayout_9.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.stage2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_4)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_working = QLabel(self.frame_4)
        self.label_working.setObjectName(u"label_working")

        self.verticalLayout_14.addWidget(self.label_working)

        self.progressBar_2 = QProgressBar(self.frame_4)
        self.progressBar_2.setObjectName(u"progressBar_2")
        self.progressBar_2.setMinimumSize(QSize(600, 20))
        self.progressBar_2.setMaximumSize(QSize(600, 16777215))
        self.progressBar_2.setStyleSheet(u"QProgressBar{\n"
"    border: 2px solid grey;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"	\n"
"	border-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: rgb(255, 130, 70);\n"
"	margin: 1px;\n"
"	width: 10px;\n"
"    \n"
"}")
        self.progressBar_2.setValue(24)

        self.verticalLayout_14.addWidget(self.progressBar_2, 0, Qt.AlignHCenter)

        self.label_done = QLabel(self.frame_4)
        self.label_done.setObjectName(u"label_done")

        self.verticalLayout_14.addWidget(self.label_done)

        self.gotostage3Button = QPushButton(self.frame_4)
        self.gotostage3Button.setObjectName(u"gotostage3Button")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(200)
        sizePolicy5.setVerticalStretch(40)
        sizePolicy5.setHeightForWidth(self.gotostage3Button.sizePolicy().hasHeightForWidth())
        self.gotostage3Button.setSizePolicy(sizePolicy5)
        self.gotostage3Button.setMinimumSize(QSize(200, 40))
        self.gotostage3Button.setMaximumSize(QSize(200, 40))
        self.gotostage3Button.setFocusPolicy(Qt.NoFocus)
        self.gotostage3Button.setStyleSheet(u"QPushButton{\n"
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

        self.verticalLayout_14.addWidget(self.gotostage3Button, 0, Qt.AlignHCenter)


        self.verticalLayout_9.addWidget(self.frame_4)

        self.stackedWidget.addWidget(self.stage2)
        self.stage3 = QWidget()
        self.stage3.setObjectName(u"stage3")
        self.verticalLayout_10 = QVBoxLayout(self.stage3)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_5 = QFrame(self.stage3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"QFrame#Continue_stage3,#First_Stage3,#Second_Stage3{\n"
"\n"
"			border-bottom: 2px solid white;\n"
"}")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_5)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.frame_12 = QFrame(self.frame_5)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_stage3_NewGame = QLabel(self.frame_12)
        self.label_stage3_NewGame.setObjectName(u"label_stage3_NewGame")

        self.horizontalLayout_19.addWidget(self.label_stage3_NewGame)

        self.label_stage3_Continue = QLabel(self.frame_12)
        self.label_stage3_Continue.setObjectName(u"label_stage3_Continue")

        self.horizontalLayout_19.addWidget(self.label_stage3_Continue)


        self.verticalLayout_15.addWidget(self.frame_12, 0, Qt.AlignHCenter)

        self.Continue_stage3 = QFrame(self.frame_5)
        self.Continue_stage3.setObjectName(u"Continue_stage3")
        self.Continue_stage3.setMinimumSize(QSize(0, 150))
        self.Continue_stage3.setMaximumSize(QSize(16777215, 150))
        self.Continue_stage3.setStyleSheet(u"")
        self.Continue_stage3.setFrameShape(QFrame.StyledPanel)
        self.Continue_stage3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.Continue_stage3)
        self.horizontalLayout_15.setSpacing(6)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(9, 9, 9, -1)
        self.label_17 = QLabel(self.Continue_stage3)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMaximumSize(QSize(200, 120))
        self.label_17.setStyleSheet(u"font:bold 12pt \"Eight Bit Dragon\";\n"
"color: rgb(255, 185, 139);")

        self.horizontalLayout_15.addWidget(self.label_17)

        self.frame_18 = QFrame(self.Continue_stage3)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setStyleSheet(u"border: none;")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.frame_18.setLineWidth(0)
        self.verticalLayout_19 = QVBoxLayout(self.frame_18)
        self.verticalLayout_19.setSpacing(15)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_10 = QLabel(self.frame_18)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_19.addWidget(self.label_10)

        self.select_stage3Button = QPushButton(self.frame_18)
        self.select_stage3Button.setObjectName(u"select_stage3Button")
        self.select_stage3Button.setMinimumSize(QSize(200, 30))
        self.select_stage3Button.setMaximumSize(QSize(200, 30))
        self.select_stage3Button.setFocusPolicy(Qt.NoFocus)
        self.select_stage3Button.setStyleSheet(u"QPushButton{\n"
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

        self.verticalLayout_19.addWidget(self.select_stage3Button, 0, Qt.AlignHCenter)


        self.horizontalLayout_15.addWidget(self.frame_18)


        self.verticalLayout_15.addWidget(self.Continue_stage3)

        self.First_Stage3 = QFrame(self.frame_5)
        self.First_Stage3.setObjectName(u"First_Stage3")
        self.First_Stage3.setMinimumSize(QSize(0, 150))
        self.First_Stage3.setMaximumSize(QSize(16777215, 150))
        self.First_Stage3.setFrameShape(QFrame.StyledPanel)
        self.First_Stage3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.First_Stage3)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_12 = QLabel(self.First_Stage3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(200, 120))
        self.label_12.setMaximumSize(QSize(200, 120))
        self.label_12.setStyleSheet(u"font:bold 12pt \"Eight Bit Dragon\";\n"
"color: rgb(255, 185, 139);")

        self.horizontalLayout_16.addWidget(self.label_12)

        self.frame_15 = QFrame(self.First_Stage3)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_15)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_14 = QLabel(self.frame_15)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_18.addWidget(self.label_14)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_18 = QLabel(self.frame_15)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMaximumSize(QSize(500, 16777215))
        self.label_18.setFont(font4)

        self.horizontalLayout_22.addWidget(self.label_18, 0, Qt.AlignHCenter)

        self.spinBox_2 = QSpinBox(self.frame_15)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setMaximumSize(QSize(80, 16777215))
        self.spinBox_2.setStyleSheet(u"font: 10pt \"Eight Bit Dragon\";\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid black;\n"
"background-color: rgb(40,40, 32);\n"
"border-color: rgb(100, 100, 100);\n"
"")
        self.spinBox_2.setMaximum(10000)
        self.spinBox_2.setValue(100)

        self.horizontalLayout_22.addWidget(self.spinBox_2)


        self.verticalLayout_18.addLayout(self.horizontalLayout_22)

        self.obconvertButton = QPushButton(self.frame_15)
        self.obconvertButton.setObjectName(u"obconvertButton")
        self.obconvertButton.setMinimumSize(QSize(200, 0))
        self.obconvertButton.setMaximumSize(QSize(200, 30))
        self.obconvertButton.setFocusPolicy(Qt.NoFocus)
        self.obconvertButton.setStyleSheet(u"QPushButton{\n"
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

        self.verticalLayout_18.addWidget(self.obconvertButton, 0, Qt.AlignHCenter)


        self.horizontalLayout_16.addWidget(self.frame_15)


        self.verticalLayout_15.addWidget(self.First_Stage3)

        self.Second_Stage3 = QFrame(self.frame_5)
        self.Second_Stage3.setObjectName(u"Second_Stage3")
        self.Second_Stage3.setMinimumSize(QSize(0, 150))
        self.Second_Stage3.setMaximumSize(QSize(16777215, 150))
        self.Second_Stage3.setBaseSize(QSize(0, 0))
        self.Second_Stage3.setFrameShape(QFrame.StyledPanel)
        self.Second_Stage3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.Second_Stage3)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_13 = QLabel(self.Second_Stage3)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(200, 120))
        self.label_13.setMaximumSize(QSize(200, 120))
        self.label_13.setStyleSheet(u"font:bold 12pt \"Eight Bit Dragon\";\n"
"color: rgb(255, 185, 139);")

        self.horizontalLayout_17.addWidget(self.label_13)

        self.frame_13 = QFrame(self.Second_Stage3)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_13)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_11 = QLabel(self.frame_13)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_17.addWidget(self.label_11)

        self.frame_16 = QFrame(self.frame_13)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.selectprotein_stage3Button = QPushButton(self.frame_16)
        self.selectprotein_stage3Button.setObjectName(u"selectprotein_stage3Button")
        self.selectprotein_stage3Button.setMinimumSize(QSize(230, 0))
        self.selectprotein_stage3Button.setMaximumSize(QSize(200, 30))
        self.selectprotein_stage3Button.setFocusPolicy(Qt.NoFocus)
        self.selectprotein_stage3Button.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout_11.addWidget(self.selectprotein_stage3Button)

        self.selectpep_stage3Button = QPushButton(self.frame_16)
        self.selectpep_stage3Button.setObjectName(u"selectpep_stage3Button")
        self.selectpep_stage3Button.setMinimumSize(QSize(230, 30))
        self.selectpep_stage3Button.setMaximumSize(QSize(200, 30))
        self.selectpep_stage3Button.setFocusPolicy(Qt.NoFocus)
        self.selectpep_stage3Button.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout_11.addWidget(self.selectpep_stage3Button)


        self.verticalLayout_17.addWidget(self.frame_16)


        self.horizontalLayout_17.addWidget(self.frame_13)


        self.verticalLayout_15.addWidget(self.Second_Stage3)

        self.Third_Stage3 = QFrame(self.frame_5)
        self.Third_Stage3.setObjectName(u"Third_Stage3")
        self.Third_Stage3.setMinimumSize(QSize(0, 150))
        self.Third_Stage3.setMaximumSize(QSize(16777215, 300))
        self.Third_Stage3.setFrameShape(QFrame.StyledPanel)
        self.Third_Stage3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.Third_Stage3)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_15 = QLabel(self.Third_Stage3)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(200, 120))
        self.label_15.setMaximumSize(QSize(200, 120))
        self.label_15.setStyleSheet(u"font:bold 12pt \"Eight Bit Dragon\";\n"
"color: rgb(255, 185, 139);")

        self.horizontalLayout_18.addWidget(self.label_15)

        self.frame_19 = QFrame(self.Third_Stage3)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setStyleSheet(u"QPushButton{\n"
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
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_19)
        self.verticalLayout_20.setSpacing(30)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_16 = QLabel(self.frame_19)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(90, 50))

        self.verticalLayout_20.addWidget(self.label_16)

        self.configureVinaButton = QPushButton(self.frame_19)
        self.configureVinaButton.setObjectName(u"configureVinaButton")
        self.configureVinaButton.setMinimumSize(QSize(200, 30))
        self.configureVinaButton.setMaximumSize(QSize(200, 30))
        self.configureVinaButton.setFocusPolicy(Qt.NoFocus)
        self.configureVinaButton.setStyleSheet(u"QPushButton{\n"
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

        self.verticalLayout_20.addWidget(self.configureVinaButton, 0, Qt.AlignHCenter)

        self.runVinaButton = QPushButton(self.frame_19)
        self.runVinaButton.setObjectName(u"runVinaButton")
        self.runVinaButton.setMinimumSize(QSize(200, 30))
        self.runVinaButton.setMaximumSize(QSize(200, 30))
        self.runVinaButton.setFocusPolicy(Qt.NoFocus)
        self.runVinaButton.setStyleSheet(u"QPushButton{\n"
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

        self.verticalLayout_20.addWidget(self.runVinaButton, 0, Qt.AlignHCenter)

        self.progressBar_vina = QProgressBar(self.frame_19)
        self.progressBar_vina.setObjectName(u"progressBar_vina")
        self.progressBar_vina.setStyleSheet(u"QProgressBar{\n"
"    border: 2px solid grey;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"	\n"
"	border-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: rgb(255, 130, 70);\n"
"	margin: 1px;\n"
"	width: 10px;\n"
"    \n"
"}")
        self.progressBar_vina.setValue(24)

        self.verticalLayout_20.addWidget(self.progressBar_vina)

        self.gotostage4Button = QPushButton(self.frame_19)
        self.gotostage4Button.setObjectName(u"gotostage4Button")
        self.gotostage4Button.setMinimumSize(QSize(200, 30))
        self.gotostage4Button.setMaximumSize(QSize(200, 30))
        self.gotostage4Button.setFocusPolicy(Qt.NoFocus)

        self.verticalLayout_20.addWidget(self.gotostage4Button, 0, Qt.AlignHCenter)


        self.horizontalLayout_18.addWidget(self.frame_19)


        self.verticalLayout_15.addWidget(self.Third_Stage3)


        self.verticalLayout_10.addWidget(self.frame_5, 0, Qt.AlignTop)

        self.stackedWidget.addWidget(self.stage3)
        self.stage4 = QWidget()
        self.stage4.setObjectName(u"stage4")
        self.verticalLayout_11 = QVBoxLayout(self.stage4)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_9 = QFrame(self.stage4)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_9)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.frame_continue = QFrame(self.frame_9)
        self.frame_continue.setObjectName(u"frame_continue")
        self.frame_continue.setEnabled(True)
        self.frame_continue.setFrameShape(QFrame.StyledPanel)
        self.frame_continue.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_continue)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.choosedir_stage4 = QPushButton(self.frame_continue)
        self.choosedir_stage4.setObjectName(u"choosedir_stage4")
        self.choosedir_stage4.setMinimumSize(QSize(300, 40))
        self.choosedir_stage4.setMaximumSize(QSize(300, 40))
        self.choosedir_stage4.setFocusPolicy(Qt.NoFocus)
        self.choosedir_stage4.setStyleSheet(u"QPushButton{\n"
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

        self.verticalLayout_22.addWidget(self.choosedir_stage4, 0, Qt.AlignHCenter)


        self.verticalLayout_21.addWidget(self.frame_continue)

        self.label_stage4 = QLabel(self.frame_9)
        self.label_stage4.setObjectName(u"label_stage4")

        self.verticalLayout_21.addWidget(self.label_stage4)

        self.frame_Selectpeptides = QFrame(self.frame_9)
        self.frame_Selectpeptides.setObjectName(u"frame_Selectpeptides")
        self.frame_Selectpeptides.setFrameShape(QFrame.StyledPanel)
        self.frame_Selectpeptides.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_Selectpeptides)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.aff_spinbox = QSpinBox(self.frame_Selectpeptides)
        self.aff_spinbox.setObjectName(u"aff_spinbox")
        self.aff_spinbox.setMaximumSize(QSize(150, 40))
        self.aff_spinbox.setStyleSheet(u"\n"
"QSpinBox::up-button {\n"
"	width:25px;\n"
"	\n"
"}\n"
"QSpinBox::down-button {\n"
"	width:25px;\n"
"\n"
"}\n"
"\n"
"*{font: 9pt \"Eight Bit Dragon\";\n"
"border: 2px solid;\n"
"border-color: rgb(100, 100, 100);\n"
"border-top-left-radius: 12px;\n"
"border-bottom-left-radius: 12px;\n"
"}")
        self.aff_spinbox.setMinimum(-20)
        self.aff_spinbox.setMaximum(0)
        self.aff_spinbox.setSingleStep(0)
        self.aff_spinbox.setStepType(QAbstractSpinBox.AdaptiveDecimalStepType)

        self.horizontalLayout_20.addWidget(self.aff_spinbox)

        self.bestpepButton = QPushButton(self.frame_Selectpeptides)
        self.bestpepButton.setObjectName(u"bestpepButton")
        self.bestpepButton.setEnabled(True)
        self.bestpepButton.setMinimumSize(QSize(40, 40))
        self.bestpepButton.setMaximumSize(QSize(200, 16777215))
        self.bestpepButton.setFocusPolicy(Qt.NoFocus)
        self.bestpepButton.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout_20.addWidget(self.bestpepButton)


        self.verticalLayout_21.addWidget(self.frame_Selectpeptides)


        self.verticalLayout_11.addWidget(self.frame_9)

        self.frame_6 = QFrame(self.stage4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.tableWidget = QTableWidget(self.frame_6)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(21, 9, 850, 192))
        self.tableWidget.setMinimumSize(QSize(850, 0))
        self.tableWidget.setMaximumSize(QSize(16777215, 200))
        self.tableWidget.setStyleSheet(u"QHeaderView::section{\n"
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
"QHeaderView::section::hover {\n"
"	background-color: rgb(80, 80, 80);\n"
"	color: white;\n"
"	font: 8pt \"Eight Bit Dragon\";\n"
"	border: 2px solid black;\n"
"	\n"
"	\n"
"	\n"
"}\n"
"\n"
"\n"
"QTableWidget QTableCornerButton::section {\n"
"    background-color: rgb(40,40, 32);\n"
"}\n"
"\n"
"*{\n"
"font: 10pt \"Eight Bit Dragon\";\n"
"background-color: rgb(40,40, 32);\n"
"}\n"
"")
        self.tableWidget.setEditTriggers(QAbstractItemView.DoubleClicked)
        self.tableWidget.setDragDropOverwriteMode(False)
        self.tableWidget.setShowGrid(True)

        self.verticalLayout_11.addWidget(self.frame_6)

        self.frame_10 = QFrame(self.stage4)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(0, 80))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_19 = QLabel(self.frame_10)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_21.addWidget(self.label_19)

        self.frame_11 = QFrame(self.frame_10)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMouseTracking(False)
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_11)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.confidenceSpinbox = QSpinBox(self.frame_11)
        self.confidenceSpinbox.setObjectName(u"confidenceSpinbox")
        self.confidenceSpinbox.setMinimumSize(QSize(0, 30))
        self.confidenceSpinbox.setStyleSheet(u"border: None;")
        self.confidenceSpinbox.setWrapping(False)
        self.confidenceSpinbox.setAlignment(Qt.AlignCenter)
        self.confidenceSpinbox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.confidenceSpinbox.setKeyboardTracking(True)
        self.confidenceSpinbox.setMaximum(100)

        self.verticalLayout_23.addWidget(self.confidenceSpinbox, 0, Qt.AlignHCenter)

        self.horizontalSlider = QSlider(self.frame_11)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setStyleSheet(u"QSlider::handle::horizontal {\n"
"\n"
"	\n"
"	\n"
"	\n"
"	background-color: rgb(255, 158, 110);\n"
"\n"
"}")
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setTracking(True)
        self.horizontalSlider.setOrientation(Qt.Horizontal)
        self.horizontalSlider.setInvertedAppearance(False)
        self.horizontalSlider.setInvertedControls(False)
        self.horizontalSlider.setTickPosition(QSlider.TicksBelow)
        self.horizontalSlider.setTickInterval(10)

        self.verticalLayout_23.addWidget(self.horizontalSlider)


        self.horizontalLayout_21.addWidget(self.frame_11)

        self.pickAAButton = QPushButton(self.frame_10)
        self.pickAAButton.setObjectName(u"pickAAButton")
        self.pickAAButton.setMinimumSize(QSize(220, 30))
        self.pickAAButton.setFocusPolicy(Qt.NoFocus)
        self.pickAAButton.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout_21.addWidget(self.pickAAButton)


        self.verticalLayout_11.addWidget(self.frame_10)

        self.tableWidget_2 = QTableWidget(self.stage4)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setMinimumSize(QSize(850, 100))
        self.tableWidget_2.setMaximumSize(QSize(16777215, 200))
        self.tableWidget_2.setStyleSheet(u"QHeaderView::section{\n"
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
"QHeaderView::section::hover {\n"
"	background-color: rgb(80, 80, 80);\n"
"	color: white;\n"
"	font: 8pt \"Eight Bit Dragon\";\n"
"	border: 2px solid black;\n"
"	\n"
"	\n"
"	\n"
"}\n"
"\n"
"\n"
"QTableWidget QTableCornerButton::section {\n"
"    background-color: rgb(40,40, 32);\n"
"}\n"
"\n"
"*{\n"
"font: 10pt \"Eight Bit Dragon\";\n"
"background-color: rgb(40,40, 32);\n"
"}\n"
"")

        self.verticalLayout_11.addWidget(self.tableWidget_2, 0, Qt.AlignHCenter)

        self.frame_14 = QFrame(self.stage4)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.frame_17 = QFrame(self.frame_14)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_17)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.label_20 = QLabel(self.frame_17)
        self.label_20.setObjectName(u"label_20")

        self.verticalLayout_24.addWidget(self.label_20)

        self.spinBox_pymol = QSpinBox(self.frame_17)
        self.spinBox_pymol.setObjectName(u"spinBox_pymol")
        self.spinBox_pymol.setMinimumSize(QSize(100, 30))
        self.spinBox_pymol.setMaximumSize(QSize(150, 16777215))
        self.spinBox_pymol.setStyleSheet(u"\n"
"QSpinBox::up-button {\n"
"	width:25px;\n"
"	\n"
"}\n"
"QSpinBox::down-button {\n"
"	width:25px;\n"
"\n"
"}\n"
"\n"
"*{font: 9pt \"Eight Bit Dragon\";\n"
"border: 2px solid;\n"
"border-color: rgb(100, 100, 100);\n"
"border-top-left-radius: 12px;\n"
"border-bottom-left-radius: 12px;\n"
"}")
        self.spinBox_pymol.setMinimum(1)
        self.spinBox_pymol.setMaximum(1000000000)

        self.verticalLayout_24.addWidget(self.spinBox_pymol, 0, Qt.AlignHCenter)


        self.horizontalLayout_12.addWidget(self.frame_17, 0, Qt.AlignRight)

        self.pymol_button = QPushButton(self.frame_14)
        self.pymol_button.setObjectName(u"pymol_button")
        self.pymol_button.setMinimumSize(QSize(120, 40))
        self.pymol_button.setMaximumSize(QSize(200, 40))
        self.pymol_button.setFocusPolicy(Qt.NoFocus)
        self.pymol_button.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout_12.addWidget(self.pymol_button, 0, Qt.AlignLeft)

        self.horizontalSpacer_4 = QSpacerItem(200, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_4)

        self.resetRPGButton = QPushButton(self.frame_14)
        self.resetRPGButton.setObjectName(u"resetRPGButton")
        self.resetRPGButton.setMinimumSize(QSize(150, 60))
        self.resetRPGButton.setMaximumSize(QSize(200, 40))
        font5 = QFont()
        font5.setFamily(u"Eight Bit Dragon")
        font5.setPointSize(15)
        font5.setBold(False)
        font5.setItalic(False)
        font5.setWeight(50)
        self.resetRPGButton.setFont(font5)
        self.resetRPGButton.setFocusPolicy(Qt.NoFocus)
        self.resetRPGButton.setStyleSheet(u"QPushButton{\n"
"font: 15pt \"Eight Bit Dragon\";\n"
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

        self.horizontalLayout_12.addWidget(self.resetRPGButton)


        self.verticalLayout_11.addWidget(self.frame_14, 0, Qt.AlignHCenter)

        self.stackedWidget.addWidget(self.stage4)

        self.verticalLayout.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.main_frame, 0, Qt.AlignTop)


        self.verticalLayout_2.addWidget(self.general_frame)

        Window.setCentralWidget(self.centralwidget)

        self.retranslateUi(Window)
        self.horizontalSlider.valueChanged.connect(self.confidenceSpinbox.setValue)
        self.confidenceSpinbox.valueChanged.connect(self.horizontalSlider.setValue)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Window)
    # setupUi

    def retranslateUi(self, Window):
        Window.setWindowTitle(QCoreApplication.translate("Window", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.minimizeButton.setToolTip(QCoreApplication.translate("Window", u"Minimize Window", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeButton.setText("")
#if QT_CONFIG(tooltip)
        self.squareButton.setToolTip(QCoreApplication.translate("Window", u"Resize Window", None))
#endif // QT_CONFIG(tooltip)
        self.squareButton.setText("")
#if QT_CONFIG(tooltip)
        self.xButton.setToolTip(QCoreApplication.translate("Window", u"Close Window", None))
#endif // QT_CONFIG(tooltip)
        self.xButton.setText("")
        self.RPG_title.setText(QCoreApplication.translate("Window", u"RPG", None))
        self.title.setText(QCoreApplication.translate("Window", u"Random Peptide Generator", None))
        self.homeButton.setText("")
        self.stage2Button.setText(QCoreApplication.translate("Window", u"Stage 2", None))
        self.stage3Button.setText(QCoreApplication.translate("Window", u"Stage 3", None))
        self.stage4Button.setText(QCoreApplication.translate("Window", u"Stage 4", None))
        self.top_label_2.setText(QCoreApplication.translate("Window", u"<html><head/><body><p>Welcome, if this is your first time press <span style=\" font-weight:600;\">New Game</span>, if you have already </p><p align=\"center\">started press <span style=\" font-weight:600;\">Continue</span> and select your stage</p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("Window", u"<html><head/><body><p align=\"center\">Select your current Stage</p></body></html>", None))
        self.newgameButton.setText(QCoreApplication.translate("Window", u"New Game", None))
        self.continueButton.setText(QCoreApplication.translate("Window", u"Continue", None))
        self.label_2.setText(QCoreApplication.translate("Window", u"In this moment the app is in develop stage, so be pacient. \n"
"You can find our laboratory page in the link below.", None))
        self.label.setText(QCoreApplication.translate("Window", u"Laboratory Page", None))
        self.pushButton_2.setText("")
        self.labiconButton.setText("")
        self.label_3.setText(QCoreApplication.translate("Window", u"Fisrt Step", None))
        self.label_4.setText(QCoreApplication.translate("Window", u"<html><head/><body><p align=\"center\">Push the atom to configure the </p><p align=\"center\">settings of your peptide. Once you'r done, </p><p align=\"center\">click on the button &quot;Ready!&quot; to get back.</p></body></html>", None))
        self.setpepButton.setText("")
        self.label_6.setText(QCoreApplication.translate("Window", u"Second Step", None))
        self.directoryButton.setText(QCoreApplication.translate("Window", u"Choose a Working Directory", None))
        self.label_7.setText(QCoreApplication.translate("Window", u"Generating Peptides...", None))
        self.gotostage2Button.setText(QCoreApplication.translate("Window", u"Go to Stage 2", None))
        self.label_stage2_newgame.setText(QCoreApplication.translate("Window", u"<html><head/><body><p align=\"center\">Your Peptides List has been setted, so now you new </p><p align=\"center\">to run Chimera to transform your peptides into 3D </p><p align=\"center\">models</p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("Window", u"<html><head/><body><p align=\"center\">To continue, select your folder again and choose the </p><p align=\"center\">number of peptides you want to convert into 3D </p><p align=\"center\">models</p></body></html>", None))
        self.stage2_selectButton.setText(QCoreApplication.translate("Window", u"Select Your Folder", None))
        self.label_8.setText(QCoreApplication.translate("Window", u"How many peptides do you want to convert?", None))
        self.runchimButton.setText(QCoreApplication.translate("Window", u"Run Chimera", None))
        self.label_working.setText(QCoreApplication.translate("Window", u"<html><head/><body><p align=\"center\">Please Wait...</p></body></html>", None))
        self.label_done.setText(QCoreApplication.translate("Window", u"<html><head/><body><p align=\"center\">Your peptides have been converted with SUCCESS !</p><p align=\"center\">Look for them in the folder name as: </p><p align=\"center\">Chimera-Peptides</p></body></html>", None))
        self.gotostage3Button.setText(QCoreApplication.translate("Window", u"Go to Stage 3", None))
        self.label_stage3_NewGame.setText(QCoreApplication.translate("Window", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">In this Stage you need to prepare your PDB files and convert them into PDBQT to run AutoDockVina. Must </span></p><p align=\"center\"><span style=\" font-size:10pt;\">also need your protein in PDBQT format (not included in this software)</span></p></body></html>", None))
        self.label_stage3_Continue.setText(QCoreApplication.translate("Window", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">To continue, select your folder again and choose the number of peptides you want to convert into PDBQT </span></p><p align=\"center\"><span style=\" font-size:10pt;\">format to prepare for run AutoDock Vina. Must also need your protein in PDBQT format (not included in this software)</span></p></body></html>", None))
        self.label_17.setText(QCoreApplication.translate("Window", u"Continue Step", None))
        self.label_10.setText(QCoreApplication.translate("Window", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Choose your working Directory</span></p></body></html>", None))
        self.select_stage3Button.setText(QCoreApplication.translate("Window", u"Select Folder", None))
        self.label_12.setText(QCoreApplication.translate("Window", u"Fisrt Step", None))
        self.label_14.setText(QCoreApplication.translate("Window", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Convert all your previous peptides into compatible format </span></p><p align=\"center\"><span style=\" font-size:10pt;\">with AutoDock Vina</span></p></body></html>", None))
        self.label_18.setText(QCoreApplication.translate("Window", u"<html><head/><body><p><span style=\" vertical-align:sub;\">How many peptides do you want to convert to PDBQT</span></p></body></html>", None))
        self.obconvertButton.setText(QCoreApplication.translate("Window", u"Convert to PDBQT", None))
        self.label_13.setText(QCoreApplication.translate("Window", u"Second Step", None))
        self.label_11.setText(QCoreApplication.translate("Window", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Now you need to choose both, your protein and your ligands</span></p></body></html>", None))
        self.selectprotein_stage3Button.setText(QCoreApplication.translate("Window", u"Select Your Protein", None))
        self.selectpep_stage3Button.setText(QCoreApplication.translate("Window", u"Select Your Ligands", None))
        self.label_15.setText(QCoreApplication.translate("Window", u"Third Step", None))
        self.label_16.setText(QCoreApplication.translate("Window", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Configure AutoDock Vina Parameters (https://vina.scripps.edu/)</span></p><p align=\"center\"><span style=\" font-size:10pt;\">Then press Run to start</span></p></body></html>", None))
        self.configureVinaButton.setText(QCoreApplication.translate("Window", u"Configure Vina", None))
        self.runVinaButton.setText(QCoreApplication.translate("Window", u"Run Vina", None))
        self.gotostage4Button.setText(QCoreApplication.translate("Window", u"Go to stage 4", None))
        self.choosedir_stage4.setText(QCoreApplication.translate("Window", u"Choose Working Directory", None))
        self.label_stage4.setText(QCoreApplication.translate("Window", u"<html><head/><body><p align=\"center\"><span style=\" font-size:9pt;\">Now you need to choose a parameter to filter your best peptides, so pick a number of </span></p><p align=\"center\"><span style=\" font-size:9pt;\">affnity that you want your peptides be greater than</span></p></body></html>", None))
        self.aff_spinbox.setSuffix(QCoreApplication.translate("Window", u"  kcal/mol", None))
        self.aff_spinbox.setPrefix("")
        self.bestpepButton.setText(QCoreApplication.translate("Window", u"Select Best Peptides", None))
        self.label_19.setText(QCoreApplication.translate("Window", u"<html><head/><body><p><span style=\" font-size:8pt;\">Pick a porcentage of confidence for</span></p><p><span style=\" font-size:8pt;\">every reapeated aminoacid in each </span></p><p><span style=\" font-size:8pt;\">position of your sequence</span></p></body></html>", None))
        self.confidenceSpinbox.setSpecialValueText("")
        self.confidenceSpinbox.setSuffix(QCoreApplication.translate("Window", u"%", None))
        self.confidenceSpinbox.setPrefix("")
        self.pickAAButton.setText(QCoreApplication.translate("Window", u"Pick aminoacids", None))
        self.label_20.setText(QCoreApplication.translate("Window", u"Select the peptide for pymol", None))
        self.pymol_button.setText(QCoreApplication.translate("Window", u"PyMol ", None))
        self.resetRPGButton.setText(QCoreApplication.translate("Window", u"Reset RPG", None))
    # retranslateUi

