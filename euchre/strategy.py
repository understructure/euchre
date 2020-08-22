import random

#
# class Strategy:
#     def __init__(self):
#         pass
#
#
# class SimpleStrategy(Strategy):
#     def __init__(self, lst_cards, trump, led_suit):
#         self.card_ranks = self._rank_cards()
#
#     def _rank_cards(self):
#         trump_cards = None
#
#     def score_hand_against_top_card(self, game, player):
#         top_card = game.hands[-1].top_card
#         top_card_turned_over = game.hands[-1].top_card_turned_over
#         player_cards = player.cards
#         if top_card.rank == "J":
#             top_card_points = 2
#         elif top_card.rank == "A":
#             top_card_points = 1
#         else:
#             top_card_points = 0
#
#


def bid_strategy(bid_phase, is_dealer, call_prob={"bidding": 0.4, "screwing": 0.5}):
    try:
        bid_prob = call_prob[bid_phase]
        if bid_phase == "screwing" and is_dealer:
            rez = "call_it"
        else:
            x = random.choice(range(100)) / 100.0
            print("Bid probability is {}, random is {}".format(bid_prob, x))
            if x <= bid_prob:
                rez = "call_it"
            else:
                rez = "pass_it"
        return rez
    except ValueError:
        raise ("Unknown bid phase {}".format(bid_phase))
