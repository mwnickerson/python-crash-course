# Dream Vacation
# Chapter 7 exercise 10
# A program to poll users of their dream vacation
# prints the results of the poll when completed

print("Hello and welcome to the dream vacation poll.")
vacations = {} # creates a dictionary for user responses

polling_active = True # sets the polling to active

while polling_active:
    # prompts user for their name and vacation
    name = input("\nWhat is your name? ")
    vacation = input("If you could go anywhere in the world where would it be? ")
    # stores the responses in vacations dictionary
    vacations[name] = vacation

    # determine if the poll will continue
    repeat = input("Is there anyone else who would like to participate? (yes/no)")
    if repeat == 'no':
        polling_active = False

# the results are displayed
print("\nThe results of the poll are in...")
for name, vacation in vacations.items():
    print(f"For their dream vacation {name.title()} would like to go to {vacation.title()}")


