# Restaraunt
# Chapter 9 exercise 1
# restaurant class with two methods
class Restaurant:
    """a simple attempt to represent a restaurant"""
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type

    def describe_restaraunt(self):
        print(f"{self.name} is a {self.type} restaurant")
    def open_restaurant(self):
        print(f"Come on in {self.name} is open for business!")

my_restaurant = Restaurant("Theo's Bar and Grill", "American",)
my_restaurant.open_restaurant()
my_restaurant.describe_restaraunt()


