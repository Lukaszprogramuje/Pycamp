from random import shuffle

class Card:
    """klasa odpowiedzialna za właściwości pojedynczej karty"""
    colors = ["clubs", "diamods", "hearts", "spades"]
    names = ["A", "J", "D", "K", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    value = {"A":11, "J":10, "D":10, "K":10, "2":2, "3":3,
     "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10}
    second_value = {"A":1, "J":10, "D":10, "K":10, "2":2, "3":3,
     "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10}
    def __init__(self, name, color):
        self.name = name
        self.color = color

class Deck:
    """klasa odpowiedzialna za talię kart używaną do gry"""
    def __init__(self):
        self.deck = []

    def add_deck(self):
        """dodaje talię do gry"""
        for color in Card.colors:
            for name in Card.names:
                # print(f" {color}  {name}")
                self.deck.append(Card(name = name, color = color))

    def shufle(self):
        """tasuje karty"""
        shuffle(self.deck)

    def print_deck(self):
        """wyswietla karty w talii"""
        for i in self.deck:
            print(f" {i.name}   {i.color} ")

    def get_card(self):
        """pobiera jedną kartę"""
        return self.deck.pop(-1)

    def check_deck(self):
        """sprawdza czy talia posiada min 10 kart, jeżeli nie to dodaje kolejną talię i ją tasuje"""
        if (len(self.deck)) < 10:
            print("za malo kart w talii, dotasowuje kolejna talie")
            self.add_deck()
            self.shufle()

class Hand:
    """klasa odpowiedzialna za karty na ręku"""
    def __init__(self):
        self.hand = []

    def check_value(self):
        """metoda sprawdzająca wartość kart"""
        points = 0                               #dla A = 11
        second_points = 0                        #dla A = 1
        if len(self.hand) == 2 and (self.hand[0].name == "A" and self.hand[1].name == "A"):
            points = 21
        else:
            for i in self.hand:
                points += Card.value[i.name]
                second_points += Card.second_value[i.name]
        #decyzja co lepsze dla gracza
        if points <= 21:
            return points
        return second_points

    def check_cards(self):
        """metoda pokazująca posiadane karty"""
        for i in self.hand:
            print(f" {i.name}   {i.color} ")

class Player(Hand):
    """klasa gracz dziedziczy po klasie Hand"""
    def __init__(self):
        super().__init__()

class Croupier(Hand):
    """klasa krupier dziedziczy po klasie"""
    def __init__(self):
        super().__init__()

talia = Deck()
player = Player()
croupier = Croupier()

talia.add_deck()
talia.check_deck()
talia.shufle()

def game():
    """główna funkcja gry, 1 runda, ruchy gracza a następnie krupiera"""
    #rozdanie początkowe
    croupier.hand.append(talia.get_card())
    player.hand.append(talia.get_card())
    croupier.hand.append(talia.get_card())
    player.hand.append(talia.get_card())

    while True:
        print(player.check_value())
        player.check_cards()
        if player.check_value() <= 21:
            players_decision = input("czy chcesz dobierac dalej TAK/NIE ").lower()
            if players_decision == "tak":
                player.hand.append(talia.get_card())
            else:
                break
        else:
            print(player.check_value())
            print("przekroczyles 21, przegrywasz")
            break

    print()
    if player.check_value() <= 21:
        print("tura krupiera")
        while croupier.check_value() < 17:
            croupier.check_cards()
            print(croupier.check_value())
            croupier.hand.append(talia.get_card())
        if croupier.check_value() > 21:
            print("krupier przekroczyl 21, gracz wygrywa")

    print()
    print("krupier posiada")
    croupier.check_cards()
    print(croupier.check_value())
    print()
    print("gracz posiada")
    player.check_cards()
    print(player.check_value())

    if player.check_value() <= 21 and croupier.check_value() <= 21:
        if player.check_value() == croupier.check_value():
            print("remis")
        elif player.check_value() < croupier.check_value():
            print("gracz przegrywa")
        else:
            print("gracz wygrywa")

game()
