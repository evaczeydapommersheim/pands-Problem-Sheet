#Solution for Weekly Task - Week 02
#Author: Eva Czeyda-Pommersheim

weight = int(input("Please enter your weight (kg): "))
height = int(input("Please enter your height (cm): "))
bmi = float(weight / ((height / 100)**2))
print("Your BMI is: {}".format(bmi))