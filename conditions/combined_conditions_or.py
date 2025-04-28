# ------------------------------------------------------------
# Title: Combined Conditions with OR Operator
# Description:
#   This script demonstrates combining two conditions using
#   the 'or' operator based on user's favorite subject.
# Author: amirprg-ir
# ------------------------------------------------------------

user_favorite_subject = input("What is your favorite subject? ")

if user_favorite_subject == "math" or user_favorite_subject == "physics":
    print("You are a science lover! 🔬")
else:
    print("That's fantastic! 🔎")
