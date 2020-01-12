"""
'Sup Playah?
"""


class Player:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.cards = []

    def call_it(self, hand, suit):
        if not hand.top_card_turned_over:
            if self.id == hand.dealer.id:
                hand.set_trump(suit)
            else:
                hand.set_trump(hand.top_card.suit)