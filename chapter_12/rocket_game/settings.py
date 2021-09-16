# Settings class for alien invaders game

class Settings:
    """A class to store all settings for Rocket game"""
    def __init__(self):
        """initialize the games settings"""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (150, 150, 150)

        # ship settings
        self.rocket_speed = 1.5

