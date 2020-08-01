# Mitchell Krouss
#3/15/2019
#Simpsons Rule


import math
import numpy as np
import matplotlib.pyplot as plt

n = 8
b = np.exp(1) + 2
a = np.exp(1)
h = (b - a)/n


def f(x):
    return 1/(x * np.log(x))

x = np.arange(a, b+h, h)

y = f(x)

int = (h/3)*(y[0] + y[n])

for i in range (1, n):
    if (i % 2)==0:
        int = int + (h/3)*2*y[i]
    else:
        int = int + 4*(h/3)*y[i]

print("int = ", int)