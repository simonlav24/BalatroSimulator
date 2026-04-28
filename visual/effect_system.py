
from visual.effects import TriggerEffect

class EffectSystem:
    def __init__(self):
        self.effects: list[TriggerEffect] = []
    
    def add_effect(self, effect: TriggerEffect) -> None:
        self.effects.append(effect)

    def step(self):
        for effect in self.effects:
            effect.step()
        self.effects = [effect for effect in self.effects if not effect.is_done]

    def draw(self, win) -> None:
        for effect in self.effects:
            effect.draw(win)