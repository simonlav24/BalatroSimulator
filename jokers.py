

import logging
from random import randint

from joker import Joker, BoardVision
from card import Card
from definitions import *
from poker import HandEvaluator

logger = logging.getLogger(__name__)

class JokerJimbo(Joker):
    def __init__(self):
        super().__init__(name='Joker')
        self.data.cost = 2

    def trigger_on_end_hand(self, board: BoardVision):
        board.add_mult(4)
        logger.info(f'{self.data.name} added 4 mult')
        super().trigger_on_end_hand(board)


class JokerGreedy(Joker):
    def __init__(self):
        super().__init__(name='Greedy Joker')
        self.data.cost = 5

    def trigger_on_play_card(self, card: Card, board: BoardVision):
        if card.is_suit(Suit.DIAMONDS):
            board.add_mult(3)
            logger.info(f'{self.data.name} added 3 mult')
        super().trigger_on_play_card(board)


class JokerLusty(Joker):
    def __init__(self):
        super().__init__(name='Lusty Joker')
        self.data.cost = 5

    def trigger_on_play_card(self, card: Card, board: BoardVision):
        if card.is_suit(Suit.HEARTS):
            board.add_mult(3)
            logger.info(f'{self.data.name} added 3 mult')
        super().trigger_on_play_card(board)


class JokerWrathful(Joker):
    def __init__(self):
        super().__init__(name='Wrathful Joker')
        self.data.cost = 5

    def trigger_on_play_card(self, card: Card, board: BoardVision):
        if card.is_suit(Suit.SPADES):
            board.add_mult(3)
            logger.info(f'{self.data.name} added 3 mult')
        super().trigger_on_play_card(board)


class JokerGluttonous(Joker):
    def __init__(self):
        super().__init__(name='Gluttonous Joker')
        self.data.cost = 5

    def trigger_on_play_card(self, card: Card, board: BoardVision):
        if card.is_suit(Suit.CLUBS):
            board.add_mult(3)
            logger.info(f'{self.data.name} added 3 mult')
        super().trigger_on_play_card(board)


class JokerJollyJoker(Joker):
    def __init__(self):
        super().__init__(name='Jolly Joker')
        self.data.cost = 3

    def trigger_on_end_hand(self, board: BoardVision):
        evaluator = HandEvaluator(board.get_played_cards(), board.get_evaluation_rules())
        if evaluator.check_pair() is not None:
            board.add_mult(8)
            logger.info(f'{self.data.name} added 8 mult')
        super().trigger_on_end_hand(board)


class JokerZanyJoker(Joker):
    def __init__(self):
        super().__init__(name='Zany Joker')
        self.data.cost = 4

    def trigger_on_end_hand(self, board: BoardVision):
        evaluator = HandEvaluator(board.get_played_cards(), board.get_evaluation_rules())
        if evaluator.check_three_of_a_kind() is not None:
            board.add_mult(12)
            logger.info(f'{self.data.name} added 12 mult')
        super().trigger_on_end_hand(board)


class JokerMadJoker(Joker):
    def __init__(self):
        super().__init__(name='Mad Joker')
        self.data.cost = 4

    def trigger_on_end_hand(self, board: BoardVision):
        evaluator = HandEvaluator(board.get_played_cards(), board.get_evaluation_rules())
        if evaluator.check_two_pair() is not None:
            board.add_mult(10)
            logger.info(f'{self.data.name} added 10 mult')
        super().trigger_on_end_hand(board)


class JokerCrazyJoker(Joker):
    def __init__(self):
        super().__init__(name='Crazy Joker')
        self.data.cost = 4

    def trigger_on_end_hand(self, board: BoardVision):
        evaluator = HandEvaluator(board.get_played_cards(), board.get_evaluation_rules())
        if evaluator.check_straight() is not None:
            board.add_mult(12)
            logger.info(f'{self.data.name} added 12 mult')
        super().trigger_on_end_hand(board)


class JokerDrollJoker(Joker):
    def __init__(self):
        super().__init__(name='Droll Joker')
        self.data.cost = 4

    def trigger_on_end_hand(self, board: BoardVision):
        evaluator = HandEvaluator(board.get_played_cards(), board.get_evaluation_rules())
        if evaluator.check_flush() is not None:
            board.add_mult(10)
            logger.info(f'{self.data.name} added 10 mult')
        super().trigger_on_end_hand(board)


