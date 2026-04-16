
from uuid import UUID

from visual.card_view import CardView

class ViewRegistry:
    def __init__(self):
        self.cards: dict[UUID, CardView] = {}
    
    def register(self, card: CardView) -> None:
        self.cards[card.id] = card
        
    def values(self) -> list[CardView]:
        return list(self.cards.values())
    
    def __getitem__(self, key):
        return self.cards[key]