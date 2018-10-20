#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 21:04:01 2018

@author: simon

Using the binomial theorem and convenient cancellation.
We are able to find that n must be odd. the (a-1)^n + (a+1)^n = 2*n*a (mod a^2)
Then use k=2n which must be 2 mod 4.
Then use lists of increasing k*a mod a^2 and check the maximum value each time 
the k terms gets larger than a.
return the maximum of those values

"""

def rmax(a):
    squared = a**2
    rs = []
    maxes = list(map(lambda x: x*a, range(1, a)))
    for Max in maxes:
        if (Max%4)==3:
            k = Max - 1
        else:
            k = Max - (Max%4) - 2
        r = (k*a)%(squared)
        rs.append(r)
#        print('{} and so {} mod {}'.format(k,r, squared))
    return max(rs)

assert rmax(7) == 42

ans = sum([rmax(a) for a in range(3,1001)])

print(ans)