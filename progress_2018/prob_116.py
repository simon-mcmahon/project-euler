#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 10:20:11 2018

@author: simon
"""

from math import factorial
arrnum = 0
bars = 50

def combs(st): # Finds N!/(n1! * n2!) from the state tuple
    N = st[0] + st[1]
    n1 = max(st[0],st[1])
    n2 = min(st[0], st[1])
    out = 1
    for x in range(n1+1, N+1):
        out *= x
    for x in range(1, n2+1):
        out = out // x
    return out
    

for psize in [2,3,4]:
    state = (0, bars) # state of the arrangement. (number of psize, number of 1's)
    
    while True:
        if state[1] >= psize:
            state = (state[0]+1, state[1]-psize)
        else:
            break
        assert state[0]*psize + state[1]*1 == bars
        
        arrnum += combs(state)

print(arrnum)