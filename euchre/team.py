

class Team:
    def __init__(self, players, id):
        self.players = players
        self.id = id
        self.score = 0

    @property
    def get_score(self):
        return self.score
