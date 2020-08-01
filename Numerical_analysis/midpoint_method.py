# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 20:19:09 2019

@author: Mitchell Krouss
Method: Midpoint_method
"""
import math
import numpy as np
import matplotlib.pyplot as plt
import scipy.special as sc 

a = 2
b = 4
h = 0.0025
n = int((b - a) / h)

def f(t,y):
    return (t*y + y)/(t*y + t)

t = np.arange(a, b+h, h)
y = np.zeros(len(t))
y[0] = 4
for i in range(1, n+2):
    ym = y[i-1] + (h/2)*f(t[i-1],y[i-1])
    tm = t[i-1] + h/2
    y[i] = y[i-1] + (h)*f(tm,ym)

def z(t):
    return sc.lambertw(2*t*np.exp(t+2))

plt.plot(t,y,t,z(t))
plt.legend(['Midpoint','Analytic'])
plt.ylabel('y(t)')
plt.xlabel('t')
plt.title('h = 0.0025')
plt.show()


