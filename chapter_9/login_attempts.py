# Login Attempts
# Chapter 9 exercise 5
# class  for a user class
class User:
    """a simple attempt to simulate a user login"""
    def __init__(self, first, last, email, username, credit):
        self.first = first
        self.last = last
        self.email = email
        self.username = username
        self.credit = credit
        self.login_attempts = 0

    def greet_user(self):
        """returns  a statement that greets the user"""
        print(f"\nGreetings {self.first.title()} {self.last.title()}!")

    def describe_user(self):
        """Prints the users info"""
        print(f"Your User name is {self.username}")
        print(f"The email we have on file is {self.email}")
        print(f"Your credit amount is {self.credit}")

    def set_login_attempts(self, attempts):
        """set login attempts to number of attempts"""
        self.login_attempts = 0

    def increment_login_attempts(self, attempts):
        """increments the number of login attemtpts"""
        self.login_attempts += attempts
    def show_login_attempts(self):
        """shows the login attempts"""
        print(f"You have made {attempts} login attempts")
    def reset_login_attepts(self):
        """reset login attempts to 0"""
        self.login_attempts(0)

# Logs user in and greets them
new_user = User('Matt', 'Nickerson', 'mwn@email.com','mwn', 200)


new_user.greet_user()
new_user.describe_user()
new_user.show_login_attempts()


