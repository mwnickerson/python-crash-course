# a shorter version of amusement_park.py

age = 16

if age < 4:
	price = 0
elif age < 18:
	price = 25
elif age < 65:
	price = 40
elif age >= 65: 
	price = 20

print(f"You admission cost is ${price}.")