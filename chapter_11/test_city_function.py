# Test City Function
# Chapter 11: Exercise 1
# Test for city_country function

import unittest
from city_functions import get_formatted_city

class CityTestCase(unittest.TestCase):
    """Tests for 'city_functions.py'."""

    def test_city_country(self):
        """Do cities like Miami, Florida work?"""
        formatted_city = get_formatted_city('miami', 'united states of america')
        self.assertEqual(formatted_city, 'Miami, United States Of America')

if __name__ == '__main__':
    unittest.main()
