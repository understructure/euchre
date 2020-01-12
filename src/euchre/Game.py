"""
Keeps track of the game, may be called a rubber eventually?
"""


class Game:
    def __init__(self, players):
        self.hands = []
        self.players = players

    def get_hands(self):
        return self.hands

    def score(self):
        pass

    def add_hand(self, hand):
        self.hands.append(hand)
