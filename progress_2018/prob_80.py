#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 23:51:54 2018

@author: simon
"""
#Shitty implementation but it works

from math import sqrt, floor
from decimal import *
getcontext().prec = 250
count = 0
b_thres = sqrt(10**100/2)

nrange = list(range(1,101))
for square in [x**2 for x in range(1,11)]:
    nrange.remove(square)

for n in nrange:
    x = floor(sqrt(n))
    x = Decimal(x)
    
    for i in range(0, 50):
        x = (x**3+3*n*x)/(3*x**2+n)
    root = x 
#    # https://math.stackexchange.com/questions/296102/fastest-square-root-algorithm

    digs = str(root).replace('.','')
    for x in range(0,100):
        count += int(digs[x])

print(count)
