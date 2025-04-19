# ------------------------------------------------------------
# Title: Full Multiplication Table (1 to 10) - Nested Loop
# Description:
#   This script prints the complete multiplication table from 1 to 10
#   using nested for loops. Each iteration of the outer loop represents
#   a base number, and the inner loop generates its multiples from 1 to 10.
#   A separator line is added for better readability between tables.
# Author: amirprg-ir
# ------------------------------------------------------------

for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} * {j} = {i * j}")
    print("-----------------------------------------------------------")