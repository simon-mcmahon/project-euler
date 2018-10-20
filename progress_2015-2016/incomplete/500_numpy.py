# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np


def sieve7(n):
    """Return an array of the primes below n."""
    prime = np.ones(n // 2, dtype=np.bool)
    sqrt_n = int(n ** .5) + 1
    for p in range(3, sqrt_n, 2):
        if prime[p // 2]:
            prime[p*p // 2::p] = False
    result = 2 * prime.nonzero()[0] + 1
    result[0] = 2
    return result

p=sieve7(10**7)

print "done primes"

okaypow=np.arange(0,21)
okaypow=2**okaypow-1
first=np.array([2,1])
second=np.array([[2,1],[3,1]])
END=500500
for a in range(1,END):
    if a%1000==0:
        print a
    first=second
    nextp=np.where(p==second[-1][0])+np.array([1])
    second=np.append(second,[[p[nextp][0][0],0]],0)
#    second=np.append(second,[[p[np.where(p>second[-1][0])[0][0]],0]],0)
    num=second[:,0]
    po=second[:,1]
    diff=np.array([])
    for x in range(0,len(po)):
        
        diff=np.append(diff,int(okaypow[po[x]+1]-okaypow[po[x]]))
    compar=num**diff
    
    wp=np.where(compar==min(compar))
    po[wp]+=1
    
    if po[-1]==0:
        second=np.delete(second,(-1),axis=0)


