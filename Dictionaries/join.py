my_list = ["a", "b", "c", "d"]
letters="abcdefghijklmnopqrstuvwxyz"

new_string = ''
for c in my_list:
    new_string += c + ", " # inneficient because it creates a new string object each iteration
print(new_string)


new_string = ", ".join(my_list)
print(new_string)

new_string = ", ".join(letters)
print(new_string)

numbers = "123456789"
new_string = " mississippi, ".join(numbers)
print(new_string)
