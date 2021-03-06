# a place to store the game stats
class GameStats:
    """track statistics for Alien Invasion"""

    def __init__(self, ai_game):
        """initialize stats"""
        self.settings = ai_game.settings
        self.reset_stats()

        # start Alien invasion in an active state
        self.game_active = True

    def reset_stats(self):
        """initialize stats that change during the game"""
        self.ships_left = self.settings.ship_limit
