
from typing import Any

import pygame
from pygame import Surface, Color


from core import Vector2, Rect
import visual.definitions as fonts


WHITE = (255, 255, 255)

def darker(color: Color) -> Color:
    return tuple(max(0, i - 60) for i in color)

class Button:
    def __init__(self, rect: Rect, text: str, color: Color, event: Any=None):
        self.rect = Rect(rect)
        self.surf = fonts.fonts.small.render(text, False, WHITE)
        self.color = color

        self.is_hovered = False
        self.is_pressed = False

        self.event = event
    
    def draw(self, surf: Surface) -> None:
        color = self.color
        if self.is_hovered:
            color = darker(color)
        pos = Vector2(self.rect.topleft)
        if self.is_pressed:
            pos[1] += 15
        pygame.draw.rect(surf, color, (pos, self.rect.size), border_radius=7)
        surf.blit(self.surf, pos + Vector2(self.rect.size) / 2 - Vector2(self.surf.get_size()) / 2)
    
    def on_click(self) -> None:
        ...


class Text:
    def __init__(self, rect: Rect, text: str, color: Color):
        self.rect = Rect(rect)
        self.color = color
        self.update(text)
    
    def update(self, text: str) -> None:
        self.surf = fonts.fonts.small.render(text, False, WHITE)

    def draw(self, surf: Surface) -> None:
        pygame.draw.rect(surf, self.color, self.rect, border_radius=7)
        surf.blit(self.surf, self.rect.center - Vector2(self.surf.get_size()) / 2)