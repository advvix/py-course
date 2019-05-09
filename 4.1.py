#1 Looking at the Euler method above create your own function which takes:
# a (from x' = ax)
# h - step
# T time range
# as an input and plots the solution of a differential equation x' = ax (1p)
#2 Beside the solution print the 'ideal' approximation on your chart using for example green color as a reference. (1p)
#2 Hint: use small step value. Use plt.legend to explain which serie is the 'ideal'

import numpy as np
import matplotlib.pyplot as plt

T = 5
h = 0.1
a = 1
initial_x = 1

t = np.arange(0,T,h)
x = np.zeros(t.shape)
x[0] = initial_x

for i in range(t.size-1):
    x[i+1] = x[i] + h * (1 * x[i])

plt.plot(t,x,'o',label="Gorsza")
plt.xlabel('t', fontsize=14)
plt.ylabel('x', fontsize=14)
h = 0.01

t = np.arange(0,T,h)
x = np.zeros(t.shape)
x[0] = initial_x

for i in range(t.size-1):
    x[i+1] = x[i] + h * (1 * x[i])

plt.plot(t,x,'g',label="Troche lepsza")
plt.legend()
plt.show()