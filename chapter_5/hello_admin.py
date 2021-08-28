# greeting users based on username

system_users = ['john', 'michelle', 'nash', 'matthew', 'admin']

for user in system_users:
	if user == 'admin':
		print(f"Good morning {user.title()}, would you like to see a status report?")
	else:
		print(f"Good morning {user.title()}, thank you for logging in again.")

