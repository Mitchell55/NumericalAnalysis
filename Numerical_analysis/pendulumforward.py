# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 19:33:02 2019

@author: Mitchell Krouss
Double Pendulem using Forward Euler
"""
import math
import numpy as np
import matplotlib.pyplot as plt
import scipy.special as sc 

c = 0.16
L = 1.2
g = 9.81
m = 0.5
a = 0
b = 18
h = 0.01
n = int((b - a) / h)

def f(w,theta):
    return -(c/m)*w - (g/L)*np.sin(theta)


t = np.arange(a, b+h, h)
w = np.zeros(len(t))
theta = np.zeros(len(t)) 
theta[0] = (np.pi)/2 #initial conditions
for i in range(1, len(t)):
    w[i] = w[i-1] + h*f(w[i-1],theta[i-1])
    theta[i] = theta[i-1] + h*w[i-1]

print("theta = ",theta)
print("t = ",t)


plt.plot(t,theta)
plt.legend(['h = 0.1','h = 0.01'])
plt.ylabel('theta')
plt.xlabel('t')
plt.title('Pendulum')
plt.show()


