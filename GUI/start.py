# -*- coding: utf-8 -*-
from GUI import mainWindow, runPic1x2, runPic1x3, runPic2x2, runPic2x1, runPic3x1
from PyQt5.QtWidgets import *
import sys
from PyQt5 import QtWidgets, uic,QtCore,QtGui
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QApplication
from PyQt5.QtGui import QIcon

Ui_MainWindow = mainWindow.Ui_MainWindow
RUNpic1x2 = runPic1x2.Ui_Dialog
RUNpic2x1 = runPic2x1.Ui_Dialog
RUNpic1x3 = runPic1x3.Ui_Dialog
RUNpic2x2 = runPic2x2.Ui_Dialog
RUNpic3x1 = runPic3x1.Ui_Dialog

class QtMain(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)

        self.initUI()

        Ui_MainWindow.__init__(self)
        self.setupUi(self)

    def initUI(self):

        '''
        create exitAction of fileMenu
        '''

        exitAction = QAction(QIcon('pic/exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)

        '''
        statusBar, need to modify
        '''
        self.statusBar().showMessage("Ready")

        '''
        create menu
        '''
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)
        menubar.setNativeMenuBar(False)

        '''
        toolbar in the menu
        '''
        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exitAction)

class run1x2_Qt(QtWidgets.QMainWindow,RUNpic1x2):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        RUNpic1x2.__init__(self)
        self.setupUi(self)
    def open(self,dir):
        if not(dir):
            QMessageBox.warning(self, "warning", \
                "Please choose a direction you want to stitch on", QMessageBox.Cancel)
            return 0
        if (dir == 2):
            self.show()

class run2x1_Qt(QtWidgets.QMainWindow,RUNpic2x1):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        RUNpic2x1.__init__(self)
        self.setupUi(self)
    def open(self,dir):
        if (dir == 1):
            self.show()

class run1x3_Qt(QtWidgets.QMainWindow,RUNpic1x3):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        RUNpic1x3.__init__(self)
        self.setupUi(self)
    def open(self,dir):
        if not(dir):
            QMessageBox.warning(self, "warning", \
                "Please choose a direction you want to stitch on", QMessageBox.Cancel)
            return 0
        if (dir == 2):
            self.show()

class run3x1_Qt(QtWidgets.QMainWindow,RUNpic3x1):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        RUNpic3x1.__init__(self)
        self.setupUi(self)
    def open(self,dir):
        if (dir == 1):
            self.show()

class run2x2_Qt(QtWidgets.QMainWindow,RUNpic2x2):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        RUNpic2x2.__init__(self)
        self.setupUi(self)
    def open(self):
        self.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_Window = QtMain()
    run1x2 = run1x2_Qt()
    run2x1 = run2x1_Qt()
    run1x3 = run1x3_Qt()
    run3x1 = run3x1_Qt()
    run2x2 = run2x2_Qt()
    main_Window.show()
    main_Window.pushButton.clicked.connect(lambda : run1x2.open(dir=main_Window.choose_1.currentIndex()))
    main_Window.pushButton.clicked.connect(lambda : run2x1.open(dir=main_Window.choose_1.currentIndex()))
    main_Window.pushButton_2.clicked.connect(lambda: run1x3.open(dir=main_Window.choose_2.currentIndex()))
    main_Window.pushButton_2.clicked.connect(lambda: run3x1.open(dir=main_Window.choose_2.currentIndex()))
    main_Window.pushButton_3.clicked.connect(run2x2.open)
    sys.exit(app.exec_())
