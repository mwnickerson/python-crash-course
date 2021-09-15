# Falcon Ship
# Chapter 12 exercise 2
# creates the user falcon ship for use by the player

import pygame

class Falcon:
    """A class to manage the ship"""
    def __init__(self, tr_game):
        """Initialize the ship and set its starting position"""
        self.screen = tr_game.screen
        self.screen_rect = tr_game.screen.get_rect()

        # load the image
        self.image = pygame.image.load('images/falcon.bmp')
        self.rect = self.image.get_rect()

        # Start each ship at the middle left of the screen
        self.rect.midleft = self.screen_rect.midleft

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)