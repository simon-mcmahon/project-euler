from __future__ import division
import math as m
n=10**5 #all primtes less than or equal to this
p=range(2,n+1)

cross_out=2

while cross_out**2<n:

    p=p[0:p.index(cross_out**2)]+filter(lambda x: x%cross_out,p[p.index(cross_out**2):])
    cross_out=p[p.index(cross_out)+1]

def pfact(num):
    a = num
    x=0
    fact=[] #list of prime factors
    while p[x]<=a:
        if a%p[x]==0:
            while a%p[x]==0:
                fact+=[p[x]]
                a=(a/p[x])
        x+=1
    fact_power=[]
    while len(fact)>0:
        fact_power+=[[fact[0],fact.count(fact[0])]]
        fact=filter(lambda x: x!=fact[0],fact)
    return fact_power #output an array of primes and their power

print pfact(600851475143)
