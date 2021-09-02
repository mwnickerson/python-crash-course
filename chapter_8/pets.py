# Pets
# chapter 8
# positional arguments

def describe_pets(animal_type, pet_name):
    """Display information about pet"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}")

describe_pets('dog', 'ori')