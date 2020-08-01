#-------------------------------------------------------------------------------
# Name:        Bisection Script
# Purpose:
#
# Author:      Mitchell Krouss
#
# Created:     31/01/2019
# Copyright:   (c) Mitchell 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import math

#Define interval with a and b
a = 1
b = 2
def f(x):
    return x**(2) - 3 #Input function here
err = 10**(-4) #Define the desired error.

if f(a) * f(b) == 0:
    print("\nNo root on this interval")
else:

    if  f(a) == 0:
        print("\na is a root")
    elif f(b) == 0:
        print("\nb is a root")

    count = float(1)
    p = (a + b)/2
    while abs(f(p))>err and count<30: #This loop stops once the error is reached or the max number of itterations.
        if f(a)*f(p) < 0:
            b = p
        else:
            a = p
        p = (a + b)/2
        count = count + 1

print(p) #This command prints the value of p_n
print(count) #This command prints the number of itterations