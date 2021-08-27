# greeting users based on usernames
# checks to see if list is empty

system_users = ['john', 'michelle', 'nash', 'matthew', 'admin']

if system_users:
	for user in system_users:
		if user == 'admin':
			print(f"Good Morning {user.title()},  would you like to see a status report?")
		else:
			print(f"Good Morning {user.title()}, thank you for logging in today.")
else:
	print("We need to find a few users!")


system_users = []

if system_users:
	for user in system_users:
		if user == 'admin':
			print(f"Good Morning {user.title()},  would you like to see a status report?")
		else:
			print(f"Good Morning {user.title()}, thank you for logging in today.")
else:
	print("We need to find a few users!")