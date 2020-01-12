import pytest

from euchre.hand import Hand
from euchre.deck import Deck
from euchre.players import Player


@pytest.fixture()
def hand_fixture():
    deck = Deck()
    p1 = player_fixture(0)
    p2 = player_fixture(1)
    p3 = player_fixture(2)
    p4 = player_fixture(3)
    return Hand(dealer=2, deal_style=[3, 2, 3, 2], players=[p1, p2, p3, p4], deck=deck)


def player_fixture(player_id):
    player = Player(name="Player {}".format(id), id=player_id, team=player_id % 2, cards=[])
    return player
