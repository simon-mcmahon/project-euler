import math as m
count=0
for x in range(0,len(str(m.factorial(100)))):
    count+=int(str(m.factorial(100))[x])
print count
