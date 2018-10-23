#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 18:53:24 2018

@author: simon
"""

from math import floor, ceil, gcd

ans = 0

maxD = 12000

for d in range(2,maxD+1):
    minN = floor(d/3 + 1)
    maxN = ceil(d/2 - 1)
    for n in range(minN, maxN+1):
        if gcd(n,d)==1:
            ans += 1

print(ans)