
from typing import Protocol, Any
import pygame

from core import Vector2, Rect
from core.event_bus import EventBus, GameEventPlay, GameEventDiscard, GameEventChangedOrder, GameEventChagnedSelection

from visual.definitions import CARD_SIZE, FPS
from visual.card_view import CardView
from visual.board_view import BoardView


class UIElement(Protocol):
    def __init__(self):
        self.is_hovered: bool = False
        self.is_pressed: bool = False
        self.rect: Rect = None
        self.event: Any = None
    
    def on_click(self): ...


class InputSystem:
    def __init__(self, board_view: BoardView, event_bus: EventBus):
        self.board_view = board_view
        self.dragged: CardView = None
        self.elements: list[UIElement] = []
        self.event_bus = event_bus

        self.hovered_card: CardView = None
        self.hovered_element: UIElement = None
        self.timer = 0

    def step(self):
        self.timer += 1
    
    def register_ui_element(self, ui_element: UIElement) -> None:
        self.elements.append(ui_element)
    
    def handle_event(self, event) -> None:
        if event.type == pygame.MOUSEMOTION:
            if self.dragged is not None:
                self.dragged.set_pos(Vector2(event.pos))
                self.board_view.on_dragging(self.dragged)
                return

            self.hovered_card = None

            hover_test = self.board_view.get_rows()

            for row in hover_test:
                for card in reversed(row.cards):
                    rect = Rect(*(card.pos() - CARD_SIZE / 2), *CARD_SIZE)
                    if rect.collidepoint(event.pos):
                        self.hovered_card = card
                        break
            
            for row in hover_test:
                for card in row.cards:
                    card.is_hovered = self.hovered_card == card
            
            self.hovered_element = None
            for element in self.elements:
                element.is_hovered = False
                if element.rect.collidepoint(event.pos):
                    element.is_hovered = True
                    self.hovered_element = element
        
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.hovered_card is not None:
                self.timer = 0
                self.dragged = self.hovered_card
                self.dragged.is_dragged = True
            
            elif self.hovered_element is not None:
                self.hovered_element.is_pressed = True
        
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if self.hovered_element is not None:
                self.hovered_element.is_pressed = False
                self.hovered_element.on_click()
                if self.hovered_element.event is not None:
                    self.event_bus.add_game_event(self.hovered_element.event)
            for element in self.elements:
                element.is_pressed = False

            if self.timer < FPS * 0.25 and self.hovered_card is not None:
                self.hovered_card.is_selected = not self.hovered_card.is_selected
                self.dragged.is_dragged = False
                self.dragged = None
                self.board_view.recalculate_positions()
                self.event_bus.add_game_event(GameEventChagnedSelection())
            
            elif self.dragged is not None:
                # drop dragged card
                self.dragged.is_dragged = False
                self.dragged = None
                self.hovered_card = None
                self.event_bus.add_game_event(GameEventChangedOrder())


        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            self.event_bus.add_game_event(GameEventPlay())
        
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
            self.event_bus.add_game_event(GameEventDiscard())

        elif event.type == pygame.USEREVENT:
            ...
                    