# chapter 13 exercise 3

import sys
import pygame

from settings import Settings
from raindrop import Raindrop

class RaindropGame:
    """overall class to manage game assets and behaviors"""

    def __init__(self):
        """initializes the game and create resources"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width,
                                               self.settings.screen_height))
        pygame.display.set_caption("Raindrop Game")

        self.raindrops = pygame.sprite.Group()

        self._create_raindrop_storm()

    def run_game(self):
        """start the main game loop"""
        while True:
            self._check_events()
            self.raindrops.update()
            self._update_screen()

    def _check_events(self):
        """watch for keyboard events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

    def _check_keydown_events(self, event):
        """respond to keypress"""
        if event.key == pygame.K_ESCAPE:
            sys.exit()

    def _create_raindrop_storm(self):
        """create the grid of raindrops"""
        # determine raindrop size
        raindrop = Raindrop(self)
        raindrop_width, raindrop_height = raindrop.rect.size
        # determine number of raindrop columns
        available_space_x = self.settings.screen_width - raindrop_width
        number_raindrops_x = available_space_x // (2 * raindrop_width)
        # determine number of rows of raindrops
        available_space_y = self.settings.screen_height
        number_rows = available_space_y // (2 * raindrop_height)
        # create the full storm of raindrops
        for row_number in range(number_rows):
            for raindrop_number in range(number_raindrops_x):
                self._create_raindrop(raindrop_number, row_number)

    def _create_raindrop(self, raindrop_number, row_number):
        """create a raindrop and place it in the row"""
        raindrop = Raindrop(self)
        raindrop_width, raindrop_height = raindrop.rect.size
        raindrop.x = raindrop_width + 2 * raindrop_width * raindrop_number
        raindrop.rect.x = raindrop.x
        raindrop.y = 2 * raindrop.rect.height * row_number
        raindrop.rect.y = raindrop_height + 2 * raindrop.rect.height * row_number
        self.raindrops.add(raindrop)

    def _update_raindrops(self):
        """update the positions of the raindrops down"""
        self.raindrops.update()

    def _update_screen(self):
        """update images on the screen and flip to a new screen"""
        self.screen.fill(self.settings.bg_color)
        self.raindrops.draw(self.screen)

        pygame.display.flip()

if __name__ == '__main__':
    # make a game instance and run it
    rg = RaindropGame()
    rg.run_game()