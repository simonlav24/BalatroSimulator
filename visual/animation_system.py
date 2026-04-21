
from typing import Callable, Any
from enum import Enum

from core.event_bus import (
    BoardArea,
    EventBus, 
    EventSelectCardsForPlay,
    EventTriggerCard, 
    TriggerEdition, 
    EventClearOut, 
    EventDiscardCard,
    EventStartPlay,
    EventDrawCard,
    EventDeselect,
    EventReorderCards,
)
from core.data_registry import CardProtocol

from visual.card_view import CardView
from visual.view_registry import ViewRegistry
from visual.board_view import BoardView
from visual.layout import CardRow
from visual.definitions import FPS

DEBUG = False

class State(Enum):
    IDLE = 0
    RUNNING = 1



class Animation:
    def __init__(self):
        self.is_done = False
    
    def step(self):
        ...


class AnimCardNudge(Animation):
    def __init__(self, card_view: CardView):
        super().__init__()
        self.card = card_view
    
    def step(self):
        self.card.nudge()
        if DEBUG: print('nudgin card')
        self.is_done = True


class AnimCardSelect(Animation):
    def __init__(self, card_view: CardView):
        super().__init__()
        self.card = card_view
    
    def step(self):
        self.card.is_selected = not self.card.is_selected
        if DEBUG: print('selecting card')
        self.is_done = True


class AnimWait(Animation):
    def __init__(self, time: int):
        super().__init__()
        self.time = time
    
    def step(self):
        self.time -= 1
        if self.time == 0:
            self.is_done = True


class AnimFunc(Animation):
    def __init__(self, func: Callable, args: list[Any]=[]):
        super().__init__()
        self.func = func
        self.args = args
    
    def step(self):
        self.func(*self.args)
        self.is_done = True


class AnimRecalc(Animation):
    def __init__(self, board_view: BoardView):
        super().__init__()
        self.board_view = board_view
    
    def step(self):
        if DEBUG: print('recalculating positions')
        self.board_view.recalculate_positions()
        self.is_done = True


class AnimationSystem:
    def __init__(self, view_reg: ViewRegistry, board_view: BoardView):
        self.view_reg = view_reg
        self.board_view = board_view
        self.animation_queue: list[Animation] = []
        self.state = State.IDLE

    def step(self):
        if self.state == State.IDLE:
            ...
        
        elif self.state == State.RUNNING:
            if len(self.animation_queue) <= 0:
                self.state = State.IDLE
                return
            self.animation_queue[0].step()
            if self.animation_queue[0].is_done:
                self.animation_queue.pop(0)

    def set_up(self, event_bus: EventBus):
        for event in event_bus.get_round_queue():
            if isinstance(event, EventStartPlay):
                # remove from row and add to play area
                for card in [self.view_reg[id] for id in event.card_ids]:
                    self.board_view.hand_row.remove(card)
                    self.board_view.played_row.add(card)
                    self.animation_queue.append(AnimRecalc(self.board_view))
                    self.animation_queue.append(AnimWait(FPS * 0.25))

            elif isinstance(event, EventTriggerCard):
                self.animation_queue.append(AnimCardNudge(self.view_reg[event.id]))
                self.animation_queue.append(AnimWait(FPS * 0.5))
            
            elif isinstance(event, EventSelectCardsForPlay):
                # select playable cards
                for card in [self.view_reg[id] for id in event.card_ids]:
                    self.animation_queue.append(AnimCardSelect(card))
                    self.animation_queue.append(AnimRecalc(self.board_view))
                    self.animation_queue.append(AnimWait(FPS * 0.25))
                self.animation_queue.append(AnimWait(FPS * 0.25))
            
            elif isinstance(event, EventDeselect):
                for card in [self.view_reg[id] for id in event.card_ids]:
                    self.animation_queue.append(AnimCardSelect(card))
                self.animation_queue.append(AnimRecalc(self.board_view))
                self.animation_queue.append(AnimWait(FPS * 1))
            
            elif isinstance(event, EventClearOut):
                def clear_out():
                    cards = self.board_view.played_row.cards.copy()
                    for card in cards:
                        self.board_view.played_row.remove(card)
                        self.board_view.discard_pile.add(card)
                self.animation_queue.append(AnimFunc(clear_out, []))
                self.animation_queue.append(AnimRecalc(self.board_view))
                self.animation_queue.append(AnimWait(FPS * 0.25))
            
            elif isinstance(event, EventDiscardCard):
                card_id = event.card_id
                def remove(id):
                    self.board_view.hand_row.remove(self.view_reg[id])
                    self.board_view.discard_pile.add(self.view_reg[id])
                self.animation_queue.append(AnimFunc(remove, [card_id]))
                self.animation_queue.append(AnimRecalc(self.board_view))
                self.animation_queue.append(AnimWait(FPS * 0.1))
            
            elif isinstance(event, EventDrawCard):
                card_id = event.card_id
                def add(id, drawn_index, board_area):
                    area: dict[BoardArea, CardRow] = {
                        BoardArea.HAND: self.board_view.hand_row,
                        BoardArea.JOKER: self.board_view.joker_row,
                    }
                    area[board_area].add(self.view_reg[id], drawn_index)
                self.animation_queue.append(AnimFunc(add, [card_id, event.drawn_index, event.board_area]))
                self.animation_queue.append(AnimRecalc(self.board_view))
                self.animation_queue.append(AnimWait(FPS * 0.1))
            
            elif isinstance(event, EventReorderCards):
                def reorder(card_ids, board_area):
                    area: dict[BoardArea, CardRow] = {
                        BoardArea.HAND: self.board_view.hand_row,
                        BoardArea.JOKER: self.board_view.joker_row,
                    }
                    id_to_card = {card.id: card for card in area[board_area].cards}
                    area[board_area].cards[:] = [id_to_card[cid] for cid in card_ids]
                self.animation_queue.append(AnimFunc(reorder, [event.card_ids, event.board_area]))
                self.animation_queue.append(AnimRecalc(self.board_view))
    
    def play(self):
        self.state = State.RUNNING
    
    def sync_to_view(self, BoardArea) -> None:
        '''reorder view to match domain order'''
        mappings: list[tuple[CardRow, list[CardProtocol]]] = [
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

            id_to_card = {card.id: card for card in row.cards}
            row.cards[:] = [id_to_card[cid] for cid in domain_ids]