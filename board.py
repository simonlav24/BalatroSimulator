

from dataclasses import dataclass
from card import Card
from joker import Joker
from poker import asses_poker_hand
from definitions import *
from evaluation_rules import EvaluationRules


class Board:
    def __init__(self):
        self.data = BoardData()
        self.hand_cards: list[Card] = []
        self.selected_cards: list[Card] = []
        self.played_cards: list[Card] = []
        self.jokers: list[Joker] = []
        self.deck: list[Card] = []
        self.evaluation_rules = EvaluationRules()

        self.chips: int = 0
        self.mult: float = 1

        self.current_hand_type: HandType = HandType.HIGH_CARD
        self.levels: dict[HandType, int] = {hand_type: 1 for hand_type in HandType}
        self.calc_mode: ClacMode = ClacMode.BEST

    def play(self):
        self.data.remaining_hands -= 1

        # handle evaluation rules
        self.evaluation_rules = EvaluationRules()
        for joker in self.jokers:
            joker.change_evaluation_rules(self)
        self.current_hand_type, self.played_cards = asses_poker_hand(self.selected_cards, self.evaluation_rules)

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
    
    def get_played_cards(self) -> list[Card]:
        return self.played_cards

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
    
    def get_evaluation_rules(self) -> EvaluationRules:
        return self.evaluation_rules
    
    def get_data(self) -> BoardData:
        return self.data

    def get_selected_cards(self) -> list[Card]:
        return self.selected_cards

    def evaluate_card_triggers_played(self, card: Card) -> int:
        # debuffed might go here
        triggers = 1
        if card.data.seal == Seal.RED:
            triggers += 1
        for joker in self.jokers:
            triggers += joker.get_card_retriggers(card, self)
        return triggers

    def get_full_deck(self) -> list[Card]:
        return self.deck
