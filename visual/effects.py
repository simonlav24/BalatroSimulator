
from pygame import Color, Surface
import pygame

from core.utils import Vector2
from core.event_bus import EventTriggerCard
import visual.definitions as fonts
from visual.definitions import FPS, Colors, CARD_SIZE
from visual.view_registry import ViewRegistry
from visual.card_view import CardView

SHAPE_BASE = 50
get_shape = lambda x, pos: [
    Vector2(-x, 0) + pos,
    Vector2(0, x) + pos,
    Vector2(x, 0) + pos,
    Vector2(0, -x) + pos,
]

def scale_formula(x: float, fin_time: float):
    return - (4 / fin_time**2) * x**2 + (4 / fin_time) * x



class TriggerEffect:
    def __init__(self, text: str, color: Color, card: CardView, is_joker=True, fin_time=FPS * 0.4):
        self.card = card
        self.color = color
        self.time = 0
        self.is_done = False
        self.surf = fonts.fonts.medium.render(text, False, Colors.WHITE)
        self.scale = 0.0
        self.fin_time = fin_time
        self.pos_offset = Vector2(0, CARD_SIZE[1] / 2) if is_joker else Vector2(0, -CARD_SIZE[1] / 2)

    def step(self) -> None:
        self.time += 1
        self.scale = scale_formula(self.time, self.fin_time)
        if self.time >= self.fin_time:
            self.is_done = True

    def draw(self, win: Surface) -> None:
        pos = self.card.pos() + self.pos_offset
        pygame.draw.polygon(win, self.color, get_shape(self.scale * SHAPE_BASE, pos))
        surf = pygame.transform.scale_by(self.surf, self.scale)
        win.blit(surf, pos - Vector2(surf.get_size()) / 2)


def create_trigger_effect(event: EventTriggerCard, reg: ViewRegistry, time_skew: float) -> TriggerEffect:
    text = None
    color = None
    if event.chips > 0:
        text = f'+{event.chips}'
        color = Colors.BLUE
    elif event.mult > 0:
        text = f'+{event.mult} mult'
        color = Colors.RED
    elif event.time_mult > 1.0:
        text = f'x{event.time_mult} mult'
        color = Colors.PURPLE
    elif event.custom_text:
        text = event.custom_text
        color = Colors.YELLOW
    if text == None:
        return None
    return TriggerEffect(text, color, reg[event.id], event.is_joker, FPS * 0.4 * time_skew)

