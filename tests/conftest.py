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
    t1 = Team(1)
    t2 = Team(2)
    p1 = Player(name="Player 0", player_id=0, team=t1)
    p2 = Player(name="Player 1", player_id=1, team=t2)
    p3 = Player(name="Player 2", player_id=2, team=t1)
    p4 = Player(name="Player 3", player_id=3, team=t2)
    t1 = [p1, p3]
    t2 = [p2, p4]
    return Hand(players=[p1, p2, p3, p4], teams=[t1, t2], deal_style=[3, 2, 3, 2], deck=deck)


@pytest.fixture()
def random_game_start():
    t1 = Team(1)
    t2 = Team(2)
    p1 = Player(name="Maashu", player_id=0, team=t1)
    p2 = Player(name="Nancy", player_id=1, team=t2)
    p3 = Player(name="Orin", player_id=2, team=t1)
    p4 = Player(name="Penelope", player_id=3, team=t2)

    g = Game(players=[p1, p2, p3, p4], points_to_win=10)
    return g


@pytest.fixture()
def player_fixture(player_id=99):
    t1 = Team(1)
    player = Player(name="Player {}".format(player_id), player_id=player_id, team=t1)
    return player


@pytest.fixture()
def suit_fixture():
    suit = Suit()
    return suit


# Game has players
# players have cards
# game has hands
# hands have tricks
# hand = 5 tricks
# Player playing card = remove card from hand, add card to trick

# Game state:
    # Dealer
    # teams
    # who's turn
    # hand original dealer
    # trick current dealer
    # Trump
    # current hand
    # hand status (active vs. over)
    # score