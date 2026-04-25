

import pygame
from core import Vector2

from domain.definitions import Suit, Rank, Enhancement, Seal


cards_texture_path = r'assets/playing_cards.png'
card_backs_texture_path = r'assets/card_backs.png'
jokers_texture_path = r'assets/jokers.png'

font_path = r'assets/m6x11.ttf'

cards_texture = pygame.image.load(cards_texture_path)
card_backs_texture = pygame.image.load(card_backs_texture_path)
jokers_texture = pygame.image.load(jokers_texture_path)


class Fonts:
    def __init__(self):
        self.small = pygame.font.Font(font_path, 24)
        self.medium = pygame.font.Font(font_path, 40)
        self.large = pygame.font.Font(font_path, 56)

fonts: Fonts | None = None

def init():
    global fonts
    fonts = Fonts()


win_size = Vector2(1280, 720)
CARD_SIZE = Vector2(71, 95)

FPS = 60

def card_surf_at(texture: pygame.Surface, x: int, y: int) -> pygame.Surface:
    surf = pygame.Surface(CARD_SIZE, pygame.SRCALPHA)
    surf.blit(texture, (0, 0), (x * CARD_SIZE[0], y * CARD_SIZE[1], *CARD_SIZE))
    return surf

def rank_suit_at(rank: Rank, suit: Suit) -> pygame.Surface:
    x = rank.value - 2
    y = suit_map[suit]
    return card_surf_at(cards_texture, x, y)

suit_map = {
    Suit.HEARTS: 0,
    Suit.CLUBS: 1,
    Suit.DIAMONDS: 2,
    Suit.SPADES: 3,
}

enhancement_map = {
    Enhancement.NONE: (1, 0),
    Enhancement.BONUS: (1, 1),
    Enhancement.MULT: (2, 1),
    Enhancement.LUCKY: (4, 1),
    Enhancement.STEEL: (6, 1),
    Enhancement.GOLD: (6, 0),
    Enhancement.STONE: (5, 0),
    Enhancement.WILD: (3, 1),
    Enhancement.GLASS: (5, 1),
}

seal_map = {
    Seal.RED: (5, 4),
    Seal.BLUE: (6, 4),
    Seal.GOLD: (2, 0),
    Seal.PURPLE: (4, 4),
}

