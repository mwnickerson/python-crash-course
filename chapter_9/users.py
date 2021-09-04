# Users
# Chapter 9 exercise 3
# class for users with two methods

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
# Create the users
matt_user = Users('Matthew', 'Nickerson', 'mattnick49@yahoo.com', 'mattnick49', 85)
nash_user = Users('Nash', 'Nickerson', 'nashnick84@yuck.com', 'nicknash', 91)
ori_user = Users('Ori', 'theDog', 'ori@gmail.com', 'oridog', 150 )
hacker_user = Users('Hacker', 'pwnedu', 'pwnu@gmail.com', 'h8ck3r', 99999)
# a for statement to loop through the list bc i didnt want to type
new_users = [matt_user, nash_user, ori_user, hacker_user]
for new_user in new_users:
    new_user.greet_user()
    new_user.describe_user()

