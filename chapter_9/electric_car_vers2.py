# Electric Car
# Chapter 9
# Defining attributes and methods for the child class
class Car:
    """a simple attempt to simulate a car"""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 85

    def get_descriptive_name(self):
        """return a descriptive name of a car"""
        long_name =f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """reads odometer"""
        print(f"This car has {self.odometer_reading} miles on it")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value
        reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """add the given amount to the odometer"""
        self.odometer_reading += miles

class ElectricCar(Car):
    """represents aspects of a car specifc to electric vehicles"""
    def __init__(self, make, model, year):
        """initialize attributes of a parent class.
        then intialize attributes specific to an electric car
        """

        super().__init__(make, model, year)
        self.battery_size = 75

    def describe_battery(self):
        """print a statement describing the battery size"""
        print(f"This car has a {self.battery_size}-kWh battery.")
my_tesla = ElectricCar('tesla', 'model s',2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()