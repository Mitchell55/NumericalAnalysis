# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 20:19:09 2019

@authors: Mitchell Krouss
Method: Backward Euler
"""
import math
import numpy as np
import matplotlib.pyplot as plt
import scipy.special as sc 

a = 0
b = 1
h = 0.00001
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
    k = y[i-1]
    d = x[i-1]
    for j in range(1, 100):
        num = -k + y[i-1] + h*f(d,k)
        denom = -1 + h*(-1998)
        k = k - num/denom
        numm = -d + x[i-1] + h*g(d,k)
        denomm = -1 + h*(1000)
        d = d - numm/denomm
    y[i] = k
    x[i] = d
   
print(y[10])
print(x[10])
print(t[10])


plt.plot(t,y)
plt.plot(t,x)
plt.legend(['y','x'])
plt.xlabel('t')
plt.title('Backwards Euler')
plt.show()
