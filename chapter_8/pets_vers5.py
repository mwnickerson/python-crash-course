# Pets Version 5
# Chapter 8
# default values

def describe_pets(pet_name, animal_type='dog'): # sets the default animal type to dog
    """Display information about pet"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}")

describe_pets('Ori')
describe_pets('mufasa', 'cat') # overwite the default function by placing a value in the argument