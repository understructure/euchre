import pytest

from euchre.suit import Suit


def test_hand(hand_fixture):
    hfx = hand_fixture
    assert hfx.top_card not in hfx.deck.cards
    dealt_cards = flatten_list([x.cards for x in hfx.players])
    assert hfx.top_card not in dealt_cards
    assert len(dealt_cards) == len(hfx.players) * 5


@pytest.mark.xfail(throws=ValueError)
def test_set_bad_trump_fail(hand_fixture):
    hand_fixture.set_trump(suit="X")


def test_set_trump(hand_fixture, suit_fixture):
    suit = Suit()
    for sx in list(suit.names.keys()):
        if sx in hand_fixture.possible_trump:
            hand_fixture.bid(
                action="set_trump",
                player=hand_fixture.players[0],
                trump=sx,
                alone=False,
            )
            # hand_fixture.set_trump(suit=sx)
        else:
            print("Can't bid {}, not in possible trump for hand".format(sx))


def flatten_list(the_list):
    return [item for sublist in the_list for item in sublist]
