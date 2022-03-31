from random import shuffle

class Card: 
    colors = ["clubs", "diamods", "hearts", "spades"]        
    names = ["A", "J", "D", "K", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    def __init__(self, name, color):
        self.name = name
        self.color = color
        #self.value = value #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
                    


  #  2.  talia: posiada karty, generuje 52 karty na talie,  
  #       tasowanie talii i pobranie 1 karty lub 1 losowa karta bez tasowania
  # kolekcja obiektow typu cart
class Deck:     
    def __init__(self):
        self.deck = []

    def do_deck(self):
        for color in Card.colors:
            for name in Card.names:
                # print(f" {color}  {name}")
                self.deck.append(Card(name = name, color = color))

    def shufle(self):
        shuffle(self.deck)
    
    def print_deck(self):
        for i in self.deck:
            print(f" {i.color}  {i.name}")

talia = Deck()
talia.do_deck()
talia.shufle()
talia.print_deck()