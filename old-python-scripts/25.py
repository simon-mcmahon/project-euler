fibb=[1,1]
count=0
import math as m
while True: #returns the (n+2)nd fibbonachi number
    if m.log(fibb[1],10)+1<1000:
        placeholder=fibb[1]
        fibb[1]=fibb[0]+fibb[1]
        fibb[0]=placeholder
        count+=1
    else:
        break
print count+2
