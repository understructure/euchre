import pytest
import random

from euchre.trick import Trick, TrickFullError, TrickNotScorableYetError
from euchre.hand import BidException


@pytest.mark.xfail(raises=TrickFullError)
def test_trick_full(hand_fixture):
    t = Trick(hand=hand_fixture)
    t.add_card(card=hand_fixture.players[0].cards[0], player=hand_fixture.players[0])
    t.add_card(card=hand_fixture.players[1].cards[0], player=hand_fixture.players[1])
    t.add_card(card=hand_fixture.players[2].cards[0], player=hand_fixture.players[2])
    t.add_card(card=hand_fixture.players[3].cards[0], player=hand_fixture.players[3])
    t.add_card(card=hand_fixture.players[0].cards[1], player=hand_fixture.players[0])


@pytest.mark.xfail(raises=ValueError)
def test_set_order_by_last_winner(hand_fixture):
    t = Trick(hand=hand_fixture)
    t.set_order_by_last_winner()


@pytest.mark.xfail(raises=TrickNotScorableYetError)
def test_score_cards_less_than_players_fail(hand_fixture):
    assert len(hand_fixture.players) == 4
    t = Trick(hand=hand_fixture)
    t.add_card(card=hand_fixture.players[0].cards[0], player=hand_fixture.players[0])
    t.add_card(card=hand_fixture.players[1].cards[0], player=hand_fixture.players[1])
    t.add_card(card=hand_fixture.players[2].cards[0], player=hand_fixture.players[2])
    t.score()



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
