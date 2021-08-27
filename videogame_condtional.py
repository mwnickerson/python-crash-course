# a series of conditional tests regarding video games
video_game = 'elden ring'
print("Is the video game Elden Ring?")
print( video_game == 'elden ring')

print("Is the video game Call of Duty?")
print( video_game == 'Call of Duty')

good_game = 'parkitect'
print("\nIs the good video game parkitect?")
print(good_game == 'parkitect')

print("Is the good video game Escape from Tarkov?")
print(good_game == 'Escape from Tarkov')

bad_game = 'last of us'
print("\nIs the bad game fortnite?")
print(bad_game == 'fortnite')

print("Is the bad game last of us?")
print(bad_game == 'last of us')

strat_game = 'humankind'
print("\nIs the 4X game Age of Empires?")
print(strat_game == 'age of empires')

print("Is the 4x game humankind?")
print(strat_game == 'humankind')

board_game = 'monopoly'
print("\nIs the board game stratego?")
print(board_game == 'stratego')
print("Is the board game monopoly")
print(board_game == 'monopoly')

owned_games = ['parkitect', 'humankind', 'sea of thieves',\
 'escape from tarkov']
sale_game = 'elden ring'

print(f"\n{sale_game.title()} is on sale!")
if sale_game not in owned_games:
	print(f"You do not own {sale_game.title()},\
	 buy it now!")

if len(owned_games) >= 2:
	print(f"\nMaybe you own too many games to play")
	print(f"Do not buy {sale_game}")

sale_game2 = 'parkitect'
print(f"\n{sale_game2.title()} is on sale!")
print(f"Do you own {sale_game2}?")
if sale_game2 in owned_games:
	print(f"You own {sale_game2.title()},\
	 do not buy it!")

