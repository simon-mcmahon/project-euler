#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 19:38:53 2018

@author: simon
"""

# dynamic program attempt 

# prime sieve

# easy way
import pandas as pd
from pyprimesieve import factorize

def prod(lst):
    out = 1
    for num in lst:
        out *= num
    return out

def rad(n):
    return prod([tup[0] for tup in factorize(n)])

maxN = 10**5

df = pd.DataFrame([[x, rad(x)] for x in range(1, maxN+1)], columns=['n','rad(n)'])

df = df.sort_values(by=['rad(n)','n'])

# 10,000th value
ans = df.iloc[[10000-1],0:2] # subtract one to account for 0 indexing
print(ans)


