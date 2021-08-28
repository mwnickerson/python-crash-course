# favorite language polling
# runs through list of people 
# checks if they have taken the poll on their fave language

favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python',
}

poll_takers = ['sarah', 'edward', 'michelle', 'edgar']

for name in poll_takers:
    print(f"\nHi {name.title()}!")
    if name not in favorite_languages.keys():
        print("Please take the poll")
    else:
        print("Thank you for taking the poll!")
    

