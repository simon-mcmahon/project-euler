#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 10:51:14 2018

@author: simon
"""

from math import ceil
import numpy as np
from collections import defaultdict
def cube_lst(k):
    # k = power of is the number of digits in the cubes
    # 10**(k-1) <= n**3 < 10**(k)
    n_range = np.arange(ceil(10**((k-1)/3)), ceil(10**((k)/3)))
    cubes = np.power(n_range,3)
    return cubes

assert np.all(np.equal(np.array([125, 216, 343, 512, 729]),cube_lst(3)))

def dig_freq(num):
    numstr = str(num)
    digs = range(0,10)
    freq = defaultdict(int)
    for char in numstr:
        freq[int(char)]+= 1
    return tuple([freq[x] for x in digs])

assert dig_freq(1112999) == (0,3,1,0,0,0,0,0,0,3)


cubelen = 2
while True:
    permutes = defaultdict(int)
    for cube in cube_lst(cubelen):
        permutes[dig_freq(cube)] += 1

    if 5 in permutes.values():
        freq5 = []
        poss_ans = []
        for freq in permutes:
            if permutes[freq]==5:
                freq5.append(freq)
        
        for cube in cube_lst(cubelen):
            if dig_freq(cube) in freq5:
                poss_ans.append(int(round(cube**(1/3))))
            
        print(poss_ans)
        ans = min(poss_ans)
        assert permutes[dig_freq(ans**3)]==5
        break
    cubelen += 1
    
print(ans**3)