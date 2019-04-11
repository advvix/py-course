import numpy as np
#enum struktura
#2 Write a function which takes sets of parameters of two figures and compares their fields. (4p)
# The exemplary input is [[Circle, 4], [Rhombus, 2, 4]]
# Expected output would be 'The first figure (Circle) has larger field'
dane = [['trojkat',2,4],['kolo',4,2]]
win = True
def countField(zestaw):
    field = None
    if zestaw[0] == 'kolo': #circle
        field = (zestaw[1]**2)*np.pi
    if zestaw[0] == 'prostkat': #rectangle
        field = zestaw[1]*zestaw[2]
    if zestaw[0] == 'trojkat' or zestaw[0] =='romb': #triangle or rhombus
        field = (1/2)*zestaw[1]*zestaw[2]
    return field

def compare(zestaw1,zestaw2):
    fig1 = countField(zestaw1)
    fig2 = countField(zestaw2)
    answ = None
    if fig1 > fig2:
        answ = 'The first figure ('+zestaw1[0]+') has larger field'
    elif fig1 == fig2:
        answ = "Both figures("+zestaw1[0]+","+zestaw2[0]+") have the same field"
    elif fig1 < fig2:
        answ = "The second figure ("+zestaw2[0]+") has larger field"
    return print(answ)

try:
    for i in [0,1]:
        if len(dane[i]) == 0:
            print('Wykryto pusta liste')
        if dane[i][0] != 'kolo' and dane[i][0] != 'romb' and dane[i][0] != 'trojkat' and dane[i][0] != 'prostokat':
            print('Wprowadzono zla nazwe figury lub zla kolejnosc wpisywania w zestawie',i+1)
        for k in range(1,len(dane[i])):
            if type(dane[i][k]) != int or type(dane[i][k]) != int:
                print("Wymiary sa zle podane w zestawie",i+1)
        if len(dane[i])<2:
            print("Brak wymiarow w zestawie",i+1)
        if (dane[i][0] == 'romb' or dane[i][0] == 'trojkat' or dane[i][0] == 'prostokat') and len(dane[i])==2:
            print(dane[i][0],"potrzebuje 2 wymiarow.")
        if dane[i][0] == 'kolo' and len(dane[i])==3:
            print(dane[i][0],"nie potrzebuje 2 wymiarow.")
    else:
        compare(dane[0],dane[1])
except:
    if not dane:
        print("Wykryto pusta liste")
    if len(dane) == 1:
        print('Wpisano tylko jeden zestaw')