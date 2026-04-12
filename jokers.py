

import logging
from random import randint, choice

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
            board.add_time_mult(1.0 + self.enhancements * 0.1)
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


class JokerObelisk(Joker):
    def __init__(self):
        super().__init__(name='Obelisk')
        self.data.cost = 8
        self.rarity = Rarity.RARE
        self.consecutive_played = 0
    
    def trigger_on_end_hand(self, board: BoardVision) -> None:
        if self.consecutive_played > 0:
            board.add_time_mult(self.consecutive_played * 0.2)
            logger.info(f'{self.data.name} added {self.consecutive_played * 0.2} time-mult')
        super().trigger_on_end_hand(board)


class JokerMidasMask(Joker):
    def __init__(self):
        super().__init__(name='Midas Mask')
        self.data.cost = 7
        self.rarity = Rarity.UNCOMMON
    
    def trigger_on_start_hand(self, board):
        for card in board.get_selected_cards():
            if board.get_evaluation_rules().is_face_card(card):
                card.data.enhancement = Enhancement.GOLD
        super().trigger_on_start_hand(board)
        

class JokerLuchador(Joker):
    def __init__(self):
        super().__init__(name='Luchador')
        self.data.cost = 5
        self.rarity = Rarity.UNCOMMON


class JokerPhotograph(Joker):
    def __init__(self):
        super().__init__(name='Photograph')
        self.data.cost = 5
    
    def trigger_on_play_card(self, card: Card, board: BoardVision) -> None:
        played_cards = board.get_played_cards()
        first_face = next((card for card in played_cards if board.get_evaluation_rules().is_face_card(card)), None)
        if card is first_face:
            board.add_time_mult(2)
            logger.info(f'{self.data.name} added 2 time-mult')
        super().trigger_on_play_card(card, board)


class JokerGiftCard(Joker):
    def __init__(self):
        super().__init__(name='Gift Card')
        self.data.cost = 6
        self.rarity = Rarity.UNCOMMON
        

class JokerTurtleBean(Joker):
    def __init__(self):
        super().__init__(name='Turtle Bean')
        self.data.cost = 6
        self.rarity = Rarity.UNCOMMON


class JokerErosion(Joker):
    def __init__(self):
        super().__init__(name='Erosion')
        self.data.cost = 6
        self.rarity = Rarity.UNCOMMON

    def trigger_on_end_hand(self, board: BoardVision) -> None:
        start = board.get_data().starting_deck_size
        current = len(board.get_full_deck())
        if current < start:
            mult = 4 * start - current
            board.add_mult(mult)
            logger.info(f'{self.data.name} added {mult} mult')
        super().trigger_on_end_hand(board)


class JokerReservedParking(Joker):
    def __init__(self):
        super().__init__(name='Reserved Parking')
        self.data.cost = 6


class JokerMailInRebate(Joker):
    def __init__(self):
        super().__init__(name='Mail-In Rebate')
        self.data.cost = 4


class JokerTotheMoon(Joker):
    def __init__(self):
        super().__init__(name='To the Moon')
        self.data.cost = 5
        self.rarity = Rarity.UNCOMMON


class JokerHallucination(Joker):
    def __init__(self):
        super().__init__(name='Hallucination')
        self.data.cost = 4


class JokerFortuneTeller(Joker):
    def __init__(self):
        super().__init__(name='Fortune Teller')
        self.data.cost = 6
        self.mult = 0
    
    def trigger_on_end_hand(self, board: BoardVision) -> None:
        if self.mult > 0:
            board.add_mult(self.mult)
            logger.info(f'{self.data.name} added {self.mult} mult')
        super().trigger_on_end_hand(board)


class JokerJuggler(Joker):
    def __init__(self):
        super().__init__(name='Juggler')
        self.data.cost = 4


class JokerDrunkard(Joker):
    def __init__(self):
        super().__init__(name='Drunkard')
        self.data.cost = 4


