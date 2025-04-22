# ------------------------------------------------------------
# Title: Insert Item If Not Exists in List
# Description:
#   This script creates a list of programming languages,
#   checks whether 'python' is present, and if not, inserts
#   it at index 1 using insert(). Finally, it prints the list.
# Author: amirprg-ir
# ------------------------------------------------------------

programming_languages = ["c#", "c++", "java", "ruby", "golang", "php", "perl"]

print(f"Original list: {programming_languages}")

flag = "python" in programming_languages
if not flag:
    programming_languages.insert(1, "python")

print(f"Updated list: {programming_languages}")
