

from domain.definitions import Rank, Suit, Enhancement, Edition, Seal
from domain.card import CardData, Card

from core.event_bus import EventBus
from core.data_registry import DataRegistry

from visual.view_registry import ViewRegistry
from visual.card_view import CardView
from visual.renderer import create_card_surf, create_joker_surf

class CardFactory:
    def __init__(self, data_registry: DataRegistry, event_bus: EventBus, view_registry: ViewRegistry):
        self.data_registry = data_registry
        self.event_bus = event_bus
        self.view_registry = view_registry
    
    def create_playing_card(self, rank: Rank, suit: Suit, enhancement: Enhancement=Enhancement.NONE, edition=Edition.BASE, seal=Seal.NONE):
        card = Card(CardData(rank, suit, enhancement, edition, seal), self.event_bus)
        self.data_registry.register(card)

        surf = create_card_surf(card.data.rank, card.data.suit, card.data.enhancement, card.data.seal, card.data.edition)
        card_view = CardView(card.id, surf)
        self.view_registry.register(card_view)
        return card
    
    def create_joker_card(self, joker_cls, edition: Edition=Edition.BASE):
        joker: Card = joker_cls(self.event_bus)
        self.data_registry.register(joker)
        joker.data.edition = edition
        
        surf = create_joker_surf(joker.data.name)
        card_view = CardView(joker.id, surf)
        self.view_registry.register(card_view)
        return joker