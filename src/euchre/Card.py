"""
Playing card (duh)
"""


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        rank_names = {"7": "Seven", "8": "Eight", "9": "Nine", "10": "Ten",
                     "J": "Jack", "Q": "Queen", "K": "King", "A": "Ace"}
        suit_names = {"S": "Spades", "D": "Diamonds", "H": "Hearts", "C": "Clubs"}
        return rank_names[self.rank] + " of " + suit_names[self.suit]