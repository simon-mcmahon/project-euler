#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 00:30:02 2018

@author: simon
"""

# this is a simple case of the integer partition function
# http://mathworld.wolfram.com/PartitionFunctionP.html
# Using property 11
import sys
import functools
from math import sqrt, floor
sys.setrecursionlimit(1500)

part_dict = {0:1, 1:1}

@functools.lru_cache(maxsize=10**6)
def PartitionP(n):
    if n < 0:
        return 0
    elif n==1 or n==0:
        return 1
    else:
        try:
            return part_dict[n]
        except KeyError:
            out = 0
            for k in range(1,floor((sqrt(24*n+1)+1)/6)+1):
                # Better upper k-bound here
                # https://arxiv.org/pdf/1612.05526.pdf
                in1 = n - (k*(3*k-1))//2
                in2 = n - (k*(3*k+1))//2
                try:
                    s1 = part_dict[in1]%10**6
                    s2 = part_dict[in2]%10**6
                    out += (-1)**(k+1)*(s1+s2)
                except KeyError:
                    out += (-1)**(k+1)*(PartitionP(in1) + PartitionP(in2))
            out = out%10**6
            part_dict.update({n:out})
            return out

assert PartitionP(5) == 7
# Agrees with https://oeis.org/A000041
#for x in range(1,15):
#    print(PartitionP(x))

count = 1
while True:
    ans = 5*count + 4
    if count%1000==0:
        print(ans)
    if PartitionP(ans)%10**6==0:
        break
    count += 1

print(ans)