class JokerSlyJoker(Joker):
    def __init__(self):
        super().__init__(name='Sly Joker')
        self.data.cost = 3

    def trigger_on_end_hand(self, board: BoardVision):
        evaluator = HandEvaluator(board.get_played_cards(), board.get_evaluation_rules())
        if evaluator.check_pair() is not None:
            board.add_chips(50)
            logger.info(f'{self.data.name} added 50 chips')
        super().trigger_on_end_hand(board)
    

class JokerWilyJoker(Joker):
    def __init__(self):
        super().__init__(name='Wily Joker')
        self.data.cost = 4

    def trigger_on_end_hand(self, board: BoardVision):
        evaluator = HandEvaluator(board.get_played_cards(), board.get_evaluation_rules())
        if evaluator.check_three_of_a_kind() is not None:
            board.add_chips(100)
            logger.info(f'{self.data.name} added 100 chips')
        super().trigger_on_end_hand(board)


class JokerCleverJoker(Joker):
    def __init__(self):
        super().__init__(name='Clever Joker')
        self.data.cost = 4

    def trigger_on_end_hand(self, board: BoardVision):
        evaluator = HandEvaluator(board.get_played_cards(), board.get_evaluation_rules())
        if evaluator.check_two_pair() is not None:
            board.add_chips(80)
            logger.info(f'{self.data.name} added 80 chips')
        super().trigger_on_end_hand(board)


class JokerDeviousJoker(Joker):
    def __init__(self):
        super().__init__(name='Devious Joker')
        self.data.cost = 4

    def trigger_on_end_hand(self, board: BoardVision):
        evaluator = HandEvaluator(board.get_played_cards(), board.get_evaluation_rules())
        if evaluator.check_straight() is not None:
            board.add_chips(100)
            logger.info(f'{self.data.name} added 100 chips')
        super().trigger_on_end_hand(board)


class JokerCraftyJoker(Joker):
    def __init__(self):
        super().__init__(name='Crafty Joker')
        self.data.cost = 4

    def trigger_on_end_hand(self, board: BoardVision):
        evaluator = HandEvaluator(board.get_played_cards(), board.get_evaluation_rules())
        if evaluator.check_flush() is not None:
            board.add_chips(80)
            logger.info(f'{self.data.name} added 80 chips')
        super().trigger_on_end_hand(board)


class JokerHalfJoker(Joker):
    def __init__(self):
        super().__init__(name='Half Joker')
        self.data.cost = 5

    def trigger_on_end_hand(self, board: BoardVision):
        if len(board.get_selected_cards()) <= 3:
            board.add_mult(20)
            logger.info(f'{self.data.name} added 20 mult')
        super().trigger_on_end_hand(board)


class JokerStencil(Joker):
    def __init__(self):
        super().__init__(name='Joker Stencil')
        self.data.cost = 8
        self.rarity = Rarity.UNCOMMON

    def trigger_on_end_hand(self, board: BoardVision):
        mult = board.get_data().joker_spaces - len(board.get_jokers())
        if mult > 1:
            board.add_time_mult(mult)
            logger.info(f'{self.data.name} added {mult} time-mult')
        super().trigger_on_end_hand(board)


class JokerFourFingers(Joker):
    def __init__(self):
        super().__init__(name='Four Fingers')
        self.data.cost = 7
        self.rarity = Rarity.UNCOMMON

    def change_evaluation_rules(self, board: BoardVision):
        board.get_evaluation_rules().fingers = 4

# todo:
class JokerMime(Joker):
    def __init__(self):
        super().__init__(name='Mime')
        self.data.cost = 5
        self.rarity = Rarity.UNCOMMON
    
    def get_hand_card_retriggers(self, card: Card, board: BoardVision) -> int:
        return 1


class JokerCreditCard(Joker):
    def __init__(self):
        super().__init__(name='Credit Card')
        self.data.cost = 1


class JokerCeremonialDagger(Joker):
    def __init__(self):
        super().__init__(name='Ceremonial Dagger')
        self.data.cost = 6
        self.mult = 0

    def trigger_on_end_hand(self, board: BoardVision):
        board.add_mult(self.mult)
        logger.info(f'{self.data.name} added {self.mult} mult')
        super().trigger_on_end_hand(board)


class JokerBanner(Joker):
    def __init__(self):
        super().__init__(name='Banner')
        self.data.cost = 5

    def trigger_on_end_hand(self, board: BoardVision):
        chips = board.get_data().remaining_discards * 30
        board.add_chips(chips)
        logger.info(f'{self.data.name} added {chips} chips')
        super().trigger_on_end_hand(board)


