import pytest

from euchre.game import Game
from euchre.trick import Trick
from euchre.player import Player
from euchre.team import Team
from euchre.deck import Deck
from euchre.hand import BidException


def test_fully_played_trick():
    deck = Deck()
    p1 = Player("A", 1)
    p2 = Player("B", 2)
    p3 = Player("C", 3)
    p4 = Player("D", 4)


    team1 = Team([p1, p3])
    team2 = Team([p2, p4])

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

    trick = Trick(players=g.hands[-1].players)

    g.hands[-1].tricks.append(trick)

    for p in g.hands[-1].players:
        g.hands[-1].tricks[-1].add_card(p.cards[0], p)

    g.hands[-1].tricks[-1].score(trump=bid_suit, deck=g.hands[-1].deck)
    print("Trick trump: {}".format(bid_suit))
    print("Trick cards: {}".format(g.hands[-1].tricks[-1].cards))
    print("Trick players: {}".format(g.hands[-1].tricks[-1].players))
    print("Trick winner ID: {}".format(g.hands[-1].tricks[-1].winner))


# from euchre.trick import Trick
# from euchre.deck import Deck
# from euchre.player import Player
# from euchre.card import Card
# from euchre.hand import Hand


# def test_trick_with_trump_led(hand_fixture):
# t = Trick()
# d = Deck()
# p0 = Player(name='matthew', player_id=0)
# p1 = Player(name='sean', player_id=1)
# p2 = Player(name='sean', player_id=2)
# p3 = Player(name='sean', player_id=3)
# h = Hand(players=[p0, p1, p2, p3], deal_style=[3, 2, 3, 2], deck=d)
# t.add_card(player=p0, card=p0.cards[0], hand=h)
# t.add_card(player=p1, card=p1.cards[0], hand=h)
# t.add_card(player=p2, card=p2.cards[0], hand=h)
# t.add_card(player=p3, card=p3.cards[0], hand=h)
#
#     t.add_card()
#     t.cards = [Card("10", "S"), Card("10", "H"), Card("10", "D"), Card("10", "C")]
#     t.led_suit = "S"
#     t.led_rank = "10"
#     t.players = [Player(name="Player {}".format(x), player_id=x) for x in [3, 0, 1, 2]]
#     hand_fixture.set_trump("H")
#     rez = t.score(hand=hand_fixture)
#     print(rez)
