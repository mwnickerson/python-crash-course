# Dice
# Chapter 9 exercise 13
# Create a die with imported random module
from random import randint as r
class Die:
    def __init__(self, sides=6):
        """initialize default dice side value"""
        self.sides = sides

    def roll_dice(self):
        """generate a number between 1 and number of sides"""
        rolled_value = r(1, self.sides)
        print(f"You rolled a {rolled_value}!")

# Rolling a six sided die 10 times
print("Rolling a  Six-Sided Die!")
six_die = Die()
x = 0;
while (x < 10):
    six_die.roll_dice()
    x += 1


# Rolling a ten-sided die 10 times
print("\nRolling a Ten-Sided Die!")
ten_die = Die(10)
x = 0;
while (x < 10):
    ten_die.roll_dice()
    x += 1

# Rolling a 20 sided dice ten times
print("\nRolling a Twenty-Sided Die!")
twenty_die = Die(20)
x = 0;
while (x < 10):
    twenty_die.roll_dice()
    x += 1

print("finished rolling the dice!")





