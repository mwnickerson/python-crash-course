# class to represent a die

from random import randint

class Die:
    """a class to represent a die"""

    def __init__(self, num_sides=6):
        """assume a six-sided die"""
        self.num_sides = num_sides

    def roll(self):
        """return a random value b/n 1 and number of sides"""
        return randint(1, self.num_sides)
