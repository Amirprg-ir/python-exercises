# ------------------------------------------------------------
# Title: Modify Dictionary - Add, Update, Delete
# Description:
#   This script demonstrates how to modify a dictionary
#   by updating values, adding new key-value pairs, and deleting keys.
# Author: amirprg-ir
# ------------------------------------------------------------

person_info = {
    "name": "amir",
    "age": 24,
    "city": "tehran"
}

print(f"Person information before any modifications: {person_info}")

person_info["city"] = "Doha"
print(f"Person information after changing city: {person_info}")

person_info["email"] = "amirprg@gmail.com"
print(f"Person information after adding email: {person_info}")

del person_info["age"]
print(f"Person information after removing age: {person_info}")