class JokerStoneJoker(Joker):
    def __init__(self):
        super().__init__(name='Stone Joker')
        self.data.cost = 6
        self.rarity = Rarity.UNCOMMON

    def trigger_on_end_hand(self, board: BoardVision) -> None:
        chips = 25 * sum(card for card in board.get_full_deck() if card.data.enhancement == Enhancement.STONE)
        if chips > 0:
            board.add_chips(chips)
            logger.info(f'{self.data.name} added {chips} chips')
        super().trigger_on_end_hand(board)


class JokerGoldenJoker(Joker):
    def __init__(self):
        super().__init__(name='Golden Joker')
        self.data.cost = 6


class JokerLuckyCat(Joker):
    def __init__(self):
        super().__init__(name='Lucky Cat')
        self.data.cost = 6
        self.rarity = Rarity.UNCOMMON
        self.lucky_hits = 0
    
    def trigger_on_end_hand(self, board: BoardVision) -> None:
        if self.lucky_hits > 0:
            board.add_time_mult(self.lucky_hits * 0.25)
            logger.info(f'{self.data.name} added {self.lucky_hits * 0.25} time-mult')
        super().trigger_on_end_hand(board)


class JokerBaseballCard(Joker):
    def __init__(self):
        super().__init__(name='Baseball Card')
        self.data.cost = 8
        self.rarity = Rarity.RARE
    
    def trigger_on_end_hand(self, board: BoardVision) -> None:
        for joker in board.get_jokers():
            if joker.rarity == Rarity.UNCOMMON:
                board.add_time_mult(1.5)
                logger.info(f'{self.data.name} added 1.5 time-mult')
        super().trigger_on_end_hand(board)


class JokerBull(Joker):
    def __init__(self):
        super().__init__(name='Bull')
        self.data.cost = 6
        self.rarity = Rarity.UNCOMMON
    
    def trigger_on_end_hand(self, board: BoardVision) -> None:
        chips = 2 * board.get_data().money
        if chips > 0:
            board.add_chips(chips)
            logger.info(f'{self.data.name} added {chips} chips')
        super().trigger_on_end_hand(board)


class JokerDietCola(Joker):
    def __init__(self):
        super().__init__(name='Diet Cola')
        self.data.cost = 6
        self.rarity = Rarity.UNCOMMON


class JokerTradingCard(Joker):
    def __init__(self):
        super().__init__(name='Trading Card')
        self.data.cost = 6
        self.rarity = Rarity.UNCOMMON


class JokerFlashCard(Joker):
    def __init__(self):
        super().__init__(name='Flash Card')
        self.data.cost = 5
        self.rarity = Rarity.UNCOMMON
        self.mult = 0

    def trigger_on_end_hand(self, board: BoardVision) -> None:
        if self.mult > 0:
            board.add_mult(self.mult)
            logger.info(f'{self.data.name} added {self.mult} mult')
        super().trigger_on_end_hand(board)


class JokerPopcorn(Joker):
    def __init__(self):
        super().__init__(name='Popcorn')
        self.data.cost = 5
        self.mult = 20

    def trigger_on_end_hand(self, board: BoardVision) -> None:
        if self.mult > 0:
            board.add_mult(self.mult)
            logger.info(f'{self.data.name} added {self.mult} mult')
        super().trigger_on_end_hand(board)
    
    def trigger_on_end_round(self, board: BoardVision) -> None:
        self.mult -= 4


class SpareTrousers(Joker):
    def __init__(self):
        super().__init__(name='Spare Trousers')
        self.data.cost = 6
        self.rarity = Rarity.UNCOMMON
        self.mult = 0

    def trigger_on_end_hand(self, board: BoardVision) -> None:
        if self.mult > 0:
            board.add_mult(self.mult)
            logger.info(f'{self.data.name} added {self.mult} mult')
        super().trigger_on_end_hand(board)
    
    def trigger_on_start_hand(self, board: BoardVision) -> None:
        evaluator = HandEvaluator(board.get_played_cards(), board.get_evaluation_rules())
        if evaluator.check_two_pair() is not None:
            self.mult += 2


