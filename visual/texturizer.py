

from core.data_registry import DataRegistry
from domain.card import CardData
from domain.definitions import Enhancement, Seal
from visual.view_registry import ViewRegistry
from visual.renderer import create_card_surf

class CardTexturizer:
    def __init__(self, data_reg: DataRegistry, view_reg: ViewRegistry):
        self.data_reg = data_reg
        self.view_reg = view_reg

    def retexture_enhancement(self, id: int, enhancement: Enhancement) -> None:
        card_data: CardData = self.data_reg[id].data
        card_view = self.view_reg[id]
        card_view.surf = create_card_surf(card_data.rank, card_data.suit, enhancement, card_data.seal, card_data.edition)