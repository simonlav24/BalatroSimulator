
from math import degrees
from typing import TYPE_CHECKING, Any
from pygame import Surface

from core.event_bus import (
    EventBus,
    GameEventDiscard,
    GameEventPlay,
    GameEventUpdateScore,
    GameEventEndHand,
    GameEventEndRound,
    GameEventInitialize,
) 
from visual.definitions import win_size, FPS, UIRatios, Colors
from visual.ui import Button, Text

if TYPE_CHECKING:
    from visual.input_system import InputSystem


class UILayerRound:
    def __init__(self, input_system: 'InputSystem', event_bus: EventBus):
        self.event_bus = event_bus
        self.button_play = Button((*UIRatios.PLAY_BUTTON_OFFSET_1, *UIRatios.PLAY_BUTTON_SIZE), 'Play Hand', Colors.BLUE, GameEventPlay())
        self.button_discard = Button((*UIRatios.PLAY_BUTTON_OFFSET_2, *UIRatios.PLAY_BUTTON_SIZE), 'Discard', Colors.RED, GameEventDiscard())
        self.chips_text = Text((60, 400, 120, 60), '0', Colors.WHITE, Colors.BLUE)
        self.mult_text = Text((210, 400, 120, 60), '0', Colors.WHITE, Colors.RED)
        self.info_text = Text((60, 300, 240, 60), '', Colors.WHITE, None)
        self.round_score_text = Text((60, 240, 240, 60), '0', Colors.WHITE, None)

        self.remaining_hands_text = Text((150, 480, 50, 40), '0', Colors.BLUE, None)
        self.remaining_discards_text = Text((200, 480, 50, 40), '0', Colors.RED, None)
        self.money_text = Text((150, 520, 100, 40), '0', Colors.YELLOW, None)

        self.chips = 0
        self.mult = 0
        self.round_score = 0
        self.info = 'hello'
        self.remaining_discards = 0
        self.remaining_hands = 0
        self.money = 0

        input_system.register_ui_element(self.button_play)
        input_system.register_ui_element(self.button_discard)
        input_system.register_ui_element(self.chips_text)
        input_system.register_ui_element(self.mult_text)
        input_system.register_ui_element(self.info_text)
        input_system.register_ui_element(self.round_score_text)
        input_system.register_ui_element(self.remaining_hands_text)
        input_system.register_ui_element(self.remaining_discards_text)
        input_system.register_ui_element(self.money_text)
    
    def _handle_update_score(self, event: GameEventUpdateScore) -> None:
        nudge_chips = False
        nudge_mult = False
        nudge_money = False
        if event.absolute:
            self.chips = event.chips
            self.mult = event.mult
        else:
            nudge_chips = event.chips != 0
            nudge_mult = event.mult != 0.0 or event.time_mult != 1.0
            nudge_money = event.money != 0
            self.chips += event.chips
            self.mult += event.mult
            self.mult *= event.time_mult
            self.money += event.money

        self.chips_text.update(str(self.chips))
        if nudge_chips:
            self.chips_text.angle.nudge(degrees(10))
            self.chips_text.scale.nudge(20)
        
        self.mult_text.update(str(int(self.mult)))
        if nudge_mult:
            self.mult_text.angle.nudge(degrees(10))
            self.mult_text.scale.nudge(20)
        
        self.money_text.update('$' + str(self.money))
        if nudge_mult:
            self.money_text.angle.nudge(degrees(10))
            self.money_text.scale.nudge(20)
        
        if event.hand_info[0] is None:
            self.info = ''
        else:
            self.info = event.hand_info[0].value + ' lvl:' + str(event.hand_info[1])
        self.info_text.update(self.info)

    def _handle_end_hand(self, event: GameEventEndHand) -> None:
        self.round_score += self.chips * self.mult
        self.round_score_text.update(str(int(self.round_score)))

    def _handle_end_round(self, event: GameEventEndRound) -> None:
        self.round_score = 0
        self.round_score_text.update(str(int(self.round_score)))

    def _handle_discard(self, event: GameEventDiscard) -> None:
        self.remaining_discards -= 1
        self.remaining_discards_text.update(str(self.remaining_discards))
    
    def _handle_play(self, event: GameEventPlay) -> None:
        self.remaining_hands -= 1
        self.remaining_hands_text.update(str(self.remaining_hands))
    
    def _handle_initialize(self, event: GameEventInitialize) -> None:
        self.remaining_hands = event.hands
        self.remaining_hands_text.update(str(self.remaining_hands))
        self.remaining_discards = event.discards
        self.remaining_discards_text.update(str(self.remaining_discards))
        self.money = event.money
        self.money_text.update('$' + str(self.money))

    def handle_game_event(self, event: Any) -> None:
        handlers = {
            GameEventUpdateScore: self._handle_update_score,
            GameEventEndHand: self._handle_end_hand,
            GameEventEndRound: self._handle_end_round,
            GameEventDiscard: self._handle_discard,
            GameEventPlay: self._handle_play,
            GameEventInitialize: self._handle_initialize,
        }
        handler = handlers.get(type(event))
        if handler:
            handler(event)


    def draw(self, surf: Surface) -> None:
        self.button_play.draw(surf)
        self.button_discard.draw(surf)
        self.chips_text.draw(surf)
        self.mult_text.draw(surf)
        self.info_text.draw(surf)
        self.round_score_text.draw(surf)
        self.remaining_hands_text.draw(surf)
        self.remaining_discards_text.draw(surf)
        self.money_text.draw(surf)
