import pytest

from euchre.card import Card
from euchre.suit import Suit
from euchre.rank import Rank

s = Suit()
r = Rank()
test_names = {"S": "Spades", "D": "Diamonds", "H": "Hearts", "C": "Clubs"}
test_symbols = {"H": "♥", "D": "♦", "C": "♣", "S": "♠"}
tes_ranks = {
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
    "10": "Ten",
    "J": "Jack",
    "Q": "Queen",
    "K": "King",
    "A": "Ace",
}


def test_card_valid_suit_pass():
    for suit in s.names.keys():
        ace = Card("A", suit)
        assert ace.__repr__() == "A{}".format(test_symbols[suit])
        assert ace.__str__() == "Ace of {}".format(test_names[suit])


@pytest.mark.xfail(raises=KeyError)
def test_card_invalid_suit_fail():
    bad = Card("A", "Q")


@pytest.mark.xfail(raises=KeyError)
def test_card_invalid_rank_fail():
    bad = Card("X", "H")
