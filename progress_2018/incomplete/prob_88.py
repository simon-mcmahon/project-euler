#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 21:03:18 2018

@author: simon
"""

#The fact that the product is larger is a huge contraint
# for the n number case, the product must be less than 9*n
# we can find the maximal k length products which are below the threshold and contrain 
# cases that way
# e.g. n = 6. (k=2) (1 terms = 4) so product - 4 = sum OR product - sum = 4
# Conjecture
# The difference between product and sum an increasing function.
# a*b - (a+b)
# a*(b+1) - (a+b+1) = a*b - (a+b) + (a-1) so if a>=2 this is true.
# exit after the product sum difference becomes larger than 4.
#prod <54. (2,2)..(2,27) (3,3)..(3,18) (4,4)..(4,14) (5,5)..(5,10) ... (7,7)
# order is not important. use comginations

from itertools import combinations_with_replacement

def prod(lst):
    out = 1
    for x in lst:
        out *= x
    return out

select = range(2,10)

iters =  sorted(list(combinations_with_replacement(select, 2)), key=lambda x: x[0]+x[1])

diff = 4
scndnum = 2
firstnum = 2
testdiff = 0
maxsum = 9*6
sol_set = []

digs = [2,2]

while digs[-2]**2 <= maxsum:

    while (prod(digs) - sum(digs) <= diff) and (prod(digs) <= maxsum):

        if prod(digs) - sum(digs) == diff:
            sol_set.append(digs.copy())
            digs[-1] += 1 
            print(digs)
        else:
            digs[-1] += 1
            print(digs)
    
    
    digs[-2] += 1
    digs[-1] = digs[-2]
    print(digs)


#while (firstnum*scndnum - (firstnum+scndnum)) <= diff:
#    if (firstnum*scndnum - (firstnum+scndnum)) == diff:
#        sol_set.append(())
#        
#        
#for x in iters:
#    print('{} prod sum diff {}'.format(x, x[0]*x[1]-(x[0]+x[1])))
