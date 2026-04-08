


from definitions import *
from card import Card, CardData
from evaluation_rules import EvaluationRules

MAX_CARDS = 5

def _is_flush(cards: list[Card], fingers=5) -> tuple[bool, Suit, list[Card]]:
    is_flush = False
    cards_playing = []
    suits = [card.get_suit() for card in cards]
    any_count = [[suit for suit in suits if (suit == test_suit) or (suit == Suit.ANY)] for test_suit in Suit]
    maximum = max(any_count, key=len)
    if len(maximum) >= fingers:
        is_flush = True
    max_set = set(maximum)
    if Suit.ANY in max_set:
        max_set.remove(Suit.ANY)
    winning_suit = next(iter(max_set))
    if len(max_set) == 0:
        cards_playing = cards
    else:
        cards_playing = [card for card in cards if card.is_suit(winning_suit)]
    return is_flush, winning_suit, cards_playing


def _is_count_max_ranks(cards: list[Card], amount: int) -> tuple[bool, Rank]:
    ranks = {}
    for card in cards:
        if card.get_rank() == Rank.NONE:
            continue
        if card.get_rank() not in ranks:
            ranks[card.get_rank()] = 0
        ranks[card.get_rank()] += 1
    return any(rank == amount for rank in ranks.values()), next(iter([rank for rank, count in ranks.items() if count == amount]), None)

def _is_house(cards: list[Card]) -> bool:
    ranks = {}
    for card in cards:
        if card.get_rank() == Rank.NONE:
            continue
        if card.get_rank() not in ranks:
            ranks[card.get_rank()] = 0
        ranks[card.get_rank()] += 1
    ranks_values = list(ranks.values())
    return len(ranks) == 2 and any([ranks_values[0] == 2 and ranks_values[1] == 3, ranks_values[0] == 3 and ranks_values[1] == 2])

def _check_sequence(cards: list[Card], skipping=False) -> bool:
    prev_rank = cards[0].get_rank().value
    for card in cards[1:]:
        if not ((card.get_rank().value == prev_rank + 1) or (skipping and card.get_rank().value == prev_rank + 2)):
            return False
        prev_rank = card.get_rank().value
    return True 

def _is_straight(cards: list[Card], fingers=5, skipping=False) -> tuple[bool, list[Card]]:
    used_ranks = [Rank.NONE]
    unique_ranked_cards: list[Card] = []
    for card in cards:
        if card.get_rank() in used_ranks:
            continue
        else:
            used_ranks.append(card.get_rank())
            unique_ranked_cards.append(card)

    unique_ranked_cards.sort(key=lambda x: x.get_rank().value)
    if _check_sequence(unique_ranked_cards):
        return True, list(set(cards).intersection(unique_ranked_cards))
    if fingers < 5:
        if _check_sequence(unique_ranked_cards[:-1]):
            return True, [card for card in cards if card in unique_ranked_cards[:-1]]
        if _check_sequence(unique_ranked_cards[1:]):
            return True, [card for card in cards if card in unique_ranked_cards[1:]]
    return False, None



def asses_poker_hand(cards: list[Card], evaluation_rules: EvaluationRules) -> tuple[HandType, list[Card]]:
    '''asses poker hand, return type and playing cards'''

    is_flush, _, _ = _is_flush(cards, 5)
    is_same_rank, _ = _is_count_max_ranks(cards, 5)

    # flush five
    if len(cards) == MAX_CARDS and is_same_rank and is_flush:
        return (HandType.FLUSH_FIVE, cards)
    
    # five of a kind
    if len(cards) == MAX_CARDS and is_same_rank:
        return (HandType.FIVE_OF_A_KIND, cards)

    # flush house
    is_house = _is_house(cards)
    if is_house and is_flush:
        return (HandType.FLUSH_HOUSE, cards)
    
    is_flush, suit, flush_cards = _is_flush(cards, evaluation_rules.fingers)
    is_straight, straight_cards = _is_straight(cards, evaluation_rules.fingers, evaluation_rules.straight_skip)

    # straight flush
    if (
        is_flush and is_straight and
        all([card.is_suit(suit) for card in straight_cards])
    ):
        return (HandType.STRAIGHT_FLUSH, straight_cards)

    # four of a kind
    is_four_of_a_kind, rank = _is_count_max_ranks(cards, 4)
    if is_four_of_a_kind:
        return (HandType.FOUR_OF_A_KIND, [card for card in cards if card.is_rank(rank)])

    # full house
    if is_house:
        return (HandType.FULL_HOUSE, cards)

    # flush
    if is_flush:
        return (HandType.FLUSH, flush_cards)
    
    # straight
    if is_straight:
        return (HandType.STRAIGHT, straight_cards)
    
    # three of a kind
    is_three_of_a_kind, rank = _is_count_max_ranks(cards, 3)
    if is_three_of_a_kind:
        return (HandType.THREE_OF_A_KIND, [card for card in cards if card.is_rank(rank)])
    
    # two pair
    ranks = {}
    for card in cards:
        if card.get_rank() == Rank.NONE:
            continue
        if card.get_rank() not in ranks:
            ranks[card.get_rank()] = 0
        ranks[card.get_rank()] += 1
    ranks = [rank for rank, count in ranks.items() if count == 2]
    if len(ranks) == 2:
        return (HandType.TWO_PAIR, [card for card in cards if card.get_rank() in ranks])
    
    # pair
    if len(ranks) == 1:
        return (HandType.PAIR, [card for card in cards if card.get_rank() in ranks])
    
    # high card
    return (HandType.HIGH_CARD, [max(cards, key=lambda x: x.get_rank().value)])


if __name__ == '__main__':
    # test hand evaluation
    from random import choice
    
    cards = [
        Card(CardData(suit=Suit.HEARTS, rank=Rank.THREE, enhancement=Enhancement.WILD)),
        Card(CardData(suit=Suit.SPADES, rank=Rank.TWO, enhancement=Enhancement.WILD)),
        Card(CardData(suit=Suit.HEARTS, rank=Rank.KING, )),
        Card(CardData(suit=Suit.SPADES, rank=Rank.KING, enhancement=Enhancement.WILD)),
        Card(CardData(suit=Suit.CLUBS, rank=Rank.KING,)),
    ]

    print(asses_poker_hand(cards))