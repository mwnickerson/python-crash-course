# Dog
# chapter 9
#  creating the dog class

class Dog:
    """A simple attempt to model a dog"""
    def __init__(self, name, age):
        """initialize name and age attributes"""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command"""
        print(f"{self.name} is now sitting.")

    def rollover(self):
        """simulate rolling over in response to a command"""
        print(f"{self.name} rolled over!")