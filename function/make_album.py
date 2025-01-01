def make_album(artist,album,songs=None):
    artist = {'artist':artist, 'album':album}
    if songs:
        artist['songs'] = songs
    return artist

a1 = make_album("jimmy Henri",'Rock')
a2 = make_album('Sonu Nigam', "Deewana")
a3 = make_album("Abhijeet Sawant", "Mohabbete")
a4 = make_album("KK","Best of KK", songs=10)

print(a1)
print(a2)
print(a3)
print(a4)

def make_album(artist,album):
    artist = {'artist':artist,'album':album}
    return artist    
while True:
    a_name = input("Please enter artist name")
    ab_name  = input("Enter album name")
artistt = make_album(a_name,ab_name)
print(artistt)
