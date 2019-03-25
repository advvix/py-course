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
    #circle
    if type ==1:
        field = (x**2)*np.pi
        print("Wynik: ",x**2,"* π")

    #rectangle
    if type ==2:
        field = x*y

    #triangle
    if type ==3:
        field = (1/2)*x*y

    #rhombus
    if type ==4:
        field = (x*y)/2
    return print('Wynik: ',field)

start,x,y = [-1,-1,-1]

while start==-1:
    tp = cs50.get_int('Pole jakiej figury chcesz obliczyc?\n1: Kolo\n2: Prostokat\n3: Trojkat\n4: Romb\n')
    if tp==1:
        start = 1
        print("Pole kola")
        while x<0:
            x = cs50.get_int("Wprowadz promien: ")
        countField(tp,x)

    if tp==2:
        start = 1
        print("Pole prostokata")
        while x<0 or y<0:
            x = cs50.get_int("Wprowadz x: ")
            y = cs50.get_int("Wprowadz y: ")
        countField(tp,x,y)

    if tp==3:
        start = 1
        print("Pole trojkata")
        while x<0 or y<0:
            x = cs50.get_int("Wprowadz podstawe: ")
            y = cs50.get_int("Wprowadz wysokosc: ")
        countField(tp,x,y)

    if tp==4:
        start = 1
        print("Pole rombu")
        while x<0 or y<0:
            x = cs50.get_int("Wprowadz przekatna(d1): ")
            y = cs50.get_int("Wprowadz przekatna(d2): ")
        countField(tp,x,y)

