
p=[2]

for x in range(3,10**6,2):
    prime=1
    if x%(10000)==0:
        print x
    for a in range(0,len(p)):
        if x%p[a]==0:
            prime=0
            break
    if prime==1:
        p+=[x]
    elif prime==0:
        continue
