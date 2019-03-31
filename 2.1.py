import cs50
import numpy as np

#0 Use alternative way of reading inputs - using library (0.5p)
s=True
x = cs50.get_float("x: ")
y = cs50.get_float("y: ")

while s==True:
    if x == 0 or x < 0:
        x = cs50.get_float("x: ")
    elif y == 0 or y < 0:
        y = cs50.get_float("y: ")
    else:
        s = False

#1 Perimeter & field of circles with given radius X for the first circle & Y for the second one. (1p)
first_circleP = 2*np.pi*x
first_circleF = np.pi*(x**2)
second_circleP = 2*np.pi*y
second_circleF =np.pi*(y**2)
print("Obwód koła x: ",first_circleP,"\nPole koła x: ",first_circleF,"\nObwód koła y: ",second_circleP,"\nPole koła y: ",second_circleF)