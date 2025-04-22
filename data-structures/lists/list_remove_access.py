# ------------------------------------------------------------
# Title: Remove and Access List Items
# Description:
#   This script creates a list of names, removes one item using
#   the remove() method, and accesses the first and last elements
#   using indexing. It also displays the list before and after changes.
# Author: amirprg-ir
# ------------------------------------------------------------

names = ["amir","ali","reza","yousef"]
print(f"the list before any changes: {names}")
names.remove("ali")
print(f"the list after any changes: {names}")
print(f"the first element in the list is => {names[0]}")
print(f"the last element in the list is => {names[-1]}")
