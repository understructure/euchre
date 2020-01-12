"""
'Sup Playah?
"""


class Player:
    def __init__(self, name, player_id, team):
        self.name = name
        self.id = player_id
        self.team = team

    def call_it(self, hand, suit, alone=False):
        hand.bidding_team = self.team
        if not hand.top_card_turned_over:
            if self.id == hand.dealer.id:
                hand.set_trump(suit)
            else:
                hand.set_trump(hand.top_card.suit)
        if alone:
            hand.set_bid_alone()

    def discard(self, hand, card):
        if hand.dealer == self.id and len(hand.hands[self.id]) == 6:
            hand.hands[self.id].remove(card)
        else:
            print("Only the dealer may discard and only when (s)he has six cards")

    @staticmethod
    def screw_the_dealer(hand):
        hand.top_card_turned_over = True
