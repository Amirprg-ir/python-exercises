# ------------------------------------------------------------
# Title: Modify Global Variable Inside Function
# Description:
#   This script demonstrates how to modify a global variable
#   inside a function using the global keyword.
# Author: amirprg-ir
# ------------------------------------------------------------

counter = 0

def increment():
    global counter
    print(f"The counter before incrementing is: {counter}")
    counter += 1
    print(f"The counter after incrementing is: {counter}")

increment()

print(f"The counter after calling increment(): {counter}")
