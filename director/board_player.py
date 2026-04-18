

from random import shuffle

from core.event_bus import EventBus, EventPlayHand, EventSelectCardsForPlay
from domain.board import Board
from domain.card import Card
from domain.joker import Joker

from visual.board_view import BoardView
from visual.animation_system import AnimationSystem


class BoardPlayer:
    def __init__(self, board: Board, board_view: BoardView, event_bus: EventBus, anim_sys: AnimationSystem):
        self.board = board
        self.board_view = board_view
        self.event_bus = event_bus
        self.anim_sys = anim_sys
    
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


    def play(self) -> None:
        # gather selected cards
        selected_card_views = self.board_view.hand_row.pop_selected()
        self.board_view.sync_to_board(self.board, selected_card_views)
        self.board_view.sync_with_board(self.board)

        # play board and create events
        self.board.play(self.event_bus)

        # events now stored in event_bus. play animations
        self.anim_sys.play_game(self.event_bus)
        
    def add_card_to_deck(self, card: Card) -> None:
        self.board.full_deck.append(card)
    
    def add_joker(self, joker: Joker) -> None:
        self.board.jokers.append(joker)
        self.board_view.sync_with_board(self.board)

    def handle_event(self, event) -> None:
        if isinstance(event, EventPlayHand):
            self.play()
