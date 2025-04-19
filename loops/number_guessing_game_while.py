# ------------------------------------------------------------
# Title: Number Guessing Game with While Loop
# Description:
#   This script generates a random number between 1 and 100
#   and repeatedly asks the user to guess it. The user receives
#   feedback if their guess is too high or too low, and the number
#   of attempts is counted. The game ends when the correct number is guessed.
# Author: amirprg-ir
# ------------------------------------------------------------

import random
system_guess_number = random.randint(1, 100)
user_guess_number = int(input("Guess a number between 1 and 100: "))
user_try_number = 1
while user_guess_number != system_guess_number:
    if user_guess_number > system_guess_number:
        print("Too high! Try again")
    else:
        print("Too low! Try again")
    user_try_number += 1
    user_guess_number = int(input("Guess a number between 1 and 100: "))
print(f"🎉 Correct! You guessed the number in {user_try_number} attempts. the system guessed number is {system_guess_number}.")