# Common Words
# Chapter 10 exercise 10
# Analyzing some books from project gutenberg
def word_count(filename):
    """Counts the amount of a word in"""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"{filename} not found.")
    word_count = contents.lower().count('the ')
    print(f"The file {filename} has the word 'the' {word_count} times.")

filenames = ['text_files/alice.txt', 'text_files/arthur.txt', 'text_files/gatsby.txt',\
             'text_files/moby_dick.txt', 'text_files/little_women.txt',\
             'text_files/odyssey.txt', 'text_files/sherlock.txt']

for filename in filenames:
    word_count(filename)
