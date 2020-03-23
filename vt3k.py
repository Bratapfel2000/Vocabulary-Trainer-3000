"""
Version vt3_0014
Python 3.8
"""

import cdw
import random

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
    fields = cdw.fields_w_four_vals('new.csv')
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

    def __add__(self, other):
        t_merged = ["Cards merged::::"]
        return Deck(karteikasten = self.karteikasten + other.karteikasten)
            
    def creator(self,number_cards=3): #for all cards
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
    
#only for testing. Will be replaced with pyqt5 or similar layout
def training_programm(amount_cards):
    deck = Deck()
##    amount_cards += 1 #because of card 0 is language def
    deck.creator() #creates all cards
    session = Session()
    deck.move_cards(session, amount_cards)
    print(session)
##    print(amount_cards)
##    print(deck)
    deck_neu = deck + session
    check_card = session
##    if amount_cards == 1:
##        k = 1
##    else:
##        k = random.randint(1,amount_cards-1) #karteikasten[n+1] not included
    k = random.randint(1,amount_cards-1) #karteikasten[n+1] not included
    print('')
    print("initialize training programm.....")
    print('')
    language1 = deck.fields[0][0]
    language2 = deck.fields[0][1]
    word_lang1 = check_card.karteikasten[k].lang1
    word_lang2 = check_card.karteikasten[k].lang2
    z = input("what is '"+word_lang1+"' in "+language2+"? :")
    if z == word_lang2:
        check_card.karteikasten[k].valcorrect += 1
        print("True!!")
    else:
        check_card.karteikasten[k].valwrong += 1
        print("Not True!!!")
    for card in deck_neu.karteikasten:
        print(card)
    #just for testing. Might drop out soon or be changed.
    save_option = input("Save results?")
    if save_option == "y":
        print(" + + + deck + + + ")
        print(deck)
        print(" + + + session + + + ")
        print(session)
        print(" + + + Deck Neu + + + ")
        print(deck_neu)
        print(" + + +  + + + ")
        #works. But retry will not refresh csv file. But when saving and ending, and starting
        #the new numbers are in.  So it works, but might load the csv in the cache or so...
        cdw.csv_exporter_3(deck_neu.dict_returner(), 'new')
        for card in deck_neu.karteikasten:
            print(card)
        print("Will be saved")
    elif save_option == "n":
        print("won't be saved")
    else:
        print("wrong inputs")
    again = str(input("Try again?"))
    if again == 'y':
        training_programm_with_objects(int(input("amount_cards=")))
    else:
        print("Ok, then not...")
        
def print_attributes(obj):
    for attr in vars(obj):
        print(attr, getattr(obj, attr))

if __name__ == "__main__":

    training_programm(int(input("amount_cards=")))
