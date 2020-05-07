from PyQt5 import QtCore, QtGui, QtWidgets
from second_screen import Ui_MainWindow2

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        font = QtGui.QFont()
        font.setPointSize(10)

        font = QtGui.QFont()
        font.setPointSize(10)

        self.label_start_window = QtWidgets.QLabel(self.centralwidget)
        self.label_start_window.setGeometry(QtCore.QRect(25, 50, 700, 91))
        font = QtGui.QFont()
        font.setFamily("Old English Text MT")
        font.setPointSize(24)
        self.label_start_window.setFont(font)
        self.label_start_window.setObjectName("label_start_window")

        self.swapper = QtWidgets.QPushButton(self.centralwidget)
        self.swapper.setGeometry(QtCore.QRect(100, 200, 250, 71))
        self.swapper.setObjectName("swapper")

        
        self.optionsbutton = QtWidgets.QPushButton(self.centralwidget)
        self.optionsbutton.setGeometry(QtCore.QRect(450, 200, 251, 71))
        self.optionsbutton.setObjectName("optionsbutton")

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

        self.swapper.clicked.connect(self.secondscr)

    def secondscr(self):
        self.MainWindow2 = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow2()
        self.ui.setupUi(self.MainWindow2)
        self.MainWindow2.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Vokabeltrainer 3000"))

        self.swapper.setText(_translate("MainWindow", "Start"))
        self.optionsbutton.setText(_translate("MainWindow", "Options"))
        self.label_start_window.setText(_translate("MainWindow", "Vokabeltrainer 3000 - Version 0.005"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
