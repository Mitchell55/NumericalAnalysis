# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 20:19:09 2019

@author: Mitchell Krouss
Method: Rk4_method
"""
import math
import numpy as np
import matplotlib.pyplot as plt
import scipy.special as sc 

a = 2
b = 4
h = 0.01
n = int((b - a) / h)

def f(t,y):
    return (t*y + y)/(t*y + t)

t = np.arange(a, b+h, h)
y = np.zeros(len(t))
y[0] = 4
for i in range(1, n+1):
    k1 = h*f(t[i-1],y[i-1])
    k2 = h*f(t[i-1] + h/2, y[i-1] + (1/2)*k1)
    k3 = h*f(t[i-1] + h/2, y[i-1] + (1/2)*k2)
    k4 = h*f(t[i], y[i-1] + k3)
    y[i] = y[i-1] + (1/6)*(k1 + 2*k2 + 2*k3 + k4)


def z(t):
    return sc.lambertw(2*t*np.exp(t+2))

plt.plot(t,y,t,z(t))
plt.legend(['RK4','Analytic'])
plt.ylabel('y(t)')
plt.xlabel('t')
plt.title('h = 0.01')
plt.show()
print(y)


