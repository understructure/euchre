class Team:
    def __init__(self, id):
        # self.players = players
        self.id = id

    def __str__(self):
        return "Team {}".format(self.id)

    def __repr__(self):
        return "Team {}".format(self.id)
