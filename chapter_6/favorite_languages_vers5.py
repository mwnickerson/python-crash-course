# printing a message to friends about their langauge
# using keys() to determine if someone took the poll

favorite_languages = {
	'jen' : 'python',
	'sarah' : 'c',
	'edward' : 'ruby',
	'phil' : 'python',
}

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
	print(f"\nHi {name.title()}.")

	if name in friends:
		language = favorite_languages[name].title()
		print(f"\t{name.title()}, I see you love {language}!")
	if 'erin' not in favorite_languages.keys():
		print("Erin, please take our poll!")