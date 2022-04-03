# This program asks the user to input any positive integer 
# it outputs the successive values using the following calculation:
# at each step it calculates the next value by taking the current value 
# if it is even, divide it by two, 
# if it is odd, multiply it by three and add one.

# The program ends if the current value is one.

# Author: Eva Czeyda-Pommersheim

def collatz(number, step=0):        # defining a function with 2 arguments: the number and the iteration for the while loop
    
    while number != 1:
        print(number)               # printing the number that is entered outside the function
        step += 1                   # iterating through the loop until number becomes = 1
        if number % 2 == 0:     # number is even
            number = int(number // 2)
       
        else:
            number = int(3*number + 1)  # number is odd
    print(int(number))

try:
    number = abs(int(input("Please enter a positiv integer: "))) # using absolute value in case a negative number is entered         
    collatz(number)
except ValueError:              # exception in case a float or string is entered
    raise ValueError("a positive integer is required")
