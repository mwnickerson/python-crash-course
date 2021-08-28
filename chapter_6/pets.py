# using dictionaries to display knowledge on pets

pet_0 = {
	'name': 'Ori',
	'owner': 'matthew',
	'type': 'dog',
	'age': 6,
	'activity': 'eating' ,
}
pet_1 = {
	'name': 'theo',
	'owner': 'michelle',
	'type': 'dog',
	'age': 3,
	'activity': 'licking'
}
pet_2 = {
	'name': 'mufasa',
	'owner': 'stephanie',
	'type': 'cat',
	'age' : 'unknown',
	'activity': 'humping',
}

pets = [pet_0, pet_1, pet_2]

for pet in pets:
	print(f"\nPet Name: {pet['name'].title()} ")
	print(f"\tOwner Name: {pet['owner'].title()}")
	print(f"\tAge: {pet['age']}")
	print(f"\tFavorite Activity: {pet['activity']}")
