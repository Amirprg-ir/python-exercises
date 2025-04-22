# ------------------------------------------------------------
# Title: Nested Multiplication Table (10x10)
# Description:
#   This script generates a 10x10 multiplication table using
#   nested lists and nested loops, then prints each row.
# Author: amirprg-ir
# ------------------------------------------------------------

multiplication_table = []

for i in range(1, 11):
    row = []
    for j in range(1, 11):
        row.append(i * j)
    multiplication_table.append(row)
    print(row)

# Optional: print full table at once
print("\nFull multiplication table:")
for row in multiplication_table:
    print(row)
