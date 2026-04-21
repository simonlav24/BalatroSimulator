
import pygame
from pygame import Vector2, Rect

from core.event_bus import EventBus

from visual.definitions import CARD_SIZE, FPS
from visual.card_view import CardView
from visual.board_view import BoardView

from director.board_player import BoardPlayer

class InputSystem:
    def __init__(self, board_view: BoardView, board_player: BoardPlayer):
        self.board_view = board_view
        self.hovered: CardView = None
        self.dragged: CardView = None
        self.player = board_player

        self.timer = 0

    def step(self):
        self.timer += 1
    
    def handle_event(self, event) -> None:
        if event.type == pygame.MOUSEMOTION:
            if self.dragged is not None:
                self.dragged.set_pos(Vector2(event.pos))
                return

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
                self.timer = 0
                self.dragged = self.hovered
                self.dragged.is_dragged = True
        
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if self.dragged is not None:
                self.board_view.recalculate_positions()
                self.dragged.is_dragged = False
                self.dragged = None
                self.hovered = None
            if self.timer < FPS * 0.25 and self.hovered is not None:
                self.hovered.is_selected = not self.hovered.is_selected
                self.board_view.recalculate_positions()

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            self.player.play()
            self.player.flush_animation()
        
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
            self.player.discard()
            self.player.draw_cards()
            self.player.flush_animation()

                    