class JokerMysticSummit(Joker):
    def __init__(self):
        super().__init__(name='Mystic Summit')
        self.data.cost = 5

    def trigger_on_end_hand(self, board: BoardVision) -> None:
        if board.get_data().remaining_discards == 0:
            board.add_mult(15)
            logger.info(f'{self.data.name} added 15 mult')
        super().trigger_on_end_hand(board)


class JokerMarbleJoker(Joker):
    def __init__(self):
        super().__init__(name='Marble Joker')
        self.data.cost = 6
        self.rarity = Rarity.UNCOMMON


class JokerLoyaltyCard(Joker):
    def __init__(self):
        super().__init__(name='Loyalty Card')
        self.data.cost = 5
        self.rarity = Rarity.UNCOMMON
        self.count = 1
    
    def trigger_on_end_hand(self, board: BoardVision) -> None:
        self.count -= 1
        if self.count == 0:
            self.count = 6
            board.add_time_mult(4)
            logger.info(f'{self.data.name} added 4 time-mult')
        super().trigger_on_end_hand(board)


class Joker8Ball(Joker):
    def __init__(self):
        super().__init__(name='8 Ball')
        self.data.cost = 5


class JokerMisprint(Joker):
    def __init__(self):
        super().__init__(name='Misprint')
        self.data.cost = 4

    def trigger_on_end_hand(self, board: BoardVision):
        mode = board.get_mode()
        if mode == CalcMode.SIMULATE:
            mult = randint(0, 23)
            board.add_mult(mult)
            logger.info(f'{self.data.name} added {mult} mult')

        if mode == CalcMode.BEST:
            board.add_mult(23)
            logger.info(f'{self.data.name} added 23 mult')
        super().trigger_on_end_hand(board)


class JokerDusk(Joker):
    def __init__(self):
        super().__init__(name='Dusk')
        self.data.cost = 6
        self.rarity = Rarity.UNCOMMON

    def get_card_retriggers(self, card: Card, board: BoardVision) -> int:
        if board.get_data().remaining_hands == 0:
            return 1
        return 0


class JokerRaisedFist(Joker):
    def __init__(self):
        super().__init__(name='RaisedFist')
        self.data.cost = 5

    def trigger_on_end_hand(self, board: BoardVision):
        cards = [card for card in board.get_hand_cards() if card.get_rank() != Rank.NONE]
        cards.sort(key=lambda x: x.get_rank().value)
        mult = 2 * base_value_map[cards[0].get_rank()]
        board.add_mult(mult)
        logger.info(f'{self.data.name} added {mult} mult')
        super().trigger_on_end_hand(board)


class JokerChaosTheClown(Joker):
    def __init__(self):
        super().__init__(name='Chaos the Clown')
        self.data.cost = 4


class JokerFibonacci(Joker):
    def __init__(self):
        super().__init__(name='Fibonacci')
        self.data.cost = 8
        self.rarity = Rarity.UNCOMMON

    def trigger_on_play_card(self, card: Card, board: BoardVision):
        if card.get_rank() in [Rank.TWO, Rank.THREE, Rank.FIVE, Rank.EIGHT, Rank.ACE]:
            board.add_mult(8)
            logger.info(f'{self.data.name} added 8 mult')
        super().trigger_on_play_card(board)


class JokerSteelJoker(Joker):
    def __init__(self):
        super().__init__(name='Steel Joker')
        self.data.cost = 7
        self.rarity = Rarity.UNCOMMON

    def trigger_on_end_hand(self, board: BoardVision):
        mult = 0.2 * sum([card for card in board.get_full_deck() if card.data.enhancement == Enhancement.STEEL])
        board.add_time_mult(mult)
        logger.info(f'{self.data.name} added {mult} time-mult')
        super().trigger_on_end_hand(board)


class JokerScaryFace(Joker):
    def __init__(self):
        super().__init__(name='Scary Face')
        self.data.cost = 4

    def trigger_on_play_card(self, card: Card, board: BoardVision):
        if board.get_evaluation_rules().is_face_card(card):
            board.add_chips(30)
            logger.info(f'{self.data.name} added 30 chips')


