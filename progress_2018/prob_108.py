#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 17:04:37 2018

@author: simon
"""

from pyprimesieve import factorize
from math import ceil

def product(iterable):
    out = 1
    for x in iterable:
        out *= x
    return out

n = 4
thresh = 1000
while True:
    factors = factorize(n)
    fact_num_N2 = product([2*tup[1]+1 for tup in factors])
#    print(n, ceil(fact_num_N2/2))
    if ceil(fact_num_N2/2) > 1000:
        break
    n += 1

print(n)