# greet users
# chapter 8
# Passing a list

def greet_users(names):
    """Print a simpl hello message to each user in the list"""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

usernames = ['hannah', 'margot', 'ty']
greet_users(usernames)
