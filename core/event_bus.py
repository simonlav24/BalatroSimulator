

from dataclasses import dataclass
from enum import Enum
from typing import Any

from core.id_gen import id_type
from domain.definitions import Edition, CardType

class BoardArea(Enum):
    HAND = 0
    PLAYED = 1
    JOKER = 2
    DISCARD = 3

###################################################
#  animation events
###################################################

@dataclass
class EventTriggerCard:
    id: int
    chips: float = 0
    mult: float = 0.0
    time_mult: float = 1.0
    custom_text: str = None
    halt: bool = True
    is_joker: bool = True

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
    board_area: BoardArea = BoardArea.HAND

@dataclass
class EventReorderCards:
    card_ids: list[id_type]
    board_area: BoardArea


###################################################
#  game events
###################################################

@dataclass
class GameEventPlay:
    is_handled: bool = False

@dataclass 
class GameEventDiscard:
    is_handled: bool = False

@dataclass 
class GameEventChangedOrder:
    is_handled: bool = False

@dataclass
class GameEventChagnedSelection:
    is_handled: bool = False

@dataclass
class GameEventEndHand:
    is_handled: bool = False

@dataclass
class GameEventEndRound:
    is_handled: bool = False

@dataclass
class GameEventUpdateScore:
    chips: int = 0
    mult: float = 0.0
    time_mult: float = 1.0
    absolute: bool = False
    hand_info: tuple[str, int] = (None, None)
    is_handled: bool = False



class EventBus:
    def __init__(self):
        self.round_queue = []
        self.game_events = []

    def add_event(self, event) -> None:
        self.round_queue.append(event)
    
    def add_game_event(self, event) -> None:
        self.game_events.append(event)

    def get_round_queue(self) -> list[Any]:
        events = self.round_queue
        self.round_queue = []
        return events

    def get_game_events(self) -> list[Any]:
        return self.game_events

    def step(self) -> None:
        self.game_events = [event for event in self.game_events if not event.is_handled]