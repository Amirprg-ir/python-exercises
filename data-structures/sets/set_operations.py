# ------------------------------------------------------------
# Title: Set Operations - Union, Intersection, Difference
# Description:
#   This script demonstrates basic set operations including
#   union, intersection, and difference between two sets.
# Author: amirprg-ir
# ------------------------------------------------------------

first_set = {"php", "python", "java", "c#", "c++", "golang"}
second_set = {"python", "perl", "java", "c#", "javascript", "golang"}

print(f"First set: {first_set}")
print(f"Second set: {second_set}")

union_set = first_set.union(second_set)
print(f"Union of first and second sets: {union_set}")

intersection_1_2 = first_set.intersection(second_set)
print(f"Intersection (first ∩ second): {intersection_1_2}")

intersection_2_1 = second_set.intersection(first_set)
print(f"Intersection (second ∩ first): {intersection_2_1}")

difference_1_2 = first_set.difference(second_set)
print(f"Difference (first - second): {difference_1_2}")

difference_2_1 = second_set.difference(first_set)
print(f"Difference (second - first): {difference_2_1}")
