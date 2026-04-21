
from math import cos, sin
import time

import pygame
from pygame import Vector2, Surface

from core.id_gen import id_type
from visual.card_view import CardView

def flow(x: float) -> float:
    return 0.5 * (0.2 * sin(time.perf_counter() * 0.3 + 0.01 * x) + 
                  0.05 * cos(-time.perf_counter() * 1.2 + 0.02 * x) +
                  0.05 * sin(time.perf_counter() * 3 + 0.08 * x))

def spread(x: float, l: int) -> float:
    return - 2 * (0.15 / l) * (x - l) - 0.15

class CardRow:
    def __init__(self, pos, width):
        self.pos = pos
        self.width = width
        self.cards: list[CardView] = []

    def add(self, card: CardView, index: int=-1) -> None:
        if index == -1:
            self.cards.append(card)
        else:
            self.cards.insert(index, card)
    
    def remove(self, card: CardView) -> None:
        self.cards.remove(card)

    def recalc(self) -> None:
        if len(self.cards) == 1:
            x = self.width / 2
            spacing = 0
        else:
            spacing = self.width / (len(self.cards) - 1)
            x = 0

        for card in self.cards:
            if card.is_dragged:
                x += spacing
                continue
            pos = self.pos + Vector2(-self.width / 2 + x, 0)
            if card.is_selected:
                pos[1] -= 30
            card.set_pos(pos)
            x += spacing

    def get_selected(self) -> list[id_type]:
        return [card.id for card in self.cards if card.is_selected]

    def step(self) -> None:
        for i, card in enumerate(self.cards):
            angle = spread(i, len(self.cards))
            angle += flow(card.pos().x)
            card.angle.set(angle)

    def draw(self, win: Surface) -> None:
        pygame.draw.circle(win, (255,0,0), self.pos, 2)
        pygame.draw.line(win, (255,0,0), self.pos - Vector2(self.width / 2, 0), self.pos + Vector2(self.width / 2, 0))
