#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 21:32:19 2018

@author: simon
"""
from math import floor, ceil

def ncr(n,r):
    if (n <= 0) or (r>n) or (r<0):
        raise ValueError('Make sure to have positive n and r <= n')
    if (n-r) > r:
        mult = n-r
        div = r
    else:
        mult = r 
        div = n-r
    
    ans = 1
    for x in range(mult+1, n+1):
        ans *= x
    for x in range(2, div+1):
        ans = ans // x
    return ans

ans = 0

for n in range(1,101):
    r_max = floor(n/2)
    for r in range(0, r_max+1):
        if ncr(n,r) > 10**6:
            if (n%2==0) and (r==r_max):
                ans += 1
            else:
                ans += 2
            
print(ans)