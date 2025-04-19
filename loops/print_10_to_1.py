# ------------------------------------------------------------
# Title: Print Numbers from 10 to 1 - Two Methods (Reverse For Loop)
# Description:
#   This script prints numbers from 10 down to 1 using two different
#   methods with for loops:
#     Option 1 (recommended): Uses range with a negative step.
#     Option 2: Uses range from 1 to 10 and subtracts the index from 11.
#   This demonstrates different ways to achieve the same logic using for loops.
# Author: amirprg-ir
# ------------------------------------------------------------

# Option 1: Using range with negative step (recommended)
for i in range(10,0,-1):
    print(i)
# Option 2: Using range from 1 to 10 and subtracting i from 11
for i in range(1,11):
    print(11-i)