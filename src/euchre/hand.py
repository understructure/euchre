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


class Hand:
    def __init__(self, dealer_id, deal_style, player_ids, deck, game):
        """
        Creates a Hand object that keeps track of trump,
        what's been played, and by whom.
        :param dealer_id: int - represents the position in the list
                for the player that dealt so we know
                what suit was led
        :param deal_style: list - [2,3,2,3], [3,2,3,2],
                [1,2,3,4], or [4,3,2,1].  Cards are dealt in
                two passes, once with the number of cards in
                forward order per player, once in the list
                order reversed.
        :param player_ids: list - could be names, numbers, whatever
        """
        self.game = game
        self.dealer = dealer_id
        self.players = player_ids[dealer_id:] + player_ids[:dealer_id]
        self.hands = {p: [] for p in self.players}
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
                print("{} not a valid suit, trump not set")
        else:
            print("Trump already set as {} for this hand".format(self.trump))

    def deal(self):
        for _ in range(2):
            for player in range(len(self.players)):
                for _ in range(self.style[player]):
                    # deal off top of deck
                    self.hands[player].append(self.deck.cards.pop(0))
            self.style.reverse()
        self.top_card = self.deck.cards.pop(0)

    def set_bid_alone(self, player_id):
        self.bid_alone = True
        self.num_players = 3
        partner_id = self.game.partner[player_id]
        self.players.remove(partner_id)
        del self.hands[partner_id]

    def hand_score(self):
        num_tricks = len(self.tricks)
        if num_tricks == 5:
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
            print("Can't score hand yet, only {} tricks of 5 played".format(num_tricks))

    def update_game_score(self, winning_team, points):
        total_team_points = self.game.teams[winning_team].points + points
        self.game.teams[winning_team].points = total_team_points
        if total_team_points > self.game.play_to_points:
            print("Game Over, Team {} wins!".format(winning_team))
            print("Final score, Team {}: {}, Team {}: {}"
                  .format(self.game.teams[0], self.game.teams[0].points,
                          self.game.teams[1], self.game.teams[1].points))
            self.game.over = True