class JokerAbstractJoker(Joker):
    def __init__(self):
        super().__init__(name='Abstract Joker')
        self.data.cost = 4

    def trigger_on_end_hand(self, board: BoardVision):
        mult = 3 * len(board.get_jokers())
        board.add_mult(mult)
        logger.info(f'{self.data.name} added {mult} mult')
        super().trigger_on_end_hand(board)


class JokerDelayedGratification(Joker):
    def __init__(self):
        super().__init__(name='Delayed Gratification')
        self.data.cost = 4


class JokerHack(Joker):
    def __init__(self):
        super().__init__(name='Hack')
        self.data.cost = 6
        self.rarity = Rarity.UNCOMMON

    def get_card_retriggers(self, card: Card, board: BoardVision) -> int:
        if card.get_rank() in [Rank.TWO, Rank.THREE, Rank.FOUR, Rank.FIVE]:
            return 1
        return 0


class JokerPareidolia(Joker):
    def __init__(self):
        super().__init__(name='Pareidolia')
        self.data.cost = 5
        self.rarity = Rarity.UNCOMMON

    def change_evaluation_rules(self, board: BoardVision) -> None:
        board.get_evaluation_rules().all_face = True


class JokerGrosMichel(Joker):
    def __init__(self):
        super().__init__(name='Gros Michel')
        self.data.cost = 5

    def trigger_on_end_hand(self, board: BoardVision) -> None:
        board.add_mult(15)
        logger.info(f'{self.data.name} added 15 mult')
        super().trigger_on_end_hand(board)


class JokerEvenSteven(Joker):
    def __init__(self):
        super().__init__(name='Even Steven')
        self.data.cost = 4

    def trigger_on_play_card(self, card: Card, board: BoardVision):
        if card.get_rank() in [Rank.TWO, Rank.FOUR, Rank.SIX, Rank.EIGHT, Rank.TEN]:
            board.add_mult(4)
            logger.info(f'{self.data.name} added 4 mult')
        super().trigger_on_play_card(board)


class JokerOddTodd(Joker):
    def __init__(self):
        super().__init__(name='Odd Todd')
        self.data.cost = 4

    def trigger_on_play_card(self, card: Card, board: BoardVision):
        if card.get_rank() in [Rank.ACE, Rank.THREE, Rank.FIVE, Rank.SEVEN, Rank.NINE]:
            board.add_chips(31)
            logger.info(f'{self.data.name} added 31 chips')
        super().trigger_on_play_card(board)


class JokerScholar(Joker):
    def __init__(self):
        super().__init__(name='Scholar')
        self.data.cost = 4

    def trigger_on_play_card(self, card: Card, board: BoardVision):
        if card.get_rank() == Rank.ACE:
            board.add_chips(20)
            board.add_mult(4)
            logger.info(f'{self.data.name} added 20 chips, 4 mult')
        super().trigger_on_play_card(board)


class JokerBusinessCard(Joker):
    def __init__(self):
        super().__init__(name='Business Card')
        self.data.cost = 4


class JokerSupernova(Joker):
    def __init__(self):
        super().__init__(name='Supernova')
        self.data.cost = 5
    
    def trigger_on_end_hand(self, board: BoardVision) -> None:
        mult = board.get_levels_table()[board.get_current_hand_type()]['played']
        if mult > 0:
            board.add_mult(mult)
            logger.info(f'{self.data.name} added {mult} mult')
        super().trigger_on_end_hand(board)


class JokerRideTheBus(Joker):
    def __init__(self):
        super().__init__(name='Ride the Bus')
        self.data.cost = 6
        self.mult = 0
    
    def trigger_on_start_hand(self, board):
        if any(board.get_evaluation_rules().is_face_card(card) for card in board.get_played_cards()):
            self.mult = 0
            logger.info(f'{self.data.name} reset')
        else:
            self.mult += 1
            board.add_mult(self.mult)
            logger.info(f'{self.data.name} added {self.mult} mult')
        return super().trigger_on_start_hand(board)

    def trigger_on_end_hand(self, board: BoardVision) -> None:
        mult = board.get_levels_table()[board.get_current_hand_type()]['played']
        if mult > 0:
            board.add_mult(mult)
            logger.info(f'{self.data.name} added {mult} mult')
        super().trigger_on_end_hand(board)


class JokerSpaceJoker(Joker):
    def __init__(self):
        super().__init__(name='Space Joker')
        self.data.cost = 5
        self.rarity = Rarity.UNCOMMON


