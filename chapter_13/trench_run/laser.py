# Chapter 12 exercise 6
# laser class
import pygame
from pygame.sprite import Sprite

class Laser(Sprite):
    """class to manage laser fired from the falcon"""

    def __init__(self, tr_game):
        """create a laser object at the ship's current location"""
        super().__init__()
        self.screen = tr_game.screen
        self.settings = tr_game.settings
        self.color = self.settings.laser_color

        # create a laser at (0,0) and then set correct position
        self.rect = pygame.Rect(0, 0, self.settings.laser_width,
                                self.settings.laser_height)
        self.rect.midright = tr_game.falcon.rect.midright

        # store the bullet's position as a decimal value
        self.x = float(self.rect.x)

    def update(self):
        """move the laser across the screen"""
        self.x += self.settings.laser_speed
        # update the rect position
        self.rect.x = self.x

    def draw_laser(self):
        """draw the laser to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)

