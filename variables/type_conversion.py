# ------------------------------------------------------------
# Title: BMI Calculator - Type Conversion Practice
# Description:
#   This script asks the user to input their weight (kg)
#   and height (meters), calculates their BMI using the
#   formula: BMI = weight / (height ** 2), and prints the result.
#   It demonstrates how to convert user input into float
#   and perform arithmetic operations.
# Author: amirprg-ir
# ------------------------------------------------------------

user_height = float(input("Please enter your height in meters: "))
user_weight = float(input("Please enter your weight in kilograms: "))
BMI = user_weight / (user_height **2)
output = f"your BMI is: {BMI:.2f}"
print(output)