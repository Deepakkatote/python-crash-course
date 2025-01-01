def make_album(artist,album,songs=None):
    artist = {'artist':artist,
              'album':album}
    if songs:
        artist['songs'] = songs
    return  artist

while True:
    a_name = input("Enter artist name: ")
    if a_name == "quit":
        break
    alb_name = input("Enter album name: ")
    if alb_name == "quit":
        break
    
    album = make_album(a_name,alb_name, songs=20)
    print(album)
    album11 = make_album(a_name,alb_name, songs=10)
    print(album11)

