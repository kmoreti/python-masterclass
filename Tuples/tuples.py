t = ("a", "b", "c")
print(t)

print("a", "b", "c")
print(("a", "b", "c"))
print("=" * 50)
welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
bad = "Bad Company" "Bad Company", 1974
budgie = "Night Flight", "Budgie", 1981
imelda = "More Mayhem", "Emilda May", 2011
metallica = "Ride the Lightning", "Metallica", 1984

print(metallica)
print(metallica[0])
print(metallica[1])
print(metallica[2])

# tuple object is immutable - The following code returns an error
# metallica[0] = "Master of puppets"

# you can update/change the variable assigning a new object
imelda = imelda[0], "Imelda May", imelda[2]
print(imelda)

metallica2 = ["Ride the Lightning", "Metallica", 1984]
metallica2[0] = "Master of puppets"
print(metallica2)

print("=" * 50)

title, artist, year = imelda
print(title)
print(artist)
print(year)