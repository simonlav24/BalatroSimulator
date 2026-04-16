

from typing import Protocol
from uuid import UUID

class CardProtocol(Protocol):
    def __init__(self):
        self.id: UUID


class DataRegistry:
    def __init__(self):
        self.cards = {}
    
    def register(self, card: CardProtocol) -> None:
        self.cards[card.id] = card
    
    def get(self, id: UUID) -> CardProtocol:
        return self.cards[id]