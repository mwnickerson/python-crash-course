# chapter 12 exercise 6

import sys

import pygame

from settings import Settings
from falcon import Falcon
from laser import Laser

class TrenchRun:
    """overall class to manage game assets and behavior"""

    def __init__(self):
        """initialize the game, and create game resources"""
        pygame.init()
        self.settings = Settings()
        # intialize the display
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Trench Run")
        # initialize the ship and bullets
        self.falcon = Falcon(self)
        self.lasers = pygame.sprite.Group()

    def run_game(self):
        """start the main game loop"""
        while True:
            self._check_events()
            self.falcon.update()
            self._update_lasers()
            self._update_screen()

    def _check_events(self):
        """watch for keyboard and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """respond to keypress down"""
        if event.key == pygame.K_UP:
            self.falcon.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.falcon.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_laser()
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """respond to key release"""
        if event.key == pygame.K_UP:
            self.falcon.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.falcon.moving_down = False

    def _fire_laser(self):
        """create a new laser and add it to the bullets group"""
        if len(self.lasers) < self.settings.lasers_allowed:
            new_laser = Laser(self)
            self.lasers.add(new_laser)

    def _update_lasers(self):
        """update the location of lasers and get rid of old lasers"""
        self.lasers.update()
        for laser in self.lasers.copy():
            if laser.rect.left >= self.screen.get_rect().right:
                self.lasers.remove(laser)

    def _update_screen(self):
        """update images on the screen and flip to the new screen"""
        self.screen.fill(self.settings.bg_color)
        self.falcon.blitme()
        for laser in self.lasers.sprites():
            laser.draw_laser()
        pygame.display.flip()

if __name__ == '__main__':
    # make the game instance and run the game
    tr_game = TrenchRun()
    tr_game.run_game()

