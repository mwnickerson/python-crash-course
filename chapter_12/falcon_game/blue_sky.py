# Blue Sky
# Chapter 12 exercise 1
# create a pygame window with a blue background

import sys
import pygame

from falcon import Falcon

class TrenchRun:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game and create the game resources"""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Trench Run")

        self.falcon = Falcon(self)

        # Set the background color
        self.bg_color = (0, 0, 230)

    def run_game(self):
        """start the main loop of the game"""
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # redraw the screen during each pass through the loop.
            self.screen.fill(self.bg_color)
            self.falcon.blitme()

            # Make the most recently drawn screen visible
            pygame.display.flip()

if __name__ == '__main__':
    # make a game instance and run the game
    tr = TrenchRun()
    tr.run_game()

