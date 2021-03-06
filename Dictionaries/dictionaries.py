fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green n citrus fruit"}

print(fruit)
print(fruit["lemon"])
fruit["pear"] = "an odd shaped apple"
print(fruit)
fruit["lime"] = "great with tequila"
print(fruit)
del fruit["lemon"]
print(fruit)
fruit.clear()
print(fruit)

fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green n citrus fruit"}

for key in fruit:
    print(fruit[key])

# for i in range(10):
#     for snack in fruit:
#         print(snack + " is " + fruit[snack])
#     print("-" * 40)

while True:
    dict_key = input("Please enter a fruit: ")
    if dict_key.casefold() == "quit":
        break
    if dict_key in fruit:
        description = fruit.get(dict_key)
        print(description)
    else:
        print("We don't have a " + dict_key)

while True:
    dict_key = input("Please enter a fruit: ")
    if dict_key.casefold() == "quit":
        break
    description = fruit.get(dict_key, "We don't have a " + dict_key)
    print(description)

# ordered_keys= list(fruit.keys())
# ordered_keys.sort()

# ordered_keys= sorted(list(fruit.keys()))
# for f in ordered_keys:
#     print (f + " is " + fruit[f])
print("*" * 50)
for f in sorted((fruit.keys())):
    print (f + " is " + fruit[f])

print("-" * 50)
for f in fruit:
    print (f + " is " + fruit[f])

print("=" * 50)
for f in fruit.values(): # Not efficient
    print (f)

print("/" * 50)
print(fruit.keys())
print(fruit.values())

print("#" * 50)

fruit_keys = fruit.keys()
print(fruit_keys)
fruit["tomato"] = "not nice with ice cream"
print(fruit_keys)

print("=" * 50)
print(fruit)
print(fruit.items())

f_tuple = tuple(fruit.items())
print(f_tuple)

for snack in f_tuple:
    item, description = snack
    print(item + " is " + description)

print(dict(f_tuple))