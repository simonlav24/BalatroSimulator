


from definitions import *
from card import Card, CardData

MAX_CARDS = 5

def _is_flush(cards: list[Card], fingers=5) -> bool:
    evaluated_suit = cards[0].get_suit()
    flush_len = 1
    for card in cards[1:]:
        if card.get_suit() == Suit.ANY:
            flush_len += 1
            continue
        if card.get_suit() != evaluated_suit and evaluated_suit == Suit.ANY:
            evaluated_suit = card.get_suit()
        elif card.get_suit() != evaluated_suit:
            continue
        flush_len += 1
    return flush_len >= fingers

def _is_count_max_ranks(cards: list[Card], amount: int) -> bool:
    ranks = {}
    for card in cards:
        if card.get_rank() == Rank.NONE:
            continue
        if card.get_rank() not in ranks:
            ranks[card.get_rank()] = 0
        ranks[card.get_rank()] += 1
    return any(rank == amount for rank in ranks.values())

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

def _is_straight(cards: list[Card], fingers=5, skipping=False) -> bool:
    ranks = set(card.get_rank().value for card in cards if card.get_rank() != Rank.NONE)
    ranks = list(ranks)
    ranks.sort()
    straight_len = 1
    prev_rank = ranks[0]
    for rank in ranks[1:]:
        if rank == prev_rank + 1:
            straight_len += 1
        elif skipping and rank == prev_rank + 2:
            straight_len += 1
        else:
            straight_len = 1
        prev_rank = rank

    if straight_len >= fingers:
        return True
    return False



def asses_poker_hand(cards: list[Card], evaluation_rules: HandEvaluationRules) -> tuple[HandType, list[Card]]:
    '''asses poker hand, return type and playing cards'''

    is_flush = _is_flush(cards, 5)
    is_same_rank = _is_count_max_ranks(cards, 5)

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
    
    is_flush = _is_flush(cards, evaluation_rules.fingers)
    is_straight = _is_straight(cards, evaluation_rules.fingers, evaluation_rules.straight_skip)
    
    # straight flush
    if is_flush and is_straight:
        return (HandType.STRAIGHT_FLUSH, cards)

    # four of a kind
    if _is_count_max_ranks(cards, 4):
        return (HandType.FOUR_OF_A_KIND, cards)

    # full house
    if is_house:
        return (HandType.FULL_HOUSE, cards)

    # flush
    if is_flush:
        return (HandType.FLUSH, cards)
    
    # straight
    if is_straight:
        return (HandType.STRAIGHT, cards)
    
    # three of a kind
    if _is_count_max_ranks(cards, 3):
        return (HandType.THREE_OF_A_KIND, cards)
    
    # two pair
    ranks = {}
    for card in cards:
        if card.get_rank() == Rank.NONE:
            continue
        if card.get_rank() not in ranks:
            ranks[card.get_rank()] = 0
        ranks[card.get_rank()] += 1
    pair_count = sum(1 for rank in ranks.values() if rank == 2)
    if pair_count == 2:
        return (HandType.TWO_PAIR, cards)
    
    # pair
    if pair_count == 1:
        return (HandType.PAIR, cards)
    
    # high card
    return (HandType.HIGH_CARD, cards)


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