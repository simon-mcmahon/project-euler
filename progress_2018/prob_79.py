#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 19:41:38 2018

@author: simon
"""

from collections import defaultdict
from itertools import permutations

passcomb = []
with open('p079_keylog.txt', 'r') as f:
    for line in f:
        tup = (int(line[0]),int(line[1]), int(line[2]))
        passcomb.append(tup)

# Really poorly implemented test function
def test(i):
    freq = defaultdict(list)
    for index, char in enumerate(str(i)):
        freq[int(char)].append(index)
#    print(freq)
    for comb in redpasscomb:
        if len(freq[comb[0]])==0:
            return False
        else:
            first = freq[comb[0]][0]
        
        for j in freq[comb[1]]:
            if j>first:
                second = j
                break
        else:
            return False
        for k in freq[comb[2]]:
            if k> second:
                third = k
                break

        else:
            return False
    
    return True

# Each sucessive two letter tuple combination is a 
# When another number aN is picked, subtract all vertices (a1,aN) (a2,aN)... if they exist

edges = set()

for tup in passcomb:
#    dg.add_edge(tup[0], tup[1])
#    dg.add_edge(tup[1], tup[2])
    edges.add((tup[0], tup[1]))
    edges.add((tup[1], tup[2]))

print(len(edges))
print(edges)
present = set()
bidirec = set()
# Get the frequency of in and out
freq_in = defaultdict(int)
freq_out = defaultdict(int)
for edge in edges:
    freq_in[edge[0]] += 1
    freq_out[edge[1]] +=1
    present.add(edge[0])
    present.add(edge[1])
    
    if (edge[1], edge[0]) in edges: # birdirectional case
        add_tup = tuple(sorted(edge))
        bidirec.add(add_tup)

# Sort them

# Sorted frequencies by in and out
freq_inlst = sorted([(key, freq_in[key]) for key in freq_in], key=lambda x: x[1], reverse=True)
freq_outlst = sorted([(key, freq_out[key]) for key in freq_out], key=lambda x: x[1], reverse=True)
print(freq_inlst)
print(freq_outlst)
print(present) 
print(bidirec) # no bidirectional vertices

# BRUTE FORCE IT
numbers = list(present)

for perm in permutations(numbers): # list of all numbers lowest to high
    num = ''
    for x in perm:
        num += str(x)
    num = int(num)
    if test(num)== True:
        break
print(num)
