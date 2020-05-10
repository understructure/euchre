"""
The standard 52-card pack can be stripped to make a deck of:
    - 32 cards (A, K, Q, J, 10, 9, 8, 7 of each suit),
    - 28 cards (7s omitted), or
    - 24 cards (7s and 8s omitted).

TODO: In some games, a joker is added.

The highest trump is the jack of the trump suit, called the "right bower."
The second-highest trump is the jack of the other suit of the same color
called the "left bower." (Example: If diamonds are trumps, the right bower
is J♦ and left bower is J♥.) The remaining trumps, and also the plain suits,
rank as follows: A (high), K, Q, J, 10, 9, 8, 7.

TODO: If a joker has been added to the pack, it acts as the highest trump.
"""
import itertools
import random

from euchre.card import Card
from euchre.suit import Suit
from euchre.rank import Rank


r = Rank()
suit = Suit()

class IllegalArgumentError(ValueError):
    pass


class Deck:
    def __init__(self, low_rank=9):
        self.low_low_rank = 7
        self.high_low_rank = 9
        low_rank = int(low_rank)
        if not self.low_low_rank <= low_rank <= self.high_low_rank:
            raise IllegalArgumentError("Low rank of {} not permitted, must be between {} and {}"
                                       .format(low_rank, self.low_low_rank, self.high_low_rank))
        self.suits = list(suit.names.keys())
        # apparently there are variations that play with 8's or 7's as the low card
        # # low_rank will be used to implement this
        self.ranks = ['A', 'K', 'Q', 'J'] + [str(x) for x in list(range(10, low_rank-1, -1))]
        self.non_bowers = [x for x in self.ranks if x != "J"]
        self.cards = [Card(**dict(zip(['card_rank', 'card_suit'], x)))
                      for x in itertools.product(self.ranks, self.suits)]
        random.shuffle(self.cards)

    def get_card_ranks_by_trump_and_led(self, trump, led_card):
        """
        :param trump: [S|H|D|C]
        :param led_card: Card
        :return: list of card ranks for the hand
        """
        led_suit = led_card.suit
        lst_extra = []
        if trump is not None:
            left_bower = Card(card_rank="J", card_suit=suit.d_bower_suits[trump])
            right_bower = Card(card_rank="J", card_suit=trump)
            lst_out = [right_bower, left_bower] + \
                      [Card(**dict(zip(['card_rank', 'card_suit'], x)))
                       for x in itertools.product(self.non_bowers, trump)]
            if not (led_suit == trump or led_card == left_bower):
                lst_extra = self.get_non_trump_led_suit_ranks(trump, led_suit)
        else:
            lst_out = list(itertools.product(self.ranks, led_suit))
        lst_out += lst_extra
        return lst_out

    def get_non_trump_led_suit_ranks(self, trump, led_suit):
        """

        :param trump: str - [C|S|D|H]
        :param led_suit: str - [C|S|D|H]
        :return:
        """
        if led_suit in [trump, suit.d_bower_suits[trump]]:
            lst_extra = [Card(**dict(zip(['card_rank', 'card_suit'], x))) for x in
                         itertools.product(self.non_bowers, led_suit)]
        else:
            lst_extra = [Card(**dict(zip(['card_rank', 'card_suit'], x))) for x in
                         itertools.product(self.ranks, led_suit)]
        return lst_extra
