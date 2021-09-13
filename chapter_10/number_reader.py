# Number Reader
# Chapter 10: Storing Data
# Using json.dump()_ and json.load()
# reading from a json file
import json

filename = 'jsons/numbers.json'
with open(filename) as f:
    numbers = json.load(f)

print(numbers)