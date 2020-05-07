import cdw
import random
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QLineEdit, QWidget, QHBoxLayout, QLabel, QMessageBox
import sys
from PyQt5.QtCore import QRect

class Card:
    def __init__(self, label='noName', lang1="-", lang2="-", valcorrect=0, valwrong=0):
        self.label = label
        self.lang1 = lang1
        self.lang2 = lang2
        self.valcorrect = valcorrect
        self.valwrong = valwrong

    def __str__(self):
        return '%s - %s - %s %s %s' % (self.label,
                                  self.lang1,
                                  self.lang2,
                                  self.valcorrect,
                                  self.valwrong)
##class Deck(Card):
class Deck:
    """take x cards to check"""
    fields = cdw.fields_w_four_vals('words.csv')
    def __init__(self, karteikasten=None):
        if karteikasten == None:
            karteikasten =  []
        self.karteikasten = karteikasten
    def __str__(self):
        t = ["Cards available...:"+str(len(self.karteikasten))]
        for obj in self.karteikasten:
            s = object.__str__(str(obj.label)+": "+obj.lang1+" - "+obj.lang2)
            t.append(s)        
        return '\n'.join(t)

    def __add__(self, other):
        t_merged = ["Cards merged::::"]
        return Deck(karteikasten = self.karteikasten + other.karteikasten)

    #dcr34t0r
    def creator(self,number_cards=4): #for all cards  (number_cards=4 is obsolete..)
        for i in range(1,len(Deck.fields)):  #De-En should not be a card  
            card = Card("Karte "+str(i),
                        Deck.fields[i][0],
                        Deck.fields[i][1],
                        int(Deck.fields[i][2]),
                        int(Deck.fields[i][3]))
            self.karteikasten.append(card)

    def dict_returner(self):#creates a dictionary with the cards for later export
        dict_ex = {}
        dict_ex[0] = [Deck.fields[0][0],
                        Deck.fields[0][1],
                        int(Deck.fields[0][2]),
                        int(Deck.fields[0][3])]
        for i in range(1,len(self.karteikasten)+1):
            dict_ex[i] = [self.karteikasten[i-1].lang1,
                      self.karteikasten[i-1].lang2,
                      self.karteikasten[i-1].valcorrect,
                      self.karteikasten[i-1].valwrong]
        return dict_ex

    def add_card(self, card):
        """Adds a card to the deck. """
        self.karteikasten.append(card)
        
    def move_cards(self, hand, card_amount):
        for i in range(card_amount):
            hand.add_card(self.pop_card())

    def pop_card(self):
        return self.karteikasten.pop(-1)

    def shuffle_deck(self):
        random.shuffle(self.karteikasten)
        
class Session(Deck):
    """ session with only a part of the box"""
    def __init__(self, karteikasten=None,all_rights=0,all_wrongs=0):
        self.all_rights = all_rights
        self.all_wrongs = all_wrongs
        if karteikasten == None:
            karteikasten =  []
        self.karteikasten = karteikasten
    def __str__(self):
        t = ["Cards available:"+str(len(self.karteikasten))]
        for obj in self.karteikasten:
            s = object.__str__(str(obj.label)+": "+obj.lang1+" - "+obj.lang2)
            t.append(s)        
        return '\n'.join(t)

def training_initialize():
    deck = Deck()
    deck.creator() #creates all cards
    amount_cards = int(input("amount_cards="))
    session = Session()
    deck.move_cards(session, amount_cards)

    for o in range(10):
        if len(session.karteikasten)==0:
            print("No Cards in Box")
            return ende()
        training_programm_with_objects(amount_cards,session,deck)


""" check if all objects fit in """  
def training_programm_with_objects(amount_cards,session,deck):
##    amount_cards += 1 #because of card 0 is language def
    print(session.karteikasten)
    for card in range(len(session.karteikasten)):
        print(card)

    print("In this session there are following ",session)
    deck_neu = deck + session
    check_card = session

    if len(check_card.karteikasten)==0:
        print("No Cards in Box")
        return ende()
    k = random.randint(0,len(check_card.karteikasten)) #karteikasten[n+1] not included
    print('>>>>>  k=',k,'amount cards=',len(check_card.karteikasten))
    print('')
    print("initialize training programm.....")
    print('')
    language1 = deck.fields[0][0]
    language2 = deck.fields[0][1]
    word_lang1 = check_card.karteikasten[k-1].lang1
    word_lang2 = check_card.karteikasten[k-1].lang2
    z = input("what is '"+word_lang1+"' in "+language2+"? :")
    if z == word_lang2:
        check_card.karteikasten[k-1].valcorrect += 1
        check_card.karteikasten.pop(k-1) #if answer correct, card will be taken out
        print("True!!")
    else:
        check_card.karteikasten[k-1].valwrong += 1
        print("Not True!!!")
    