class JokerAncientJoker(Joker):
    def __init__(self):
        super().__init__(name='Ancient Joker')
        self.data.cost = 8
        self.rarity = Rarity.RARE
        self.suit = Suit.HEARTS
    
    def trigger_on_play_card(self, card: Card, board: BoardVision) -> None:
        if board.get_evaluation_rules().is_suit(card, self.suit):
            board.add_time_mult(1.5)
            logger.info(f'{self.data.name} added 1.5 time-mult')
        super().trigger_on_play_card(card, board)

    def trigger_on_end_round(self, board: BoardVision) -> None:
        self.suit = choice([Suit.SPADES, Suit.HEARTS, Suit.DIAMONDS, Suit.CLUBS])


class JokerRamen(Joker):
    def __init__(self):
        super().__init__(name='Ramen')
        self.data.cost = 6
        self.rarity = Rarity.UNCOMMON
        self.remaining_discards = 200
    
    def trigger_on_play_card(self, card: Card, board: BoardVision) -> None:
        mult = self.remaining_discards * 0.01
        board.add_time_mult(mult)
        logger.info(f'{self.data.name} added {mult} time-mult')
        super().trigger_on_play_card(card, board)
    
    def on_discard(self, card_discarded: Card, board: BoardVision) -> None:
        self.remaining_discards -= 1

    def trigger_on_end_round(self, board: BoardVision) -> None:
        self.suit = choice([Suit.SPADES, Suit.HEARTS, Suit.DIAMONDS, Suit.CLUBS])


class JokerWalkieTalkie(Joker):
    def __init__(self):
        super().__init__(name='Walkie Talkie')
        self.data.cost = 4
    
    def trigger_on_play_card(self, card: Card, board: BoardVision) -> None:
        if card.get_rank() in [Rank.FOUR, Rank.TEN]:
            board.add_chips(10)
            board.add_mult(4)
            logger.info(f'{self.data.name} added 10 chips, 4 mult')
        super().trigger_on_play_card(card, board)


class JokerSeltzer(Joker):
    def __init__(self):
        super().__init__(name='Seltzer')
        self.data.cost = 6
        self.rarity = Rarity.UNCOMMON

    def get_card_retriggers(self, card: Card, board: BoardVision) -> int:
        return 1


class JokerCastle(Joker):
    def __init__(self):
        super().__init__(name='Castle')
        self.data.cost = 6
        self.rarity = Rarity.UNCOMMON
        self.chips = 0
        self.suit = Suit.HEARTS
    
    def trigger_on_end_hand(self, board: BoardVision) -> None:
        if self.chips > 0:
            board.add_chips(self.chips)
            logger.info(f'{self.data.name} added {self.chips} chips')
        super().trigger_on_end_hand(board)
    
    def on_discard(self, card_discarded: Card, board: BoardVision) -> None:
        if board.get_evaluation_rules().is_suit(card_discarded, self.suit):
            self.chips += 3

    def trigger_on_end_round(self, board: BoardVision) -> None:
        self.suit = choice([Suit.SPADES, Suit.HEARTS, Suit.DIAMONDS, Suit.CLUBS])


class JokerSmileyFace(Joker):
    def __init__(self):
        super().__init__(name='Smiley Face')
        self.data.cost = 4
    
    def trigger_on_play_card(self, card: Card, board: BoardVision) -> None:
        if board.get_evaluation_rules().is_face_card(card):
            board.add_mult(5)
            logger.info(f'{self.data.name} added 5 mult')
        super().trigger_on_play_card(card, board)


class JokerCampfire(Joker):
    def __init__(self):
        super().__init__(name='Campfire')
        self.data.cost = 9
        self.rarity = Rarity.RARE
        self.solds = 0
    
    def trigger_on_end_hand(self, board: BoardVision) -> None:
        if self.solds > 0:
            board.add_time_mult(self.solds * 0.25)
            logger.info(f'{self.data.name} added {self.solds * 0.25} time-mult')
        super().trigger_on_end_hand(board)


