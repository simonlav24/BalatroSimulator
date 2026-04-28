


from random import choice

import pygame

from domain.definitions import Enhancement, Seal, Edition
from domain.card import create_standard_deck
from domain.jokers import *
from domain.utils import get_all_joker_classes

from visual.definitions import win_size, FPS
from visual import definitions
from director.director import Director
from director.debug_helper import DebugHelper

def initialize_data() -> Director:
    director = Director()
    factory = director.get_card_factory()
    player = director.get_player()

    deck = create_standard_deck()
    for card in deck:
        new_card = factory.create_playing_card(card.rank, card.suit)
        player.add_card_to_deck(new_card)
    player.add_joker(factory.create_joker_card(JokerPhotograph))
    player.add_joker(factory.create_joker_card(JokerHangingChad))

    player.reset()
    player.shuffle()
    player.draw_cards(8)
    player.flush_animation()

    DebugHelper().set_director(director)

    return director

def main():
    pygame.init()
    definitions.init()

    win = pygame.display.set_mode(win_size)
    pygame.display.set_caption("Balatro Simulator")

    # Clock for FPS
    clock = pygame.time.Clock()

    director = initialize_data()
    factory = director.get_card_factory()
    player = director.get_player()

    director.initialize_round_ui()

    # Main loop
    done = False
    while not done:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            director.input_system.handle_event(event)

            if event.type == pygame.KEYDOWN and event.key == pygame.K_t:
                # DebugHelper().print_hand_cards()
                joker_cls = choice(get_all_joker_classes())
                player.add_joker(factory.create_joker_card(joker_cls))
                player.flush_animation()

            if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                done = True
        
        # step
        director.step()

        # draw
        win.fill((0, 0, 0))
        
        director.renderer.draw(win)


        # Update display
        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()