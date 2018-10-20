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
    while a!=1:
        if a%p[x]==0:
            while a%p[x]==0:
                fact+=[p[x]]
                a=(a/p[x])
        x+=1
    fact_power=[]
    while len(fact)>0:
        fact_power+=[[fact[0],fact.count(fact[0])]]
        fact=filter(lambda x: x!=fact[0],fact)
    sumq=1
    for x in range(0,len(fact_power)):
        sumq=sumq*(fact_power[x][1]+1)
    return sumq #output number of factors

triangle=1
count=2

while pfact(triangle)<=500:

    triangle=triangle+count
    count+=1

print triangle
