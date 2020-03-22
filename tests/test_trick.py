from euchre.trick import Trick
from euchre.deck import Deck
from euchre.player import Player
from euchre.card import Card


def test_trick_with_trump_led(hand_fixture):
    t = Trick()
    d = Deck()
    t.cards = [Card("10", "S"), Card("10", "H"), Card("10", "D"), Card("10", "C")]
    t.led_suit = "S"
    t.led_rank = "10"
    t.players = [Player(name="Player {}".format(x), player_id=x) for x in [3, 0, 1, 2]]
    hand_fixture.set_trump("H")
    rez = t.score(hand=hand_fixture)
    print(rez)
