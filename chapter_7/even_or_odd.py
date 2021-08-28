# even or odd
# chapter 7
# using the modulo operator to determine even or odd

number = input("Enter a number and I'll tell you if its even or odd: ")
number = int(number)
if number % 2 == 0:
    print(f"The number {number} is even")
else:
    print(f"The number {number} is odd")