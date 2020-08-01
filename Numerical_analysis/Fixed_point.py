#-------------------------------------------------------------------------------
# Name:        Fixed Point Method
# Purpose:
#
# Author:      Mitchell Krouss
#
# Created:     06/02/2019
# Copyright:   (c) Mitchell 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import math

def g(x):
    return math.acos(-x**(2)/10) #Input g(x) here

tol = 10**(-4) #Input error here
count = float(1)
p=3 #Input initial guess

while abs(g(p)-p)>tol and count<30:
    p=g(p)
    count=count+1

print(p) #Prints roots
print(count) #Prints interations
