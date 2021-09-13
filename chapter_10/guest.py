# Guest
# Chapter 10 exercise 3
# program that prompts user for name
# stores response in a text document
filename = 'text_files/guest.txt'
guest_name= input("Please enter your name: ")
with open(filename, 'w') as f:
    f.write(guest_name)
