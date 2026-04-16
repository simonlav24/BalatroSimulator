
import pygame
from pygame import Vector2, Rect

from visual.definitions import CARD_SIZE
from visual.card_view import CardView
from visual.board_view import BoardView

class InputSystem:
    def __init__(self, board_view: BoardView):
        self.board_view = board_view
        self.hovered: CardView
    
    def handle_event(self, event) -> None:
        if event.type == pygame.MOUSEMOTION:
            self.hovered = None

            for card in reversed(self.board_view.hand_row.cards):
                rect = Rect(*(card.pos() - CARD_SIZE / 2), *CARD_SIZE)
                if(rect.collidepoint(event.pos)):
                    self.hovered = card
                    break
            
            for card in self.board_view.hand_row.cards:
                card.is_hovered = self.hovered == card
        
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.hovered is not None:
                # self.hovered.nudge(0.5)
                self.hovered.is_selected = not self.hovered.is_selected

                    