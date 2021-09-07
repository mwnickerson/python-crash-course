# Admin
# Chapter 9 exercise 7
# a class for an admin based off of User

# user class with greeting and description
class Users:
    """a simple attempt at user system"""
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
    """a simple attempt at an admin system"""
    def __init__(self, first, last, email, username, credit):
        """initialize attributes of parent class"""
        super().__init__(self)
        self.admin_rights = ['can add post', 'can delete post', 'can ban user']
    def show_privileges(self):
        print(f"Your special privs include: {self.admin_rights} ")

# calling the class with admin

admin_user = Admin('Admin', 'Admin','admin@mail.com', 'admin', 0)
admin_user.greet_user()
admin_user.describe_user()
admin_user.show_privileges()

