


from __future__ import annotations
from typing import Any

class SingletonMeta(type):
    _instances: dict[type, Any] = {}

    def __call__(cls, *args, **kwargs) -> Any:
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

id_type = int

class IdGen(metaclass=SingletonMeta):
    def __init__(self):
        self.num = 0
    
    def gen(self) -> id_type:
        self.num += 1
        return self.num - 1

def gen_id() -> id_type:
    return IdGen().gen()

if __name__ == '__main__':
    num = IdGen().gen()
    num = IdGen().gen()
    num = IdGen().gen()
    num = IdGen().gen()
    print(num)