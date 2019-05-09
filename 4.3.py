#3 Find a differential equation which represents a process / model (your choice)
# and implement it using odeint python function (1p)


import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def F(x, t):
    dx = [0, 0]
    dx[0] = x[1]  #
    dx[1] = -x[0] # schemat Eulera
    return dx

t_min = 0
t_max = 20
h = 0.01
t = np.arange(t_min, t_max+h, h)

initial_x = ((1,1))

X = odeint(F, initial_x, t)
plt.figure(1)
plt.plot(t,X)
plt.figure(2)
plt.plot(X[:,0],X[:,1])
plt.axis('equal')
plt.show()