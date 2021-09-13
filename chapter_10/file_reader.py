# File Reader
# Chapter 10
# reads and prints the contents of a file

with open('text_files/pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())

