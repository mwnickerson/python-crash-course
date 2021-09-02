# pets version 4
# Chapter 8
# Keyword arguments

def describe_pets(animal_type, pet_name):
    """Display information about pet"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}")

describe_pets(animal_type='dog',pet_name='ori')
describe_pets(pet_name='Mufasa',animal_type='cat')

