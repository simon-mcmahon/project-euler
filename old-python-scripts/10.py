from __future__ import division
import math as m
n=2*10**6 #all primtes less than or equal to this
p=range(2,n+1)

cross_out=2

while cross_out**2<n:

    p=p[0:p.index(cross_out**2)]+filter(lambda x: x%cross_out,p[p.index(cross_out**2):])
    cross_out=p[p.index(cross_out)+1]

print "done primes"

print sum(p)
