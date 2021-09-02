# city names
# chapter 8 exercise 6
# function that takes in and formats name of a city and country

def city_country(city_name, city_country):
    """returns city name and country formatted"""
    city_formatted = {'City': city_name, 'Country': city_country}
    return city_formatted

city = city_country('Santiago', 'Chile')
print(city)
city = city_country('Miami', 'u.s.a')
print(city)
city = city_country('shanghai', 'china')
print(city)


