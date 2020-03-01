

class Rank:
    def __init__(self):
        self.names = {"7": "Seven", "8": "Eight", "9": "Nine", "10": "Ten",
                      "J": "Jack", "Q": "Queen", "K": "King", "A": "Ace"}
        self.non_bowers = self._get_non_bowers()

    def _get_non_bowers(self):
        non_bowers = self.names.copy()
        del non_bowers["J"]
        return non_bowers
