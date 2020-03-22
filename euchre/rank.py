"""
I hold information about rank names and bowers
"""


class Rank:
    def __init__(self):
        self.names = {"7": "Seven", "8": "Eight", "9": "Nine", "10": "Ten",
                      "J": "Jack", "Q": "Queen", "K": "King", "A": "Ace"}

    @property
    def non_bowers(self):
        non_bowers = self.names.copy()
        del non_bowers["J"]
        return non_bowers
