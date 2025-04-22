# ------------------------------------------------------------
# Title: Access Items in a Nested List
# Description:
#   This script defines a 3x3 nested list (matrix) and accesses
#   the middle and the last elements using double indexing.
# Author: amirprg-ir
# ------------------------------------------------------------

matrix_3_3 = [
    [20,30,70],
    [30,50,95],
    [65,93,15]
]
middle_item_of_matrix_3_3 = matrix_3_3[1][1]
last_item_of_matrix_3_3 = matrix_3_3[2][2]
print(f"Original matrix: {matrix_3_3}")
print(f"Middle item of the matrix: {middle_item_of_matrix_3_3}")
print(f"Last item of the matrix: {last_item_of_matrix_3_3}")
