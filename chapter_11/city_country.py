# City Country
# Chapter 11: Exercise 1
# program that prints formatted city country
from city_functions import get_formatted_city

print("Enter 'q' at any time to quit.")
while True:
    city = input("\nPlease enter a city: ")
    if city == 'q':
        break
    country = input("Enter the country that city resides in:")
    if country == 'q':
        break

    city_country = get_formatted_city(city, country)
    print(f"{city_country}")