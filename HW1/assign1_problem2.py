"""

Author: Disha Gupta
Date: February 3, 2016
Section: #05
Program: Assignment 1 - Problem #2: Using the Print Function
Purpose: Use the input and print functions to collect three names and display them in every possible order.

"""

# ask user for three different names
name1 = input("Please enter a name: ")
name2 = input("Please enter another name: ")
name3 = input("Please enter one more name: ")

print("")
print("Here are your names in every possible order: ")
print("--------------------------------------------")
print("")

# print out names in all possible orders
print("1.", name1, name2, name3)
print("")
print("2.", name1, name3, name2)
print("")
print("3.", name3, name1, name2)
print("")
print("4.", name2, "\n", name3, "\n", name1)
print("")
print("5.", name3, "\n", name2, "\n", name1)
print("")
print("6.", name3, "\n", name1, "\n", name2)
