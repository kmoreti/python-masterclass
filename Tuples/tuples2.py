imelda = "More Mayhem", "Emilda May", 2011, (
    (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))
print(imelda)

print(len(imelda))

title, artist, year, tracks = imelda
print(title)
print(artist)
print(year)
print(tracks)

print(len(tracks))

my_iterator = iter(tracks)
for i in range(len(tracks)):
    track, song = next(my_iterator)
    print("Track #{} - {}".format(track, song))

print("=" * 50)
print("Challenge")
print("=" * 50)

imelda = "More Mayhem", "Emilda May", 2011, (
    (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))

title, artist, year, tracks = imelda
print(title)
print(artist)
print(year)
for song in tracks:
    track, title = song
    print("\tTrack #{} - {}".format(track, title))

print("=" * 50)

imelda = "More Mayhem", "Emilda May", 2011, (
    [(1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz")],
    [(1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz")]
)

print(imelda)

imelda[3][0].append((5, "All for You"))
title, artist, year, tracks = imelda
tracks[1].append((6, "Eternity"))
print(title)
print(artist)
print(year)
for trackx in tracks:
    for song in trackx:
        track, title = song
        print("\tTrack #{} - Title: {}".format(track, title))

