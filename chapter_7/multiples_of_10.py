# multiples of 10
# chapter 7 exercise 3
# prompts users for a number and tells if multiple of 10

user_number = input("Please give me a number: ")
user_number = int(user_number)
if user_number % 10 == 0:
    print(f"{user_number} is a multiple of ten")
else:
    print(f"{user_number} is not a multiple of ten")