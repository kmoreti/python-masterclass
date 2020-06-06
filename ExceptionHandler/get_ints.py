import sys


def get_int(prompt):
    while True:
        try:
            number = int(input(prompt))
            return number
        except EOFError:
            sys.exit(1)
        except ValueError:  # Should really be except ValueError:
            print("Invalid number entered, please try again!")
        finally:
            print("The finally clause always executes")


first_number = get_int("Please enter first number ")
second_number = get_int("Please enter second number ")

try:
    print("{} divided by {} is {}".format(first_number, second_number, first_number / second_number))
except ZeroDivisionError:
    print("You cannot divide by zero!!!")
    sys.exit(2)
else:
    print("Division performed successfully")
