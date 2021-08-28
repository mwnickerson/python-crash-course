# Lists and accesing items in a list 
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())

# index positions start at 0 not 1
print(bicycles[1]) # 1 calls the second object in the list 
print(bicycles[3]) # calls last value in list

# calling values from a list with a negative
print(bicycles[-1])

# using individual values from a list
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)

