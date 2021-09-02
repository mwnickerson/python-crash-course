# Pizza version 2
# Chapter 8
# Passing an arbitrary number of Arguments
# uses a while statemeent to describe pizza

def make_pizza(*toppings):
    """summarize the pizza being made"""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza('Pepperoni')
make_pizza('mushrooms', 'extra cheese', 'onions' )
