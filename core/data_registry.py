

from typing import Protocol
from core.id_gen import id_type

class CardProtocol(Protocol):
    def __init__(self):
        self.id: id_type


class DataRegistry:
    def __init__(self):
        self.cards: dict[id_type, CardProtocol] = {}
    
    def register(self, card: CardProtocol) -> None:
        self.cards[card.id] = card
    
    def __getitem__(self, key: id_type) -> CardProtocol:
        return self.cards[key]
