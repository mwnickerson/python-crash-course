# Cities
# Chapter 8 exercise 5
# a function that take name and city and retruns a statement
# has a default city and country

def describe_city(city='Miami', country='U.S.A'):
    print(f"{city.title()} is in {country.title()}")
describe_city()
describe_city('paris','france')
describe_city('philadelphia')
describe_city('Austin')

