# pizza
# Chapter 8
# Storing your functions in modules
def make_pizza(size, *toppings):
    """summarize pizza being made"""
    print(f"\n Making a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
