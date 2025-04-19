# ------------------------------------------------------------
# Title: Login System with 3 Attempts - While Loop
# Description:
#   This script prompts the user to enter the correct password.
#   The user is allowed up to 3 attempts. If the correct password
#   is not entered within the limit, the account is locked.
#   Otherwise, access is granted.
# Author: amirprg-ir
# ------------------------------------------------------------

input_pasword = input("Enter your password: ")
corret_password = "python123"
try_counter = 3
while input_pasword != corret_password:
    if try_counter == 1 :
        exit("❌ Account locked. Too many failed attempts.")
    try_counter -= 1
    input_pasword = input("Enter your password again: ")
print("✅ Access granted.")