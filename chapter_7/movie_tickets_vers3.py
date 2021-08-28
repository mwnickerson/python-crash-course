# movie tickets version 3
# chapter 7 exercise 6
# evaluate age, assign price, exit with break statement
prompt = "\nHow old are you?"
prompt += "\n(enter 'quit' when finished)"

while True:
    customer_age = input(prompt)
    if customer age == 'quit':
        break
    else:
        customer_age = int(customer_age)
        if customer_age < 3.0:
            print("Your ticket is free. Go on ahead!")
        elif customer_age < 13.0:
            print("Your ticket is $10. Please pay at the next window.")
        else:
            print("Your ticket is $15. Please pay at the next window.")