
from math import cos, sin
import time

import pygame
from pygame import Vector2, Surface

from visual.card_view import CardView

def flow(x: float) -> float:
    return 0.5 * (0.2 * sin(time.perf_counter() * 0.3 + 0.01 * x) + 
                  0.05 * cos(-time.perf_counter() * 1.2 + 0.02 * x) +
                  0.05 * sin(time.perf_counter() * 3 + 0.08 * x))

def spread(x: float, l: int) -> float:
    return - 2 * (0.2 / l) * (x - l) - 0.2

class CardRow:
    def __init__(self, pos, width):
        self.pos = pos
        self.width = width
        self.cards: list[CardView] = []

    def recalc(self) -> None:
        if len(self.cards) == 1:
            x = self.width / 2
            spacing = 0
        else:
            spacing = self.width / (len(self.cards) - 1)
            x = 0

        for card in self.cards:
            pos = self.pos + Vector2(-self.width / 2 + x, 0)
            if card.is_selected:
                pos[1] -= 30
            card.set_pos(pos)
            x += spacing
    
    def step(self) -> None:
        for i, card in enumerate(self.cards):
            angle = spread(i, len(self.cards))
            angle += flow(card.pos().x)
            card.angle.set(angle)

    def draw(self, win: Surface) -> None:
        pygame.draw.circle(win, (255,0,0), self.pos, 2)
        pygame.draw.line(win, (255,0,0), self.pos - Vector2(self.width / 2, 0), self.pos + Vector2(self.width / 2, 0))