class JokerEgg(Joker):
    def __init__(self):
        super().__init__(name='Space Joker')
        self.data.cost = 4
        self.sell_addition = 0


class JokerBurglar(Joker):
    def __init__(self):
        super().__init__(name='Burglar')
        self.data.cost = 6
        self.rarity = Rarity.UNCOMMON
    
    def trigger_on_start_hand(self, board):
        board.get_data().discards = 0
        board.get_data().remaining_hands += 3
        logger.info(f'{self.data.name} added 3 hands and removed discards')
        return super().trigger_on_start_hand(board)


class JokerBlackboard(Joker):
    def __init__(self):
        super().__init__(name='Blackboard')
        self.data.cost = 6
        self.rarity = Rarity.UNCOMMON
    
    def trigger_on_end_hand(self, board: BoardVision) -> None:
        if all(board.get_evaluation_rules().is_suit(card, Suit.SPADES) or board.get_evaluation_rules().is_suit(card, Suit.CLUBS) for card in board.get_hand_cards()):
            board.add_time_mult(3)
            logger.info(f'{self.data.name} added 3 time-mult')
        super().trigger_on_end_hand(board)


class JokerRunner(Joker):
    def __init__(self):
        super().__init__(name='Runner')
        self.data.cost = 5
        self.chips = 0

    def trigger_on_start_hand(self, board) -> None:
        if board.get_current_hand_type() in [HandType.STRAIGHT, HandType.STRAIGHT_FLUSH]:
            self.chips += 15
        return super().trigger_on_start_hand(board)
    
    def trigger_on_end_hand(self, board: BoardVision) -> None:
        if self.chips > 0:
            board.add_chips(self.chips)
            logger.info(f'{self.data.name} added {self.chips} chips')
        super().trigger_on_end_hand(board)


class JokerIceCream(Joker):
    def __init__(self):
        super().__init__(name='Ice Cream')
        self.data.cost = 5
        self.chips = 100
    
    def trigger_on_end_hand(self, board: BoardVision) -> None:
        if self.chips > 0:
            board.add_chips(self.chips)
            logger.info(f'{self.data.name} added {self.chips} chips')
            self.chips -= 5
        super().trigger_on_end_hand(board)


class JokerDNA(Joker):
    def __init__(self):
        super().__init__(name='DNA')
        self.data.cost = 8
        self.rarity = Rarity.RARE


class JokerSplash(Joker):
    def __init__(self):
        super().__init__(name='Splash')
        self.data.cost = 3
    
    def change_evaluation_rules(self, board: BoardVision) -> None:
        board.get_evaluation_rules().play_all_cards = True
    

class JokerBlueJoker(Joker):
    def __init__(self):
        super().__init__(name='Blue Joker')
        self.data.cost = 5
    
    def trigger_on_end_hand(self, board: BoardVision) -> None:
        chips = len(board.get_full_deck()) * 2
        if chips > 0:
            board.add_chips(chips)
            logger.info(f'{self.data.name} added {chips} chips')
        super().trigger_on_end_hand(board)


class JokerSixthSense(Joker):
    def __init__(self):
        super().__init__(name='Sixth Sense')
        self.data.cost = 6
        self.rarity = Rarity.UNCOMMON


class JokerConstellation(Joker):
    def __init__(self):
        super().__init__(name='Constellation')
        self.data.cost = 6
        self.rarity = Rarity.UNCOMMON
        self.mult_tens = 0

    def trigger_on_end_hand(self, board: BoardVision) -> None:
        if self.mult_tens > 0:
            board.add_time_mult(self.mult_tens * 0.1)
            logger.info(f'{self.data.name} added {self.mult_tens * 0.1} time-mult')
        super().trigger_on_end_hand(board)


class JokerHiker(Joker):
    def __init__(self):
        super().__init__(name='Hiker')
        self.data.cost = 5
        self.rarity = Rarity.UNCOMMON
    
    def trigger_on_play_card(self, card, board) -> None:
        card.data.value_bonus += 5
        logger.info(f'{self.data.name} added 5 bonus to {card}')
        super().trigger_on_play_card(card, board)


class JokerFacelessJoker(Joker):
    def __init__(self):
        super().__init__(name='Faceless Joker')
        self.data.cost = 4
    

