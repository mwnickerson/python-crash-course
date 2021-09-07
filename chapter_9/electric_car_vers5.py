# Electric Car
# Chapter 9
# Overriding methods from the parent class
# instances as attributes adding range of battery

# A class for a car
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
# Class for a battery
class Battery:
    """a simple attempt to model a battery for an electric car"""
    def __init__(self, battery_size=75):
        """Initiliaze the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-KWH battery.")

    def get_range(self):
        """print a statement about the range this battery provides"""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge.")


# Class for an electric car
class ElectricCar(Car):
    """represents aspects of a car specifc to electric vehicles"""
    def __init__(self, make, model, year):
        """initialize attributes of a parent class.
        then intialize attributes specific to an electric car
        """
        super().__init__(make, model, year)
        self.battery = Battery()

    def describe_battery(self):
        """print a statement describing the battery size"""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def fill_gas_tank(self):
        """Electric Cars dont have gas tanks."""
        print("This car doesnt need to have a gas tank!")

# Print statements about the car and the battery
my_tesla = ElectricCar('tesla', 'model s', 2019)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()