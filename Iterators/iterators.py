string = "1234567890"

# for char in string:
#     print(char)

# my_iterator = iter(string)
# print(my_iterator)
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))

# for char in string:
#     print(char)
#
# print()
#
# for char in iter(string):
#     print(char)
#
items = [1, 2, 3, 4, 5]

my_iter = iter(items)

for i in range(len(items)):
    print(next(my_iter))



my_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

my_iterator = iter(my_list)

for i in range(len(my_list)):
    next_item = next(my_iterator)
    print(next_item)
