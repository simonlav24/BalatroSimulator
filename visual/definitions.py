
import pygame
from pygame import Vector2

from domain.definitions import Enhancement, Suit, Rank


cards_texture_path = f'assets/playing_cards.png'
card_backs_texture_path = f'assets/card_backs.png'
jokers_texture_path = f'assets/jokers.png'

cards_texture = pygame.image.load(cards_texture_path)
card_backs_texture = pygame.image.load(card_backs_texture_path)
jokers_texture = pygame.image.load(jokers_texture_path)

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

jokers_map = {
    'Joker': (0,0),
}