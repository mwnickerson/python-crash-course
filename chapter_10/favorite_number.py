# favorite number
# Chapter 10 exercise 11
# program that prompts user for favorite user
# stores that favorite number in a json
import json

fave_number = input("What is your favorite number? ")

filename = 'jsons/fave_numbers.json'
with open(filename, 'w') as f:
    json.dump(fave_number, f)
    print(f"We will remember that {fave_number} is your favorite.")

