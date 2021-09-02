# Sending Messages
# Chapter 8 exercise 10
# sends messages using functions
def send_messages(new_messages, sent_messages):
    """Prints message and moves it to sent"""
    while new_messages:
        outbox_message = new_messages.pop()
        print(outbox_message)
        sent_messages.append(outbox_message)

new_messages = ['hello', 'whatsup', 'lmao', 'i love python']
sent_messages = []

send_messages(new_messages, sent_messages)

print("\Messages:")
print(f"outbox: {new_messages}")
print(f"sent: {sent_messages}")

