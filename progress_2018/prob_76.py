#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 19:32:03 2018

@author: simon
"""

def subset_sum(n):
    # Generator which gives all the unique partitions up to sum n in order.
    
    p=[0]*n
    k=0
    p[k] = n
    
    while True:
        yield p[0:k+1]
        
        rem_val = 0
        while k>=0 and p[k]==1:
            rem_val += p[k]
            k -= 1
        
        if k<0:
            return
        
        p[k] = p[k] - 1
        rem_val += 1
        
        while rem_val > p[k]:
            p[k+1] = p[k]
            rem_val = rem_val - p[k]
            k += 1
        
        p[k+1] = rem_val
        k+=1

ans = 0

for s in subset_sum(100):
    ans += 1

print(ans-1) # Exclude the case where the sum is 1 long.