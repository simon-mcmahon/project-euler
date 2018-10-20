from __future__ import division
import math as m
import itertools as it

n=10**6 #all primtes less than or equal to this
p=range(2,n+1)

cross_out=2

while cross_out**2<n:

    p=p[0:p.index(cross_out**2)]+filter(lambda x: x%cross_out,p[p.index(cross_out**2):])
    cross_out=p[p.index(cross_out)+1]


print "done primes"

def perm_list(num):
    l=[]
    for x in range(0,len(str(num))):
        l+=[int(str(num)[x:len(str(num))]+str(num)[0:x])]
    return list(set(l))

##    return list(set(map(int,map(''.join,list(it.permutations(str(num)))))))
#returns list of all of the permutations of num[0] as a list


def rem_if(val,lis):
    try:
        lis.remove(val)
        return (1,lis)
    
    except ValueError:
        return (0,lis)

cylic=[]

def case_elim(num):
    if ('0' in str(num)) or ('2' in str(num)) or ('4' in str(num)) or ('6' in str(num)) or ('8' in str(num)) or ('5' in str(num)):
        return 0
    else:
        return 1
p=[2,5]+filter(case_elim,p)
##print p

while len(p)>=1:
    if len(p)%500==0:
        print len(p)
    success=1
    check=p[0]
    cycle=perm_list(check)
    for x in range(0,len(cycle)):
        temp=rem_if(cycle[x],p)
        p=temp[1]
        if temp[0]==0:
            success=0
    if success==1:
        cylic+=[cycle[x] for x in range(0,len(cycle))]

print len(cylic)
    
