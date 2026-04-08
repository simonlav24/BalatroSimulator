

from card import Card, CardData
from board import Board
from definitions import *
from jokers import *

def main():
    board = Board()

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
    
    board.jokers = [
        JokerRaisedFist(),
    ]

    board.play()

if __name__ == '__main__':
    main()