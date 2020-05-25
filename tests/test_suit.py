import pytest

from euchre.card import Card
from euchre.suit import Suit
s = Suit()


@pytest.mark.parametrize("card,trump,effective", [(Card("J", "C"), "C", "C"),
                                                  (Card("J", "C"), "S", "S"),
                                                  (Card("J", "C"), "H", "C"),
                                                  (Card("J", "C"), "D", "C"),
                                                  (Card("A", "S"), "C", "S"),
                                                  (Card("A", "S"), "D", "S"),
                                                  (Card("A", "S"), "H", "S"),
                                                  (Card("A", "S"), "S", "S"),])
def test_effective_suit(card, trump, effective):
    assert s.effective_suit(card=card, trump=trump) == effective
