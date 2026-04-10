

import unittest
import sys
from pathlib import Path

sys.path.append(Path(__file__).parent.parent)

from card import Card, CardData
from board import Board
from definitions import *
from jokers import *
from poker import asses_poker_hand
from evaluation_rules import EvaluationRules


class TestSimple(unittest.TestCase):
    def test_highcard(self):
        cards = [
            Card(CardData(suit=Suit.DIAMONDS, rank=Rank.FOUR)),
            Card(CardData(suit=Suit.DIAMONDS, rank=Rank.FIVE)),
            Card(CardData(suit=Suit.CLUBS, rank=Rank.SIX)),
            Card(CardData(suit=Suit.DIAMONDS, rank=Rank.ACE)),
            Card(CardData(suit=Suit.DIAMONDS, rank=Rank.EIGHT)),
            ]
        evaluation_rules = EvaluationRules()
        hand_type, played_cards = asses_poker_hand(cards, evaluation_rules)
        self.assertEqual(hand_type, HandType.HIGH_CARD)
        self.assertEqual(played_cards, [cards[3]])


    def test_flush_four_fingers(self):
        cards = [
            Card(CardData(suit=Suit.DIAMONDS, rank=Rank.FOUR)),
            Card(CardData(suit=Suit.DIAMONDS, rank=Rank.FIVE)),
            Card(CardData(suit=Suit.CLUBS, rank=Rank.SIX)),
            Card(CardData(suit=Suit.DIAMONDS, rank=Rank.ACE)),
            Card(CardData(suit=Suit.DIAMONDS, rank=Rank.EIGHT)),
            ]
        evaluation_rules = EvaluationRules(fingers=4)
        hand_type, played_cards = asses_poker_hand(cards, evaluation_rules)
        self.assertEqual(hand_type, HandType.FLUSH)
        self.assertEqual(played_cards, [card for card in cards if card.is_suit(Suit.DIAMONDS)])


    def test_straight_flush_four_fingers(self):
        cards = [
            Card(CardData(suit=Suit.DIAMONDS, rank=Rank.FOUR)),
            Card(CardData(suit=Suit.DIAMONDS, rank=Rank.FIVE)),
            Card(CardData(suit=Suit.DIAMONDS, rank=Rank.SIX)),
            Card(CardData(suit=Suit.DIAMONDS, rank=Rank.ACE)),
            Card(CardData(suit=Suit.DIAMONDS, rank=Rank.SEVEN)),
            ]
        evaluation_rules = EvaluationRules(fingers=4)
        hand_type, played_cards = asses_poker_hand(cards, evaluation_rules)
        self.assertEqual(hand_type, HandType.STRAIGHT_FLUSH)
        self.assertEqual(played_cards, [card for card in cards if not card.is_rank(Rank.ACE)])


    def test_four(self):
        cards = [
            Card(CardData(suit=Suit.DIAMONDS, rank=Rank.FOUR)),
            Card(CardData(suit=Suit.CLUBS, rank=Rank.ACE)),
            Card(CardData(suit=Suit.DIAMONDS, rank=Rank.ACE)),
            Card(CardData(suit=Suit.HEARTS, rank=Rank.ACE)),
            Card(CardData(suit=Suit.SPADES, rank=Rank.ACE)),
            ]
        evaluation_rules = EvaluationRules()
        hand_type, played_cards = asses_poker_hand(cards, evaluation_rules)

        self.assertEqual(hand_type, HandType.FOUR_OF_A_KIND)
        self.assertEqual(played_cards, [card for card in cards if card.is_rank(Rank.ACE)])
    

    def test_three(self):
        cards = [
            Card(CardData(suit=Suit.DIAMONDS, rank=Rank.FOUR)),
            Card(CardData(suit=Suit.CLUBS, rank=Rank.ACE)),
            Card(CardData(suit=Suit.DIAMONDS, rank=Rank.ACE)),
            Card(CardData(suit=Suit.HEARTS, rank=Rank.ACE)),
            Card(CardData(suit=Suit.SPADES, rank=Rank.FIVE)),
            ]
        evaluation_rules = EvaluationRules()
        hand_type, played_cards = asses_poker_hand(cards, evaluation_rules)

        self.assertEqual(hand_type, HandType.THREE_OF_A_KIND)
        self.assertEqual(played_cards, [card for card in cards if card.is_rank(Rank.ACE)])


    def test_straight(self):
        cards = [
            Card(CardData(suit=Suit.HEARTS, rank=Rank.SIX)),
            Card(CardData(suit=Suit.DIAMONDS, rank=Rank.THREE)),
            Card(CardData(suit=Suit.CLUBS, rank=Rank.FIVE)),
            Card(CardData(suit=Suit.DIAMONDS, rank=Rank.FOUR)),
            Card(CardData(suit=Suit.SPADES, rank=Rank.SEVEN)),
            ]
        evaluation_rules = EvaluationRules()
        hand_type, played_cards = asses_poker_hand(cards, evaluation_rules)

        self.assertEqual(hand_type, HandType.STRAIGHT)
        self.assertEqual(played_cards, cards)


    def test_straight_skipping(self):
        cards = [
            Card(CardData(suit=Suit.HEARTS, rank=Rank.JACK)),
            Card(CardData(suit=Suit.DIAMONDS, rank=Rank.THREE)),
            Card(CardData(suit=Suit.CLUBS, rank=Rank.SEVEN)),
            Card(CardData(suit=Suit.DIAMONDS, rank=Rank.FIVE)),
            Card(CardData(suit=Suit.SPADES, rank=Rank.NINE)),
            ]
        evaluation_rules = EvaluationRules(straight_skip=True)
        hand_type, played_cards = asses_poker_hand(cards, evaluation_rules)

        self.assertEqual(hand_type, HandType.STRAIGHT)
        self.assertEqual(played_cards, cards)


    def test_straight_four_1(self):
        cards = [
            Card(CardData(suit=Suit.HEARTS, rank=Rank.THREE)),
            Card(CardData(suit=Suit.DIAMONDS, rank=Rank.FOUR)),
            Card(CardData(suit=Suit.CLUBS, rank=Rank.FIVE)),
            Card(CardData(suit=Suit.DIAMONDS, rank=Rank.SIX)),
            Card(CardData(suit=Suit.SPADES, rank=Rank.KING)),
            ]
        evaluation_rules = EvaluationRules(fingers=4)
        hand_type, played_cards = asses_poker_hand(cards, evaluation_rules)

        self.assertEqual(hand_type, HandType.STRAIGHT)
        self.assertEqual(played_cards, [card for card in cards if not card.is_rank(Rank.KING)])


    def test_straight_four_2(self):
        cards = [
            Card(CardData(suit=Suit.SPADES, rank=Rank.TWO)),
            Card(CardData(suit=Suit.HEARTS, rank=Rank.SEVEN)),
            Card(CardData(suit=Suit.DIAMONDS, rank=Rank.FOUR)),
            Card(CardData(suit=Suit.CLUBS, rank=Rank.FIVE)),
            Card(CardData(suit=Suit.DIAMONDS, rank=Rank.SIX)),
            ]
        evaluation_rules = EvaluationRules(fingers=4)
        hand_type, played_cards = asses_poker_hand(cards, evaluation_rules)

        self.assertEqual(hand_type, HandType.STRAIGHT)
        self.assertEqual(played_cards, [cards[1], cards[2], cards[3], cards[4]])
    

    def test_straight_four_3(self):
        cards = [
            Card(CardData(suit=Suit.SPADES, rank=Rank.FIVE)),
            Card(CardData(suit=Suit.HEARTS, rank=Rank.SIX)),
            Card(CardData(suit=Suit.DIAMONDS, rank=Rank.SEVEN)),
            Card(CardData(suit=Suit.CLUBS, rank=Rank.EIGHT)),
            Card(CardData(suit=Suit.DIAMONDS, rank=Rank.EIGHT)),
            ]
        evaluation_rules = EvaluationRules(fingers=4)
        hand_type, played_cards = asses_poker_hand(cards, evaluation_rules)

        self.assertEqual(hand_type, HandType.STRAIGHT)
        self.assertEqual(played_cards, [cards[0], cards[1], cards[2], cards[3]])


    def test_straight_false(self):
        cards = [
            Card(CardData(suit=Suit.SPADES, rank=Rank.FIVE)),
            Card(CardData(suit=Suit.HEARTS, rank=Rank.SIX)),
            Card(CardData(suit=Suit.DIAMONDS, rank=Rank.EIGHT)),
            Card(CardData(suit=Suit.CLUBS, rank=Rank.NINE)),
            Card(CardData(suit=Suit.DIAMONDS, rank=Rank.TEN)),
            ]
        evaluation_rules = EvaluationRules(fingers=4)
        hand_type, played_cards = asses_poker_hand(cards, evaluation_rules)

        self.assertEqual(hand_type, HandType.HIGH_CARD)
        self.assertEqual(played_cards, [cards[4]])


    def test_straight_aces_high(self):
        cards = [
            Card(CardData(suit=Suit.SPADES, rank=Rank.FIVE)),
            Card(CardData(suit=Suit.HEARTS, rank=Rank.JACK)),
            Card(CardData(suit=Suit.DIAMONDS, rank=Rank.ACE)),
            Card(CardData(suit=Suit.DIAMONDS, rank=Rank.QUEEN)),
            Card(CardData(suit=Suit.CLUBS, rank=Rank.KING)),
            ]
        evaluation_rules = EvaluationRules(fingers=4)
        hand_type, played_cards = asses_poker_hand(cards, evaluation_rules)

        self.assertEqual(hand_type, HandType.STRAIGHT)
        self.assertEqual(played_cards, [cards[1], cards[2], cards[3], cards[4]])

    def test_straight_aces_low(self):
        cards = [
            Card(CardData(suit=Suit.SPADES, rank=Rank.FOUR)),
            Card(CardData(suit=Suit.HEARTS, rank=Rank.THREE)),
            Card(CardData(suit=Suit.DIAMONDS, rank=Rank.ACE)),
            Card(CardData(suit=Suit.DIAMONDS, rank=Rank.TWO)),
            Card(CardData(suit=Suit.CLUBS, rank=Rank.KING)),
            ]
        evaluation_rules = EvaluationRules(fingers=4)
        hand_type, played_cards = asses_poker_hand(cards, evaluation_rules)

        self.assertEqual(hand_type, HandType.STRAIGHT)
        self.assertEqual(played_cards, [cards[0], cards[1], cards[2], cards[3]])


    def test_two_pair(self):
        cards = [
            Card(CardData(suit=Suit.DIAMONDS, rank=Rank.FOUR)),
            Card(CardData(suit=Suit.CLUBS, rank=Rank.ACE)),
            Card(CardData(suit=Suit.DIAMONDS, rank=Rank.ACE)),
            Card(CardData(suit=Suit.HEARTS, rank=Rank.FIVE)),
            Card(CardData(suit=Suit.SPADES, rank=Rank.FIVE)),
            ]
        evaluation_rules = EvaluationRules()
        hand_type, played_cards = asses_poker_hand(cards, evaluation_rules)

        self.assertEqual(hand_type, HandType.TWO_PAIR)
        self.assertEqual(played_cards, [card for card in cards if card.is_rank(Rank.ACE) or card.is_rank(Rank.FIVE)])


    def test_pair(self):
        cards = [
            Card(CardData(suit=Suit.DIAMONDS, rank=Rank.FOUR)),
            Card(CardData(suit=Suit.CLUBS, rank=Rank.ACE)),
            Card(CardData(suit=Suit.DIAMONDS, rank=Rank.ACE)),
            Card(CardData(suit=Suit.HEARTS, rank=Rank.FIVE)),
            Card(CardData(suit=Suit.SPADES, rank=Rank.SEVEN)),
            ]
        evaluation_rules = EvaluationRules()
        hand_type, played_cards = asses_poker_hand(cards, evaluation_rules)

        self.assertEqual(hand_type, HandType.PAIR)
        self.assertEqual(played_cards, [card for card in cards if card.is_rank(Rank.ACE)])
    

    def test_stones(self):
        cards = [
            Card(CardData(suit=Suit.DIAMONDS, rank=Rank.FOUR)),
            Card(CardData(suit=Suit.CLUBS, rank=Rank.ACE, enhancement=Enhancement.STONE)),
            Card(CardData(suit=Suit.DIAMONDS, rank=Rank.KING)),
            Card(CardData(suit=Suit.HEARTS, rank=Rank.FIVE)),
            Card(CardData(suit=Suit.SPADES, rank=Rank.SEVEN)),
            ]
        evaluation_rules = EvaluationRules()
        hand_type, played_cards = asses_poker_hand(cards, evaluation_rules)

        self.assertEqual(hand_type, HandType.HIGH_CARD)
        self.assertEqual(played_cards, [cards[2]])


if __name__ == '__main__':
    unittest.main()