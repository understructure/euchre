import pytest
import random

from euchre.game import Game
from euchre.trick import Trick
from euchre.player import Player
from euchre.team import Team
from euchre.hand import BidException


def test_fully_played_hand_actually():
    # setup game
    team1 = Team(1)
    team2 = Team(2)
    p1 = Player("A", 1, team1)
    p2 = Player("B", 2, team2)
    p3 = Player("C", 3, team1)
    p4 = Player("D", 4, team2)

    teamz =[team1, team2]
    # game comes with empty hand
    g = Game(players=[p1, p2, p3, p4], points_to_win=10)

    while not g.is_over:
        g.new_hand()
        print("Hand number: {}".format(len(g.hands)))
        print("Scores: ")
        print(g.get_scores())
        # setup bidding - simulate screw the dealer
        the_hand = g.hands[-1]
        the_hand.bid(g.hands[-1].players[0], "pass")
        the_hand.bid(g.hands[-1].players[0], "pass")
        the_hand.bid(g.hands[-1].players[0], "pass")
        the_hand.bid(g.hands[-1].players[0], "pass")

        the_hand.top_card_turned_over = True

        the_hand.bid(g.hands[-1].players[0], "pass")
        the_hand.bid(g.hands[-1].players[0], "pass")
        the_hand.bid(g.hands[-1].players[0], "pass")

        # next one should throw screw the dealer
        with pytest.raises(BidException):
            the_hand.bid(the_hand.players[0], "pass")

        bid_suit = random.choice(g.hands[-1].possible_trump)
        the_hand.bid(the_hand.players[0], "set_trump", bid_suit)

        assert len(the_hand.tricks) == 0

        for i in range(0, 5):
            trick = Trick(hand=the_hand)
            if i > 0:
                trick.set_order_by_last_winner()
            _test_trick(trick, g)
        print("=" * 50, "Scoring trick", "=" * 50)
        the_hand.score()


def _test_trick(trick, game):
    the_hand = game.hands[-1]
    for p in the_hand.players:
        trick.add_card(p.cards[0], p)

    trick.score()
    the_hand.tricks.append(trick)
    # print("Trick trump: {}".format(bid_suit))
    print("Trick cards: {}".format(game.hands[-1].tricks[-1].cards))
    print("Trick players: {}".format(game.hands[-1].tricks[-1].players))
    print("Trick winner ID: {}".format(game.hands[-1].tricks[-1].winner))

# for i in range(0, 5):
#     trick = Trick(players=g.hands[-1].players)
#     test_trick(trick, g.hands[-1].tricks, g.hands[-1].players)
#
# # print([x.winner for x in g.hands[-1].tricks])
# g.hands[-1].score()
# print("Team {} got {} points".format(g.hands[-1].winning_team.id, g.hands[-1].winning_points))
# print(len(g.hands))
# # print([(h.winning_team.id, h.winning_points) for h in g.hands])
