import random as rand


class Game:
    def __init__(self):
        self.deck = Deck()
        self.dealer = Player()
        self.player = Player()

    def start_game():
        pass

    def update(self):
        pass


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.pretty_suits = {
            'S': '\u2664',
            'C': '\u2667',
            'H': '\u2661',
            'D': '\u2662'
        }

    def __str__(self):
        return f"{self.rank} {self.pretty_suits[self.suit]}"

    def __repr__(self):
        return str(self)

    def __add__(self, other):
        return self.value() + other.value()

    def value(self):
        if type(self.rank) == int:
            return self.rank
        elif self.rank == 'A':
            return 11
        else:
            return 10


class Deck:
    def __init__(self):
        self.number = 52
        self.pile = {}
        ranks = [i for i in range(2, 11)]+['J', 'Q', 'K', 'A']
        for suit in ['S', 'C', 'D', 'H']:
            for rank in ranks:
                self.pile[Card(rank, suit)] = 1

    def deal(self):
        item = [0, 0]
        while item[1] == 0:
            item = rand.choice(list(self.pile.items()))
        self.pile[item[0]] = 0
        self.number -= 1
        return item[0]


# class Dealer:
#     def __init__(self):
#         pass


class Player:
    def __init__(self):
        self.hand = []

    def add_to_hand(self, card):
        self.hand.append(card)

    def hand_value(self):
        return sum([card.value() for card in self.hand])


player = Player()
deck = Deck()
card1 = deck.deal()
card2 = deck.deal()
