# City Country
# Chapter 11 exercise 1

from city_functions import get_city_country

print("Enter 'q' at any time to quit")

while True:
    city = input("Please enter a city: ")
    if city == 'q':
        break
    country = input("Please enter a country: ")
    if country == 'q':
        break

    city_country = get_city_country(city, country)
    print(f"\t{city}, {country}")

