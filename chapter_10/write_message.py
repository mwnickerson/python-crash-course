# Write Message
# Chapter 10
# version 1
# Writing to an empty file
#filename = 'text_files/programming.txt'
#
#with open(filename, 'w') as file_object:
#    file_object.write("I love programming!")

# version 2
# Writing Multiple lines
#filename = 'text_files/programming.txt'
#
#with open(filename, 'w') as file_object:
#    file_object.write("I love programming!\n")
#    file_object.write("I love creating games!\n")

# version 3
# appending to a file
filename = 'text_files/programming.txt'

with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in a large dataset.\n")
    file_object.write("I love creating apps that can run in a browser.\n")

