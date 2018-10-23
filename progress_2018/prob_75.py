#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 00:19:15 2018

@author: simon
"""
from pyprimesieve import factorize
from itertools import product
from collections import defaultdict
import numpy as np
maxb = 750000
total_Sum = 1.5*10**6


def valFactors(num):
    """
    Generate the pairs of factors with the same parity of a number
    using the prime factor of the number
    """
    fact_pairs = set()
    factors = factorize(num)
    
    Args = [range(p[1]+1) for p in factors]
    primes = [p[0] for p in factors]
    for pow_comb in product(*Args):
        fact1 = np.prod(np.power(primes, pow_comb))
        fact2 = num//fact1
        if (fact2 < fact1) or (fact1 % 2)!=(fact2 % 2):
            continue
        else:
            fact_pairs.add((fact1, fact2))
    
    return fact_pairs
            
    
pyth_trips = set()    


for b_val in range(2, maxb+1):
    if b_val%10000==0:
        print(b_val)
    # a^2 + b^2 = c^2 
    # b^2 = (c+a)(c-a)
    # c+a is larger of mult of b and a factor of b (k)
    # so long as k and (b/k) are the same mod 2.
    for pair in valFactors(b_val**2):
        for p in [pair, tuple(list(pair)[::-1])]: #account for forward and reverse
            
            if p[0] + b_val > total_Sum:
                continue
            c = (p[0] + p[1])//2
            a = (p[0] - p[1])//2
            total = p[0] + b_val
            assert a**2 + b_val**2 == c**2
            assert a + b_val + c == total
            # no degerate solutions
            if a >= 1 and c>=1: #and ((min(a,b_val), max(a,b_val),c) not in pyth_trips) and total <= total_Sum: 
                # make sure tuples are unique by making a < b
                pyth_trips.add((min(a,b_val), max(a,b_val),c))


    
#print(pyth_trips)
print('----------------------------')

qq = defaultdict(int)
count = 0

for pythag in pyth_trips:
    total = sum(pythag)
    qq[total] += 1

for x in qq:
    if qq[x]== 1:
        count += 1

print(count)