class JokerGoldenTicket(Joker):
    def __init__(self):
        super().__init__(name='Golden Ticket')
        self.data.cost = 5
    
    def trigger_on_play_card(self, card: Card, board: BoardVision) -> None:
        if card.data.enhancement == Enhancement.GOLD:
            board.get_data().money += 4
            logger.info(f'{self.data.name} added 4 gold')
        super().trigger_on_play_card(card, board)


class JokerMrBones(Joker):
    def __init__(self):
        super().__init__(name='Mr. Bones')
        self.data.cost = 5
        self.rarity = Rarity.UNCOMMON


class JokerAcrobat(Joker):
    def __init__(self):
        super().__init__(name='Acrobat')
        self.data.cost = 6
        self.rarity = Rarity.UNCOMMON
    
    def trigger_on_end_hand(self, board: BoardVision) -> None:
        if board.get_data().remaining_hands == 0:
            board.add_time_mult(3)
            logger.info(f'{self.data.name} added 3 time-mult')
        super().trigger_on_end_hand(board)


class JokerSockAndBuskin(Joker):
    def __init__(self):
        super().__init__(name='Sock and Buskin')
        self.data.cost = 6
        self.rarity = Rarity.UNCOMMON

    def get_card_retriggers(self, card: Card, board: BoardVision) -> int:
        if board.get_evaluation_rules().is_face_card(card):
            return 1
        return 0


class JokerSwashbuckler(Joker):
    def __init__(self):
        super().__init__(name='Swashbuckler')
        self.data.cost = 4

    def trigger_on_end_hand(self, board: BoardVision) -> None:
        mult = sum(joker.get_sell_value(board) for joker in board.get_jokers())
        board.add_mult(mult)
        logger.info(f'{self.data.name} added {mult} mult')
        super().trigger_on_end_hand(board)


class JokerTroubadour(Joker):
    def __init__(self):
        super().__init__(name='Troubadour')
        self.data.cost = 6
        self.rarity = Rarity.UNCOMMON


class JokerCertificate(Joker):
    def __init__(self):
        super().__init__(name='Certificate')
        self.data.cost = 6
        self.rarity = Rarity.UNCOMMON


class JokerSmearedJoker(Joker):
    def __init__(self):
        super().__init__(name='Smeared Joker')
        self.data.cost = 7
        self.rarity = Rarity.UNCOMMON
    
    def change_evaluation_rules(self, board: BoardVision):
        board.get_evaluation_rules().smeared = True


class JokerThrowback(Joker):
    def __init__(self):
        super().__init__(name='Throwback')
        self.data.cost = 6
        self.rarity = Rarity.UNCOMMON
    
    def trigger_on_end_hand(self, board: BoardVision) -> None:
        if board.get_data().skipped_blinds > 0:
            board.add_time_mult(0.25 * board.get_data().skipped_blinds)
            logger.info(f'{self.data.name} added {0.25 * board.get_data().skipped_blinds} time-mult')
        super().trigger_on_end_hand(board)


class JokerHangingChad(Joker):
    def __init__(self):
        super().__init__(name='Hanging Chad')
        self.data.cost = 4

    def get_card_retriggers(self, card: Card, board: BoardVision) -> int:
        if card == board.get_played_cards()[0]:
            return 2
        return 0


class JokerRoughGem(Joker):
    def __init__(self):
        super().__init__(name='Rough Gem')
        self.data.cost = 7
        self.rarity = Rarity.UNCOMMON

    def trigger_on_play_card(self, card: Card, board: BoardVision) -> None:
        if board.get_evaluation_rules().is_suit(card, Suit.DIAMONDS):
            board.get_data().money += 1
            logger.info(f'{self.data.name} added 1 gold')
        super().trigger_on_play_card(card, board)


