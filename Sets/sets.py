farm_animals = {"sheep", "cow", "hen"}
print(farm_animals)

for animal in farm_animals:
    print(animal)

print("=" * 50)

wild_animals = set(["lion", "tiger", "panther", "elephant", "hare"])

for animal in wild_animals:
    print(animal)

farm_animals.add("horse")
wild_animals.add("horse")
print(farm_animals)
print(wild_animals)

print(sorted(farm_animals))

print("=" * 50)

empty_set = set()
empty_set_2 = {} # creates a dictionary, not a set
empty_set.add("a")
# empty_set_2.add("a")

even = set(range(0, 40, 2))
print("even: {}".format(even))
squares_tuple = (4, 6, 9, 16, 25)
squares = set(squares_tuple)
print("squares: {}".format(squares))

print("=" * 50)
print("UNION")
even = set(range(0, 40, 2))
print("even: {}".format(even))
print("len(even): {}".format(len(even)))

squares_tuple = (4, 6, 9, 16, 25)
squares = set(squares_tuple)
print("squares: {}".format(squares))
print("len(squares): {}".format(len(squares)))

print("even union squares")
print(even.union(squares))
print(len(even.union(squares)))
print("squares union even")
print(squares.union(even))

print("=" * 50)
print("INTERSECTION")
print("even intersection squares")
print(even.intersection(squares))
print(even & squares)
print("squares intersection even")
print(squares.intersection(even))
print(squares & even)

print("=" * 50)
print("DIFFERENCE")

even = set(range(0, 40, 2))
print("even: {}".format(sorted(even)))
squares_tuple = (4, 6, 9, 16, 25)
squares = set(squares_tuple)
print("squares: {}".format(sorted(squares)))

print("even minus squares")
print(sorted(even.difference(squares)))
print(sorted(even - squares))

print("squares minus even")
print(sorted(squares.difference(even)))
print(sorted(squares - even))


print("=" * 50)
print(sorted(even))
print(squares)
print(sorted(even))

print("=" * 50)

even = set(range(0, 40, 2))
print("even: {}".format(sorted(even)))
squares_tuple = (4, 6, 9, 16, 25)
squares = set(squares_tuple)
print("squares: {}".format(sorted(squares)))

print("Symmetric difference even minus squares")
print(even.symmetric_difference(squares))

print("Symmetric difference squares minus even")
print(squares.symmetric_difference(even))

print("=" * 50)

even = set(range(0, 40, 2))
print("even: {}".format(even))
squares_tuple = (4, 6, 9, 16, 25)
squares = set(squares_tuple)
print("squares: {}".format(squares))

squares.discard(4)
squares.remove(16)
squares.discard(8)  # no error, does nothing
print("squares: {}".format(squares))
# squares.remove(8)   # throws error if the item does not exist
if 8 in squares:
    squares.remove(8)

try:
    squares.remove(8)
except KeyError:
    print("The item 8 is not a member of the set")


print("=" * 50)

even = set(range(0, 40, 2))
print("even: {}".format(even))
squares_tuple = (4, 6, 16)
squares = set(squares_tuple)
print("squares: {}".format(squares))

if squares.issubset(even):
    print("squares is a subset of even")

if even.issuperset(squares):
    print("even is a superset of squares")

print("=" * 50)

even = frozenset(range(0, 100, 2))
print(even)
