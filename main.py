
import inspect
import random

from domain.card import Card, CardData
from domain.board import Board
from domain.definitions import *
import domain.jokers as jokers
from domain.jokers import *



def main():
    board = Board()

    jokers_classes = [
        cls for _, cls in inspect.getmembers(jokers, inspect.isclass)
        if cls.__module__ == jokers.__name__
    ]
    # board.jokers = [random.choice(jokers_classes)() for _ in range(5)]
    # print(board.jokers)

    board.jokers = [JokerAncientJoker(), JokerCampfire(), JokerBusinessCard(), JokerDusk(), JokerSteelJoker()]

    board.hand_cards = [
        Card(CardData(suit=Suit.HEARTS, rank=Rank.ACE)),
        Card(CardData(suit=Suit.HEARTS, rank=Rank.THREE)),
        Card(CardData(suit=Suit.HEARTS, rank=Rank.KING)),
        Card(CardData(suit=Suit.HEARTS, rank=Rank.KING)),
        ]
    
    board.selected_cards = [
        Card(CardData(suit=Suit.DIAMONDS, rank=Rank.FOUR)),
        Card(CardData(suit=Suit.DIAMONDS, rank=Rank.FIVE)),
        Card(CardData(suit=Suit.CLUBS, rank=Rank.SIX)),
        Card(CardData(suit=Suit.DIAMONDS, rank=Rank.SEVEN)),
        Card(CardData(suit=Suit.DIAMONDS, rank=Rank.EIGHT)),
        ]
    

    board.play()

if __name__ == '__main__':
    main()