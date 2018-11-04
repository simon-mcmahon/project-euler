#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 23:14:03 2018

@author: simon
"""

from pyprimesieve import factorize
from collections import defaultdict
def phi(n):
    primes = [tup[0] for tup in factorize(n)]
    prod = 1
    num = n
    for prime in primes:
        num = num // prime
        prod = prod * (prime-1)
    prod *= num
    return prod

perm_phi = []

for n in range(2,10**7):
    if n%(10**(7-2))==0:
        print(n)
    strP = str(phi(n))
    strN = str(n)
    if len(strN)!=len(strP):
        continue
    
    else:
        digN = defaultdict(int)
        digP = defaultdict(int)
        for c in strN:
            digN[c] += 1
        for c in strP: 
            digP[c] += 1
        if digN == digP:
            perm_phi.append((strN, strP))
            
# Sort the list by ratio. answer is the 1st entry

sorted_perm_phi = sorted(perm_phi, key=lambda x: int(x[0])/int(x[1]))
print(sorted_perm_phi[0])