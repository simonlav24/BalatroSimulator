

import unittest
import sys
from pathlib import Path

sys.path.append(Path(__file__).parent.parent)

from domain.card import Card, CardData
from domain.board import Board
from domain.definitions import *
from domain.jokers import *
from domain.poker import asses_poker_hand
from domain.evaluation_rules import EvaluationRules
from domain.factory import Factory

class TestSimple(unittest.TestCase):
    def setUp(self):
        self.factory = Factory()

    def test_highcard(self):
        card = self.factory.card
        cards = [
            card(suit=Suit.DIAMONDS, rank=Rank.FOUR),
            card(suit=Suit.DIAMONDS, rank=Rank.FIVE),
            card(suit=Suit.CLUBS, rank=Rank.SIX),
            card(suit=Suit.DIAMONDS, rank=Rank.ACE),
            card(suit=Suit.DIAMONDS, rank=Rank.EIGHT),
            ]
        evaluation_rules = EvaluationRules()
        hand_type, played_cards = asses_poker_hand(cards, evaluation_rules)
        self.assertEqual(hand_type, HandType.HIGH_CARD)
        self.assertEqual(played_cards, [cards[3]])


    def test_flush_four_fingers(self):
        card = self.factory.card
        cards = [
            card(suit=Suit.DIAMONDS, rank=Rank.FOUR),
            card(suit=Suit.DIAMONDS, rank=Rank.FIVE),
            card(suit=Suit.CLUBS, rank=Rank.SIX),
            card(suit=Suit.DIAMONDS, rank=Rank.ACE),
            card(suit=Suit.DIAMONDS, rank=Rank.EIGHT),
            ]
        evaluation_rules = EvaluationRules(fingers=4)
        hand_type, played_cards = asses_poker_hand(cards, evaluation_rules)
        self.assertEqual(hand_type, HandType.FLUSH)
        self.assertEqual(played_cards, [card for card in cards if card.is_suit(Suit.DIAMONDS)])


    def test_straight_flush_four_fingers(self):
        card = self.factory.card
        cards = [
            card(suit=Suit.DIAMONDS, rank=Rank.FOUR),
            card(suit=Suit.DIAMONDS, rank=Rank.FIVE),
            card(suit=Suit.DIAMONDS, rank=Rank.SIX),
            card(suit=Suit.DIAMONDS, rank=Rank.ACE),
            card(suit=Suit.DIAMONDS, rank=Rank.SEVEN),
            ]
        evaluation_rules = EvaluationRules(fingers=4)
        hand_type, played_cards = asses_poker_hand(cards, evaluation_rules)
        self.assertEqual(hand_type, HandType.STRAIGHT_FLUSH)
        self.assertEqual(played_cards, [card for card in cards if not card.is_rank(Rank.ACE)])


    def test_four(self):
        card = self.factory.card
        cards = [
            card(suit=Suit.DIAMONDS, rank=Rank.FOUR),
            card(suit=Suit.CLUBS, rank=Rank.ACE),
            card(suit=Suit.DIAMONDS, rank=Rank.ACE),
            card(suit=Suit.HEARTS, rank=Rank.ACE),
            card(suit=Suit.SPADES, rank=Rank.ACE),
            ]
        evaluation_rules = EvaluationRules()
        hand_type, played_cards = asses_poker_hand(cards, evaluation_rules)

        self.assertEqual(hand_type, HandType.FOUR_OF_A_KIND)
        self.assertEqual(played_cards, [card for card in cards if card.is_rank(Rank.ACE)])
    

    def test_three(self):
        card = self.factory.card
        cards = [
            card(suit=Suit.DIAMONDS, rank=Rank.FOUR),
            card(suit=Suit.CLUBS, rank=Rank.ACE),
            card(suit=Suit.DIAMONDS, rank=Rank.ACE),
            card(suit=Suit.HEARTS, rank=Rank.ACE),
            card(suit=Suit.SPADES, rank=Rank.FIVE),
            ]
        evaluation_rules = EvaluationRules()
        hand_type, played_cards = asses_poker_hand(cards, evaluation_rules)

        self.assertEqual(hand_type, HandType.THREE_OF_A_KIND)
        self.assertEqual(played_cards, [card for card in cards if card.is_rank(Rank.ACE)])


    def test_straight(self):
        card = self.factory.card
        cards = [
            card(suit=Suit.HEARTS, rank=Rank.SIX),
            card(suit=Suit.DIAMONDS, rank=Rank.THREE),
            card(suit=Suit.CLUBS, rank=Rank.FIVE),
            card(suit=Suit.DIAMONDS, rank=Rank.FOUR),
            card(suit=Suit.SPADES, rank=Rank.SEVEN),
            ]
        evaluation_rules = EvaluationRules()
        hand_type, played_cards = asses_poker_hand(cards, evaluation_rules)

        self.assertEqual(hand_type, HandType.STRAIGHT)
        self.assertEqual(played_cards, cards)


    def test_straight_skipping(self):
        card = self.factory.card
        cards = [
            card(suit=Suit.HEARTS, rank=Rank.JACK),
            card(suit=Suit.DIAMONDS, rank=Rank.THREE),
            card(suit=Suit.CLUBS, rank=Rank.SEVEN),
            card(suit=Suit.DIAMONDS, rank=Rank.FIVE),
            card(suit=Suit.SPADES, rank=Rank.NINE),
            ]
        evaluation_rules = EvaluationRules(straight_skip=True)
        hand_type, played_cards = asses_poker_hand(cards, evaluation_rules)

        self.assertEqual(hand_type, HandType.STRAIGHT)
        self.assertEqual(played_cards, cards)


    def test_straight_four_1(self):
        card = self.factory.card
        cards = [
            card(suit=Suit.HEARTS, rank=Rank.THREE),
            card(suit=Suit.DIAMONDS, rank=Rank.FOUR),
            card(suit=Suit.CLUBS, rank=Rank.FIVE),
            card(suit=Suit.DIAMONDS, rank=Rank.SIX),
            card(suit=Suit.SPADES, rank=Rank.KING),
            ]
        evaluation_rules = EvaluationRules(fingers=4)
        hand_type, played_cards = asses_poker_hand(cards, evaluation_rules)

        self.assertEqual(hand_type, HandType.STRAIGHT)
        self.assertEqual(played_cards, [card for card in cards if not card.is_rank(Rank.KING)])


    def test_straight_four_2(self):
        card = self.factory.card
        cards = [
            card(suit=Suit.SPADES, rank=Rank.TWO),
            card(suit=Suit.HEARTS, rank=Rank.SEVEN),
            card(suit=Suit.DIAMONDS, rank=Rank.FOUR),
            card(suit=Suit.CLUBS, rank=Rank.FIVE),
            card(suit=Suit.DIAMONDS, rank=Rank.SIX),
            ]
        evaluation_rules = EvaluationRules(fingers=4)
        hand_type, played_cards = asses_poker_hand(cards, evaluation_rules)

        self.assertEqual(hand_type, HandType.STRAIGHT)
        self.assertEqual(played_cards, [cards[1], cards[2], cards[3], cards[4]])
    

    def test_straight_four_3(self):
        card = self.factory.card
        cards = [
            card(suit=Suit.SPADES, rank=Rank.FIVE),
            card(suit=Suit.HEARTS, rank=Rank.SIX),
            card(suit=Suit.DIAMONDS, rank=Rank.SEVEN),
            card(suit=Suit.CLUBS, rank=Rank.EIGHT),
            card(suit=Suit.DIAMONDS, rank=Rank.EIGHT),
            ]
        evaluation_rules = EvaluationRules(fingers=4)
        hand_type, played_cards = asses_poker_hand(cards, evaluation_rules)

        self.assertEqual(hand_type, HandType.STRAIGHT)
        self.assertEqual(played_cards, [cards[0], cards[1], cards[2], cards[3]])


    def test_straight_false(self):
        card = self.factory.card
        cards = [
            card(suit=Suit.SPADES, rank=Rank.FIVE),
            card(suit=Suit.HEARTS, rank=Rank.SIX),
            card(suit=Suit.DIAMONDS, rank=Rank.EIGHT),
            card(suit=Suit.CLUBS, rank=Rank.NINE),
            card(suit=Suit.DIAMONDS, rank=Rank.TEN),
            ]
        evaluation_rules = EvaluationRules(fingers=4)
        hand_type, played_cards = asses_poker_hand(cards, evaluation_rules)

        self.assertEqual(hand_type, HandType.HIGH_CARD)
        self.assertEqual(played_cards, [cards[4]])


    def test_straight_aces_high(self):
        card = self.factory.card
        cards = [
            card(suit=Suit.SPADES, rank=Rank.FIVE),
            card(suit=Suit.HEARTS, rank=Rank.JACK),
            card(suit=Suit.DIAMONDS, rank=Rank.ACE),
            card(suit=Suit.DIAMONDS, rank=Rank.QUEEN),
            card(suit=Suit.CLUBS, rank=Rank.KING),
            ]
        evaluation_rules = EvaluationRules(fingers=4)
        hand_type, played_cards = asses_poker_hand(cards, evaluation_rules)

        self.assertEqual(hand_type, HandType.STRAIGHT)
        self.assertEqual(played_cards, [cards[1], cards[2], cards[3], cards[4]])

    def test_straight_aces_low(self):
        card = self.factory.card
        cards = [
            card(suit=Suit.SPADES, rank=Rank.FOUR),
            card(suit=Suit.HEARTS, rank=Rank.THREE),
            card(suit=Suit.DIAMONDS, rank=Rank.ACE),
            card(suit=Suit.DIAMONDS, rank=Rank.TWO),
            card(suit=Suit.CLUBS, rank=Rank.KING),
            ]
        evaluation_rules = EvaluationRules(fingers=4)
        hand_type, played_cards = asses_poker_hand(cards, evaluation_rules)

        self.assertEqual(hand_type, HandType.STRAIGHT)
        self.assertEqual(played_cards, [cards[0], cards[1], cards[2], cards[3]])


    def test_two_pair(self):
        card = self.factory.card
        cards = [
            card(suit=Suit.DIAMONDS, rank=Rank.FOUR),
            card(suit=Suit.CLUBS, rank=Rank.ACE),
            card(suit=Suit.DIAMONDS, rank=Rank.ACE),
            card(suit=Suit.HEARTS, rank=Rank.FIVE),
            card(suit=Suit.SPADES, rank=Rank.FIVE),
            ]
        evaluation_rules = EvaluationRules()
        hand_type, played_cards = asses_poker_hand(cards, evaluation_rules)

        self.assertEqual(hand_type, HandType.TWO_PAIR)
        self.assertEqual(played_cards, [card for card in cards if card.is_rank(Rank.ACE) or card.is_rank(Rank.FIVE)])


    def test_pair(self):
        card = self.factory.card
        cards = [
            card(suit=Suit.DIAMONDS, rank=Rank.FOUR),
            card(suit=Suit.CLUBS, rank=Rank.ACE),
            card(suit=Suit.DIAMONDS, rank=Rank.ACE),
            card(suit=Suit.HEARTS, rank=Rank.FIVE),
            card(suit=Suit.SPADES, rank=Rank.SEVEN),
            ]
        evaluation_rules = EvaluationRules()
        hand_type, played_cards = asses_poker_hand(cards, evaluation_rules)

        self.assertEqual(hand_type, HandType.PAIR)
        self.assertEqual(played_cards, [card for card in cards if card.is_rank(Rank.ACE)])
    

    def test_stones(self):
        card = self.factory.card
        cards = [
            card(suit=Suit.DIAMONDS, rank=Rank.FOUR),
            card(suit=Suit.CLUBS, rank=Rank.ACE, enhancement=Enhancement.STONE),
            card(suit=Suit.DIAMONDS, rank=Rank.KING),
            card(suit=Suit.HEARTS, rank=Rank.FIVE),
            card(suit=Suit.SPADES, rank=Rank.SEVEN),
            ]
        evaluation_rules = EvaluationRules()
        hand_type, played_cards = asses_poker_hand(cards, evaluation_rules)

        self.assertEqual(hand_type, HandType.HIGH_CARD)
        self.assertEqual(played_cards, [cards[2]])

    def test_all_stones(self):
        card = self.factory.card
        cards = [
            card(suit=Suit.DIAMONDS, rank=Rank.FOUR, enhancement=Enhancement.STONE),
            card(suit=Suit.CLUBS, rank=Rank.ACE, enhancement=Enhancement.STONE),
            card(suit=Suit.DIAMONDS, rank=Rank.KING, enhancement=Enhancement.STONE),
            card(suit=Suit.HEARTS, rank=Rank.FIVE, enhancement=Enhancement.STONE),
            card(suit=Suit.SPADES, rank=Rank.SEVEN, enhancement=Enhancement.STONE),
            ]
        evaluation_rules = EvaluationRules()
        hand_type, played_cards = asses_poker_hand(cards, evaluation_rules)

        self.assertEqual(hand_type, HandType.HIGH_CARD)
        self.assertEqual(played_cards, [])


if __name__ == '__main__':
    unittest.main()