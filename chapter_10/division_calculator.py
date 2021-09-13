# Division Calculator
# Chapter 10: Exceptions
# Handling the ZeroDivisionError Exception

#print(5/0)
# this throws a zerodivisionerror

# using try except blocks
#try:
#    print(5/0)
#except ZeroDivisionError:
#    print("You can't divide by zero!")

# using exceptions to prevent crashes
# the else block

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit")
while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    else:
        print(answer)
