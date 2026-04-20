

from dataclasses import dataclass

from core.id_gen import id_type
from domain.definitions import Edition


@dataclass
class EventTriggerCard:
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
    card_ids: list[id_type]

@dataclass
class EventDeselect:
    card_ids: list[id_type]

@dataclass
class EventStartPlay:
    card_ids: list[id_type]

@dataclass
class EventClearOut:
    ...

@dataclass
class EventDiscardCard:
    card_id: id_type

@dataclass 
class EventDrawCard:
    card_id: id_type
    drawn_index: int = -1


class EventBus:
    def __init__(self):
        self.round_queue = []

    def add_event(self, event):
        self.round_queue.append(event)

    def get_round_queue(self):
        events = self.round_queue
        self.round_queue = []
        return events