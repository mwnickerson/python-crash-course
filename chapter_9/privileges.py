# Privileges
# Chapter 9 exercise 8
# a new instance of admin with a privileges class

# user class with greeting and description
class Users:
    """greets and displays user info"""
    def __init__(self, first, last, email, username, credit):
        self.first = first
        self.last = last
        self.email = email
        self.username = username
        self.credit = credit

    def greet_user(self):
        print(f"\nGreetings {self.first.title()} {self.last.title()}!")

    def describe_user(self):
        print(f"Your User name is {self.username}")
        print(f"The email we have on file is {self.email}")
        print(f"Your credit amount is {self.credit}")

# admin class with list of privs based on users
class Admin(Users):
    """A user with admin privs"""
    def __init__(self, first, last, email, username, credit):
        """initialize attributes of parent class"""
        super().__init__(first, last, email, username, credit )
        """initialize an empty list of privs"""
        self.privileges = Privileges()

# privileges class that has the admin privs
class Privileges():
    """A simple attempt to model admin prvis"""
    def __init__(self, privileges = ["can add post", "can delete post", "can ban user" ]):
        self.privileges = privileges

    def show_privs(self):
        print("Your privileges include:")
        if self.privileges:
            for privilege in self.privileges:
                print(f"- {privilege}")
        else:
            print("Sorry you have no privileges :{")

matthew = Admin('matthew', 'nickerson', 'mwn@mail.com', 'mwn', 0)

matthew.greet_user()
matthew.describe_user()
matthew.privileges.show_privs()
