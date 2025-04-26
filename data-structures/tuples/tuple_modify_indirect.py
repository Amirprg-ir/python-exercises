# ------------------------------------------------------------
# Title: Modify Tuple Indirectly
# Description:
#   This script shows how to modify a tuple by first converting
#   it to a list, making changes, and then converting it back
#   to a tuple.
# Author: amirprg-ir
# ------------------------------------------------------------

names_tuple = ("sara", "mina", "tina", "sima", "amir", "ali")

print(f"Tuple before modification: {names_tuple}")

names_tuple = list(names_tuple)
names_tuple.append("ahmad")
names_tuple.insert(2, "erfan")
names_tuple = tuple(names_tuple)

print(f"Tuple after modification: {names_tuple}")