class JokerGreenJoker(Joker):
    def __init__(self):
        super().__init__(name='Green Joker')
        self.data.cost = 4
        self.mult = 0
    
    def trigger_on_start_hand(self, board: BoardVision) -> None:
        self.mult += 1
        super().trigger_on_start_hand(board)
    
    def trigger_on_end_hand(self, board: BoardVision) -> None:
        if self.mult > 0:
            board.add_mult(self.mult)
            logger.info(f'{self.data.name} added {self.mult} mult')
        super().trigger_on_end_hand(board)


class JokerSuperposition(Joker):
    def __init__(self):
        super().__init__(name='Superposition')
        self.data.cost = 4


class JokerToDoList(Joker):
    def __init__(self):
        super().__init__(name='To Do List')
        self.data.cost = 4


class JokerCavendish(Joker):
    def __init__(self):
        super().__init__(name='Cavendish')
        self.data.cost = 4
    
    def trigger_on_end_hand(self, board: BoardVision) -> None:
        board.add_time_mult(3)
        logger.info(f'{self.data.name} added 3 time-mult')
        super().trigger_on_end_hand(board)


class JokerCardSharp(Joker):
    def __init__(self):
        super().__init__(name='Card Sharp')
        self.data.cost = 6
        self.rarity = Rarity.UNCOMMON
        self.played_hands: set[HandType] = set()
    
    def trigger_on_end_hand(self, board: BoardVision) -> None:
        if board.get_current_hand_type() in self.played_hands:
            board.add_time_mult(3)
            logger.info(f'{self.data.name} added 3 time-mult')
        self.played_hands.add(board.get_current_hand_type())
        super().trigger_on_end_hand(board)


class JokerRedCard(Joker):
    def __init__(self):
        super().__init__(name='Red Card')
        self.data.cost = 5
        self.mult = 0
    
    def trigger_on_end_hand(self, board: BoardVision) -> None:
        if self.mult > 0:
            board.add_mult(self.mult)
            logger.info(f'{self.data.name} added {self.mult} mult')
        super().trigger_on_end_hand(board)


class JokerMadness(Joker):
    def __init__(self):
        super().__init__(name='Madness')
        self.data.cost = 7
        self.rarity = Rarity.UNCOMMON
        self.mult = 0
    
    def trigger_on_end_hand(self, board: BoardVision) -> None:
        if self.mult > 0:
            board.add_time_mult(self.mult)
            logger.info(f'{self.data.name} added {self.mult} time-mult')
        super().trigger_on_end_hand(board)


class JokerSquareJoker(Joker):
    def __init__(self):
        super().__init__(name='Square Joker')
        self.data.cost = 4
        self.chips = 0
    
    def trigger_on_start_hand(self, board: BoardVision) -> None:
        if len(board.get_selected_cards()) == 4:
            self.chips += 4
        super().trigger_on_start_hand(board)

    def trigger_on_end_hand(self, board: BoardVision) -> None:
        if self.chips > 0:
            board.add_chips(self.chips)
            logger.info(f'{self.data.name} added {self.chips} chips')
        super().trigger_on_end_hand(board)


class JokerSeance(Joker):
    def __init__(self):
        super().__init__(name='Seance')
        self.data.cost = 6
        self.rarity = Rarity.UNCOMMON


class JokerRiffRaff(Joker):
    def __init__(self):
        super().__init__(name='Riff-Raff')
        self.data.cost = 6


class JokerVampire(Joker):
    def __init__(self):
        super().__init__(name='Vampire')
        self.data.cost = 7
        self.rarity = Rarity.UNCOMMON
        self.enhancements = 0
    
    def trigger_on_start_hand(self, board: BoardVision) -> None:
        for card in board.get_played_cards():
            if card.data.enhancement != Enhancement.NONE:
                card.data.enhancement = Enhancement.NONE
                self.enhancements += 1
                logger.info(f'{self.data.name} removed enhancement from {card}')
        super().trigger_on_start_hand(board)
    
    def trigger_on_end_hand(self, board: BoardVision) -> None:
        if self.enhancements > 0:
            board.add_time_mult(self.enhancements * 0.1)
            logger.info(f'{self.data.name} added {self.enhancements * 0.1} time-mult')
        super().trigger_on_end_hand(board)


class JokerShortcut(Joker):
    def __init__(self):
        super().__init__(name='Shortcut')
        self.data.cost = 7
        self.rarity = Rarity.UNCOMMON

    def change_evaluation_rules(self, board: BoardVision) -> None:
        board.get_evaluation_rules().straight_skip = True


