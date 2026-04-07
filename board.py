

from dataclasses import dataclass
from card import Card
from joker import Joker
from poker import asses_poker_hand
from definitions import *

@dataclass
class BoardData:
    hand_size: int = 8
    hands_play: int = 4
    hands_discard: int = 3


class Board:
    def __init__(self):
        self.BoardData = BoardData()
        self.hand_cards: list[Card] = []
        self.selected_cards: list[Card] = []
        self.played_cards: list[Card] = []
        self.jokers: list[Joker] = []

        self.chips: int = 0
        self.mult: float = 1

        self.current_hand_type: HandType = HandType.HIGH_CARD
        self.levels: dict[HandType, int] = {hand_type: 1 for hand_type in HandType}
        self.calc_mode: ClacMode = ClacMode.BEST

    def play(self):
        # handle evaluation rules
        evaluation_rules = HandEvaluationRules()
        for joker in self.jokers:
            joker.change_evaluation_rules(evaluation_rules)
        self.current_hand_type, self.played_cards = asses_poker_hand(self.selected_cards, evaluation_rules)

        # start from hand type base level
        chips, mult = get_hand_level_chips_mult(self.current_hand_type, self.levels[self.current_hand_type])
        self.chips = chips
        self.mult = mult

        # trigger jokers on start hand
        for joker in self.jokers:
            joker.trigger_on_start_hand(self)

        for card in self.played_cards:
            # calculate card triggers
            card_triggers = self.evaluate_card_triggers_played(card)

            for _ in range(card_triggers):
                # trigger card
                card.trigger_on_play(self)

                # trigger jokers on play card
                for joker in self.jokers:
                    joker.trigger_on_play_card(card, self)

        # trigger jokers on end hand
        for joker in self.jokers:
            joker.trigger_on_end_hand(self)

        # final calculation
        final_chips_best = int(self.chips * self.mult)

        print(f'Played hand: {self.current_hand_type}')
        print(f'Score: {final_chips_best}')


    def get_hand_cards(self) -> list[Card]:
        return self.hand_cards

    def get_jokers(self) -> list['Joker']:
        return self.jokers
    
    def add_mult(self, mult: float):
        self.mult += mult

    def add_chips(self, chips: int):
        self.chips += chips

    def add_time_mult(self, mult: float):
        self.mult *= mult
    
    def get_mode(self) -> ClacMode:
        return self.calc_mode

    def evaluate_card_triggers_played(self, card: Card):
        # debuffed might go here
        base = 1
        if card.data.seal == Seal.RED:
            base += 1
        return base