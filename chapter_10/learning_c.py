# Learning C
# Chapter 10 exercise 2
# reading through a file and replacing python for c
filename = 'text_files/learning_python.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    line = line.rstrip()
    print(line.replace('python', 'c'))

