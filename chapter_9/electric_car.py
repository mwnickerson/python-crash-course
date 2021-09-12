# Electric Car
# Chapter 9
# A class for electric car and battery for import
from car import Car

class Battery:
    """A simple attempt to model a battery for an electric car"""
    def __init__(self, battery_size=75):
        """initialize the battery attributes"""
        self.battery_size = battery_size

    def describe_battery(self):
        """print a statement to describe a batter"""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on a full charge")

class ElectricCar(Car):
    """Model aspects of a car, specific to electric vehicles"""
    def __init__(self, make, model, year):
        """
        initialize the attributes of the parent class
        initializes the attrributes specific to an electric car
        """
        super().__init__(make, model, year)
        self.battery = Battery()

