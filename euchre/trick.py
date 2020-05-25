"""
Represents each player playing a card
"""
from logging import getLogger

logger = getLogger(__name__)

class TrickFullError:
    pass


class TrickNotScorableYetError:
    pass


class Trick:
    def __init__(self, hand):
        self.cards = []
        self.hand = hand
        self.players = hand.players
        self.led_suit = None
        self.led_rank = None
        self.led_card = None
        self.winner = None

    def add_card(self, card, player):
        if len(self.cards) == 0:
            self.led_card = card
            self.led_suit = card.suit
            self.led_rank = card.rank
        if len(self.cards) < len(self.players):
            self.cards.append(card)
            player.cards.remove(card)
        else:
            raise TrickFullError("{} cards in hand and {} cards in trick, time to score it!"
                                 .format(len(self.cards), len(self.players)))

    def score(self):
        if len(self.cards) == len(self.players):
            card_ranks_by_trump_and_led = \
                self.hand.deck.get_card_ranks_by_trump_and_led(self.hand.trump, self.led_card)
            self.set_winner(card_ranks_by_trump_and_led)
        else:
            raise TrickNotScorableYetError("Hand only has {} cards, need {} cards to score it"
                                           .format(len(self.cards), len(self.players)))

    def set_winner(self, trick_ranked_cards):
        trick_values = []
        for card in self.cards:
            if card in trick_ranked_cards:
                ranked = trick_ranked_cards.index(card)
            else:
                ranked = 99
            trick_values.append(ranked)
        min_trick_val = min(trick_values)
        logger.debug("min trick val: {}".format(min_trick_val))
        self.winner = self.players[trick_values.index(min_trick_val)]

    def set_order_by_last_winner(self):
        if len(self.hand.tricks) > 0 and len(self.cards) == 0:
            p_winner = self.hand.tricks[-1].winner
            winner_idx = self.players.index(p_winner)
            self.players = self.players[winner_idx:] + self.players[:winner_idx]
        else:
            print("First trick in hand, can't set order by last winner")
