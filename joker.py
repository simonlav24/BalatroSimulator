
from typing import Protocol
from dataclasses import dataclass
from definitions import *
from card import Card

@dataclass
class JokerData:
    name: str
    cost: int = 0
    edition: Edition = Edition.BASE


class BoardVision(Protocol):
    def get_hand_cards(self) -> list[Card]: ...
    def get_jokers(self) -> list['Joker']: ...
    def add_mult(self, mult: float): ...
    def add_chips(self, chips: int): ...
    def add_time_mult(self, mult: float): ...
    def get_mode(self) -> ClacMode: ...


class Joker:
    def __init__(self, name: str):
        self.data = JokerData(name=name)
        self.active: bool = True
        self.rarity: Rarity = Rarity.COMMON
    
    def trigger_on_start_hand(self, board: BoardVision):
        ...

    def trigger_on_end_hand(self, board: BoardVision):
        # todo: evaluate edition
        ...
    
    def trigger_on_play_card(self, card: Card, board: BoardVision):
        ...
    
    def trigger_on_discard_cards(self, cards: list[Card], board: BoardVision):
        ...

    def change_evaluation_rules(self, rules: HandEvaluationRules):
        ...