

from typing import Protocol
from pygame import Vector2

from domain.board import Board
from core.data_registry import DataRegistry

from visual.definitions import win_size
from visual.layout import CardRow
from visual.view_registry import ViewRegistry



class BoardView:
    def __init__(self, view_reg: ViewRegistry, data_reg: DataRegistry):
        self.view_reg = view_reg
        self.data_reg = data_reg

        self.hand_row = CardRow(Vector2(win_size[0] / 2, 500), 400)
        self.played_row = CardRow(Vector2(win_size[0] / 2, 300), 400)
        self.joker_row = CardRow(Vector2(win_size[0] / 2, 100), 400)

        self.discard_pile = CardRow(Vector2(win_size[0] + 50, 300), 0)
        self.rows = [self.hand_row, self.played_row, self.joker_row, self.discard_pile]

    def recalculate_positions(self):
        for row in self.rows:
            row.recalc()

    def step(self):
        for row in self.rows:
            row.step()
            for card in row.cards:
                card.step()

        