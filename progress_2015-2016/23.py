from __future__ import division
import math as m
n=10**5 #all primtes less than or equal to this
p=range(2,n+1)

cross_out=2

while cross_out**2<n:

    p=p[0:p.index(cross_out**2)]+filter(lambda x: x%cross_out,p[p.index(cross_out**2):])
    cross_out=p[p.index(cross_out)+1]

def fact_sum(num):
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
    product=1
    for x in range(0,len(fact_power)):
        k=0
        for a in range(0,fact_power[x][1]+1):
            k+=fact_power[x][0]**a
        product=product*k
    return (product-num)

def abundant(num):
    if fact_sum(num)>num:
        return 1
    else:
        return 0

abundant_list=filter(abundant,range(1,28123+1))

print "done list generation"
unable=[]

for x in range(1,28123+1):
    y=0
    success=1
    if x<=12:
        unable+=[x]
        continue
    while abundant_list[y]<=x:
        if x-abundant_list[y] in abundant_list:
            success=0
            break
        y+=1
    if success==1:
        unable+=[x]


###possible sums
##
##sums=[]
##
##unable=range(1,28123+1)
##
##for a in range(0,len(abundant_list)):
##    for b in range(0,len(abundant_list)):
##        sums+=[a+b]
##        if (a+b) in unable:
##            unable.remove(a+b)

##def insums(num):
##    if num in sums:
##        return 0 #false so filter function will give inverse
##    else:
##        return 1
##
##unable=filter(insums,range(1,28123+1))
##print sum(unable)