def print_cards(deck,session,deck_neu):
    print("")
    print(" + + + whole deck + + + ")
    print(deck)

    print("")
    print(" + + + This session:",20*" +")
    print(session)

    print("")
    print(" + + + Deck Neu (Total Deck+ + + ")
    print(deck_neu)
    
    print(" + + + All Cards with Results + + + ")
    for card in deck_neu.karteikasten:
        print(card)
    

def save_option(deck_1):
    save_option = input("Save results?")
    if save_option == "y":
        #works. But retry will not refresh csv file. But when saving and ending, and starting
        #the new numbers are in.  So it works, but might load the csv in the cache or so...
        cdw.csv_exporter_3(deck_1.dict_returner(), 'new')
        for card in deck_1.karteikasten:
            print(card)
        print("Will be saved")
    elif save_option == "n":
        print("won't be saved")
    else:
        print("wrong inputs")

def try_again():
    again = str(input("Try again?"))
    if again == 'y':
        training_programm_with_objects(int(input("amount_cards=")))
    else:
        print("Ok, then not...")
        
def ende():
    print("This is the end")
    
def trainer():
    checkwords = input(card.lang1)

def print_attributes(obj):
    for attr in vars(obj):
        print(attr, getattr(obj, attr))

class Ui_MainWindow(Session,Deck):
    def __init__(self,message=3,message_g2=1):               #644_g2_t_g3ie
        self.message = message                       #644_g2_t_g3ie
        session = Session()
        self.deck.move_cards(self.session, int(message))
        self.message_g2 = message_g2 #imported from g2_screen and it got it from second_screen
    deck = Deck()
    deck.creator(4) #creates all cards   #dcr34t0r
    session = Session()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        #lineedit
        #answerbox
        height_lineedit = 20
        hbox =QHBoxLayout()
        self.lineedit = QLineEdit(self.centralwidget)
        self.lineedit.hide()
        self.lineedit.setFont(QtGui.QFont("Sanserif",15))
        self.lineedit.setGeometry(QtCore.QRect(20, 200, 200, 50))
        self.lineedit.returnPressed.connect(self.onPressed)

        hbox.addWidget(self.lineedit)

        #label_lineedit
        #truefalsebox
        heigth_label_lineedit = 20
        self.label_lineedit = QtWidgets.QLabel(self.centralwidget)
        self.label_lineedit.hide()
        self.label_lineedit.setGeometry(QtCore.QRect(400, 200, 300, 50))
        self.label_lineedit.setObjectName("label_lineedit")
        self.label_lineedit.setFont(QtGui.QFont("Sanserif",15))
        self.label_lineedit.setStyleSheet("background-color: yellow")

        #header
        heigth_header = 75
        self.label_header = QtWidgets.QLabel(self.centralwidget)
        self.label_header.setGeometry(QtCore.QRect(50, heigth_header, 111, 51))
        self.label_header.setObjectName("label")

        #000out
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.hide()
        self.pushButton.setGeometry(QtCore.QRect(250, 200, 140, 50))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.onPressed)

        self.pushButton.clicked.connect(self.pressed_3)
        self.lineedit.returnPressed.connect(self.pressed_3)
     
        height_pushButton_newword3  = 450
        self.pushButton_newword3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_newword3.clicked.connect(self.pressed_3)
        self.pushButton_newword3.setGeometry(QtCore.QRect(200, 250, 200, 50))

        self.label_pushButton_newword3 = QtWidgets.QLabel(self.centralwidget)
        self.label_pushButton_newword3.setGeometry(QtCore.QRect(50, 150, 500, 50))
        self.label_pushButton_newword3.setFont(QtGui.QFont("Sanserif",15))

        self.label_pushButton_newword33 = QtWidgets.QLabel(self.centralwidget)
        self.label_pushButton_newword33.hide()
        self.label_pushButton_newword33.setGeometry(QtCore.QRect(50, 300, 300, 51))
        self.label_pushButton_newword33.setFont(QtGui.QFont("Sanserif",15))
        self.label_pushButton_newword33.setStyleSheet("background-color: red")

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
        MainWindow.setWindowTitle(_translate("MainWindow", "Vokabeltrainer 3000 - Feel The Words"))
        self.label_header.setText(_translate("MainWindow", "Vokabeltrainer 3000"))

        self.label_lineedit.setText(_translate("MainWindow", "Heelo! #h41"))

        #5263a
        #whatisfield
        #644_g2_t_g3ie
        self.label_pushButton_newword3.setText(_translate("MainWindow", str(self.message)+" words in box"))
        self.label_pushButton_newword33.setText(_translate("MainWindow", "H#5263b"))

        testword = Ui_MainWindow.session.fields[0][0]

        self.pushButton.setText(_translate("MainWindow", "Check!"))
        self.pushButton_newword3.setText(_translate("MainWindow", "Start")) 
           
    def closescr(self, MainWindow):
        MainWindow.hide()

        
    def onPressed(self):
        self.label_pushButton_newword33.hide()
        if int(len(self.session.karteikasten)) == 0:
            self.show_popup()
        if self.message_g2 == 1:
            word_lang1 = Ui_MainWindow.session.karteikasten[0].lang1
            word_lang2 = Ui_MainWindow.session.karteikasten[0].lang2
        elif self.message_g2 == 0:
            word_lang2 = Ui_MainWindow.session.karteikasten[0].lang1
            word_lang1 = Ui_MainWindow.session.karteikasten[0].lang2
        else:
            print("Some error might have occured... ")

        if self.lineedit.text() == word_lang1:
            self.label_lineedit.setText("True!")
            self.label_lineedit.setStyleSheet("background-color: green")
            self.label_lineedit.show()
            self.lineedit.clear()
            Ui_MainWindow.session.karteikasten.pop(0)
            Ui_MainWindow.session.all_rights += 1
        else:
            self.label_lineedit.setText("False! It is '"+word_lang1+"'")
            self.label_lineedit.setStyleSheet("background-color: red")
            self.label_lineedit.show()
            self.lineedit.clear()
            Ui_MainWindow.session.karteikasten.pop(0)
            Ui_MainWindow.session.all_wrongs += 1

    #Startbutton
    def pressed_3(self):
        if int(len(self.session.karteikasten)) == 0:
            self.show_popup()
            return 0

        check_card = Ui_MainWindow.session
        check_card.shuffle_deck()

        if self.message_g2 == 1:
            word_lang1 = Ui_MainWindow.session.karteikasten[0].lang1
            word_lang2 = Ui_MainWindow.session.karteikasten[0].lang2
            request_lang = Ui_MainWindow.session.fields[0][0]
        elif self.message_g2 == 0:
            word_lang2 = Ui_MainWindow.session.karteikasten[0].lang1
            word_lang1 = Ui_MainWindow.session.karteikasten[0].lang2
            request_lang = Ui_MainWindow.session.fields[0][1]
        else:
            print("Some error might have occured... ")
            
        self.label_pushButton_newword3.setText("What is '" +word_lang2+"' in "+ request_lang+"?   ("+str(len(self.session.karteikasten)-1)+" words left)")
        self.label_pushButton_newword33.setText(word_lang1 +" = " +word_lang2+str(len(Ui_MainWindow.session.karteikasten)))
        self.pushButton_newword3.hide()  #when starting, start button dissapears and field shows up
        #but actually we need it to swap for next word...
        self.lineedit.show()
        self.pushButton.show()
        
    def pressed_2(self):
        fields = {0: ['bust', 'sprengen', 0, 0],
                 1: ['bold', 'kuehn', 0, 0],
                 2: ['to become apostate', 'abtruennig werden', 0, 0],
                 3: ['paste', 'kleister', 0, 0]}

        randnum = random.randint(0,3)
        
    def show_popup(self):
        msg = QMessageBox()
        msg.setWindowTitle("Results")
        msg.setText("wrong:"+str(self.session.all_wrongs)+"-right:"+str(self.session.all_rights))
        x = msg.exec()

"""
#can stay for testing. needs to be taken out when called from g2_screen
if __name__ == "__main__":
    import sys
    print("#1")
    app = QtWidgets.QApplication(sys.argv)
    print("#2")
    MainWindow = QtWidgets.QMainWindow()
    print("#3")
    ui = Ui_MainWindow()
    print("#4")
##    ui.training_initialize()
    ui.setupUi(MainWindow)
    print("#5")
    MainWindow.show()
    print("#6")
    sys.exit(app.exec_())
    print("#7")
"""