class JokerBloodstone(Joker):
    def __init__(self):
        super().__init__(name='Bloodstone')
        self.data.cost = 7
        self.rarity = Rarity.UNCOMMON

    def trigger_on_play_card(self, card: Card, board: BoardVision) -> None:
        if board.get_evaluation_rules().is_suit(card, Suit.HEARTS):
            mode = board.get_mode()
            if mode == CalcMode.BEST:
                board.add_time_mult(1.5)
                logger.info(f'{self.data.name} added 1.5 time-mult')
            elif mode == CalcMode.SIMULATE:
                if randint(0, 1) == 0:
                    board.add_time_mult(1.5)
                    logger.info(f'{self.data.name} added 1.5 time-mult')
        super().trigger_on_play_card(card, board)


class JokerArrowhead(Joker):
    def __init__(self):
        super().__init__(name='Arrowhead')
        self.data.cost = 7
        self.rarity = Rarity.UNCOMMON

    def trigger_on_play_card(self, card: Card, board: BoardVision) -> None:
        if board.get_evaluation_rules().is_suit(card, Suit.SPADES):
            board.add_chips(50)
            logger.info(f'{self.data.name} added 50 chips')
        super().trigger_on_play_card(card, board)


class JokerOnyxAgate(Joker):
    def __init__(self):
        super().__init__(name='Onyx Agate')
        self.data.cost = 7
        self.rarity = Rarity.UNCOMMON

    def trigger_on_play_card(self, card: Card, board: BoardVision) -> None:
        if board.get_evaluation_rules().is_suit(card, Suit.SPADES):
            board.add_mult(7)
            logger.info(f'{self.data.name} added 7 mult')
        super().trigger_on_play_card(card, board)


class JokerGlassJoker(Joker):
    def __init__(self):
        super().__init__(name='Glass Joker')
        self.data.cost = 6
        self.rarity = Rarity.UNCOMMON
        self.glass_broken = 0

    def trigger_on_end_hand(self, board: BoardVision) -> None:
        if self.glass_broken > 0:
            board.add_time_mult(0.75 * self.glass_broken)
            logger.info(f'{self.data.name} added {0.75 * self.glass_broken} time-mult')
        super().trigger_on_end_hand(board)


class JokerShowman(Joker):
    def __init__(self):
        super().__init__(name='Showman')
        self.data.cost = 5
        self.rarity = Rarity.UNCOMMON


class JokerFlowerPot(Joker):
    def __init__(self):
        super().__init__(name='FlowerPot')
        self.data.cost = 6
        self.rarity = Rarity.UNCOMMON
    
    def trigger_on_end_hand(self, board: BoardVision) -> None:
        cards = [card for card in board.get_played_cards() if card.data.enhancement != Enhancement.STONE]
        if len(cards) >= 4:
            suits = {
                Suit.SPADES: False,
                Suit.HEARTS: False,
                Suit.CLUBS: False,
                Suit.DIAMONDS: False,
            }
            for card in sorted(cards, key=lambda x: 1 if x.data.enhancement == Enhancement.WILD else 0):
                determined = False
                for key_suit in suits.keys():
                    if card.get_suit() == key_suit and not suits[key_suit]:
                        suits[key_suit] = True
                        determined = True
                if determined:
                    continue
                if board.get_evaluation_rules().smeared:
                    for key_suit in suits.keys():
                        similar = get_similar(card.get_suit())
                        if similar == key_suit and not suits[key_suit]:
                            suits[key_suit] = True
                            determined = True
                if determined:
                    continue
                if card.data.enhancement == Enhancement.WILD:
                    for key_suit in suits.keys():
                        if not suits[key_suit]:
                            suits[key_suit] = True
                            determined = True
            if all(suits.values()):
                board.add_time_mult(3)
                logger.info(f'{self.data.name} added 3 time-mult')
        super().trigger_on_end_hand(board)


class JokerCopier(Joker):
    def __init__(self, name: str):
        super().__init__(name=name)
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

    def get_card_retriggers(self, card: Card, board: BoardVision) -> int:
        return self.copied_joker.get_card_retriggers(card, board)
    
    def get_hand_card_retriggers(self, card: Card, board: BoardVision) -> int:
        return self.copied_joker.get_hand_card_retriggers(card, board)


