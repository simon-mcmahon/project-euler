import math as m

def numfact(a):
    b=[int(str(a)[x]) for x in range(0,len(str(a)))]
    b=map(lambda x: m.factorial(x),b)
    return sum(b)
ans=0

for x in range(10,10**6):
    if numfact(x)==x:
        ans+=x
        print ans
    if x%(100000)==0:
        print x
        
