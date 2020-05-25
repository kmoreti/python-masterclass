import random

highest = 100
answer = random.randint(1, highest)
print(answer) # TODO: Remove after testing
guess = 0
print("Please guess a number between 1 and {}: ".format(highest))

while guess != answer:
    guess = int(input())
    if guess == 0:
        print("Game Over")
        break
    if guess == answer:
        print("Well done, you guessed it")
    else:
        if guess < answer:
            print("Please guess higher")
        else:   # guess must be grater than answer
            print("Please guess lower")
