import sys
import os
from PyQt5.QtWidgets import QApplication
from MainWin.PrincipalWindow import MainWindow
from PepWin.PeptideWindow import PepWindow
from PyQt5 import QtGui



if __name__ == "__main__":

    app = QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('icon.ico'))
    main_window = MainWindow()
    sec_window = PepWindow()
    # main_window.setWindowTitle("RPG")
    # main_window.setFixedWidth(800)
    # main_window.setFixedHeight(650)
    main_window.show()

    # sec_window.show()
    # sec_window.hide()
    sys.exit(app.exec_())
