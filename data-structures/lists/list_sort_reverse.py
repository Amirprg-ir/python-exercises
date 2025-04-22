# ------------------------------------------------------------
# Title: Sort and Reverse List
# Description:
#   This script creates a list of numbers, sorts it in ascending
#   order using sort(), then reverses the sorted list using reverse().
# Author: amirprg-ir
# ------------------------------------------------------------

list_numbers = [58, 85, 93, 14, 51, 35, 58, 73, 92.5, 14.75, 783]

print(f"Original list: {list_numbers}")

list_numbers.sort()
print(f"List sorted in ascending order: {list_numbers}")

list_numbers.reverse()
print(f"List sorted in descending order: {list_numbers}")
