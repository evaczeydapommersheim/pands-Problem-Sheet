# program called plottask.py that displays a plot of 
# the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.
# Source to support solution was W3Schools: https://www.w3schools.com/python/matplotlib_intro.asp

# Author: Eva Czeyda-Pommersheim

import numpy as np
import matplotlib.pyplot as plt

xpoints = np.array(range(0, 5)) #setting the range for the values of "x" (0, 5) in order to have [0, 4] displayed
fx = xpoints                    # defining the values for each function of x
gx = xpoints ** 2
hx = xpoints ** 3
plt.plot(xpoints, fx, 'o:b', label= 'x')    #plotting f(x) as a blue dotted line with circular markers, adding label to allow for legend to be displayed, 'o:b' for marker/line/colour selection
plt.plot(xpoints, gx, 'o:g', label = 'x2')  #plotting f(x2) as a green dotted line with circular markers, adding label to allow for legend to be displayed
plt.plot(xpoints, hx, 'o-r', label = 'x3')  #plotting f(x3) as a red continuous line with circular markers, adding label to allow for legend to be displayed

plt.title("Function of x", color = 'blue', size = 20)  #setting the titel and formatting of the chart name
plt.xlabel("Value of x", color = 'purple', size = 15)    # setting the name and formatting of the x-axis
plt.ylabel("Value of y", color = 'purple', size = 15)    # setting the name and formatting of the y axis

plt.grid(color = 'black', linestyle = ':', linewidth = '0.4') #adding gridlines to the chart
plt.legend() # creating the legend based on labels of the functions
plt.show()