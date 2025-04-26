# ------------------------------------------------------------
# Title: Access Keys, Values, and Items in Dictionary
# Description:
#   This script demonstrates how to access all keys, values,
#   and key-value pairs from a dictionary using keys(), values(),
#   and items() methods.
# Author: amirprg-ir
# ------------------------------------------------------------

user_info = {
    "name": "amir",
    "age": 24,
    "city": "tehran"
}

keys = user_info.keys()
values = user_info.values()
items = user_info.items()

print(f"Keys: {keys}")
print(f"Values: {values}")
print(f"Items: {items}")
