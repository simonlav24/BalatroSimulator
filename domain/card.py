
from dataclasses import dataclass
from typing import Protocol
from random import randint
from core.id_gen import gen_id

from domain.definitions import *

from core.event_bus import EventBus, EventTriggerCard, TriggerEdition


@dataclass
class CardData:
    rank: Rank
    suit: Suit
    enhancement: Enhancement = Enhancement.NONE
    edition: Edition = Edition.BASE
    seal: Seal = Seal.NONE
    value_bonus: int = 0


class BoardVision(Protocol):
    def get_hand_cards(self) -> list['Card']: ...
    def add_mult(self, mult: float): ...
    def add_chips(self, chips: int): ...
    def add_time_mult(self, mult: float): ...
    def get_mode(self) -> CalcMode: ...


class Card:
    def __init__(self, data: CardData, event_bus: EventBus):
        self.data = data
        self.id = gen_id()
        self.event_bus = event_bus
    
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
        # chips
        chips = 0
        if self.data.enhancement == Enhancement.STONE:
            chips = 50 + self.data.value_bonus
        
        elif self.data.enhancement == Enhancement.BONUS:
            chips = self.get_value() + 30
        
        else:
            chips = self.get_value()
        
        board.add_chips(chips)
        self.event_bus.add_event(EventTriggerCard(self.id, chips=chips, is_joker=False))

        # mult
        mult = 0
        if self.data.enhancement == Enhancement.MULT:
            mult = 4

        elif self.data.enhancement == Enhancement.LUCKY:
            if board.get_mode() == CalcMode.BEST:
                mult = 20
            if board.get_mode() == CalcMode.SIMULATE:
                if randint(1, 5) == 1:
                    mult = 20
        
        if mult > 0:
            board.add_mult(mult)
            self.event_bus.add_event(EventTriggerCard(self.id, mult=mult, is_joker=False))

        if self.data.enhancement == Enhancement.GLASS:
            board.add_time_mult(2)
            self.event_bus.add_event(EventTriggerCard(self.id, time_mult=2, is_joker=False))
        

        # editions
        if self.data.edition == Edition.FOIL:
            board.add_chips(50)
            self.event_bus.add_event(TriggerEdition(self.id, self.data.edition))

        elif self.data.edition == Edition.HOLOGRAPHIC:
            board.add_mult(10)
            self.event_bus.add_event(TriggerEdition(self.id, self.data.edition))
        
        elif self.data.edition == Edition.POLYCHROME:
            board.add_time_mult(1.5)
            self.event_bus.add_event(TriggerEdition(self.id, self.data.edition))


    def trigger_in_hand_on_hand_end(self, board: BoardVision) -> None:
        if self.data.enhancement == Enhancement.STEEL:
            board.add_time_mult(1.5)
            self.event_bus.add_event(EventTriggerCard(self.id, time_mult=1.5, is_joker=False))


def create_standard_deck() -> list[CardData]:
    deck: list[Card] = []
    for rank in Rank:
        if rank == Rank.NONE:
            continue
        for suit in Suit:
            if suit in [Suit.NONE, Suit.ANY]:
                continue
            deck.append(CardData(rank, suit))
    return deck

