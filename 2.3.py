import cs50
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#3 Check if X is divisible by Y (do it in one line of code), print 'X is divisible by Y' or 'X is not divisible by Y'. (1p)
#Ad 3 Hint- use the "ternary operator" as we did calculating xIsEvenLog above.
X = cs50.get_int("X: ")
Y = cs50.get_int("Y: ")

XYLog = 'X is divisible by Y' if X % Y else 'X is not divisible by Y'

