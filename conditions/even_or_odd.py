# ------------------------------------------------------------
# Title: Even or Odd Number Checker
# Description:
#   This script prompts the user to enter an integer number and
#   checks whether it is even or odd using the modulo operator (%).
#   It prints a corresponding message based on the result.
# Author: amirprg-ir
# ------------------------------------------------------------

input_number = int(input("Enter a number: "))
if input_number % 2 == 0:
    print("The Number Is Even!")
else:
    print("The Number Is Odd!")