import numpy as np
import cs50

#1 Write a function countField which calculates the field of a given figure. It takes the following input parameters:
# - type: circle/rectangle/triangle/rhombus
# - x & optional y.
# For circle we get only x which stands for radius. For Rectangle x&y are the figure's sides, for triangle they are
# accordingly the base and the height and for rhombus - diagonals (4p)
#2 Write a function which takes sets of parameters of two figures and compares their fields. (4p)
# The exemplary input is [[Circle, 4], [Rhombus, 2, 4]]
# Expected output would be 'The first figure (Circle) has larger field'
#3 Test your solutions

def countField(type, x, y=1):
    x=int(x)
    y=int(y)
    #circle
    if type =='circle':
        field = (x**2)*np.pi

    #rectangle
    if type =='rectangle':
        field = x*y

    #triangle
    if type =='triangle':
        field = (1/2)*x*y

    #rhombus
    if type =='rhombus':
        field = (x*y)/2
    return field

def compare(type1,type2,x1,x2,y1=1,y2=1):
    fig1 = countField(type1,x1,y1)
    fig2 = countField(type2,x2,y2)
    if fig1>fig2:
        answ = 'The first figure ('+type1+') has larger field'
    elif fig1==fig2:
        answ = "Both figures("+type1+","+type2+") have the same field"
    elif fig1<fig2:
        answ = "The second figure ("+type2+") has larger field"
    return print(answ)

dane = np.array([['circle', 4, 0], ['rhombus', 2, 4]])
dane[0,0] = input("XDDD")
#compare(dane[0,0],dane[1,0],dane[0,1],dane[1,1],dane[0,2],dane[1,2])
