import sys
from PyQt5.QtCore import Qt, QPoint
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QLineEdit, QVBoxLayout, QCheckBox, QHBoxLayout, QMainWindow
from PyQt5.QtGui import QIntValidator
from PepWin.ui_Peptide import *

import resources_rc
import sqlite3


######################################################################################################################################
########### ALGUNAS VARIABLES IMPORTANTES  #######################
######################################################################################################################################
allAminoAcids = {1: ('A', 'ALA', 'alanine'),
                 2: ('R', 'ARG', 'arginine'),
                 3: ('N', 'ASN', 'asparagine'),
                 4: ('D', 'ASP', 'aspartic acid'),
                 5: ('C', 'CYS', 'cysteine'),
                 6: ('Q', 'GLN', 'glutamine'),
                 7: ('E', 'GLU', 'glutamic acid'),
                 8: ('G', 'GLY', 'glycine'),
                 9: ('H', 'HIS', 'histidine'),
                 10: ('I', 'ILE', 'isoleucine'),
                 11: ('L', 'LEU', 'leucine'),
                 12: ('K', 'LYS', 'lysine'),
                 13: ('M', 'MET', 'methionine'),
                 14: ('F', 'PHE', 'phenylalanine'),
                 15: ('P', 'PRO', 'proline'),
                 16: ('S', 'SER', 'serine'),
                 17: ('T', 'THR', 'threonine'),
                 18: ('W', 'TRP', 'tryptophan'),
                 19: ('Y', 'TYR', 'tyrosine'),
                 20: ('V', 'VAL', 'valine'),
                 }
one2all = {'A': ('A', 'ALA', 'alanine'),
           'R': ('R', 'ARG', 'arginine'),
           'N': ('N', 'ASN', 'asparagine'),
           'D': ('D', 'ASP', 'aspartic acid'),
           'C': ('C', 'CYS', 'cysteine'),
           'Q': ('Q', 'GLN', 'glutamine'),
           'E': ('E', 'GLU', 'glutamic acid'),
           'G': ('G', 'GLY', 'glycine'),
           'H': ('H', 'HIS', 'histidine'),
           'I': ('I', 'ILE', 'isoleucine'),
           'L': ('L', 'LEU', 'leucine'),
           'K': ('K', 'LYS', 'lysine'),
           'M': ('M', 'MET', 'methionine'),
           'F': ('F', 'PHE', 'phenylalanine'),
           'P': ('P', 'PRO', 'proline'),
           'S': ('S', 'SER', 'serine'),
           'T': ('T', 'THR', 'threonine'),
           'W': ('W', 'TRP', 'tryptophan'),
           'Y': ('Y', 'TYR', 'tyrosine'),
           'V': ('V', 'VAL', 'valine')}
all2one = {"Alanine": "A", "Arginine": "R", "Asparagine": "N",
           "Aspartic acid": "D", "Cysteine": "C", "Glutamine": "Q",
           "Glutamic acid": "E", "Glycine": "G", "Histidine": "H",
           "Isoleucine": "I", "Leucine": "L", "Lysine": "K",
           "Methionine": "M", "Phenylalanine": "F", "Proline": "P",
           "Serine": "S", "Threonine": "T", "Tryptophan": "W",
           "Tyrosine": "Y", "Valine": "V"}
peptideDict = {}
numb = 0

######################################################################################################################################
########### VENTANA DEL PEPTIDO  #######################
######################################################################################################################################


class PepWindow(QDialog):

    def __init__(self, parent=None):
        QDialog.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)


        #loadJsonStyle(self, self.ui)

        self.ui.tabWidget.currentChanged.connect(self.tabChanged)
        self.ui.generateButton.clicked.connect(self.choosenumber)
        self.ui.resetButton_2.clicked.connect(self.getValuesCheckBox)
        self.ui.resetButton.clicked.connect(self.resetAll)


        self.ui.selectButton.clicked.connect(self.checkAll)
        self.ui.minimizeButton.clicked.connect(self.showMinimized)
        self.ui.selectButton.setEnabled(False)
        self.ui.listoButton.setEnabled(False)
        self.ui.resetButton.setEnabled(False)
        onlyInt = QIntValidator(0,20, self)
        # onlyInt.setRange(0, 20)
        self.ui.lineEdit.setValidator(onlyInt)
        self.tabs = self.ui.tabWidget


######################################################################################################################################
########### Permite Mover la Ventana  ##############################################################
######################################################################################################################################

    def mousePressEvent(self, event):
        self.oldPosition = event.globalPos()

    def mouseMoveEvent(self, e):
        delta = QPoint(e.globalPos() - self.oldPosition)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPosition = e.globalPos()


