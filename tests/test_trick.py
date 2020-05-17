import pytest

from euchre.game import Game
from euchre.trick import Trick
from euchre.player import Player
from euchre.team import Team
from euchre.hand import BidException


def test_fully_played_hand_actually():
    p1 = Player("A", 1)
    p2 = Player("B", 2)
    p3 = Player("C", 3)
    p4 = Player("D", 4)

    team1 = Team([p1, p3], id=0)
    team2 = Team([p2, p4], id=1)

    teamz =[team1, team2]
    g = Game(teams=teamz, points_to_win=10)

    g.hands[-1].bid(g.hands[-1].players[0], "pass")
    g.hands[-1].bid(g.hands[-1].players[0], "pass")
    g.hands[-1].bid(g.hands[-1].players[0], "pass")
    g.hands[-1].bid(g.hands[-1].players[0], "pass")

    g.hands[-1].top_card_turned_over == True

    g.hands[-1].bid(g.hands[-1].players[0], "pass")
    g.hands[-1].bid(g.hands[-1].players[0], "pass")
    g.hands[-1].bid(g.hands[-1].players[0], "pass")

    # next one should throw screw the dealer
    with pytest.raises(BidException):
        g.hands[-1].bid(g.hands[-1].players[0], "pass")

    bid_suit = g.hands[-1].possible_trump[0]
    g.hands[-1].bid(g.hands[-1].players[0], "set_trump", bid_suit)

    assert len(g.hands[-1].tricks) == 0
    def test_trick(trick, tricks, players):
        tricks.append(trick)

        for p in players:
            trick.add_card(p.cards[0], p)

        trick.score(trump=bid_suit, deck=g.hands[-1].deck)
        print("Trick trump: {}".format(bid_suit))
        print("Trick cards: {}".format(g.hands[-1].tricks[-1].cards))
        print("Trick players: {}".format(g.hands[-1].tricks[-1].players))
        print("Trick winner ID: {}".format(g.hands[-1].tricks[-1].winner))

    for i in range(0, 5):
        trick = Trick(players=g.hands[-1].players)
        test_trick(trick, g.hands[-1].tricks, g.hands[-1].players)

    print([x.winner for x in g.hands[-1].tricks])
    g.hands[-1].score()
    print("Team {} got {} points".format(g.hands[-1].winning_team.id, g.hands[-1].winning_points))
