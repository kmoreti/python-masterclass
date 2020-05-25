import shelve

with shelve.open('ShelfTest') as fruit:
    fruit["orange"] = "a sweet, orange, citrus fruit"
    fruit["apple"] = "good for making cider"
    fruit["lemon"] = "a sour, yellow citrus fruit"
    fruit["grape"] = "a small, sweet fruit growing in bunches"
    fruit["lime"] = "a sour, green n citrus fruit"

    print(fruit["lemon"])
    print(fruit["grape"])

print(fruit)

print("=" * 50)
fruit2 = shelve.open('ShelfTest2')
fruit2["orange"] = "a sweet, orange, citrus fruit"
fruit2["apple"] = "good for making cider"
fruit2["lemon"] = "a sour, yellow citrus fruit"
fruit2["grape"] = "a small, sweet fruit growing in bunches"
fruit2["lime"] = "a sour, green n citrus fruit"

print(fruit2["lemon"])
print(fruit2["grape"])

fruit2.close()

print(fruit2)

print("=" * 50)
fruit3 = shelve.open('ShelfTest3')
fruit3["orange"] = "a sweet, orange, citrus fruit"
fruit3["apple"] = "good for making cider"
fruit3["lemon"] = "a sour, yellow citrus fruit"
fruit3["grape"] = "a small, sweet fruit growing in bunches"
fruit3["lime"] = "a sour, green n citrus fruit"

print(fruit3["lemon"])
print(fruit3["grape"])

fruit3["lime"] = "great with tequila"

for snack in fruit3:
    print(snack + ": " + fruit3[snack])

fruit3.close()

print(fruit3)

print("=" * 50)
fruit4 = shelve.open('ShelfTest4')
fruit4["orange"] = "a sweet, orange, citrus fruit"
fruit4["apple"] = "good for making cider"
fruit4["lemon"] = "a sour, yellow citrus fruit"
fruit4["grape"] = "a small, sweet fruit growing in bunches"
fruit4["lime"] = "a sour, green n citrus fruit"

while True:
    dict_key = input("Please enter a fruit: ")
    if dict_key.casefold() == "quit":
        break

    # if dict_key in fruit4:
    #     description = fruit4[dict_key]
    # else:
    #     description = "We don't have a " + dict_key

    description = fruit4.get(dict_key, "We don't have a " + dict_key)   # Default value when the key does NOT exist
    print(description)
print("*" * 50)
for f in fruit4:
    print(f + " = " + fruit4[f])
print("-" * 50)
print("SORTED")
ordered_keys = list(fruit4.keys())
ordered_keys.sort()

for f in ordered_keys:
    print(f + " = " + fruit4[f])

print("-" * 50)
print("Values")
for v in fruit4.values():
    print(v)

print(fruit4.values())

print("-" * 50)
print("Items")
for f in fruit4.items():
    print(f)

print(fruit4.items())

fruit4.close()
