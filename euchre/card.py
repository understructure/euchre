"""
Playing card (duh)
"""
from euchre.suit import Suit
from euchre.rank import Rank

_s = Suit()
_r = Rank()


class Card:
    def __init__(self, card_rank, card_suit):
        self.rank = str(card_rank)
        self.suit = card_suit
        self.suit_symbol = _s.symbols[card_suit]
        self.suit_name = _s.names[card_suit]
        self.rank_name = _r.names[self.rank]

    def __str__(self):
        return self.rank_name + " of " + self.suit_name

    def __repr__(self):
        return self.rank + self.suit_symbol

    def __eq__(self, other):
        return self.__repr__() == other.__repr__()
