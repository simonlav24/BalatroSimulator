

from random import randint, choice, uniform
from pygame import Surface

from core import Vector2
from core.id_gen import id_type
from visual.definitions import *

SPRING_FORCE = 80.0
SPRING_DAMP = 10.0
TIME_SCALE = 0.03


class MotionVector:
    def __init__(self, value, dist_func=lambda a, b: abs(a-b)):
        self.value = value
        self.value_target = value
        self.vel = value * 0
        self.dist_func = dist_func
    
    def nudge(self, value) -> None:
        self.vel += value

    def step(self) -> None:
        force =  SPRING_FORCE * (self.value_target - self.value)
        damping = -SPRING_DAMP * self.vel
        acc = force + damping
        self.vel += acc * TIME_SCALE
        self.value += self.vel * TIME_SCALE
        if self.dist_func(self.value, self.value_target) < 0.001:
            self.value = self.value_target
            
    def set(self, value) -> None:
        self.value_target = value
    
    def __call__(self):
        return self.value


class CardView:
    def __init__(self, id: id_type, surf: Surface):
        self.id: id_type = id
        self.surf = surf

        self.pos = MotionVector(Vector2(), lambda a, b: (a - b).length())
        self.scale = MotionVector(1.0)
        self.angle = MotionVector(0)

        self.is_hovered = False
        self.is_selected = False
        self.is_dragged = False

    def __repr__(self):
        return f'CardView({self.id})'

    def set_pos(self, pos: Vector2) -> None:
        self.pos.set(pos)

    def step(self) -> None:
        if self.is_hovered:
            self.scale.set(1.2)
        else:
            self.scale.set(1.0)
        
        if abs(self.pos.vel.x) > 100:
            self.angle.set(-self.pos.vel.x * 0.001)

        self.pos.step()
        self.angle.step()
        self.scale.step()
    
    def nudge(self, factor: float=1.0) -> None:
        self.angle.nudge(uniform(7 * factor, -7 * factor))
        self.scale.nudge(5 * factor)
