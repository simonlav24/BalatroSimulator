
from dataclasses import dataclass
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

class EventBus:
    def __init__(self):
        self.queue = []

    def add_event(self, event):
        self.queue.append(event)

    def drain(self):
        events = self.queue
        self.queue = []
        return events