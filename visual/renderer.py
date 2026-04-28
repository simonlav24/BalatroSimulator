
from math import degrees
from pygame import Surface

from domain.card import CardData

from visual.definitions import *
from visual.board_view import BoardView
from visual.view_registry import ViewRegistry
from visual.input_system import InputSystem
from visual.card_view import CardView
from visual.layout import CardRow
from visual.animation_system import AnimationSystem


def create_card_surf(data: CardData) -> Surface:
    # back
    card_surf = card_surf_at(card_backs_texture, *enhancement_map[data.enhancement])
    # image
    card_surf.blit(rank_suit_at(data.rank, data.suit))

    if data.seal != Seal.NONE:
        card_surf.blit(card_surf_at(card_backs_texture, *seal_map[data.seal]))

    return card_surf


def create_joker_surf(name: str) -> Surface:
    return card_surf_at(jokers_texture, *jokers_map[name])


def draw_card(card: CardView, surf: Surface):
    transformed = pygame.transform.rotozoom(card.surf, degrees(card.angle()), card.scale())
    surf.blit(transformed, card.pos() - Vector2(transformed.get_size()) / 2)

def draw_row_debug(row: CardRow, surf: Surface) -> None:
    pygame.draw.circle(surf, (255,0,0), row.pos, 2)
    pygame.draw.line(surf, (255,0,0), row.pos - Vector2(row.width / 2, 0), row.pos + Vector2(row.width / 2, 0))


class Renderer:
    def __init__(self, board_view: BoardView, view_reg: ViewRegistry, input_system: InputSystem):
        self.board = board_view
        self.view_reg = view_reg
        self.input_system = input_system
        self.ui_layer = None

        self.systems = []

    def register_system(self, system) -> None:
        self.systems.append(system)

    def draw(self, win: Surface) -> None:
        # draw ui
        if self.ui_layer:
            self.ui_layer.draw(win)

        # draw cards
        for row in self.board.rows:
            draw_row_debug(row, win)
            for card in row.cards:
                draw_card(card, win)
        
        # redraw dragged card
        if self.input_system.dragged is not None:
            draw_card(self.input_system.dragged, win)
        
        # draw systems
        for system in self.systems:
            system.draw(win)

