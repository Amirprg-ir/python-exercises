# ------------------------------------------------------------
# Title: Password Checker with While Loop
# Description:
#   This script prompts the user to enter a password.
#   If the entered password is incorrect, the program will
#   ask again until the correct password is provided.
#   It uses a while loop for continuous validation.
# Author: amirprg-ir
# ------------------------------------------------------------

correct_password = "python123"
user_input_password = input("Enter your password: ")
while user_input_password != correct_password:
    print("Incorrect password. Try again!")
    user_input_password = input("Enter your password: ")
print("Access granted. ✅")