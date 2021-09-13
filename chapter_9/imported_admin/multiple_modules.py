# multiple modules
# Chapter 9 exercise 12
# importing from multiple modules

from user import User
from admin import Admin, Privileges

matthew = Admin('matthew', 'nickerson', 'mwn@mail.com', 'mwn', 0)
matthew.privileges.show_privs()