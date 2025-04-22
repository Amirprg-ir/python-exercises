# ------------------------------------------------------------
# Title: Loop Through Nested List
# Description:
#   This script defines a 3x3 nested list (matrix) and prints
#   all elements using nested loops along with their positions.
# Author: amirprg-ir
# ------------------------------------------------------------

matrix_3_3 = [
    [75, 20, 85],
    [65, 93, 89],
    [65, 45, 87]
]

rows = 0
cols = 0

for row in matrix_3_3:
    for col in row:
        print(f"matrix[{rows}][{cols}] = {col}")
        cols += 1
    rows += 1
    cols = 0
