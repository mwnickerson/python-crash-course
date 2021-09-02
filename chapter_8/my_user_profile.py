# My User Profile
# Chapter 8 exercise 13
# Use the function to create a user profile for myself
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('matthew', 'nickerson',
                             location='miami',
                             field='information security',
                             hobbies='3d-printing and hacking')
print(user_profile)