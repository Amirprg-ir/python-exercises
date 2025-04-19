# ------------------------------------------------------------
# Title: Number Sign Checker (Positive, Negative, or Zero)
# Description:
#   This script prompts the user to enter a number and determines
#   whether it is positive, negative, or zero. It uses if-elif-else
#   logic and displays the result using the exit() function.
# Author: amirprg-ir
# ------------------------------------------------------------

input_number = int(input("Enter a number: "))
if input_number > 0:
    exit("the number is positive")
elif input_number < 0:
    exit("the number is negative")
else:
    exit("the number is zero")