# File Reader
# Chapter 10
# reads and prints the contents of a file

# Version 1
# with open('text_files/pi_digits.txt') as file_object:
#    contents = file_object.read()
#    print(contents.rstrip())

# Version 2
# reading line by line
#filename = 'text_files/pi_digits.txt'
#
#with open(filename) as file_object:
#    for line in file_object:
#        print(line.rstrip())

# Version 3
# making a list of lines from a file
filename = 'text_files/pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

