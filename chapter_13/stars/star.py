# chapter 13 exercise 1
# class for a star
import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    """A class to represent a star"""

    def __init__(self, star_game):
        """initialize the star and its starting position"""
        super().__init__()
        self.screen = star_game.screen
        # load the star image
        self.image = pygame.image.load('images/star.bmp')
        self.rect = self.image.get_rect()
        # start each new star near the top left screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # store the star's vertical positions
        self.y = float(self.rect.y)
