#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 18:54:25 2018

@author: simon
"""
import numpy as np
from sympy.ntheory.primetest import isprime

np_prime1 = np.vectorize(isprime)

def allQuad(n):
    outlst = []
    for tup in quad_tups:
        outlst.append(int(tup[0]*n**2 + tup[1]*n + tup[2]))
    return np.asarray(outlst)

print('------- Finished iterating in primes to memory -------------------')

quad_tups = []
A = np.asarray([[1,1],[4,2]])
# Find the quadratics in question
for res in [(3,13), (7,21), (5,17), (9,25)]:
    b = np.asarray([[res[0]-1],[res[1]-1]], dtype=np.int)
    x = np.dot(np.linalg.inv(A), b)
    tup = (int(x[0]), int(x[1]), 1)
    quad_tups.append(tup)

diags = np.asarray([1])

side = 3
pcnt = 0
while True:
    if (side-3)%100==0:
        print(side)
    maxN = np.floor(side/2)
    new_nums = allQuad(maxN)
    pcnt += np.sum(np_prime1(new_nums))
    diags = np.append(diags, allQuad(maxN))
#    print('{}: {}'.format(side,diags))
    ratio = pcnt/len(diags)
#    print('{} / {} = {}'.format(pcnt, len(diags), ratio))
    if (ratio <= 0.1): #or (side > 20):
        break
#    elif side**2 > maxp:
#        raise ValueError('Too Few primes')
    else:
#        break
        side += 2

print(side)