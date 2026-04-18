
from pygame import Surface

from visual.board_view import BoardView
from visual.view_registry import ViewRegistry

class Renderer:
    def __init__(self, board: BoardView, view_reg: ViewRegistry):
        self.board = board
        self.view_reg = view_reg

    def draw(self, win: Surface) -> None:
        for row in self.board.rows:
            row.draw(win)
            for card in row.cards:
                card.draw(win)
