from __future__ import division
import math as m
import itertools as it

n=10**6 #all primtes less than or equal to this
p=range(2,n+1)

def case_elim(num):
    if ('0' in str(num)) or ('4' in str(num)) or ('6' in str(num)) or ('8' in str(num)):
        return 0
    else:
        return 1
#cross out the numbers with non-prime digits

p=filter(case_elim,p)

cross_out=p[0]

while cross_out<p[-1]:

##    p=p[0:p.index(cross_out**2)]+filter(lambda x: x%cross_out,p[p.index(cross_out**2):])
    p=filter(lambda x: (x%cross_out!=0) or (x==cross_out),p)
    cross_out=p[p.index(cross_out)+1]


print "done primes"

def isprime(num):
    if num==1:
        return 0
    if num==2:
        return 1
    max=int(m.floor(m.sqrt(num)))
    for x in [2]+range(3,(max+1),2):
        if num%x==0:
            return 0
    else:
        return 1


def isprime_l(lis):
    for x in lis:
        if isprime(x)==0:
            return 0
    else:
        return 1

##q=[2,5]+filter(case_elim,p)

def truncate(num):
    #from right
    trun=[]
    s=str(num)
    for a in range(0,len(s)):
        trun+=[int(s[0:len(s)-a])]
    #from left. 1 to avoid double original
    for a in range(1,len(s)):
        trun+=[int(s[a:len(s)])]
    return trun

ans=[]

for x in range(p.index(7)+1,len(p)):
    if isprime_l(truncate(p[x]))==1:
        ans+=[p[x]]




