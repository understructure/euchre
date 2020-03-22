from euchre.deck import Deck
from euchre.card import Card


def test_get_card_ranks_by_trump_and_led():
    d = Deck(low_rank="9")
    card = Card("A", "S")
    rez = d.get_card_ranks_by_trump_and_led("S", card)
    assert [repr(x) for x in rez] == ["J♠", "J♣", "A♠", "K♠", "Q♠", "10♠", "9♠"]

    # when non-bower suit is led, J should be in the rankings
    # for the non-trump and non-bower suit

    card = Card("A", "D")
    rez = d.get_card_ranks_by_trump_and_led("S", card)
    assert [repr(x) for x in rez] == ["J♠", "J♣", "A♠", "K♠", "Q♠", "10♠", "9♠",
                   "A♦", "K♦", "Q♦","J♦", "10♦", "9♦"]

    card = Card("A", "H")
    rez = d.get_card_ranks_by_trump_and_led("S", card)
    assert [repr(x) for x in rez] == ["J♠", "J♣", "A♠", "K♠", "Q♠", "10♠", "9♠",
                   "A♥", "K♥", "Q♥", "J♥", "10♥", "9♥"]

    card = Card("A", "C")
    rez = d.get_card_ranks_by_trump_and_led("S", card)
    assert [repr(x) for x in rez] == ["J♠", "J♣", "A♠", "K♠", "Q♠", "10♠", "9♠",
                   "A♣", "K♣", "Q♣", "10♣", "9♣"]

# @pytest.mark.parametrize(
#     "test_input,expected", [(9, 24), (8, 28), (7, 32),
#                             pytest.param(10, None, marks=pytest.mark.xfail())]
# )
# def test_deck_differing_low_ranks(test_input, expected):
#     test_deck = Deck(low_rank=test_input)
#     assert len(test_deck.cards) == expected
#
#
# def test_get_non_bower_ranks():
#     test_deck = Deck()
#     non_bowers = test_deck.get_non_bower_ranks()
#     assert 'J' not in non_bowers
#
#
# @pytest.mark.parametrize(
#     "the_trump,the_led_suit,expected", [("S", "S",
#                                          [("J", "S"), ("J", "C"),
#                                           ("A", "S"), ("K", "S"),
#                                           ("Q", "S"), ("10", "S"),
#                                           ("9", "S")])]
# )
# def test_get_card_ranks_by_trump_and_led(the_trump, the_led_suit, expected):
#     test_deck = Deck()
#     ranked_cards = test_deck.get_card_ranks_by_trump_and_led(trump=the_trump, led_suit=the_led_suit)
#     print(ranked_cards)
#     # assert ranked_cards == expected
#     assert len(ranked_cards) == 7
