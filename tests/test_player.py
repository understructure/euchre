import pytest

from euchre.card import Card
from euchre.player import Player


def test_create_player():
    p1 = Player(name="Monkeyboy", player_id=1)
    assert p1.id == 1
    assert p1.name == "Monkeyboy"
    p2 = Player(name="Yoyo", player_id=99)
    assert p2.name == "Yoyo"
    assert p2.id == 99
    assert p1.cards == []


@pytest.mark.xfail(raises=ValueError)
def test_remove_card_empty_hand_throws_error(player_fixture):
    p1 = player_fixture
    assert p1.cards == []
    c = Card("10", "D")
    p1.remove_card(card=c)


def test_bid_action():
    pass


def test_call_it_up():
    pass


def test_dealer_call_it():
    pass


def test_screw_the_dealer():
    pass


def test_screwed_call_it():
    pass
