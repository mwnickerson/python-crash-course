# Person Version 2
# Chapter 8
# Returning a dictionary with an optional argument

def build_person(first_name, last_name, age=None):
    """Return a dictionary of info on a person"""
    person ={'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person
musician = build_person('Jimi', 'Hendrix', age=27 )
print(musician)
