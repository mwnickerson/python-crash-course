# Addition Calculator
# Chapter 10 exercise 7
# Addition calculator that uses a while loop
print("Welcome to the addition calculator!")
print("enter 'q' to exit the program.")

while True:
    try:
        x = input("\nFirst number: ")
        if x == 'q':
            break

        x = int(x)

        y = input("Second number: ")
        if y == 'q':
            break
        y = int(y)

    except ValueError:
        print("I need a number please.")

    else:
        answer = x + y
        print(answer)



