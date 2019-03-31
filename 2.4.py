import cs50

#4 Add rounding for the above x/y operation. Round to 2 decimal points. Hint: look up in Google "python limiting number of decimals". (1p)
s=True
while s==True:
    X = cs50.get_int("X: ")
    Y = cs50.get_int("Y: ")

    if Y==0:
        print("Nie mozna dzielic przez 0")
        Y = cs50.get_int("Y: ")

    divisibility = X/Y
    if X == 0 and Y < 0:
        divisibility = abs(divisibility)

    print(round(divisibility,2)) # średnio działa (jak jest .0 to konczy)
    print( "%.2f" % divisibility)  # działa
    s=False