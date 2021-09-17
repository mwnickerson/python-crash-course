# chapter 12 exercise 6
# built in modules
import sys
from random import random

# external modules
import pygame

# custom built modules
from settings import Settings
from falcon import Falcon
from laser import Laser
from tie_fighter import TieFighter

class TrenchRun:
    """overall class to manage game assets and behavior"""

    def __init__(self):
        """initialize the game, and create game resources"""
        pygame.init()
        # load the settings
        self.settings = Settings()
        # intialize the display
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Trench Run")
        # initialize the ship and bullets
        self.falcon = Falcon(self)
        self.lasers = pygame.sprite.Group()
        # initialize the tie fighter enemy
        self.tie_fighters = pygame.sprite.Group()
        self._create_tie_fighter()

    def run_game(self):
        """start the main game loop"""
        while True:
            self._check_events()
            self.falcon.update()
            self._update_lasers()
            self._update_tie_fighters()
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
        elif event.key == pygame.K_ESCAPE:
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
        self._check_laser_tie_fighter_collisions()

    def _check_laser_tie_fighter_collisions(self):
        """respond to laser hits on tie fighters"""
        # remove any lasers and tie fighters that have collided
        collisions = pygame.sprite.groupcollide(
            self.lasers, self.tie_fighters, True, True)
        if not self.tie_fighters:
            # destroy existing bullets and create a new fleet
            self.lasers.empty()
            self._create_tie_fighter()
# Below is commented out code that spawns a fleet of tie fighters
# uncomment for fleet mode
    #def _create_fleet(self):
    #    """create the fleet of tie fighters"""
    #    tie_fighter = TieFighter(self)
    #    # determine the size and amount on the screen
    #    tie_fighter_width, tie_fighter_height = tie_fighter.rect.size
    #    available_space_x = self.settings.screen_width - (2 * tie_fighter_width)
    #    available_space_y = self.settings.screen_height - (2 * tie_fighter_height)
    #    number_tie_fighters_y = available_space_y // (2 * tie_fighter_height)
    #    number_columns = available_space_x // (2 * tie_fighter_width)
    #    # create the fleet of tie fighters
    #    for column_number in range(number_columns):
    #        for tie_fighter_number in range(number_tie_fighters_y):
    #            self._create_tie_fighter(tie_fighter_number, column_number)

    #def _change_fleet_direction(self):
    #    """move the fleet forward and change direction"""
    #    for tie_fighter in self.tie_fighters.sprites():
    #        tie_fighter.rect.x += self.settings.fleet_close_speed
    #    self.settings.fleet_direction *= -1

    #def _create_tie_fighter(self, tie_fighter_number, column_number):
    #    """create a tie fighter and place it on the screen"""
    #    tie_fighter = TieFighter(self)
    #    tie_fighter_width, tie_fighter_height = tie_fighter.rect.size
    #    tie_fighter.y = tie_fighter_width + 2 * tie_fighter_height * tie_fighter_number
    #    tie_fighter.rect.y = tie_fighter.y
    #    tie_fighter.rect.x = tie_fighter_height + 2 * tie_fighter.rect.height * column_number
    #    self.tie_fighters.add(tie_fighter)

    # creates random tie attacker mode
    # comment this section and uncomment the other section for fleet mode
    def _create_tie_fighter(self):
        """create a tie fighter if conditions are right"""
        if random() < self.settings.tie_fighter_frequency:
            tie_fighter = TieFighter(self)
            self.tie_fighters.add(tie_fighter)
            print(len(self.tie_fighters))

    def _update_tie_fighters(self):
        """update the position of the tie fighters"""
        self.tie_fighters.update()

    def _update_screen(self):
        """update images on the screen and flip to the new screen"""
        self.screen.fill(self.settings.bg_color)
        self.falcon.blitme()
        for laser in self.lasers.sprites():
            laser.draw_laser()
        self.tie_fighters.draw(self.screen)
        pygame.display.flip()

if __name__ == '__main__':
    # make the game instance and run the game
    tr_game = TrenchRun()
    tr_game.run_game()

