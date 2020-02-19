import random as rand


class Game:
    """
    Sets up a simplified dealer vs player blackjack game.
    As soon as the player hits 21, they win.
    """

    def __init__(self):
        self.deck = Deck()
        self.dealer = Player('Dealer')
        player_name = input("Enter the player's name: ")
        self.player = Player(f' {player_name} ')
        self.stop = False
        self.winner = []

        self.start_game()

    def deal_to(self, player):
        player.add_to_hand(self.deck.deal())

    def print_table(self):
        dealer = self.dealer
        player = self.player

        def center(value):
            return str(value).center(28)
        print(f"""
{'='*60}
|{center(dealer)}||{center(player)}|
|{center(dealer.hand)}||{center(player.hand)}|
|{center(dealer.hand_value())}||{center(player.hand_value())}|
{'='*60}""")

    def start_game(self):
        self.dealer.add_to_hand(self.deck.deal())
        self.player.add_to_hand(self.deck.deal())
        self.player.add_to_hand(self.deck.deal())
        self.print_table()
        self.update()

    def player_action(self):
        while self.player.hand_value() < 21:
            action = input("Hit or stay? ")
            if action == 'hit':
                self.deal_to(self.player)
                self.print_table()
            elif action == 'stay':
                break
        if self.player.hand_value() == 21:
            self.winner = self.player
            self.stop = True
        elif self.player.hand_value() > 21:
            self.winner = self.dealer
            self.stop = True

    def dealer_action(self):
        if self.player.hand_value() >= 21:
            return
        else:
            while self.dealer.hand_value() <= self.player.hand_value() and self.dealer.hand_value() < 21:
                self.deal_to(self.dealer)
                self.print_table()
        if self.dealer.hand_value() > 21:
            self.winner = self.player
            self.stop = True

    def update(self):
        self.player_action()
        self.dealer_action()
        while not self.stop:
            self.player_action()
            self.dealer_action()
        print(f"""
The winner is {str(self.winner)}
""")


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    pretty_suits = {
        'S': '\u2664',
        'C': '\u2667',
        'H': '\u2661',
        'D': '\u2662'
    }

    def __str__(self):
        return f"{self.rank} {Card.pretty_suits[self.suit]}"

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
    """
    Stores a deck of cards, deals cards, and keeps track of what cards are left
    """

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


class Player:
    def __init__(self, name):
        self.hand = []
        self.name = name
        # self.name = "Player" +input("Enter the player's name? ")

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def add_to_hand(self, card):
        self.hand.append(card)

    def hand_value(self):
        value = sum([card.value() for card in self.hand])
        ace_in_hand = [card.rank == 'A' for card in self.hand]
        if True in ace_in_hand and value >21:
            return value - 10
        else:
            return value


if __name__ == '__main__':
    Game()
