# Word Count
# Chapter 10: Exceptions
# Working with multiple files

def count_words(filename):
    """Counts the approximate number of words in a file"""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has {num_words} words.")

filenames = ['text_files/alice.txt', 'text_files/siddartha.txt',\
             'text_files/moby_dick.txt', 'text_files/little_women.txt']

for filename in filenames:
    count_words(filename)
