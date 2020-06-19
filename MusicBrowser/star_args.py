# from __future__ import print_function  # python 2
# print("Hello", "planet", "Earth")

# from __future__ import division


def average(*args):
    print(type(args))
    print("args is {}".format(args))
    print("*args is {}", *args)
    mean = 0
    for arg in args:
        mean += arg
    return mean / len(args)


print(average(1, 2, 3, 4))


# def print_backwards(*args, end=' ', **kwargs):
# def print_backwards(*args, **kwargs):
#     print(kwargs)
#     kwargs.pop('end', None)
#     for word in args[::-1]:
#         print(word[::-1], end=' ', **kwargs)

def print_backwards(*args, **kwargs):
    end_character = kwargs.pop('end', '\n')
    sep_character = kwargs.pop('sep', '\n')
    for word in args[:0:-1]:
        print(word[::-1], end=sep_character, **kwargs)
    # print(end=end_character)
    print(args[0][::-1], end=end_character, **kwargs)


def backwards_print(*args, **kwargs):
    sep_character = kwargs.pop('sep', ' ')
    print(sep_character.join(word[::-1] for word in args[::-1]), **kwargs)


with open("backwards.txt", 'w') as backwards:
    print_backwards("hello", "planet", "earth", "take", "me", "to", "your", "leader", end='\n')
    print("Another String")

print()
print("hello", "planet", "earth", "take", "me", "to", "your", "leader", end='', sep="\n**\n")
print_backwards("hello", "planet", "earth", "take", "me", "to", "your", "leader", end='', sep="\n**\n")
print("="*10)

backwards_print("hello", "planet", "earth", "take", "me", "to", "your", "leader", end='', sep="|")