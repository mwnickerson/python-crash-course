# Test Cities
# Chapter 11 exercise 2
#  added a second test to account for population
import unittest
from city_functions import get_city_country

class CitiesTestCase(unittest.TestCase):
    """Tests for 'city_functions.py"""

    def test_city_country(self):
        """Do Cities like Miami, Florida work?"""
        city_country = get_city_country('miami', 'florida')
        self.assertEqual(city_country, 'Miami, Florida')

    def test_city_country_population(self):
        """Do cities with a population work?"""
        city_country_population = get_city_country(
            'miami', 'florida', 5000000)
        self.assertEqual(city_country_population, "Miami, Florida - Population 5000000")

if __name__ == '__main__':
    unittest.main()