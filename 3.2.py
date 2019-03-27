import numpy as np
import cs50
#2 Write a function which takes sets of parameters of two figures and compares their fields. (4p)
# The exemplary input is [[Circle, 4], [Rhombus, 2, 4]]
# Expected output would be 'The first figure (Circle) has larger field'
#3 Test your solutions

def countField(type, x, y=None):
    global field
    x=int(x)
    y=int(y)
    #circle
    if type =='kolo':
        field = (x**2)*np.pi
    #rectangle
    if type =='prostkat':
        field = x*y
    #triangle or rhombus
    if type =='trojkat' or type =='romb':
        field = (1/2)*x*y
    return field

def compare(type1,type2,x1,x2,y1=1,y2=1):
    fig1 = countField(type1,x1,y1)
    fig2 = countField(type2,x2,y2)
    global answ
    if fig1>fig2:
        answ = 'The first figure ('+type1+') has larger field'
    elif fig1==fig2:
        answ = "Both figures("+type1+","+type2+") have the same field"
    elif fig1<fig2:
        answ = "The second figure ("+type2+") has larger field"
    return print(answ)

s,type,y=[True,None,0]
dane = []
while s==True:
    type = input("Jaka figura? : ")
    if type=='kolo' or type=='prostokat' or type=='trojkat' or type=='romb':
        x = cs50.get_float("Wprowadz X")
        if type != 'kolo':
            y = cs50.get_float("Wprowadz Y")
        if x>=0 and y>=0:
            dane.append([type,x,y])
            if len(dane) == 2:
                compare(dane[0][0],dane[1][0],dane[0][1],dane[1][1],dane[0][2],dane[1][2])
                s=False
        else:
            print("Zle dane")

    if type!='kolo' and type!='prostokat' and type!='trojkat' and type!='romb':
        print('Wprowadzono zla figure')