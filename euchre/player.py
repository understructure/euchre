"""
'Sup Playah?
"""
import logging

logger = logging.getLogger("euchre")

from euchre.suit import Suit

_suit = Suit()


class Player:
    def __init__(self, name, player_id, team):
        self.name = name
        self.id = player_id
        self.cards = []
        self.dealer = False
        self.team = team

    def __repr__(self):
        return "Player {}".format(self.name)

    def get_playable_cards(self, led_card, trump):
        led_suit = _suit.effective_suit(led_card, trump)
        led_in_hand = [
            y for y in self.cards if _suit.effective_suit(y, trump) == led_suit
        ]
        trump_in_hand = [
            x for x in self.cards if _suit.effective_suit(x, trump) == trump
        ]

        if not led_in_hand:
            # can play anything
            return self.cards
        elif trump == led_suit:
            # led_in_hand and trump_in_hand will be the same, just return one
            # return all cards if no trump in hand
            return trump_in_hand or self.cards
        else:
            return trump_in_hand + led_in_hand or self.cards

    def remove_card(self, card):
        try:
            idx = self.cards.index(card)
            rez = self.cards.pop(idx)
            return rez
        except ValueError:
            logger.error("{} is not in player's hand".format(card))
            raise

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
            logger.error(
                "ERROR - tried to call trump when top card already turned over!"
            )
            raise
