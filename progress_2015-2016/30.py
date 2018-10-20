last_num=10

def num5(a):
    b=[int(str(a)[x]) for x in range(0,len(str(a)))]
    b=map(lambda x: x**5,b)
    return sum(b)

ans=0

for x in range(2,10**6):
    if num5(x)==x:
        ans+=x
print ans
        
    
