# This program outputs whether or not today is a weekday.
# THIS IS AN UPDATE TO MY ORIGINAL SUBMISSION BASED ON FEEDBACK RECEIVED ON 08-MAR-2022

# Author: Eva Czeyda-Pommersheim

print("\nAlternative Solution 1")
import datetime
# Python has a module called datetime Source: W3 Schools, Python Dates Chapter

today = (datetime.datetime.now()).strftime("%A")    # Source: W3 Schools, Python Dates Chapter; this prints the date of the week based on today's date with a type str

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'] #listing the days during the week
weekendDays = ['Saturday', 'Sunday'] #created additional variable to list the days of the weekend also

if today in weekdays:      # REMOVED THE ANY FUNCTION AS THE IF/ELSE PROVES TO BE SUFFICIENT TO GIVE THE SAME OUTCOME
    print("Yes, unfortunately today is a weekday.")
    
else:
    print("It is the weekend, yay!") 

print("\nAlternative Solution 2")
# This program is to provide a second solution to weekly task - WEEK05
import datetime

today = int(datetime.datetime.now().strftime("%w"))     
# Source is 3W schools Python Dates chapter, using format code %w to output Weekday as a number 0-6, 0 is Sunday. 
# (https://www.w3schools.com/python/python_datetime.asp)
if today >=1 and today <=5: 
    print("Yes, unfortunately today is a weekday.")
    #Setting if criteria for today to be between 1 and 5 (inclusive) 1 being Monday and 5 being Friday
else:
    print("It is the weekend, yay!")   
    # the only options left is 0 for Sunday and 6 for Saturday which are days of the weekend.



