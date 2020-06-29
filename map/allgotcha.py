entries = []

# 1st gotcha
if entries:
    print("all: {}".format(all(entries)))
else:
    print(False)
print("any: {}".format(any(entries)))

# 2nd gotcha
result = bool(entries) and all(entries)
print(result)
