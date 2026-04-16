
from pygame import Surface

from domain.board import Board

from visual.view_registry import ViewRegistry

class Renderer:
    def __init__(self, board: Board, view_reg: ViewRegistry):
        self.board = board
        self.view_reg = view_reg

    def draw(self, win: Surface) -> None:
        # draw cards in hand
        for card in self.board.get_hand_cards():
            self.view_reg[card.id].draw(win)
