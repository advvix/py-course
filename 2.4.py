import cs50
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#4 Add rounding for the above x/y operation. Round to 2 decimal points. Hint: look up in Google "python limiting number of decimals". (1p)
X = cs50.get_int("X: ")
Y = cs50.get_int("Y: ")

divisibility = X/Y
print(round(divisibility,2)) # średnio działa
print( "%.2f" % divisibility)  # działa

#testowanko
print(round(divisibility,244)) #jak pojawia sie (...0) to koniec
print("%.244f" % divisibility) #znowu dziala