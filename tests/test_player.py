import pytest

from euchre.card import Card
from euchre.player import Player
from euchre.team import Team


def test_create_player():
    t1 = Team(id=1)
    p1 = Player(name="Monkeyboy", player_id=1, team=t1)
    assert p1.id == 1
    assert p1.name == "Monkeyboy"
    t2 = Team(id=2)
    p2 = Player(name="Yoyo", player_id=99, team=t2)
    assert p2.name == "Yoyo"
    assert p2.id == 99
    assert p1.cards == []


@pytest.mark.xfail(raises=ValueError)
def test_remove_card_empty_hand_throws_error(player_fixture):
    p1 = player_fixture
    assert p1.cards == []
    c = Card("10", "D")
    p1.remove_card(card=c)


def test_get_playable_cards_has_trump(player_fixture):
    p1 = player_fixture
    p1.cards = [Card("A", "S"), Card("Q", "D"), Card("J", "D"), Card("9", "H")]
    led_card = Card("A", "H")
    trump = "H"
    playable = p1.get_playable_cards(led_card, trump)
    assert len(playable) == 2
    print("Playable cards: {}".format(", ".join([repr(x) for x in playable])))


def test_get_playable_cards_no_trump(player_fixture):
    p1 = player_fixture
    p1.cards = [Card("A", "S"), Card("Q", "D"), Card("J", "S")]
    led_card = Card("A", "H")
    trump = "C"
    playable = p1.get_playable_cards(led_card, trump)
    assert len(playable) == 3
    print("Playable cards: {}".format(", ".join([repr(x) for x in playable])))


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
