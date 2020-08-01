#-------------------------------------------------------------------------------
# Name:        Numerical_Differentiation
# Purpose:
#
# Author:      Mitchell Krouss
#
# Created:     9/03/2019
# Copyright:   (c) Mitchell 2019
#-------------------------------------------------------------------------------
import math
import numpy
import matplotlib.pyplot as plt


x = [7.4, 7.6, 7.8, 8] #x-data points here
y = [-68.3193, -71.6982, -75.1576, -78.6974] #y-data points here
h = abs(x[0] - x[1]) #define step size
n = len(x)

for i in range(n):
    if i==0:
        fprime = (1/(2*h))*(-3*y[0] + 4*y[1] - y[2])
        print("f'(x_",i,") = ", fprime)
    elif i==n-1:
        fprime = (1/(2*h))*(y[i-2] - 4*y[i-1] + 3*y[i])
        print("f'(x_",i,") = ", fprime)
    else:
        fprime = (1/(2*h))*(y[i+1] - y[i-1])
        print("f'(x_",i,") = ", fprime)
        