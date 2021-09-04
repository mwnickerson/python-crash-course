# Cars version 3
# Chapter 8
# modifying attribute values
# modifying an attribute's value directly

class Car:
    """a simple attempt to simulate a car"""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """return a descriptive name of a car"""
        long_name =f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """reads odometer"""
        print(f"This car has {self.odometer_reading}")

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()


