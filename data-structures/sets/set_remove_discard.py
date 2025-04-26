# ------------------------------------------------------------
# Title: Remove and Discard Items from Set
# Description:
#   This script demonstrates how to remove items from a set
#   using remove() and discard() methods, and highlights the
#   difference between them.
# Author: amirprg-ir
# ------------------------------------------------------------

sample_set = {"amir", "ali", (12, 5), "tina"}

print(f"Original set: {sample_set}")

sample_set.remove("amir")
print(f"The set after using remove(): {sample_set}")

sample_set.discard("yousef")
print(f"The set after using discard() (item not found): {sample_set}")
