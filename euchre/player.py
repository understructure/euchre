"""
'Sup Playah?
"""
import logging

logger = logging.getLogger(__name__)

from euchre.suit import Suit

_suit = Suit()

class Player:
    def __init__(self, name, player_id):
        self.name = name
        self.id = player_id
        self.cards = []
        self.dealer = False

    def __repr__(self):
        return "Player ID: {}, name: {}".format(self.id, self.name)

    def get_playable_cards(self, led_card, trump):
        led_suit = _suit.effective_suit(led_card, trump)
        led_in_hand = [y for y in self.cards if _suit.effective_suit(y, trump) == led_suit]
        trump_in_hand = [x for x in self.cards if _suit.effective_suit(x, trump) == trump]

        if not led_in_hand:
            # can play anything
            return self.cards
        elif trump == led_suit:
            # led_in_hand and trump_in_hand will be the same, just return one
            return trump_in_hand
        else:
            return trump_in_hand + led_in_hand

    def remove_card(self, card):
        try:
            idx = self.cards.index(card)
            rez = self.cards.pop(idx)
            return rez
        except ValueError:
            logger.error("{} is not in player's hand".format(card))
            raise

    def bid_action2(self, action):
        if action == "pass":
            rez = "pass"
        elif action == "call_it_up":
            rez = self.call_it_up(hand=hand, **kwargs)
        elif action == "screw_the_dealer":
            pass
        return rez

    def bid_action(self, hand, action, **kwargs):
        if action == "pass":
            rez = "pass"
        elif action == "call_it_up":
            rez = self.call_it_up(hand=hand, **kwargs)
        elif action == "screw_the_dealer":
            pass
        return rez

    def call_it_up(self, hand, alone=False, **kwargs):
        rez = {"called_up": False}
        if not hand.top_card_turned_over:
            rez["called_up"] = True
            hand.top_card_turned_over = True
            hand.set_trump(hand.top_card.suit)
            if self.dealer:
                discard = kwargs.get("discard")
                self.dealer_call_it(hand=hand, discard=discard)
                hand.phase = "playing"
            else:
                hand.phase = "dealer_discard"
            if alone:
                hand.set_bid_alone()
        else:
            logger.error("ERROR - tried to call trump when top card already turned over!")
            raise

    def dealer_call_it(self, hand, discard):
        temp_hand = [x for x in self.cards if x != discard]
        temp_hand.append(hand.top_card)
        self.cards = temp_hand
        hand.top_card_turned_over = True
        hand.set_trump(hand.top_card.suit)
        hand.phase = "playing"

    @staticmethod
    def screw_the_dealer(hand):
        hand.top_card_turned_over = True
        hand.phase = "screwing"

    @staticmethod
    def screwed_call_it(hand, trump):
        if not hand.top_card_turned_over:
            logger.error("Can't call this method if top card isn't turned over!")
            raise
        elif trump == hand.top_card.suit:
            logger.error("Can't call this as trump, top card was turned over!")
            raise
        else:
            hand.trump = trump
            hand.phase = "playing"
