from __future__ import division
import math as m
n=10**4 #all primtes less than or equal to this
p=range(2,n+1)

cross_out=2

while cross_out**2<n:

    p=p[0:p.index(cross_out**2)]+filter(lambda x: x%cross_out,p[p.index(cross_out**2):])
    cross_out=p[p.index(cross_out)+1]

def gold(num): #eturns [p,k] in a tuple
    x=0
    success=0
    while p[x]<=num-2:
        if num-p[x]<0:
            return 1
        if int(m.sqrt((num-p[x])/2))-m.sqrt((num-p[x])/2)==0:
            success=1
            break
        elif x>=len(p):
            success=0
            break
        x+=1
    if success==1:
        return [p[x],int(m.sqrt((num-p[x])/2))]
    else:
        return [0,0]

print gold(9)
print gold(15)
print gold(21)
print gold(25)
print gold(27)
print gold(33)
#verified function

#make iterated list of non-prime odd numbers
iterate=range(3,n,2)
iterate=filter(lambda x: x not in p,iterate)

for a in range(0,len(iterate)):
    if gold(iterate[a])==[0,0]:
        print iterate[a]
        break
