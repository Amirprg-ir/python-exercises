# ------------------------------------------------------------
# Title: Multiplication Table Generator
# Description:
#   This script asks the user for a number and then prints its
#   multiplication table from 1 to 10 using a for loop.
#   The output is formatted using f-strings for clarity.
# Author: amirprg-ir
# ------------------------------------------------------------

user_input_number = int(input("Enter a number: "))
for i in  range(1,11):
    print(f"{user_input_number} * {i} = {user_input_number * i}")