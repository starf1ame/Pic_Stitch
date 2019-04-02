# -*- coding: utf-8 -*-
from GUI import mainWindow, runPic1x2, runPic1x3
import sys
from PyQt5 import QtWidgets, uic,QtCore,QtGui
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QApplication
from PyQt5.QtGui import QIcon

Ui_MainWindow = mainWindow.Ui_MainWindow
RUNpic1x2 = runPic1x2.Ui_Dialog
RUNpic1x3 = runPic1x3.Ui_Dialog

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
    def open(self):
        self.show()

class run1x3_Qt(QtWidgets.QMainWindow,RUNpic1x3):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        RUNpic1x3.__init__(self)
        self.setupUi(self)
    def open(self):
        self.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_Window = QtMain()
    run1x2 = run1x2_Qt()
    run1x3 = run1x3_Qt()
    main_Window.show()
    main_Window.pushButton.clicked.connect(run1x2.open)
    main_Window.pushButton_2.clicked.connect(run1x3.open)
    sys.exit(app.exec_())