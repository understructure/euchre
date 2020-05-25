import pytest
import random

from euchre.game import Game
from euchre.trick import Trick
from euchre.player import Player
from euchre.team import Team
from euchre.hand import BidException


def test_fully_played_game_screw_dealer():
    # setup game
    team1 = Team(1)
    team2 = Team(2)
    p1 = Player("A", 1, team1)
    p2 = Player("B", 2, team2)
    p3 = Player("C", 3, team1)
    p4 = Player("D", 4, team2)

    g = Game(players=[p1, p2, p3, p4], points_to_win=10)

    while not g.is_over:
        # game starts with no hands
        g.new_hand()
        print("=" * 50, "Hand number: {}".format(len(g.hands)), "=" * 50)
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
        print("=" * 50, "Scoring hand {}".format(len(g.hands)), "=" * 50)
        the_hand.score()


def _test_trick(trick, game):
    the_hand = game.hands[-1]
    for p in the_hand.players:
        if p != the_hand.players[0]:
            playable_cards = p.get_playable_cards(led_card=trick.led_card, trump=the_hand.trump)
        else:
            playable_cards = p.cards
        play_card = random.choice(playable_cards)
        trick.add_card(play_card, p)

    trick.score()
    the_hand.tricks.append(trick)
    print([x for x in zip(game.hands[-1].tricks[-1].players, game.hands[-1].tricks[-1].cards)])
    print("Trick winner: {}".format(game.hands[-1].tricks[-1].winner))
