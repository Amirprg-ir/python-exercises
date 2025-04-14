# ------------------------------------------------------------
# Title: Age Group Classifier with Validation - If Elif Else
# Description:
#   This script prompts the user to enter their age and first
#   validates it to ensure the value is within a realistic range.
#   Then, using if-elif-else conditions, it classifies the user
#   into one of the following categories:
#   - Child (under 13)
#   - Teenager (13 to 19)
#   - Young Adult (20 to 35)
#   - Middle-aged (36 to 60)
#   - Senior (above 60)
# Author: amirprg-ir
# ------------------------------------------------------------

user_age = int(input("Enter your age: "))
if user_age < 1 or user_age > 150:
    exit("invalid age.")
if user_age < 13:
    print("You are a child.")
elif user_age >= 13 and user_age <= 19:
    print("You are a teenager.")
elif user_age > 19 and user_age < 36:
    print("You are a young adult.")
elif user_age > 35 and user_age < 61:
    print("You are a middle-aged.")
else:
    print("You are a senior.")