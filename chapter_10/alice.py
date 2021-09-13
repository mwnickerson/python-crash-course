# Alice
# Chapter 10: Exceptions
# Handling the FileNotFound exception

#This throws a FileNotFoundError
#filename = 'text_files/alice.txt'
#
#with open(filename, encoding='utf-8') as f:
#    contents = f.read()
#
# This will handle the error of file not founf
#filename = 'text_files/alice.txt'
#
#try:
#    with open(filename, encoding='utf-8') as f:
#        contents = f.read()
#except FileNotFoundError:
#    print(f"Sorry, the file {filename} does not exist")

# Analyzing text
filename = 'text_files/alice.txt'

try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"sorry, the file {filename} was not found")
else:
    # Counts the number of words in the files
    words = contents.split()
    num_words = len(words)
    print(f"The file {filename} has {num_words} words.")
