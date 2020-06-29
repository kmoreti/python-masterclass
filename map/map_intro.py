import timeit

text = "what have the romans ever done for us"

capitals = [char.upper() for char in text]
print(capitals)

# use map
map_capitals = list(map(str.upper, text))
print(map_capitals)

words = [word.upper() for word in text.split(' ')]
print(words)

# use map
map_words = list(map(str.upper, text.split(' ')))
print(map_words)

for x in map(str.upper, text.split(' ')):
    print(x)


def capitals():
    return [char.upper() for char in text]


def map_capitals():
    return list(map(str.upper, text))


def words():
    return [word.upper() for word in text.split(' ')]


def map_words():
    return list(map(str.upper, text.split(' ')))


if __name__ == '__main__':
    print("capitals: ", timeit.timeit(capitals, number=10000))
    print("map_capitals: ", timeit.timeit(map_capitals, number=10000))
    print("words: ", timeit.timeit(words, number=10000))
    print("mapwords: ", timeit.timeit(map_words, number=10000))
