"""
Keeps track of the game, may be called a rubber eventually?
"""


class Game:
    def __init__(self, teams, points_to_win):
        self.over = False
        self.hands = []
        self.teams = teams
        self.play_to_points = points_to_win
        self.partner = {0: 2, 2: 0, 1: 3, 3: 1}

    def get_scores(self):
        return {0: self.teams[0].points,
                1: self.teams[1].points}

    # def add_hand(self, hand):
    #     self.hands.append(hand)
