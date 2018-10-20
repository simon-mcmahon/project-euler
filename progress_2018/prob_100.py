#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 23:00:45 2018

@author: simon
"""

# When you do the algebra and solve as q quadratic you find that.
# N = (1+sqrt(8*b**2-8*b+1))/2
# and relies on 8*b**2-8*b+1 being a square number
# We can then go further and find the minimum value of b to make N > 10**12
# b > (2+sqrt(4+2*(alpha-1)))/4
# where alpha = (2*N -1)**2

from math import sqrt, ceil

def N(b):
    return (1+sqrt(8*b**2-8*b+1))/2

def isSquare(i):
    return int(sqrt(i))**2==i

minN = 10**12

alpha = (2*minN -1)**2

minB = (2+sqrt(4+2*(alpha-1)))/4

print('b > {} and N(minB)={}'.format(minB, N(minB)))
# Checking working out done correctly
assert int(N(minB)) == 10**12

# By dong more math on the equatin 8b**2 - 8b + 1 = k**2
# We can discover we need solutions to k^2 - 2j^2 = -1 
# where the sqrt(2k**2 + 2) isi congruent to 2 mod 4

# From the link https://math.stackexchange.com/questions/531833/generating-all-solutions-for-a-negative-pell-equation
#We can generate all solutions of this negative pell equation using
# x**2 - 2y**2 = -1
# x[n+1] = 3x[n] + 4y[n] AND y[n+1] = 2x[n] + 3y[n]
# with x0 = y0 = 1

minK = ceil(sqrt(8*minB**2 - 8*minB + 1))
x = 1
y = 1

count = 0
maxcount = 10**4
while True and count <= maxcount:
    x1 = 3*x + 4*y
    y1 = 2*x + 3*y
    x = x1
    y = y1
    assert x**2 - 2*y**2 == -1
    if x > minK:
        if isSquare(2*x**2 + 2):
            j = int(sqrt(2*x**2 + 2))
            if j%4 == 2:
                b = (2+j)//4
                if isSquare(8*b**2-8*b+1):
                    break
    else:
        count += 1
        continue
    

assert b > ceil(minB)
assert N(b) > 10**12
assert N(b) - int(N(b)) == 0.0

print('solution b = {}, N = {}'.format(b, N(b)))
