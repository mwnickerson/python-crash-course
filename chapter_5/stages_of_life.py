# Stages of life if, elif, else chain
# evaluates a persons age and tells them what they are
person_age = 30

if person_age < 2:
	print("You are a baby.")
elif person_age < 4:
	print("You are a toddler.")
elif person_age < 13:
	print("You are a kid.")
elif person_age < 20:
	print("You are a teenager.")
elif person_age < 65:
	print("You are an adult.")
else:
	print("You are an elder")