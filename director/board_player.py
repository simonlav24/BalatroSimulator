

from random import shuffle

from core.event_bus import (
    BoardArea,
    EventBus,
    EventClearOut,
    EventDiscardCard,
    EventDrawCard,
    EventStartPlay,
    EventSelectCardsForPlay,
    EventDeselect,
    EventReorderCards,
    GameEventPlay,
    GameEventDiscard,
    GameEventChangedOrder,
    GameEventChagnedSelection,
    GameEventUpdateScore,
)
from core.data_registry import DataRegistry
from domain.board import Board
from domain.card import Card
from domain.joker import Joker

from visual.board_view import BoardView
from visual.animation_system import AnimationSystem
from visual.view_registry import ViewRegistry
from visual.layout import CardRow

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

    def handle_game_event(self, event) -> None:
        if isinstance(event, GameEventPlay):
            self.play()
            self.draw_cards()
            self.flush_animation()
            event.is_handled = True
        
        elif isinstance(event, GameEventDiscard):
            self.discard()
            self.draw_cards()
            self.flush_animation()
            event.is_handled = True
        
        elif isinstance(event, GameEventChangedOrder):
            self.sync_to_domain()
            print('synced to domain')
            self.board_view.recalculate_positions()
            event.is_handled = True
        
        elif isinstance(event, GameEventChagnedSelection):
            hand_info, chips, mult = self.board.get_initial_score([self.data_reg[card.id] for card in self.board_view.hand_row.cards if card.is_selected])
            self.event_bus.add_game_event(GameEventUpdateScore(chips=chips, mult=mult, absolute=True, hand_info=hand_info))
            event.is_handled = True
            

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
        
        self.event_bus.add_event(EventReorderCards([card.id for card in self.board.hand_cards], BoardArea.HAND))

    def add_joker(self, joker: Joker) -> None:
        self.board.jokers.append(joker)
        self.event_bus.add_event(EventDrawCard(joker.id, self.board.jokers.index(joker), BoardArea.JOKER))

    def _sort(self) -> None:
        ''' sort hand cards, Domain only!'''
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

        # event for chosen played cards
        self.event_bus.add_event(EventStartPlay(selected_cards_ids))

        self.board.play_initialize()
        self.event_bus.add_event(EventSelectCardsForPlay([card.id for card in self.board.get_played_cards()]))
        # play board and create events
        self.board.play()

        # deselect cards
        self.event_bus.add_event(EventDeselect([card.id for card in self.board.get_played_cards()]))

        # discard played cards
        for card in [self.data_reg[id] for id in selected_cards_ids]:
            self.board.selected_cards.remove(card)

        self.board.played_cards.clear()
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
    
    def sync_to_domain(self) -> None:
        '''reorder domain to match view order'''
        mappings: list[tuple[CardRow, list[Card]]] = [
            (self.board_view.hand_row, self.board.hand_cards),
            (self.board_view.played_row, self.board.played_cards),
            (self.board_view.joker_row, self.board.jokers),
        ]

        for row, domain_row in mappings:
            row_ids = [card.id for card in row.cards]
            domain_ids = [card.id for card in domain_row]

            if row_ids == domain_ids:
                continue  # already synced

            if set(row_ids) != set(domain_ids):
                raise ValueError("View/domain mismatch — cannot safely reorder")

            id_to_card = {card.id: card for card in domain_row}
            domain_row[:] = [id_to_card[cid] for cid in row_ids]
