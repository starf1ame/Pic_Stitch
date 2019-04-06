# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'runPic1x2.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPalette, QPixmap, QColor
from PyQt5.QtWidgets import *
from Stitch import picStitchSIFT
from Stitch import picStitchSURF
import os
from PyQt5.QtGui import QIcon

class Ui_Dialog(object):

    targetFiles = {}
    alg_default = "SIFT"
    alg_list = ["SIFT", "SURF"]
    button_style = ('''
                       QPushButton
                       {text-align : center;
                       background-color : white;
                       font: bold;
                       border-color: gray;
                       border-width: 2px;
                       border-radius: 10px;
                       padding: 6px;
                       height : 14px;
                       border-style: outset;
                       min-width: 6em;
                       font: 12px \"Microsoft YaHei\";}
                       QPushButton:pressed
                       {text-align : center;
                       background-color : light gray;
                       font: bold;
                       border-color: gray;
                       border-width: 2px;
                       border-radius: 10px;
                       padding: 6px;
                       height : 14px;
                       border-style: outset;
                       min-width: 6em;
                       font : 12px \"Microsoft YaHei\";}
                       '''
                    )
    showSwitch = 0 # 1 means showing result now

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(815, 378)
        self.initUI()

        '''
        Label for the left side picture
        '''
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 90, 210, 190))
        self.label.setObjectName("label")

        '''
        Label for the right side picture
        '''
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(270, 90, 210, 190))
        self.label_2.setObjectName("label_2")

        '''
        Button for choosing the left side picture file
        '''
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(77, 300, 115, 35))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.left_pic)
        self.pushButton.setStyleSheet(self.button_style)

        '''
        Button for choosing the right side picture file
        '''
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(317, 300, 115, 35))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.right_pic)
        self.pushButton_2.setStyleSheet(self.button_style)

        '''
        Label for showing result
        '''
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(510, 130, 270, 150))
        self.label_3.setObjectName("label_3")

        '''
        Box for choosing algorithm
        '''
        self.chooseAlg = QtWidgets.QComboBox(Dialog)
        self.chooseAlg.setGeometry(QtCore.QRect(510, 90, 250, 30))
        self.chooseAlg.setObjectName("chooseAlgorithm")
        self.initAlg_box()

        # '''
        # ButtonBox for run the algorithm
        # '''
        # self.ifRun = QtWidgets.QDialogButtonBox(Dialog)
        # self.ifRun.setGeometry(QtCore.QRect(510, 300, 165, 30))
        # self.ifRun.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel| \
        #                               QtWidgets.QDialogButtonBox.Ok)
        # self.ifRun.setObjectName("ifRun")
        # self.ifRun.accepted.connect(self.runStich)  # 确定
        # self.ifRun.rejected.connect(self.close)  # 取消
        #
        '''
        Button for run the algorithm
        '''
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(510, 300, 115, 35))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setStyleSheet(self.button_style)
        self.pushButton_3.clicked.connect(self.runStich)

        '''
        Button for showing result of program
        '''
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(665, 300, 115, 35))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setStyleSheet(self.button_style)
        self.pushButton_4.clicked.connect(self.switch)


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "pic_1"))
        self.label_2.setText(_translate("Dialog", "pic_2"))
        self.pushButton.setText(_translate("Dialog", "choose left"))
        self.pushButton_2.setText(_translate("Dialog", "choose right"))
        self.pushButton_3.setText(_translate("Dialog", "Run Algorithm"))
        self.pushButton_4.setText(_translate("Dialog", "Show Switch"))
        self.label_3.setText(_translate("Dialog", "show_process"))

        pixmap = QPixmap("pic/c1.jpg")
        self.label.setScaledContents(True)
        self.label.setPixmap(pixmap)
        pixmap = QPixmap("pic/c1.jpg")
        self.label_2.setScaledContents(True)
        self.label_2.setPixmap(pixmap)
        pixmap = QPixmap("pic/c1.jpg")
        self.label_3.setScaledContents(True)
        self.label_3.setPixmap(pixmap)

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

    def initAlg_box(self):
        self.chooseAlg.addItem("Choose an Algorithm")
        self.chooseAlg.addItems(self.alg_list)

    def runStich(self):
        # print(self.chooseAlg.currentIndex())
        # print(self.chooseAlg.currentText())
        if (not("left" in self.targetFiles) or \
            not("right" in self.targetFiles)):
            QMessageBox.warning(self, "warning", \
                "Please Choose pictures", QMessageBox.Cancel)
            return 0
        if not(self.chooseAlg.currentIndex()):
            QMessageBox.warning(self, "warning", \
                "Please Choose Algorithm", QMessageBox.Cancel)
            return 0
        if (self.chooseAlg.currentIndex()==1):
            picStitchSIFT.pic_sti(self.targetFiles["left"], \
                self.targetFiles["right"], 'result.jpg')
        elif (self.chooseAlg.currentIndex()==2):
            picStitchSURF.pic_sti(self.targetFiles["left"], \
                self.targetFiles["right"], 'result.jpg')
        pixmap = QPixmap("../test/res_Pic/result.jpg")
        self.label_3.setScaledContents(True)
        self.label_3.setPixmap(pixmap)
        self.showSwitch = 1

    @pyqtSlot()
    def left_pic(self):
        openfile = \
        QFileDialog.getOpenFileName(self, '选择文件', '', 'All Files (*);;PNG Files (*.png);;JPG Files (*.jpg)')[0]
        print(openfile)
        pixmap = QPixmap(openfile)
        self.label.setScaledContents(True)
        self.label.setPixmap(pixmap)
        self.targetFiles["left"]=openfile
        print(self.targetFiles)

    @pyqtSlot()
    def right_pic(self):
        openfile = \
        QFileDialog.getOpenFileName(self, '选择文件', '', 'All Files (*);;PNG Files (*.png);;JPG Files (*.jpg)')[0]
        print(openfile)
        pixmap = QPixmap(openfile)
        self.label_2.setScaledContents(True)
        self.label_2.setPixmap(pixmap)
        self.targetFiles["right"] = openfile
        print(self.targetFiles)

    def switch(self):
        if (not os.path.exists("../test/res_Pic/result.jpg")):
            QMessageBox.warning(self, "warning", \
                "You haven't fininshed running", QMessageBox.Cancel)
            return 0
        if (self.showSwitch==0):
            pixmap = QPixmap("../test/res_Pic/result.jpg")
            self.label_3.setScaledContents(True)
            self.label_3.setPixmap(pixmap)
            self.showSwitch = 1
        elif (self.showSwitch==1):
            pixmap = QPixmap("../test/process/process.jpg")
            self.label_3.setScaledContents(True)
            self.label_3.setPixmap(pixmap)
            self.showSwitch = 0
