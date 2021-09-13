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
filename = 'text_files/programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming!\n")
    file_object.write("I love creating games!\n")

