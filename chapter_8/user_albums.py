# User Albums
# Chapter 8 exercise 8
# a function that returns a dictionary of album and artist
# takes user input and loops with a while statement

def make_album(album_name, artist_name):
    """Returns a dictionary of Album and Artist"""
    album = {'Album name': album_name, 'Artist name': artist_name}
    return album
while True:
    print("\nWhat is you favorite album? ")  # prompts user for favorite album
    print("(Enter q at any time to quit)")

    u_album = input("Favorite album: ")
    if u_album == 'q':
        break
    u_artist = input("Who is that by? ")
    if u_artist == 'q':
        break
    user_album = make_album(u_album, u_artist)
    print(user_album)


