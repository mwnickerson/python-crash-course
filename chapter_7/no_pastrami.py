# No Pastrami!
# Chapter 7 exercise 9
# Moving completed sandwiches from order to completed
# There is no pastrami so no pastrami sandwiches will be made

sandwich_orders = ['roast beef', 'pastrami',\
                   'chicken salad', 'cheesesteak', 'cheese', 'pastrami', 'italian', 'pastrami' ]
completed_orders = []
print("Hello and welcome to Matt's Deli!")
print("Unfortunately today we have run out of pastrami.")
print("No pastrami sandwiches will be made today")
print("\n-----Completed Sandwich Orders-----")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    completed_orders = sandwich_orders.pop()

    print(f"Your {completed_orders} sandwich is ready for pickup!")
