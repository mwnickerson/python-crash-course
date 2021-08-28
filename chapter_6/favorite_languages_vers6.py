# looping through a dictionary's keys in a particular order
favorite_languages = {
	'jen' : 'python',
	'sarah' : 'c',
	'edward' : 'ruby',
	'phil' : 'python',
}

for name in sorted(favorite_languages.keys()):
	print(f"{name.title()}, thank you for taking the poll.")
	