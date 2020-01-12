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


class IllegalArgumentError(ValueError):
    pass


class Deck:
    def __init__(self, low_rank=9):
        card = Card()
        if not 7 <= low_rank <= 9:
            raise IllegalArgumentError
        self.suits = list(card.suit_names.keys())
        # apparently there are two variations, one that plays with 8's
        # and one that plays with 8's and 7's, low_rank will be used
        # to implement these in the future
        self.ranks = ['A', 'K', 'Q', 'J'] + [str(x) for x in list(range(10, low_rank-1, -1))]
        # self.d_cards_by_suit = {s: [x for x in itertools.
        #                         product(self.ranks, s)] for s in self.suits}
        # self.d_cards_by_suit[None] = []
        self.cards = [x for x in itertools.product(self.ranks, self.suits)]
        random.shuffle(self.cards)

    def get_non_bower_ranks(self):
        lst_out = list(self.ranks)
        lst_out.remove('J')
        return lst_out

    def get_card_ranks_by_trump_and_led(self, trump, led_suit):
        lst_out = []
        d_bowers = {'S': 'C', 'C': 'S', 'D': 'H', 'H': 'D'}
        non_bowers = self.get_non_bower_ranks()
        if trump is not None:
            lst_out = [('J', trump), ('J', d_bowers[trump])] \
                   + list(itertools.product(non_bowers, trump))
            if trump != led_suit:
                lst_out = lst_out + list(itertools.product(self.ranks, led_suit))
        else:
            lst_out = list(itertools.product(self.ranks, led_suit))
        return lst_out
