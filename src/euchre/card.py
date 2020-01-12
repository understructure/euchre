"""
Playing card (duh)
"""


class Card:
    def __init__(self, rank, suit):
        self.rank_names = {"7": "Seven", "8": "Eight", "9": "Nine", "10": "Ten",
                      "J": "Jack", "Q": "Queen", "K": "King", "A": "Ace"}
        self.suit_names = {"S": "Spades", "D": "Diamonds", "H": "Hearts", "C": "Clubs"}
        self.suit_symbols = {"H": "♥", "D": "♦", "C": "♣", "S": "♠"}
        self.rank = rank
        self.suit = suit
        self.symbol = suit_symbols[suit]

    def __repr__(self):
        return rank_names[self.rank] + " of " + suit_names[self.suit]

    def __str__(self):
        return self.rank + self.symbol


# class CardHandTrick(Card):
#     def __init__(self, card, hand, trick):
#         trick.led_suit
#         hand.trump