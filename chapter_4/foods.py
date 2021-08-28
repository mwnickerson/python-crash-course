# copying a list
my_foods = ['pizza', 'falafel', 'carrot cake']
friends_food = my_foods[:]

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friends_food)

my_foods.append('cannoli')
friends_food.append('ice cream')

print("\nMy favorite foods are:")
for food in my_foods:
	print(food)

print("\nMy friend's favorite foods are:")
for food in friends_food:
	print(food)

