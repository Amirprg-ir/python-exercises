# ------------------------------------------------------------
# Title: Secure Login Check - Combined Conditions
# Description:
#   This script prompts the user for their age, username, and password.
#   Access is granted only if:
#     - The user is at least 18 years old, AND
#     - Either the password is correct ('python123') OR the username is 'admin'
#   This example demonstrates how to combine logical conditions using
#   AND and OR with proper use of parentheses.
# Author: amirprg-ir
# ------------------------------------------------------------

user_age = int(input("Enter your age: "))
user_name = input("Enter your user_name: ")
user_password = input("Enter your user_password: ")
if (user_age >=18) and (user_password == "python123" or user_name == "admin"):
    print("✅ Access granted. Welcome!")
else:
    exit("❌ Access denied. Invalid credentials.")