import cs50
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#0 Use alternative way of reading inputs - using library (0.5p)
x=-1
y=-1
while x<0 or y<0:
    x = cs50.get_int("x: ")
    y = cs50.get_int("y: ")

#1 Perimeter & field of circles with given radius X for the first circle & Y for the second one. (1p)
first_circleP = 2*np.pi*x
first_circleF = np.pi*(x**2)
second_circleP = 2*np.pi*y
second_circleF =np.pi*(y**2)
print("Obwód koła x: ",first_circleP,"\nPole koła x: ",first_circleF,"\nObwód koła y: ",second_circleP,"\nPole koła y: ",second_circleF)

#2 Find X & Y that satisfy: X is divisible by Y and both X & Y are even. (0.5p)

XY = False

while XY == False:
    X = cs50.get_int("X: ")
    Y = cs50.get_int("Y: ")
    if Y!=0:
        xIsEven = X % 2 == 0
        yIsEven = Y % 2 == 0
        if xIsEven and yIsEven:
            XY = X % Y == 0
            print("Jest podzielna i obie sa parzyste")
    elif Y==0:
        print('Nie mozesz wprowadzic 0')

#3 Check if X is divisible by Y (do it in one line of code), print 'X is divisible by Y' or 'X is not divisible by Y'. (1p)
#Ad 3 Hint- use the "ternary operator" as we did calculating xIsEvenLog above.
X = cs50.get_int("X: ")
Y = cs50.get_int("Y: ")

XYLog = 'X is divisible by Y' if X % Y else 'X is not divisible by Y'


#4 Add rounding for the above x/y operation. Round to 2 decimal points. Hint: look up in Google "python limiting number of decimals". (1p)
X = cs50.get_int("X: ")
Y = cs50.get_int("Y: ")

divisibility = X/Y
print(round(divisibility,2)) # średnio działa
print( "%.2f" % divisibility)  # działa

#testowanko
print(round(divisibility,244)) #jak pojawia sie (...0) to koniec
print("%.244f" % divisibility) #znowu dziala


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
