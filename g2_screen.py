from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QLineEdit, QWidget, QHBoxLayout, QLabel
from g3_screen import Ui_MainWindow
import random
class Ui_MainWindow_g2(object):
    def __init__(self,message_g2="Test"):               #644_g2_t_g3ie
        self.message_g2 = message_g2
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 300)

        
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.foto1 = QtWidgets.QLabel(self.centralwidget)
        self.foto1.setGeometry(QtCore.QRect(10, 40, 541, 351))
        self.foto1.setText("")
        self.foto1.setPixmap(QtGui.QPixmap("../test/108389_04.JPG"))
        self.foto1.setScaledContents(True)
        self.foto1.setObjectName("foto1")

        self.sky = QtWidgets.QPushButton(self.centralwidget)
        self.sky.setGeometry(QtCore.QRect(280, 110, 150, 30))
        self.sky.setObjectName("sky")

        self.exit_button = QtWidgets.QPushButton(self.centralwidget)
        self.exit_button.setGeometry(QtCore.QRect(280, 200, 151, 31))
        self.exit_button.setObjectName("sky")

        #lineedit
        self.lineedit = QLineEdit(self.centralwidget)
        self.lineedit.setFont(QtGui.QFont("Sanserif",15))
        self.lineedit.setGeometry(QtCore.QRect(50, 100, 200, 50))

        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(20, 20, 600, 91))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label1.setFont(font)
        self.label1.setObjectName("label1")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.exit_button.clicked.connect(lambda:self.closescr(MainWindow))

        ##0sc003
        self.sky.clicked.connect(self.g3_scr)
        self.sky.clicked.connect(lambda:self.closescr(MainWindow))


    #0041close
    def closescr(self, MainWindow):
        MainWindow.hide()

    ##0sc003
    def g3_scr(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.message = self.lineedit.text() #644_g2_t_g3ie
        self.message_g2_3 = self.message_g2 #644_g2_t_g3ie
        self.ui = Ui_MainWindow(self.message,self.message_g2_3) #644_g2_t_g3ie
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Enter a number"))
        self.sky.setText(_translate("MainWindow", "Go!"))
        self.exit_button.setText(_translate("MainWindow", "Back"))
        self.label1.setText(_translate("MainWindow", "Enter how many words to check (max="+str(len(Ui_MainWindow.deck.karteikasten)))+")")
  
"""        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_g2()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
"""
