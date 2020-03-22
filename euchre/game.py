"""
Keeps track of the game, may be called a rubber eventually?
"""
import random

from euchre.hand import Hand
from euchre.deck import Deck


class Game:
    def __init__(self, teams, points_to_win):
        self.hands = []
        self.teams = teams
        self.play_to_points = points_to_win
        # whatever number is selected will rotate to the next
        # value in sequence when new game is started
        self.first_dealer = random.choice(seq=range(4))
        self.players = self.set_players_order()
        self.deal_style = [2, 3, 2, 3]
        self.low_rank = "9"
        self.new_hand()
        # dealer is first in list, person to dealer's right
        # is first person to bid
        self.players[1].current_turn = True

    @property
    def dealer(self):
        return self.hands[-1].players[0]

    @property
    def is_over(self):
        return not all(x.score < self.play_to_points for x in self.teams)

    @property
    def hand_number(self):
        return len(self.hands)

    def set_players_order(self):
        temp = []
        # assumes teams are same length
        for i in range(len(self.teams)):
            for j in range(len(self.teams[i].players)):
                temp.append(self.teams[j].players[i])
        return temp[self.first_dealer:] + temp[:self.first_dealer]

    def get_scores(self):
        return {x: self.teams[x].score
                for x in range(len(self.teams))}

    def new_hand(self):
        deck = Deck(low_rank=self.low_rank)
        self.rotate_dealer()
        self.hands.append(Hand(players=self.players,
                               deal_style=self.deal_style,
                               deck=deck))

    def rotate_dealer(self):
        temp = self.players
        self.players = temp[1:] + temp[:1]

    # def update_score(self):
    #     # which is the winning team?
    #     # how many points?
    #     hand = self.hands[-1]
    #     hand.score()
    #     if self.is_over:
    #         print("Game Over, Team {} wins!".format(winning_team))
    #         print("Final score, Team {}: {}, Team {}: {}"
    #               .format(self.game.teams[0], self.game.teams[0].points,
    #                       self.game.teams[1], self.game.teams[1].points))
