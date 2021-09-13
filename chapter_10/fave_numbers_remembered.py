# Favorite Numbers Remembered
# Chapter 10 exercise 12
# combines adding and storing into one file
# prompts user for fave number if no existing json
import json

# load the favorite number if it is stored
# Otherwise, prompt for favorite number and store it

filename = 'jsons/fave_numbers.json'
try:
    with open(filename) as f:
        fave_number = json.load(f)
except FileNotFoundError:
    fave_number = input("What is your favorite number? ")
    with open(filename, 'w') as f:
        json.dump(fave_number, f)
        print(f"We will remember that {fave_number} is your favorite.")
else: print(f"I know your favorite numbers. It's {fave_number}!")