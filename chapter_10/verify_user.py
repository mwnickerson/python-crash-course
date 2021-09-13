# Verify User
# Chapter 10 exercise 13
# greets a user from json
# creates a new line on the json for new user
import json

def get_stored_username():
    """Get stored username if available."""
    filename = 'jsons/username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """prompt for a new username"""
    username = input("What is your name? ")
    filename = 'jsons/username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        correct = input(f"Are you {username}? (y/n) ")
        if correct == 'y':
            print(f"Welcome back, {username}!")
            return
        else:
            username = get_new_username()
            print(f"We'll remember you when you come back, {username}")

greet_user()