# pets version 3
# chapter 8
# order matters in positional arguments

def describe_pets(animal_type, pet_name):
    """Display information about pet"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}")

describe_pets('ori', 'dog')