class JokerBlueprint(JokerCopier):
    def __init__(self):
        super().__init__(name='Blueprint')

    def change_evaluation_rules(self, board: BoardVision) -> None:
        # get copied
        self.copied_joker = Joker('dummy')
        jokers = board.get_jokers()
        self_index = jokers.index(self)
        if self_index + 1 < len(jokers):
            candidate = jokers[self_index + 1]
            if isinstance(candidate, JokerCopier):
                self.copied_joker = candidate.copied_joker
            else:
                self.copied_joker = candidate
        
        if self.copied_joker is self:
            self.copied_joker = Joker('dummy')
        print(f'{self.data.name} copying {self.copied_joker}')


class JokerWeeJoker(Joker):
    def __init__(self):
        super().__init__(name='Wee Joker')
        self.data.cost = 8
        self.rarity = Rarity.RARE
        self.chips = 0

    def trigger_on_play_card(self, card: Card, board: BoardVision) -> None:
        if card.get_rank() is Rank.TWO:
            self.chips += 8
        super().trigger_on_play_card(card, board)
    
    def trigger_on_end_hand(self, board: BoardVision) -> None:
        if self.chips > 0:
            board.add_chips(self.chips)
            logger.info(f'{self.data.name} added {self.chips} chips')
        super().trigger_on_end_hand(board)


class JokerMerryAndy(Joker):
    def __init__(self):
        super().__init__(name='Merry Andy')
        self.data.cost = 7
        self.rarity = Rarity.UNCOMMON


class JokerOopsAll6s(Joker):
    def __init__(self):
        super().__init__(name='Oops! All 6s')
        self.data.cost = 4
        self.rarity = Rarity.UNCOMMON


class JokerTheIdol(Joker):
    def __init__(self):
        super().__init__(name='The Idol')
        self.data.cost = 6
        self.rarity = Rarity.UNCOMMON
        self.rank = Rank.KING
        self.suit = Suit.HEARTS
    
    def trigger_on_play_card(self, card: Card, board: BoardVision) -> None:
        if card.get_rank() == self.rank and board.get_evaluation_rules().is_suit(card, self.suit):
            board.add_time_mult(2)
            logger.info(f'{self.data.name} added 2 time-mult')
        super().trigger_on_play_card(card, board)


class JokerSeeingDouble(Joker):
    def __init__(self):
        super().__init__(name='Seeing Double')
        self.data.cost = 6
        self.rarity = Rarity.UNCOMMON
    
    def trigger_on_end_hand(self, board: BoardVision) -> None:
        club = next((card for card in board.get_selected_cards() if board.get_evaluation_rules().is_suit(card, Suit.CLUBS)), None)
        if club is not None and \
            any(board.get_evaluation_rules().get_suit(card) in [Suit.SPADES, Suit.DIAMONDS, Suit.HEARTS, Suit.ANY] for card in board.get_selected_cards()):
            
            board.add_time_mult(2)
            logger.info(f'{self.data.name} added 2 time-mult')
        super().trigger_on_end_hand(board)


class JokerMatador(Joker):
    def __init__(self):
        super().__init__(name='Matador')
        self.data.cost = 7
        self.rarity = Rarity.UNCOMMON


class JokerHitTheRoad(Joker):
    def __init__(self):
        super().__init__(name='Hit the Road')
        self.data.cost = 8
        self.rarity = Rarity.RARE
        self.jacks = 0
    
    def on_discard(self, card_discarded: Card, board: BoardVision):
        if card_discarded.get_rank() == Rank.JACK:
            self.jacks += 1
        super().on_discard(card_discarded, board)
    
    def trigger_on_end_hand(self, board: BoardVision) -> None:
        if self.jacks > 0:
            board.add_time_mult(0.5 * self.jacks)
            logger.info(f'{self.data.name} added {0.5 * self.jacks} time-mult')
        super().trigger_on_end_hand(board)
    
    def trigger_on_end_round(self, board: BoardVision) -> None:
        self.jacks = 0
        super().trigger_on_end_round(board)
    

