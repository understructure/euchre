"""
I hold information for card suit names and symbols.
TODO: Implement Joker here?
"""


class Suit:
    def __init__(self):
        self.names = {"S": "Spades", "D": "Diamonds", "H": "Hearts", "C": "Clubs"}
        self.symbols = {"H": "♥", "D": "♦", "C": "♣", "S": "♠"}
        self.d_bower_suits = {'S': 'C', 'C': 'S', 'D': 'H', 'H': 'D', None: None}

    def effective_suit(self, card, trump):
        if card.suit == self.d_bower_suits[trump] and card.rank == "J":
            return trump
        else:
            return card.suit
