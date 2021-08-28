# one of the guests cant make it, program removes them and invites someone else
guest = ['alexander the great', 'genghis khan', 'kevin mitnick', 'J.R.R Tolkien', 'John F. Kennedy']
print(f"Unfortunately, {guest[4].title()} can't make it to the party.")
guest[4] = 'babe ruth'

print(f"Dear {guest[0].title()}, \nPlease join me for a great feast")
print(f"Dear {guest[1].title()}, \nCome talk of your conquests.")
print(f"Dear {guest[2].title()}, \nJoin us and tell your stories")
print(f"Dear {guest[3].title()}, \nCome and chronicle our feast.")
print(f"Dear {guest[4].title()}, \nJoin us for dinner, it will be a homerun!")

