# ------------------------------------------------------------
# Title: Countdown from Any Number to 1 - While Loop with Input Validation
# Description:
#   This script prompts the user to enter a positive number,
#   validates the input, and performs a countdown from that number
#   down to 1 using a while loop. After the countdown, it prints "Boom!".
#   Demonstrates loop control, input validation, and decrementing logic.
# Author: amirprg-ir
# ------------------------------------------------------------

input_number = int(input("Enter a number: "))
if input_number < 1:
    exit("invalid input")
while input_number >= 1:
    print(input_number)
    input_number -= 1
print("Boom! 💥")