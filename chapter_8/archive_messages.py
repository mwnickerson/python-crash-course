# Archive Messages
# Chapter 8 exercise 11
# function that sends messages while retaining the original list
def send_messages(new_messages, sent_messages):
    while new_messages:
        outbox_message = new_messages.pop()
        print(f'Sending "{outbox_message}"')
        sent_messages.append(outbox_message)

new_messages = ['Hi', 'lmao', 'i love python', 'can you get dinner?']
sent_messages = []

send_messages(new_messages[:], sent_messages)

print("\nMessages:")
print(f"Sent: {sent_messages}")
print(f"Archive: {new_messages}")
