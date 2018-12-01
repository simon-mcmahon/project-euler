#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 13:54:43 2018

@author: simon
"""

from pyprimesieve import factorize
import numpy as np

def fact_num(n):
    return np.prod([tup[1]+1 for tup in factorize(n)])
    
assert fact_num(120)==len([1,2,3,4,5,6,8,10,12,15,20,24,30,40,60,120])
np_fact = np.vectorize(fact_num)

for n in [100, 10**8]:
    q = np.mod(np_fact(np.arange(1,n+1)), 6).astype(np.uint64)
    ans = np.sum(q==1)
    if n==100:
        assert ans==2
    else:
        assert ans==69
print(ans)

