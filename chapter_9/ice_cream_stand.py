# Ice Cream Stand
# Chapter 9 exercise 6
# an ice cream class that inherits restaraunt class

# restaraunt class
class Restaurant:
    """a simple attempt to represent a restaurant"""
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
    def describe_restaraunt(self):
        print(f"{self.name} is a {self.type}"
              f" restaurant")
    def open_restaurant(self):
        print(f"Come on in {self.name} is"
              f" open for business!")

# an ice cream stand class
class IceCreamStand(Restaurant):
    """represents aspect of a restaurant
    specific to an Ice Cream Stand"""

    def __init__(self, restaurant_name, cuisine_type):
        """initialize attributes of the parent class."""
        super().__init__(restaurant_name, cuisine_type)
        self.ice_cream_flavors = ["vanilla", "chocolate",
                                  "strawberry", "butter pecan"]
    def list_flavors(self):
        """list the flavors available in the ice cream shop"""
        print(f"The flavors available today"
              f" are {self.ice_cream_flavors}")

# calling the ice cream stand class
ice_cream_stand = IceCreamStand("Ori's Ice Cream", "Ice Cream")

ice_cream_stand.describe_restaraunt()
ice_cream_stand.open_restaurant()
ice_cream_stand.list_flavors()




