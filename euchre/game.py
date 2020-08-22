"""
Keeps track of game state, may be called a rubber eventually?
"""
import random

from euchre.hand import Hand
from euchre.deck import Deck
# from collections import Counter


class Game:
    def __init__(self, players, points_to_win):
        self.hands = []
        self.teams = list(set([x.team for x in players]))
        self.play_to_points = points_to_win
        # whatever number is selected will rotate to the next
        # value in sequence when new game is started
        self.players = self.set_players_order(players)
        self.deal_style = [2, 3, 2, 3]
        self.low_rank = "9"
        # dealer is first in list, person to dealer's right
        # is first person to bid
        self.players[1].current_turn = True

    @property
    def dealer(self):
        return self.hands[-1].dealer
        # return self.hands[-1].players[0]

    @property
    def is_over(self):
        print("SCORES: {}".format(str(self.scores)))
        return any([x >= self.play_to_points for x in self.scores.values()])
        # scores = self.get_scores()
        # print("SCORES: {}".format(str(scores)))
        # return any([x >= self.play_to_points for x in scores.values()])

    @property
    def hand_number(self):
        return len(self.hands)

    @property
    def scores(self):
        rez = {t: 0 for t in self.teams}
        for hand in self.hands:
            if hand.winning_team:
                rez[hand.winning_team] += hand.winning_points
            else:
                print("No winner for hand yet")
        return rez

    def set_players_order(self, players):
        deal_team = random.choice(self.teams)
        other_team = [x for x in self.teams if x != deal_team][0]
        deal_player = random.choice([x for x in players if x.team == deal_team])
        deal_partner = [x for x in players if x.team == deal_team and x != deal_player][0]
        other_players = [x for x in players if x.team == other_team]
        ordered_players = [
            deal_player,
            other_players[0],
            deal_partner,
            other_players[1]
        ]
        return ordered_players

    # def get_scores(self):
    #     rez = {t: 0 for t in self.teams}
    #     for hand in self.hands:
    #         if hand.winning_team:
    #             rez[hand.winning_team] += hand.winning_points
    #         else:
    #             print("No winner for hand yet")
    #     return rez

    def new_hand(self):
        deck = Deck(low_rank=self.low_rank)
        self.rotate_dealer()
        self.hands.append(Hand(players=self.players,
                               teams=self.teams,
                               deal_style=self.deal_style,
                               deck=deck))

    def rotate_dealer(self):
        temp = self.players
        self.players = temp[1:] + temp[:1]
