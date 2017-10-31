from __future__ import division
import math as m
n=32000 #all primtes less than or equal to this
p=range(2,n+1)

cross_out=2

while cross_out**2<n:

    p=p[0:p.index(cross_out**2)]+filter(lambda x: x%cross_out,p[p.index(cross_out**2):])
    cross_out=p[p.index(cross_out)+1]

print "done primes"

def isprime(num): #check if prime
    if num==1:
        return 0 #false
    x=0
    while p[x]<=m.sqrt(num):
        if num%p[x]==0:
            return 0
        else:
            x+=1
    return 1

#other idea iteratively generate

pan_list=[1,12,21]
for n in range(2,9):
    ndiglist=filter(lambda x: len(str(x))==n,pan_list)
    adding=[] #numbers to be added
    for x in range(0,len(ndiglist)):
        adding=[]
        for a in range(0,n+1):
            adding+=[int(str(ndiglist[x])[0:a]+str(n+1)+str(ndiglist[x])[a:len(str(ndiglist[x]))])]
        pan_list+=adding

pan_list.sort()
pan_list.reverse() #highest first

for x in range(0,len(pan_list)): #iterate over list and do prime check
    if isprime(pan_list[x])==1: 
        print pan_list[x]
        break
    
    
