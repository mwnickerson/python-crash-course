person_1 = {
	'first': 'michelle',
	'last': 'leon',
	'age': 27,
	'city': 'miami',
}
person_2 = {
	'first': 'theo',
	'last': 'dog',
	'age': 3,
	'city' : 'dogtown',
}
person_3 = {
	'first': 'Ori',
	'last' : 'dog',
	'age': 6,
	'city': 'dogville'
}

people = [person_1, person_2, person_3]

for person in people:
	full_name = f"{person['first'].title()} {person['last'].title()}"
	print(f"\nFull name: {full_name}")
	print(f"Age: {person['age']}")
	print(f"Location: {person['city'].title()}")