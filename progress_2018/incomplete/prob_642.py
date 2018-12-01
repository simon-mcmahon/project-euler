#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 19:20:54 2018

@author: simon
"""

from pyprimesieve import factorize, primes
from math import floor, log2
from itertools import product
from random import randint

# Do it the manual way
def f(x): # Find the maximum prime inside a number
    if x==1:
        return 1
    ps = [tup[0] for tup in factorize(x)]
    return max(ps)
assert f(1)==1
assert f(1024)==2
assert f(4350983450)==48533

def manual_phi(x,y):
    count = 0
    for i in range(1,floor(x)+1):
        if f(i) <= y:
            count += 1
    return count

# Recursive phi using the identities
_phicache = {}
# Populate the cache
high_pop = 100
for tup in product(range(1,high_pop+1), primes(high_pop+1)):
    if tup[1] > tup[0]:
        continue
    _phicache.update({tup: manual_phi(tup[0], tup[1])})

print('built cache length is {}'.format(len(_phicache)))

maxCache = 10**6

def phi(x,y):
    if y >= x:
        return x

    if type(x)!=int:
        raise ValueError('only put integers into the recursive function')
    try: # Try the cache
        return _phicache[(x,y)]
    except KeyError: # Not in the cache so calculate

        if y==2:
            outsum = floor(log2(x)) + 1
            outsum = outsum%(10**9)
            if len(_phicache) < maxCache:
                _phicache.update({(x,y):outsum})
            return outsum
        else:
            # TODO Generate it using a dynamic programming approach
            outsum = 1
            ps = primes(y+1)
            pnum = len(ps)
            for cnt, p in enumerate(ps):
#                if p >= floor(x/p): # All larger primes equal to x
#                    for i in ps[cnt:]:
#                        outsum += floor(x/p)
##                        assert p >= floor(x/p)
#                    return outsum
##                    outsum += (pnum-cnt)*
#                else:
                outsum += phi(floor(x/p), p)%(10**9)
            outsum = outsum%(10**9)
            if len(_phicache) < maxCache:
                _phicache.update({(x,y):outsum})
            return outsum

assert phi(3487, 13) == manual_phi(3487, 13)

def F(x):
    # Sum of the top prime factors up to x
    # Validate the identity found
    out = 0
    for p in primes(x):
        out += (p * phi(floor(x/p), p))%(10**9)
        out = (out%10**9)
    return out

assert F(10)==32
assert F(100)==1915
assert F(10000)==10118280

# Test on random numbers
#def rand_prime(maxnum):
#    ps = primes(maxnum+1)
#    pnum = len(ps)
#    return ps[randint(0, pnum-1)]
#
#maxNum = 10**5
#testNum = 100
#for x in range(0, testNum):
#    print(x)
#    testprime = rand_prime(maxNum)
#    testX = randint(2, maxNum)
#    assert phi(testX, testprime) == manual_phi(testX, testprime)



