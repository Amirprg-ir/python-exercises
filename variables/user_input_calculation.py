# ------------------------------------------------------------
# Title: Age Projection - 10 Years Later
# Description:
#   This script prompts the user to enter their current age,
#   converts the input to an integer, calculates their age
#   after 10 years, and prints the result in a friendly message.
#   It helps beginners understand type conversion and arithmetic.
# Author: amirprg-ir
# ------------------------------------------------------------

user_age = int(input("Enter your age: "))
user_age_after_10_years = user_age + 10
output = f"Your age is {user_age} and your age after 10 years is {user_age_after_10_years}. have a good time."
print(output)