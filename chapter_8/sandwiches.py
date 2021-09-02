# Sandwiches
# Chapter 8 exercise 12
# a function that makes a sandwich and prints a summary of it
def make_sandwich(*toppings):
    """prints a summary of sandwich toppings"""
    print(f"Make a sandwich with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_sandwich('roast beef', 'lettuce', 'onions', 'horse radish')

