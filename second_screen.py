from PyQt5 import QtCore, QtGui, QtWidgets
from g2_screen import Ui_MainWindow_g2

class Ui_MainWindow2(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.foto1 = QtWidgets.QLabel(self.centralwidget)
        self.foto1.setGeometry(QtCore.QRect(10, 40, 541, 351))
        self.foto1.setText("")
        self.foto1.setPixmap(QtGui.QPixmap("../test/108389_04.JPG"))
        self.foto1.setScaledContents(True)
        self.foto1.setObjectName("foto1")

        self.truck_2 = QtWidgets.QPushButton(self.centralwidget)
        self.truck_2.setGeometry(QtCore.QRect(50, 200, 131, 31))
        self.truck_2.setObjectName("truck_2")

        self.sky = QtWidgets.QPushButton(self.centralwidget)
        self.sky.setGeometry(QtCore.QRect(200, 200, 151, 31))
        self.sky.setObjectName("sky")

        self.exit_button = QtWidgets.QPushButton(self.centralwidget)
        self.exit_button.setGeometry(QtCore.QRect(200, 250, 151, 31))
        self.exit_button.setObjectName("sky")


        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(50, 50, 400, 91))
        font = QtGui.QFont()
        font.setFamily("Old English Text MT")
        font.setPointSize(36)
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
        
        self.sky.clicked.connect(self.g2_scr_1)
        self.sky.clicked.connect(lambda:self.closescr(MainWindow))
        self.truck_2.clicked.connect(self.g2_scr_2)
        self.truck_2.clicked.connect(lambda:self.closescr(MainWindow))

        #0041close
        self.exit_button.clicked.connect(lambda:self.closescr(MainWindow))

    #0041close
    def closescr(self, MainWindow):
        MainWindow.hide()

    def g2_scr_1(self):
        self.MainWindow_g2 = QtWidgets.QMainWindow()
        self.message_g2 = 1 #se_deen_1
        self.ui = Ui_MainWindow_g2(self.message_g2) #se_deen_1
        self.ui.setupUi(self.MainWindow_g2)
        self.MainWindow_g2.show()

    def g2_scr_2(self):
        self.MainWindow_g2 = QtWidgets.QMainWindow()
        self.message_g2 = 0 #se_deen_1
        self.ui = Ui_MainWindow_g2(self.message_g2) #se_deen_1
        self.ui.setupUi(self.MainWindow_g2)
        self.MainWindow_g2.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Chose Language"))
        self.truck_2.setText(_translate("MainWindow", "English - German"))  #truck_2
        self.sky.setText(_translate("MainWindow", "German - English"))
        self.exit_button.setText(_translate("MainWindow", "Back"))
        self.label1.setText(_translate("MainWindow", "Choose language"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow2()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
