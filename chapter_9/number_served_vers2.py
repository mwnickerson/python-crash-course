# Number Served
# Chapter 9 exercise 4
# a class thats for a restaurant
# track number of people served
#
class Restaurant:
    """a simple attempt to represent a restaurant"""
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = 0

    def describe_restaraunt(self):
        """returns a descriptive statment about the restaurant"""
        print(f"{self.name} is a {self.type} restaurant")

    def open_restaurant(self):
        """returns a statement to open the restaurant"""
        print(f"Come on in {self.name} is open for business!")

    def read_number_served(self):
        """prints the number of customers served"""
        print(f"{self.name} has served {self.number_served} customers today")

    def set_number_served(self, served):
        """sets the number served"""
        self.number_served = served

    def increment_number_served(self, served):
        """incremenets the number of customers served"""
        self.number_served += served

# prints the statements abot the restaurant and number served
my_restaurant = Restaurant("Theo's Bar & Grille", "American Bar")

my_restaurant.open_restaurant()
my_restaurant.set_number_served(5)
my_restaurant.read_number_served()

my_restaurant.increment_number_served(1)
my_restaurant.read_number_served()



