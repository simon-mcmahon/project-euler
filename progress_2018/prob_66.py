#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 16:27:19 2018

@author: simon
"""
from math import floor, sqrt, gcd
# Generate the array of D values to test
maxD = 1000
Ds = list(range(1,maxD + 1))
squares = []
n = 1
while n**2 <= maxD:
    squares.append(n**2)
    n += 1

for square in squares:
    Ds.remove(square)

# Manual value for testing

sols = []

#Ds = [2,3,5,6,7,13,14,15]
#Ds = [13]
for D in Ds:
    # Finding the cocntinued square root
    # https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Continued_fraction_expansion
    m = [0]
    d = [1]
    a = [floor(sqrt(D))]
    
    seen_triple = set()
    seen_triple.add((m[0], d[0], a[0]))
    
    while True:
    
        m += [d[-1]*a[-1] - m[-1]]
        d += [(D - m[-1]**2)//(d[-1])]
        a += [floor((a[0] + m[-1])//(d[-1]) )]
        
        if (m[-1], d[-1], a[-1]) not in seen_triple:
            seen_triple.add((m[-1], d[-1], a[-1]))
        else:
            break
    
    # Write one too many iterations. too lazy to fix now
    m = m[:-1]
    d = d[:-1]
    a = a[:-1] # first entry a0, rest the periodic terms
    rec_a = a[1:] #reccuring part of a
        
    # Make the code for finding the fundamental solution
    # Using http://mathworld.wolfram.com/PellEquation.html
    p = [a[0]]
    q = [1]
    if len(a) > 1:
        p += [a[0]*a[1]+1]
        q += [a[1]]
    
    
    # Test p1,q1 and p2,q2 (p=x, q=y)
    for j in [0,1]:
        if p[j]**2 - D*q[j]**2 == 1:
            sol = (p[j], q[j])
    
    # Find the value of r
    r = a.index(2*a[0])-1
    if r%2!=0: # Odd case
        top = r
    else: # even case
        top = 2*r + 1
        
    n = 0
    while True:
        # Note (n-1)%(r+1) used to make the reccursive part of a loop over and over
        if (n!=0) and (n!=1):
            p += [rec_a[(n-1)%(r+1)]*p[n-1] + p[n-2]]
            q += [rec_a[(n-1)%(r+1)]*q[n-1] + q[n-2]]
        if n>=top:
            break
        n+=1
    
    # Check solution (reducing the fraction first)
    x = p[top]//gcd(p[top], q[top])
    y = q[top]//gcd(p[top], q[top])
    if x**2 - D*y**2 == 1:
        sols += [(x, y)]
    else:
        raise ValueError('djhdjfhdf')
    

# Find value of D with max x value
xs = [sol[0] for sol in sols]
max_index = xs.index(max(xs))
ans = Ds[max_index]
print(ans)

    #while 
    
    # pn = an * pn-1 + pn-2
    # qn = an * qn-1 + qn-2
