#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 13:32:28 2018

@author: simon
"""
# Not particularly proud of this one
# Solution is bashy.
# It is an awkward mess of the minimum which would have been
# The minimum sum approach and the full dynamic programming approach 
# It works however and it fast.

import numpy as np
import functools
import sys

sys.setrecursionlimit(1500)

with open('p081_matrix.txt', 'r') as f:
    lines = f.readlines()

matrix = []
for line in lines:
    row = list(map(lambda x: int(x),line.strip().split(',')))
    matrix.append(row)

matrix = np.array(matrix)
mat_max = matrix.max()

assert matrix.shape== (80,80)
assert matrix[0,0]==4445
assert matrix[2,0]==9607

# Assemble the small test case matrix
# Shortest path sum 2427

test5 = '''131,673,234,103,18,
201,96,342,965,150,
630,803,746,422,111,
537,699,497,121,956,
805,732,524,37,331'''

matrix5 = [x.split(',') for x in test5.split('\n')]
matrix5 = [[int(k) for k in x if k!=''] for x in matrix5]
matrix5 = np.array(matrix5)
mat5_max = matrix5.max()

assert matrix5.shape == (5,5)
print(matrix5)


# ATTEMPT 2. I WANT TO DO IT WITHOUT THE PATH 

# Dynamic programming attempt
@functools.lru_cache(maxsize=10**5)
def minSum(curr_tot, curr_pos=(79,79)):
    if curr_pos[0]>=80 or curr_pos[0]<0 or curr_pos[1]>=80 or curr_pos[1]<0:
        # Out of bounds case
        val = -999
        return val
    else:
        val = matrix[curr_pos[0], curr_pos[1]]
        
    if curr_pos == (0,0):
        return curr_tot + val

    else:
        left = minSum(curr_tot + val, (curr_pos[0]-1,curr_pos[1]))
        up = minSum(curr_tot + val, (curr_pos[0],curr_pos[1]-1))
        if min([left, up]) < 0:
            minSums = max([left, up])
        else:
            minSums = min([left, up])


        return minSums

_cache = {(0,0):matrix[0,0]}

def minPath(curr_pos):
    try:
        o1 = _cache[(curr_pos[0]-1,curr_pos[1])] + matrix[(curr_pos[0],curr_pos[1])]
        o2 = _cache[(curr_pos[0],curr_pos[1]-1)] + matrix[(curr_pos[0],curr_pos[1])]
        if min(o1, o2) > 0:
            out = min(o1, o2)
        else:
            out = max(o1, o2)
#        out =   + _cache[(curr_pos[0],curr_pos[1]-1)]
        _cache.update({curr_pos: out})
        return out
    except KeyError:
        o1 = minSum(matrix[(curr_pos[0],curr_pos[1])], (curr_pos[0]-1,curr_pos[1]))
        o2 = minSum(matrix[(curr_pos[0],curr_pos[1])], (curr_pos[0],curr_pos[1]-1))
        if min(o1, o2) > 0:
            out = min(o1, o2)
        else:
            out = max(o1, o2)
#        print(out)
        _cache.update({curr_pos: out})
        return out

maxRowCol = 79
for x in range(0,maxRowCol+1):
    for y in range(0,maxRowCol+1):
        if (x,y)==(0,0):
            continue
        minPath((x,y))

print(_cache)
print(matrix[0:3, 0:3])
#q = minPath((2,2))
#print(q)