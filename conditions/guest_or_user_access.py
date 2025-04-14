# ------------------------------------------------------------
# Title: Guest or User Access - Logical OR Condition
# Description:
#   This script allows access to the system if either the user
#   enters the correct password ("python123") or logs in as a guest
#   (username = "guest"). If neither condition is met,
#   the access is denied and the program exits.
# Author: amirprg-ir
# ------------------------------------------------------------

username = input("Enter your username: ")
password = input("Enter your password: ")
if username == "guest" or password == "python123":
    print("Access granted. wellcome to your account!")
else:
    exit("Access denied. Invalid credentials.")
