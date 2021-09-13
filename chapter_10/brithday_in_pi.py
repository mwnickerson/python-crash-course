# Is your birthday in pi
# Chapter 10
# finding whether a birthday is contained in pi
filename = 'text_files/pi_million_digits.txt'
# opens and reads first million digits of pi and stores in pi_string
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

# prompts user for birthday and tries to locate it in pi
birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first one million digits of pi")
else:
    print("Your birthday does not appear in the first million digits of pi")

    
