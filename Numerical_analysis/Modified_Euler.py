# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 20:19:09 2019

@author: Mitchell Krouss
Method: Modified Euler
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
    slopebegin = f(t[i-1],y[i-1])
    yeu = y[i-1] + h*slopebegin
    slopeend = f(t[i],yeu)
    y[i] = y[i-1] + (h/2)*(slopebegin + slopeend)
    

def z(t):
    return sc.lambertw(2*t*np.exp(t+2))


plt.plot(t,y,t,z(t))
plt.legend(['Modified Euler','Analytic'])
plt.ylabel('y(t)')
plt.xlabel('t')
plt.title('h = 0.0025')
plt.show()



