from scipy import linspace ,sin, cos , exp, random, meshgrid, zeros,arccos,tanh
from scipy.optimize import fmin
from matplotlib.pyplot import plot, show, legend, figure, cm, contour, clabel
from mpl_toolkits.mplot3d import Axes3D
from termcolor import colored

def f(x):
    return exp(- x[0]**2 - x[1]**2) * sin(x[1]**2) + cos(x[0])

def neg_f(x):
    return -f(x)

minXY = [-1.5,-2] # punkt startowy
local_X_Y = minXY
local_fmin = fmin(neg_f,local_X_Y,disp=False)
minVAL = -1000

for i in range(500):
    lel = random.randn(2)
    xd = fmin(neg_f,lel,disp=False)
    if minVAL < f(xd):
        minXY = xd
        minVAL = f(minXY)

delta = 4.5
x_knots = linspace(minXY[0] - delta, minXY[0] + delta, 41)
y_knots = linspace(minXY[1] - delta, minXY[1] + delta, 41)
X, Y = meshgrid(x_knots, y_knots)
Z = zeros(X.shape)
for i in range(Z.shape[0]):
    for j in range(Z.shape[1]):
        Z[i][j] = f([X[i, j], Y[i, j]])

print(50*"#")
print(colored('Ekstremum lokalne: \n', 'green'),'Punkt: ',local_fmin,'\nWartosc: ',f(local_fmin),
      colored('\nEkstremum globalne: \n','red'),'Punkt: ',minXY,'\nWartosc: ',minVAL)
print(50*"#")

ax = Axes3D(figure(figsize=(8, 6)))
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0.8)
ax.plot([local_X_Y[0]], [local_X_Y[1]],[f(local_X_Y)], color='g', marker='o', markersize=10, label='punkt startowy')
ax.plot([local_fmin[0]], [local_fmin[1]], [f(local_fmin)], color='r', marker='o', markersize=15, label='lokalne')
ax.plot([minXY[0]], [minXY[1]], [f(minXY)], color='k', marker='o', markersize=10, label='globalne')
ax.legend()
show()


#5 Create your own 3d function with multiple local optima.
# Create an algorithm which takes an initial point and looks for the closest local optimum (1p)
# Create an algorithm which aims to find a global optimum, the time of execution is limiter to ~30sec (1p)
# If your solution is heuristic test its quality. Measure the probability of finding the GLOBAL optimum (1p).
# You can, for example, execute your search function multiple times and check if the returned result is what you expected.
# Measure the success / total trials rate (2p).