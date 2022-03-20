# program called plottask.py that displays a plot of 
# the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.

# Author: Eva Czeyda-Pommersheim

import numpy as np
import matplotlib.pyplot as plt

xpoints = np.array(range(0, 5))
fx = xpoints
gx = xpoints ** 2
hx = xpoints ** 3
plt.plot(xpoints, fx, 'o:b')
plt.plot(xpoints, gx, 'o:g')
plt.plot(xpoints, hx, 'o-r')

plt.title("Function of x")
plt.xlabel("Value of x")
plt.ylabel("Value of y")

plt.grid(color = 'black', linestyle = ':', linewidth = '0.4')

plt.show()