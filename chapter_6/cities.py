# Cities
# dictionaries inside of dictionaries

cities = {
	'miami': {
	'state': 'florida',
	'sports team': 'hurricanes',
	'attraction' : 'south beach'
	},
	'philadelphia': {
	'state': 'pennsylvania',
	'sports team': 'eagles',
	'attraction': 'liberty bell'
	},
	'new york city': {
	'state': 'new york',
	'sports team': 'yankees',
	'attraction': 'times square'
	}
}
for city, city_info in cities.items():
	print(f"\nCITY: {city.title()}")
	state = city_info['state'].title()
	sports_team = city_info['sports team'].title()
	attraction = city_info['attraction'].title()
	print(state)
	print(sports_team)
	print(attraction)
	
