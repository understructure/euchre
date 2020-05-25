"""
Represents a round of the game

The following shows all scoring situations:

- Partnership making trump wins 3 or 4 tricks – 1 point
- Partnership making trump wins 5 tricks – 2 points
- Lone hand wins 3 or 4 tricks – 1 point
- Lone hand wins 5 tricks – 4 points
- Partnership or lone hand is euchred, opponents score 2 points

The first player or partnership to score 5, 7 or 10 points,
as agreed beforehand, wins the game. In the 5-point game,
a side is said to be "at the bridge" when it has scored
4 and the opponents have scored 2 or less.
"""
import collections, functools, operator

from euchre.suit import Suit
suit = Suit()
from euchre.trick import Trick

class BidException(BaseException):
    pass

class Hand:
    def __init__(self, players, teams, deal_style, deck):
        """
        Creates a Hand object that keeps track of trump,
        what's been played, and by whom.  List of players
        always has dealer as first in list.
        :param deal_style: list - [2,3,2,3], [3,2,3,2],
                [1,2,3,4], or [4,3,2,1].  Cards are dealt in
                two passes, once with the number of cards in
                forward order per player, once in the list
                order reversed.
        :param deck: a Deck object based on game stetings
                (e.g., low card, joker added)
        """
        self.players = players
        self.teams = teams
        self.players_original_order = players
        self.dealer = players[0]
        self.deck = deck
        self.trump = None
        self.bid_alone = False
        self.style = deal_style
        # create players list starting with dealer
        self.top_card = None
        self.top_card_turned_over = False
        self.tricks = []
        self.num_players = len(self.players)  # change to 3 when going alone
        self.deal() # also sets self.top_card
        self.possible_trump = self.top_card.suit
        self.phase = "bidding"  # [bidding | discarding | playing | screwing]
        self.rotate_active_player()
        self._bidding_team = None
        self.winning_team = None
        self.winning_points = 0

    @property
    def bidding_team(self):
        return self._bidding_team

    @bidding_team.setter
    def bidding_team(self, value):
        self._bidding_team = value

    def rotate_active_player(self):
        self.players = self.players[1:] + self.players[:1]

    # def set_trump(self, suit):
    #     """
    #     Sets trump for the hand.  Can't set it to be None.
    #     :param suit: char - S, H, D, C
    #     :return:
    #     """
    #     if self.trump is None:
    #         if suit in self.deck.suits:
    #             self.trump = suit
    #             print("Trump successfully set as {} for this hand".format(self.trump))
    #         else:
    #             raise ValueError("{} not a valid suit, trump not set".format(suit))
    #     else:
    #         print("Trump already set as {} for this hand".format(self.trump))

    def deal(self):
        for _ in range(2):
            # for player in range(len(self.players)):
            for player in range(len(self.players)):
                for _ in range(self.style[player]):
                    # deal off top of deck
                    self.players[player].cards.append(self.deck.cards.pop(0))
            self.style.reverse()
        self.top_card = self.deck.cards.pop(0)

    def set_bid_alone(self, player_id):
        self.bid_alone = True
        self.num_players = 3
        partner_id = self.game.partner[player_id]
        self.players.remove(partner_id)

    def bid(self, player, action, trump=None, alone=False):
        if action == "pass":
            if player == self.dealer:
                if not self.top_card_turned_over:
                    self.top_card_turned_over = True
                    self.possible_trump = [x for x in suit.names.keys() if self.top_card.suit != x]
                else:
                    raise BidException("Screw the dealer, you must bid!".format(trump))
            self.rotate_active_player()
        elif action == "pick_it_up":
            self.phase = "discarding"
            # this is ok as top card isn't in the deck
            self.dealer.cards += self.top_card
            self.bidding_team = [x for x in self.teams if player in x][0]

        elif action == "set_trump":
            if trump in self.possible_trump:
                self.trump = trump
                print("Trump successfully set as {} for this hand".format(self.trump))
                self.bidding_team = player.team
                print("Bidding team: {}".format(self.bidding_team))
                if not alone:
                    self.players = self.players_original_order
                    self.rotate_active_player()
                    self.phase = "playing"
                else:
                    raise NotImplementedError("Need to implment going alone")
            else:
                raise BidException("Can't set trump to {}!".format(trump))
        else:
            raise BidException("Invalid action: {}".format(action))

    def score(self):
        team_scores = {t: 0 for t in self.teams}
        for trick in self.tricks:
            team_scores[trick.winner.team] += 1
        self.winning_team = max(team_scores.items(), key=operator.itemgetter(1))[0]

        # this should be dynamic
        if len(self.tricks) == 5:
            if self.bidding_team == self.winning_team:
                if 3 <= team_scores[self.winning_team] <= 4:
                    # 1 point to bidding team
                    points = 1
                elif not self.bid_alone:
                    # 2 points to bidding team
                    points = 2
                else:
                    # 4 points, all 5 tricks taken alone
                    points = 4
            else:
                # euch'd! 2 points to non-bidding team
                points = 2
            self.winning_points = points
        else:
            print("Can't score hand yet, only {} trick(s) of 5 played".format(num_tricks))

    def start_play(self):
        """
        dealer is always first player in list, may have to change this
        for going alone?
        :return:
        """
        self.current_player = self.players[1]
        self.phase = "playing"
