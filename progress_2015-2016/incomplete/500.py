from __future__ import division
import math as m
n=10**4 #all primtes less than or equal to this
p=range(2,n+1)

cross_out=2

while cross_out**2<n:

    p=p[0:p.index(cross_out**2)]+filter(lambda x: x%cross_out,p[p.index(cross_out**2):])
    cross_out=p[p.index(cross_out)+1]

print "done primes"
##def pfact(num):
##    a = num
##    x=0
##    fact=[] #list of prime factors
##    while p[x]<=num:
##        if a%p[x]==0:
##            while a%p[x]==0:
##                fact+=[p[x]]
##                a=(a/p[x])
##        x+=1
##    fact_power=[]
##    while len(fact)>0:
##        fact_power+=[[fact[0],fact.count(fact[0])]]
##        fact=filter(lambda x: x!=fact[0],fact)
##    product=1
##    for x in range(0,len(fact_power)):
##        product=product*(fact_power[x][1]+1)
##    return product,fact_power #output an array of primes and their power
##
##x=1
##while True:
##    a=pfact(x)
##    if a[0]==64:
##        print a
##        break
##
##    x+=1

#    TESTING
#iterative process determined by adding the lowest number needed to make up the next power of 1 less than a power of 2

compar_list=[]
fact=[]
END=1000-1
import time
start=time.time()
##low_fact=range(1,END+2)
low_fact=[]
low_fact+=[[1,[[2,1]]]]
low_fact+=[[2,[[2,1],[3,1]]]]
for a in range(1,END): #FINISHES AT 2^(END+1)
    if a%10000==0:
        print a
    #set fact as the ptime factor
    fact=[]
##    print fact
    fact=low_fact[1][1]
    #add in the next prime to the zeroth power
    fact=fact+[[p[p.index(fact[-1][0])+1],0]]

    #list comparing the new numbers to add
    compar_list=[]

    for x in range(0,len(fact)):
        num=fact[x][0]
        po=(2**(int(m.log((1+fact[x][1]),2))+1)-1)-fact[x][1]
        compar_list+=[num**po]
    #now that list is done find index of min value on list
    winning_prime=compar_list.index(min(compar_list))
##    print fact
    fact[winning_prime][1]=(2**(int(m.log((1+fact[winning_prime][1]),2))+1)-1)
##    print fact
    if fact[-1][1]==0:
        fact=fact[0:len(fact)-1]
##    print fact
    appen=low_fact[1][0]+1,fact
    low_fact[0]=low_fact[1]
    low_fact[1]=appen
##    print low_fact

end=time.time()
print end-start

##END=10-1
##low_fact=[1]
##low_fact[0]=[[2,1]]
##low_fact+=[[[2,1],[3,1]]]
##for a in range(1,END): #FINISHES AT 2^(END+1)
##    if a%10000==0:
##        print a
##    #set fact as the ptime factor
##    fact=[]
##    print fact
##    fact=[low_fact[a]]
##    #add in the next prime to the zeroth power
##    fact=fact+[[p[p.index(fact[-1][0])+1],0]]
##
##    #list comparing the new numbers to add
##    compar_list=[]
##
##    for x in range(0,len(fact)):
##        num=fact[x][0]
##        po=(2**(int(m.log((1+fact[x][1]),2))+1)-1)-fact[x][1]
##        compar_list+=[num**po]
##    #now that list is done find index of min value on list
##    winning_prime=''
##    winning_prime=compar_list.index(min(compar_list))
##    print fact
##    fact[winning_prime][1]=(2**(int(m.log((1+fact[winning_prime][1]),2))+1)-1)
##    print fact
##    if fact[-1][1]==0:
##        fact=fact[0:len(fact)-1]
##    print fact
##    low_fact.append([fact])


