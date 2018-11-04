#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 15:33:36 2018

@author: simon
"""

from sympy.ntheory.primetest import isprime
from collections import defaultdict
import numpy as np

# First part of the code is a manual setup mainly for testing purpooses 
# When conjectures and a more mathematical approach was taken
# Using hexagonal coordinates, manually assigning numbers,
# Taking the neighbours and checking if prime
# Works manageably up to around 3*10**6 for 150ish values

# Setting up some general hexagonal coordinate helper functions
# Borrowing heavily from https://www.redblobgames.com/grids/hexagons/#conversions

cube_dirs = {'N':(0,+1,-1), 'NE':(+1,0,-1), 'SE':(+1,-1,0), 'S':(0,-1,+1), 'SW':(-1,0,+1), 'NW':(-1,+1,0)}

def move(coord, direct):
    direct = cube_dirs[direct]
    new_coord = (coord[0]+direct[0], coord[1]+direct[1], coord[2]+direct[2])
    assert sum(new_coord)==0
    return new_coord

def n_move(coord, direct, num):
    new_coord = coord
    for x in range(0,num):
        new_coord = move(new_coord, direct)
    
    return new_coord


assert move(n_move((0,0,0), 'SW', 2),'S')==(-2, -1, 3)
assert move(n_move((0,0,0), 'S', 2),'N')==(0, -1, 1)
assert move(n_move((0,0,0), 'NE', 2),'S')==(2, -1, -1)

# Assemble the spiral by travelling around in a hexagonal pattern
N_layers =10
O = (0,0,0)
dir_order = ['SW', 'S', 'SE', 'NE', 'N', 'NW']
seen_coords = {O}
spiral_num = [[O,1]]
count = 2
for layer in range(1,N_layers+1):
    start = n_move(O, 'N', layer)
    spiral_num += [[start ,count]]
    seen_coords.add(start)
    count += 1
    move_pt = start
    for direct in dir_order:
        if direct=='NW':
            reps = layer - 1
        else:
            reps = layer
        for i in range(0, reps):
            move_pt = move(move_pt, direct) 
            spiral_num += [[move_pt ,count]]
            seen_coords.add(move_pt)
            count += 1
        
    assert move_pt == move(start, 'SE')

assert count==(3*N_layers**2 + 3*N_layers + 1) + 1
assert len(spiral_num)+1 == count

count_key = {tup[1]:tup[0] for tup in spiral_num}
pt_key = {tup[0]: tup[1] for tup in spiral_num}

np_isprime = np.vectorize(isprime)

def PD(n):
    try:
        surrounding_coords = [move(count_key[n], direc) for direc in cube_dirs]
        surrounding_vals = np.asarray([pt_key[coord] for coord in surrounding_coords])
    except KeyError: # Points not loaded into the spiral
        return -999

    primes = np_isprime(np.abs(n - surrounding_vals))
    return np.sum(primes)
    
ans_list = []
for cnt in count_key:
    if cnt%6!=1 and cnt%6!=2:
        continue
    PD_val = PD(cnt)
    if PD_val==3:
        ans_list.append(cnt)
    
print(ans_list)
print('{}. PD=3 numbers out of {}'.format(len(ans_list), count-1))


# Correct PD(3) output for 100 layers
# [1, 2, 8, 19, 20, 37, 61, 128, 217, 271, 398, 919, 1519, 1520, 2978, 3170, 4220, 4447, 4681, 5677, 5941, 6488, 8269, 9920, 10621, 12481, 16651, 17558, 22448, 26227, 29701]
# Identical to when we skip all values 0 mod 3.

from math import floor, ceil, sqrt
from numba import jit
# ALTERNATIVE COORDINATE APPROACH
# Using polarish coordinates for which spiral and modular rotation of the 
# Spiral, use a quadratic subtraction approach to solve the question
# Does not require storing each number in memory.
# VERY IMPORTANT CONJECTURE. values must be -1 mod 6N or 0 mod 6N

def surround(V):
    try:
        surrounding_coords = [move(count_key[V], direc) for direc in cube_dirs]
        surrounding_vals = [pt_key[coord] for coord in surrounding_coords]
    except KeyError: # Points not loaded into the spiral
        return -999
    
    return set(surrounding_vals)

@jit(nopython=True)
def V(N, k):
    if N!=0:
        k = k%(6*N)
    else:
        assert k<6
    if N==0 and k==0:
        return 1
    return 3*N**2 - 3*N + 2 + k

@jit(nopython=True)
def coord(V):
    if V==1:
        return (0,0)
    N = floor((3+sqrt(3**2 - 4*3*(2-V)))/6)
    k = V - (3*N**2 - 3*N + 2)
    assert k == (k%(6*N))
    return (N,k)

assert V(3, 2)==22
assert V(3, -1)==37
assert coord(37)==(3,17)
assert surround(8)=={20,21,9,2,19,37}

@jit(nopython=True)
def surround2(Val):
    if Val==1:
        return {2,3,4,5,6,7}
    coords = coord(Val)
    N = coords[0]
    k = coords[1]
    mod = 6*N
    if k%N==0:  # Corner case
        c_num = (k//N)%6 #corner numebr around the hexagon
        inner = [(N-1, c_num*(N-1))]
        current = [(N, k-1), (N, k+1)]
        outer = [(N+1, c_num*(N+1)-1), (N+1, c_num*(N+1)), (N+1, c_num*(N+1)+1)]
    else:
        in_num = (k/N)*(N-1)
        out_num = (k/N)*(N+1)
        inner = [(N-1, floor(in_num)), (N-1, ceil(in_num))]
        current = [(N, k-1), (N, k+1)]
        outer = [(N+1, floor(out_num) ), (N+1, ceil(out_num))]
    
    combined = inner + current + outer
    return set([V(x[0], x[1]) for x in combined])
    
assert surround2(8) == surround(8)
assert surround2(35) == surround(35)

@jit(nopython=False)
def PD2(Val):
    surrounds = np.asarray(list(surround2(Val)))
    primes = np_isprime(np.abs(Val - surrounds))
    return np.sum(primes)

# Check the surrounding function is identical to the 
for x in range(1,3*N_layers**2 - 3*N_layers + 2):
    try:
        assert surround2(x)==surround(x)
        assert PD2(x) == PD(x)
    except AssertionError:
        print(surround(x))
        print(surround2(x))


# VERY IMPORTANT
# All the answers thus far are -1 mod 6N or 0 mod6N.
# Go for a hunch and 
N1 = 0
ansCount = 2000
ans_list2 = []
while (True) and len(ans_list2)<= ansCount:
    for k1 in [0,-1]:
        if PD2(V(N1,k1))==3:
            ans_list2.append(V(N1,k1))
            print(len(ans_list2))
    N1+= 1

print(len(ans_list2))
ans = ans_list2[2000]
print(ans)

