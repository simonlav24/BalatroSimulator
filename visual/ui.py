
from typing import Any

import pygame
from pygame import Surface, Color


from core import Vector2, Rect
import visual.definitions as fonts
from visual.card_view import MotionVector

WHITE = (255, 255, 255)

def darker(color: Color) -> Color:
    return tuple(max(0, i - 60) for i in color)

class UIElement:
    def __init__(self, event: Any=None):
        self.event = event

class Button(UIElement):
    def __init__(self, rect: Rect, text: str, color: Color, event: Any=None):
        super().__init__(event)
        self.rect = Rect(rect)
        self.surf = fonts.fonts.small.render(text, False, WHITE)
        self.color = color

        self.is_hovered = False
        self.is_pressed = False
    
    def step(self) -> None:
        ...
    
    def draw(self, surf: Surface) -> None:
        color = self.color
        if self.is_hovered:
            color = darker(color)
        pos = Vector2(self.rect.topleft)
        if self.is_pressed:
            pos[1] += 15
        pygame.draw.rect(surf, color, (pos, self.rect.size), border_radius=7)
        surf.blit(self.surf, pos + Vector2(self.rect.size) / 2 - Vector2(self.surf.get_size()) / 2)


class Text(UIElement):
    def __init__(self, rect: Rect, text: str, text_color: Color, back_color: Color):
        super().__init__()
        self.rect = Rect(rect)
        self.text_color = text_color
        self.back_color = back_color
        self.update(text)
        self.angle = MotionVector(0)
        self.scale = MotionVector(1.0)
    
    def update(self, text: str) -> None:
        self.surf = fonts.fonts.small.render(text, False, WHITE)
    
    def step(self) -> None:
        self.angle.step()
        self.scale.step()

    def draw(self, surf: Surface) -> None:
        if self.back_color:
            pygame.draw.rect(surf, self.back_color, self.rect, border_radius=7)
        text_surf = pygame.transform.rotozoom(self.surf, self.angle(), self.scale())
        surf.blit(text_surf, self.rect.center - Vector2(text_surf.get_size()) / 2)