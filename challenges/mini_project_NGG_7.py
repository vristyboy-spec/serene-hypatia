#Number Guessing Game Project

import random

secret_number = random.randint(1,10)
guess = 0

while guess != secret_number:
    guess = int(input("guess the number:"))
    if guess < secret_number:
        print("Too low")
    elif guess > secret_number:
        print("Too high")
    else:
        print("You got it!")