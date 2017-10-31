#n=0 is a prime and so b is apositive prime from 1,1000
#quadratic is greater than 0, so discriminant shows that -2sqrt(b)<a<2sqrt(b)
#a must be odd for the sequence of primes to be longer than 2.
#modular arithmatic with the nth prime subtract (n-1)st prime

from __future__ import division
import math as m
n=10**5 #all primtes less than or equal to this
p=range(2,n+1)

cross_out=2

while cross_out**2<n:

    p=p[0:p.index(cross_out**2)]+filter(lambda x: x%cross_out,p[p.index(cross_out**2):])
    cross_out=p[p.index(cross_out)+1]

b_l=filter(lambda x: x<1000,p)


def iterate_prim(a,b):
    seq_len=1
    N=0
    while True:
        if N**2+a*N+b<=0:
            return seq_len
        if (N**2+a*N+b<n) and (N**2+a*N+b in p):
            N+=1
            seq_len+=1
        elif (N**2+a*N+b>=n):
            print "n value not high enough"
        else:
            return seq_len
    return seq_len

max_len=1
coeff=[]
for b in range(0,len(b_l)):
    for a in filter(lambda x: x%2!=0,range(int(m.floor(-2*m.sqrt(b_l[b]))+1),int(m.floor(2*m.sqrt(b_l[b]))+1))):
        if iterate_prim(a,b_l[b])>max_len:
            max_len=iterate_prim(a,b_l[b])
            coeff=[a,b_l[b]]

print reduce(lambda x,y: x*y, coeff)

