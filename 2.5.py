import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#5 Look at lab2-plot.py and create your own script which takes a number as an input and plots the same 3D wave but with different characteristics
# it's totally up to your imagination how do you want to amend the figure according to the input number (1p)

number = float(input("Number: "))
x_knots = np.linspace(-number*np.pi,number*np.e,201)
y_knots = np.linspace(number**np.pi,np.e**2+number*np.pi,201)
X, Y = np.meshgrid(x_knots, y_knots)
R = np.sqrt(X**2)
Z = np.cos(R**2)-np.e*R
ax = Axes3D(plt.figure(figsize=(6,5)))
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.cm.prism, linewidth=0.2)
plt.show()


#6 Test your code. Check various edge cases. In other words: does your program (1, 3, 4 & 5)work for all input values?
# In case of task 4  do not forget to round to different amount of decimals and see if it still works.(3p)
