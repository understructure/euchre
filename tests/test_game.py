from euchre.card import Card
from euchre.deck import Deck


def test_cards_dealt_properly(random_game_start):
    game = random_game_start
    # cards not initially dealt to players
    the_hand = game.hands[0]
    game_cards = [the_hand.top_card] + the_hand.deck.cards
    fresh_deck = Deck()
    assert [len(x.cards) == 5 for x in game.players]
    assert len(game_cards) == 4
    assert isinstance(the_hand.top_card, Card)
    lst_player_cards = []
    for x in game.players:
        for y in x.cards:
            lst_player_cards.append(y)
    # make sure all cards accounted for
    assert not [x for x in lst_player_cards +
            game_cards if x not in fresh_deck.cards]
    assert not [x for x in fresh_deck.cards if x not in
            lst_player_cards + game_cards]
