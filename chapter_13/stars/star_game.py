# Chapter 13 exercise 1
# star game
import sys
import pygame

from settings import Settings
from star import Star

class StarsGame:
    """main class to manage game assets and behavior"""

    def __init__(self):
        """initialize the game and creat resources"""
        pygame.init()
        self.settings = Settings()
        # display window
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Stars')

        self.stars = pygame.sprite.Group()
        self._create_stars()

    def run_game(self):
        """Start the main game loop"""
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        """watch for keyboard events """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

    def _check_keydown_events(self, event):
        """respond to keypress"""
        if event.key == pygame.K_ESCAPE:
            sys.exit()

    def _create_stars(self):
        """create the grid of stars"""
        # create a star and find the stars amount of columns of stars
        star = Star(self)
        star_width, star_height = star.rect.size
        available_space_x = self.settings.screen_width - (star_width)
        number_stars_x = available_space_x // (2 * star_width)
        # find number of rows that fit on the screen
        available_space_y = (self.settings.screen_height -
                             (2 * star_height))
        number_rows = available_space_y // (2 * star_height)
        # place the stars on the screen
        for row_number in range(number_rows):
            for star_number in range(number_stars_x):
                self._create_star(star_number, row_number)

    def _create_star(self, star_number, row_number):
        star =Star(self)
        star_width, star_height = star.rect.size
        star.x = star_width + 2 * star.rect.height * star_number
        star.rect.x = star.x
        star.rect.y = star_height = 2 * star.rect.height * row_number
        self.stars.add(star)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.stars.draw(self.screen)

        pygame.display.flip()

if __name__ == '__main__':
    # makes the game instance and runs it
    sg = StarsGame()
    sg.run_game()






