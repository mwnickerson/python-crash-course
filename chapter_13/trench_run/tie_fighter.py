# Chapter 13: exercise 5
import pygame
from pygame.sprite import Sprite
from random import randint

class TieFighter(Sprite):
    """a class to represent a tie fighter enemy"""

    def __init__(self, tr_game):
        """initialize the alien and sets its starting position"""
        super().__init__()
        self.screen = tr_game.screen
        self.settings = tr_game.settings

        # load the image of the tie fighter
        self.image = pygame.image.load('images/tie_fighter.bmp')
        self.rect = self.image.get_rect()

        # start each new alien at a random position on the right side
        self.rect.left = self.screen.get_rect().right
        tie_fighter_top_max = self.settings.screen_height - self.rect.height
        self.rect.top = randint(0, tie_fighter_top_max)

        # store the tie fighters exact positions
        self.x = float(self.rect.x)


    def update(self):
        """move the tie fighters towards the left side"""
        self.x -= self.settings.tie_fighter_speed
        self.rect.x = self.x
