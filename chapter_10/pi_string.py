# Pi String
# Chapter 10
# version 1
# Working with a file's contents

#filename = 'text_files/pi_digits.txt'

#with open(filename) as file_object:
#    lines = file_object.readlines()

#pi_string = ''
#for line in lines:
#    pi_string += line.rstrip()

#print(pi_string)
#print(len(pi_string))


# version 2
# Large files: one million digits
filename = 'text_files/pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(f"{pi_string[:52]}...")
print(len(pi_string))
