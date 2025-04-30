# ------------------------------------------------------------
# Title: Student Class - Pass/Fail Checker
# Description:
#   This script defines a 'Student' class with name and grade
#   attributes, and includes a method to check if the student
#   has passed based on a grade threshold. It demonstrates how
#   to store multiple objects in a list and iterate through them.
# Author: amirprg-ir
# ------------------------------------------------------------

class Student:
    def __init__(self, name, grade):
        grade = float(grade)
        if grade > 20 or grade < 0:
            exit("invalid grade. exit program")
        self.name = name
        self.grade = grade

    def has_passed(self):
        if self.grade > 10:
            print(f"{self.name} is passed")
        else:
            print(f"{self.name} is not passed")

students = [
    Student("Amir", 20),
    Student("Ali", 15),
    Student("Hasan", 10),
]

for student in students:
    student.has_passed()
