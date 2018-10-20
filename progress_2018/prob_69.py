#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 19:04:31 2018

@author: simon
"""

from pyprimesieve import factorize

def phi(n):
    primes = [tup[0] for tup in factorize(n)]
    prod = 1
    num = n
    for prime in primes:
        num = num // prime
        prod = prod * (prime-1)
    prod *= num
    return prod
    

tups = factorize(100)
print(tups)

maxn = 10**6
maxfrac = 0
sol = 0
for n in range(1,maxn+1):
    ph = phi(n)
    frac = n/ph
    if frac > maxfrac:
        maxfrac = frac
        sol = n

print(sol)