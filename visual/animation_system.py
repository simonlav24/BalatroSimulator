

from enum import Enum

from core.event_bus import EventBus, EventSelectCardsForPlay, TriggerCard, TriggerEdition

from visual.card_view import CardView
from visual.view_registry import ViewRegistry


FPS = 60

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
        print('nudgin card')
        self.is_done = True


class AnimWait(Animation):
    def __init__(self, time: int):
        super().__init__()
        self.time = time
    
    def step(self):
        self.time -= 1
        if self.time == 0:
            self.is_done = True




class AnimationSystem:
    def __init__(self, view_reg: ViewRegistry):
        self.view_reg = view_reg
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

    def play_game(self, event_bus: EventBus):
        self.animation_queue.append(AnimWait(FPS))
        for event in event_bus.get_round_queue():
            
            if isinstance(event, TriggerCard):
                self.animation_queue.append(AnimCardNudge(self.view_reg[event.id]))
                self.animation_queue.append(AnimWait(FPS))
        
        self.play()
    
    def play(self):
        self.state = State.RUNNING