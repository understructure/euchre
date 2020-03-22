import pytest

from euchre.team import Team
from euchre.game import Game
from euchre.hand import Hand
from euchre.deck import Deck
from euchre.player import Player
from euchre.suit import Suit


@pytest.fixture()
def hand_fixture():
    deck = Deck()
    p1 = player_fixture(0)
    p2 = player_fixture(1)
    p3 = player_fixture(2)
    p4 = player_fixture(3)
    return Hand(players=[p1, p2, p3, p4], deal_style=[3, 2, 3, 2], deck=deck)


@pytest.fixture()
def random_game_start():
    p1 = Player(name="Maashu", player_id=1)
    p2 = Player(name="Nancy", player_id=2)
    p3 = Player(name="Orin", player_id=3)
    p4 = Player(name="Penelope", player_id=4)

    t1 = Team(players=[p1, p3])
    t2 = Team(players=[p2, p4])

    g = Game(teams=[t1, t2], points_to_win=10)
    return g


def player_fixture(player_id):
    player = Player(name="Player {}".format(id), player_id=player_id)
    return player


@pytest.fixture()
def suit_fixture():
    suit = Suit()
    return suit
