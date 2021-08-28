# looping through all key pairs in a dictionary

user_0 = {
	'username' : 'efermi',
	'first' : 'enrico',
	'last' : 'fermi',
}

for key, value in user_0.items(): #can be shortened to "for k, v in user_0.items():"
	print(f"\nKey: {key}")
	print(f"Value: {value}")