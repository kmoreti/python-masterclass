print("Today is a good day to learn Python")
print('Python is fun')
print("Python's string are easy to use")
print('We can even include "quotes" in strings')
print("hello" + " world")
greeting = "Hello"
name = input("Please enter your name ")
print(greeting + name)

# if we want a space, we can add that too
print(greeting + ' ' + name)

age = 24
print(age)

print(type(greeting))
print(type(age))

age = "2 years"
print(age)
print(type(age))

age = 24
print(name + " is " + str(age) + " years old")

print(name + f" is {age} years old")

print(f"Pi is approximatly {22 / 7 :12.50f}")

pi = 22/7
print(f"Pi is approximatly {pi:12.50f}")