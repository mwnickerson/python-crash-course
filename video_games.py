# a program to perform functions on a list of video games
games = ['call of duty', 'star wars battlefront', 'parkitect', 'escape from tarkov', 'humankind']
print(games)
print(games[3])
print(f"I am most excited to play {games[-1].title()} shortly")

games[1] = 'sea of thieves' # replaces the second item in the list
print(games)
games.append('new world') # adds a game to the end of the list
print(games) 

games.insert(2, 'population one') # adds a game in a position on a list
print(games)

del games[6]
print(games)

dead_game = games.pop(4)  # pop a game off the list and use the popped list item
print(f"I dont play {dead_game.title()} anymore")
print(games)

bad_game = 'call of duty'  # remove a game by name
games.remove(bad_game)
print(games)
print(f"\nI no longer play {bad_game} because it takes up too much space on my hard drive.")

print("\nHere is the list of games I play in alphabetical order")
print(sorted(games))
print("\nHere is the list of games I play in reverse order:")
print(sorted(games, reverse=True))
print("\nHere is the list before being sorted:")
print(games)

print(f"\nI used to play more games but now i only play {len(games)} games")














