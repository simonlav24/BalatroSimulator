
from typing import Protocol
from dataclasses import dataclass

from definitions import *
from card import Card
from evaluation_rules import EvaluationRules


@dataclass
class JokerData:
    name: str
    cost: int = 0
    edition: Edition = Edition.BASE


class BoardVision(Protocol):
    def get_hand_cards(self) -> list[Card]: ...
    def get_played_cards(self) -> list[Card]: ...
    def get_selected_cards(self) -> list[Card]: ...
    def get_jokers(self) -> list['Joker']: ...
    def add_mult(self, mult: float): ...
    def add_chips(self, chips: int): ...
    def add_time_mult(self, mult: float): ...
    def get_mode(self) -> ClacMode: ...
    def get_evaluation_rules(self) -> EvaluationRules: ...
    def get_data(self) -> BoardData: ...
    def get_full_deck(self) -> list[Card]: ...


class Joker:
    def __init__(self, name: str):
        self.data = JokerData(name=name)
        self.active: bool = True
        self.rarity: Rarity = Rarity.COMMON
    
    def trigger_on_start_hand(self, board: BoardVision) -> None:
        ...

    def trigger_on_end_hand(self, board: BoardVision) -> None:
        # todo: evaluate edition
        ...
    
    def trigger_on_play_card(self, card: Card, board: BoardVision) -> None:
        ...
    
    def trigger_on_discard_cards(self, cards: list[Card], board: BoardVision) -> None:
        ...

    def change_evaluation_rules(self, board: BoardVision) -> None:
        ...

    def get_card_retriggers(self, card: Card, board: BoardVision) -> int:
        return 0