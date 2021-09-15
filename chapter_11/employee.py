# Employee functions
# Chapter 11 exercise 3

class Employee():

    def __init__(self, first_name, last_name, salary):
        """Initialize the employee"""
        self.first = first_name.title()
        self.last = last_name.title()
        self.salary = salary

    def give_raise(self, amount=5000):
        """give the employee a raise"""
        self.salary += amount

