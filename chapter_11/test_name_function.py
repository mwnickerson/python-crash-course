# Test Name Function
# Chapter 11
# Unit tests and Test cases: A passing test

import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Tests for 'name_fucntion.py'."""

    def test_first_last_name(self):
        """DO names like 'Janis Joplin' Work"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

if __name__ == '__main__':
    unittest.main()
