
import inspect
import random

from domain.card import Card, CardData
from domain.board import Board
from domain.definitions import *
import domain.jokers as jokers
from domain.jokers import *
from domain.factory import Factory

from core.event_bus import EventBus


def main():
    board = Board()
    factory = Factory(EventBus())

    card = factory.card
    joker = factory.joker

    jokers_classes = [
        cls for _, cls in inspect.getmembers(jokers, inspect.isclass)
        if cls.__module__ == jokers.__name__
    ]
    # board.jokers = [joker(random.choice(jokers_classes)) for _ in range(5)]
    # print(board.jokers)

    board.jokers = [
        joker(JokerRaisedFist),
        joker(JokerGreedy)
    ]

    board.hand_cards = [
        card(suit=Suit.HEARTS, rank=Rank.ACE),
        card(suit=Suit.HEARTS, rank=Rank.THREE),
        card(suit=Suit.HEARTS, rank=Rank.KING),
        card(suit=Suit.HEARTS, rank=Rank.KING),
        ]
    
    board.selected_cards = [
        card(suit=Suit.DIAMONDS, rank=Rank.FOUR),
        card(suit=Suit.DIAMONDS, rank=Rank.FIVE),
        card(suit=Suit.CLUBS, rank=Rank.SIX),
        card(suit=Suit.DIAMONDS, rank=Rank.SEVEN),
        card(suit=Suit.DIAMONDS, rank=Rank.EIGHT),
        ]
    
    board.play()

    chips, mult = get_hand_level_chips_mult(HandType.STRAIGHT)
    print(f'chips: {chips}, mult: {mult}')
    for event in factory.event_bus.queue:
        print(f'card {factory.registry.get(event.id)}: {event}')
        if isinstance(event, TriggerCard):
            chips += event.chips
            mult += event.mult
            if event.time_mult > 0:
                mult *= event.time_mult
        print(f'chips: {chips}, mult: {mult}')

if __name__ == '__main__':
    main()