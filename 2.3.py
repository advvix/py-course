import cs50

#3 Check if X is divisible by Y (do it in one line of code), print 'X is divisible by Y' or 'X is not divisible by Y'. (1p)
#Ad 3 Hint- use the "ternary operator" as we did calculating xIsEvenLog above.
s=True
X = cs50.get_float("X: ")
Y = cs50.get_float("Y: ")
while s == True:
    if Y == 0:
        Y = cs50.get_float("Nie mozna dzielic przez 0\nWprowadz Y: ")
    elif Y > 0:
        s = False

print('X is divisible by Y' if X % Y == 0 else 'X is not divisible by Y')