my_pizzas = ['pepperoni', 'cheese', 'buffalo chicken']
friend_pizzas = my_pizzas[:]
my_pizzas.append('sausage')
friend_pizzas.append('hawaiian')
print("My favorite foods are:")
for pizza in my_pizzas:
	print(pizza)

print("\nMy friend's favorite foods are:")
for pizza in friend_pizzas:
	print(pizza)
	