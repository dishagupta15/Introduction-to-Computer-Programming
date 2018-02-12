"""

Author: Disha Gupta
Date: February 3, 2016
Section: #05
Program: Assignment 1 - Problem #3: Math Expressions
Purpose: Calculating the speed of light in different units; calculating earths rotation in different units; displayng all calculation answers.

"""

# store the value for speed of light in a vacuum 
speed_of_light_kps = 299792.458

# calculate speed of light in mps, half speed of light, and quarter speed of light then store the values
speed_of_light_mps = speed_of_light_kps*0.621
half_speed_of_light = speed_of_light_mps/2
quarter_speed_of_light = speed_of_light_mps/4

# print out the values of speed of light in different units etc.
print("Speed of light (Kilometers / sec):    ", speed_of_light_kps, "kps")
print("Speed of light (Miles / sec):         ", speed_of_light_mps , "mps")
print("Half speed of light (Miles / sec):    ", half_speed_of_light, "mps")
print("Quarter speed of light (Miles / sec): ", quarter_speed_of_light, "mps")

# store the value for earth's rotation around the sun
earths_rotation = 66600

# calculate earths rotation in kps and its percentage of speed of light
earths_rotation_kps = earths_rotation*0.00044704
earths_percent_speed_of_light = earths_rotation_kps/speed_of_light_kps *100

print()

# print out earths rotation information
print("The earth moves 66,600 miles / hour around the sun")
print("66,600 miles per hour is equal to:    ", earths_rotation_kps, "kps")
print("66,600 miles per hour is equal to:    ", earths_percent_speed_of_light, "% of the speed of light")
