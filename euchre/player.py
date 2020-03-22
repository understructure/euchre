"""
'Sup Playah?
"""
import logging

logger = logging.getLogger(__name__)


class Player:
    def __init__(self, name, player_id):
        self.name = name
        self.id = player_id
        self.cards = []
        self.dealer = False

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
