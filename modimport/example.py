print(dir())
# print(dir(__builtins__))
for m in dir(__builtins__):
    print(m)
print("=" * 50)
import shelve
print(dir())
print(dir(shelve))
print("=" * 50)
for obj in dir(shelve.Shelf):
    if obj[0] != "_":
        print(obj)

print("=" * 50)
help(shelve)