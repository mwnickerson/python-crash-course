# Test Employee
# Chapter 11 exercise 3
# tests the employee function

import unittest

from employee import Employee

class TestEmployee(unittest.TestCase):
    """tests for the class Employee"""

    def setUp(self):
        """makes an employee for the tests"""
        self.matthew = Employee('matthew', 'nickerson', 80_000 )

    def test_default_give_raise(self):
        self.matthew.give_raise()
        self.assertEqual(self.matthew.salary, 85000)

    def test_custome_give_raise(self):
        self.matthew.give_raise(7000)
        self.assertEqual(self.matthew.salary, 87000)
