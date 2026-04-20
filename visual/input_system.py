
import pygame
from pygame import Vector2, Rect

from core.event_bus import EventBus

from visual.definitions import CARD_SIZE
from visual.card_view import CardView
from visual.board_view import BoardView

from director.board_player import BoardPlayer

class InputSystem:
    def __init__(self, board_view: BoardView, board_player: BoardPlayer):
        self.board_view = board_view
        self.hovered: CardView = None
        self.player = board_player
    
    def handle_event(self, event) -> None:
        if event.type == pygame.MOUSEMOTION:
            self.hovered = None

            hover_test = self.board_view.hand_row.cards + self.board_view.played_row.cards + self.board_view.joker_row.cards

            for card in reversed(hover_test):
                rect = Rect(*(card.pos() - CARD_SIZE / 2), *CARD_SIZE)
                if(rect.collidepoint(event.pos)):
                    self.hovered = card
                    break
            
            for card in hover_test:
                card.is_hovered = self.hovered == card
        
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.hovered is not None:
                print(f"Clicked on card {self.hovered.id}")
                self.hovered.is_selected = not self.hovered.is_selected
                self.board_view.recalculate_positions()

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            self.player.play()
            self.player.flush_animation()
        
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
            self.player.discard()
            self.player.draw_cards()
            self.player.flush_animation()

                    