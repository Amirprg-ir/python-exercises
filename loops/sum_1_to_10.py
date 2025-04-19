# ------------------------------------------------------------
# Title: Sum Numbers from 1 to 10 - For Loop
# Description:
#   This script calculates the sum of numbers from 1 to 10
#   using a for loop. It maintains a running total and prints
#   the result at the end using an f-string for formatting.
# Author: amirprg-ir
# ------------------------------------------------------------

total = 0
for i in range(1, 11):
    total += i
print(f"the sum of 1 to 10 is => {total}")