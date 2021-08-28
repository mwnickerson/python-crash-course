# pizza toppings
# chapter 7 exercise 4
# a conditional loop that prompts user to enter toppings


prompt ="\nWhat topping would you like on your pizza?"
message = ""
while message != 'quit':
    message = input(prompt)
    topping = message
    if message != 'quit':
        print(f"I will add {topping} to your pizza!")