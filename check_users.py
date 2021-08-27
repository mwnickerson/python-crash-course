# checking for unique usernames using 
current_users = ['matthew', 'nash', 'michelle', 'ori', 'theo']
new_users = ['nicole', 'stephanie', 'MATTHEW', 'Michelle', 'sam']
current_users_lower = []
for user in current_users:
	current_users_lower.append(user.lower())

for user in new_users:
	if user.lower() in current_users:
		print(f"Sorry, {user} is taken, choose another one.")
	else:
		print(f"{user} is available, would you like to use it?")