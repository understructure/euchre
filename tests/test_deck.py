import pytest

from euchre.deck import Deck, IllegalArgumentError
from euchre.card import Card
from euchre.suit import Suit

def test_init_deck_low_rank_too_low_fail():
    with pytest.raises(IllegalArgumentError):
        d = Deck(low_rank=4)


def test_init_deck_low_rank_too_high_fail():
    with pytest.raises(IllegalArgumentError):
        d = Deck(low_rank=10)


@pytest.mark.parametrize("rank", [7, 8, 9])
@pytest.mark.parametrize("suit", ["C", "H", "D", "S"])
def test_init_deck_low_rank_ok_pass(rank, suit):
    d = Deck(low_rank=rank)
    test_card = Card(card_rank=rank, card_suit=suit)
    assert test_card in d.cards


def test_get_card_ranks_by_trump_and_led_bower_led_pass():
    low_rank = 9
    d = Deck(low_rank=low_rank)

    card = Card("J", "C")
    rez = d.get_card_ranks_by_trump_and_led("S", card)
    assert [repr(x) for x in rez] == ["J♠", "J♣", "A♠", "K♠", "Q♠", "10♠", "9♠"]

    card = Card("J", "S")
    rez = d.get_card_ranks_by_trump_and_led("C", card)
    assert [repr(x) for x in rez] == ["J♣", "J♠", "A♣", "K♣", "Q♣", "10♣", "9♣"]

    card = Card("J", "D")
    rez = d.get_card_ranks_by_trump_and_led("H", card)
    assert [repr(x) for x in rez] == ["J♥", "J♦", "A♥", "K♥", "Q♥", "10♥", "9♥"]

    card = Card("J", "H")
    rez = d.get_card_ranks_by_trump_and_led("D", card)
    assert [repr(x) for x in rez] == ["J♦", "J♥", "A♦", "K♦", "Q♦", "10♦", "9♦"]


def test_get_card_ranks_by_trump_and_led_non_bower_led_pass():
    low_rank = 9
    d = Deck(low_rank=low_rank)
    card = Card("A", "S")
    rez = d.get_card_ranks_by_trump_and_led("S", card)
    assert [repr(x) for x in rez] == ["J♠", "J♣", "A♠", "K♠", "Q♠", "10♠", "9♠"]

    # when non-bower suit is led, J should be in the rankings
    # for the non-trump and non-bower suit

    card = Card("A", "D")
    rez = d.get_card_ranks_by_trump_and_led("S", card)
    assert [repr(x) for x in rez] == ["J♠", "J♣", "A♠", "K♠", "Q♠", "10♠", "9♠",
                   "A♦", "K♦", "Q♦", "J♦", "10♦", "9♦"]

    card = Card("A", "H")
    rez = d.get_card_ranks_by_trump_and_led("S", card)
    assert [repr(x) for x in rez] == ["J♠", "J♣", "A♠", "K♠", "Q♠", "10♠", "9♠",
                   "A♥", "K♥", "Q♥", "J♥", "10♥", "9♥"]

    card = Card("A", "C")
    rez = d.get_card_ranks_by_trump_and_led("S", card)
    assert [repr(x) for x in rez] == ["J♠", "J♣", "A♠", "K♠", "Q♠", "10♠", "9♠",
                   "A♣", "K♣", "Q♣", "10♣", "9♣"]


@pytest.mark.parametrize("trump,led,symbol",
                         [("S", "C", "♣"), ("C", "S", "♠"),
                         ("D", "H", "♥"), ("H", "D", "♦")])
def test_get_non_trump_led_suit_ranks_bowers_pass(trump, led, symbol):
    d = Deck(low_rank=9)
    rez = d.get_non_trump_led_suit_ranks(trump=trump, led_suit=led)
    assert [repr(x) for x in rez] == [x + symbol for x in ["A", "K", "Q", "10", "9"]]


@pytest.mark.parametrize("trump,led,symbol",
                         [("S", "D", "♦"), ("S", "H", "♥"), ("C", "D", "♦"), ("C", "H", "♥"),
                          ("D", "C", "♣"), ("D", "S", "♠"), ("H", "C", "♣"), ("H", "S", "♠")])
def test_get_non_trump_led_suit_ranks_non_bowers_different_suits_pass(trump, led, symbol):
    d = Deck(low_rank=9)
    rez = d.get_non_trump_led_suit_ranks(trump=trump, led_suit=led)
    assert [repr(x) for x in rez] == [x + symbol for x in ["A", "K", "Q", "J", "10", "9"]]


@pytest.mark.parametrize("suit", ["C", "D", "H", "S"])
def test_get_non_trump_led_suit_ranks_non_bowers_same_suit_pass(suit):
    d = Deck(low_rank=9)
    s = Suit()
    symbol = s.symbols[suit]
    rez = d.get_non_trump_led_suit_ranks(trump=suit, led_suit=suit)
    assert [repr(x) for x in rez] == [x + symbol for x in ["A", "K", "Q", "10", "9"]]


def test_get_card_ranks_by_trump_and_led_no_trump():
    trump = None
    d = Deck(low_rank=9)
    rez = d.get_card_ranks_by_trump_and_led(trump, led_card=Card("9", "C"))
    print(rez)
