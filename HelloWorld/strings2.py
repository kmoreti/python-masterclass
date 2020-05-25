parrot = "Norwegian Blue"

print(parrot)

# Indexing

print(parrot[3])
print(parrot[4])
print(parrot[9])
print(parrot[3])
print(parrot[6])
print(parrot[8])

print()

print(parrot[-1])
print(parrot[-14])

print()

print(parrot[-11])
print(parrot[-10])
print(parrot[-5])
print(parrot[-11])
print(parrot[-8])
print(parrot[-6])

print()

print(parrot[3 - 14])
print(parrot[4 - 14])
print(parrot[9 - 14])
print(parrot[3 - 14])
print(parrot[6 - 14])
print(parrot[8 - 14])

print()

# Slicing

print(parrot[0:6]) # Norweg
print(parrot[3:5])
print(parrot[0:9])
print(parrot[:9])
print(parrot[10:14])
print(parrot[10:])

print(parrot[:])

print()

print(parrot[-4:-2]) # Bl
print(parrot[-4:2])
print(parrot[-4:12]) # Bl

print()

# Step in Slice

print(parrot[0:6:2]) #Nre
print(parrot[0:6:3]) #Nw

number = "9,223,372,036,854,775,807"
print(number[1::4])

number = "9,223;372:036 854,775;807"
print(number[1::4])

separators = number[1::4]
print(separators)

values = "".join(char if char not in separators else " " for char in number).split()
print([int(val) for val in values])
