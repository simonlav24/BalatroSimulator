


from joker import Joker, BoardVision
from card import Card
from definitions import *
from evaluation_rules import EvaluationRules


class JokerJimbo(Joker):
    def __init__(self):
        super().__init__(name='Joker')
        self.data.cost = 2

    def trigger_on_end_hand(self, board: BoardVision):
        board.add_mult(4)
        super().trigger_on_end_hand(board)


class JokerGreedy(Joker):
    def __init__(self):
        super().__init__(name='Greedy Joker')
        self.data.cost = 5

    def trigger_on_play_card(self, card: Card, board: BoardVision):
        if card.is_suit(Suit.DIAMONDS):
            board.add_mult(3)
        super().trigger_on_play_card(board)


class JokerLusty(Joker):
    def __init__(self):
        super().__init__(name='Lusty Joker')
        self.data.cost = 5

    def trigger_on_play_card(self, card: Card, board: BoardVision):
        if card.is_suit(Suit.HEARTS):
            board.add_mult(3)
        super().trigger_on_play_card(board)


class JokerWrathful(Joker):
    def __init__(self):
        super().__init__(name='Wrathful Joker')
        self.data.cost = 5

    def trigger_on_play_card(self, card: Card, board: BoardVision):
        if card.is_suit(Suit.SPADES):
            board.add_mult(3)
        super().trigger_on_play_card(board)


class JokerGluttonous(Joker):
    def __init__(self):
        super().__init__(name='Gluttonous Joker')
        self.data.cost = 5

    def trigger_on_play_card(self, card: Card, board: BoardVision):
        if card.is_suit(Suit.CLUBS):
            board.add_mult(3)
        super().trigger_on_play_card(board)


class JokerHangingChad(Joker):
    def __init__(self):
        super().__init__(name='Hanging Chad')
        self.data.cost = 4

    def get_card_retriggers(self, card: Card, board: BoardVision) -> int:
        if card == board.get_played_cards()[0]:
            return 2
        return 0


class JokerSeltzer(Joker):
    def __init__(self):
        super().__init__(name='Seltzer')
        self.data.cost = 6
        self.rarity = Rarity.UNCOMMON

    def get_card_retriggers(self, card: Card, board: BoardVision) -> int:
        return 1


class JokerDusk(Joker):
    def __init__(self):
        super().__init__(name='Dusk')
        self.data.cost = 6
        self.rarity = Rarity.UNCOMMON

    def get_card_retriggers(self, card: Card, board: BoardVision) -> int:
        if board.get_data().remaining_hands == 0:
            return 1
        return 0


class JokerSockAndBuskin(Joker):
    def __init__(self):
        super().__init__(name='Sock and Buskin')
        self.data.cost = 6

    def get_card_retriggers(self, card: Card, board: BoardVision) -> int:
        if board.get_evaluation_rules().is_face_card(card):
            return 1
        return 0


class JokerShortcut(Joker):
    def __init__(self):
        super().__init__(name='Shortcut')
        self.data.cost = 7
        self.rarity = Rarity.UNCOMMON

    def change_evaluation_rules(self, board: BoardVision) -> None:
        board.get_evaluation_rules().straight_skip = True


class JokerFourFingers(Joker):
    def __init__(self):
        super().__init__(name='Four Fingers')
        self.data.cost = 7
        self.rarity = Rarity.UNCOMMON

    def change_evaluation_rules(self, board: BoardVision):
        board.get_evaluation_rules().fingers = 4


class JokerPareidolia(Joker):
    def __init__(self):
        super().__init__(name='Pareidolia')
        self.data.cost = 5
        self.rarity = Rarity.UNCOMMON

    def change_evaluation_rules(self, board: BoardVision):
        board.get_evaluation_rules().all_face = True


class JokerPhotograph(Joker):
    def __init__(self):
        super().__init__(name='Photograph')
        self.data.cost = 5
        self.first_card: Card | None = None

    def trigger_on_start_hand(self, board: BoardVision) -> None:
        cards = board.get_played_cards()
        for card in cards:
            if board.get_evaluation_rules().is_face_card(card):
                self.first_card = card
                break
    
    def trigger_on_play_card(self, card: Card, board: BoardVision) -> None:
        if self.first_card and card == self.first_card:
            board.add_time_mult(2)

    def trigger_on_end_hand(self, board: BoardVision) -> None:
        self.first_card = None


    