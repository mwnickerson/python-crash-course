# Programming Poll
# Chapter 10 exercise 5
# asks users why they like programming
# stores the results in a poll results
filename = 'text_files/programming_poll_results.txt'
print("Welcome to the programming poll")
print(" Enter 'quit' to exit at any point")
while True:
    user_name = input("Enter your name: ")
    if user_name == 'quit':
        break
    else:
        programming_reason = input("Why do you like programming? ")
    if programming_reason == 'quit':
        break
    else:
        with open(filename, 'a') as f:
            f.write(f"{user_name}: {programming_reason}\n")
