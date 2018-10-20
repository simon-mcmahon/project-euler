import math as m
triples=[]
for a in range(1,1000):
    for b in range(1,1000):
        if int(m.sqrt(a**2+b**2))-m.sqrt(a**2+b**2)==0:
            triples+=[[a,b,int(m.sqrt(a**2+b**2))]]

#exactly 2 of each solution produced except for the double ups. No doubles exist as integer triads.

sum_triples=[]
for x in range(0,len(triples)):
    sum_triples+=[sum(triples[x])]

max_sols=0
p=0

for x in range(0,1001):
    if sum_triples.count(x)>max_sols:
        max_sols=sum_triples.count(x)
        p=x

print p
