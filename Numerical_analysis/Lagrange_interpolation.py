#-------------------------------------------------------------------------------
# Name:        Lagrange Interpolation
# Purpose:
#
# Author:      Mitchell Krouss
#
# Created:     20/02/2019
# Copyright:   (c) Mitchell 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import math
import numpy
import matplotlib.pyplot as plt

x = [8.1, 8.3, 8.6, 8.7] # x-data points here
y = [16.94410, 17.56492, 18.50515, 18.82091] # y-data points here

# calculate l funcrions

A = numpy.linspace(8.1,8.4,num=2*10**(4))
B = numpy.linspace(8.004,8.7,num=2*10**(4))
z = numpy.concatenate((A,B),axis=0)
n = len(x)
p = 0

for i in range(n):
    L=1
    for j in range(n):
        if i==j:
            pass
        else:
            # L = L * (z-x[j])/(x[i]-x[j])
            L *= (z-x[j])/(x[i]-x[j])
    p += y[i] * L

print(p[2*10**(4) - 1])
plt.plot(x,y,'ko',z,p)






