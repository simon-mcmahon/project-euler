#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 17:14:58 2018

@author: simon
"""

# dynamic progamming approach
from math import factorial

facts = {str(x):factorial(x) for x in range(0, 10)}

def dig_fact(n):
    total = 0
    numstr = str(n)
    for char in numstr:
        total += facts[char]
    return total
    
# ATTEMPT 2 - no fancy programminng. Just loops.

ans = 0

for number in range(1,10**6):
    if number%(10**4)==0: # each print is a 1% iteration in the loop
        print(number)
    count = 1
    seens = {number}
    prev_iter = number
    while True and count <=70:
        next_iter = dig_fact(prev_iter)
        if next_iter in seens:
            break
        else:
            prev_iter = next_iter
            seens.add(prev_iter)
            count += 1
    
    if count == 60:
        ans += 1

print(ans)

