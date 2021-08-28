# greeter version 2
# chapter 7
# greeting with more than one line
prompt = "If you tell us who you are, we can \
 personalize the message you see."
prompt += "\nWhat is your first name?"
name = input(prompt)
print(f"\nHello {name.title()}!")
