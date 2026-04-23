
from typing import TYPE_CHECKING, Any
from pygame import Surface

from core.event_bus import EventBus, GameEventDiscard, GameEventPlay, GameEventUpdateScore
from visual.definitions import win_size, FPS, UIRatios, Colors
from visual.ui import Button, Text

if TYPE_CHECKING:
    from visual.input_system import InputSystem


class UILayerRound:
    def __init__(self, input_system: 'InputSystem', event_bus: EventBus):
        self.event_bus = event_bus
        self.button_play = Button((*UIRatios.PLAY_BUTTON_OFFSET_1, *UIRatios.PLAY_BUTTON_SIZE), 'Play Hand', Colors.BLUE, GameEventPlay())
        self.button_discard = Button((*UIRatios.PLAY_BUTTON_OFFSET_2, *UIRatios.PLAY_BUTTON_SIZE), 'Discard', Colors.RED, GameEventDiscard())
        
        self.chips_text = Text((60, 400, 120, 60), '0', Colors.BLUE)
        self.mult_text = Text((210, 400, 120, 60), '0', Colors.RED)
        self.chips = 0
        self.mult = 0

        input_system.register_ui_element(self.button_play)
        input_system.register_ui_element(self.button_discard)
    
    def handle_game_event(self, event: Any) -> None:
        if isinstance(event, GameEventUpdateScore):
            print('handling score change')
            if event.absolute:
                self.chips = event.chips
                self.mult = event.mult
            else:
                self.chips += event.chips
                self.mult += event.mult
                self.mult *= event.time_mult

            self.chips_text.update(str(self.chips))
            self.mult_text.update(str(self.mult))
            event.is_handled = True

    def draw(self, surf: Surface) -> None:
        self.button_play.draw(surf)
        self.button_discard.draw(surf)
        self.chips_text.draw(surf)
        self.mult_text.draw(surf)