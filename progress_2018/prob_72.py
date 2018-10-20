#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 18:02:10 2018

@author: simon
"""

# Grab the totient function from problem 69

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

# Test the number of relatively prime fraction is the sum of the totient
total = 0
for x in range(2,9):
    total += phi(x)
assert total == 21

# It is correct so

ans = 0 
for x in range(2, 10**6+1):
    ans += phi(x)

print(ans)