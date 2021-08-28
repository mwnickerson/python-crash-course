# modifying items in a list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

# Adding elements to a list 
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.append('ducati')
print(motorcycles)

# building a list with append
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print(motorcycles)

# inserting elements into a list
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)

# removing elements from a list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[0]
print(motorcycles)
motorcycles = ['honda', 'yamaha', 'suzuki']
del motorcycles[1]
print(motorcycles)

# Removing item with pop()
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

# Use case of pop
motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()

print(f"The last motorcycle I owned was a {last_owned.title()}")

# Popping from any position
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)

print(f"The first motorcycles I owned was a {first_owned.title()}")

# Removing an item by value
motorcycles = ['ducati', 'honda', 'yamaha', 'suzuki']

print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

# Use case 
motorcycles = ['ducati', 'honda', 'yamaha', 'suzuki']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")