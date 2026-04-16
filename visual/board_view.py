

from typing import Protocol
from pygame import Vector2

from visual.layout import CardRow

win_size = (1280, 720)

class BoardView:
    def __init__(self, view_registry):
        self.view_registry = view_registry

        self.hand_row = CardRow(Vector2(win_size[0] / 2, 500), 400)
        # self.joker_row = CardRow(pos=..., width=...)

    def sync_with_board(self, board):
        self.hand_row.cards = [
            self.view_registry[card.id] for card in board.get_hand_cards()
        ]

        # self.joker_row.cards = [
        #     self.view_registry[cid] for cid in board.joker
        # ]

    def step(self):
        self.hand_row.recalc()
        self.hand_row.step()
        for card in self.hand_row.cards:
            card.step()
        