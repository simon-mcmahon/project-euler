#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 11:17:52 2018

@author: simon
"""

# Not great but workable

from itertools import permutations
from math import log10, ceil
from numba import jit
s = '123456789'
ispan = set()
for tup in permutations(s, len(s)):
    ispan.add(int(''.join(char for char in tup)))

assert len(ispan) == 9*8*7*6*5*4*3*2*1

fN2 = 1
fN1 = 2
fN = 2
N = 2
maxN = 10**6
approx_percentage = ceil(log10(maxN))-2
ans = 0

@jit(nopython=False)
def fibloop(maxN):
    approx_percentage = ceil(log10(maxN))-2
    fN2 = 1
    fN1 = 2
    fN = 2
    for N in range(4, maxN + 1):
        fN = fN1 + fN2
        fN2 = fN1
        fN1 = fN
#        print(fN)       
        if N%10**approx_percentage==0:
            print(N)
    #    print(fN, N)
        if fN > 10**10:
            first9 =  fN // 10 ** (int(log10(fN)) - 9 + 1)
            
        if fN < 10**574:
            continue
        elif (first9 in ispan) and (fN%10**9 in ispan):
            print(N)
            return N
    return 0

fibloop(100)        
q = fibloop(10**6)
print(q)

    
    