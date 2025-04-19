# ------------------------------------------------------------
# Title: Average Grade Calculator - While Loop
# Description:
#   This script prompts the user to enter grades between 0 and 20.
#   It validates the input and continues to collect scores until
#   a negative number is entered. Then it calculates and displays
#   the average of all valid scores entered.
# Author: amirprg-ir
# ------------------------------------------------------------

input_score = float(input("Enter the score: "))
if input_score >= 21 or input_score < 0:
    exit("invalid score")
score_count = 0
score_sum = 0
while input_score >= 0 and input_score <= 20:
    score_sum += input_score
    score_count += 1
    input_score = float(input("Enter the next score: "))

print(f"the average of {score_count} scores is: {score_sum/score_count:.2f}")