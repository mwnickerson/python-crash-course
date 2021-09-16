# Keys
# chapter 12 exercise 5
# takes a keydown event
# prints the event.key attribute
import sys
import pygame

from settings import Settings

class KeyConverter:
    """overall class to manage program assets and behavior"""

    def __init__(self):
        """initialize the program and create the resources"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Event.key Dictionary")

    def run_program(self):
        """Starts the program loop"""
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        """responds to keypresses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses"""
        # show the key that was pressed
        print(event.key)
        if event.key == pygame.K_ESCAPE:
            sys.exit()

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        pygame.display.flip()

if __name__ == '__main__':
    kc = KeyConverter()
    kc.run_program()