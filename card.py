
from dataclasses import dataclass
from typing import Protocol

from definitions import *


@dataclass
class CardData:
    suit: Suit
    rank: Rank
    value_bonus: int = 0
    enhancement: Enhancement = Enhancement.NONE
    seal: Seal = Seal.NONE
    edition: Edition = Edition.BASE


class BoardVision(Protocol):
    def get_hand_cards(self) -> list['Card']: ...
    def add_mult(self, mult: float): ...
    def add_chips(self, chips: int): ...
    def add_time_mult(self, mult: float): ...
    def get_mode(self) -> ClacMode: ...


class Card:
    def __init__(self, data: CardData):
        self.data = data
    
    def is_suit(self, suit: Suit) -> bool:
        if self.data.enhancement == Enhancement.WILD:
            return True
        if self.data.enhancement == Enhancement.STONE:
            return False
        return self.data.suit == suit

    def is_rank(self, rank: Rank) -> bool:
        if self.data.enhancement == Enhancement.STONE:
            return False
        return self.data.rank == rank
    
    def __repr__(self):
        enh = f'({self.data.enhancement})' if self.data.enhancement != Enhancement.NONE else ''
        seal = f' [{self.data.seal}]' if self.data.seal != Seal.NONE else ''
        edition = f' ({self.data.edition})' if self.data.edition != Edition.BASE else ''
        return f'{self.data.rank.name} of {self.data.suit.name}{enh}{seal}{edition}'

    def get_rank(self) -> Rank:
        if self.data.enhancement == Enhancement.STONE:
            return Rank.NONE
        return self.data.rank
    
    def get_suit(self) -> Suit:
        if self.data.enhancement == Enhancement.STONE:
            return Suit.NONE
        if self.data.enhancement == Enhancement.WILD:
            return Suit.ANY
        return self.data.suit

    def get_value(self) -> int:
        base_value = base_value_map[self.data.rank]
        return base_value + self.data.value_bonus

    def trigger_on_play(self, board: BoardVision) -> None:
        # enhancements
        if self.data.enhancement == Enhancement.BONUS:
            board.add_chips(self.get_value() + 30)

        elif self.data.enhancement == Enhancement.MULT:
            board.add_chips(self.get_value())
            board.add_mult(4)

        elif self.data.enhancement == Enhancement.GLASS:
            board.add_chips(self.get_value())
            board.add_time_mult(2)
        
        elif self.data.enhancement == Enhancement.STONE:
            board.add_chips(50 + self.data.value_bonus)

        elif self.data.enhancement == Enhancement.LUCKY:
            board.add_chips(self.get_value())
            if board.get_mode() == ClacMode.BEST:
                board.add_mult(20)
        
        else:
            board.add_chips(self.get_value())
        
        # editions
        if self.data.edition == Edition.FOIL:
            board.add_chips(50)

        elif self.data.edition == Edition.HOLOGRAPHIC:
            board.add_mult(10)
        
        elif self.data.edition == Edition.POLYCHROME:
            board.add_time_mult(1.5)
