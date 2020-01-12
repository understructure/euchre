"""
Deck o' cards
"""
import itertools
import random


class Deck:
    def __init__(self, low_rank=9):
        self.suits = ['S', 'H', 'D', 'C']
        # apparently there are two variations, one that plays with 8's
        # and one that plays with 8's and 7's, low_rank will be used
        # to implement these in the future
        self.ranks = ['A', 'K', 'Q', 'J'] + list(range(10, low_rank-1, -1))
        # self.d_cards_by_suit = {s: [x for x in itertools.
        #                         product(self.ranks, s)] for s in self.suits}
        # self.d_cards_by_suit[None] = []
        self.cards = [x for x in itertools.product(self.suits, self.ranks)]
        random.shuffle(self.cards)

    def get_card_ranks_by_trump_and_led(self, trump, led_suit):
        d_bowers = {'S': 'C', 'C': 'S', 'D': 'H', 'H': 'D'}
        non_bowers = list(self.ranks)
        non_bowers.remove('J')
        if trump is not None:
            return [('J', trump), ('J', d_bowers[trump])] \
                   + list(itertools.product(non_bowers, trump)) \
                   + list(itertools.product(self.ranks, led_suit))
        else:
            return list(itertools.product(non_bowers, led_suit))