class JokerTheDuo(Joker):
    def __init__(self):
        super().__init__(name='The Duo')
        self.data.cost = 8
        self.rarity = Rarity.RARE
    
    def trigger_on_end_hand(self, board: BoardVision) -> None:
        evaluator = HandEvaluator(board.get_played_cards(), board.get_evaluation_rules())
        if evaluator.check_pair() is not None:
            board.add_time_mult(2)
            logger.info(f'{self.data.name} added 2 time-mult')
        super().trigger_on_end_hand(board)


class JokerTheTrio(Joker):
    def __init__(self):
        super().__init__(name='The Trio')
        self.data.cost = 8
        self.rarity = Rarity.RARE
    
    def trigger_on_end_hand(self, board: BoardVision) -> None:
        evaluator = HandEvaluator(board.get_played_cards(), board.get_evaluation_rules())
        if evaluator.check_three_of_a_kind() is not None:
            board.add_time_mult(3)
            logger.info(f'{self.data.name} added 3 time-mult')
        super().trigger_on_end_hand(board)


class JokerTheFamily(Joker):
    def __init__(self):
        super().__init__(name='The Family')
        self.data.cost = 8
        self.rarity = Rarity.RARE
    
    def trigger_on_end_hand(self, board: BoardVision) -> None:
        evaluator = HandEvaluator(board.get_played_cards(), board.get_evaluation_rules())
        if evaluator.check_four_of_a_kind() is not None:
            board.add_time_mult(4)
            logger.info(f'{self.data.name} added 4 time-mult')
        super().trigger_on_end_hand(board)


class JokerTheOrder(Joker):
    def __init__(self):
        super().__init__(name='The Order')
        self.data.cost = 8
        self.rarity = Rarity.RARE
    
    def trigger_on_end_hand(self, board: BoardVision) -> None:
        evaluator = HandEvaluator(board.get_played_cards(), board.get_evaluation_rules())
        if evaluator.check_straight() is not None:
            board.add_time_mult(3)
            logger.info(f'{self.data.name} added 3 time-mult')
        super().trigger_on_end_hand(board)


class JokerTheTribe(Joker):
    def __init__(self):
        super().__init__(name='The Tribe')
        self.data.cost = 8
        self.rarity = Rarity.RARE
    
    def trigger_on_end_hand(self, board: BoardVision) -> None:
        evaluator = HandEvaluator(board.get_played_cards(), board.get_evaluation_rules())
        if evaluator.check_flush() is not None:
            board.add_time_mult(2)
            logger.info(f'{self.data.name} added 2 time-mult')
        super().trigger_on_end_hand(board)


class JokerStuntman(Joker):
    def __init__(self):
        super().__init__(name='Stuntman')
        self.data.cost = 7
        self.rarity = Rarity.RARE
    
    def trigger_on_end_hand(self, board: BoardVision) -> None:
        board.add_chips(250)
        logger.info(f'{self.data.name} added 250 chips')
        super().trigger_on_end_hand(board)


class JokerInvisibleJoker(Joker):
    def __init__(self):
        super().__init__(name='Invisible Joker')
        self.data.cost = 8
        self.rarity = Rarity.RARE


class JokerBrainstorm(JokerCopier):
    def __init__(self):
        super().__init__(name='Brainstorm')

    def change_evaluation_rules(self, board: BoardVision) -> None:
        # get copied
        self.copied_joker = Joker('dummy')
        candiadte = board.get_jokers()[0]
        if isinstance(candiadte, JokerCopier):
            self.copied_joker = candiadte.copied_joker
        else:
            self.copied_joker = candiadte
        
        if self.copied_joker is self:
            self.copied_joker = Joker('dummy')
        print(f'{self.data.name} copying {self.copied_joker}')


class JokerSatellite(Joker):
    def __init__(self):
        super().__init__(name='Satellite')
        self.data.cost = 6
        self.rarity = Rarity.UNCOMMON


