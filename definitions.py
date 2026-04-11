
from dataclasses import dataclass
from enum import Enum

class Suit(Enum):
    HEARTS = 'Hearts'
    DIAMONDS = 'Diamonds'
    CLUBS = 'Clubs'
    SPADES = 'Spades'
    ANY = 'Any'
    NONE = 'None'

class Rank(Enum):
    NONE = 0
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14

base_value_map = {
    Rank.TWO: 2,
    Rank.THREE: 3,
    Rank.FOUR: 4,
    Rank.FIVE: 5,
    Rank.SIX: 6,
    Rank.SEVEN: 7,
    Rank.EIGHT: 8,
    Rank.NINE: 9,
    Rank.TEN: 10,
    Rank.JACK: 10,
    Rank.QUEEN: 10,
    Rank.KING: 10,
    Rank.ACE: 11
}

class Enhancement(Enum):
    NONE = 0
    BONUS = 1
    MULT = 2
    WILD = 3
    GLASS = 4
    STEEL = 5
    STONE = 6
    GOLD = 7
    LUCKY = 8


class Seal(Enum):
    NONE = 0
    GOLD = 1
    RED = 2
    BLUE = 3
    PURPLE = 4


class Edition(Enum):
    BASE = 'Base'
    FOIL = 'Foil'
    HOLOGRAPHIC = 'Holographic'
    POLYCHROME = 'Polychrome'
    NEGATIVE = 'Negative'


class Rarity(Enum):
    COMMON = 'Common'
    UNCOMMON = 'Uncommon'
    RARE = 'Rare'
    LEGENDARY = 'Legendary'


class HandType(Enum):
    HIGH_CARD = 'High Card'
    PAIR = 'Pair'
    TWO_PAIR = 'Two Pair'
    THREE_OF_A_KIND = 'Three of a Kind'
    STRAIGHT = 'Straight'
    FLUSH = 'Flush'
    FULL_HOUSE = 'Full House'
    FOUR_OF_A_KIND = 'Four of a Kind'
    STRAIGHT_FLUSH = 'Straight Flush'
    FIVE_OF_A_KIND = 'Five of a Kind'
    FLUSH_HOUSE = 'Flush House'
    FLUSH_FIVE = 'Flush Five'


class CalcMode(Enum):
    BEST = 'Best'
    WORST = 'Worst'
    SIMULATE = 'Simulate'


level_dict = {
    HandType.FLUSH_FIVE: (160, 16, 50, 3),
    HandType.FLUSH_HOUSE: (140, 14, 40, 4),
    HandType.FIVE_OF_A_KIND: (120, 12, 35, 3),
    HandType.STRAIGHT_FLUSH: (100, 8, 40, 4),
    HandType.FOUR_OF_A_KIND: (60, 7, 20, 3),
    HandType.FULL_HOUSE: (40, 4, 25, 2),
    HandType.FLUSH: (35, 4, 15, 2),
    HandType.STRAIGHT: (30, 4, 20, 3),
    HandType.THREE_OF_A_KIND: (30, 3, 20, 2),
    HandType.TWO_PAIR: (20, 2, 20, 1),
    HandType.PAIR: (10, 2, 15, 1),
    HandType.HIGH_CARD: (5, 1, 10, 1),
}


def get_hand_level_chips_mult(hand_type: HandType, level: int) -> tuple[int, int]:
    chips = level_dict[hand_type][0] + (level - 1) * level_dict[hand_type][2]
    mult = level_dict[hand_type][1] + (level - 1) * level_dict[hand_type][3]
    return chips, mult

@dataclass
class BoardData:
    hand_size: int = 8
    total_hands: int = 4
    remaining_hands: int = 4
    discards: int = 3
    remaining_discards: int = 3
    money: int = 10
    joker_spaces = 5