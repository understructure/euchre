"""
Represents each player playing a card
"""


class Trick:
    def __init__(self):
        self.cards = []
        self.players = []
        self.led_suit = None
        self.led_rank = None

    def add_card(self, player, card, hand):
        if len(self.cards) == 0:
            self.led_suit = card.suit
            self.led_rank = card.rank
        self.cards.append(card)
        self.players.append(player)
        # hmm...
        player.cards.remove(card)
        if len(self.cards) == hand.num_players:
            result = self.score(hand)
            return result

    def score(self, hand):
        possible_winning_players = []
        possible_winning_cards = []
        if len(self.cards) == 4:
            # trump
            trump = hand.trump
            lst_trump_and_led = \
                hand.deck.get_card_ranks_by_trump_and_led(trump, self.led_suit)
            possible_winning_cards = []
            for i in range(len(self.cards)):
                the_card = self.cards[i]
                if the_card in lst_trump_and_led:
                    possible_winning_players.append(i)
                    possible_winning_cards.append(possible_winning_cards.index(the_card))
        winner = possible_winning_players[possible_winning_cards.index(min(possible_winning_cards))]
        hand.tricks.append({"winner": winner, "cards": self.cards, "players": self.players})
        return winner
