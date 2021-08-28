# Favorite places 
# lists inside of dictionaries
favorite_places = {
	'michelle': ['venezuela', 'canada', 'miami'],
	'nash': ['new hampshire', 'missouri', 'japan'],
    'matthew': ['china', 'australia', 'china']
}

for name, places in favorite_places.items():
    print(f"\n{name.title()}'s favorite places are: ")
    for place in places:
        print(f"\t{place.title()}")
