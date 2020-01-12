from euchre.hand import Hand
from euchre.deck import Deck


def test_hand(hand_fixture):
    d = Deck()
    hand = Hand(dealer=2, deal_style=[3,2,3,2], players=[0,1,2,3], deck=d)
    hand.deal()
    assert hand.top_card not in hand.deck.cards
    dealt_cards = flatten_list(hand.hands.values())
    assert hand.top_card not in dealt_cards
    assert sorted(list(set(dealt_cards))) == sorted(list(dealt_cards))


def test_set_trump():
    set_trump

def flatten_list(the_list):
    return [item for sublist in the_list for item in sublist]
