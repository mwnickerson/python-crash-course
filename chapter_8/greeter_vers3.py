# greeter version 3
# Chapter 8
# using a function with a while loop
# with an infinite loop
def get_formatted_name(first_name, last_name):
    """return a full name, neatly formatted"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

# This is an infinite loop!
while True:
    print("\nPlease tell me your name:")
    f_name = input("First Name: ")
    l_name = input("Last Name: ")
    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")