#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 23:41:04 2018

@author: simon
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 23:30:04 2018

@author: simon
"""

# Should be a fairly straight forward dynamic programming with a list of primes
# Dont forget to memoize 

# Firstly lets build the machinery for the primes

# Inefficient sieve
from sympy.ntheory.primetest import isprime
from math import ceil, sqrt
import bisect
import functools

maxPrime = 10**5
primes = range(2,maxPrime+1)
f_mod = 2
seen_mods = set()
while f_mod <= ceil(sqrt(maxPrime)):
    primes = list(filter(lambda x: x==f_mod or x%f_mod!=0, primes))
    seen_mods.add(f_mod)
    count = 0
    while True:
        if primes[count] not in seen_mods:
            f_mod = primes[count]
            break
        else:
            count += 1

# Check the sieve
for x in primes:
    assert isprime(x)==True

def pBelow(N):
    #Efficient use of binary search on the sorted list
    return primes[0:bisect.bisect_right(primes, N)]

# Dynamic Programming

def memoize(func):
    cache = dict()

    def memoized_func(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result

    return memoized_func

@memoize
def pSum(diff, picked=()):
    if diff==1 or diff<0:
        return 0
    elif diff==0:
        return 1
    else:
        if len(picked)!=0:
            pLimit = min(picked)
        else:
            pLimit = diff
        ps = pBelow(pLimit)
        return sum([pSum(diff-p, tuple(list(picked)+[p])) for p in ps])

ans = 2
while True:
    if pSum(ans) > 5000:
        break
    ans += 1

print(ans)