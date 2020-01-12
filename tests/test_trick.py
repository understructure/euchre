from euchre.trick import Trick
from euchre.card import Card
from euchre.deck import Deck
from euchre.hand import Hand

def test_trick_with_trump_led():
    t = Trick()
    d = Deck()
    t.cards = [("10", "S"), ("10", "H"), ("10", "D"), ("10", "C")]
    t.led_suit = "S"
    t.led_rank = "10"
    t.players = [3, 0, 1, 2]
    handy = Hand(dealer=2, deal_style=[3,2,3,2], players={0: "Matthew", 1: "Sean", 2: "Melissa", 3: "Mione"}, deck=d)
    handy.trump = "H"
    rez = t.score(hand=handy)
    print(rez)