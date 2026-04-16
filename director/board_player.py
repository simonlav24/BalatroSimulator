

from random import shuffle

from domain.board import Board
from visual.board_view import BoardView

class BoardPlayer:
    def __init__(self, board: Board, board_view: BoardView):
        self.board = board
        self.board_view = board_view
    
    def reset(self) -> None:
        self.board.remaining_deck = self.board.full_deck.copy()
        self.board.hand_cards.clear()
        self.board.played_cards.clear()
        self.board.selected_cards.clear()

        self.board_view.sync_with_board(self.board)

    def shuffle(self) -> None:
        shuffle(self.board.remaining_deck)

    def draw_cards(self, amount: int) -> None:
        for _ in range(amount):
            if len(self.board.remaining_deck) == 0:
                continue
            card = self.board.remaining_deck.pop()
            self.board.hand_cards.append(card)
        
        self.sort()
    
    def sort(self) -> None:
        self.board.hand_cards.sort(key=lambda x: (x.get_rank().value, x.data.suit.value), reverse=True)
        self.board_view.sync_with_board(self.board)


