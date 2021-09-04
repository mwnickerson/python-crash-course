# My Dog
# Chapter 9
# making an instance from a class
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

my_dog = Dog('ori', 6 )
print(f"My dog's name is {my_dog.name.title()}.")
print(f"My dog is {my_dog.age} years old")

# Calling methods
my_dog.sit()
my_dog.rollover()