def make_album(artist,album):
    artist = {'artist':artist,
              'album':album}
    return artist

while True:
    a_name = input("Enter name of the artist: ")
    if a_name == "q":
        break
    alb_name = input("Enter the album: ")
    if alb_name == "q":
        break
    album = make_album(a_name,alb_name)
    print(album)