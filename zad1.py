import numpy as np
from matplotlib.pyplot import *


#1 calculate & print the value of function y = 2x^2 + 2x + 2 for x=[56, 57, ... 100] (0.5p)
for i in range (56,101):
    y = 2*(i**2)+(2*i)+2
    print(y)

#2 ask the user for a number and print its factorial (1p)
def factorial(x):
    i=x-1
    while i>0:
        x=x*i
        i=i-1
    return x

x=int(input("-"*20+"\nObliczanie silni\nWprowadz liczbe: "))
print("Silnia: ",factorial(x))

#3 write a function which takes an array of numbers as an input and finds the lowest value. Return the index of that element and its value (1p)
list = [5,6,12,46,120,2,37,126,298,8383,13,14]
#list = []
#list = np.random.randint(1,280,12)

k=2
if list[0]>list[1]:
    minl = list[1]
else:
    minl=list[0]

for j in range(10):
    if minl>list[k]:
        minl=list[k]
    k+=1
print(list,"\nLowest value: ",minl)

#4 looking at lab1-input and lab1-plot files create your own python script that takes a number and returns any chart of a given length.
#the length of a chart is the input to your script. The output is a plot (it doesn't matter if it's a y=x or y=e^x+2x or y=|x| function, use your imagination)
#test your solution properly. Look how it behaves given different input values. (1p)

inp = int(input("Input: "))
X=np.random.rand(inp)
Y=np.linspace(-200,200,inp)

plot(Y,X)
show()

#5 upload the solution as a Github repository. I suggest creating a directory for the whole python course and subdirectories lab1, lab2 etc. (0.5p)
#Ad 5 Hint write in Google "how to create a github repo". There are plenty of tutorials explaining this matter.

# https://github.com/advvix/py-course
