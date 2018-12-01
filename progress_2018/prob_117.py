#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 10:41:48 2018

@author: simon
"""

arrnum = 0
bars = 50

from itertools import product
from math import floor

def combs(st): # Finds N!/(n1! * n2! * ... * nk!) from the state tuple
    N = sum(st)
    n1 = max(st)
    ns = list(st)
    ns.remove(n1)
    out = 1
    for x in range(n1+1, N+1):
        out *= x
    for n in ns:
        for x in range(1, n+1):
            out = out // x
    return out

# Brute force iterate over all the combinations of 
# 4*B + 3*G + 2*R + Bl = 50

for Bl in range(0, bars+1): 
    sumtot = bars-Bl
    Bmax = floor(sumtot/4)
    Gmax = floor(sumtot/3)
    
    for BG in product(range(Bmax+1), range(Gmax+1)):
        twoR = sumtot - 4*BG[0] - 3*BG[1]
        if ((twoR)%2 == 0) and (twoR >= 0):
            R = (twoR)//2
            state = (BG[0], BG[1], R, Bl) 
            # system state (Blue, Green, Red, Black)
            assert 4*state[0] + 3*state[1] + 2*state[2] + state[3] == bars
            arrnum += combs(state)
            

print(arrnum)