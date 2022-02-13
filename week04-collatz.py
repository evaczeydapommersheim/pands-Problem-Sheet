# This program asks the user to input any positive integer 
# it outputs the successive values using the following calculation:
# at each step it calculates the next value by taking the current value 
# if it is even, divide it by two, 
# if it is odd, multiply it by three and add one.

# The program ends if the current value is one.

# Author: Eva Czeyda-Pommersheim

num = int(input('Please enter a positiv integer: '))

print(num)              # prints out the starting number
while num != 1:         # WHILE LOOP WILL CONTINUE UNTIL THE OUTCOME IS EQUAL TO 1.
    if num <= 0:        # The program prompts to only enter numbers greater than zero.
        print('Please enter a number greater than 0.')
        num = int(input('Please enter a positiv integer: '))
    elif num % 2 == 0:    # NUMBERS DIVIDED BY 2 WITH NO REMAINDER ARE EVEN NUMBERS
        num = num / 2
        print(int(num))     # Print the result, while loop will continue to do the calculation.
    else:
        num = (num * 3) + 1     #  if the number is not even, the if condition is False AND PROGRAM WILL EXECUTE THE ELSE CONDITION
        print(int(num))      # Print the result, while loop will continue to do the calculation.       
       
