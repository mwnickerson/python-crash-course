# Division Calculator
# Chapter 10: Exceptions
# Handling the ZeroDivisionError Exception

#print(5/0)
# this throws a zerodivisionerror

# using try except blocks
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
