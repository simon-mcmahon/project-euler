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
    while p[x]<=num:
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

def sumfact(num):
    pfactor=pfact(num)
    ans=1
    for x in range(0,len(pfactor)):
        ans=ans*((pfactor[x][0]**(pfactor[x][1]+1)-1)/(pfactor[x][0]-1))
    return int(ans-num)
    #sum of factors function

#dummy range to sample over
#answer array
amic_pairs=[]
for x in range(2,10**4+1):
    a=x
    b=sumfact(x)
    if (sumfact(b)==a) and (a!=b):
        amic_pairs+=[a,b]

print sum(set(amic_pairs)) #sum of unique valuess
