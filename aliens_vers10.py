# generating aliens 
# changes the first three aliens to yellow 


# make an empty list for storing aliens
aliens = []

# make 30 green aliens
for alien_number in range(30):
	new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
	aliens.append(new_alien)

# adds some yellow aliens
for alien in aliens[:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['points'] = '10'
		alien['speed'] = 'medium'
	elif alien['color'] == 'yellow':
		alien['color'] = 'red'
		alien['speed'] = 'fast'
		alien['points'] = 15
 
# show the first five aliens
for alien in aliens[:5]:
	print(alien)
print("...")

#show how many aliens have been created
print(f"\nTotal number of aliens: {len(aliens)}")