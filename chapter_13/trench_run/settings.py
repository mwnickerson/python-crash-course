# chapter 12 exercise 6
# main settings for the game

class Settings:
    """A class to store all settings for Trench Run"""

    def __init__(self):
        """initialize the game's settings"""
        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)

        # falcon settings
        self.falcon_speed = 1.0

        # laser settings
        self.laser_speed = 1.0
        self.laser_width = 12.5
        self.laser_height = 5
        self.laser_color =(250, 250, 0)
        self.lasers_allowed = 6

        # Tie Fighter Settings
        self.tie_fighter_speed = 0.5
        self.tie_fighter_frequency = 3
        # 1 reps movement up, -1 reps movement down
        self.fleet_direction = 1

