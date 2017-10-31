#two digit n & m . fraction is n/m
#mod 10 divisibility implies m*(n%10)==n*(m%10)

#populate 2 dig list with no trivial 10's
import itertools as it
mn=list(it.combinations(range(10,100),2))

def commondigit(ee):
    common=set()
    for x in range(0,len(str(ee[0]))):
        if str(ee[1]).find(str(ee[0])[x])!=-1:
            common.add(int(str(ee[0])[x]))
    return list(common)

def cancelcheck(ee):
    common=commondigit(ee)
    if 0 in common:
        return 0
    if len(common)==0:
        return 0
    for x in range(0,len(common)):
        N=ee[0]
        M=ee[1]
        n=int(str(ee[0]).replace(str(common[x]),'',1))
        m=int(str(ee[1]).replace(str(common[x]),'',1))
        if N*m==M*n:
            return 1
    else:
        return 0

mn=filter(cancelcheck,mn)

print mn

from fractions import gcd

for x in range(0,len(mn)):
    mn[x]=list(mn[x])
    g=gcd(mn[x][0],mn[x][1])
    mn[x][0]=mn[x][0]/g
    mn[x][1]=mn[x][1]/g

den=1
numer=1
for x in range(0,len(mn)):
    numer=numer*mn[x][0]
    den=den*mn[x][1]

print mn

g=gcd(numer,den)
numer=numer/g
den=den/g
print str(numer) + ' / ' + str(den)

##n is top
##for x in range(0,len(mn)):
##    n=min(mn[x])
##    m=max(mn[x])
##    if m*(n%10)==n*(m%10):
##        dig_can=[[n,m]]

