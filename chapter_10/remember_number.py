# remember number
# Chapter 10 exercise 11
# remembers number by pulling from json
import json
filename = 'jsons/fave_numbers.json'

with open(filename) as f:
    fave_number = json.load(f)
    print(f"I know your favorite numbers. It's {fave_number}!")