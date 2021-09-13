# user class with greeting and description
class User:
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


