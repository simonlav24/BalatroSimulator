


from joker import Joker, BoardVision
from card import Card
from definitions import *

class JokerJimbo(Joker):
    def __init__(self):
        super().__init__(name='Joker')
        self.cost = 2

    def trigger_on_end_hand(self, board: BoardVision):
        board.add_mult(4)
        super().trigger_on_end_hand(board)


class JokerGreedy(Joker):
    def __init__(self):
        super().__init__(name='Greedy Joker')
        self.cost = 5

    def trigger_on_play_card(self, card: Card, board: BoardVision):
        if card.is_suit(Suit.DIAMONDS):
            board.add_mult(3)
        super().trigger_on_play_card(board)


class JokerLusty(Joker):
    def __init__(self):
        super().__init__(name='Lusty Joker')
        self.cost = 5

    def trigger_on_play_card(self, card: Card, board: BoardVision):
        if card.is_suit(Suit.HEARTS):
            board.add_mult(3)
        super().trigger_on_play_card(board)


class JokerWrathful(Joker):
    def __init__(self):
        super().__init__(name='Wrathful Joker')
        self.cost = 5

    def trigger_on_play_card(self, card: Card, board: BoardVision):
        if card.is_suit(Suit.SPADES):
            board.add_mult(3)
        super().trigger_on_play_card(board)


class JokerGluttonous(Joker):
    def __init__(self):
        super().__init__(name='Gluttonous Joker')
        self.cost = 5

    def trigger_on_play_card(self, card: Card, board: BoardVision):
        if card.is_suit(Suit.CLUBS):
            board.add_mult(3)
        super().trigger_on_play_card(board)





class JokerShortcut(Joker):
    def __init__(self):
        super().__init__(name='Shortcut')
        self.cost = 7
        self.rarity = Rarity.UNCOMMON

    def change_evaluation_rules(self, rules):
        rules.straight_skip = True


class JokerFourFingers(Joker):
    def __init__(self):
        super().__init__(name='Four Fingers')
        self.cost = 7
        self.rarity = Rarity.UNCOMMON

    def change_evaluation_rules(self, rules):
        rules.fingers = 4
