"""

Author: Disha Gupta
Date: February 10, 2016
Section: #05
Program: Assignment 2 - Problem #1: Dynamic Tip Calculator
Purpose: Calculating the total amount of a bill for a user based on the amount of tip they want to leave and how many individuals are splitting the bill.

"""
# Ask user for bill amount, how much they want to tip, and how many people are paying.
print("Hello! I'm here to help you calculate your tip.")
bill = float(input("How much was your bill? (Enter a numeric value without commas or dollar signs): "))
tip = float(input("How much tip would you like to leave? (Enter an integer value): "))
people = float(input("How many individuals are splitting the bill? (Enter an integer value): "))

print()

print("Thanks! Calculating your bill & tip ...")

print()

# Change tip to a percentage.
tip_percentage = tip / 100

# Calculate tip amount, the total cost of the meal with the tip, and how much each person needs to pay.
tip_amount = bill * tip_percentage
total_bill = tip_amount + bill
individual_amount = total_bill / people

# Format the variable tip_amount, total_bill, and individual_amount so that it only displays two decimal points.
f_tip_amount = format (tip_amount, '.2f')
f_total_bill = format (total_bill, '.2f')
f_individual_amount = format (individual_amount, '.2f')

# Display the tip amount, total bill cost, and the amount each individual needs to pay.
print("You need to leave $", f_tip_amount, " as a tip.", sep="")
print("Your total bill will be $", f_total_bill, ".", sep="")
print("Each individual should pay $", f_individual_amount, ".", sep="")
