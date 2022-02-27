# This program outputs whether or not today is a weekday.

# Author: Eva Czeyda-Pommersheim

import datetime # Python has a module called datetime Source: W3 Schools, Python Dates Chapter

today = (datetime.datetime.now()).strftime("%A")    # Source: W3 Schools, Python Dates Chapter; this prints the date of the week based on today's date with a type str

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'] #listing the days during the week
weekendDays = ['Saturday', 'Sunday'] #created additional variable to list the days of the weekend also

if today in weekdays:   #using the if/else function to print out the different outcomes.
    today == any(weekdays[:])  
        # Using the any() Python built-in function (Source RealPython newsletter https://realpython.com/courses/python-any-boolean-function/?__s=vn9uk2a450mzn2xle474) 
        # to iterate through the list of weekdays Mon-Friday. If this condition becomes false, today variable can only be one of the weekend days.
        # additional reading on W3 School https://www.w3schools.com/python/ref_func_any.asp)
    print("Yes, unfortunately today is a weekday.")
else:
    today == any(weekendDays[:])
    print("It is the weekend, yay!") 