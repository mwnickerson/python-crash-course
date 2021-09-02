# T-Shirt Version 2
# Chapter 8 exercise 4
# take size and message and returns a statement
# large is the default size

def make_shirt(shirt_size='large', shirt_message='I love python'):
    """Takes a shrit size and message and printsmessage"""
    """default size is large"""
    print(f"The shirt is {shirt_size} and says {shirt_message}")

make_shirt()
make_shirt('medium')
make_shirt('small', 'SGFja1RoZVBsYW5ldA==' )
make_shirt(shirt_message='SGFja1RoZVBsYW5ldA==')

