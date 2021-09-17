# Chapter 13 exercise 3

import pygame
from pygame.sprite import Sprite

class Raindrop(Sprite):
    """a class to represent a raindrop"""

    def __init__(self,raindrop_game):
        """initialize the raindrop and its starting position"""
        super().__init__()
        self.screen = raindrop_game.screen
        self.settings = raindrop_game.settings
        # load the image of the raindrop
        self.image = pygame.image.load('images/raindrop.bmp')
        self.rect = self.image.get_rect()
        # start each new raindrop neat the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # store the raindrop horizontal and vertical position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def check_disappeared(self):
        """check if the drop dissapeared off the screen"""
        if self.rect.top > self.screen.get_rect().bottom:
            return True
        else:
            return False

    def update(self):
        self.y += self.settings.raindrop_drop_speed
        self.rect.y = self.y

