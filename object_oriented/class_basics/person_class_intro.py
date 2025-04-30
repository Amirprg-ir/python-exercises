# ------------------------------------------------------------
# Title: Simple Person Class - Object Oriented Basics
# Description:
#   This script defines a basic 'Person' class with name and age
#   attributes, and includes a method to print a self-introduction
#   message. It demonstrates how to define a class and create an
#   object instance in Python.
# Author: amirprg-ir
# ------------------------------------------------------------

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

amir = Person("Amir", 19)
ali = Person("Ali", 20)

amir.introduce()
ali.introduce()
