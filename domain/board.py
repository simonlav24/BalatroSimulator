


from domain.card import Card
from domain.joker import Joker
from domain.poker import asses_poker_hand
from domain.definitions import *
from domain.evaluation_rules import EvaluationRules


class Board:
    def __init__(self):
        self.data = BoardData()
        self.jokers: list[Joker] = []

        self.selected_cards: list[Card] = []
        self.played_cards: list[Card] = []
        self.hand_cards: list[Card] = []
        self.full_deck: list[Card] = []
        self.remaining_deck: list[Card] = []

        self.evaluation_rules = EvaluationRules()

        self.chips: int = 0
        self.mult: float = 1

        self.current_hand_type: HandType = HandType.HIGH_CARD
        self.levels: dict[HandType, dict[str, int]] = {hand_type: {'level': 1, 'played': 0} for hand_type in HandType}
        self.calc_mode: CalcMode = CalcMode.BEST

    def play_initialize(self):
        self.data.remaining_hands -= 1

        # handle evaluation rules
        self.evaluation_rules = EvaluationRules()
        for joker in self.jokers:
            joker.change_evaluation_rules(self)
        self.current_hand_type, self.played_cards = asses_poker_hand(self.selected_cards, self.evaluation_rules)

        self.levels[self.current_hand_type]['played'] += 1

        # add stone cards
        self.played_cards += [card for card in self.selected_cards if card not in self.played_cards and card.data.enhancement == Enhancement.STONE]
        
        if self.evaluation_rules.play_all_cards:
            self.played_cards = self.selected_cards
        
    def play(self) -> dict[str, int | float]:

        # start from hand type base level
        chips, mult = get_hand_level_chips_mult(self.current_hand_type, self.levels[self.current_hand_type]['level'])
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

        # trigger cards in hands
        for card in self.hand_cards:
            # calculate card triggers
            card_triggers = self.evaluate_card_triggers_in_hand(card)

            for _ in range(card_triggers):
                # trigger card
                card.trigger_in_hand_on_hand_end(self)

                # trigger jokers on hand card
                for joker in self.jokers:
                    joker.trigger_on_card_in_hand(card, self)

        # trigger jokers on end hand
        for joker in self.jokers:
            joker.trigger_on_end_hand(self)

        # trigger jokers editions
        for joker in self.jokers:
            joker.trigger_edition(self)

        # final calculation
        final_score = int(self.chips * self.mult)

        print(f'Played hand: {self.current_hand_type}')
        print(f'played_cards: {self.played_cards}')
        print(f'Chips: {self.chips}, Mult: {self.mult}')
        print(f'Score: {final_score}')
        return {'score': final_score, 'chips': self.chips, 'mult': self.mult}

    def get_initial_score(self, cards: list[Card]) -> tuple[str, int, float]:
        if len(cards) == 0:
            return (None, None), 0, 0.0
        hand_type, _ = asses_poker_hand(cards, self.evaluation_rules)
        hand_level = self.levels[hand_type]['level']
        chips, mult = get_hand_level_chips_mult(hand_type, hand_level)
        return (hand_type, hand_level), chips, mult

    def play_test(self) -> dict[str, int | float]:
        self.play_initialize()
        return self.play()

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
    
    def get_mode(self) -> CalcMode:
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
    
    def evaluate_card_triggers_in_hand(self, card: Card) -> int:
        # debuffed might go here
        triggers = 1
        if card.data.seal == Seal.RED:
            triggers += 1
        for joker in self.jokers:
            triggers += joker.get_hand_card_retriggers(card, self)
        return triggers

    def get_full_deck(self) -> list[Card]:
        return self.full_deck
    
    def get_levels_table(self) -> dict[HandType, dict[str, int]]:
        return self.levels

    def get_current_hand_type(self) -> HandType:
        return self.current_hand_type
    
