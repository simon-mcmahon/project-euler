#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 12:08:13 2018

@author: simon
"""

import itertools
from pyprimesieve import factorize   
from math import sqrt , floor

def issquare(n):
    tol = 10**(-12)
    if sqrt(n) - floor(sqrt(n)) < tol:
        return True
    else:
        return False

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

def fact_num(n):
    return prod([x+1 for x in fact(n)[1]])

assert fact_num(120)==len([1,2,3,4,5,6,8,10,12,15,20,24,30,40,60,120])
assert sorted(list(factors(120))) == [1,2,3,4,5,6,8,10,12,15,20,24,30,40,60,120]

ans = 0
maxn = 10**6 - 1
for n in range(2, maxn+1):
    if fact_num(n) < 10: # One set of factors can have 2 sols
        continue
    else:
        seen_facts = set()
        sols = set()
        for factor in factors(n):
            other = ((n)//factor)
            if (factor in seen_facts) or (other in seen_facts):
                continue
            seen_facts.add(factor)
            seen_facts.add(other)
            
            # If the a and d values are integers
            if (factor%2 == (other)%2) and (factor+other)%4==0:
                d = (factor+other)//4
                # The positive case
                a = d + int(sqrt(4*d**2 - n))
                # Check 
                assert (a+2*d)**2 - (a+d)**2 - a**2 == n
                assert issquare(4*d**2 - n)==True
                sols.add((a,d,n))
                
                if int(sqrt(4*d**2 - n)) < d:
                    # Second case where sol exists sometimes.
                    a = d - int(sqrt(4*d**2 - n))
                    # Check
                    assert issquare(4*d**2 - n)==True
                    assert (a+2*d)**2 - (a+d)**2 - a**2 == n
                    assert a > 0
                    sols.add((a,d,n))

        if len(sols) == 10:
#            print(n)
#            break
            ans += 1

print(ans)
        
    
        

    


    
    
    
    
    
    