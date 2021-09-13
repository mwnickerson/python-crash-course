# Guest Book
# chapter 10 exercise 4
# Greets user and prompts user for their name
# stores the user response in guestbook
filename = 'text_files/guest_book.txt'
while True:
    print("Hello and welcome!")
    guest_name = input("Please enter your name: ")
    print("Or enter 'quit' to exit")
    if guest_name == "quit":
        break
    else:
        with open(filename, 'a') as f:
            f.write(f"\n{guest_name.title()}")
