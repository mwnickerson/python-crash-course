# Number Writer
# Chapter 10: Storing Data
# using json.dump() and json.load()
# stores a list in a json
import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'jsons/numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)

