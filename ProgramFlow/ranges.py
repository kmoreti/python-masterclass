for i in range(1, 21):
    print("i is now {}".format(i))
print("*" * 80)
for i in range(1, -5, -1):
    print("i is now {}".format(i))
print("*" * 80)
for i in range(10):
    print("i is now {}".format(i))
print("*" * 80)
for i in range(0, 10, 2):
    print("i is now {}".format(i))
print("*" * 80)
for i in range(10, 0, -2):
    print("i is now {}".format(i))

# This solution uses a step value for the range function
for i in range(0, 101, 7):
    print(i)

# This solution uses a slice
for i in range(101)[::7]:
    print(i)