class JokerShootTheMoon(Joker):
    def __init__(self):
        super().__init__(name='Shoot the Moon')
        self.data.cost = 5
    
    def trigger_on_card_in_hand(self, card, board):
        if card.get_rank() == Rank.QUEEN:
            board.add_mult(13)
            logger.info(f'{self.data.name} added 13 mult')
        super().trigger_on_card_in_hand(card, board)


class JokerDriversLicense(Joker):
    def __init__(self):
        super().__init__(name='Driver\'s License')
        self.data.cost = 7
        self.rarity = Rarity.RARE
    
    def trigger_on_end_hand(self, board: BoardVision) -> None:
        amount = sum(card for card in board.get_full_deck() if card.data.enhancement != Enhancement.NONE)
        if amount > 0:
            board.add_time_mult(3)
            logger.info(f'{self.data.name} added 3 time-mult')
        super().trigger_on_end_hand(board)


class JokerCartomancer(Joker):
    def __init__(self):
        super().__init__(name='Cartomancer')
        self.data.cost = 6
        self.rarity = Rarity.UNCOMMON


class JokerAstronomer(Joker):
    def __init__(self):
        super().__init__(name='Astronomer')
        self.data.cost = 8
        self.rarity = Rarity.UNCOMMON


class JokerBurntJoker(Joker):
    def __init__(self):
        super().__init__(name='Burnt Joker')
        self.data.cost = 8
        self.rarity = Rarity.RARE

    def trigger_on_discard_cards(self, cards, board):
        raise NotImplementedError()


class JokerBootstraps(Joker):
    def __init__(self):
        super().__init__(name='Bootstraps')
        self.data.cost = 7
        self.rarity = Rarity.UNCOMMON

    def trigger_on_end_hand(self, board: BoardVision) -> None:
        mult = 2 * int(board.get_data().money / 5)
        if mult > 0:
            board.add_mult(mult)
            logger.info(f'{self.data.name} added {mult} mult')
        super().trigger_on_end_hand(board)


class JokerCanio(Joker):
    def __init__(self):
        super().__init__(name='Canio')
        self.data.cost = 20
        self.rarity = Rarity.LEGENDARY
        self.mult = 1

    def trigger_on_end_hand(self, board: BoardVision) -> None:
        if self.mult > 0:
            board.add_time_mult(self.mult)
            logger.info(f'{self.data.name} added {self.mult} time-mult')
        super().trigger_on_end_hand(board)


class JokerTriboulet(Joker):
    def __init__(self):
        super().__init__(name='Triboulet')
        self.data.cost = 20
        self.rarity = Rarity.LEGENDARY

    def trigger_on_play_card(self, card: Card, board: BoardVision) -> None:
        if card.get_rank() in [Rank.QUEEN, Rank.KING]:
            board.add_time_mult(2)
            logger.info(f'{self.data.name} added 2 time-mult')
        super().trigger_on_play_card(card, board)


class JokerYorick(Joker):
    def __init__(self):
        super().__init__(name='Yorick')
        self.data.cost = 20
        self.rarity = Rarity.LEGENDARY
        self.mult = 1
        self.discards_remaining = 23

    def trigger_on_end_hand(self, board: BoardVision) -> None:
        if self.mult > 0:
            board.add_time_mult(self.mult)
            logger.info(f'{self.data.name} added {self.mult} time-mult')
        super().trigger_on_end_hand(board)
    
    def on_discard(self, card_discarded: Card, board: BoardVision) -> None:
        self.discards_remaining -= 1
        if self.discards_remaining == 0:
            self.discards_remaining += 1
            self.mult += 1
        super().on_discard(card_discarded, board)


class JokerChicot(Joker):
    def __init__(self):
        super().__init__(name='Chicot')
        self.data.cost = 20
        self.rarity = Rarity.LEGENDARY


class JokerPerkeo(Joker):
    def __init__(self):
        super().__init__(name='Perkeo')
        self.data.cost = 20
        self.rarity = Rarity.LEGENDARY
