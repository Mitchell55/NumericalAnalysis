# Mitchell Krouss
# Trapezoidal Rule
# 3/14/2019

import math
import numpy as np
import matplotlib.pyplot as plt

n = 8
a = np.exp(1) 
b = np.exp(1) + 2
h = (b - a)/n

x = np.arange(a, b+h, h)

def f(x):
    return 1/(x * np.log(x))

y = f(x)

intt = (h/2)*y[0]

for i in range(1, n):
   intt = intt + (h/2)*(2*y[i])



int = intt + (h/2)*y[n]

print("int = ", int) 

