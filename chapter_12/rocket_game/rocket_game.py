# Rocket Game
# Chapter 12 exercise 4
# rocket can move around in 4 directions

import sys
import pygame

from settings import Settings
from rocket import Rocket

class RocketGame:
    """overall class to manage game assets and behavior"""

    def __init__(self):
        """initialize the game and create the game resources"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Rocket Game")

        self.rocket = Rocket(self)

    def run_game(self):
            """starts the game loop"""
            while True:
                self._check_events()
                self.rocket.update()
                self._update_screen()

    def _check_events(self):
        """watch the keyboard and mouse for events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """respond to key press"""
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = True
        elif event.key == pygame.K_UP:
            self.rocket.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = False
        elif event.key == pygame.K_UP:
            self.rocket.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = False

    def _update_screen(self):
        """update images on the screen and flip to new screen"""
        self.screen.fill(self.settings.bg_color)
        self.rocket.blitme()

        pygame.display.flip()

if __name__ == '__main__':
    # make a game instance and run it
    rg = RocketGame()
    rg.run_game()


