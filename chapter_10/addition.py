# Addition
# Chapter 10 exercise 6
# adds two numbers together
# if user inputs non numerical value it returns an error message
user_number_one = input("First Number: ")
try:
    first_number = int(user_number_one)
except ValueError:
    print(f"{user_number_one} is not a valid number")
    exit()
user_number_two = input("Second Number: ")
try:
    second_number = int(user_number_two)
except ValueError:
    print(f"{user_number_two} is not a valid number")
    exit()
answer = first_number + second_number
print(answer)

