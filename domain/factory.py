
from domain.definitions import *
from domain.card import Card, CardData
from domain.jokers import *

from core.event_bus import EventBus
from core.data_registry import DataRegistry

class Factory:
    def __init__(self, event_bus: EventBus=None, registry: DataRegistry=None):
        self.event_bus = event_bus
        if self.event_bus is None:
            self.event_bus = EventBus()
        
        self.registry = registry
        if self.registry is None:
            self.registry = DataRegistry()

    def card(self, rank: Rank, suit: Suit, enhancement: Enhancement=Enhancement.NONE, edition=Edition.BASE, seal=Seal.NONE):
        card = Card(CardData(rank, suit, enhancement, edition, seal), self.event_bus)
        self.registry.register(card)
        return card

    def joker(self, cls, edition: Edition=Edition.BASE):
        joker: Joker = cls(self.event_bus)
        self.registry.register(joker)
        joker.data.edition = edition
        return joker