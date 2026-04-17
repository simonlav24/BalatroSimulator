

from typing import Protocol
from uuid import UUID

class CardProtocol(Protocol):
    def __init__(self):
        self.id: UUID


class DataRegistry:
    def __init__(self):
        self.cards: dict[UUID, CardProtocol] = {}
    
    def register(self, card: CardProtocol) -> None:
        self.cards[card.id] = card
    
    def __getitem__(self, key: UUID) -> CardProtocol:
        return self.cards[key]
