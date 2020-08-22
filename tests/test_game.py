import pytest
import random

from euchre.card import Card
from euchre.deck import Deck
from tests.test_trick import _test_trick, Trick, BidException


def test_cards_dealt_properly(random_game_start, hand_fixture):
    game = random_game_start
    # cards not initially dealt to players
    # the_hand = game.hands[0]
    the_hand = hand_fixture
    non_hand_cards = [the_hand.top_card] + the_hand.deck.cards
    fresh_deck = Deck()
    assert [len(x.cards) == 5 for x in game.players]
    assert len(non_hand_cards) == 4
    assert isinstance(the_hand.top_card, Card)
    lst_player_cards = []
    for x in the_hand.players:
        for y in x.cards:
            lst_player_cards.append(y)
    print(len(lst_player_cards))
    print(len(the_hand.deck.cards))
    print(the_hand.top_card)
    # make sure all cards accounted for
    assert not [
        x for x in lst_player_cards + non_hand_cards if x not in fresh_deck.cards
    ]
    # for x in fresh_deck.cards:
    #     if x not in lst_player_cards + game_cards:
    #         print(x)
    # print(lst_player_cards)
    # assert not [x for x in fresh_deck.cards if x not in
    #         lst_player_cards + game_cards]


def test_players_setup_properly(random_game_start):
    """
    Make sure first and third player (first dealers) are
    on the same team.
    :param random_game_start:
    :return:
    """
    game = random_game_start
    assert game.players[0].team == game.players[2].team
    assert game.players[1].team == game.players[3].team
    # sorted_deal_ids = sorted([game.players[0].id, game.players[2].id])
    # sorted_other_ids = sorted([game.players[1].id, game.players[3].id])
    # assert sorted([sorted_other_ids, sorted_deal_ids]) == \
    #        sorted([[x.id for x in game.teams[0].players],
    #        sorted([y.id for y in game.teams[1].players])])


def test_rotate_dealer(random_game_start):
    game = random_game_start
    orig_player_order = game.players
    dealer1 = game.players[0]
    # rotate
    game.rotate_dealer()
    was_dealer1 = game.players[3]
    assert dealer1 == was_dealer1
    dealer2 = game.players[0]
    # rotate
    game.rotate_dealer()
    was_dealer2 = game.players[3]
    assert dealer2 == was_dealer2
    dealer3 = game.players[0]
    # rotate
    game.rotate_dealer()
    was_dealer3 = game.players[3]
    assert dealer3 == was_dealer3
    # rotate
    game.rotate_dealer()
    dealer4 = game.players[0]
    assert dealer1 != dealer2 != dealer3 != dealer4
    assert game.players == orig_player_order


def test_get_initial_scores(random_game_start):
    game = random_game_start
    assert game.scores == {x: 0 for x in game.teams}


def test_get_hand_number(random_game_start):
    game = random_game_start
    game.new_hand()
    assert game.hand_number == 1


def test_game_start_not_over(random_game_start):
    game = random_game_start
    assert game.is_over is False


def test_game_add_hand(random_game_start):
    game = random_game_start
    # add first hand to game
    game.new_hand()
    assert len(game.hands) == 1
    first_dealer = game.dealer
    game.new_hand()
    assert game.hand_number == 2
    second_dealer = game.dealer
    assert second_dealer not in [first_dealer]

    game.new_hand()
    assert game.hand_number == 3
    third_dealer = game.dealer
    assert third_dealer not in [first_dealer, second_dealer]

    game.new_hand()
    assert game.hand_number == 4
    fourth_dealer = game.dealer
    assert fourth_dealer not in [first_dealer, second_dealer, third_dealer]

    game.new_hand()
    assert game.hand_number == 5
    fifth_dealer = game.dealer
    assert first_dealer == fifth_dealer
    # scores never set, hands never played
    assert game.scores == {x: 0 for x in game.teams}


def test_set_players_order(random_game_start):
    game = random_game_start
    assert game.players[0].team == game.players[2].team
    assert game.players[1].team == game.players[3].team


def test_game_points_setup_correctly(setup_game):
    game = setup_game
    assert list(game.scores.values()) == [0, 0]


def test_fully_played_game_screw_dealer(setup_game):
    g = setup_game

    while not g.is_over:
        # game starts with no hands
        g.new_hand()
        print("Dealer is now {}".format(g.players[0]))
        print("=" * 50, "Hand number: {}".format(len(g.hands)), "=" * 50)
        the_hand = g.hands[-1]
        print("Top card is now {}".format(the_hand.top_card))
        print("Players: {}".format(the_hand.players))
        bid_player = g.hands[-1].players[0]
        the_hand.bid(bid_player, "pass")
        print(str(bid_player) + " passes")

        bid_player = g.hands[-1].players[0]
        the_hand.bid(bid_player, "pass")
        print(str(bid_player) + " passes")

        bid_player = g.hands[-1].players[0]
        the_hand.bid(bid_player, "pass")
        print(str(bid_player) + " passes")

        bid_player = g.hands[-1].players[0]
        the_hand.bid(bid_player, "pass")
        print(str(bid_player) + " passes")

        the_hand.top_card_turned_over = True

        bid_player = g.hands[-1].players[0]
        the_hand.bid(bid_player, "pass")
        print(str(bid_player) + " passes")

        bid_player = g.hands[-1].players[0]
        the_hand.bid(bid_player, "pass")
        print(str(bid_player) + " passes")

        bid_player = g.hands[-1].players[0]
        the_hand.bid(bid_player, "pass")
        print(str(bid_player) + " passes")

        # next one should throw screw the dealer
        with pytest.raises(BidException):
            the_hand.bid(the_hand.players[0], "pass")

        bid_suit = random.choice(g.hands[-1].possible_trump)
        the_hand.bid(the_hand.players[0], "set_trump", bid_suit)
        print("Trump set as {}".format(the_hand.trump))
        assert len(the_hand.tricks) == 0

        for i in range(0, 5):
            trick = Trick(hand=the_hand)
            if i > 0:
                trick.set_order_by_last_winner()
            _test_trick(trick, g)
        print("=" * 50, "Scoring hand {}".format(len(g.hands)), "=" * 50)
        the_hand.score()
