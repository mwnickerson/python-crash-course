# Cats and Dogs
# Chapter 10 exercise 8
# Prints list of cats and dogs from multiple files
# Handles FileNotFoundError
def pet_names(filename):
    """Prints the names of pets from file"""
    try:
        with open(filename, encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"{filename} cannot be found.")
    else:
        for line in lines:
            print(line.rstrip())

filenames = ['text_files/dogs.txt', 'text_files/cats.txt', 'gerbils.txt']
for filename in filenames:
    print(f"---{filename}---")
    pet_names(filename)