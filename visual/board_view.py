

from typing import Protocol
from pygame import Vector2

from domain.board import Board
from core.data_registry import DataRegistry

from visual.card_view import CardView
from visual.layout import CardRow
from visual.view_registry import ViewRegistry


win_size = (1280, 720)

class BoardView:
    def __init__(self, view_reg: ViewRegistry, data_reg: DataRegistry):
        self.view_reg = view_reg
        self.data_reg = data_reg

        self.hand_row = CardRow(Vector2(win_size[0] / 2, 500), 400)
        self.played_row = CardRow(Vector2(win_size[0] / 2, 300), 400)
        self.joker_row = CardRow(Vector2(win_size[0] / 2, 100), 400)

    def sync_to_board(self, board: Board, selected_cards: list[CardView]):
        board.selected_cards = [
            self.data_reg[card.id] for card in selected_cards
        ]
        board.hand_cards = [
            self.data_reg[card.id] for card in self.hand_row.cards
        ]
        board.jokers = [
            self.data_reg[card.id] for card in self.joker_row.cards
        ]

    def sync_with_board(self, board: Board):
        self.hand_row.cards = [
            self.view_reg[card.id] for card in board.get_hand_cards()
        ]
        self.played_row.cards = [
            self.view_reg[card.id] for card in board.get_selected_cards()
        ]
        self.joker_row.cards = [
            self.view_reg[card.id] for card in board.get_jokers()
        ]

    def step(self):
        for row in [self.hand_row, self.played_row, self.joker_row]:
            row.recalc()
            row.step()
            for card in row.cards:
                card.step()

        