

from enum import Enum
from collections import Counter

from definitions import *
from card import Card, CardData
from evaluation_rules import EvaluationRules

class HandEvaluator:
    def __init__(self, cards: list[Card], evaluation_rules: EvaluationRules):
        self.cards = [card for card in cards if card.get_rank() != Rank.NONE]
        self.eval = evaluation_rules

        self.ranks = sorted((card.get_rank().value for card in self.cards))
        self.suits = {self.eval.get_suit(card): 0 for card in self.cards if self.eval.get_suit(card) != Suit.ANY}
        for card in self.cards:
            if self.eval.get_suit(card) == Suit.ANY:
                for key in self.suits.keys():
                    self.suits[key] += 1
                continue
            self.suits[self.eval.get_suit(card)] += 1
        self.rank_counts = Counter(self.ranks)
        self.ranks = sorted(set(self.ranks))

    # =================== utilities ===================
    def _get_flush(self, fingers) -> Suit | None:
        for suit, count in self.suits.items():
            if count >= fingers:
                return suit
        return None

    def _get_straight(self) -> list[Card] | None:
        if len(self.cards) < self.eval.fingers:
            return None
        straight_ranks = self.ranks.copy()
        valid_diffs = [1, 2] if self.eval.straight_skip else [1]
        
        checks = [straight_ranks]
        if 14 in straight_ranks:
            second = straight_ranks.copy()
            second.remove(14)
            second.insert(0, 1)
            checks.append(second)

        is_straight = False
        for check in checks:
            diffs = [b - a in valid_diffs for a, b in zip(check, check[1:])]
            while diffs and not diffs[0]:
                check.pop(0)
                diffs.pop(0)
            while diffs and not diffs[-1]:
                check.pop()
                diffs.pop()
            
            if not all(diffs) or len(diffs) < self.eval.fingers - 1:
                continue
            is_straight = True
            straight_ranks = check

        if not is_straight:
            return None

        if 1 in straight_ranks:
            straight_ranks.remove(1)
            straight_ranks.append(14)

        straight = []
        used = []
        for card in self.cards:
            rank = card.get_rank().value
            if rank not in used and rank in straight_ranks:
                straight.append(card)
                used.append(rank)
        return straight

    # =================== checkers ===================
    def check_flush_five(self) -> list[Card] | None:
        flush_suit = self._get_flush(5)
        is_five_of_a_kind = any(count == 5 for count in self.rank_counts.values())
        if flush_suit != None and is_five_of_a_kind:
            return self.cards
        return None

    def check_five_of_a_kind(self) -> list[Card] | None:
        if any(count == 5 for count in self.rank_counts.values()):
            return self.cards
        return None

    def check_flush_house(self) -> list[Card] | None:
        is_house = all(i in self.rank_counts.values() for i in [2, 3])
        flush_suit = self._get_flush(5)
        if is_house and flush_suit != None:
            return self.cards
        return None

    def check_straight_flush(self) -> list[Card] | None:
        flush_suit = self._get_flush(self.eval.fingers)
        straight_cards = self._get_straight()

        if (
            straight_cards != None and flush_suit != None and
            all([self.eval.is_suit(card, flush_suit) for card in straight_cards])
        ):
            return straight_cards
        return None

    def check_four_of_a_kind(self) -> list[Card] | None:
        rank = next((rank for rank, count in self.rank_counts.items() if count == 4), None)
        if rank is not None:
            return [card for card in self.cards if card.get_rank().value == rank]
        return None

    def check_full_house(self) -> list[Card] | None:
        if all(i in self.rank_counts.values() for i in [2, 3]):
            return self.cards
        return None

    def check_flush(self) -> list[Card] | None:
        flush_suit = self._get_flush(self.eval.fingers)
        if flush_suit != None:
            return [card for card in self.cards if self.eval.is_suit(card, flush_suit)]
        return None
    
    def check_straight(self) -> list[Card] | None:
        straight_cards = self._get_straight()
        if straight_cards is not None:
            return straight_cards
        return None
    
    def check_three_of_a_kind(self) -> list[Card] | None:
        rank = next((rank for rank, count in self.rank_counts.items() if count == 3), None)
        if rank is not None:
            return [card for card in self.cards if card.get_rank().value == rank]
        return None
    
    def check_two_pair(self) -> list[Card] | None:
        pairs_rank = [rank for rank, count in self.rank_counts.items() if count == 2]
        if len(pairs_rank) == 2:
            return [card for card in self.cards if card.get_rank().value in pairs_rank]
        return None
    
    def check_pair(self) -> list[Card] | None:
        rank = next((rank for rank, count in self.rank_counts.items() if count == 2), None)
        if rank is not None:
            return [card for card in self.cards if card.get_rank().value == rank]
        return None
    
    def check_high_card(self) -> list[Card] | None:
        if len(self.cards) == 0:
            return []
        max_rank = self.ranks[-1]
        for card in self.cards:
            if card.get_rank().value == max_rank:
                return [card]
        return []

    def get_evaluation(self) -> tuple[HandType, list[Card]]:
        checks = [
            (HandType.FLUSH_FIVE, self.check_flush_five),
            (HandType.FIVE_OF_A_KIND, self.check_five_of_a_kind),
            (HandType.FLUSH_HOUSE, self.check_flush_house),
            (HandType.STRAIGHT_FLUSH, self.check_straight_flush),
            (HandType.FOUR_OF_A_KIND, self.check_four_of_a_kind),
            (HandType.FULL_HOUSE, self.check_full_house),
            (HandType.FLUSH, self.check_flush),
            (HandType.STRAIGHT, self.check_straight),
            (HandType.THREE_OF_A_KIND, self.check_three_of_a_kind),
            (HandType.TWO_PAIR, self.check_two_pair),
            (HandType.PAIR, self.check_pair),
            (HandType.HIGH_CARD, self.check_high_card),
        ]
        for hand_type, check in checks:
            played_cards = check()
            if played_cards != None:
                return hand_type, played_cards
        return HandType.HIGH_CARD, []


def asses_poker_hand(cards: list[Card], evaluation_rules: EvaluationRules) -> tuple[HandType, list[Card]]:
    evaluator = HandEvaluator(cards, evaluation_rules)
    return evaluator.get_evaluation()

