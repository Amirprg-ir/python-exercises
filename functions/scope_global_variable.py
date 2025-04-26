# ------------------------------------------------------------
# Title: Global Variable Scope Example
# Description:
#   This script demonstrates how a global variable can be
#   accessed inside a function without modifying it.
# Author: amirprg-ir
# ------------------------------------------------------------

count = 0

def show_count():
    print(f"The count inside the function is: {count}")

show_count()

print(f"The count outside the function is: {count}")
