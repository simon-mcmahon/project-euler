#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 12:46:20 2018

@author: simon
"""

import itertools
from pyprimesieve import factorize
from math import sqrt, floor

def issquare(n):
    tol = 10**(-12)
    if sqrt(n) - floor(sqrt(n)) < tol:
        return True
    else:
        return False

assert issquare(4)==True
assert issquare(1567**2)==True
assert issquare(8787)==False
    

def fact(n):
    f = factorize(n)
    primes = [tup[0] for tup in f]
    powers = [tup[1] for tup in f]
    return [primes, powers]

def prod(iterable):
    out = 1
    for elem in iterable:
        out *= elem
    return out

def p_fact_times(primes, powers):
    return prod([primes[x]**powers[x] for x in range(0,len(primes))])

assert p_fact_times(fact(120)[0], fact(120)[1]) == 120

def factors(n): 
    # Generator returning the factors of a number out of order
    f = fact(n)
    prod_args = [range(0, x+1) for x in f[1]]
    # Get the combinations of prime factors
    for pow_comb in itertools.product(*prod_args):
        yield p_fact_times(f[0], pow_comb)
    

assert sorted(list(factors(120))) == [1,2,3,4,5,6,8,10,12,15,20,24,30,40,60,120]

# Generate Pythagorean triples
maxb = 10**4
ans_found = False
b = 3
while True and b <= maxb and ans_found==False:
    trips = set()
    seen_facts = set()
    trip_cnt = 0 # number of pythagorean triples
    for factor in factors(b**2):
        other = ((b**2)//factor)
        if factor == other:
            continue
        if (factor in seen_facts) or (other in seen_facts):
            continue
        seen_facts.add(factor)
        seen_facts.add(other)

        if factor%2 == (other)%2:
            a = abs(factor - other)//2
            c = (factor+other)//2
            assert a**2 + b**2 == c**2
            trip_cnt += 1
            trips.add(tuple([min(a,b), max(a,b), c]))
    
    # Triples finished generating
    if trip_cnt >= 2: # More than 1 tip with b = constant
        trips = list(trips)
        # Iterate over all 2 combinations
        for dbl in itertools.combinations(trips, 2):
            # Assign a1 lowest nonb entry a2 max.
            asbs = [dbl[0][0], dbl[0][1], dbl[1][0], dbl[1][1] ]
            asbs = list(filter(lambda x: x!=b, asbs))
            a1 = min(asbs)
            a2 = max(asbs)
            
            if a1%2 != a2%2: # x, y, z not integers
                continue
            
            y = (a1**2 + a2**2)//2
            z = (a2**2 - a1**2)//2
            x = b**2 + y
            # Error checking code
            assert issquare(x-y)==True
            assert issquare(y-z)==True
            assert issquare(y+z)==True
            assert issquare(x-z)==True
            assert issquare(x+z)==True
            if issquare(x+y):
                ans = (x,y,z)
                ans_found = True
                break
        
    b+= 1

if ans_found:
    print(ans)
    print(sum(ans))