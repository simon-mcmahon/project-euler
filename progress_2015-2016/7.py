import math as m
p=range(10**6)
for x in ([2]+(map(lambda a: a+1,range(2,10**6,2)))):
    p=list(filter(lambda y: not((y%x==0) & (y!=x)),p))

print p[10001] #includes 1 as 0
