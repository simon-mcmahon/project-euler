#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 10:19:53 2018

@author: simon
"""
import numpy as np

def polySub(coeffs, xval):
    """
    return output of polynomial using a coefficient array [a_N a_N-1 ... a0]
    """
    degree = len(coeffs)-1
    pow_terms = np.power(np.repeat(xval, degree+1), np.arange(degree,-1,-1))
    return np.sum(np.multiply(coeffs, pow_terms).astype(int))

# Checking polySub
def f(x):
    return 2*x**2 + 3*x - 4

for x in range(-10, 10):
    assert f(x) == polySub(np.asarray([2,3,-4]), x)

# Generate the sequence
def seq(xval):
    return polySub([1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1], xval)

uN = [seq(x) for x in range(1,15)]

FITs = []

k = 1
while True and (k<20):
    print(k)
    vstacks = []
    # Generate the OP polynomials
    for i in range(1, k+1):
        vstacks.append(np.power(np.repeat(i, k), np.arange(k-1, -1, -1)))
    
    A = np.vstack(vstacks)
#    print(A)
    b = np.asarray(uN[0:k]).reshape(k,1)
#    print(b)
    coeff = np.linalg.solve(A,b)
    assert np.allclose(np.dot(A, coeff), b) # check eq
    # Check poly values
    coeff = np.round(coeff[:,0]) # convert to a 1D array so polySub works 
    for i in range(1,k+1):
        assert polySub(coeff.astype(int), i) == uN[i-1]
    
    FIT = polySub(coeff.astype(int), k+1)
    if FIT == uN[(k+1)-1]:
        break
    else: 
        FITs.append(FIT)
    
    k += 1
    
print(sum(FITs))
 
