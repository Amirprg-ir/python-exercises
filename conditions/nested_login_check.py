# ------------------------------------------------------------
# Title: Nested Login Check - Age and Password Validation
# Description:
#   This script first checks if the user's age is at least 18.
#   If the user is underage, access is denied immediately.
#   Otherwise, it asks for a password. If the password matches
#   the expected value, access is granted. Otherwise, access is denied.
#   Demonstrates nested if conditions in a real-world scenario.
# Author: amirprg-ir
# ------------------------------------------------------------

user_age = int(input("Enter your age: "))
if user_age < 18:
    exit("Access denied due to age restriction!")
else:
    user_pass = input("Enter your password: ")
    if user_pass == "python123":
        print("Access Granted. wellcome to your account!")
    else:
        print("invalid password!")