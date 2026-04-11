

import unittest
import sys
from pathlib import Path

sys.path.append(Path(__file__).parent.parent)

from definitions import Rank, Suit, Enhancement
from card import Card, CardData
from board import Board
from jokers import *


class TestRuns(unittest.TestCase):
    def test_baron(self):
        board = Board()

        board.hand_cards = [
            Card(CardData(suit=Suit.HEARTS, rank=Rank.KING)),
            Card(CardData(suit=Suit.HEARTS, rank=Rank.KING)),
            Card(CardData(suit=Suit.HEARTS, rank=Rank.KING)),
            ]
        
        board.selected_cards = [
            Card(CardData(suit=Suit.DIAMONDS, rank=Rank.FIVE)),
            ]
        
        board.jokers = [
            JokerBaron(),
        ]

        self.assertEqual(board.play()['score'], 33)
        mime = JokerMime()
        board.jokers.append(mime)
        self.assertEqual(board.play()['score'], 113)
        another_king = Card(CardData(suit=Suit.HEARTS, rank=Rank.KING))
        board.hand_cards.append(another_king)
        self.assertEqual(board.play()['score'], 256)
        another_king.data.seal = Seal.RED
        self.assertEqual(board.play()['score'], 384)
        another_king.data.enhancement = Enhancement.STEEL
        self.assertEqual(board.play()['score'], 1297)
        blueprint = JokerBlueprint()
        board.jokers.insert(0, blueprint)
        self.assertEqual(board.play()['score'], 49878)
        board.jokers.remove(blueprint)
        board.jokers.insert(1, blueprint)
        self.assertEqual(board.play()['score'], 9852)
        blueprint.data.edition = Edition.POLYCHROME
        self.assertEqual(board.play()['score'], 14778)
        mime.data.edition = Edition.POLYCHROME
        self.assertEqual(board.play()['score'], 22168)
        brainstorm = JokerBrainstorm()
        board.jokers.append(brainstorm)
        self.assertEqual(board.play()['score'], 4314398)
        board.jokers.remove(blueprint)
        board.jokers.insert(0, blueprint)
        self.assertEqual(board.play()['score'], 4314398)
        board.jokers.remove(brainstorm)
        board.jokers.insert(0, brainstorm)
        self.assertEqual(board.play()['score'], 112227)
        board.jokers.remove(brainstorm)
        board.jokers.insert(1, brainstorm)
        self.assertEqual(board.play()['score'], 2919)
        board.jokers.remove(blueprint)
        board.jokers.append(blueprint)
        self.assertEqual(board.play()['score'], 2919)

    def test_golden_vampire(self):
        board = Board()

        board.hand_cards = [
            Card(CardData(suit=Suit.HEARTS, rank=Rank.KING)),
            Card(CardData(suit=Suit.HEARTS, rank=Rank.KING)),
            Card(CardData(suit=Suit.HEARTS, rank=Rank.KING)),
            ]
        
        board.selected_cards = [
            Card(CardData(suit=Suit.DIAMONDS, rank=Rank.FIVE)),
            Card(CardData(suit=Suit.SPADES, rank=Rank.KING)),
            Card(CardData(suit=Suit.DIAMONDS, rank=Rank.KING)),
            Card(CardData(suit=Suit.CLUBS, rank=Rank.KING)),
            Card(CardData(suit=Suit.DIAMONDS, rank=Rank.FIVE)),
            ]
        
        board.jokers = [
            JokerMidasMask(),
            JokerVampire()
        ]

        self.assertEqual(board.play()['score'], 416)
    
    def test_photochad(self):
        board = Board()

        board.hand_cards = [
            Card(CardData(suit=Suit.HEARTS, rank=Rank.KING)),
            Card(CardData(suit=Suit.HEARTS, rank=Rank.KING)),
            Card(CardData(suit=Suit.HEARTS, rank=Rank.KING)),
            ]
        
        board.selected_cards = [
            Card(CardData(suit=Suit.DIAMONDS, rank=Rank.KING)),
            Card(CardData(suit=Suit.CLUBS, rank=Rank.KING)),
            Card(CardData(suit=Suit.SPADES, rank=Rank.KING)),
            Card(CardData(suit=Suit.DIAMONDS, rank=Rank.FIVE)),
            Card(CardData(suit=Suit.DIAMONDS, rank=Rank.FIVE)),
            ]
        
        board.jokers = [
            JokerPhotograph(),
            JokerHangingChad()
        ]

        self.assertEqual(board.play()['score'], 3200)
        board.jokers.append(JokerSockAndBuskin())
        self.assertEqual(board.play()['score'], 8320)


    def test_baseball_card(self):
        board = Board()

        board.hand_cards = [
            Card(CardData(suit=Suit.HEARTS, rank=Rank.KING)),
            Card(CardData(suit=Suit.HEARTS, rank=Rank.KING)),
            Card(CardData(suit=Suit.HEARTS, rank=Rank.KING)),
            ]
        
        board.selected_cards = [
            Card(CardData(suit=Suit.DIAMONDS, rank=Rank.KING)),
            Card(CardData(suit=Suit.CLUBS, rank=Rank.KING)),
            Card(CardData(suit=Suit.SPADES, rank=Rank.KING)),
            Card(CardData(suit=Suit.DIAMONDS, rank=Rank.FIVE)),
            Card(CardData(suit=Suit.DIAMONDS, rank=Rank.FIVE)),
            ]
        
        board.jokers = [
            JokerPhotograph(),
            JokerBaseballCard(),
            JokerFourFingers(),
            JokerGiftCard(),
        ]

        self.assertEqual(board.play()['score'], 1440)
        board.jokers.append(JokerSockAndBuskin())
        self.assertEqual(board.play()['score'], 5940)

