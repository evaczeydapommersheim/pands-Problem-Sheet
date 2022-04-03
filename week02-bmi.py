#Solution for Weekly Task - Week 02
#Author: Eva Czeyda-Pommersheim

weight = int(input("Enter weight (kg): "))
height = int(input("Enter height (cm): "))
bmi = round(float(weight / ((height / 100)**2)), 2)         

# bmi formula searched online, Uom is kg/m2, hence formula to convert the heaight from cm to m. Change type to float to allow for decimal results.
# using the round() function to ensure that the solution is displayed up to two decimals

print("The BMI is (kg/m2): {}.".format(bmi))