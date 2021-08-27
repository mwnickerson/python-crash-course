# invite more guests to the dinner by adding entries to the list 
guest = ['alexander the great', 'genghis khan', 'kevin mitnick', 'J.R.R Tolkien', 'john f. kennedy']
print(f"Unfortunately, {guest[4].title()} can't make it to the party.")
guest[4] = 'babe ruth'
print("Esteemed Guests,\nI have found a larger table so we will be inviting more guests!")
guest.insert(0, 'teddy roosevelt')
guest.insert(2, 'Thomas Paine')
guest.append('king arthur')

print(f"Dear {guest[0].title()}, \nPlease join me for a great feast")
print(f"Dear {guest[1].title()}, \nCome talk of your conquests.")
print(f"Dear {guest[2].title()}, \nJoin us and tell your stories")
print(f"Dear {guest[3].title()}, \nCome and chronicle our feast.")
print(f"Dear {guest[4].title()}, \nJoin us for dinner, it will be a homerun!")
print(f"Dear {guest[5].title()}, \nCome to dinner make sure to bring potatoes")
print(f"Dear {guest[6].title()}, \nPlease join me for some food")
print(f"Dear {guest[7].title()}, \nCome grab some grub")

print(guest)