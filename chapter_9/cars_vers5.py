# Cars version 5
# Chapter 9
# Modifying an attribute value through a method
# rejects turning back the odometer

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
        print(f"This car has {self.odometer_reading}")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value
        reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")


my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(15)
my_new_car.read_odometer()