for i in range(1, 13):
    print("No. {0:2} squared {1:3} and cube is {2:4}".format(i, i ** 2, i ** 3))

print()

# Left alignment

for i in range(1, 13):
    print("No. {0:2} squared {1:<3} and cube is {2:<4}".format(i, i ** 2, i ** 3))

print()

# Center alignment

for i in range(1, 13):
    print("No. {0:2} squared {1:^3} and cube is {2:^4}".format(i, i ** 2, i ** 3))

print()

print("Pi is approximately {0}".format(22/7))
print("Pi is approximately {0:12}".format(22/7))
print("Pi is approximately {0:12f}".format(22/7))
print("Pi is approximately {0:12.50f}".format(22/7))
print("Pi is approximately {0:52.50f}".format(22/7))
print("Pi is approximately {0:62.50f}".format(22/7))
print("Pi is approximately {0:72.50f}".format(22/7))
print("Pi is approximately {0:<72.50f}".format(22/7))
print("Pi is approximately {0:<72.54f}".format(22/7))

print()

for i in range(1,13):
    print("No. {:2} squared {:3} and cube is {:4}".format(i, i ** 2, i ** 3))