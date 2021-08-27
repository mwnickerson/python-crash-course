# removes guests from the list
guest = ['alexander the great', 'genghis khan', 'kevin mitnick', 'J.R.R Tolkien', 'john f. kennedy']
print(f"Unfortunately, {guest[4].title()} can't make it to the party.")
guest[4] = 'babe ruth'
print("Esteemed Guests,\nI have found a larger table so we will be inviting more guests!")
guest.insert(0, 'teddy roosevelt')
guest.insert(2, 'Thomas Paine')
guest.append('king arthur')
print("Sorry for the dissapointment, but that table broke\nI will be uninviting some of you")
univited_guest = guest.pop()
print(f"I am sorry {univited_guest.title()} there is no room for you at dinner")
univited_guest = guest.pop()
print(f"Unfortuantely dinner is canceled, {univited_guest.title()}, we will have dinner soon")
univited_guest = guest.pop()
print(f"No dinner for  you, {univited_guest.title()}, we will get em next time")
univited_guest = guest.pop(0)
print(f"Sorry {univited_guest.title()}, you didn't make the cut")
univited_guest = guest.pop()
print(f"My bad, {univited_guest.title()}, the table just couldn't fit us all")
univited_guest = guest.pop(1)
print(f"You almost made the cut {univited_guest.title()} but didn't.")

print(f"Dinner is still on {guest[0].title()}")
print(f"Sorry for the scare {guest[1].title()} dinner is still on.")

del guest[0]
del guest[0]

print(guest)
