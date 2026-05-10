from visual.texturizer import DescriptionMaker
from domain.jokers import *
from domain.board import Board
import visual.definitions as visual

import pygame
pygame.font.init()

maker = DescriptionMaker(Board())
visual.init()

surf = maker.create_joker_description(JokerAbstractJoker(None))
pygame.image.save(surf, 'temp.png')
