import pytest

from euchre.suit import Suit


def test_hand(hand_fixture):
    hand_fixture.deal()
    assert hand_fixture.top_card not in hand_fixture.deck.cards
    dealt_cards = flatten_list(hand_fixture.hands.values())
    assert hand_fixture.top_card not in dealt_cards
    # assert sorted(list(set(dealt_cards))) == sorted(list(dealt_cards))


@pytest.mark.xfail(throws=ValueError)
def test_set_trump(hand_fixture):
    hand_fixture.set_trump(suit="X")


# @pytest.mark.paramaterize("suit",[])

def test_set_trump(hand_fixture, suit_fixture):
    suit = Suit()
    for sx in list(suit.names.keys()):
        hand_fixture.set_trump(suit=sx)


def flatten_list(the_list):
    return [item for sublist in the_list for item in sublist]
