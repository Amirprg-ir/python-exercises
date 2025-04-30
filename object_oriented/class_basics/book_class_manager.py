# ------------------------------------------------------------
# Title: Book Class - Basic Library Book Manager
# Description:
#   This script defines a 'Book' class with title, author, and
#   publication year attributes. It includes methods to print
#   book details and check if the book is older than 10 years.
#   Demonstrates basic class structure and behavior in Python.
# Author: amirprg-ir
# ------------------------------------------------------------

import datetime

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_info(self):
        print(f"Title: {self.title}, Author: {self.author}, Year: {self.year}")

    def is_old(self):
        current_year = datetime.date.today().year
        if current_year - self.year > 10:
            print("This book is old.")
        else:
            print("This book is new.")

book1 = Book("Python Programming", "Guido van Rossum", 1999)
book2 = Book("Math is Good", "Alan Turing", 2020)

book1.get_info()
book1.is_old()

book2.get_info()
book2.is_old()
