# Messages
# Chapter 8 exercise 9
# using a function to display mesages from a list

def show_messages(messages):
    """Prints the messages in the list"""
    for message in messages:
        print(message)

messages = ['hello', 'lmao', 'wya', 'i love python']
show_messages(messages)