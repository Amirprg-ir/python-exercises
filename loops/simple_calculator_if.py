# ------------------------------------------------------------
# Title: Simple Calculator with If-Elif-Else - While Loop
# Description:
#   This script implements a simple interactive calculator
#   using a while loop and if-elif-else conditions.
#   The user is presented with a menu to choose an operation:
#     [1] Addition
#     [2] Subtraction
#     [3] Multiplication
#     [4] Division
#     [q] Quit
#   After selecting an operation, the user is asked to input
#   two numbers, and the result is calculated and displayed.
#   The program continues to show the menu until the user
#   chooses to quit by entering 'q'.
# Author: amirprg-ir
# ------------------------------------------------------------

menu_text = """
============================
     Simple Calculator
============================
[1] Add
[2] Subtract
[3] Multiply
[4] Divide
[q] Quit

Please enter your choice: 
"""

correct_operation = ["1", "2", "3", "4"]
operation = input(menu_text)

while operation != "q":
    if operation in correct_operation:
        number1 = float(input("Enter the first number: "))
        number2 = float(input("Enter the second number: "))

        if operation == "1":
            result = number1 + number2
            print(f"The sum of {number1} and {number2} is => {result}")
        elif operation == "2":
            result = number1 - number2
            print(f"The difference of {number1} and {number2} is => {result}")
        elif operation == "3":
            result = number1 * number2
            print(f"The product of {number1} and {number2} is => {result}")
        elif operation == "4":
            if number2 != 0:
                result = number1 / number2
                print(f"The quotient of {number1} and {number2} is => {result:.2f}")
            else:
                print("Error! Cannot divide by zero.")
    else:
        print("Invalid input. Please try again.")

    input("Press Enter to return to menu...")  # Pause
    operation = input(menu_text)

print("👋 Quit the program. Have a nice day!")
