# Write Message
# Chapter 10
# Writing to an empty file
filename = 'text_files/programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming!")

