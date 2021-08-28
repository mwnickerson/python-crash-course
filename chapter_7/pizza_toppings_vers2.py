# Pizza toppings version 2
# chapter 7 exercise 6
# rewritten with a active variable
prompt ="\nWhat topping would you like on your pizza?"
prompt += "\ntype 'quit' to exit: "
active = True
while active:
    topping = input(prompt)
    if topping == 'quit':
        active = False
    else:
        print(f"I will add {topping} to your pizza")
