# a dictionary containing rivers and their country
# prints a sentence about each one
# prints river name and river country from a loop

rivers_0 = {
    'nile' : 'egypt',
    'amazon' : 'brazil',
    'mississippi' : 'united states',
    'yangtze' : 'china',
    'rhine' : 'germany'
}

for river, country in rivers_0.items():
    print(f"The {river.title()} river runs through {country.title()}")

print(f"\nThe rivers that I thought of:")
for river in rivers_0.keys():
    print(river.title())

print(f"\nThe countries with rivers are:")
for country in rivers_0.values():
    print(country.title())

    