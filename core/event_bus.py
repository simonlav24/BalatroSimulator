

from dataclasses import dataclass
from uuid import UUID

from domain.definitions import Edition


@dataclass
class TriggerCard:
    id: int
    chips: float = 0
    mult: float = 0
    time_mult: float = 0

@dataclass
class TriggerEdition:
    id: int
    edition: Edition

@dataclass
class EventSelectCardsForPlay:
    card_ids: list[UUID]

@dataclass
class EventPlayHand:
    ...


class EventBus:
    def __init__(self):
        self.game_queue = []
        self.round_queue = []

    def add_event(self, event):
        self.round_queue.append(event)
    
    def add_game_event(self, event):
        self.game_queue.append(event)

    def get_game_queue(self):
        events = self.game_queue
        self.game_queue = []
        return events

    def get_round_queue(self):
        events = self.round_queue
        self.round_queue = []
        return events