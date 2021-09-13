# Learning Python
# Chapter 10 exercise 1
# reading a text file and printing whats inside three different ways
filename = 'text_files/learning_python.txt'

print("Method 1: Printing entire file")
with open(filename) as file_object:
    contents = file_object.read()
print(contents)

print("\nMethod 2: Printing Line by Line")
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

print("\nMethod 3: Storing Lines in a list")
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
