import math as m
pall=[]

for x in range(1,10**6+1):
    if str(x)[::-1]==str(x):
       pall+=[x]


def binary_pall(num):
    st=''
    a=num
    dig=int(m.floor(m.log(a,2)))
    for x in range(dig,-1,-1):
        if 2**x>a:
            st+='0'
            continue
        else:
            a=a-2**x
            st+='1'
    if st[::-1]==st:
        return 1
    return 0

pall=filter(binary_pall,pall)

print sum(pall)

