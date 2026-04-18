

from random import shuffle

from core.event_bus import EventBus, EventClearOut, EventDiscardCard, EventDrawCard
from core.data_registry import DataRegistry
from domain.board import Board
from domain.card import Card
from domain.joker import Joker

from visual.board_view import BoardView
from visual.animation_system import AnimationSystem
from visual.view_registry import ViewRegistry


class BoardPlayer:
    def __init__(self, board: Board, board_view: BoardView, event_bus: EventBus, anim_sys: AnimationSystem, data_reg: DataRegistry, view_reg: ViewRegistry):
        self.board = board
        self.board_view = board_view
        self.event_bus = event_bus
        self.anim_sys = anim_sys
        self.data_reg = data_reg
        self.view_reg = view_reg
    
    def reset(self) -> None:
        self.board.remaining_deck = self.board.full_deck.copy()
        self.board.hand_cards.clear()
        self.board.played_cards.clear()
        self.board.selected_cards.clear()

    def shuffle(self) -> None:
        shuffle(self.board.remaining_deck)

    def draw_cards(self, amount: int=-1) -> None:
        if amount == -1:
            # draw to full hand
            amount = self.board.get_data().hand_size - len(self.board.hand_cards)

        drawn_cards_ids = []
        for _ in range(amount):
            if len(self.board.remaining_deck) == 0:
                continue
            card_id = self.board.remaining_deck.pop().id
            drawn_cards_ids.append(card_id)
            # update domain
            self.board.hand_cards.append(self.data_reg[card_id])
            # update view
            # self.board_view.hand_row.add(self.view_reg[card_id])
        
        self._sort()
        for card in self.board.hand_cards:
            if card.id in drawn_cards_ids:
                index_in_hand = self.board.hand_cards.index(card)
                self.event_bus.add_event(EventDrawCard(card.id, index_in_hand))
    
    def _sort(self) -> None:
        self.board.hand_cards.sort(key=lambda x: (x.get_rank().value, x.data.suit.value), reverse=True)

    def play(self) -> None:
        # gather selected cards
        selected_cards_ids = self.board_view.hand_row.get_selected()
        for id in selected_cards_ids:
            self.view_reg[id].is_selected = False
        # update domain
        for card in [self.data_reg[id] for id in selected_cards_ids]:
            self.board.hand_cards.remove(card)
            self.board.selected_cards.append(card)

        # play board and create events
        self.board.play(self.event_bus)
        self.event_bus.add_event(EventClearOut())

    def discard(self) -> None:
        # update domain
        selected_cards_ids = self.board_view.hand_row.get_selected()
        for card in [self.data_reg[id] for id in selected_cards_ids]:
            self.board.hand_cards.remove(card)

        # update view
        # for card in [self.view_reg[id] for id in selected_cards_ids]:
        #     self.board_view.hand_row.remove(card)
        #     self.board_view.discard_pile.add(card)

        for id in selected_cards_ids:
            self.event_bus.add_event(EventDiscardCard(id))


    def flush_animation(self) -> None:
        self.anim_sys.set_up(self.event_bus)
        self.anim_sys.play()
        

    def add_card_to_deck(self, card: Card) -> None:
        self.board.full_deck.append(card)
    
    def add_joker(self, joker: Joker) -> None:
        self.board.jokers.append(joker)

