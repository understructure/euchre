

class Team:
    def __init__(self, players):
        self.players = players
        self.score = 0

    @property
    def get_score(self):
        return self.score
