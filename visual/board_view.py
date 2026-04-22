

from typing import Protocol

from domain.board import Board
from core.data_registry import DataRegistry
from core import Vector2

from visual.definitions import win_size
from visual.layout import CardRow
from visual.view_registry import ViewRegistry
from visual.card_view import CardView



class BoardView:
    def __init__(self, view_reg: ViewRegistry, data_reg: DataRegistry):
        self.view_reg = view_reg
        self.data_reg = data_reg

        self.hand_row = CardRow(Vector2(win_size[0] / 2, 500), 400, spread=True)
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
    
    def get_rows(self) -> list[CardRow]:
        return self.rows[:-1]

    def on_dragging(self, dragged_card: CardView):
        '''dragging cards, visual reordering only'''
        row = next((row for row in self.rows if dragged_card in row.cards), None)
        for card in row.cards:
            if card == dragged_card:
                continue
            # find two cards between which the dragged card is
            left = next((c for c in reversed(row.cards) if c.pos().x < dragged_card.pos().x), None)
            right = next((c for c in row.cards if c.pos().x > dragged_card.pos().x), None)
            if left is not None and right is not None:
                # insert dragged card between left and right
                row.cards.remove(dragged_card)
                row.cards.insert(row.cards.index(right), dragged_card)
            elif left is not None:
                # insert dragged card at the end
                row.cards.remove(dragged_card)
                row.cards.append(dragged_card)
            elif right is not None:
                # insert dragged card at the beginning
                row.cards.remove(dragged_card)
                row.cards.insert(0, dragged_card)
        row.recalc()
        