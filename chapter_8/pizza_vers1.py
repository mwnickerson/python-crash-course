# Pizza
# Chapter 8
# Passing an Arbitrary number of Arguments
def make_pizza(*toppings):
    """print the list of toppings requested"""
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
