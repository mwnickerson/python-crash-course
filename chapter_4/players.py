# looping through a slice
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:
	print(player.title())

print("The first three items in the list are:")
for player in players[:3]:
	print(player.title())

print("\nThe middle three items in the list are:")
for player in players[1:4]:
	print(player.title())

print("\nThe last three items in the list are:")
for player in players[2:5]:
	print(player.title())
