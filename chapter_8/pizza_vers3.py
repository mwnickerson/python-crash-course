# Pizza version 3
# Chapter 8
# Mixing positional and arbitrary arguments
def make_pizza(size, *toppings):
    """summarize pizza being made"""
    print(f"\n Making a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')