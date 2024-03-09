import sys
import os
import csv
from itertools import product
import multiprocessing
from PyQt5 import QtCore
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, QPoint
from MainWin.ui_mainwindow import *
from PepWin.ui_Peptide import *
from MainWin.ui_vinawin import *
from PepWin.PeptideWindow import PepWindow
from PepWin.PeptideWindow import peptideDict
from ConfigWin.ui_configwin import Ui_Dialog
from ConfigWin.ConfVinaWindow import ConfWindow
from pathlib import Path
import shutil
from openbabel import openbabel as ob
import subprocess
import time
import pandas as pd
import random
import concurrent.futures

dir_save = None


#################################################################################################################################
########## Vetana y Incio de Programa ###############################################################################################
#################################################################################################################################

class MainWindow(QMainWindow):

    #Define todas las variables que utilizara la clase, conecta los botones con diferentes funciones
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.protein_save = None
        self.ligands_save = None
        self.dir_save = None
        self.center = None
        self.size = None
        self.exh = None
        self.ui = Ui_Window()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.move(50, 50)

        # Defino a la segunda ventana y la inicio en mi ventana principal, es importante hacerlo en el __init__ para que este implementado en toda la ventana
        self.window = PepWindow(self)
        self.confwin = ConfWindow(self)
        self.vinawin = Window(self)

        # Botones y sus conexiones#
        self.ui.setpepButton.clicked.connect(self.openPepWin)
        self.ui.xButton.clicked.connect(sys.exit)
        self.window.ui.xButton.clicked.connect(self.closeBefore)
        self.ui.minimizeButton.clicked.connect(self.showMinimized)
        self.ui.directoryButton.clicked.connect(self.saveBrowser)
        self.ui.stage1Button.clicked.connect(self.moveStage1)
        self.ui.stage3Button.clicked.connect(self.moveStage3_FromContin)
        self.ui.stage4Button.clicked.connect(self.moveStage4_FromContin)
        self.ui.homeButton.clicked.connect(self.moveHome)
        self.ui.newgameButton.clicked.connect(self.newgameFun)
        self.ui.continueButton.clicked.connect(self.continueFun)
        self.ui.runchimButton.clicked.connect(self.stage2_RunChim)
        self.window.ui.listoButton.pressed.connect(self.closePept)  # Aca se utilizo un boton de la otra ventana
        self.ui.obconvertButton.clicked.connect(self.stage3_SetPDBQT)
        self.ui.select_stage3Button.clicked.connect(self.selectFolder_Stage3)
        self.ui.selectprotein_stage3Button.clicked.connect(self.stage3_SelectProtein)
        self.ui.selectpep_stage3Button.clicked.connect(self.stage3_SelectLigands)
        self.ui.configureVinaButton.clicked.connect(self.stage3_ConfVina)
        self.confwin.ui.saveButton.clicked.connect(self.saveConfig)
        self.ui.runVinaButton.clicked.connect(self.stage3_RunVina)
        self.ui.bestpepButton.clicked.connect(self.stage4_CSV)
        self.ui.choosedir_stage4.clicked.connect(self.selectFolder_Stage4)
        self.ui.gotostage4Button.clicked.connect(self.moveStage4_FromNew)
        self.ui.pickAAButton.clicked.connect(self.stage4_BestAmino)
        self.ui.resetRPGButton.clicked.connect(self.moveHome)
        self.ui.pymol_button.clicked.connect(self.ena_Pymol)
        self.ui.helpButton.clicked.connect(self.help_button)
        self.ui.squareButton.clicked.connect(self.maximize_win)
        self.ui.pushButton_2.clicked.connect(self.web_button)


        # Configuracion de Botones y Ventanas#
        self.ui.label_9.setVisible(False)
        self.ui.label_done.setVisible(False)
        self.ui.label_working.setVisible(False)
        self.ui.gotostage2Button.setVisible(False)
        self.ui.label_5.setVisible(False)
        self.ui.label_stage2_newgame.setVisible(False)
        self.ui.stage2_selectButton.setVisible(False)
        self.ui.runchimButton.setVisible(False)
        self.ui.label_8.setVisible(False)
        self.ui.spinBox.setVisible(False)
        self.ui.stage1Button.setEnabled(False)
        self.ui.stage2Button.setEnabled(False)
        self.ui.stage3Button.setEnabled(False)
        self.ui.stage4Button.setEnabled(False)
        self.ui.textEdit.setReadOnly(True)
        self.ui.listnameFrame.setVisible(False)
        self.ui.textEdit.setVisible(False)
        self.ui.label_7.setVisible(False)
        self.swidget = self.ui.stackedWidget
        self.swidget.setCurrentIndex(0)
        self.ui.gotostage3Button.setVisible(False)
        self.ui.runVinaButton.setVisible(False)

    #Permite mover la ventana de un lado para otro solo agarrandola con el mouse
    def mousePressEvent(self, event):
        self.oldPosition = event.globalPos()

    def mouseMoveEvent(self, e):
        delta = QPoint(e.globalPos() - self.oldPosition)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPosition = e.globalPos()

    def maximize_win(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

    def web_button(self):
        web_link = 'https://www.rivaspardo-lab.org/lab'
        QDesktopServices.openUrl((QUrl(web_link)))


    def help_button(self):
        github_link = 'https://github.com/RivasPardoLab/RPG-Software.git'
        QDesktopServices.openUrl((QUrl(github_link)))
#################################################################################################################################
########## Home Funcionamiento ###############################################################################################
##################################################################################################################################

    def newgameFun(self):
        self.swidget.setCurrentIndex(1)
        self.ui.homeButton.setEnabled(True)
        self.ui.stage1Button.setEnabled(True)
        self.ui.stage2Button.clicked.connect(self.moveStage2_NewGame)
        self.ui.gotostage2Button.clicked.connect(self.moveStage2_NewGame)
        self.ui.stage2Button.setEnabled(False)
        self.ui.stage3Button.setEnabled(False)
        self.ui.stage4Button.setEnabled(False)

    def continueFun(self):
        self.ui.stage1Button.setEnabled(True)
        self.ui.stage2Button.setEnabled(True)
        self.ui.stage3Button.setEnabled(True)
        self.ui.stage4Button.setEnabled(True)
        self.ui.continueButton.setVisible(False)
        self.ui.newgameButton.setVisible(False)
        self.ui.label_9.setVisible(True)
        self.ui.stage2Button.clicked.connect(self.moveStage2_Continue)

    # Funciones para moverse en el StackWidget  ###################################################################################################3

    def moveHome(self):
        self.swidget.setCurrentIndex(0)
        self.ui.newgameButton.setVisible(True)
        self.ui.continueButton.setVisible(True)
        self.ui.newgameButton.setVisible(True)

    def moveStage1(self):
        self.swidget.setCurrentIndex(1)
        self.ui.stage2Button.setEnabled(False)
        self.ui.stage3Button.setEnabled(False)
        self.ui.stage4Button.setEnabled(False)


#################################################################################################################################
########## Stage 1 Funcionamiento ###############################################################################################
#################################################################################################################################

    # Permite Abrir la ventana del Peptido

    def openPepWin(self):
        self.window.show()
        self.ui.setpepButton.setEnabled(False)

    # Permite mostrar los objetos cuando se cierra la ventana

    def closePept(self):
        self.window.hide()
        self.ui.setpepButton.setEnabled(True)
        self.ui.mid_frame.setVisible(True)
        self.ui.setpepButton.setEnabled(True)
        self.ui.listnameFrame.setVisible(True)



    def closeBefore(self):
        self.ui.mid_frame.setVisible(False)
        self.ui.setpepButton.setEnabled(True)
        self.ui.listnameFrame.setVisible(False)
        self.window.hide()
        print('Cerrado!')



    # Funciones para guardar el directorio de trabajo y guarda la lista de peptidos

    def saveBrowser(self):
        global dir_save
        self.dir_save =''

        chimpyfile = "Scripts/ChimeraAuto-Run.py"
        namelist = "peptides.txt"
        path = os.path.expanduser('~\Documents' + "\\")
        # dir_save = QFileDialog.getExistingDirectory(self, "Select your working directory", path, options=QFileDialog.DontUseNativeDialog)
        self.dir_save = QFileDialog.getExistingDirectory(self, "Select your working directory", path,
                                                         options=QFileDialog.DontUseNativeDialog)
        if self.dir_save != '':

            Path(self.dir_save + "/Scripts").mkdir(parents=True, exist_ok=True)
            Path(self.dir_save + "/Parameters").mkdir(parents=True, exist_ok=True)
            Path(self.dir_save + "/Chimera-Peptides").mkdir(parents=True, exist_ok=True)
            Path(self.dir_save + "/Ligands").mkdir(parents=True, exist_ok=True)
            Path(self.dir_save + "/VinaResults").mkdir(parents=True, exist_ok=True)
            shutil.copytree("chimpdbs", self.dir_save + "/Parameters//", dirs_exist_ok=True)
            shutil.copy(chimpyfile, self.dir_save + "/Scripts")
            os.chdir(self.dir_save)

            msj = QMessageBox()
            msj.setFont(QFont("Eight Bit Dragon", 8))
            msj.setContentsMargins(0, 30, 0, 0)
            msj.setStyleSheet(
                'QDialog{border: 2px solid rgb(120, 120, 120);}' '*{background-color: rgb(40,40, 32); color: white;}')
            msj.setWindowFlag(Qt.FramelessWindowHint)

            if os.path.isfile(self.dir_save + "/" + namelist):
                msj.setText("You must delete or rename your older peptide list, then try again")
                msj.setIcon(QMessageBox.Warning)
                msj.setWindowTitle("Warning")
                msj.exec_()

            else:
                # txt_save = QFileDialog.getSaveFileNameself, "Save your List File", dir_save+"//Lista.txt", "Text Files (*.txt)")
                msj.setText("Success : Petide List Save as: " + namelist)
                msj.setIcon(QMessageBox.Information)
                msj.setWindowTitle("Success")
                msj.exec_()
                os.chdir(self.dir_save)

                self.ui.setpepButton.setEnabled(False)
                self.ui.directoryButton.setEnabled(False)
                self.ui.textEdit.setVisible(True)
                self.ui.label_7.setVisible(True)
                self.ui.textEdit.setPlainText("Your peptides are being generated...")

                ##################################
                print(peptideDict)

                self.max_pep = 1

                for list in peptideDict.values():
                    self.max_pep *= len(list)

                print(self.max_pep)
                time_st = (0.0000000199 * self.max_pep + -0.0316)
                time_st = int(time_st)

                self.thread_pep = MyPeptide()
                print("MyPeptide()")
                self.thread_pep.progress_pep.connect(self.finish_pep)
                self.thread_pep.start()
                print("Start()")
                self.ui.textEdit.setText('Working... the estimated time is: ' + str(time_st)+' Minutes')





    def finish_pep(self, value):
        print("Print")
        if value == 1:
            self.ui.gotostage2Button.setVisible(True)
            self.ui.gotostage2Button.setEnabled(True)
            self.ui.textEdit.setText('Your peptides has been generated, now continue to the second stage')
            self.ui.stage2Button.setEnabled(True)
            print('Helo')
#################################################################################################################################
########## Stage 2 Funcionamientooo###############################################################################################
##################################################################################################################################

    def moveStage2_Continue(self):
        self.swidget.setCurrentIndex(2)
        self.ui.label_stage2_newgame.setVisible(False)
        self.ui.label_5.setVisible(True)
        self.ui.stage2_selectButton.setVisible(True)
        self.ui.stage2_selectButton.clicked.connect(self.selectFolder_Stage2)
        self.ui.progressBar_2.setVisible(False)
        self.ui.runchimButton.setEnabled(True)
        self.ui.progressBar_2.setValue(0)
        self.ui.gotostage3Button.setEnabled(False)
        self.ui.gotostage3Button.setVisible(False)
        self.ui.stage4Button.setEnabled(False)
        self.ui.stage3Button.setEnabled(False)


    def selectFolder_Stage2(self):
        chimpyfile = "Scripts/ChimeraAuto-Run.py"
        path = os.path.expanduser('~\Documents' + "\\")
        self.dir_save = QFileDialog.getExistingDirectory(self, "Select your working directory", path, options=QFileDialog.DontUseNativeDialog)
        if self.dir_save != '':

            Path(self.dir_save + "/Scripts").mkdir(parents=True, exist_ok=True)
            Path(self.dir_save + "/Parameters").mkdir(parents=True, exist_ok=True)
            Path(self.dir_save + "/Chimera-Peptides").mkdir(parents=True, exist_ok=True)
            Path(self.dir_save + "/Ligands").mkdir(parents=True, exist_ok=True)
            Path(self.dir_save + "/VinaResults").mkdir(parents=True, exist_ok=True)
            shutil.copytree("chimpdbs", self.dir_save + "/Parameters//", dirs_exist_ok=True)
            shutil.copy(chimpyfile, self.dir_save + "/Scripts")
            os.chdir(self.dir_save)

            self.ui.label_8.setVisible(True)
            self.ui.spinBox.setVisible(True)
            self.ui.runchimButton.setVisible(True)

    def moveStage2_NewGame(self):
        self.swidget.setCurrentIndex(2)
        self.ui.label_stage2_newgame.setVisible(True)
        self.ui.label_8.setVisible(True)
        self.ui.spinBox.setVisible(True)
        self.ui.runchimButton.setVisible(True)
        self.ui.progressBar_2.setVisible(False)
        self.ui.progressBar_2.setValue(0)
        self.ui.gotostage3Button.setEnabled(False)

    def stage2_RunChim(self):
        self.ui.progressBar_2.setValue(0)
        self.ui.progressBar_2.setMaximum(100)
        self.ui.progressBar_2.setVisible(True)
        self.ui.label_working.setVisible(True)
        self.number_box = self.ui.spinBox.value()


        archivo_entrada = open('peptides.txt', 'r')
        lineas = archivo_entrada.readlines()
        archivo_entrada.close()
        print(len(lineas))
        numero_lineas_deseado = self.number_box
        if len(lineas) < numero_lineas_deseado:
            lineas_aleatorias = random.sample(lineas, len(lineas))

        else:
            lineas_aleatorias = random.sample(lineas, numero_lineas_deseado)

        archivo_nuevo = open('random.txt', 'w')
        archivo_nuevo.writelines(lineas_aleatorias)
        archivo_nuevo.close()
        self.lineas_alnum = len(lineas_aleatorias)
        magic_num = 0
        num = 0
        self.inicio = time.time()

        if self.lineas_alnum >= 25:
            magic_num = int(self.lineas_alnum/25)
            num = 25
            print(magic_num)

        if self.lineas_alnum < 25:
            num = self.lineas_alnum
            magic_num = 1
            print('Menor a 25')

        for i in range(magic_num):


            with open("Parameters/parameters.dat", "w") as bin:
                bin.write(str(i*num)+ '\n')
                bin.write(str((i+1)*num))
                bin.flush()
                bin.close()

            self.ui.runchimButton.setEnabled(False)
            self.thread2 = MyChim(magic_num, i)
            self.thread2.progress_updated3.connect(self.progress_bar_chim)
            self.thread2.start()

            time.sleep(2)




    def progress_bar_chim(self, value):

        self.ui.progressBar_2.setMaximum(self.lineas_alnum)
        self.ui.progressBar_2.setValue(value)

        if self.lineas_alnum == value:

            self.ui.label_working.setVisible(False)
            self.ui.stage3Button.setEnabled(True)
            self.ui.runchimButton.setEnabled(False)
            self.ui.stage2_selectButton.setEnabled(False)
            self.ui.gotostage3Button.clicked.connect(self.moveStage3_FromNew)
            self.ui.stage3Button.clicked.connect(self.moveStage3_FromNew)
            self.ui.gotostage3Button.setVisible(True)
            self.ui.runchimButton.setEnabled(True)
            self.ui.gotostage3Button.setEnabled(True)
            final= time.time() - self.inicio
            print(final/60)

#################################################################################################################################
########## Stage 3 Funcionamientooo###############################################################################################
##################################################################################################################################
    def moveStage3_FromContin(self):
        self.swidget.setCurrentIndex(3)
        self.ui.label_stage3_NewGame.setVisible(False)
        self.ui.First_Stage3.setVisible(False)
        self.ui.Second_Stage3.setVisible(False)
        self.ui.Third_Stage3.setVisible(False)
        self.ui.gotostage4Button.setVisible(False)
        self.ui.select_stage3Button.setEnabled(True)
        self.ui.stage4Button.setEnabled(False)

    def moveStage3_FromNew(self):
        self.swidget.setCurrentIndex(3)
        self.ui.label_stage3_Continue.setVisible(False)
        self.ui.Continue_stage3.setVisible(False)
        self.ui.First_Stage3.setVisible(True)
        self.ui.Second_Stage3.setVisible(False)
        self.ui.Third_Stage3.setVisible(False)
        self.ui.gotostage4Button.setVisible(False)
        self.ui.progressBar_vina.setVisible(False)

    def selectFolder_Stage3(self):
        chimpyfile = "Scripts/ChimeraAuto-Run.py"
        path = os.path.expanduser('~\Documents' + "\\")
        self.dir_save = QFileDialog.getExistingDirectory(self, "Select your working directory", path, options=QFileDialog.DontUseNativeDialog)

        if self.dir_save != '':
            Path(self.dir_save + "/Scripts").mkdir(parents=True, exist_ok=True)
            Path(self.dir_save + "/Parameters").mkdir(parents=True, exist_ok=True)
            Path(self.dir_save + "/Chimera-Peptides").mkdir(parents=True, exist_ok=True)
            Path(self.dir_save + "/Ligands").mkdir(parents=True, exist_ok=True)
            Path(self.dir_save + "/VinaResults").mkdir(parents=True, exist_ok=True)
            shutil.copytree("chimpdbs", self.dir_save + "/Parameters//", dirs_exist_ok=True)
            shutil.copy(chimpyfile, self.dir_save + "/Scripts")
            os.chdir(self.dir_save)
            self.ui.First_Stage3.setVisible(True)
            self.ui.progressBar_vina.setVisible(False)

    def stage3_SetPDBQT(self):
            try:
                obConversion = ob.OBConversion()
                obConversion.SetInAndOutFormats("pdb", "pdbqt")

                number_read = self.ui.spinBox_2.value()
                print(number_read)
                mol = ob.OBMol()
                for pdbs in range(number_read):

                    pdb = str(pdbs + 1)  # este +1 es para no empezar desde 0
                    archivo = (pdb+".pdb")
                    if os.path.exists(os.path.join("Chimera-Peptides/", archivo)):
                        obConversion.ReadFile(mol, "Chimera-Peptides/" + pdb + ".pdb")
                        # Open Babel will uncompress automatically
                        mol.AddHydrogens()
                        obConversion.WriteFile(mol, "Ligands/" + pdb + '.pdbqt')

                    else:
                        break

                print(self.dir_save)

                os.umask(0)
                os.chmod('VinaResults', 0o777)
                self.ui.Second_Stage3.setVisible(True)
                self.ui.select_stage3Button.setEnabled(False)
            except Exception as e:
                print("Error al ejecutar el comando:", e)


    def stage3_SelectProtein(self):

        self.protein_save, _ = QFileDialog.getOpenFileName(self, "Select Your Protein", self.dir_save, "PDBQT(*.pdbqt)", options=QFileDialog.DontUseNativeDialog)
        #trash, self.protein_save = os.path.split(str(self.protein_save))
        # if self.protein_save != None:
        #     self.ui.selectprotein_stage3Button.setEnabled(False)
        print(self.protein_save)

    def stage3_SelectLigands(self):

        self.ligands_save, _ = QFileDialog.getOpenFileNames(self, "Select Your Ligands", self.dir_save,
                                                            "PDBQT(*.pdbqt)", options=QFileDialog.DontUseNativeDialog)
        # self.ui.selectpep_stage3Button.setEnabled(False)
        print(self.ligands_save)
        if self.protein_save != None:
            if self.ligands_save != []:
                self.ui.Third_Stage3.setVisible(True)

    def stage3_ConfVina(self):
        self.confwin.show()

    def saveConfig(self):
        vx = self.confwin.ui.centerx_box.value()
        vy = self.confwin.ui.centery_box_2.value()
        vz = self.confwin.ui.centerx_box_3.value()
        self.center = [vx, vy, vz]
        print(self.center)
        sx = self.confwin.ui.sizeX_box.value()
        sy = self.confwin.ui.sizey_box.value()
        sz = self.confwin.ui.sizeZ_box.value()
        self.size = [sx, sy, sz]
        print(self.size)
        exh = self.confwin.ui.Exhaustivness_box.value()
        print(exh)

        self.ui.progressBar_vina.setValue(0)


        with open('config.txt', "w") as c:
            c.write('center_x = ')
            c.write(str(vx))
            c.write('\n')
            c.write('center_y= ')
            c.write(str(vy))
            c.write('\n')
            c.write('center_z = ')
            c.write(str(vz))
            c.write('\n')
            c.write('size_x = ')
            c.write(str(sx))
            c.write('\n')
            c.write('size_y= ')
            c.write(str(sy))
            c.write('\n')
            c.write('size_z = ')
            c.write(str(sz))
            c.write('\n')
            c.write('num_modes = 10')
            c.write('\n')
            c.write('energy_range = 4')
            c.write('\n')
            c.write('exhaustiveness = ')
            c.write(str(exh))
            c.write('\n')


        self.ui.configureVinaButton.setVisible(False)
        self.ui.runVinaButton.setVisible(True)
        self.confwin.close()

    def stage3_RunVina(self, text):

        folder = self.dir_save + "/VinaResults/"

        files = os.listdir(folder)
        howmanyfiles = (len(files))

        msj = QMessageBox()
        msj.setFont(QFont("Eight Bit Dragon", 8))
        msj.setContentsMargins(0, 30, 0, 0)
        msj.setStyleSheet(
            'QDialog{border: 2px solid rgb(120, 120, 120);}' '*{background-color: rgb(40,40, 32); color: white; top-margin: 30px;}')
        msj.setWindowFlag(Qt.FramelessWindowHint)

        if howmanyfiles > 0:
            msj.setText("You have at least one file in the VinaResults folder, delete or back-up those files")
            msj.setIcon(QMessageBox.Warning)
            msj.setWindowTitle("Warning")
            msj.exec_()
        else:
            self.ui.progressBar_vina.setVisible(True)
            self.thread = MyThread(self.protein_save, self.ligands_save, self.dir_save)
            self.thread.progress_updated.connect(self.update_progress_bar)
            self.thread.start()

            print(self.ui.progressBar_vina.value())
            print('HEREHEREHERE')
            if self.ui.progressBar_vina.value() >= 100:
                self.stage4but()

            self.ui.runVinaButton.setVisible(False)

    def update_progress_bar(self, value):
        # Esta función actualiza el valor de la barra de progreso y la etiqueta con el valor dado
        # self.progress_bar.setMaximum(len(self.ligands_save))
        # self.progress_bar.setValue(value)

        #print(len(self.ligands_save))
        self.ui.progressBar_vina.setMaximum(len(self.ligands_save))
        self.ui.progressBar_vina.setValue(value)
        if self.ui.progressBar_vina.value() == len(self.ligands_save):
            self.ui.gotostage4Button.setVisible(True)

#################################################################################################################################
########## Stage 4 Funcionamientooo###############################################################################################
##################################################################################################################################

    def moveStage4_FromContin(self):
        self.swidget.setCurrentIndex(4)

        self.ui.frame_Selectpeptides.setVisible(False)
        self.ui.label_stage4.setVisible(False)
        self.ui.frame_10.setVisible(False)
        self.ui.tableWidget_2.setVisible(False)
        self.ui.tableWidget.setVisible(False)
        self.ui.resetRPGButton.setVisible(False)
        self.ui.frame_14.setVisible(False)
        self.ui.frame_continue.setVisible(True)
        self.ui.choosedir_stage4.setVisible(True)

    def moveStage4_FromNew(self):
        self.swidget.setCurrentIndex(4)
        self.ui.frame_continue.setVisible(False)
        self.ui.frame_Selectpeptides.setVisible(True)
        self.ui.choosedir_stage4.setVisible(False)
        self.ui.frame_10.setVisible(False)
        self.ui.tableWidget_2.setVisible(False)
        self.ui.resetRPGButton.setVisible(False)
        self.ui.tableWidget.setVisible(False)
        self.ui.frame_14.setVisible(False)

    def selectFolder_Stage4(self):
        chimpyfile = "Scripts/ChimeraAuto-Run.py"
        path = os.path.expanduser('~\Documents' + "\\")
        self.dir_save = QFileDialog.getExistingDirectory(self, "Select your working directory", path)
        if self.dir_save != '':

            shutil.copytree("chimpdbs", self.dir_save + "/Parameters//", dirs_exist_ok=True)
            shutil.copy(chimpyfile, self.dir_save + "/Scripts")
            os.chdir(self.dir_save)
            self.ui.frame_Selectpeptides.setVisible(True)

            self.ui.label_stage4.setVisible(True)
            self.ui.choosedir_stage4.setVisible(False)

    def stage4_CSV(self):

        msj = QMessageBox()
        msj.setFont(QFont("Eight Bit Dragon", 8))
        msj.setContentsMargins(0, 30, 0, 0)
        msj.setStyleSheet(
            'QDialog{border: 2px solid rgb(120, 120, 120);}' '*{background-color: rgb(40,40, 32); color: white;}')
        msj.setWindowFlag(Qt.FramelessWindowHint)

        if self.ui.aff_spinbox.value() == 0:
            msj.setText("You must choose a negative number")
            msj.setIcon(QMessageBox.Warning)
            msj.setWindowTitle("Warning")
            msj.exec_()

        else:

            self.ui.tableWidget.setVisible(True)
            with open('peptides.txt', "r") as f:
                ligandnumber = int
                ligandnumber = (len(f.readline()) - 1)

            listofdict = []
            field = ["Peptide Name", "Affinity"]
            self.numpep = 0
            for root_dir, cur_dir, files in os.walk(r'VinaResults/'):
                self.numpep += len(files)

            # print(ligandnumber)
            # print(self.numpep)
            self.bestpepnum = 0

            print(self.numpep)

            for j in range(ligandnumber):
                field.append(j + 1)
            with open("random.txt", 'r') as f:
                newline = []
                for i, line in enumerate(f):
                    print(i)
                    if i + 1 <= self.numpep:
                        dct = {"Peptide Name": [""], "Affinity": [""]}
                        for o in range(ligandnumber):
                            dct[o + 1] = ['']

                        name = 'VinaResults/' + str(i + 1) + "-out.pdbqt"
                        print(name)
                        file = open(name, 'r')
                        content = file.readlines()[1]
                        spl = content.split()
                        affinity = spl[3]
                        number = self.ui.aff_spinbox.value()
                        if float(affinity) < number:
                            dct["Peptide Name"] = (str(i + 1))
                            dct["Affinity"] = float(affinity)
                            newline.append(line)

                            l = list(line)
                            print(i)
                            print(l)

                            self.n = 1
                            for k in l[:-1]:
                                dct[self.n] = k
                                self.n += 1
                                #print(dct)
                            self.bestpepnum += 1
                            listofdict.append(dct)
                        else:
                            ...
                            #print('Low Affinity')

                        dct = {}

                    else:
                        break


            with open('Best-Peptides.csv', 'w') as f:
                w = csv.DictWriter(f, fieldnames=field)

                w.writeheader()

                for l in listofdict:
                    w.writerow(l)
            try:

                self.csv_data = pd.read_csv("Best-Peptides.csv")

                self.ui.tableWidget.setColumnCount(len(self.csv_data.columns))
                self.ui.tableWidget.setRowCount(len(self.csv_data.index))
                self.ui.tableWidget.setHorizontalHeaderLabels(self.csv_data.columns)
                # print(self.ui.tableWidget.currentColumn())


                for i in range(len(self.csv_data.index)):
                    for j in range(len(self.csv_data.columns)):
                        # self.ui.tableWidget.setItem(i, j, QTableWidgetItem(str(self.csv_data.iat[i, j])))
                        item = QTableWidgetItem(str(self.csv_data.iat[i, j]))
                        item.setFlags(item.flags() ^ (QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsSelectable))
                        self.ui.tableWidget.setItem(i, j, item)

                self.ui.tableWidget.sortItems(1, order=Qt.AscendingOrder)
                self.ui.frame_10.setVisible(True)


                self.ui.resetRPGButton.setVisible(True)
                self.ui.pymol_button.setEnabled(True)
                self.ui.frame_14.setVisible(True)
                self.ui.pymol_button.setText('Open PyMOL')

            except Exception as e:
                print("Error al ejecutar el comando:", e)
    def stage4_BestAmino(self):

        porcent_cover = (self.ui.confidenceSpinbox.value()/100)
        ligandnumber = int(self.n)-1
        numpep2 = int(self.bestpepnum)
        print(numpep2)
        peplist = []
        aalist = ['A', 'N', 'R', 'D', 'C', 'Q', 'E', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P', 'O', 'S', 'U', 'T', 'W',
                  'Y', 'V', 'B', 'Z', 'X']
        df = pd.read_csv("Best-Peptides.csv")
        for j in range(ligandnumber):
            # field.append(j + 1)
            peplist.append(str(j + 1))


        with open('Best-AminoAcids.csv', 'w') as f:
            w = csv.writer(f)
            w.writerow(["Peptide Position", "Best AminoAcid"])
            for aa in aalist:
                print(peplist)
                count = df[peplist].applymap(lambda x: str.count(x, aa)).sum()
                for i in peplist:
                    # print(count[i])
                    if count[i] >= (numpep2 * porcent_cover):
                        w.writerow([i, aa])

        self.ui.tableWidget_2.setVisible(True)

        self.csv_data2 = pd.read_csv("Best-AminoAcids.csv")

        self.ui.tableWidget_2.setColumnCount(len(self.csv_data2.columns))
        self.ui.tableWidget_2.setRowCount(len(self.csv_data2.index))
        self.ui.tableWidget_2.setHorizontalHeaderLabels(self.csv_data2.columns)



        for i in range(len(self.csv_data2.index)):
            for j in range(len(self.csv_data2.columns)):
                self.ui.tableWidget_2.setItem(i, j, QTableWidgetItem(str(self.csv_data2.iat[i, j])))

        self.ui.resetRPGButton.setVisible(True)
        self.ui.pymol_button.setEnabled(True)

    def ena_Pymol(self):
        try:
            value = self.ui.spinBox_pymol.value()
            if self.protein_save != None:
                pass


            else:
                self.protein_save, _ = QFileDialog.getOpenFileName(self, "Select Your Protein", self.dir_save,
                                                                   "PDBQT(*.pdbqt)",
                                                                   options=QFileDialog.DontUseNativeDialog)
                # trash, self.protein_save = os.path.split(str(self.protein_save))

                print(self.protein_save)

            command = 'pymolwin -d "load {}; hide all; show surface; color white; load .\/VinaResults/{}-out.pdbqt"'.format(self.protein_save, str(value))
            os.system(command)

        except Exception as e:
            print("Error al ejecutar el comando:", e)



#################################################################################################################################
########## Ventana de Vina ###############################################################################################
###########################################################################################################
class Window(QDialog):

    def __init__(self, parent=None):
        QDialog.__init__(self)
        self.vinaui = Ui_Dialog()
        self.vinaui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.move(1100, 100)



#################################################################################################################################
########## Seccion de Threads ###############################################################################################
###########################################################################################################
class MyThread(QThread):
    # Se define una señal que será emitida cuando se haya actualizado el progreso
    progress_updated = pyqtSignal(int)

    def __init__(self, protein, ligands, dir_save):
        QThread.__init__(self)
        self.protein = protein
        self.ligands = ligands
        self.dir_save = dir_save
        self.win = MainWindow(self)


    def run(self):
        print(self.protein)
        # Esta función contiene la lógica que se ejecutará en un hilo separado
        ligsum = 0

        # Se crea un ThreadPoolExecutor con el número máximo de hilos que se ejecutarán simultáneamente
        with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
            # Se crea una lista de Futures, que representan las tareas que se ejecutarán en hilos separados
            futures = []
            # Se realiza un bucle que simula una tarea larga y que actualiza el progreso cada 0.5 segundos
            for ligand in self.ligands:

                ligname = str(ligsum + 1)

                # Se agrega una tarea al ThreadPoolExecutor

                future = executor.submit(self.run_command, ligand, ligname)
                futures.append(future)

                ligsum = ligsum + 1

            concurrent.futures.wait(futures)

            folder = self.dir_save + "/VinaResults/"

            files = os.listdir(folder)
            self.progress_updated.emit(len(files))

            # Se espera a que todas las tareas del ThreadPoolExecutor hayan terminado


        # Se emite la señal de progreso actualizado cuando todos los hilos han terminado



    def run_command(self, ligand, ligname):
        # Esta función ejecuta el comando en un hilo separado

        dir = self.dir_save + '/VinaResults/'+ ligname
        command = 'vina --receptor {} --ligand {} --config {}/config.txt --out {}-out.pdbqt'.format(self.protein, ligand, self.dir_save, dir)
        os.system(command)
        folder = self.dir_save + "/VinaResults/"
        files = os.listdir(folder)
        print(str(len(files)))
        self.progress_updated.emit(len(files))


class MyChim(QThread):
    progress_updated3 = pyqtSignal(int)
    def __init__(self, magic, i):
        QThread.__init__(self)
        self.magic = magic
        self.i = i


    def run(self):
        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor2:
            try:
                futures2 = []
                future2 = executor2.submit(self.runChim)
                futures2.append(future2)

                concurrent.futures.wait(futures2)

            except Exception as e:
                print("Error al ejecutar el comando:", e)


        return print('Listo')



    def runChim(self):

        # os.system('chimera --nogui Scripts/ChimeraAuto-Run.py')
        # print('Hi')
        comando = ['chimera', '--nogui', 'Scripts/ChimeraAuto-Run.py']
        palabra_buscar = 'Model'
        contador = 0

        try:
            proceso = subprocess.Popen(comando, stdout=subprocess.PIPE, universal_newlines=True)
            # print('Hi2')
            for linea in proceso.stdout:
                # print(linea)
                # Buscar la palabra en la línea (puedes usar otras lógicas de búsqueda según tus necesidades)
                if palabra_buscar in linea:
                    contador += 1
                    # print('Peptido :'+str(contador*self.magic))
                    # print(self.i+1)
                    # print(self.magic)
                    if self.magic == (self.i+1):
                        self.progress_updated3.emit(contador*self.magic)


            proceso.wait()

        except subprocess.CalledProcessError as e:
            print("Error al ejecutar el comando:", e)

        print(f"La palabra '{palabra_buscar}' apareció {contador} veces en la salida.")


class MyPeptide(QThread):
    progress_pep = pyqtSignal(int)

    def __init__(self):
        QThread.__init__(self)

    def run(self):
        self.progress_pep.emit(0)
        destino = 'peptides.txt'
        length = len(peptideDict)
        self.num_processes = length

        with concurrent.futures.ThreadPoolExecutor(max_workers=self.num_processes) as executor:
            try:
                futures = []
                args_list = [(peptideDict, length, self.num_processes, i) for i in range(self.num_processes)]
                for args in args_list:
                    future = executor.submit(self.generate_peptides_helper, args)
                    futures.append(future)

                concurrent.futures.wait(futures)

            except Exception as e:
                print("Error:", e)

        self.unir_archivos(destino)
        self.progress_pep.emit(1)

    def unir_archivos(self, destino):
        with open(destino, 'w') as archivo_destino:
            for archivo in range(self.num_processes):
                print(archivo)
                with open(str(archivo), 'r') as archivo_fuente:
                    contenido = archivo_fuente.read()
                    archivo_destino.write(contenido)
                os.remove(str(archivo))

    def generate_peptides_helper(self, args):
        pepdict, length, num_processes, process_index = args
        peptides = []
        suma = 0
        bar = 0
        amino_acids_lists = [pepdict[i] for i in range(length)]  # Get lists of amino acids
        print("Instance method")
        try:
            with open(str(process_index), 'w') as w:
                ...
            for c in product(*amino_acids_lists):
                if sum([amino_acids_lists[i].index(aa) for i, aa in enumerate(c)]) % length == process_index:
                    peptides.append(''.join(c) + '\n')
                    suma += 1
                    bar += 1
                    if suma == 1000000:
                        with open(str(process_index), 'a') as w:
                            for pep in peptides:
                                cadena = ''.join(pep)
                                w.write(cadena)
                                suma = 0
                                peptides = []
                            w.close()
                        print('Progress ' + str(process_index) + ':' + str(bar * num_processes))

            with open(str(process_index), 'a') as w:
                for pep in peptides:
                    cadena = ''.join(pep)
                    w.write(cadena)
                w.close()
            print('Progress ' + str(process_index) + ':' + str(bar * num_processes))

        except Exception as e:
            print("An error occurred:", e)

# class MyPeptide(QThread):
#     progress_pep = pyqtSignal(int)
#     def __init__(self):
#         QThread.__init__(self)
#
#     def run(self):
#
#         self.progress_pep.emit(0)
#         destino = 'peptides.txt'
#         archivos = []
#         length = len(peptideDict)
#         self.num_processes = (length)
#         pool = multiprocessing.Pool(processes=self.num_processes)
#         print("Star Pool")
#         args_list = [(peptideDict, length, self.num_processes, i) for i in range(self.num_processes)]
#         pool.map(self.generate_peptides_helper, args_list)
#         self.unir_archivos(destino)
#         return self.progress_pep.emit(1)
#
#
#     def unir_archivos(self, destino):
#
#         with open(destino, 'w') as archivo_destino:
#             for archivo in range(self.num_processes):
#                 print(archivo)
#                 with open(str(archivo), 'r') as archivo_fuente:
#                     contenido = archivo_fuente.read()
#                     archivo_destino.write(contenido)
#                 os.remove(str(archivo))
#
#
#
#     @staticmethod
#     def generate_peptides_helper(args):
#         pepdict, length, num_processes, process_index = args
#         peptides = []
#         suma = 0
#         bar = 0
#         amino_acids_lists = [pepdict[i] for i in range(length)]  # Get lists of amino acids
#         print("Staticmethod")
#         try:
#             with open(str(process_index), 'w') as w:
#                 ...
#             for c in product(*amino_acids_lists):
#                 if sum([amino_acids_lists[i].index(aa) for i, aa in enumerate(c)]) % length == process_index:
#                     peptides.append(''.join(c) + '\n')
#                     suma += 1
#                     bar += 1
#                     if suma == 1000000:
#                         with open(str(process_index), 'a') as w:
#                             for pep in peptides:
#
#                                 cadena = ''.join(pep)
#                                 w.write(cadena)
#                                 suma = 0
#                                 peptides = []
#
#                             w.close()
#                         print('Progreso '+str(process_index)+ ':' + str(bar*num_processes))
#
#             with open(str(process_index), 'a') as w:
#                 for pep in peptides:
#                     cadena = ''.join(pep)
#                     w.write(cadena)
#
#                 w.close()
#             print('Progreso '+str(process_index)+ ':' + str(bar*num_processes))
#
#         except Exception as e:
#             print("Ocurrió un error:", e)





