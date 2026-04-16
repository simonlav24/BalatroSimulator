


from random import choice

import pygame
from pygame import Vector2

from domain.card import create_standard_deck

from director.director import Director


def initialize_data() -> Director:
    director = Director()
    deck = create_standard_deck()
    for card in deck:
        director.add_card_to_deck(card)
    
    director.deck_player.reset()
    director.deck_player.shuffle()
    director.deck_player.draw_cards(8)

    return director

def main():
    pygame.init()

    # Screen dimensions
    win_size = Vector2(1280, 720)
    win = pygame.display.set_mode(win_size)
    pygame.display.set_caption("Balatro Simulator")

    # Clock for FPS
    clock = pygame.time.Clock()
    FPS = 60

    director = initialize_data()

    # Main loop
    running = True
    while running:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            director.input_system.handle_event(event)

            if event.type == pygame.QUIT:
                running = False
        
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