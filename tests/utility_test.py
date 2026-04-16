

import unittest
import sys
from pathlib import Path

sys.path.append(Path(__file__).parent.parent)

from domain.card import Card, CardData
from domain.definitions import Rank, Suit, Enhancement
from domain.evaluation_rules import EvaluationRules
from domain.factory import Factory
from core.event_bus import EventBus

class TestEvaluationRules(unittest.TestCase):
    def setUp(self):
        self.factory = Factory()

    def test_is_suit(self):
        e = EvaluationRules()
        card = self.factory.card
        
        self.assertTrue(e.is_suit(card(suit=Suit.HEARTS, rank=Rank.ACE), Suit.HEARTS))
        self.assertFalse(e.is_suit(card(suit=Suit.HEARTS, rank=Rank.ACE), Suit.SPADES))

        self.assertTrue(e.is_suit(card(suit=Suit.HEARTS, rank=Rank.ACE, enhancement=Enhancement.WILD), Suit.HEARTS))
        self.assertTrue(e.is_suit(card(suit=Suit.HEARTS, rank=Rank.ACE, enhancement=Enhancement.WILD), Suit.DIAMONDS))

        self.assertFalse(e.is_suit(card(suit=Suit.HEARTS, rank=Rank.ACE, enhancement=Enhancement.WILD), Suit.NONE))
        self.assertFalse(e.is_suit(card(suit=Suit.HEARTS, rank=Rank.ACE, enhancement=Enhancement.STONE), Suit.HEARTS))
        self.assertFalse(e.is_suit(card(suit=Suit.HEARTS, rank=Rank.ACE, enhancement=Enhancement.STONE), Suit.ANY))

    def test_is_suit_reds(self):
        e = EvaluationRules(smeared=True)
        card = self.factory.card
        
        self.assertTrue(e.is_suit(card(suit=Suit.HEARTS, rank=Rank.ACE), Suit.HEARTS))
        self.assertTrue(e.is_suit(card(suit=Suit.HEARTS, rank=Rank.ACE), Suit.DIAMONDS))
        self.assertTrue(e.is_suit(card(suit=Suit.DIAMONDS, rank=Rank.ACE), Suit.HEARTS))
        self.assertFalse(e.is_suit(card(suit=Suit.SPADES, rank=Rank.ACE), Suit.HEARTS))
        self.assertFalse(e.is_suit(card(suit=Suit.CLUBS, rank=Rank.ACE), Suit.HEARTS))
        self.assertTrue(e.is_suit(card(suit=Suit.CLUBS, rank=Rank.ACE), Suit.CLUBS))
        self.assertTrue(e.is_suit(card(suit=Suit.CLUBS, rank=Rank.ACE), Suit.SPADES))

    def test_face_cards(self):
        e = EvaluationRules()
        card = self.factory.card

        self.assertTrue(e.is_face_card(card(suit=Suit.CLUBS, rank=Rank.KING)))
        self.assertFalse(e.is_face_card(card(suit=Suit.CLUBS, rank=Rank.ACE)))
        self.assertFalse(e.is_face_card(card(suit=Suit.CLUBS, rank=Rank.KING, enhancement=Enhancement.STONE)))

        e = EvaluationRules(all_face=True)
        self.assertTrue(e.is_face_card(card(suit=Suit.CLUBS, rank=Rank.KING)))
        self.assertTrue(e.is_face_card(card(suit=Suit.CLUBS, rank=Rank.ACE)))
        self.assertTrue(e.is_face_card(card(suit=Suit.CLUBS, rank=Rank.ACE, enhancement=Enhancement.STONE)))