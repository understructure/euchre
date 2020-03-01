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

        if not 7 <= low_rank <= 9:
            raise IllegalArgumentError
        self.suits = list(suit.names.keys())
        # apparently there are two variations, one that plays with 8's
        # and one that plays with 8's and 7's, low_rank will be used
        # to implement these in the future
        self.ranks = ['A', 'K', 'Q', 'J'] + [str(x) for x in list(range(10, low_rank-1, -1))]
        self.non_bowers = [x for x in self.ranks if x != "J"]
        # self.d_cards_by_suit = {s: [x for x in itertools.
        #                         product(self.ranks, s)] for s in self.suits}
        # self.d_cards_by_suit[None] = []
        self.cards = [Card(**dict(zip(['card_rank', 'card_suit'], x)))
                      for x in itertools.product(self.ranks, self.suits)]
        random.shuffle(self.cards)

    def get_card_ranks_by_trump_and_led(self, trump, led_card):
        """
        TODO: If the bower suit is led (e.g. Clubs led when
        Spades is trump), remove left bower from product of led_suit
        and ranks
        :param trump:
        :param led_suit:
        :return:
        """
        led_suit = led_card.suit
        d_bowers = suit.d_bower_suits
        left_bower = Card(card_rank="J", card_suit=d_bowers[trump])
        right_bower = Card(card_rank="J", card_suit=trump)
        lst_extra = []
        if trump is not None:
            lst_out = [right_bower, left_bower] + \
                      [Card(**dict(zip(['card_rank', 'card_suit'], x)))
                       for x in itertools.product(self.non_bowers, trump)]
            # list(itertools.product(non_bowers, trump))

            # calling left bower's suit its natural suit, should
            # probably change it to be an honorary trump suit?
            if trump != led_suit:
                print(led_card == left_bower)
                if led_card != left_bower:
                    lst_extra = list(itertools.product(
                        self.ranks, led_suit))
                else:
                    lst_extra = [Card(**dict(zip(['card_rank', 'card_suit'], x)))
                                 for x in itertools.product(self.non_bowers, led_suit)]
        else:
            lst_out = list(itertools.product(self.ranks, led_suit))
        lst_out += lst_extra
        return lst_out
