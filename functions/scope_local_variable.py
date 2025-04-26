# ------------------------------------------------------------
# Title: Local Variable Scope Example
# Description:
#   This script demonstrates how a variable defined inside a
#   function is only accessible within that function (local scope).
# Author: amirprg-ir
# ------------------------------------------------------------

def show_message():
    message = "Hello from inside the function!"
    print(message)

# Calling the function
show_message()

# Trying to access the local variable outside the function
print(message)  # ⛔ Error: NameError: name 'message' is not defined
