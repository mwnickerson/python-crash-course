# pizza toppings version 3
# chapter 7 exercise 6
# prompts pizza toppings with break exit
prompt ="\nWhat topping would you like on your pizza?"
prompt += "\n(type 'quit' to quit)"

while true:
    topping = input(prompt)
    if topping == 'quit'
        print("Goodbye!")
    else:
        print(f"I will add {topping} to your pizza.")