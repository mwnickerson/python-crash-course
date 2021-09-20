# Random Walk
# Chapter 15

from random import choice

class RandomWalk:
    """a class to generate random walks"""

    def __init__(self, num_points=5000):
        """initialize the attributes of a walk"""
        self.num_points = num_points

        # all walks start at (0,0)
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        """determine the direction and distance for a step"""
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4, 5])
        step = distance * direction
        return step

    def fill_walk(self):
        """calculate all points in the walk"""

        # keep taking steps until the walk reaches the desired length
        while len(self.x_values) < self.num_points:
            # decide which direction to go and how far to go
            x_step = self.get_step()
            y_step = self.get_step()

            # reject moves that go nowhere
            if x_step == 0 and y_step == 0:
                continue
            # calculate new position
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