jokers_map = {
    "8 Ball": (0, 5),
    "Abstract Joker": (3, 3),
    "Acrobat": (2, 1),
    "Ancient Joker": (7, 15),
    "Arrowhead": (1, 8),
    "Astronomer": (2, 7),
    "Banner": (1, 2),
    "Baron": (6, 12),
    "Baseball Card": (6, 14),
    "Blackboard": (2, 10),
    "Bloodstone": (0, 8),
    "Blue Joker": (7, 10),
    "Blueprint": (0, 3),
    "Bootstraps": (9, 8),
    "Brainstorm": (7, 7),
    "Bull": (7, 14),
    "Burglar": (1, 10),
    "Burnt Joker": (3, 7),
    "Business Card": (1, 4),
    "Campfire": (5, 15),
    "Canio": (3, 8),
    "Card Sharp": (6, 11),
    "Cartomancer": (7, 3),
    "Castle": (9, 15),
    "Cavendish": (5, 11),
    "Ceremonial Dagger": (5, 5),
    "Certificate": (8, 8),
    "Chaos the Clown": (1, 0),
    "Chicot": (6, 8),
    "Clever Joker": (2, 14),
    "Cloud 9": (7, 12),
    "Constellation": (8, 7),
    "Crafty Joker": (4, 14),
    "Crazy Joker": (5, 0),
    "Credit Card": (5, 1),
    "DNA": (5, 10),
    "Delayed Gratification": (4, 3),
    "Devious Joker": (3, 14),
    "Diet Cola": (8, 14),
    "Driver's License": (0, 7),
    "Droll Joker": (6, 0),
    "Drunkard": (1, 1),
    "Dusk": (4, 7),
    "Space Joker": (3, 5),
    "Erosion": (5, 13),
    "Even Steven": (8, 3),
    "Faceless Joker": (1, 11),
    "Fibonacci": (1, 5),
    "Flash Card": (0, 15),
    "FlowerPot": (0, 6),
    "Fortune Teller": (7, 5),
    "Four Fingers": (6, 6),
    "Gift Card": (3, 13),
    "Glass Joker": (1, 3),
    "Gluttonous Joker": (9, 1),
    "Golden Joker": (9, 2),
    "Golden Ticket": (5, 3),
    "Greedy Joker": (6, 1),
    "Green Joker": (2, 11),
    "Gros Michel": (7, 6),
    "Hack": (5, 2),
    "Half Joker": (7, 0),
    "Hallucination": (9, 13),
    "Hanging Chad": (9, 6),
    "Hiker": (0, 11),
    "Hit the Road": (8, 5),
    "Hologram": (4, 12),
    "Ice Cream": (4, 10),
    "Invisible Joker": (1, 7),
    "Joker": (0, 0),
    "Jolly Joker": (2, 0),
    "Juggler": (0, 1),
    "Loyalty Card": (4, 2),
    "Luchador": (1, 13),
    "Lucky Cat": (5, 14),
    "Lusty Joker": (7, 1),
    "Mad Joker": (4, 0),
    "Madness": (8, 11),
    "Mail-In Rebate": (7, 13),
    "Marble Joker": (3, 2),
    "Matador": (4, 5),
    "Merry Andy": (8, 0),
    "Midas Mask": (0, 13),
    "Mime": (4, 1),
    "Misprint": (6, 2),
    "Mr. Bones": (3, 4),
    "Mystic Summit": (2, 2),
    "Obelisk": (9, 12),
    "Odd Todd": (9, 3),
    "Onyx Agate": (2, 8),
    "Oops! All 6s": (5, 6),
    "Pareidolia": (6, 3),
    "Perkeo": (7, 8),
    "Photograph": (2, 13),
    "Popcorn": (1, 15),
    "RaisedFist": (8, 2),
    "Ramen": (2, 15),
    "Red Card": (7, 11),
    "Reserved Parking": (6, 13),
    "Ride the Bus": (1, 6),
    "Riff-Raff": (1, 12),
    "Rocket": (8, 12),
    "Rough Gem": (9, 7),
    "Runner": (3, 10),
    "Satellite": (8, 7),
    "Scary Face": (2, 3),
    "Scholar": (3, 6),
    "Seance": (0, 12),
    "Seeing Double": (4, 4),
    "Seltzer": (3, 15),
    "Shoot the Moon": (2, 6),
    "Shortcut": (3, 12),
    "Showman": (6, 5),
    "Sixth Sense": (8, 10),
    "Sly Joker": (0, 14),
    "Smeared Joker": (4, 6),
    "Smiley Face": (6, 15),
    "Sock and Buskin": (3, 1),
    "Splash": (6, 10),
    "Square Joker": (9, 11),
    "Steel Joker": (7, 2),
    "Joker Stencil": (2, 5),
    "Stone Joker": (9, 0),
    "Stuntman": (8, 6),
    "Supernova": (2, 4),
    "Superposition": (3, 11),
    "Swashbuckler": (9, 5),
    "The Duo": (5, 4),
    "The Family": (7, 4),
    "The Idol": (6, 7),
    "The Order": (8, 4),
    "The Tribe": (9, 4),
    "The Trio": (6, 4),
    "Throwback": (5, 7),
    "To Do List": (4, 11),
    "To the Moon": (8, 13),
    "Trading Card": (9, 14),
    "Triboulet": (4, 8),
    "Troubadour": (0, 2),
    "Turtle Bean": (4, 13),
    "Vagabond": (5, 12),
    "Vampire": (2, 12),
    "Walkie Talkie": (8, 15),
    "Wee Joker": (0, 0),
    "Wily Joker": (1, 14),
    "Wrathful Joker": (8, 1),
    "Yorick": (5, 8),
    "Zany Joker": (3, 0),
    "Spare Trousers": (4, 15)
}

class UIRatios:
    PLAY_BUTTON_SIZE = win_size.elementwise() * Vector2(0.1, 0.1)
    PLAY_BUTTON_OFFSET_1 = win_size.elementwise() * Vector2(0.37, 0.83)
    PLAY_BUTTON_OFFSET_2 = win_size.elementwise() * Vector2(0.6, 0.83)

class Colors:
    WHITE = (255, 255, 255)
    BLUE = (0, 147, 254)
    RED = (254, 76, 64)
    YELLOW = (254, 152, 0)
    PURPLE = (119, 122, 217)