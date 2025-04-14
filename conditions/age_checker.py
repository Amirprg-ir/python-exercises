# ------------------------------------------------------------
# Title: Age Checker with Validation - If Else Condition
# Description:
#   This script prompts the user to enter their age and
#   performs basic validation to ensure the age is within
#   a realistic range (1 to 150). If the age is invalid,
#   the program exits with an error message. Otherwise,
#   it checks whether the user is an adult (18 or older)
#   and prints an appropriate message using if-else logic.
# Author: amirprg-ir
# ------------------------------------------------------------

user_age = int(input("Enter your age: "))
if user_age < 1 or user_age > 150:
    exit("invalid age")
if user_age >= 18:
    print("You are an adult.")
else:
    print("You are underage.")