
from math import degrees
from typing import TYPE_CHECKING, Any
from pygame import Surface

from core.event_bus import EventBus, GameEventDiscard, GameEventPlay, GameEventUpdateScore, GameEventEndHand, GameEventEndRound
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

        self.chips = 0
        self.mult = 0
        self.round_score = 0
        self.info = 'hello'

        input_system.register_ui_element(self.button_play)
        input_system.register_ui_element(self.button_discard)
        input_system.register_ui_element(self.chips_text)
        input_system.register_ui_element(self.mult_text)
        input_system.register_ui_element(self.info_text)
        input_system.register_ui_element(self.round_score_text)
    
    def handle_game_event(self, event: Any) -> None:
        if isinstance(event, GameEventUpdateScore):
            nudge_chips = False
            nudge_mult = False
            if event.absolute:
                self.chips = event.chips
                self.mult = event.mult
            else:
                nudge_chips = event.chips != 0
                nudge_mult = event.mult != 0.0 or event.time_mult != 1.0
                self.chips += event.chips
                self.mult += event.mult
                self.mult *= event.time_mult

            self.chips_text.update(str(self.chips))
            if nudge_chips:
                self.chips_text.angle.nudge(degrees(10))
                self.chips_text.scale.nudge(20)
            
            self.mult_text.update(str(int(self.mult)))
            if nudge_mult:
                self.mult_text.angle.nudge(degrees(10))
                self.mult_text.scale.nudge(20)
            
            if event.hand_info[0] is None:
                self.info = ''
            else:
                self.info = event.hand_info[0].value + ' lvl:' + str(event.hand_info[1])
            self.info_text.update(self.info)
            
            event.is_handled = True
        
        elif isinstance(event, GameEventEndHand):
            self.round_score += self.chips * self.mult
            self.round_score_text.update(str(int(self.round_score)))
            event.is_handled = True
        
        elif isinstance(event, GameEventEndRound):
            self.round_score = 0
            self.round_score_text.update(str(int(self.round_score)))
            event.is_handled = True


    def draw(self, surf: Surface) -> None:
        self.button_play.draw(surf)
        self.button_discard.draw(surf)
        self.chips_text.draw(surf)
        self.mult_text.draw(surf)
        self.info_text.draw(surf)
        self.round_score_text.draw(surf)