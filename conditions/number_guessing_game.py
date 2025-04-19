# ------------------------------------------------------------
# Title: One-Time Number Guessing Game
# Description:
#   This script generates a random number between 1 and 100.
#   The user is prompted to guess the number, and the program
#   provides feedback if the guess is too high, too low,
#   or correct. Demonstrates basic conditional logic and use
#   of the random module.
# Author: amirprg-ir
# ------------------------------------------------------------

import random
user_guess_number = int(input("Guess a number between 1 and 100: "))
system_guess_number = random.randint(1, 100)
if user_guess_number == system_guess_number:
    exit("Congratulations! You guessed my number!")
elif user_guess_number > system_guess_number:
    exit(f"Too high! Try again. the system guessed is {system_guess_number}.")
else:
    exit(f"Too low! Try again. the system guessed is {system_guess_number}")
