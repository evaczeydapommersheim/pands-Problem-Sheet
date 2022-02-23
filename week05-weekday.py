# This program outputs whether or not today is a weekday.

# Author: Eva Czeyda-Pommersheim

from ast import Break
from calendar import weekday
import datetime # Python has a module called datetime Source: W3 Schools, Python Dates Chapter

today = (datetime.datetime.now()).strftime("%A")    # Source: W3 Schools, Python Dates Chapter; this prints the date of the week based on today's date with a type str

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

if True:
    today == any(weekdays[:])  
            # Using the any() Python built-in function (Source RealPython newsletter https://realpython.com/courses/python-any-boolean-function/?__s=vn9uk2a450mzn2xle474) 
        # to iterate through the list of weekdays Mon-Friday. If this condition becomes false, today variable can only be one of the weekend days.
        # additional reading on W3 School https://www.w3schools.com/python/ref_func_any.asp)
    print("Yes, unfortunately today is a weekday.")
else:
    print("It is the weekend, yay!") 