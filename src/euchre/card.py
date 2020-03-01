"""
Playing card (duh)
"""
from euchre.suit import Suit
from euchre.rank import Rank

s = Suit()
r = Rank()


class Card:
    def __init__(self, card_rank, card_suit):
        self.rank = card_rank
        self.suit = card_suit
        self.suit_symbol = s.symbols[card_suit]
        self.suit_name = s.names[card_suit]
        self.rank_name = r.names[card_rank]

    def __str__(self):
        return self.rank_name + " of " + self.suit_name

    def __repr__(self):
        return self.rank + self.suit_symbol

    def __eq__(self, other):
        return self.__repr__() == other.__repr__()


# class CardHandTrick(Card):
#     def __init__(self, card, hand, trick):
#         trick.led_suit
#         hand.trump
