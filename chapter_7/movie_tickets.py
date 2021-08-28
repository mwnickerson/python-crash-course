# movie tickets
# chapter 7 exercise 5
# evaluating age and assigning price using flags to exit
active = True
pay_message = "\nHow old are you?"
pay_message += "\n(enter 'quit' when finished)"
while active:
    customer_age = input(pay_message)
    if customer_age == 'quit':
        print("Goodbye!")
        active = False
    else:
        customer_age = int(customer_age)
        if customer_age < 3.0:
            print("Your ticket is free. Go on ahead!")
        elif customer_age < 13.0:
            print("Your ticket is $10. Please pay at the next window.")
        else:
            print("Your ticket is $15. Please pay at the next window.")





