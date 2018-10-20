#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 19:02:16 2018

@author: simon
"""

from fractions import Fraction

def inv(frac):
    return Fraction(frac.denominator, frac.numerator)

f=[]
f += [1 + Fraction(1,2)]
ans = 0
while len(f) <= 1000:
    nextf = inv(f[-1] + 1) + 1
    if len(str(nextf.numerator)) > len(str(nextf.denominator)):
        ans += 1
    f += [nextf]
    
print(f[0:5])
print(ans)
