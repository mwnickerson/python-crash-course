# class for an admin user
from user import User
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

class Admin(User):
    """A user with admin privs"""
    def __init__(self, first, last, email, username, credit):
        """initialize attributes of parent class"""
        super().__init__(first, last, email, username, credit )
        """initialize an empty list of privs"""
        self.privileges = Privileges()

# privileges class that has the admin privs
