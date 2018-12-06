#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 17:45:16 2018

@author: simon
"""

from math import floor
from math import sqrt

def ispal(number):
    s = str(number)
    l = len(s)
    for x in range(0, floor(l/2) + 1):
        if s[x] != s[l-(x+1)]:
            return False
    return True

assert ispal(12321)==True
assert ispal(123421)==False
assert ispal(456654)==True
assert ispal(2)==True
assert ispal(13)==False

# Fresh start

maxnum = 10**8
pal_ans = set()  # Make sure pal nums are unique
for minsq in range(1, floor(sqrt(maxnum))+2):
    sofsq = minsq**2
    numadd = minsq+1
    while sofsq < maxnum:
        sofsq += numadd**2
        if ispal(sofsq)==True and sofsq<maxnum:
            pal_ans.add(sofsq)
        
        numadd += 1

print(sum(pal_ans))
        
        