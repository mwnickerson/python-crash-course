# movie tickets vers 2
# chapter 7 exercise 6
# ask for age and assign ticket price with a conditional loop
prompt = "\nHow old are you?"
prompt += "\n(enter 'quit' when finished)"
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        message = int(message)
        customer_age = message
        if customer_age < 3.0:
            print("Your ticket is free. Go on ahead!")
        elif customer_age < 13.0:
            print("Your ticket is $10. Please pay at the next window.")
        else:
            print("Your ticket is $15. Please pay at the next window.")
    print(message)
