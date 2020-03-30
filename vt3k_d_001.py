from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")



        heigth_header = 50
        self.label_header = QtWidgets.QLabel(self.centralwidget)
        self.label_header.setGeometry(QtCore.QRect(50, heigth_header, 111, 51))
        self.label_header.setObjectName("label")


        height_label = 100
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, height_label, 111, 51))
        self.label.setObjectName("label")
        
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(200, height_label, 111, 51))
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(300, height_label, 111, 51))
        self.label_3.setObjectName("label_3")

        height_text = 200
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(100, height_text, 200, 25))
        self.plainTextEdit.setObjectName("plainTextEdit")
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(350, height_text-12, 140, 50))
        self.pushButton.setObjectName("pushButton")
##        self.pushButton.setStyleSheet("background-color: grey")

        height_label_4 = 250
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(100, height_label_4, 200, 50))
        self.label_4.setObjectName("label_4")
        self.label_4.setStyleSheet("background-color: green")


        
        height_buttons_2 = 400
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(100, height_buttons_2, 200, 50))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setStyleSheet("background-color: grey")

##        #501
##        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
##        self.toolButton.setGeometry(QtCore.QRect(50, 600, 25, 19))
##        self.toolButton.setObjectName("toolButton")
##        self.toolButton.setStyleSheet("background-color: green")

##        #523
##        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
##        self.radioButton.setGeometry(QtCore.QRect(50, 680, 82, 17))
##        self.radioButton.setObjectName("radioButton")
##        self.radioButton.setStyleSheet("background-color: blue")

##        #503
##        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
##        self.checkBox.setGeometry(QtCore.QRect(230, 700, 70, 17))
##        self.checkBox.setObjectName("checkBox")

##        #533
##        self.buttonBox = QtWidgets.QDialogButtonBox(self.centralwidget)
##        self.buttonBox.setGeometry(QtCore.QRect(100, 750, 156, 23))
##        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
##        self.buttonBox.setObjectName("buttonBox")
##        self.buttonBox.setStyleSheet("background-color: orange")

##        #555
##        self.listView = QtWidgets.QListView(self.centralwidget)
##        self.listView.setGeometry(QtCore.QRect(420, 600, 100, 100))
##        self.listView.setObjectName("listView")

        
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

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_header.setText(_translate("MainWindow", "VT3K Design 001 #01"))
        self.label.setText(_translate("MainWindow", "'Hallo'#11"))
        self.label_2.setText(_translate("MainWindow", "in #12"))
        self.label_3.setText(_translate("MainWindow", "English ?#13"))
        self.label_4.setText(_translate("MainWindow", "Correct! #142"))
        self.pushButton.setText(_translate("MainWindow", "Check! #1"))
        self.pushButton_2.setText(_translate("MainWindow", "Next Word ! #2"))
##        self.toolButton.setText(_translate("MainWindow", "...")) #501
##        self.radioButton.setText(_translate("MainWindow", "#RadioButton"))  #523
##        self.checkBox.setText(_translate("MainWindow", "CheckBox")) #503


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
