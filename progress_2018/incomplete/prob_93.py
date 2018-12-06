#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 11:24:24 2018

@author: simon
"""

from itertools import permutations, product, combinations
from fractions import Fraction

def operate(prev, nxt, op):
    assert type(prev)== Fraction
    assert type(nxt) == Fraction
    # 1 = plus, 2 = minus,  3 = times, 4 = divide
    if op==1:
        return prev + nxt
    elif op==2:
        return prev-nxt
    elif op==3:
        return prev*nxt
    elif op==4:
        return prev/nxt

def getresult(numord, opord):
    numord = list(map(Fraction, numord))
    for cnt, op in enumerate(opord):
        if cnt==0:
            out = operate(numord[cnt], numord[cnt+1], op)
        else:
            out = operate(out, numord[cnt+1], op)
    if out.denominator==1 and out.numerator > 0: # Only output the useful integer results
        return out.numerator
    else:
        return 'not an int'

assert getresult((3,1,2,4), (1,4,3))==8

def allresults(nums):
    outputs = set()
    for numorderings in permutations(nums):
        for oporderings in product(range(1,5), repeat=3):
            result = getresult(numorderings, oporderings)
            if type(result) != str:
                outputs.add(result)
    sortuniques = sorted(list(outputs))
    return sortuniques

maxN = 10
maxConsec=0
anstup = [0,0,0,0]
#[[1,2,3,4], [28, 2,3,4], [30, 2,3,6], [2,3,5,7], [1,2,3,5], [2,3,4,5], [1,2,4,7]]:

for nums in combinations(range(1,maxN+1), 4):
    sortuniques = allresults(nums)
    x = 1
    while True:
        if sortuniques[x-1] == x:
            x+=1
            continue
        else:
            break
    if (x-1) >= maxConsec:
        anstup = nums
        maxConsec = x-1
#    print(sortuniques)
#    print(x-1)
            
print(maxConsec)
print(anstup)
