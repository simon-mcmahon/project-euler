import math as m
ans=0

for x in range(1,1001):
    for a in range(1,int(m.floor(x/2)+1)):
        a=a
        b=x-a
        if m.sqrt(a**2+b**2)-int(m.sqrt(a**2+b**2))==0 and int(m.sqrt(a**2+b**2))==1000-(x):
            ans=a*b*m.sqrt(a**2+b**2)
            break
    if ans!=0:
        break


print ans