######################################################################################################################################
########### Funciones Distintas para la funcion de la ventana  ##############################################################
######################################################################################################################################
    # def closePep(self):
    #     self.hide()



    def choosenumber(self):

        msj = QMessageBox()
        msj.setWindowTitle("Error")
        msj.setText("Your number must be between 1-20")
        msj.setIcon(QMessageBox.Warning)
        msj.setFont(QFont("Eight Bit Dragon", 8))
        msj.setContentsMargins(0,30,0,0)
        msj.setStyleSheet('QDialog{border: 2px solid rgb(120, 120, 120);}' '*{background-color: rgb(40,40, 32); color: white;}')
        msj.setWindowFlag(Qt.FramelessWindowHint)

        if self.ui.lineEdit.text() == '':
            msj.exec_()
        else:

            numb = int(self.ui.lineEdit.text())
            if numb > 20:
                msj.exec_()
                self.ui.lineEdit.setText("")

            else:

                self.createTabs(numb)
                self.ui.selectButton.setEnabled(True)
                self.ui.listoButton.setEnabled(False)
                self.ui.resetButton.setEnabled(True)

    def tabChanged(self):
        print("TabChanged", self.ui.tabWidget.currentIndex())


    def resetAll(self):
        self.ui.tabWidget.clear()

        self.ui.selectButton.setEnabled(False)
        self.ui.generateButton.setEnabled(True)
        self.ui.lineEdit.setEnabled(True)
        self.ui.lineEdit.clear()


    def createTabs(self, number):
        # self.tabs.setStyleSheet('QTabWidget{background-color: rgb(40,40, 32); color: white;}')
        for i in range(number):
            self.tabs.addTab(TabContents(), str(i + 1))


        self.ui.generateButton.setEnabled(False)
        self.ui.lineEdit.setEnabled(False)

    def getValuesCheckBox(self):
        global peptideDict
        self.sum = 0
        self.tri = 0

        msj = QMessageBox()
        msj.setFont(QFont("Eight Bit Dragon", 8))
        msj.setContentsMargins(0, 30, 0, 0)
        msj.setStyleSheet(
            'QDialog{border: 2px solid rgb(120, 120, 120);}' '*{background-color: rgb(40,40, 32); color: white;')
        msj.setWindowFlag(Qt.FramelessWindowHint)

        for tab in range(self.ui.tabWidget.count()):
            peptideDict[tab] = []  # Solo para crear un diccionario con los key necesarios

        ######################################################################################################################################
        # AQUI GUARDAMOS LOS DATOS INGRESADOS POR EL USUARIO #

        for tab in range(self.ui.tabWidget.count()):
            self.sum = 0
            for checkstate in self.ui.tabWidget.widget(tab).findChildren(QCheckBox):
                #print(str(checkstate.objectName()) + " " + str(checkstate.isChecked()))

                if checkstate.isChecked() == False:
                    self.sum += 1


                if checkstate.isChecked() == True:
                    trad = all2one[checkstate.text()]
                    peptideDict[tab] += [trad]



            if self.sum < 20:
                self.tri += 1

        print(self.ui.tabWidget.count())


        if self.tri == self.ui.tabWidget.count():
            self.ui.listoButton.setEnabled(True)
            self.max_pep = 1

            for list in peptideDict.values():
                self.max_pep *= len(list)

            msj.setText("Your total combinations are: {}".format(str(self.max_pep) + '\n'+ 'Press Ready! to continue'))

            msj.setIcon(QMessageBox.Information)
            msj.setWindowTitle("Accepted")
            msj.exec_()



        if self.tri < self.ui.tabWidget.count():

            msj.setText("You must select at least one aminoacid in each position, then try again")
            msj.setIcon(QMessageBox.Warning)
            msj.setWindowTitle("Warning")
            msj.exec_()





    def checkAll(self):
        current = self.ui.tabWidget.currentIndex()
        for checkbox in self.ui.tabWidget.widget(current).findChildren(QCheckBox):

            if checkbox.isChecked() == False:
                checkbox.setChecked(True)

######################################################################################################################################
########### CLASE PARA LA CREACION DE OBJETOS DENTRO DEL "TABWIDGET" #######################
######################################################################################################################################
class TabContents(QWidget):

    def __init__(self):
        super(TabContents, self).__init__()
        self.createWidgets()

    ######################################################################################################################################
    # ACA SE GENERAN LOS CHECKBOX PARA PODER INGRESAR NUESTROS AMINOACIDOS ITERADORES #
    def createWidgets(self):
        global numb
        self.layout = QHBoxLayout()
        self.vbox = QVBoxLayout()
        self.xbox = QVBoxLayout()
        self.layout.addLayout(self.vbox)
        self.layout.addLayout(self.xbox)
        self.setLayout(self.layout)
        setattr(QWidget, "xbox", self.xbox)
        setattr(QWidget, "vbox", self.vbox)




        for k in sorted(allAminoAcids.keys())[:10]:
            newName = "checkbox" + "_" + str(numb) + "_" + str(k)
            self.checkbox = QCheckBox(allAminoAcids[k][2].capitalize())
            self.checkbox.setObjectName(newName)
            self.vbox.addWidget(self.checkbox)
            self.setLayout(self.vbox)
            setattr(QWidget, "checkbox", self.checkbox)

        for k in sorted(allAminoAcids.keys())[10:]:
            newName = "checkbox" + "_" + str(numb) + "_" + str(k)
            self.checkbox = QCheckBox(allAminoAcids[k][2].capitalize())
            self.checkbox.setObjectName(newName)
            self.xbox.addWidget(self.checkbox)
            self.setLayout(self.xbox)
            setattr(QWidget, "checkbox", self.checkbox)
            # print(self.checkbox.objectName())
        numb += 1

