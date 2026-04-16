
from typing import Protocol
from dataclasses import dataclass
from math import floor
from uuid import uuid4

from domain.definitions import *
from domain.card import Card
from domain.evaluation_rules import EvaluationRules

from core.event_bus import EventBus


@dataclass
class JokerData:
    name: str
    cost: int = 0
    extra_value: int = 0
    edition: Edition = Edition.BASE


class BoardVision(Protocol):
    def get_hand_cards(self) -> list[Card]: ...
    def get_played_cards(self) -> list[Card]: ...
    def get_selected_cards(self) -> list[Card]: ...
    def get_jokers(self) -> list['Joker']: ...
    def add_mult(self, mult: float) -> None: ...
    def add_chips(self, chips: int) -> None: ...
    def add_time_mult(self, mult: float) -> None: ...
    def get_mode(self) -> CalcMode: ...
    def get_evaluation_rules(self) -> EvaluationRules: ...
    def get_data(self) -> BoardData: ...
    def get_full_deck(self) -> list[Card]: ...
    def get_levels_table(self) -> dict[HandType, dict[str, int]]: ...
    def get_current_hand_type(self) -> HandType: ...


class Joker:
    def __init__(self, name: str, event_bus: EventBus):
        self.data = JokerData(name=name)
        self.id = uuid4()
        self.active: bool = True
        self.rarity: Rarity = Rarity.COMMON
        self.event_bus = event_bus
    
    def __repr__(self):
        return self.data.name

    def trigger_on_start_hand(self, board: BoardVision) -> None:
        ...

    def trigger_on_end_hand(self, board: BoardVision) -> None:
        ...
    
    def trigger_on_play_card(self, card: Card, board: BoardVision) -> None:
        ...
    
    def trigger_on_card_in_hand(self, card: Card, board: BoardVision) -> None:
        ...
    
    def trigger_on_discard_cards(self, cards: list[Card], board: BoardVision) -> None:
        ...

    def change_evaluation_rules(self, board: BoardVision) -> None:
        ...

    def get_card_retriggers(self, card: Card, board: BoardVision) -> int:
        return 0
    
    def get_hand_card_retriggers(self, card: Card, board: BoardVision) -> int:
        return 0
    
    def trigger_on_end_round(self, board: BoardVision) -> None:
        ...
    
    def trigger_edition(self, board: BoardVision) -> None:
        if self.data.edition == Edition.FOIL:
            board.add_chips(50)
        elif self.data.edition == Edition.HOLOGRAPHIC:
            board.add_mult(10)
        elif self.data.edition == Edition.POLYCHROME:
            board.add_time_mult(1.5)
    
    def on_discard(self, card_discarded: Card, board: BoardVision) -> None:
        ...
    
    def on_sell(self, board: BoardVision) -> None:
        ...
    
    def on_added_card(self, board: BoardVision) -> None:
        ...
    
    def on_blind_selected(self, board: BoardVision) -> None:
        ...
    
    def get_sell_value(self, board: BoardVision) -> int:
        buy_cost = floor((self.data.cost + edition_cost[self.data.edition]) * board.get_data().discount_percent)
        sell_cost = floor(buy_cost / 2)
        return sell_cost


class JokerCopier(Joker):
    def __init__(self, name: str, event_bus: EventBus):
        super().__init__(name=name, event_bus=event_bus)
        self.data.cost = 10
        self.rarity = Rarity.RARE
        self.copied_joker: Joker = Joker('dummy', event_bus=event_bus)

    def trigger_on_start_hand(self, board: BoardVision) -> None:
        self.copied_joker.trigger_on_start_hand(board)

    def trigger_on_end_hand(self, board: BoardVision) -> None:
        self.copied_joker.trigger_on_end_hand(board)
    
    def trigger_on_play_card(self, card: Card, board: BoardVision) -> None:
        self.copied_joker.trigger_on_play_card(card, board)
    
    def trigger_on_card_in_hand(self, card: Card, board: BoardVision) -> None:
        self.copied_joker.trigger_on_card_in_hand(card, board)
    
    def trigger_on_discard_cards(self, cards: list[Card], board: BoardVision) -> None:
        self.copied_joker.trigger_on_discard_cards(cards, board)

    def get_card_retriggers(self, card: Card, board: BoardVision) -> int:
        return self.copied_joker.get_card_retriggers(card, board)
    
    def get_hand_card_retriggers(self, card: Card, board: BoardVision) -> int:
        return self.copied_joker.get_hand_card_retriggers(card, board)