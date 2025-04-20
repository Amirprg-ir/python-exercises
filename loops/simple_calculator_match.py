# ------------------------------------------------------------
# Title: Simple Calculator with Match-Case - While Loop
# Description:
#   This script implements a simple interactive calculator using Python's
#   match-case (introduced in version 3.10). The user selects operations
#   from a menu, inputs two numbers, and receives the result. The menu
#   loops until the user chooses to quit.
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

Please enter your choice: """

input_operation = input(menu_text)

while input_operation != "q":
    match input_operation:
        case "1":
            number1 = float(input("Enter first number: "))
            number2 = float(input("Enter second number: "))
            result = number1 + number2
            print(f"The sum of {number1} and {number2} is => {result}")
        case "2":
            number1 = float(input("Enter first number: "))
            number2 = float(input("Enter second number: "))
            result = number1 - number2
            print(f"The difference of {number1} and {number2} is => {result}")
        case "3":
            number1 = float(input("Enter first number: "))
            number2 = float(input("Enter second number: "))
            result = number1 * number2
            print(f"The product of {number1} and {number2} is => {result}")
        case "4":
            number1 = float(input("Enter first number: "))
            number2 = float(input("Enter second number: "))
            if number2 != 0:
                result = number1 / number2
                print(f"The quotient of {number1} and {number2} is => {result}")
            else:
                print("Error! Cannot divide by zero.")
        case _:
            print("Invalid input.")

    input("Press Enter to return to menu...")
    input_operation = input(menu_text)

exit("👋 Exiting the program. Have a nice day!")
