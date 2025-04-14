# ------------------------------------------------------------
# Title: Price Calculator - Multiplying Variables
# Description:
#   This script asks the user for the quantity of a product
#   and its unit price, then calculates and displays the
#   total cost using integer variables and basic arithmetic.
# Author: amirprg-ir
# ------------------------------------------------------------

product_unit_price = float(input("Enter product unit price in Dollars: "))
product_quantity = int(input("Enter product quantity: "))
final_price = product_unit_price * product_quantity
output = f"Your bought {product_quantity} items at {product_unit_price:,.2f} dollars. total cost: {final_price:,.2f} dollars."
print(output)