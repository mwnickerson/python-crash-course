# Greet User
# Chapter 10: Storing Data
# reading user generated data
import json

filename = 'jsons/username.json'

with open(filename) as f:
    username = json.load(f)
    print(f"Welcome back, {username}!")

