"""
Version vt3_0015
Python 3.8
"""

import cdw
import random

class Card:
    """creates a Vocabulary Card with a word in Language1 and Language 2 (label),
    valcorrect/valwrong tells how often the word was guessed right or wrong"""
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
class Deck:
    """Creates a box with Vocabulary cards"""
    fields = cdw.fields_w_four_vals('new.csv')  #load csv file with words.
                                                #2 additional vals for right/wrong guess
    def __init__(self, karteikasten=None):      #creates list with (vocabulary) Card objects
        if karteikasten == None:
            karteikasten =  []
        self.karteikasten = karteikasten
    def __str__(self):                          #print out cards
        t = ["Cards available:"]
        for obj in self.karteikasten:
            s = object.__str__(str(obj.label)+": "+obj.lang1+" - "+obj.lang2)
            t.append(s)        
        return '\n'.join(t)

    def __add__(self, other):                   #merge 2 Deck's
        t_merged = ["Decks merged:"]
        return Deck(karteikasten = self.karteikasten + other.karteikasten)
            
    def creator(self):  #creates Deck with all available Dards
        for i in range(1,len(Deck.fields)):  #Deck.fields[0] with Language not a card  
            card = Card("Karte "+str(i),
                        Deck.fields[i][0],
                        Deck.fields[i][1],
                        int(Deck.fields[i][2]),
                        int(Deck.fields[i][3]))
            self.karteikasten.append(card)

    def dict_returner(self):    #creates a histogram with the cards for later export
        dict_ex = {}            #export could happen to save right/wrong answers
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
        """Adds a card to the Deck. """
        self.karteikasten.append(card)
        
    def move_cards(self, hand, card_amount):
        """ takes a card from Deck and puts it in another one"""
        for i in range(card_amount):
            hand.add_card(self.pop_card())

    def pop_card(self):
        return self.karteikasten.pop(-1)

    def shuffle_deck(self):
        random.shuffle(self.karteikasten)
        
class Session(Deck):
    """Take a part of all available Cards from Deck and put it in other box for training"""
    def __init__(self, karteikasten=None):
        if karteikasten == None:
            karteikasten =  []
        self.karteikasten = karteikasten
    def __str__(self):
        t = ["Cards available:"]
        for obj in self.karteikasten:
            s = object.__str__(str(obj.label)+": "+obj.lang1+" - "+obj.lang2)
            t.append(s)        
        return '\n'.join(t)
    
def training_initialize():
    """Interface for testing, will be replaced with PyQt5"""
    deck = Deck()
    deck.creator() #creates Deck with all Voc. Cards
    amount_cards = int(input("Enter amount of random Cards for Test (max.="+
                             str(len(deck.karteikasten))+"):"))
    amount_rounds = int(input("Enter amount of rounds for Test:"))
    session = Session() 
    deck.move_cards(session, amount_cards)  #creates Box with requested amount of cards
    for o in range(amount_rounds):          #how many times you want to try
        if len(session.karteikasten)==0:
            print("No More Cards in Box. Good job!")
            return ende()
        training_programm_with_objects(amount_cards,session,deck)

def training_programm_with_objects(amount_cards,session,deck):
    """Also only for testing"""
    print("")
    print("In this session there are following ",session)
    print("")
    deck_neu = deck + session
    check_card = session
    k = random.randint(0,len(check_card.karteikasten)) #karteikasten[n+1] not included
    print('')
    print("initialize training programm.....")
    print('')
    language1 = deck.fields[0][0]
    language2 = deck.fields[0][1]
    word_lang1 = check_card.karteikasten[k-1].lang1
    word_lang2 = check_card.karteikasten[k-1].lang2
    z = input("what is '"+word_lang1+"' in "+language2+"? :")
    if z == word_lang2:
        check_card.karteikasten[k-1].valcorrect += 1  #Correct value +1 in Card
        check_card.karteikasten.pop(k-1) #if answer correct, card will be taken out
    else:
        check_card.karteikasten[k-1].valwrong += 1  #Wrong value +1 in Card
    
def print_cards(deck,session,deck_neu):
    """For testing reasons in menu"""
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
    """will save cards for later use. right/wrong values included"""
    save_option = input("Save results?")
    if save_option == "y":
        cdw.csv_exporter_3(deck_1.dict_returner(), 'new')
        for card in deck_1.karteikasten:
            print(card)
        print("Will be saved")
    elif save_option == "n":
        print("won't be saved")
    else:
        print("wrong inputs")

def try_again():
    """retry option in menu"""
    again = str(input("Try again?"))
    if again == 'y':
        training_programm_with_objects(int(input("amount_cards=")))
    else:
        print("Ok, then not...")
        
def ende():
    print("This is the end")

def print_attributes(obj):
    for attr in vars(obj):
        print(attr, getattr(obj, attr))

if __name__ == "__main__":
    training_initialize()
