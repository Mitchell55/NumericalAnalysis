# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 20:19:09 2019

@author: Mitchell Krouss
Method: Forward Euler
"""
import math
import numpy as np
import matplotlib.pyplot as plt
import scipy.special as sc 

a = 0
b = 1
h = 0.0001
n = int((b - a) / h)


def f(x,y):
    return 998*x - 1998*y
def g(x,y):
    return 1000*x - 2000*y

t = np.arange(a, b+h, h) 
y = np.zeros(len(t))
x = np.zeros(len(t))
y[0] = 2
x[0] = 1
for i in range(1, len(t)):
    y[i] = y[i-1] + h*f(x[i-1],y[i-1])
    x[i] = x[i-1] + h*g(x[i-1],y[i-1])

print(x[1000])
print(y[1000])
print(t[1000])

plt.plot(t,y)
plt.plot(t,x)
plt.legend(['y(t)','x(t)'])
plt.xlabel('t')
plt.title('Forward Euler')
plt.show()


