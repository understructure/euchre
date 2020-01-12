"""
Represents a round of the game
"""


class Hand:
    def __init__(self, dealer, deal_style, players, deck):
        """
        Creates a Hand object that keeps track of trump,
        what's been played, and by whom.
        :param dealer: int - represents the position in the list
                for the player that dealt so we know
                what suit was led
        :param deal_style: list - [2,3,2,3], [3,2,3,2],
                [1,2,3,4], or [4,3,2,1].  Cards are dealt in
                two passes, once with the number of cards in
                forward order per player, once in the list
                order reversed.
        :param players: list - could be names, numbers, whatever
        """
        self.trump = None
        self.dealer = dealer
        self.style = deal_style
        # create players list starting with dealer
        self.players = players[dealer:] + players[:dealer]
        self.hands = {p: [] for p in self.players}
        self.deck = deck
        self.top_card = deck[0] # kind of a cheat but eh
        self.top_card_turned_over = False

    def set_trump(self, suit):
        """
        Sets trump for the hand.  Can't set it to be None.
        :param suit: char - S, H, D, C
        :return:
        """
        if self.trump_set is None:
            if suit in self.deck.suits:
                self.trump = suit
                self.trump_set = True
            else:
                print("{} not a valid suit, trump not set")
        else:
            print("Trump already set as {} for this hand".format(self.trump))

    def deal(self):
        for _ in range(2):
            for player in range(len(self.players)):
                for _ in range(self.style[player]):
                    self.hands[player].append(self.deck.cards.pop())
            self.style.reverse()