class JokerHologram(Joker):
    def __init__(self):
        super().__init__(name='Hologram')
        self.data.cost = 7
        self.rarity = Rarity.UNCOMMON
        self.added_cards = 0
    
    def trigger_on_end_hand(self, board: BoardVision) -> None:
        if self.added_cards > 0:
            board.add_time_mult(self.added_cards * 0.25)
            logger.info(f'{self.data.name} added {self.added_cards * 0.25} time-mult')
        super().trigger_on_end_hand(board)


class JokerVagabond(Joker):
    def __init__(self):
        super().__init__(name='Vagabond')
        self.data.cost = 8
        self.rarity = Rarity.RARE


class JokerBaron(Joker):
    def __init__(self):
        super().__init__(name='Baron')
        self.data.cost = 8
        self.rarity = Rarity.RARE
    
    def trigger_on_card_in_hand(self, card: Card, board: BoardVision) -> None:
        if card.get_rank() == Rank.KING:
            board.add_time_mult(1.5)
            logger.info(f'{self.data.name} added 1.5 time-mult')
        super().trigger_on_card_in_hand(card, board)


class JokerCloud9(Joker):
    def __init__(self):
        super().__init__(name='Cloud 9')
        self.data.cost = 7
        self.rarity = Rarity.UNCOMMON


class JokerRocket(Joker):
    def __init__(self):
        super().__init__(name='Rocket')
        self.data.cost = 6
        self.rarity = Rarity.UNCOMMON



















class JokerHangingChad(Joker):
    def __init__(self):
        super().__init__(name='Hanging Chad')
        self.data.cost = 4

    def get_card_retriggers(self, card: Card, board: BoardVision) -> int:
        if card == board.get_played_cards()[0]:
            return 2
        return 0


class JokerSeltzer(Joker):
    def __init__(self):
        super().__init__(name='Seltzer')
        self.data.cost = 6
        self.rarity = Rarity.UNCOMMON

    def get_card_retriggers(self, card: Card, board: BoardVision) -> int:
        return 1


class JokerSockAndBuskin(Joker):
    def __init__(self):
        super().__init__(name='Sock and Buskin')
        self.data.cost = 6

    def get_card_retriggers(self, card: Card, board: BoardVision) -> int:
        if board.get_evaluation_rules().is_face_card(card):
            return 1
        return 0


class JokerPhotograph(Joker): ############# todo: make it better
    def __init__(self):
        super().__init__(name='Photograph')
        self.data.cost = 5
        self.first_card: Card | None = None

    def trigger_on_start_hand(self, board: BoardVision) -> None:
        cards = board.get_played_cards()
        for card in cards:
            if board.get_evaluation_rules().is_face_card(card):
                self.first_card = card
                break
    
    def trigger_on_play_card(self, card: Card, board: BoardVision) -> None:
        if self.first_card and card == self.first_card:
            board.add_time_mult(2)

    def trigger_on_end_hand(self, board: BoardVision) -> None:
        self.first_card = None


class JokerBlueprint(Joker):
    def __init__(self):
        super().__init__(name='Blueprint')
        self.data.cost = 10
        self.rarity = Rarity.RARE
        self.copied_joker: Joker = Joker('dummy')

    def trigger_on_start_hand(self, board: BoardVision) -> None:
        self.copied_joker.trigger_on_start_hand(board)

    def trigger_on_end_hand(self, board: BoardVision) -> None:
        self.copied_joker.trigger_on_end_hand(board)
    
    def trigger_on_play_card(self, card: Card, board: BoardVision) -> None:
        self.copied_joker.trigger_on_play_card(card, board)
    
    def trigger_on_card_in_hand(self, card: Card, board: BoardVision) -> None:
        self.copied_joker.trigger_on_card_in_hand(card, board)
    
    def trigger_on_discard_cards(self, cards: list[Card], board: BoardVision) -> None:
        self.copied_joker.trigger_on_discard_cards(cards, board)

    def change_evaluation_rules(self, board: BoardVision) -> None:
        # get copied
        jokers = board.get_jokers()
        self_index = jokers.index(self)
        if self_index + 1 < len(jokers):
            self.copied_joker = jokers[self_index + 1]

    def get_card_retriggers(self, card: Card, board: BoardVision) -> int:
        return self.copied_joker.get_card_retriggers(card, board)
    
    def get_hand_card_retriggers(self, card: Card, board: BoardVision) -> int:
        return self.copied_joker.get_hand_card_retriggers(card, board)
