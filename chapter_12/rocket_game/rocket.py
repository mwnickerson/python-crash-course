# Rocket
# Chapter 12 exercise 4
# rocket that can be moved in four directions
import pygame

class Rocket:
    """a class to manage the rocket"""

    def __init__(self, rocket_game):
        """initialize the rocket and set its starting positions"""
        self.screen = rocket_game.screen
        self.settings = rocket_game.settings
        self.screen_rect = rocket_game.screen.get_rect()

        # load the rocket image
        self.image = pygame.image.load('images/falcon.bmp')
        self.rect = self.image.get_rect()

        # starting position for rocket
        self.rect.center = self.screen_rect.center

        # store a decimal value for the rocket's horizontal
        # and vertical positions
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # movement flags
        self.moving_right, self.moving_left = False, False
        self.moving_up, self.moving_down = False, False

    def update(self):
        """update the rocket's position"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.rocket_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.rocket_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.rocket_speed
        if self.moving_down and self.rect.bottom <= self.screen_rect.bottom:
            self.y += self.settings.rocket_speed

        # update objecty from position attributes
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)