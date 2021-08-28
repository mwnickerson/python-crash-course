# parrot version 2
# chapter 7
# letting the user choose when to quit

prompt = "\nTell me something, and I will repeat it back to you. "
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit': # we can add this to eliminate the printing of quit
        print(message)

