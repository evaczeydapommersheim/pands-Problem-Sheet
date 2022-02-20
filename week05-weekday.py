# This program outputs whether or not today is a weekday.

# Author: Eva Czeyda-Pommersheim

import datetime # Python has a module called datetime Source: W3 Schools, Python Dates Chapter

today = datetime.datetime.now()
print(today.strftime("%A"))     # Source: W3 Schools, Python Dates Chapter; this prints the date of the week based on today's date with a type str

days = {
    "weekday" : [
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday',
        ],
    "weekend" : [
        'Saturday',
        'Sunday'
    ]
   }

for day in days:
    if today == days.itemsweekday.value[:]
        print("Weekday")
    
print("Weekend")