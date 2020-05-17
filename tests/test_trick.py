from euchre.trick import Trick
from euchre.deck import Deck
from euchre.player import Player
from euchre.card import Card
from euchre.hand import Hand


def test_trick_with_trump_led(hand_fixture):
t = Trick()
d = Deck()
p0 = Player(name='matthew', player_id=0)
p1 = Player(name='sean', player_id=1)
p2 = Player(name='sean', player_id=2)
p3 = Player(name='sean', player_id=3)
h = Hand(players=[p0, p1, p2, p3], deal_style=[3, 2, 3, 2], deck=d)
t.add_card(player=p0, card=p0.cards[0], hand=h)
t.add_card(player=p1, card=p1.cards[0], hand=h)
t.add_card(player=p2, card=p2.cards[0], hand=h)
t.add_card(player=p3, card=p3.cards[0], hand=h)

    t.add_card()
    t.cards = [Card("10", "S"), Card("10", "H"), Card("10", "D"), Card("10", "C")]
    t.led_suit = "S"
    t.led_rank = "10"
    t.players = [Player(name="Player {}".format(x), player_id=x) for x in [3, 0, 1, 2]]
    hand_fixture.set_trump("H")
    rez = t.score(hand=hand_fixture)
    print(rez)
