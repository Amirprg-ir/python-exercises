# ------------------------------------------------------------
# Title: Loop Through Dictionary Items
# Description:
#   This script demonstrates how to iterate through a
#   dictionary's key-value pairs using a for loop and items().
# Author: amirprg-ir
# ------------------------------------------------------------

user_info = {
    "name": "amir",
    "age": 24,
    "city": "tehran",
    "email": "test@gmail.com"
}

for key, value in user_info.items():
    print(f"The {key} is {value}.")
