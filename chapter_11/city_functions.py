# City Functions
# Chapter 11 Exercise 2
# added a population function
def get_city_country(city, country, population=''):
    """Generate city country formatted"""
    if population:
        city_country = f"{city}, {country} - population {population}"
    else:
        city_country = f"{city}, {country}"
    return city_country.title()


