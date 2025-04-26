# ------------------------------------------------------------
# Title: Tuple Count and Index
# Description:
#   This script demonstrates how to use count() and index()
#   methods on a tuple to find the number of occurrences and
#   the position of a specific element.
# Author: amirprg-ir
# ------------------------------------------------------------

names_tuple = ("sara", "ali", "mina", "tina", "sara", "amir")

print(f"Original tuple: {names_tuple}")

count_of_sara = names_tuple.count("sara")
print(f"The number of times 'sara' appears: {count_of_sara}")

first_position_of_sara = names_tuple.index("sara")
print(f"The index of the first occurrence of 'sara': {first_position_of_sara}")
