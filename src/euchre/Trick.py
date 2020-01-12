"""
Represents each player playing a card
"""


class Trick:
    def __init__(self):
        self.cards = []
        self.players = []

    def add_card(self, player, card):
        self.cards.append(card)
        self.players.append(player)
        player.hand.cards.remove(card)

    def score(self, hand):
        possible_winning_players = []
        possible_winning_cards = []
        if len(self.cards) == 4:
            # what was led
            led_suit, led_rank = self.cards[0]
            # trump
            trump = hand.trump
            possible_winning_cards = \
                hand.deck.get_card_ranks_by_trump_and_led(trump, led_suit)
            for i in range(len(self.cards)):
                the_card = self.cards[i]
                if the_card in possible_winning_cards:
                    possible_winning_players.append(i)
                    possible_winning_cards.append(possible_winning_cards.index(the_card))
        winner = possible_winning_players[possible_winning_cards.index(min(possible_winning_cards))]
        return winner
