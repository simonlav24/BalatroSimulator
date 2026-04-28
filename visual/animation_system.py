
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
    GameEventUpdateScore,
    GameEventEndHand,
)
from core.data_registry import CardProtocol

from visual.card_view import CardView
from visual.view_registry import ViewRegistry
from visual.board_view import BoardView
from visual.layout import CardRow
from visual.definitions import FPS
from visual.effects import TriggerEffect, create_trigger_effect

DEBUG = False

TRIGGER_BASE_WAIT = 0.5
TIME_SKEW_MULTIPLIER = 0.95
MINIMUM_TIME_SKEW = 5.0
BASE_WAIT = 0.25
BASE_WAIT_QUICK = 0.1


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
        if self.time <= 0:
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


class AnimEventTrigger(Animation):
    def __init__(self, event_bus: EventBus, event: Any):
        super().__init__()
        self.event = event
        self.event_bus = event_bus
    
    def step(self):
        self.event_bus.add_game_event(self.event)
        self.is_done = True


class AnimationSystem:
    def __init__(self, view_reg: ViewRegistry, board_view: BoardView):
        self.view_reg = view_reg
        self.board_view = board_view
        self.animation_queue: list[Animation] = []
        self.state = State.IDLE

        self.effects: list[TriggerEffect] = []
        self.time_skew = 1.0

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
        
        for effect in self.effects:
            effect.step()
        self.effects = [effect for effect in self.effects if not effect.is_done]

    def _handle_start_play(self, event, event_bus: EventBus) -> None:
        # remove from row and add to play area
        for card in [self.view_reg[id] for id in event.card_ids]:
            self.board_view.hand_row.remove(card)
            self.board_view.played_row.add(card)
            self.animation_queue.append(AnimRecalc(self.board_view))
            self.animation_queue.append(AnimWait(FPS * BASE_WAIT))
    
    def _handle_trigger_card(self, event, event_bus: EventBus) -> None:
        self.animation_queue.append(AnimCardNudge(self.view_reg[event.id]))
        self.animation_queue.append(AnimEventTrigger(event_bus, GameEventUpdateScore(chips=event.chips, mult=event.mult, time_mult=event.time_mult)))
        def add_effect(animation_sys: AnimationSystem, effect: TriggerEffect):
            animation_sys.effects.append(effect)
        effect = create_trigger_effect(event, self.view_reg, self.time_skew)
        if effect:
            self.animation_queue.append(AnimFunc(add_effect, [self, effect]))
        if event.halt:
            wait_time = max(MINIMUM_TIME_SKEW, FPS * TRIGGER_BASE_WAIT * self.time_skew)
            self.time_skew *= TIME_SKEW_MULTIPLIER
            self.animation_queue.append(AnimWait(wait_time))
    
    def _handle_select_for_play(self, event, event_bus: EventBus) -> None:
        # select playable cards
        for card in [self.view_reg[id] for id in event.card_ids]:
            self.animation_queue.append(AnimCardSelect(card))
            self.animation_queue.append(AnimRecalc(self.board_view))
            self.animation_queue.append(AnimWait(FPS * BASE_WAIT))
        self.animation_queue.append(AnimWait(FPS * BASE_WAIT))
    
    def _handle_deselect(self, event, event_bus: EventBus) -> None:
        for card in [self.view_reg[id] for id in event.card_ids]:
            self.animation_queue.append(AnimCardSelect(card))
        self.animation_queue.append(AnimRecalc(self.board_view))
        self.animation_queue.append(AnimEventTrigger(event_bus, GameEventEndHand()))
        self.animation_queue.append(AnimWait(FPS * BASE_WAIT))

    def _handle_clear_out(self, event, event_bus: EventBus) -> None:
        def clear_out():
            cards = self.board_view.played_row.cards.copy()
            for card in cards:
                self.board_view.played_row.remove(card)
                self.board_view.discard_pile.add(card)
        self.animation_queue.append(AnimFunc(clear_out, []))
        self.animation_queue.append(AnimRecalc(self.board_view))
        self.animation_queue.append(AnimWait(FPS * BASE_WAIT))
    
    def _handle_discard(self, event, event_bus: EventBus) -> None:
        card_id = event.card_id
        def remove(id):
            self.board_view.hand_row.remove(self.view_reg[id])
            self.board_view.discard_pile.add(self.view_reg[id])
        self.animation_queue.append(AnimFunc(remove, [card_id]))
        self.animation_queue.append(AnimRecalc(self.board_view))
        self.animation_queue.append(AnimWait(FPS * BASE_WAIT_QUICK))
    
    def _handle_draw_card(self, event, event_bus: EventBus) -> None:
        card_id = event.card_id
        def add(id, drawn_index, board_area):
            area: dict[BoardArea, CardRow] = {
                BoardArea.HAND: self.board_view.hand_row,
                BoardArea.JOKER: self.board_view.joker_row,
            }
            area[board_area].add(self.view_reg[id], drawn_index)
        self.animation_queue.append(AnimFunc(add, [card_id, event.drawn_index, event.board_area]))
        self.animation_queue.append(AnimRecalc(self.board_view))
        self.animation_queue.append(AnimWait(FPS * BASE_WAIT_QUICK))
    
    def _handle_reorder(self, event, event_bus: EventBus) -> None:
        def reorder(card_ids, board_area):
            area: dict[BoardArea, CardRow] = {
                BoardArea.HAND: self.board_view.hand_row,
                BoardArea.JOKER: self.board_view.joker_row,
            }
            id_to_card = {card.id: card for card in area[board_area].cards}
            area[board_area].cards[:] = [id_to_card[cid] for cid in card_ids]
        self.animation_queue.append(AnimFunc(reorder, [event.card_ids, event.board_area]))
        self.animation_queue.append(AnimRecalc(self.board_view))

    def set_up(self, event_bus: EventBus):
        handlers = {
            EventStartPlay: self._handle_start_play,
            EventTriggerCard: self._handle_trigger_card,
            EventSelectCardsForPlay: self._handle_select_for_play,
            EventDeselect: self._handle_deselect,
            EventClearOut: self._handle_clear_out,
            EventDiscardCard: self._handle_discard,
            EventDrawCard: self._handle_draw_card,
            EventReorderCards: self._handle_reorder,
        }
        for event in event_bus.get_round_queue():
            handler = handlers.get(type(event))
            if handler:
                handler(event, event_bus)

    
    def play(self):
        self.state = State.RUNNING
    
    def draw(self, win) -> None:
        for effect in self.effects:
            effect.draw(win)
