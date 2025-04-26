# ------------------------------------------------------------
# Title: Update, Delete and Loop Dictionary
# Description:
#   This script demonstrates updating a value, deleting a key,
#   and iterating through the updated dictionary to print all
#   key-value pairs.
# Author: amirprg-ir
# ------------------------------------------------------------

user_info = {
    "name": "amir",
    "age": 24,
    "city": "tehran",
    "email": "test@gmail.com",
    "phone number": "09120000000"
}

print(f"Dictionary before any updates: {user_info}")

user_info["city"] = "Doha"
print(f"Dictionary after updating city: {user_info}")

del user_info["phone number"]
print(f"Dictionary after deleting phone number: {user_info}")

print("--------------- Printing all items ---------------")
for key, value in user_info.items():
    print(f"{key}: {value}")
