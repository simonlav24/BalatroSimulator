
from pygame import Surface

from visual.board_view import BoardView
from visual.view_registry import ViewRegistry
from visual.input_system import InputSystem

class Renderer:
    def __init__(self, board: BoardView, view_reg: ViewRegistry, input_system: InputSystem):
        self.board = board
        self.view_reg = view_reg
        self.input_system = input_system

    def draw(self, win: Surface) -> None:
        for row in self.board.rows:
            row.draw(win)
            for card in row.cards:
                card.draw(win)
        
        if self.input_system.dragged is not None:
            self.input_system.dragged.draw(win)
