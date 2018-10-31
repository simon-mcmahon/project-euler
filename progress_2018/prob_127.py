#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 18:58:37 2018

@author: simon
"""

from pyprimesieve import factorize
from math import gcd, ceil
sumC = 0
maxC = 120000
sol_tup = []
rad_dict = {}

def rad(n):
    try:
        return rad_dict[n]
    except KeyError:
        out = 1
        primes = [tup[0] for tup in factorize(n)]
        for prime in primes:
            out *= prime
        rad_dict.update({n:out})
        return out

for c in range(2, maxC):
    if rad(c)==c:
        continue
    red_c = c//rad(c) # make it an integer
    if c%1000==0:
        print(c)
    c_fact = factorize(c)
    primes = [tup[0] for tup in c_fact]
    a_range = range(1, ceil(c/2))
    for prime in primes: # filter down to coprime elements
        a_range = list(filter(lambda x: x%prime!=0 ,a_range))
    
    for a in a_range:
        if rad(a) > red_c:
            continue
        b = c-a
        if gcd(b,c)==1 and gcd(a,b)==1:
            if rad(a)*rad(b) < red_c:
                sumC += c
                sol_tup += [(a,b,c)]
        else:
            continue