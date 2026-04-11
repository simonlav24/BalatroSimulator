

from dataclasses import dataclass

from card import Card
from definitions import Rank, Suit

@dataclass
class EvaluationRules:
    straight_skip: bool = False
    fingers: int = 5
    all_face: bool = False
    play_all_cards: bool = False
    smeared: bool = False

    def is_face_card(self, card: Card) -> bool:
        if self.all_face:
            return True
        return card.get_rank() in [Rank.JACK, Rank.QUEEN, Rank.KING]

    def get_suit(self, card: Card) -> Suit:
        suit = card.get_suit()
        if self.smeared and suit == Suit.DIAMONDS:
            return Suit.HEARTS
        if self.smeared and suit == Suit.CLUBS:
            return Suit.SPADES
        return suit

    def is_suit(self, card: Card, suit: Suit) -> Suit:
        card_suit = card.get_suit()
        if card_suit == Suit.NONE or suit == Suit.NONE:
            return False
        if suit == Suit.ANY or card_suit == Suit.ANY:
            return True
        if self.smeared and all(s in [Suit.DIAMONDS, Suit.HEARTS] for s in [suit, card_suit]):
            return True
        if self.smeared and all(s in [Suit.CLUBS, Suit.SPADES] for s in [suit, card_suit]):
            return True
        return card_suit == suit
