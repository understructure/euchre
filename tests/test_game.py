from euchre.card import Card
from euchre.deck import Deck


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
    assert not [x for x in lst_player_cards +
            non_hand_cards if x not in fresh_deck.cards]
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
    assert game.get_scores() == {x: 0 for x in game.teams}


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
    assert game.get_scores() == {x: 0 for x in game.teams}
