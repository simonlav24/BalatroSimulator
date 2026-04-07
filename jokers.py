


from joker import Joker, BoardVision
from card import Card
from definitions import *


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


class JokerHalfJoker(Joker):
    def __init__(self):
        super().__init__(name='Half Joker')
        self.data.cost = 5

    def trigger_on_end_hand(self, board: BoardVision):
        if len(board.get_selected_cards()) <= 3:
            board.add_mult(20)
        super().trigger_on_end_hand(board)


class JokerCeremonialDagger(Joker):
    def __init__(self):
        super().__init__(name='Ceremonial Dagger')
        self.data.cost = 6
        self.mult = 0

    def trigger_on_end_hand(self, board: BoardVision):
        board.add_mult(self.mult)
        super().trigger_on_end_hand(board)


class JokerBanner(Joker):
    def __init__(self):
        super().__init__(name='Banner')
        self.data.cost = 5

    def trigger_on_end_hand(self, board: BoardVision):
        board.add_chips(board.get_data().remaining_discards * 30)
        super().trigger_on_end_hand(board)


class JokerMysticSummit(Joker):
    def __init__(self):
        super().__init__(name='Mystic Summit')
        self.data.cost = 5

    def trigger_on_end_hand(self, board: BoardVision):
        if board.get_data().remaining_discards == 0:
            board.add_mult(15)
        super().trigger_on_end_hand(board)


class JokerMisprint(Joker):
    def __init__(self):
        super().__init__(name='Misprint')
        self.data.cost = 4

    def trigger_on_end_hand(self, board: BoardVision):
        if board.get_mode() == ClacMode.BEST:
            board.add_mult(23)
        super().trigger_on_end_hand(board)


class JokerDusk(Joker):
    def __init__(self):
        super().__init__(name='Dusk')
        self.data.cost = 6
        self.rarity = Rarity.UNCOMMON

    def get_card_retriggers(self, card: Card, board: BoardVision) -> int:
        if board.get_data().remaining_hands == 0:
            return 1
        return 0


class JokerRaisedFist(Joker):
    def __init__(self):
        super().__init__(name='RaisedFist')
        self.data.cost = 5

    def trigger_on_end_hand(self, board: BoardVision):
        cards = [card for card in board.get_hand_cards() if card.get_rank() != Rank.NONE]
        cards.sort(key=lambda x: x.get_rank().value)
        board.add_mult(2 * base_value_map[cards[0].get_rank()])
        super().trigger_on_end_hand(board)


class JokerChaosTheClown(Joker):
    def __init__(self):
        super().__init__(name='Chaos the Clown')
        self.data.cost = 4


class JokerFibonacci(Joker):
    def __init__(self):
        super().__init__(name='Fibonacci')
        self.data.cost = 8
        self.rarity = Rarity.UNCOMMON

    def trigger_on_play_card(self, card: Card, board: BoardVision):
        if card.get_rank() in [Rank.TWO, Rank.THREE, Rank.FIVE, Rank.EIGHT, Rank.ACE]:
            board.add_mult(8)
        super().trigger_on_play_card(board)


class JokerSteelJoker(Joker):
    def __init__(self):
        super().__init__(name='Steel Joker')
        self.data.cost = 7
        self.rarity = Rarity.UNCOMMON

    def trigger_on_end_hand(self, board: BoardVision):
        mult = 0.2 * sum([card for card in board.get_full_deck() if card.data.enhancement == Enhancement.STEEL])
        board.add_time_mult(mult)
        super().trigger_on_end_hand(board)


class JokerScaryFace(Joker):
    def __init__(self):
        super().__init__(name='Scary Face')
        self.data.cost = 4

    def trigger_on_play_card(self, card: Card, board: BoardVision):
        if board.get_evaluation_rules().is_face_card(card):
            board.add_chips(30)


class JokerAbstractJoker(Joker):
    def __init__(self):
        super().__init__(name='Abstract Joker')
        self.data.cost = 4

    def trigger_on_end_hand(self, board: BoardVision):
        mult = 3 * len(board.get_jokers())
        board.add_mult(mult)
        super().trigger_on_end_hand(board)


class JokerDelayedGratification(Joker):
    def __init__(self):
        super().__init__(name='Delayed Gratification')
        self.data.cost = 4


class JokerHack(Joker):
    def __init__(self):
        super().__init__(name='Hack')
        self.data.cost = 6
        self.rarity = Rarity.UNCOMMON

    def get_card_retriggers(self, card: Card, board: BoardVision) -> int:
        if card.get_rank() in [Rank.TWO, Rank.THREE, Rank.FOUR, Rank.FIVE]:
            return 1
        return 0


class JokerPareidolia(Joker):
    def __init__(self):
        super().__init__(name='Pareidolia')
        self.data.cost = 5
        self.rarity = Rarity.UNCOMMON

    def change_evaluation_rules(self, board: BoardVision):
        board.get_evaluation_rules().all_face = True


class JokerGrosMichel(Joker):
    def __init__(self):
        super().__init__(name='Gros Michel')
        self.data.cost = 5

    def trigger_on_end_hand(self, board: BoardVision):
        board.add_mult(15)
        super().trigger_on_end_hand(board)


class JokerEvenSteven(Joker):
    def __init__(self):
        super().__init__(name='Even Steven')
        self.data.cost = 4

    def trigger_on_play_card(self, card: Card, board: BoardVision):
        if card.get_rank() in [Rank.TWO, Rank.FOUR, Rank.SIX, Rank.EIGHT, Rank.TEN]:
            board.add_mult(4)
        super().trigger_on_play_card(board)


class JokerOddTodd(Joker):
    def __init__(self):
        super().__init__(name='Odd Todd')
        self.data.cost = 4

    def trigger_on_play_card(self, card: Card, board: BoardVision):
        if card.get_rank() in [Rank.ACE, Rank.THREE, Rank.FIVE, Rank.SEVEN, Rank.NINE]:
            board.add_chips(31)
        super().trigger_on_play_card(board)


class JokerScholar(Joker):
    def __init__(self):
        super().__init__(name='Scholar')
        self.data.cost = 4

    def trigger_on_play_card(self, card: Card, board: BoardVision):
        if card.get_rank() == Rank.ACE:
            board.add_chips(20)
            board.add_mult(4)
        super().trigger_on_play_card(board)


class JokerBusinessCard(Joker):
    def __init__(self):
        super().__init__(name='Business Card')
        self.data.cost = 4


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


    