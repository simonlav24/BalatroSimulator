

from dataclasses import dataclass

from card import Card
from definitions import Rank

@dataclass
class EvaluationRules:
    straight_skip: bool = False
    fingers: int = 5
    all_face: bool = False
    play_all_cards: bool = False

    def is_face_card(self, card: Card) -> bool:
        if self.all_face:
            return True
        return card.get_rank() in [Rank.JACK, Rank.QUEEN, Rank.KING]