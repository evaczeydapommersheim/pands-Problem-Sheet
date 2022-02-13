# This program asks the user to input any positive integer 
# it outputs the successive values using the following calculation:
# at each step it calculates the next value by taking the current value 
# if it is even, divide it by two, 
# if it is odd, multiply it by three and add one.

# The program ends if the current value is one.

# Author: Eva Czeyda-Pommersheim

num = int(input('Please enter a positiv integer: '))
print(num)              # prints out the starting number
while num != 1:
    if num % 2 == 0:    # if the number is even there will be no remainder if devided by 2.
        num = num / 2
        print(int(num))
    else:
        num = (num * 3) + 1
        print(int(num))             #  if the number is not even, the if condition is False it can only be odd
       
