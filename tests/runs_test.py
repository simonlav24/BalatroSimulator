

import unittest
import sys
from pathlib import Path

sys.path.append(Path(__file__).parent.parent)

from domain.definitions import Rank, Suit, Enhancement
from domain.card import Card, CardData
from domain.board import Board
from domain.jokers import *
from domain.factory import Factory


class TestRuns(unittest.TestCase):
    def setUp(self):
        self.factory = Factory()

    def test_baron(self):
        card = self.factory.card
        joker = self.factory.joker
        board = Board()

        board.hand_cards = [
            card(suit=Suit.HEARTS, rank=Rank.KING),
            card(suit=Suit.HEARTS, rank=Rank.KING),
            card(suit=Suit.HEARTS, rank=Rank.KING),
            ]
        
        board.selected_cards = [
            card(suit=Suit.DIAMONDS, rank=Rank.FIVE),
            ]
        
        board.jokers = [
            joker(JokerBaron),
        ]

        self.assertEqual(board.play()['score'], 33)
        mime = joker(JokerMime)
        board.jokers.append(mime)
        self.assertEqual(board.play()['score'], 113)
        another_king = card(suit=Suit.HEARTS, rank=Rank.KING)
        board.hand_cards.append(another_king)
        self.assertEqual(board.play()['score'], 256)
        another_king.data.seal = Seal.RED
        self.assertEqual(board.play()['score'], 384)
        another_king.data.enhancement = Enhancement.STEEL
        self.assertEqual(board.play()['score'], 1297)
        blueprint = joker(JokerBlueprint)
        board.jokers.insert(0, blueprint)
        self.assertEqual(board.play()['score'], 49878)
        board.jokers.remove(blueprint)
        board.jokers.insert(1, blueprint)
        self.assertEqual(board.play()['score'], 9852)
        blueprint.data.edition = Edition.POLYCHROME
        self.assertEqual(board.play()['score'], 14778)
        mime.data.edition = Edition.POLYCHROME
        self.assertEqual(board.play()['score'], 22168)
        brainstorm = joker(JokerBrainstorm)
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
        card = self.factory.card
        joker = self.factory.joker
        board = Board()

        board.hand_cards = [
            card(suit=Suit.HEARTS, rank=Rank.KING),
            card(suit=Suit.HEARTS, rank=Rank.KING),
            card(suit=Suit.HEARTS, rank=Rank.KING),
            ]
        
        board.selected_cards = [
            card(suit=Suit.DIAMONDS, rank=Rank.FIVE),
            card(suit=Suit.SPADES, rank=Rank.KING),
            card(suit=Suit.DIAMONDS, rank=Rank.KING),
            card(suit=Suit.CLUBS, rank=Rank.KING),
            card(suit=Suit.DIAMONDS, rank=Rank.FIVE),
            ]
        
        board.jokers = [
            joker(JokerMidasMask),
            joker(JokerVampire)
        ]

        self.assertEqual(board.play()['score'], 416)
    
    def test_photochad(self):
        card = self.factory.card
        joker = self.factory.joker
        board = Board()

        board.hand_cards = [
            card(suit=Suit.HEARTS, rank=Rank.KING),
            card(suit=Suit.HEARTS, rank=Rank.KING),
            card(suit=Suit.HEARTS, rank=Rank.KING),
            ]
        
        board.selected_cards = [
            card(suit=Suit.DIAMONDS, rank=Rank.KING),
            card(suit=Suit.CLUBS, rank=Rank.KING),
            card(suit=Suit.SPADES, rank=Rank.KING),
            card(suit=Suit.DIAMONDS, rank=Rank.FIVE),
            card(suit=Suit.DIAMONDS, rank=Rank.FIVE),
            ]
        
        board.jokers = [
            joker(JokerPhotograph),
            joker(JokerHangingChad)
        ]

        self.assertEqual(board.play()['score'], 3200)
        board.jokers.append(joker(JokerSockAndBuskin))
        self.assertEqual(board.play()['score'], 8320)


    def test_baseball_card(self):
        card = self.factory.card
        joker = self.factory.joker
        board = Board()

        board.hand_cards = [
            card(suit=Suit.HEARTS, rank=Rank.KING),
            card(suit=Suit.HEARTS, rank=Rank.KING),
            card(suit=Suit.HEARTS, rank=Rank.KING),
            ]
        
        board.selected_cards = [
            card(suit=Suit.DIAMONDS, rank=Rank.KING),
            card(suit=Suit.CLUBS, rank=Rank.KING),
            card(suit=Suit.SPADES, rank=Rank.KING),
            card(suit=Suit.DIAMONDS, rank=Rank.FIVE),
            card(suit=Suit.DIAMONDS, rank=Rank.FIVE),
            ]
        
        board.jokers = [
            joker(JokerPhotograph),
            joker(JokerBaseballCard),
            joker(JokerFourFingers),
            joker(JokerGiftCard),
        ]

        self.assertEqual(board.play()['score'], 1440)
        board.jokers.append(joker(JokerSockAndBuskin))
        self.assertEqual(board.play()['score'], 5940)

    def test_flower_pot(self):
        card = self.factory.card
        joker = self.factory.joker
        board = Board()
        board.hand_cards = []
        board.selected_cards = [
            card(suit=Suit.CLUBS, rank=Rank.JACK, enhancement=Enhancement.STONE),
            card(suit=Suit.DIAMONDS, rank=Rank.JACK),
            card(suit=Suit.CLUBS, rank=Rank.JACK),
            card(suit=Suit.HEARTS, rank=Rank.JACK),
            card(suit=Suit.SPADES, rank=Rank.JACK),
            ]
        board.jokers = [
            joker(JokerFlowerPot),
        ]
        self.assertEqual(board.play()['score'], 3150)

        board.selected_cards = [
            card(suit=Suit.CLUBS, rank=Rank.JACK, enhancement=Enhancement.STONE),
            card(suit=Suit.DIAMONDS, rank=Rank.JACK, enhancement=Enhancement.WILD),
            card(suit=Suit.CLUBS, rank=Rank.JACK, enhancement=Enhancement.WILD),
            card(suit=Suit.HEARTS, rank=Rank.JACK, enhancement=Enhancement.WILD),
            card(suit=Suit.SPADES, rank=Rank.JACK, enhancement=Enhancement.WILD),
            ]
        self.assertEqual(board.play()['score'], 3150)

        board.selected_cards = [
            card(suit=Suit.CLUBS, rank=Rank.JACK, enhancement=Enhancement.STONE),
            card(suit=Suit.DIAMONDS, rank=Rank.JACK, enhancement=Enhancement.WILD),
            card(suit=Suit.DIAMONDS, rank=Rank.JACK, enhancement=Enhancement.WILD),
            card(suit=Suit.DIAMONDS, rank=Rank.JACK, enhancement=Enhancement.WILD),
            card(suit=Suit.DIAMONDS, rank=Rank.JACK, enhancement=Enhancement.WILD),
            ]
        self.assertEqual(board.play()['score'], 3150)

        board.selected_cards = [
            card(suit=Suit.CLUBS, rank=Rank.JACK, enhancement=Enhancement.STONE),
            card(suit=Suit.DIAMONDS, rank=Rank.JACK, enhancement=Enhancement.WILD),
            card(suit=Suit.DIAMONDS, rank=Rank.JACK, enhancement=Enhancement.WILD),
            card(suit=Suit.DIAMONDS, rank=Rank.JACK, enhancement=Enhancement.WILD),
            card(suit=Suit.SPADES, rank=Rank.JACK),
            ]
        self.assertEqual(board.play()['score'], 3150)

        board.jokers.append(joker(JokerSmearedJoker))
        board.selected_cards = [
            card(suit=Suit.CLUBS, rank=Rank.JACK, enhancement=Enhancement.STONE),
            card(suit=Suit.CLUBS, rank=Rank.JACK),
            card(suit=Suit.CLUBS, rank=Rank.JACK),
            card(suit=Suit.DIAMONDS, rank=Rank.JACK),
            card(suit=Suit.DIAMONDS, rank=Rank.JACK),
            ]
        self.assertEqual(board.play()['score'], 3150)
    
    def test_wee_joker(self):
        card = self.factory.card
        joker = self.factory.joker
        board = Board()
        board.hand_cards = []
        board.selected_cards = [
            card(suit=Suit.HEARTS, rank=Rank.TWO, seal=Seal.RED, edition=Edition.POLYCHROME),
            card(suit=Suit.HEARTS, rank=Rank.TWO, seal=Seal.RED, edition=Edition.POLYCHROME),
            card(suit=Suit.CLUBS, rank=Rank.TWO, enhancement=Enhancement.MULT),
            card(suit=Suit.DIAMONDS, rank=Rank.TWO, enhancement=Enhancement.MULT),
            card(suit=Suit.CLUBS, rank=Rank.TWO),
            ]
        board.jokers = [
            joker(JokerWeeJoker),
            joker(JokerHangingChad),
            joker(JokerHack)
        ]
        self.assertEqual(board.play()['score'], 84122)
