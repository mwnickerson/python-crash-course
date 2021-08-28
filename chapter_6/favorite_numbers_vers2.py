# Favorite Numbers
# Allowing people to have multiple numbers

favorite_numbers = {
	'nash': [1, 12, 42],
	'theo': [6, 420, 1001],
	'michelle': [15, 26, 7],
	'ori': [9, 8, 12],
	'nicole': [69, 420, 180],
}

for name, numbers in favorite_numbers.items():
	print(f"\n{name.title()}")
	for number in numbers:
		print(number)

		