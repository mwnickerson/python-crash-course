# Three restaurants
# chapter 9 exercise 2
# using three restaurants in our class
class Restaurant:
    """a simple attempt to represent a restaurant"""
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
    def describe_restaraunt(self):
        print(f"{self.name} is a {self.type} restaurant")
    def open_restaurant(self):
        print(f"Come on in {self.name} is open for business!")

my_restaurant = Restaurant("Daily Bread", "Middle-Eastern")
michelle_restaurant = Restaurant("Silver Palace", "Chinese")
theo_restaurant = Restaurant("Bobby's Burger Place", "American")

my_restaurant.open_restaurant()
my_restaurant.describe_restaraunt()
michelle_restaurant.open_restaurant()
michelle_restaurant.describe_restaraunt()
theo_restaurant.open_restaurant()
theo_restaurant.describe_restaraunt()