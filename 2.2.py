import cs50

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
            print(X,"jest podzielne przez ",Y," i obie sa parzyste")
            XY == True
    elif Y==0:
        print('Nie mozna dzielic przez 0')