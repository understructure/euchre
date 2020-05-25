

class Strategy:
    def __init__(self):
        pass


class SimpleStrategy(Strategy):
    def __init__(self, lst_cards, trump, led_suit):
        self.card_ranks = self._rank_cards()

    def _rank_cards(self):
        trump_cards = None
