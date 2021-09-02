# Sandwich Function
# Chapter 8 exercise 16
# sandwich making function
def make_sandwich(*toppings):
    """prints a summary of sandwich toppings"""
    print(f"Making a sandwich with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")