# ------------------------------------------------------------
# Title: Balance Update - Variable Manipulation Practice
# Description:
#   This script simulates a simple account balance update.
#   It asks the user for an initial balance, a deposit amount,
#   and a withdrawal amount, then calculates and displays
#   the final balance using formatted float output.
# Author: amirprg-ir
# ------------------------------------------------------------

balance = float(input("Enter the balance: "))
deposit = float(input("Enter the deposit: "))
withdrawal = float(input("Enter the withdrawal: "))
final_balance = (balance + deposit ) - withdrawal
output = f"initial balance: {balance:,.2f} dollars \ndeposit: {deposit:,.2f} dollars \nwithdrawal: {withdrawal:,.2f} dollars \nfinal balance: {final_balance:,.2f} dollars"
print(output)