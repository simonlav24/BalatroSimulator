

from pygame import Vector2, Rect

def format_float(num: float) -> str:
    return f'{num:.2f}'.rstrip('0').rstrip('.')