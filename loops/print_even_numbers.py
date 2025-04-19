# ------------------------------------------------------------
# Title: Print Even Numbers from 1 to 20 - For Loop
# Description:
#   This script prints all even numbers between 1 and 20
#   using a for loop in two different ways:
#     Option 1: Using range() with a step of 2.
#     Option 2: Iterating from 1 to 20 and checking if
#               the number is divisible by 2 (i % 2 == 0).
#   This demonstrates both range-based stepping and conditional filtering.
# Author: amirprg-ir
# ------------------------------------------------------------

# Option 1: Using range() with step 2.
for i in range(2,21,2):
    print(i)
# Option 2: Using a conditional (i % 2 == 0) inside loop.
for i in range(1,21):
    if i % 2 == 0:
        print(i)