# Lottery
# Chapter 9 exercise 14
# Randomly draws lottery numbers and letters
from random import choice
lottery_pool = (73, 1, 22, 66, 17, 85, 71, 47,\
                89, 34, 73, 91, 46, 'm', 'i', 'd', 'e', 'p')
winning_numbers = []
print("Drawing the winning lottery numbers. Take out your tickets.")
# while loop to pull numbers for the winning ticket
# makes sure there are no duplicates
while (len(winning_numbers) < 4):
    pulled_number = choice(lottery_pool)
    if pulled_number not in winning_numbers:
        print(f"We pulled a {pulled_number}")
        winning_numbers.append(pulled_number)

print(f"The winning numbers are {winning_numbers}")
print("If your ticket matches these, come down and claim a prize")





