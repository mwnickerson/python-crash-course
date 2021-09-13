# Lottery Analysis
# Chapter 9 exercise 15
# Analyze a lottery
from random import choice
def get_winning_ticket(lottery_pool):
    winning_ticket = []
    """draws the winning numbers from the lottery pool"""
    while (len(winning_ticket) < 4):
        pulled_number = choice(lottery_pool)
        if pulled_number not in winning_ticket:
            winning_ticket.append(pulled_number)
    return winning_ticket

def check_ticket(my_ticket, winning_ticket):
    """compares the winning ticket with my ticket"""
    for element in my_ticket:
        if element not in winning_ticket:
            return False
    return True

def play_my_ticket(lottery_pool):
    my_ticket = []
    """draws numbers and letters for my ticket"""
    while (len(my_ticket) < 4):
        played_number = choice(lottery_pool)
        if played_number not in my_ticket:
            my_ticket.append(played_number)
    return my_ticket

# Running through creating the tickets and comparing
# counts each iteration
lottery_pool = (73, 1, 22, 66, 17, 85, 71, 47,\
                89, 34, 73, 91, 46, 'm', 'i', 'd', 'e', 'p', 'm')
winning_ticket = get_winning_ticket(lottery_pool)
plays = 0
won = False
max_tries = 1_000_000
# creates a players ticket and compares
# quits if it is over 1 million attempts
while not won:
    new_ticket = play_my_ticket(lottery_pool)
    won = check_ticket(new_ticket, winning_ticket)
    plays += 1
    if plays >= max_tries:
        break
if won:
    print("We have a winning ticket!")
    print(f"Your ticket: {new_ticket}")
    print(f"Winning Ticket: {winning_ticket}")
    print(f"It took {plays} attempts to win")
else:
    print(f"Tried {plays} combonations and still no win")

