"""

Author: Disha Gupta
Date: February 3, 2016
Section: #05
Program: Assignment 1 - Problem #1: Variables & Print Statements 
Purpose: Using print statements and variables to display the given output.

"""

# store name of class in a variable
classname = "Introduction to Computer Programming"

# assign data to variables (in this case, test scores for the class)
test1 = "95"
test2 = "76"
test3 = "87"

# print out test scores for the class
print("""Average Test Scores For """, end="")
print('"', classname, '"', ":", sep="")
print("- Test #1: ", test1)
print("- Test #2: ", test2)
print("- Test #3: ", test3)
