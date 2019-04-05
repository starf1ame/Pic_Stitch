from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    dir_list = ["up/down", "left/right"]

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 550)
        MainWindow.setStyleSheet("#MainWindow{background-color: white}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(MainWindow)
        self.label.setGeometry(QtCore.QRect(140, 70, 600, 250))
        self.label.setObjectName("label")


        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 250, 180, 180))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("pic/c1.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(175, 175))
        self.pushButton.setAutoRepeatDelay(200)
        self.pushButton.setObjectName("pushButton")

        '''
        Box for choosing up/down or left/right
        '''
        self.choose_1 = QtWidgets.QComboBox(MainWindow)
        self.choose_1.setGeometry(QtCore.QRect(30, 480, 180, 30))
        self.choose_1.setObjectName("chooseDir")
        self.initDir_box(choose=self.choose_1)

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 250, 180, 180))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("pic/c2.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setIconSize(QtCore.QSize(175, 175))
        self.pushButton_2.setAutoRepeatDelay(200)
        self.pushButton_2.setObjectName("pushButton_2")

        '''
        Box for choosing up/down or left/right
        '''
        self.choose_2 = QtWidgets.QComboBox(MainWindow)
        self.choose_2.setGeometry(QtCore.QRect(240, 480, 180, 30))
        self.choose_2.setObjectName("chooseDir")
        self.initDir_box(choose=self.choose_2)

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(450, 250, 180, 180))
        self.pushButton_3.setObjectName("pushButton_3")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("pic/c3.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon3)
        self.pushButton_3.setIconSize(QtCore.QSize(175, 175))
        self.pushButton_3.setAutoRepeatDelay(200)

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(660, 250, 180, 180))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("pic/c4.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon4)
        self.pushButton_4.setIconSize(QtCore.QSize(175, 175))
        self.pushButton_4.setAutoRepeatDelay(200)
        self.pushButton_4.setObjectName("pushButton_4")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Pic-stitch", "Pic-stitch"))
        pixmap = QtGui.QPixmap("pic/pic_stitch.jpg")
        self.label.setScaledContents(True)
        self.label.setPixmap(pixmap)
        self.pushButton.setText(_translate("MainWindow", ""))
        self.pushButton_2.setText(_translate("MainWindow", ""))
        self.pushButton_3.setText(_translate("MainWindow", ""))
        self.pushButton_4.setText(_translate("MainWindow", ""))

    def initDir_box(self,choose):
        choose.addItem("Choose a Direction")
        choose.addItems(self.dir_list)




