# This program is to include a funtion which will read in a positive floating number as an input
# and outputs an approximation of its suqare root.

# Author: Eva CZ-P

number = float(input('Please enter a positive number: '))      # allowing for a float number to be entered, otherwise it would be considered as a type: string.

def sqrt(n, l = 0.00001):      #n is the number the square root of which we are trying to find out, "l" is the tolerance for error, as to how many decimal places the square root should be shown 0.01
    n = number
    x = n   # assuming that square root of n is n (like square root of 1 is 1)
    iter = 0
    while(1):       
    # based on Newton's method the root of a number = 0.5*(x+(n/x)), where x can be assumed to be anywhere between n or 1. 
    # Iteration starting from 1 and step increasing by +1 in the while loop.
        iter += 1
        root = 0.5 * (x + (n / x))
        if (abs(root - x)) < 0.01:
        # in order to get a close enough result in the approximate square root value, add "if"  for the difference between assumed value and calculated root to be less than 0.01, as close to zero as possible
        # using the abs function to get the difference as opposed to negative number.
            break
        # the loop is to finish once the difference between the assumed value of x is close enough to the value calculated for root.
        x = root
        # at the end of each while loop the value of root calculation is given to x in order to continue the loop.
    
    return(root)
    # return value of the function when called

print("The square root of ", number, "is approximately", round(sqrt(number),1)) # command to print out the square root of the number rounded to one decimal place.
