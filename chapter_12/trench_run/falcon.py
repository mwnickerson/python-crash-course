# chapter 12 exercise 6
# creates the user image

import pygame

class Falcon:
    """a class to manage the spaceship"""

    def __init__(self, tr_game):
        """initialize the ship and its starting point"""
        self.screen = tr_game.screen
        self.settings = tr_game.settings
        self.screen_rect = tr_game.screen.get_rect()

        # load the space ship and get its rect
        self.image = pygame.image.load('images/falcon.bmp')
        self.rect = self.image.get_rect()

        # start each new ship at the middle left of the screen
        self.rect.midleft = self.screen_rect.midleft

        # store a decimal value for the ships vertical position
        self.y = float(self.rect.y)

        # movement flag
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """update the falcon's position based on the movement flag"""
        # update the ship's y value, not the rect
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.falcon_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.falcon_speed

        self.rect.y = self.y

    def blitme(self):
        """draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)

