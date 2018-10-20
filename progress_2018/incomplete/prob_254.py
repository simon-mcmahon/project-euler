#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 18:27:24 2018

@author: simon
"""

from math import factorial

fact_dict = {x: factorial(x) for x in range(0,10)}

f_vals = {}
sf_vals= {}
g_vals = {}
sg_vals = {}
def f(n):
    try:
        return f_vals[n]
    except KeyError:
        total = 0
        for char in str(n):
            total += fact_dict[int(char)]
        f_vals.update({n: total})
        return total


def sf(n):
    try:
        return sf_vals[n]
    except KeyError:
        total = 0
        num = f(n)
        for char in str(num):
            total += int(char)
        sf_vals.update({n:total})
        return total
    
def g(i):
    try:
        return g_vals[i]
    except KeyError:
        # Iterate over the memoized answers for sf first
        for num, key in enumerate(sf_vals):
            if num+1 != key:
                raise ValueError('dict elements out of order')
            elif sf_vals[key]==i:
                g_vals.update({i:key})
                return key
        # If not iterate over starting from the largest of the keys
        if len(sf_vals) > 0:
            count = max(sf_vals.keys())
        else:
            count = 1
        while True:
            if sf(count)==i:
                break
            count += 1
        g_vals.update({i:count})
        return count

def sg(i):
    try:
        return sg_vals[i]
    except KeyError:
        total = 0
        num = g(i)
        for char in str(num):
            total += int(char)
        sg_vals.update({i:total})
        return total
    
# Verify functions
tot = 0
for x in range(1,21):
    tot += sg(x)
assert tot == 156

## Actual code
#ans= 0
#for x in range(1,151):
#    print(x)
#    ans += sg(x)
#print(ans)