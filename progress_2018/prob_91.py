#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 18:53:53 2018

@author: simon
"""
# Problem boils down to having one pair of lines perpendicular with 
# m_perp = -1/m
# yields 3 equation possibilites
# which work despite inclusion of zeroes surprisingly
# just iterate over them and add up matches

from itertools import product, combinations
N = 50
ans = 0
points = list(product(range(0, N+1), repeat=2))

for pair in combinations(points, 2):
    if (0,0) in pair: # P and Q do not contain origin
        continue
    x1, y1 = pair[0]
    x2, y2 = pair[1]
    if y1*y2 + x1*x2 == 0:
        ans += 1
    elif y1*y2 + x1*x2 == y1**2 + x1**2:
        ans += 1
    elif y1*y2 + x1*x2 == y2**2 + x2**2:
        ans += 1

print(ans)