# Looping through values in a dictionary 
# using set() to ensure unique values

favorite_languages = {
	'jen' : 'python',
	'sarah' : 'c',
	'edward' : 'ruby',
	'phil' : 'python',
}
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()): # wrapping in set() allows removal of multiples
	print(language.title())

