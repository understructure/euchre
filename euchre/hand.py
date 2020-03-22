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

class Hand:
    def __init__(self, players, deal_style, deck):
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
        self.dealer = players[0]
        self.deck = deck
        self.trump = None
        self.bidding_team = None
        self.bid_alone = False
        self.style = deal_style
        # create players list starting with dealer
        self.top_card = None
        self.top_card_turned_over = False
        self.tricks = []
        self.num_players = 4  # change to 3 when going alone
        self.deal()
        self.phase = "bidding"  # [bidding | playing | screwing]
        self.current_player_num = None
        self.current_player = None
        self.set_current_player_num(num=1)

    def set_current_player_num(self, num):
        self.current_player_num = num
        self.current_player = self.players[num]

    def set_trump(self, suit):
        """
        Sets trump for the hand.  Can't set it to be None.
        :param suit: char - S, H, D, C
        :return:
        """
        if self.trump is None:
            if suit in self.deck.suits:
                self.trump = suit
            else:
                print("{} not a valid suit, trump not set".format(suit))
        else:
            print("Trump already set as {} for this hand".format(self.trump))

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

    def hand_score(self):
        num_tricks = len(self.tricks)
        if num_tricks == 5:
            lst_trick_scores = [t.score for t in self.tricks]
            result = dict(functools.reduce(operator.add,
                                           map(collections.Counter, lst_trick_scores)))
            hand_scores = self.game.get_scores()
            num_winner_tricks = max(hand_scores.values())
            winning_team = [k for k in hand_scores.keys()
                            if hand_scores[k] == num_winner_tricks][0]
            if self.bidding_team == winning_team:
                if 3 <= num_winner_tricks <= 4:
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
            self.update_game_score(self.game, winning_team, points)
        else:
            print("Can't score hand yet, only {} trick(s) of 5 played".format(num_tricks))

    def update_game_score(self, winning_team, points):
        total_team_points = self.game.teams[winning_team].points + points
        self.game.teams[winning_team].points = total_team_points
        if total_team_points > self.game.play_to_points:
            print("Game Over, Team {} wins!".format(winning_team))
            print("Final score, Team {}: {}, Team {}: {}"
                  .format(self.game.teams[0], self.game.teams[0].points,
                          self.game.teams[1], self.game.teams[1].points))
            self.game.over = True

    def rotate_active_player(self):
        """
        Sets current_player object and current_player_num
        Advances from 0 to 3 and then resets to 0
        :return:
        """
        next_player_num = self.current_player_num + 1 \
            if self.current_player_num < len(self.players) - 1 \
            else 0
        self.set_current_player_num(num=next_player_num)

    def start_play(self):
        """
        dealer is always first player in list
        :return:
        """
        self.current_player = self.players[1]
        self.phase = "playing"
