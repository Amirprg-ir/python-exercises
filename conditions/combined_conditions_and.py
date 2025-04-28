# ------------------------------------------------------------
# Title: Combined Conditions with AND Operator
# Description:
#   This script demonstrates combining two conditions using
#   the 'and' operator to validate age and city.
# Author: amirprg-ir
# ------------------------------------------------------------

user_city = input("What is your city name? ")
user_age = int(input("What is your age? "))

if user_age > 120 or user_age < 1:
    exit("Invalid age.")

if user_age > 18 and user_city == "tehran":
    print("Access granted. ✅")
else:
    exit("Access denied. ❌")
