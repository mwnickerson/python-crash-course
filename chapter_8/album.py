# album
# chapter 8 exercise 7
# function that makes an album
# uses a dictionary inside of a function

def make_album(record_name, record_artist):
    """Return a dictionary of info about a person"""
    new_record = {'Album name': record_name, 'Artist name': record_artist}
    return new_record

album_final = make_album('Man on the Moon', 'Kid Cudi')
print(album_final)
album_final = make_album(record_artist='Porter Robinson', record_name='Nurture')
print(album_final)
album_final = make_album('Worlds', 'porter robinson')
print(album_final)