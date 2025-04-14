# ------------------------------------------------------------
# Title: Login Validator - Combined Conditions (and)
# Description:
#   This script prompts the user to enter their age and password.
#   It validates whether the user meets both of the following:
#     - Is 18 years or older
#     - Has entered the correct password ("python123")
#   If both conditions are satisfied, access is granted.
#   Otherwise, access is denied with a friendly message.
# Author: amirprg-ir
# ------------------------------------------------------------

user_age = int(input("Enter your age: "))
user_password = input("Enter your password: ")
if user_age > 18 and user_password == "python123":
    print("Access granted. wellcome to your account.")
else:
    print("Access denied. Check your age or password and try again.")
